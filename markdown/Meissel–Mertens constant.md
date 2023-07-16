# Meissel–Mertens constant

## Task Link
[Rosetta Code - Meissel–Mertens constant](https://rosettacode.org/wiki/Meissel%E2%80%93Mertens_constant)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

/**
 * Calculates the Meissel-Mertens constant correct to 9 s.f. in approximately 15 seconds.
 */
public final class MeisselMertensConstant {
	
	public static void main(String[] aArgs) {
		List<Double> primeReciprocals = listPrimeReciprocals(1_000_000_000);
		final double euler = 0.577_215_664_901_532_861;
		double sum = 0.0;
	    for ( double reciprocal : primeReciprocals ) {
	    	sum +=  reciprocal + Math.log(1.0 - reciprocal);
	    }	
	    
	    final double constant = euler + sum;	
	    System.out.println("The Meissel-Mertens constant = " + constant);
	}	
	
	private static List<Double> listPrimeReciprocals(int aLimit) {
		BitSet sieve = new BitSet(aLimit + 1);
		sieve.set(2, aLimit + 1);
		
		final int squareRoot = (int) Math.sqrt(aLimit);
		for ( int i = 2; i <= squareRoot; i = sieve.nextSetBit(i + 1) ) {
			for ( int j = i * i; j <= aLimit; j += i ) {
				sieve.clear(j);
			}
		}
		
		List<Double> result = new ArrayList<Double>(sieve.cardinality());
		for ( int i = 2; i >= 0; i = sieve.nextSetBit(i + 1) ) {
			result.add(1.0 / i);
		}
		
		return result;
	}

}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python

from math import log

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False        
    return True


if __name__ == '__main__':
    Euler = 0.57721566490153286
    m = 0
    for x in range(2, 10_000_000):
        if isPrime(x):
            m += log(1-(1/x)) + (1/x)

    print("MM =", Euler + m)

```

