# Consecutive primes with ascending or descending differences

## Task Link
[Rosetta Code - Consecutive primes with ascending or descending differences](https://rosettacode.org/wiki/Consecutive_primes_with_ascending_or_descending_differences)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

public final class ConsecutivePrimes {

	public static void main(String[] aArgs) {
		final int limit = 1_000_000;
		List<Integer> primes = listPrimeNumbers(limit);
		
		List<Integer> asc = new ArrayList<Integer>();
		List<Integer> desc = new ArrayList<Integer>();
		List<List<Integer>> maxAsc = new ArrayList<List<Integer>>();
		List<List<Integer>> maxDesc = new ArrayList<List<Integer>>();
	    int maxAscSize = 0;
	    int maxDescSize = 0;
	    
	    for ( int prime : primes ) {
	   	    final int ascSize = asc.size();
	        if ( ascSize > 1 && prime - asc.get(ascSize - 1) <= asc.get(ascSize - 1) - asc.get(ascSize - 2) ) {
	            asc = new ArrayList<Integer>(asc.subList(ascSize - 1, asc.size()));
	        }	        
	        asc.add(prime);
	        
	        if ( asc.size() >= maxAscSize ) {
	            if ( asc.size() > maxAscSize ) {
	                maxAscSize = asc.size();
	                maxAsc.clear();
	            }
	            maxAsc.add( new ArrayList<Integer>(asc) );
	        }
	        
	        final int descSize = desc.size();
	        if ( descSize > 1 && prime - desc.get(descSize - 1) >= desc.get(descSize - 1) - desc.get(descSize - 2) ) {
	            desc = new ArrayList<Integer>(desc.subList(descSize - 1, desc.size()));
	        }
	        desc.add(prime);
	        
	        if ( desc.size() >= maxDescSize ) {
	            if ( desc.size() > maxDescSize ) {
	                maxDescSize = desc.size();
	                maxDesc.clear();
	            }
	            maxDesc.add( new ArrayList<Integer>(desc) );
	        }
	    }
	    
	    System.out.println("Longest run(s) of ascending prime gaps up to " + limit + ":");
	    for ( List<Integer> list : maxAsc ) {
	        displayResult(list);
	    }
	    System.out.println();
	    
	    System.out.println("Longest run(s) of descending prime gaps up to " + limit + ":");
	    for( List<Integer> list : maxDesc ) {
	        displayResult(list);
	    }
	}
	
	private static List<Integer> listPrimeNumbers(int aLimit) {
		BitSet sieve = new BitSet(aLimit + 1);
		sieve.set(2, aLimit + 1);
		for ( int i = 2; i <= Math.sqrt(aLimit); i = sieve.nextSetBit(i + 1) ) {
			for ( int j = i * i; j <= aLimit; j = j + i ) {
				sieve.clear(j);
			}
		}
		
		List<Integer> result = new ArrayList<Integer>(sieve.cardinality());
		for ( int i = 2; i >= 0; i = sieve.nextSetBit(i + 1) ) {
			result.add(i);
		}
		return result;
	}
	
	private static void displayResult(List<Integer> aList) {
		for ( int i = 0; i < aList.size(); i++ ) {
	        if ( i > 0 ) {
	            System.out.print(" (" + ( aList.get(i) - aList.get(i - 1) ) + ") ");
	        }
	        System.out.print(aList.get(i));
	    }
	    System.out.println();
	}

}

```

## Python Code
### python_code_1.txt
```python
from sympy import sieve

primelist = list(sieve.primerange(2,1000000))

listlen = len(primelist)

# ascending

pindex = 1
old_diff = -1
curr_list=[primelist[0]]
longest_list=[]

while pindex < listlen:

    diff = primelist[pindex] - primelist[pindex-1]
    if diff > old_diff:
        curr_list.append(primelist[pindex])
        if len(curr_list) > len(longest_list):
            longest_list = curr_list
    else:
        curr_list = [primelist[pindex-1],primelist[pindex]]
        
    old_diff = diff
    pindex += 1
    
print(longest_list)

# descending

pindex = 1
old_diff = -1
curr_list=[primelist[0]]
longest_list=[]

while pindex < listlen:

    diff = primelist[pindex] - primelist[pindex-1]
    if diff < old_diff:
        curr_list.append(primelist[pindex])
        if len(curr_list) > len(longest_list):
            longest_list = curr_list
    else:
        curr_list = [primelist[pindex-1],primelist[pindex]]
        
    old_diff = diff
    pindex += 1
    
print(longest_list)

```

