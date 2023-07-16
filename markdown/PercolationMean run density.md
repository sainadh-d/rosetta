# Percolation/Mean run density

## Task Link
[Rosetta Code - Percolation/Mean run density](https://rosettacode.org/wiki/Percolation/Mean_run_density)

## Java Code
### java_code_1.txt
```java
import java.util.concurrent.ThreadLocalRandom;

public final class PercolationMeanRun {

	public static void main(String[] aArgs) {
		System.out.println("Running 1000 tests each:" + System.lineSeparator());
		System.out.println(" p\tlength\tresult\ttheory\t   difference");
		System.out.println("-".repeat(48));
		
	    for ( double probability = 0.1; probability <= 0.9; probability += 0.2 ) {
	        double theory = probability * ( 1.0 - probability );
	        int length = 100;
	        while ( length <= 100_000 ) {
	            double result = runTest(probability, length, 1_000);
	            System.out.println(String.format("%.1f\t%6d\t%.4f\t%.4f\t%+.4f (%+.2f%%)",
	            	probability, length, result, theory, result - theory, ( result - theory ) / theory * 100));
	            length *= 10;
	        }
	        System.out.println();
	    }

	}
	
	private static double runTest(double aProbability, int aLength, int aRunCount) {
		double count = 0.0;
	    for ( int run = 0; run < aRunCount; run++ ) {
	        int previousBit = 0;
	        int length = aLength;
	        while ( length-- > 0 ) {
	            int nextBit = ( random.nextDouble(1.0) < aProbability ) ? 1 : 0;
	            if ( previousBit < nextBit ) {
	            	count += 1.0;
	            }
	            previousBit = nextBit;
	        }
	    }
	    return count / aRunCount / aLength;
	}

	private static ThreadLocalRandom random = ThreadLocalRandom.current();

}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division
from random import random
from math import fsum

n, p, t = 100, 0.5, 500

def newv(n, p): 
    return [int(random() < p) for i in range(n)]

def runs(v): 
    return sum((a & ~b) for a, b in zip(v, v[1:] + [0]))

def mean_run_density(n, p):
    return runs(newv(n, p)) / n

for p10 in range(1, 10, 2):
    p = p10 / 10
    limit = p * (1 - p)
    print('')
    for n2 in range(10, 16, 2):
        n = 2**n2
        sim = fsum(mean_run_density(n, p) for i in range(t)) / t
        print('t=%3i p=%4.2f n=%5i p(1-p)=%5.3f sim=%5.3f delta=%3.1f%%'
              % (t, p, n, limit, sim, abs(sim - limit) / limit * 100 if limit else sim * 100))

```

