# Sieve of Pritchard

## Task Link
[Rosetta Code - Sieve of Pritchard](https://rosettacode.org/wiki/Sieve_of_Pritchard)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

public final class SieveOfPritchard {
 
	public static void main(String[] args) {		
		System.out.println(sieveOfPritchard(150) + System.lineSeparator());
		System.out.println("Number of primes up to 1,000,000 is " + sieveOfPritchard(1_000_000).size() + ".");
		System.out.println();
		
		final long start = System.currentTimeMillis();		
		System.out.print("Number of primes up to 100,000,000 is " + sieveOfPritchard(100_000_000).size());
		final long finish = System.currentTimeMillis();
		System.out.println(". Obtained in a time of " + ( (double) finish - start ) / 1_000 + " seconds.");
	}
	
	private static List<Integer> sieveOfPritchard(int limit) {		
		List<Integer> primes = new ArrayList<Integer>();
		BitSet members = new BitSet(limit + 1);
	    members.set(1);
	    List<Integer> deletions = new ArrayList<Integer>();
	    final int rootLimit = (int) Math.sqrt(limit);
	    int nLimit = 2;
	    int stepLength = 1;
	    int prime = 2;	  
	    	    		
	    while ( prime <= rootLimit ) {
	    	if ( stepLength < limit ) { 
	    		for ( int w = 1; w >= 0; w = members.nextSetBit(w + 1) ) {
                    int n = w + stepLength;	                    
                    while ( n <= nLimit ) {
                        members.set(n);
                        n += stepLength;
		            }
	    		}
	            stepLength = nLimit;
	    	} 
	    	
	    	deletions.clear();
	    	int nextPrime = 5;
	        for ( int w = 1; w < nLimit; w = members.nextSetBit(w + 1) ) {
                if ( nextPrime == 5 && w > prime ) {
                    nextPrime = w;
                }
                final int n = prime * w;
                if ( n > nLimit ) {
                	break;
                }
                deletions.add(n);
	        }
	        for ( int deletion : deletions ) {
	        	members.clear(deletion);
	        }
	        
	        if ( nextPrime < prime ) {
	            break;
	        }
	        
	        primes.add(prime);
	        prime = ( prime == 2 ) ? 3 : nextPrime;	        
	        nLimit = (int) Math.min((long) stepLength * prime, limit);	            
	    }
	    
	    if ( stepLength < limit ) {
	    	for ( int w = 1; w >= 0; w = members.nextSetBit(w + 1) ) {
                int n = w + stepLength;	                    
                while ( n <= limit ) {
                    members.set(n);
                    n += stepLength;
	            }
    		}
	    }
	    
	    members.clear(1);
	    for ( int i = members.nextSetBit(0); i >= 0; i = members.nextSetBit(i + 1) ) {
	    	primes.add(i);
	    }; 
	    
	    return primes;	
	}

}

```

## Python Code
### python_code_1.txt
```python
""" Rosetta Code task rosettacode.org/wiki/Sieve_of_Pritchard """

from numpy import ndarray
from math import isqrt


def pritchard(limit):
    """ Pritchard sieve of primes up to limit """
    members = ndarray(limit + 1, dtype=bool)
    members.fill(False)
    members[1] = True
    steplength, prime, rtlim, nlimit = 1, 2, isqrt(limit), 2
    primes = []
    while prime <= rtlim:
        if steplength < limit:
            for w in range(1, len(members)):
                if members[w]:
                    n = w + steplength
                    while n <= nlimit:
                        members[n] = True
                        n += steplength
            steplength = nlimit

        np = 5
        mcpy = members.copy()
        for w in range(1, len(members)):
            if mcpy[w]:
                if np == 5 and w > prime:
                    np = w
                n = prime * w
                if n > nlimit:
                    break  # no use trying to remove items that can't even be there
                members[n] = False  # no checking necessary now

        if np < prime:
            break
        primes.append(prime)
        prime = 3 if prime == 2 else np
        nlimit = min(steplength * prime, limit)  # advance wheel limit

    newprimes = [i for i in range(2, len(members)) if members[i]]
    return sorted(primes + newprimes)


print(pritchard(150))
print('Number of primes up to 1,000,000:', len(pritchard(1000000)))

```

