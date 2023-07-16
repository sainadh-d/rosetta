# Boyer-Moore string search

## Task Link
[Rosetta Code - Boyer-Moore string search](https://rosettacode.org/wiki/Boyer-Moore_string_search)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * An implementation of the Boyer-Moore string search algorithm. 
 * It finds all occurrences of a pattern in a text, performing a case-insensitive search on ASCII characters.
 * 
 * For all full description of the algorithm visit:
 * https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
 */
public final class BoyerMooreStringSearch {
	
	public static void main(String[] aArgs) {		
		List<String> texts = List.of(
			"GCTAGCTCTACGAGTCTA",
		    "GGCTATAATGCGTA",
		    "there would have been a time for such a word",
		    "needle need noodle needle",
		    "DKnuthusesandshowsanimaginarycomputertheMIXanditsassociatedmachinecodeandassemblylanguagestoillustrate",
		    "Farms grew an acre of alfalfa on the dairy's behalf, with bales of that alfalfa exchanged for milk.");
		         
		List<String> patterns = List.of( "TCTA", "TAATAAA", "word", "needle", "put", "and", "alfalfa" );
		
		for ( int i = 0; i < texts.size(); i++ ) {
			System.out.println("text" + ( i + 1 ) + " = " + texts.get(i));
		}
		System.out.println();
		
		for ( int i = 0; i < patterns.size(); i++ ) {
			final int j = ( i < 5 ) ? i : i - 1;		
			System.out.println("Found \"" + patterns.get(i) + "\" in 'text" + ( j + 1 ) + "' at indexes "
				+ stringSearch(texts.get(j), patterns.get(i)));
		}
    }
	
	/**
	 * Return a list of indexes at which the given pattern matches the given text.
	 */	
	private static List<Integer> stringSearch(String aText, String aPattern) {	    
	    if ( aPattern.isEmpty() || aText.isEmpty() || aText.length() < aPattern.length() ) {
	        return Collections.emptyList();
	    }

	    List<Integer> matches = new ArrayList<Integer>();

	    // Preprocessing
	    List<List<Integer>> R = badCharacterTable(aPattern);
	    int[] L = goodSuffixTable(aPattern);
	    int[] F = fullShiftTable(aPattern);

	    int k = aPattern.length() - 1; // Represents the alignment of the end of aPattern relative to aText
	    int previousK = -1; // Represents the above alignment in the previous phase
	    while ( k < aText.length() ) {
	        int i = aPattern.length() - 1; // Index of the character to compare in aPattern
	        int h = k; // Index of the character to compare in aText
	        while ( i >= 0 && h > previousK && aPattern.charAt(i) == aText.charAt(h) ) {
	            i -= 1;
	            h -= 1;
	        }
	        if ( i == -1 || h == previousK ) { // Match has been found
	            matches.add(k - aPattern.length() + 1);
	            k += ( aPattern.length() > 1 ) ? aPattern.length() - F[1] : 1;
	        } else { // No match, shift by the maximum of the bad character and good suffix rules
	        	int suffixShift;
	            int charShift = i - R.get(alphabetIndex(aText.charAt(h))).get(i);
	            if ( i + 1 == aPattern.length() ) { // Mismatch occurred on the first character
	                suffixShift = 1;
	            } else if ( L[i + 1] == -1 ) { // Matched suffix does not appear anywhere in aPattern
	                suffixShift = aPattern.length() - F[i + 1];
	            } else { // Matched suffix appears in aPattern
	                suffixShift = aPattern.length() - 1 - L[i + 1];
	            }
	            int shift = Math.max(charShift, suffixShift);
	            if ( shift >= i + 1 ) { // Galil's rule
	            	previousK = k;
	            }
	            k += shift;
	        }
	    }
	    return matches;
	}
	
    /**
     * Create the shift table, F, for the given text, which is an array such that
     * F[i] is the length of the longest suffix of, aText.substring(i), which is also a prefix of the given text.
     * 
     * Use case: If a mismatch occurs at character index i - 1 in the pattern,
     * the magnitude of the shift of the pattern, P, relative to the text is: P.length() - F[i].
     */ 
	private static int[] fullShiftTable(String aText) {	    
	    int[] F = new int[aText.length()];
	    int[] Z = fundamentalPreprocess(aText);
	    int longest = 0;
	    Collections.reverse(Arrays.asList(Z));
	    for ( int i = 0; i < Z.length; i++ ) {
	    	int zv = Z[i];	
	    	if ( zv == i + 1 ) {
	    		longest = Math.max(zv, longest);
	    	}
	        F[F.length - i - 1] = longest;
	    }
	    return F;
	}
	
	/**
     * Create the good suffix table, L, for the given text, which is an array such that
     * L[i] = k, is the largest index in the given text, S,
     * such that S.substring(i) matches a suffix of S.substring(0, k).
     * 
     * Use case: If a mismatch of characters occurs at index i - 1 in the pattern, P,
     * then a shift of magnitude, P.length() - L[i], is such that no instances of the pattern in the text are omitted. 
     * Furthermore, a suffix of P.substring(0, L[i]) matches the same substring of the text that was matched by a
     * suffix in the pattern on the previous matching attempt.
     * In the case that L[i] = -1, the full shift table must be used.
     */
	private static int[] goodSuffixTable(String aText) {
		int[] L = IntStream.generate( () -> -1 ).limit(aText.length()).toArray();
	    String reversed = new StringBuilder(aText).reverse().toString();
	    int[] N = fundamentalPreprocess(reversed);
	    Collections.reverse(Arrays.asList(N));
	    for ( int j = 0; j < aText.length() - 1; j++ ) {
	        int i = aText.length() - N[j];
	        if ( i != aText.length() ) {
	            L[i] = j;
	        }
	    }
	    return L;
	}
	
	/**
     * Create the bad character table, R, for the given text,
     * which is a list indexed by the ASCII value of a character, C, in the given text.
     * 
     * Use case: The entry at index i of R is a list of size: 1 + length of the given text.
     * This inner list gives at each index j the next position at which character C will be found
     * while traversing the given text from right to left starting from index j.
     */
	private static List<List<Integer>> badCharacterTable(String aText) {	    
	    if ( aText.isEmpty() ) {
	        return Collections.emptyList();
	    }
	    
	    List<List<Integer>> R = IntStream.range(0, ALPHABET_SIZE).boxed()
	    	.map( i -> new ArrayList<Integer>(Collections.nCopies(1,-1)) ).collect(Collectors.toList());
	    List<Integer> alpha = new ArrayList<Integer>(Collections.nCopies(ALPHABET_SIZE, -1));
	    
	    for ( int i = 0; i < aText.length(); i++ ) {
	        alpha.set(alphabetIndex(aText.charAt(i)), i);
	        for ( int j = 0; j < alpha.size(); j++ ) {
	            R.get(j).add(alpha.get(j));
	        }
	    }
	    return R;
	}
	
	/**
	 * Create the fundamental preprocess, Z, of the given text, which is an array such that
     * Z[i] is the length of the substring of the given text beginning at index i which is also a prefix of the text.
     */
	private static int[] fundamentalPreprocess(String aText) {	    
	    if ( aText.isEmpty() ) {
	        return new int[0];
	    }
	    if ( aText.length() == 1 ) {
	        return new int[] { 1 };
	    }
	    
	    int[] Z = new int[aText.length()];	
	    Z[0] = aText.length();
	    Z[1] = matchLength(aText, 0, 1);
	    for ( int i = 2; i <= Z[1]; i++ ) {  
	        Z[i] = Z[1] - i + 1;
	    }
	    
	    // Define the left and right limits of the z-box
	    int left = 0;
	    int right = 0;
	    for ( int i = 2 + Z[1]; i < aText.length(); i++ ) {
	        if ( i <= right ) { // i falls within existing z-box
	            final int k = i - left;
	            final int b = Z[k];
	            final int a = right - i + 1;
	            if ( b < a ) { // b ends within existing z-box
	                Z[i] = b;
	            } else { // b ends at or after the end of the z-box,
	            		 // an explicit match to the right of the z-box is required
	                Z[i] = a + matchLength(aText, a, right + 1);
	                left = i;
	                right = i + Z[i] - 1;
	            }
	        } else { // i does not fall within existing z-box
	            Z[i] = matchLength(aText, 0, i);
	            if ( Z[i] > 0 ) {
	                left = i;
	                right = i + Z[i] - 1;
	            }
	        }
	    }	    
	    return Z;
	}
	
	/**
	 * Return the length of the match of the two substrings of the given text beginning at each of the given indexes.
	 */ 
	private static int matchLength(String aText, int aIndexOne, int aIndexTwo) {	    
	    if ( aIndexOne == aIndexTwo ) {
	        return aText.length() - aIndexOne;
	    }
	    
	    int matchCount = 0;
	    while ( aIndexOne < aText.length() && aIndexTwo < aText.length() 
	    	    && aText.charAt(aIndexOne) == aText.charAt(aIndexTwo) ) {
	        matchCount += 1;
	        aIndexOne += 1;
	        aIndexTwo += 1;
	    }
	    return matchCount;
	}	
	
	/**
	 * Return the ASCII index of the given character, if it is such, otherwise throw an illegal argument exception.
	 */ 
	private static int alphabetIndex(char aChar) {		
		final int result = (int) aChar;
		if ( result >= ALPHABET_SIZE ) {
			throw new IllegalArgumentException("Not an ASCII character:" + aChar);
		}
		return result;
	} 	

	/* The range of ASCII characters is 0..255, both inclusive. */
	private static final int ALPHABET_SIZE = 256;
	
}

```

## Python Code
### python_code_1.txt
```python
"""
This version uses ASCII for case-sensitive matching. For Unicode you may want to match in UTF-8
bytes instead of creating a 0x10FFFF-sized table.
"""

from typing import List

ALPHABET_SIZE = 256

def alphabet_index(c: str) -> int:
    """Return the index of the given ASCII character. """
    val = ord(c)
    assert 0 <= val < ALPHABET_SIZE
    return val

def match_length(S: str, idx1: int, idx2: int) -> int:
    """Return the length of the match of the substrings of S beginning at idx1 and idx2."""
    if idx1 == idx2:
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

def fundamental_preprocess(S: str) -> List[int]:
    """Return Z, the Fundamental Preprocessing of S.

    Z[i] is the length of the substring beginning at i which is also a prefix of S.
    This pre-processing is done in O(n) time, where n is the length of S.
    """
    if len(S) == 0:  # Handles case of empty string
        return []
    if len(S) == 1:  # Handles case of single-character string
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1 + z[1]):  # Optimization from exercise 1-5
        z[i] = z[1] - i + 1
    # Defines lower and upper limits of z-box
    l = 0
    r = 0
    for i in range(2 + z[1], len(S)):
        if i <= r:  # i falls within existing z-box
            k = i - l
            b = z[k]
            a = r - i + 1
            if b < a:  # b ends within existing z-box
                z[i] = b
            else:  # b ends at or after the end of the z-box, we need to do an explicit match to the right of the z-box
                z[i] = a + match_length(S, a, r + 1)
                l = i
                r = i + z[i] - 1
        else:  # i does not reside within existing z-box
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i + z[i] - 1
    return z

