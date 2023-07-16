# Wieferich primes

## Task Link
[Rosetta Code - Wieferich primes](https://rosettacode.org/wiki/Wieferich_primes)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class WieferichPrimes {
    public static void main(String[] args) {
        final int limit = 5000;
        System.out.printf("Wieferich primes less than %d:\n", limit);
        for (Integer p : wieferichPrimes(limit))
            System.out.println(p);
    }    

    private static boolean[] primeSieve(int limit) {
        boolean[] sieve = new boolean[limit];
        Arrays.fill(sieve, true);
        if (limit > 0)
            sieve[0] = false;
        if (limit > 1)
            sieve[1] = false;
        for (int i = 4; i < limit; i += 2)
            sieve[i] = false;
        for (int p = 3; ; p += 2) {
            int q = p * p;
            if (q >= limit)
                break;
            if (sieve[p]) {
                int inc = 2 * p;
                for (; q < limit; q += inc)
                    sieve[q] = false;
            }
        }
        return sieve;
    }

    private static long modpow(long base, long exp, long mod) {
        if (mod == 1)
            return 0;
        long result = 1;
        base %= mod;
        for (; exp > 0; exp >>= 1) {
            if ((exp & 1) == 1)
                result = (result * base) % mod;
            base = (base * base) % mod;
        }
        return result;
    }

    private static List<Integer> wieferichPrimes(int limit) {
        boolean[] sieve = primeSieve(limit);
        List<Integer> result = new ArrayList<>();
        for (int p = 2; p < limit; ++p) {
            if (sieve[p] && modpow(2, p - 1, p * p) == 1)
                result.add(p);
        }
        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False        
    return True

def isWeiferich(p):
    if not isPrime(p):
        return False
    q = 1
    p2 = p ** 2
    while p > 1:
        q = (2 * q) % p2
        p -= 1
    if q == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Wieferich primes less than 5000: ")
    for i in range(2, 5001):
        if isWeiferich(i):
            print(i)

```

