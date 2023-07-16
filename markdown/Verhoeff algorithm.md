# Verhoeff algorithm

## Task Link
[Rosetta Code - Verhoeff algorithm](https://rosettacode.org/wiki/Verhoeff_algorithm)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.List;

public class VerhoeffAlgorithm {

	public static void main(String[] args) {
		initialise();

		List<List<Object>> tests = List.of(
			List.of( "236", true ), List.of( "12345", true ), List.of( "123456789012", false ) );
		
		for ( List<Object> test : tests ) {
		    Object object = verhoeffChecksum((String) test.get(0), false, (boolean) test.get(1));		    
		    System.out.println("The check digit for " + test.get(0) + " is " + object + "\n");
		    
		    for ( String number : List.of( test.get(0) + String.valueOf(object), test.get(0) + "9" ) ) {		    	
		        object = verhoeffChecksum(number, true, (boolean) test.get(1));
		        String result = (boolean) object ? "correct" : "incorrect";
		        System.out.println("The validation for " + number + " is " + result + ".\n");
		    }
		}
	}
	
	private static Object verhoeffChecksum(String number, boolean doValidation, boolean doDisplay) {
		if ( doDisplay ) {
			String calculationType = doValidation ? "Validation" : "Check digit";
	        System.out.println(calculationType + " calculations for " + number + "\n");
	        System.out.println(" i  ni  p[i, ni]  c");
	        System.out.println("-------------------");
	    }
		
		if ( ! doValidation ) {
			number += "0";			
		}
		
	    int c = 0;
	    final int le = number.length() - 1;
	    for ( int i = le; i >= 0; i-- ) {
	    	final int ni = number.charAt(i) - '0'; 
	        final int pi = permutationTable.get((le - i) % 8).get(ni);
	        c = multiplicationTable.get(c).get(pi);
	        
	        if ( doDisplay ) {
	        	System.out.println(String.format("%2d%3d%8d%6d\n", le - i, ni, pi, c)); 
	        }
	    }
		
	    if ( doDisplay && ! doValidation ) {
	    	System.out.println("inverse[" + c + "] = " + inverse.get(c) + "\n");
	    }
	    
	    return doValidation ? c == 0 : inverse.get(c);
	}
	
	private static void initialise() {
		multiplicationTable = List.of(
			List.of( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ),
			List.of( 1, 2, 3, 4, 0, 6, 7, 8, 9, 5 ),
			List.of( 2, 3, 4, 0, 1, 7, 8, 9, 5, 6 ),
			List.of( 3, 4, 0, 1, 2, 8, 9, 5, 6, 7 ),
			List.of( 4, 0, 1, 2, 3, 9, 5, 6, 7, 8 ),
			List.of( 5, 9, 8, 7, 6, 0, 4, 3, 2, 1 ),
			List.of( 6, 5, 9, 8, 7, 1, 0, 4, 3, 2 ),
			List.of( 7, 6, 5, 9, 8, 2, 1, 0, 4, 3 ),
			List.of( 8, 7, 6, 5, 9, 3, 2, 1, 0, 4 ),
			List.of( 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 )
		);		
		
		inverse = Arrays.asList( 0, 4, 3, 2, 1, 5, 6, 7, 8, 9 );
		
		permutationTable = List.of(
				List.of( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ),
				List.of( 1, 5, 7, 6, 2, 8, 3, 0, 9, 4 ),
				List.of( 5, 8, 0, 3, 7, 9, 6, 1, 4, 2 ),
				List.of( 8, 9, 1, 6, 0, 4, 3, 5, 2, 7 ),
				List.of( 9, 4, 5, 3, 1, 2, 6, 8, 7, 0 ),
				List.of( 4, 2, 8, 6, 5, 7, 3, 9, 0, 1 ),
				List.of( 2, 7, 9, 3, 8, 0, 6, 4, 1, 5 ),
				List.of( 7, 0, 4, 6, 9, 1, 3, 2, 5, 8 )
		);	
	}
	
	private static List<List<Integer>> multiplicationTable;
	private static List<Integer> inverse;
	private static List<List<Integer>> permutationTable;
	
}

```

## Python Code
### python_code_1.txt
```python
MULTIPLICATION_TABLE = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 0, 6, 7, 8, 9, 5),
    (2, 3, 4, 0, 1, 7, 8, 9, 5, 6),
    (3, 4, 0, 1, 2, 8, 9, 5, 6, 7),
    (4, 0, 1, 2, 3, 9, 5, 6, 7, 8),
    (5, 9, 8, 7, 6, 0, 4, 3, 2, 1),
    (6, 5, 9, 8, 7, 1, 0, 4, 3, 2),
    (7, 6, 5, 9, 8, 2, 1, 0, 4, 3),
    (8, 7, 6, 5, 9, 3, 2, 1, 0, 4),
    (9, 8, 7, 6, 5, 4, 3, 2, 1, 0),
]

INV = (0, 4, 3, 2, 1, 5, 6, 7, 8, 9)

PERMUTATION_TABLE = [
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 5, 7, 6, 2, 8, 3, 0, 9, 4),
    (5, 8, 0, 3, 7, 9, 6, 1, 4, 2),
    (8, 9, 1, 6, 0, 4, 3, 5, 2, 7),
    (9, 4, 5, 3, 1, 2, 6, 8, 7, 0),
    (4, 2, 8, 6, 5, 7, 3, 9, 0, 1),
    (2, 7, 9, 3, 8, 0, 6, 4, 1, 5),
    (7, 0, 4, 6, 9, 1, 3, 2, 5, 8),
]

def verhoeffchecksum(n, validate=True, terse=True, verbose=False):
    """
    Calculate the Verhoeff checksum over `n`.
    Terse mode or with single argument: return True if valid (last digit is a correct check digit).
    If checksum mode, return the expected correct checksum digit.
    If validation mode, return True if last digit checks correctly.
    """
    if verbose:
        print(f"\n{'Validation' if validate else 'Check digit'}",\
            f"calculations for {n}:\n\n i  nᵢ  p[i,nᵢ]   c\n------------------")
    # transform number list
    c, dig = 0, list(str(n if validate else 10 * n))
    for i, ni in enumerate(dig[::-1]):
        p = PERMUTATION_TABLE[i % 8][int(ni)]
        c = MULTIPLICATION_TABLE[c][p]
        if verbose:
            print(f"{i:2}  {ni}      {p}    {c}")

    if verbose and not validate:
        print(f"\ninv({c}) = {INV[c]}")
    if not terse:
        print(f"\nThe validation for '{n}' is {'correct' if c == 0 else 'incorrect'}."\
              if validate else f"\nThe check digit for '{n}' is {INV[c]}.")
    return c == 0 if validate else INV[c]

if __name__ == '__main__':

    for n, va, t, ve in [
        (236, False, False, True), (2363, True, False, True), (2369, True, False, True),
        (12345, False, False, True), (123451, True, False, True), (123459, True, False, True),
        (123456789012, False, False, False), (1234567890120, True, False, False),
        (1234567890129, True, False, False)]:
        verhoeffchecksum(n, va, t, ve)

```

