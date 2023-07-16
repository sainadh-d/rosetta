# Lucas-Lehmer test

## Task Link
[Rosetta Code - Lucas-Lehmer test](https://rosettacode.org/wiki/Lucas-Lehmer_test)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
public class Mersenne
{

    public static boolean isPrime(int p) {
        if (p == 2)
            return true;
        else if (p <= 1 || p % 2 == 0)
            return false;
        else {
            int to = (int)Math.sqrt(p);
            for (int i = 3; i <= to; i += 2)
                if (p % i == 0)
                    return false;
            return true;
        }
    }

    public static boolean isMersennePrime(int p) {
        if (p == 2)
            return true;
        else {
            BigInteger m_p = BigInteger.ONE.shiftLeft(p).subtract(BigInteger.ONE);
            BigInteger s = BigInteger.valueOf(4);
            for (int i = 3; i <= p; i++)
                s = s.multiply(s).subtract(BigInteger.valueOf(2)).mod(m_p);
            return s.equals(BigInteger.ZERO);
        }
    }

    // an arbitrary upper bound can be given as an argument
    public static void main(String[] args) {
        int upb;
        if (args.length == 0)
            upb = 500;
        else
            upb = Integer.parseInt(args[0]);

        System.out.print(" Finding Mersenne primes in M[2.." + upb + "]:\nM2 ");
        for (int p = 3; p <= upb; p += 2)
            if (isPrime(p) && isMersennePrime(p))
                System.out.print(" M" + p);
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
from sys import stdout
from math import sqrt, log

def is_prime ( p ):
  if p == 2: return True # Lucas-Lehmer test only works on odd primes
  elif p <= 1 or p % 2 == 0: return False
  else:
    for i in range(3, int(sqrt(p))+1, 2 ): 
      if p % i == 0: return False
    return True

def is_mersenne_prime ( p ):
  if p == 2:
    return True
  else:
    m_p = ( 1 << p ) - 1
    s = 4
    for i in range(3, p+1): 
      s = (s ** 2 - 2) % m_p
    return s == 0

precision = 20000   # maximum requested number of decimal places of 2 ** MP-1 #
long_bits_width = precision * log(10, 2)
upb_prime = int( long_bits_width - 1 ) / 2    # no unsigned #
upb_count = 45      # find 45 mprimes if int was given enough bits #

print (" Finding Mersenne primes in M[2..%d]:"%upb_prime)

count=0
for p in range(2, int(upb_prime+1)): 
  if is_prime(p) and is_mersenne_prime(p):
    print("M%d"%p),
    stdout.flush()
    count += 1
  if count >= upb_count: break
print

```

### python_code_2.txt
```python
def isqrt(n):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        a = 1 << ((1 + n.bit_length()) >> 1)
        while True:
            b = (a + n // a) >> 1
            if b >= a:
                return a
            a = b
 
def isprime(n):
    if n < 5:
        return n == 2 or n == 3
    elif n%2 == 0:
        return False
    else:
        r = isqrt(n)
        k = 3
        while k <= r:
            if n%k == 0:
                return False
            k += 2
        return True
 
def lucas_lehmer_fast(n):
    if n == 2:
        return True
    elif not isprime(n):
        return False
    else:
        m = 2**n - 1
        s = 4
        for i in range(2, n):
            sqr = s*s
            s = (sqr & m) + (sqr >> n)
            if s >= m:
                s -= m
            s -= 2
        return s == 0

# test taken from the previous rosetta implementation

from math import log
from sys import stdout

precision = 20000   # maximum requested number of decimal places of 2 ** MP-1 #
long_bits_width = precision * log(10, 2)
upb_prime = int( long_bits_width - 1 ) / 2    # no unsigned #
# upb_count = 45      # find 45 mprimes if int was given enough bits #
upb_count = 15      # find 45 mprimes if int was given enough bits #
 
print (" Finding Mersenne primes in M[2..%d]:"%upb_prime)
 
count=0
# for p in range(2, upb_prime+1): 
for p in range(2, int(upb_prime+1)): 
  if lucas_lehmer_fast(p):
    print("M%d"%p),
    stdout.flush()
    count += 1
  if count >= upb_count: break
print

```

### python_code_3.txt
```python
import gmpy2 as mp

def lucas_lehmer(n):
    if n == 2:
        return True
    if not mp.is_prime(n):
        return False
    two = mp.mpz(2)
    m = two**n - 1
    s = two*two
    for i in range(2, n):
        sqr = s*s
        s = (sqr & m) + (sqr >> n)
        if s >= m:
            s -= m
        s -= two
    return mp.is_zero(s)

```

