# Euclid-Mullin sequence

## Task Link
[Rosetta Code - Euclid-Mullin sequence](https://rosettacode.org/wiki/Euclid-Mullin_sequence)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class EulerMullinSequence {

	public static void main(String[] aArgs) {
		primes = listPrimesUpTo(1_000_000);
		
		System.out.println("The first 27 terms of the Euler-Mullin sequence:");
		System.out.println(2);
		for ( int i = 1; i < 27; i++ ) {
			System.out.println(nextEulerMullin());
		}

	}
	
	private static BigInteger nextEulerMullin() {
		BigInteger smallestPrime = smallestPrimeFactor(product.add(BigInteger.ONE));
		product = product.multiply(smallestPrime);
		
		return smallestPrime;
	}
	
	private static BigInteger smallestPrimeFactor(BigInteger aNumber) {
		if ( aNumber.isProbablePrime(probabilityLevel) ) {
			return aNumber;
		}
		
		for ( BigInteger prime : primes ) {
			if ( aNumber.mod(prime).signum() == 0 ) {
				return prime;
			}
 		}
		
		BigInteger factor = pollardsRho(aNumber);
		return smallestPrimeFactor(factor);
	}
	
	private static BigInteger pollardsRho(BigInteger aN) {
		if ( aN.equals(BigInteger.ONE) ) {
			return BigInteger.ONE;
		}
		
		if ( aN.mod(BigInteger.TWO).signum() == 0 ) {
			return BigInteger.TWO;
		}
		
		final BigInteger core  = new BigInteger(aN.bitLength(), random);
		BigInteger x  = new BigInteger(aN.bitLength(), random);
		BigInteger xx = x;
		BigInteger divisor = null;		
		
		do {
			x = x.multiply(x).mod(aN).add(core).mod(aN);
			xx = xx.multiply(xx).mod(aN).add(core).mod(aN);
			xx = xx.multiply(xx).mod(aN).add(core).mod(aN);
			divisor = x.subtract(xx).gcd(aN);
		} while ( divisor.equals(BigInteger.ONE) );
		
		return divisor;
	}	
	
	private static List<BigInteger> listPrimesUpTo(int aLimit) {
		BitSet sieve = new BitSet(aLimit + 1);
		sieve.set(2, aLimit + 1);
		
		final int squareRoot = (int) Math.sqrt(aLimit);
		for ( int i = 2; i <= squareRoot; i = sieve.nextSetBit(i + 1) ) {
			for ( int j = i * i; j <= aLimit; j = j + i ) {
				sieve.clear(j);
			}
		}
		
		List<BigInteger> result = new ArrayList<BigInteger>(sieve.cardinality());
		for ( int i = 2; i >= 0; i = sieve.nextSetBit(i + 1) ) {
			result.add(BigInteger.valueOf(i));
		}
		
		return result;
	}
	
	private static List<BigInteger> primes;
	private static BigInteger product = BigInteger.TWO;
	private static ThreadLocalRandom random = ThreadLocalRandom.current();
	
	private static final int probabilityLevel = 20;

}

```

## Python Code
### python_code_1.txt
```python
""" Rosetta code task: Euclid-Mullin_sequence """

from primePy import primes

def euclid_mullin():
    """ generate Euclid-Mullin sequence """
    total = 1
    while True:
        next_iter = primes.factor(total + 1)
        total *= next_iter
        yield next_iter

GEN = euclid_mullin()
print('First 16 Euclid-Mullin numbers:', ', '.join(str(next(GEN)) for _ in range(16)))

```