def bad_character_table(S: str) -> List[List[int]]:
    """
    Generates R for S, which is an array indexed by the position of some character c in the
    ASCII table. At that index in R is an array of length |S|+1, specifying for each
    index i in S (plus the index after S) the next location of character c encountered when
    traversing S from right to left starting at i. This is used for a constant-time lookup
    for the bad character rule in the Boyer-Moore string search algorithm, although it has
    a much larger size than non-constant-time solutions.
    """
    if len(S) == 0:
        return [[] for a in range(ALPHABET_SIZE)]
    R = [[-1] for a in range(ALPHABET_SIZE)]
    alpha = [-1 for a in range(ALPHABET_SIZE)]
    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    return R

def good_suffix_table(S: str) -> List[int]:
    """
    Generates L for S, an array used in the implementation of the strong good suffix rule.
    L[i] = k, the largest position in S such that S[i:] (the suffix of S starting at i) matches
    a suffix of S[:k] (a substring in S ending at k). Used in Boyer-Moore, L gives an amount to
    shift P relative to T such that no instances of P in T are skipped and a suffix of P[:L[i]]
    matches the substring of T matched by a suffix of P in the previous match attempt.
    Specifically, if the mismatch took place at position i-1 in P, the shift magnitude is given
    by the equation len(P) - L[i]. In the case that L[i] = -1, the full shift table is used.
    Since only proper suffixes matter, L[0] = -1.
    """
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1])  # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S) - 1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

