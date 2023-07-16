# Achilles numbers

## Task Link
[Rosetta Code - Achilles numbers](https://rosettacode.org/wiki/Achilles_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public final class AchlllesNumbers {

	public static void main(String[] aArgs) {
		Set<Integer> perfectPowers = perfectPowers(500_000);
	    List<Integer> achilles = achilles(1, 250_000, perfectPowers);
	    List<Integer> totients = totients(250_000);

	    System.out.println("First 50 Achilles numbers:");
	    for ( int i = 0; i < 50; i++ ) {
	    	System.out.print(String.format("%4d%s", achilles.get(i), ( ( i + 1 ) % 10 == 0 ) ? "\n" : " "));
	    }
	    System.out.println();
	    
	    System.out.println("First 50 strong Achilles numbers:");
	    for ( int i = 0, count = 0; count < 50; i++ ) {
	    	if ( achilles.contains(totients.get(achilles.get(i))) ) {
	    		System.out.print(String.format("%6d%s", achilles.get(i), ( ++count % 10 == 0 ) ? "\n" : " "));
	    	}
	    }
	    System.out.println();
	    
	    System.out.println("Number of Achilles numbers with:");
	    for ( int i = 100; i < 1_000_000; i *= 10 ) {
	    	final int digits = String.valueOf(i).length() - 1;
	    	System.out.println("    " + digits + " digits: " + achilles(i / 10, i - 1, perfectPowers).size());
	    }
	}
	
	private static List<Integer> achilles(int aFrom, int aTo, Set<Integer> aPerfectPowers) {
	    Set<Integer> result = new TreeSet<Integer>();
	    final int cubeRoot = (int) Math.cbrt(aTo / 4);
	    final int squareRoot = (int) Math.sqrt(aTo / 8);
	    for ( int b = 2; b <= cubeRoot; b++ ) {
	        final int bCubed = b * b * b;
	        for ( int a = 2; a <= squareRoot; a++ ) {
	            int achilles = bCubed * a * a;
	            if ( achilles >= aTo ) {
	                break;
	            }
	            if ( achilles >= aFrom && ! aPerfectPowers.contains(achilles) ) {
	                result.add(achilles);
	            }
	        }
	    }
	    return new ArrayList<Integer>(result);
	}
	
	private static Set<Integer> perfectPowers(int aN) {
	    Set<Integer> result = new TreeSet<Integer>();
	    for ( int i = 2, root = (int) Math.sqrt(aN); i <= root; i++ ) {
	        for ( int perfect = i * i; perfect < aN; perfect *= i ) {
	            result.add(perfect);
	        }
	    }
	    return result;
	}
	
	private static List<Integer> totients(int aN) {
		List<Integer> result = IntStream.rangeClosed(0, aN).boxed().collect(Collectors.toList());;
		for ( int i = 2; i <= aN; i++ ) {
			if ( result.get(i) == i ) {
				result.set(i, i - 1);
				for ( int j = i * 2; j <= aN; j = j + i ) {
					result.set(j, ( result.get(j) / i ) * ( i - 1 ));
				}
			}
		}
		return result;
	}	

}

```

## Python Code
### python_code_1.txt
```python
from math import gcd
from sympy import factorint
 
def is_Achilles(n):
    p = factorint(n).values()
    return all(i > 1 for i in p) and gcd(*p) == 1

def is_strong_Achilles(n):
    return is_Achilles(n) and is_Achilles(totient(n))
 
def test_strong_Achilles(nachilles, nstrongachilles):
    # task 1
    print('First', nachilles, 'Achilles numbers:')
    n, found = 0, 0
    while found < nachilles:
        if is_Achilles(n):
            found += 1
            print(f'{n: 8,}', end='\n' if found % 10 == 0 else '')
        n += 1

    # task 2
    print('\nFirst', nstrongachilles, 'strong Achilles numbers:')
    n, found = 0, 0
    while found < nstrongachilles:
        if is_strong_Achilles(n):
            found += 1
            print(f'{n: 9,}', end='\n' if found % 10 == 0 else '')
        n += 1

    # task 3
    print('\nCount of Achilles numbers for various intervals:')
    intervals = [[10, 99], [100, 999], [1000, 9999], [10000, 99999], [100000, 999999]]
    for interval in intervals:
        print(f'{interval}:', sum(is_Achilles(i) for i in range(*interval)))


test_strong_Achilles(50, 100)

```

