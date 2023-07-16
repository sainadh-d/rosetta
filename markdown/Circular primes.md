# Circular primes

## Task Link
[Rosetta Code - Circular primes](https://rosettacode.org/wiki/Circular_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.Arrays;

public class CircularPrimes {
    public static void main(String[] args) {
        System.out.println("First 19 circular primes:");
        int p = 2;
        for (int count = 0; count < 19; ++p) {
            if (isCircularPrime(p)) {
                if (count > 0)
                    System.out.print(", ");
                System.out.print(p);
                ++count;
            }
        }
        System.out.println();
        System.out.println("Next 4 circular primes:");
        int repunit = 1, digits = 1;
        for (; repunit < p; ++digits)
            repunit = 10 * repunit + 1;
        BigInteger bignum = BigInteger.valueOf(repunit);
        for (int count = 0; count < 4; ) {
            if (bignum.isProbablePrime(15)) {
                if (count > 0)
                    System.out.print(", ");
                System.out.printf("R(%d)", digits);
                ++count;
            }
            ++digits;
            bignum = bignum.multiply(BigInteger.TEN);
            bignum = bignum.add(BigInteger.ONE);
        }
        System.out.println();
        testRepunit(5003);
        testRepunit(9887);
        testRepunit(15073);
        testRepunit(25031);
    }

    private static boolean isPrime(int n) {
        if (n < 2)
            return false;
        if (n % 2 == 0)
            return n == 2;
        if (n % 3 == 0)
            return n == 3;
        for (int p = 5; p * p <= n; p += 4) {
            if (n % p == 0)
                return false;
            p += 2;
            if (n % p == 0)
                return false;
        }
        return true;
    }

    private static int cycle(int n) {
        int m = n, p = 1;
        while (m >= 10) {
            p *= 10;
            m /= 10;
        }
        return m + 10 * (n % p);
    }

    private static boolean isCircularPrime(int p) {
        if (!isPrime(p))
            return false;
        int p2 = cycle(p);
        while (p2 != p) {
            if (p2 < p || !isPrime(p2))
                return false;
            p2 = cycle(p2);
        }
        return true;
    }

    private static void testRepunit(int digits) {
        BigInteger repunit = repunit(digits);
        if (repunit.isProbablePrime(15))
            System.out.printf("R(%d) is probably prime.\n", digits);
        else
            System.out.printf("R(%d) is not prime.\n", digits);
    }

    private static BigInteger repunit(int digits) {
        char[] ch = new char[digits];
        Arrays.fill(ch, '1');
        return new BigInteger(new String(ch));
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(8):#number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True

def isPrime(n: int) -> bool:
    '''
        https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
    '''
    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def rotations(n: int)-> set((int,)):
    '''
        >>> {123, 231, 312} == rotations(123)
        True
    '''
    a = str(n)
    return set(int(a[i:] + a[:i]) for i in range(len(a)))

def isCircular(n: int) -> bool:
    '''
        >>> [isCircular(n) for n in (11, 31, 47,)]
	[True, True, False]
    '''
    return all(isPrime(int(o)) for o in rotations(n))

from itertools import product

def main():
    result = [2, 3, 5, 7]
    first = '137'
    latter = '1379'
    for i in range(1, 6):
        s = set(int(''.join(a)) for a in product(first, *((latter,) * i)))
        while s:
            a = s.pop()
            b = rotations(a)
            if isCircular(a):
                result.append(min(b))
            s -= b
    result.sort()
    return result

assert [2, 3, 5, 7, 11, 13, 17, 37, 79, 113, 197, 199, 337, 1193, 3779, 11939, 19937, 193939, 199933] == main()


repunit = lambda n: int('1' * n)

def repmain(n: int) -> list:
    '''
        returns the first n repunit primes, probably.
    '''
    result = []
    i = 2
    while len(result) < n:
        if is_Prime(repunit(i)):
            result.append(i)
        i += 1
    return result

assert [2, 19, 23, 317, 1031] == repmain(5)

# because this Miller-Rabin test is already on rosettacode there's no good reason to test the longer repunits.

```