def full_shift_table(S: str) -> List[int]:
    """
    Generates F for S, an array used in a special case of the good suffix rule in the Boyer-Moore
    string search algorithm. F[i] is the length of the longest suffix of S[i:] that is also a
    prefix of S. In the cases it is used, the shift magnitude of the pattern P relative to the
    text T is len(P) - F[i] for a mismatch occurring at i-1.
    """
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i + 1 else longest
        F[-i - 1] = longest
    return F

def string_search(P, T) -> List[int]:
    """
    Implementation of the Boyer-Moore string search algorithm. This finds all occurrences of P
    in T, and incorporates numerous ways of pre-processing the pattern to determine the optimal
    amount to shift the string and skip comparisons. In practice it runs in O(m) (and even
    sublinear) time, where m is the length of T. This implementation performs a case-sensitive
    search on ASCII characters. P must be ASCII as well.
    """
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      # Represents alignment of end of P relative to T
    previous_k = -1     # Represents alignment in previous phase (Galil's rule)
    while k < len(T):
        i = len(P) - 1  # Character to compare in P
        h = k           # Character to compare in T
        while i >= 0 and h > previous_k and P[i] == T[h]:  # Matches starting from end of P
            i -= 1
            h -= 1
        if i == -1 or h == previous_k:  # Match has been found (Galil's rule)
            matches.append(k - len(P) + 1)
            k += len(P) - F[1] if len(P) > 1 else 1
        else:  # No match, shift by max of bad character and good suffix rules
            char_shift = i - R[alphabet_index(T[h])][i]
            if i + 1 == len(P):  # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i + 1] == -1:  # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i + 1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - 1 - L[i + 1]
            shift = max(char_shift, suffix_shift)
            previous_k = k if shift >= i + 1 else previous_k  # Galil's rule
            k += shift
    return matches

TEXT1 = 'InhisbookseriesTheArtofComputerProgrammingpublishedbyAddisonWesleyDKnuthusesanimaginarycomputertheMIXanditsassociatedmachinecodeandassemblylanguagestoillustratetheconceptsandalgorithmsastheyarepresented'
TEXT2 = "Nearby farms grew a half acre of alfalfa on the dairy's behalf, with bales of all that alfalfa exchanged for milk."
PAT1, PAT2, PAT3 = 'put', 'and', 'alfalfa'

print("Found", PAT1, "at:", string_search(PAT1, TEXT1))
print("Found", PAT2, "at:", string_search(PAT2, TEXT1))
print("Found", PAT3, "at:", string_search(PAT3, TEXT2))

```

