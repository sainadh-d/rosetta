# Bioinformatics/Global alignment

## Task Link
[Rosetta Code - Bioinformatics/Global alignment](https://rosettacode.org/wiki/Bioinformatics/Global_alignment)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public final class BioinformaticsGlobalAlignment {

	public static void main(String[] aArgs) {
		List<List<String>> testSequences = Arrays.asList(
			Arrays.asList( "TA", "AAG", "TA", "GAA", "TA" ),
			Arrays.asList( "CATTAGGG", "ATTAG", "GGG", "TA" ),
			Arrays.asList( "AAGAUGGA", "GGAGCGCAUC", "AUCGCAAUAAGGA" ),
			Arrays.asList( "ATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTAT",
				"GGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGT",
				"CTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA",
				"TGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
				"AACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT",
				"GCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTC",
				"CGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATTCTGCTTATAACACTATGTTCT",
				"TGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
				"CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATGCTCGTGC",
				"GATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATT",
				"TTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
				"CTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA",
				"TCTCTTAAACTCCTGCTAAATGCTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGA" )
		);
		
		for ( List<String> test : testSequences ) {
			for ( String superstring : shortestCommonSuperstrings(test) ) {
				printReport(superstring);
			}
		}
	}
	
	// Return a set containing all of the shortest common superstrings of the given list of strings. 
	private static Set<String> shortestCommonSuperstrings(List<String> aList) {
		List<String> deduplicated = deduplicate(aList);
		Set<String> shortest = new HashSet<String>();
		shortest.add(String.join("", deduplicated));
		int shortestLength = aList.stream().mapToInt( s -> s.length() ).sum();
			  
		for ( List<String> permutation : permutations(deduplicated) ) {
			String candidate = permutation.stream().reduce("", (a, b) -> concatenate(a, b) );
	        if ( candidate.length() < shortestLength ) {
	            shortest.clear();
	            shortest.add(candidate);
	            shortestLength = candidate.length();
	        } else if ( candidate.length() == shortestLength ) {
	            shortest.add(candidate);
	        }
		}
		return shortest;		
	}

	// Remove duplicate strings and strings which are substrings of other strings in the given list.
	private static List<String> deduplicate(List<String> aList) {
		List<String> unique = aList.stream().distinct().collect(Collectors.toList());
		List<String> result = new ArrayList<String>(unique);
		List<String> markedForRemoval = new ArrayList<String>();
		for ( String testWord : result ) {
			for ( String word : unique ) {
				if ( ! word.equals(testWord) && word.contains(testWord) ) {
					markedForRemoval.add(testWord);
				}
			}
		}
		result.removeAll(markedForRemoval);
		return result;
	}	
	
	// Return aBefore concatenated with aAfter, removing the longest suffix of aBefore that matches a prefix of aAfter.
	private static String concatenate(String aBefore, String aAfter) {	
	    for ( int i = 0; i < aBefore.length(); i++ ) {
	        if ( aAfter.startsWith(aBefore.substring(i, aBefore.length())) ) {
	            return aBefore.substring(0, i) + aAfter;
	        }
	    }
	    return aBefore + aAfter;
	}
	
	// Return all permutations of the given list of strings.
	private static List<List<String>> permutations(List<String> aList) {
		int[] indexes = new int[aList.size()];
	    List<List<String>> result = new ArrayList<List<String>>();
	    result.add( new ArrayList<String>(aList) );
	    int i = 0;
		while ( i < aList.size() ) {
		    if ( indexes[i] < i ) {
		    	final int j = ( i % 2 == 0 ) ? 0 : indexes[i];
		    	String temp = aList.get(j);
		    	aList.set(j, aList.get(i));
		    	aList.set(i, temp);
		        result.add( new ArrayList<String>(aList) );
		        indexes[i]++;
		        i = 0;
		    } else {
		        indexes[i] = 0;
		        i += 1;
		    }
		}	    
		return result;
	}
	
	// Print a report of the given string to the standard output device.
	private static void printReport(String aText) {
		char[] nucleotides = new char[] {'A', 'C', 'G', 'T' };
		Map<Character, Integer> bases = new HashMap<Character, Integer>();
		for ( char base : nucleotides ) {
			bases.put(base, 0);
		}
		
		for ( char ch : aText.toCharArray() ) {
			bases.merge(ch, 1, Integer::sum);
		}
		final int total = bases.values().stream().reduce(0, Integer::sum);
		
		System.out.print("Nucleotide counts for: " + ( ( aText.length() > 50 ) ? System.lineSeparator() : "") );
		System.out.println(aText);
		System.out.print(String.format("%s%d%s%d%s%d%s%d",
			"Bases: A: ", bases.get('A'), ", C: ", bases.get('C'), ", G: ", bases.get('G'), ", T: ", bases.get('T')));
		System.out.println(", total: " + total + System.lineSeparator());
	}

}

