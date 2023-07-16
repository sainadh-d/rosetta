# Brilliant numbers

## Task Link
[Rosetta Code - Brilliant numbers](https://rosettacode.org/wiki/Brilliant_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class BrilliantNumbers {
    public static void main(String[] args) {
        var primesByDigits = getPrimesByDigits(100000000);
        System.out.println("First 100 brilliant numbers:");
        List<Integer> brilliantNumbers = new ArrayList<>();
        for (var primes : primesByDigits) {
            int n = primes.size();
            for (int i = 0; i < n; ++i) {
                int prime1 = primes.get(i);
                for (int j = i; j < n; ++j) {
                    int prime2 = primes.get(j);
                    brilliantNumbers.add(prime1 * prime2);
                }
            }
            if (brilliantNumbers.size() >= 100)
                break;
        }
        Collections.sort(brilliantNumbers);
        for (int i = 0; i < 100; ++i) {
            char c = (i + 1) % 10 == 0 ? '\n' : ' ';
            System.out.printf("%,5d%c", brilliantNumbers.get(i), c);
        }
        System.out.println();
        long power = 10;
        long count = 0;
        for (int p = 1; p < 2 * primesByDigits.size(); ++p) {
            var primes = primesByDigits.get(p / 2);
            long position = count + 1;
            long minProduct = 0;
            int n = primes.size();
            for (int i = 0; i < n; ++i) {
                long prime1 = primes.get(i);
                var primes2 = primes.subList(i, n);
                int q = (int)((power + prime1 - 1) / prime1);
                int j = Collections.binarySearch(primes2, q);
                if (j == n)
                    continue;
                if (j < 0)
                    j = -(j + 1);
                long prime2 = primes2.get(j);
                long product = prime1 * prime2;
                if (minProduct == 0 || product < minProduct)
                    minProduct = product;
                position += j;
                if (prime1 >= prime2)
                    break;
            }
            System.out.printf("First brilliant number >= 10^%d is %,d at position %,d\n",
                                p, minProduct, position);
            power *= 10;
            if (p % 2 == 1) {
                long size = primes.size();
                count += size * (size + 1) / 2;
            }
        }
    }

    private static List<List<Integer>> getPrimesByDigits(int limit) {
        PrimeGenerator primeGen = new PrimeGenerator(100000, 100000);
        List<List<Integer>> primesByDigits = new ArrayList<>();
        List<Integer> primes = new ArrayList<>();
        for (int p = 10; p <= limit; ) {
            int prime = primeGen.nextPrime();
            if (prime > p) {
                primesByDigits.add(primes);
                primes = new ArrayList<>();
                p *= 10;
            }
            primes.add(prime);
        }
        return primesByDigits;
    }
}

```

## Python Code
### python_code_1.txt
```python
from primesieve.numpy import primes
from math import isqrt
import numpy as np

max_order = 9
blocks = [primes(10**n, 10**(n + 1)) for n in range(max_order)]

def smallest_brilliant(lb):
    pos = 1
    root = isqrt(lb)

    for blk in blocks:
        n = len(blk)
        if blk[-1]*blk[-1] < lb:
            pos += n*(n + 1)//2
            continue

        i = np.searchsorted(blk, root, 'left')
        i += blk[i]*blk[i] < lb

        if not i:
            return blk[0]*blk[0], pos

        p = blk[:i + 1]
        q = (lb - 1)//p
        idx = np.searchsorted(blk, q, 'right')

        sel = idx < n
        p, idx = p[sel], idx[sel]
        q = blk[idx]

        sel = q >= p
        p, q, idx = p[sel], q[sel], idx[sel]

        pos += np.sum(idx - np.arange(len(idx)))
        return np.min(p*q), pos

res = []
p = 0
for i in range(100):
    p, _ = smallest_brilliant(p + 1)
    res.append(p)

print(f'first 100 are {res}')

for i in range(max_order*2):
    thresh = 10**i
    p, pos = smallest_brilliant(thresh)
    print(f'Above 10^{i:2d}: {p:20d} at #{pos}')

```

