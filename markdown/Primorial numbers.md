# Primorial numbers

## Task Link
[Rosetta Code - Primorial numbers](https://rosettacode.org/wiki/Primorial_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PrimorialNumbers {
    final static int sieveLimit = 1300_000;
    static boolean[] notPrime = sieve(sieveLimit);

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++)
            System.out.printf("primorial(%d): %d%n", i, primorial(i));

        for (int i = 1; i < 6; i++) {
            int len = primorial((int) Math.pow(10, i)).toString().length();
            System.out.printf("primorial(10^%d) has length %d%n", i, len);
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
from pyprimes import nprimes
from functools import reduce


primelist = list(nprimes(1000001))    # [2, 3, 5, ...]

def primorial(n):
    return reduce(int.__mul__, primelist[:n], 1)

if __name__ == '__main__':
    print('First ten primorals:', [primorial(n) for n in range(10)])
    for e in range(7):
        n = 10**e
        print('primorial(%i) has %i digits' % (n, len(str(primorial(n)))))

```