```

## Python Code
### python_code_1.txt
```python
import os

from collections import Counter
from functools import reduce
from itertools import permutations

BASES = ("A", "C", "G", "T")


def deduplicate(sequences):
    """Return the set of sequences with those that are a substring
    of others removed too."""
    sequences = set(sequences)
    duplicates = set()

    for s, t in permutations(sequences, 2):
        if s != t and s in t:
            duplicates.add(s)

    return sequences - duplicates


def smash(s, t):
    """Return `s` concatenated with `t`. The longest suffix of `s`
    that matches a prefix of `t` will be removed."""
    for i in range(len(s)):
        if t.startswith(s[i:]):
            return s[:i] + t
    return s + t


def shortest_superstring(sequences):
    """Return the shortest superstring covering all sequences. If
    there are multiple shortest superstrings, an arbitrary
    superstring is returned."""
    sequences = deduplicate(sequences)
    shortest = "".join(sequences)

    for perm in permutations(sequences):
        superstring = reduce(smash, perm)
        if len(superstring) < len(shortest):
            shortest = superstring

    return shortest


def shortest_superstrings(sequences):
    """Return a list of all shortest superstrings that cover
    `sequences`."""
    sequences = deduplicate(sequences)

    shortest = set(["".join(sequences)])
    shortest_length = sum(len(s) for s in sequences)

    for perm in permutations(sequences):
        superstring = reduce(smash, perm)
        superstring_length = len(superstring)
        if superstring_length < shortest_length:
            shortest.clear()
            shortest.add(superstring)
            shortest_length = superstring_length
        elif superstring_length == shortest_length:
            shortest.add(superstring)

    return shortest


def print_report(sequence):
    """Writes a report to stdout for the given DNA sequence."""
    buf = [f"Nucleotide counts for {sequence}:\n"]

    counts = Counter(sequence)
    for base in BASES:
        buf.append(f"{base:>10}{counts.get(base, 0):>12}")

    other = sum(v for k, v in counts.items() if k not in BASES)
    buf.append(f"{'Other':>10}{other:>12}")

    buf.append(" " * 5 + "_" * 17)
    buf.append(f"{'Total length':>17}{sum(counts.values()):>5}")

    print(os.linesep.join(buf), "\n")


if __name__ == "__main__":
    test_cases = [
        ("TA", "AAG", "TA", "GAA", "TA"),
        ("CATTAGGG", "ATTAG", "GGG", "TA"),
        ("AAGAUGGA", "GGAGCGCAUC", "AUCGCAAUAAGGA"),
        (
            "ATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTAT",
            "GGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGT",
            "CTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA",
            "TGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
            "AACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTT",
            "GCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTC",
            "CGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATTCTGCTTATAACACTATGTTCT",
            "TGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
            "CGTAAAAAATTACAACGTCCTTTGGCTATCTCTTAAACTCCTGCTAAATGCTCGTGC",
            "GATGGAGCGCATCGAACGCAATAAGGATCATTTGATGGGACGTTTCGTCGACAAAGTCTTGTTTCGAGAGTAACGGCTACCGTCTTCGATT",
            "TTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGATGGAGCGCATC",
            "CTATGTTCTTATGAAATGGATGTTCTGAGTTGGTCAGTCCCAATGTGCGGGGTTTCTTTTAGTACGTCGGGAGTGGTATTATA",
            "TCTCTTAAACTCCTGCTAAATGCTCGTGCTTTCCAATTATGTAAGCGTTCCGAGACGGGGTGGTCGATTCTGAGGACAAAGGTCAAGA",
        ),
    ]

    for case in test_cases:
        for superstring in shortest_superstrings(case):
            print_report(superstring)

    # or ..
    #
    # for case in test_cases:
    #     print_report(shortest_superstring(case))
    #
    # .. if you don't want all possible shortest superstrings.

```

