# Sequence of primorial primes

## Task Link
[Rosetta Code - Sequence of primorial primes](https://rosettacode.org/wiki/Sequence_of_primorial_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PrimorialPrimes {

    final static int sieveLimit = 1550_000;
    static boolean[] notPrime = sieve(sieveLimit);

    public static void main(String[] args) {

        int count = 0;
        for (int i = 1; i < 1000_000 && count < 20; i++) {
            BigInteger b = primorial(i);
            if (b.add(BigInteger.ONE).isProbablePrime(1)
                    || b.subtract(BigInteger.ONE).isProbablePrime(1)) {
                System.out.printf("%d ", i);
                count++;
            }
        }
    }

    static BigInteger primorial(int n) {
        if (n == 0)
            return BigInteger.ONE;

        BigInteger result = BigInteger.ONE;
        for (int i = 0; i < sieveLimit && n > 0; i++) {
            if (notPrime[i])
                continue;
            result = result.multiply(BigInteger.valueOf(i));
            n--;
        }
        return result;
    }

    public static boolean[] sieve(int limit) {
        boolean[] composite = new boolean[limit];
        composite[0] = composite[1] = true;

        int max = (int) Math.sqrt(limit);
        for (int n = 2; n <= max; n++) {
            if (!composite[n]) {
                for (int k = n * n; k < limit; k += n) {
                    composite[k] = true;
                }
            }
        }
        return composite;
    }
}

```

## Python Code
### python_code_1.txt
```python
import pyprimes

def primorial_prime(_pmax=500):
    isprime = pyprimes.isprime
    n, primo = 0, 1
    for prime in pyprimes.nprimes(_pmax):
        n, primo = n+1, primo * prime
        if isprime(primo-1) or isprime(primo+1):
            yield n
        
if __name__ == '__main__':
    # Turn off warning on use of probabilistic formula for prime test
    pyprimes.warn_probably = False  
    for i, n in zip(range(20), primorial_prime()):
        print('Primorial prime %2i at primorial index: %3i' % (i+1, n))

```

