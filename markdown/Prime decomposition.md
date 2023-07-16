# Prime decomposition

## Task Link
[Rosetta Code - Prime decomposition](https://rosettacode.org/wiki/Prime_decomposition)

## Java Code
### java_code_1.txt
```java
public boolean prime(BigInteger i);

```

### java_code_2.txt
```java
public static List<BigInteger> primeFactorBig(BigInteger a){
    List<BigInteger> ans = new LinkedList<BigInteger>();
    //loop until we test the number itself or the number is 1
    for (BigInteger i = BigInteger.valueOf(2); i.compareTo(a) <= 0 && !a.equals(BigInteger.ONE);
         i = i.add(BigInteger.ONE)){
        while (a.remainder(i).equals(BigInteger.ZERO) && prime(i)) { //if we have a prime factor
            ans.add(i); //put it in the list
            a = a.divide(i); //factor it out of the number
        }
    }
    return ans;
}

```

### java_code_3.txt
```java
private static final BigInteger two = BigInteger.valueOf(2);

public List<BigInteger> primeDecomp(BigInteger a) {
    // impossible for values lower than 2
    if (a.compareTo(two) < 0) {
        return null; 
    }

    //quickly handle even values
    List<BigInteger> result = new ArrayList<BigInteger>();
    while (a.and(BigInteger.ONE).equals(BigInteger.ZERO)) {
        a = a.shiftRight(1);
        result.add(two);
    }

    //left with odd values
    if (!a.equals(BigInteger.ONE)) {
        BigInteger b = BigInteger.valueOf(3);
        while (b.compareTo(a) < 0) {
            if (b.isProbablePrime(10)) {
                BigInteger[] dr = a.divideAndRemainder(b);
                if (dr[1].equals(BigInteger.ZERO)) {
                    result.add(b);
                    a = dr[0];
                }
            }
            b = b.add(two);
        }
        result.add(b); //b will always be prime here...
    }
    return result;
}

```

### java_code_4.txt
```java
private static final BigInteger TWO = BigInteger.valueOf(2);
private static final BigInteger THREE = BigInteger.valueOf(3);
private static final BigInteger FIVE = BigInteger.valueOf(5);

public static ArrayList<BigInteger> primeDecomp(BigInteger n){
    if(n.compareTo(TWO) < 0) return null;
    ArrayList<BigInteger> factors = new ArrayList<BigInteger>();
    
    // handle even values
    while(n.and(BigInteger.ONE).equals(BigInteger.ZERO)){
        n = n.shiftRight(1);
        factors.add(TWO);
    }
    
    // handle values divisible by three
    while(n.mod(THREE).equals(BigInteger.ZERO)){
        factors.add(THREE);
        n = n.divide(THREE);
    }
    
    // handle values divisible by five
    while(n.mod(FIVE).equals(BigInteger.ZERO)){
        factors.add(FIVE);
        n = n.divide(FIVE);
    }
    
    // much like how we can skip multiples of two, we can also skip
    // multiples of three and multiples of five. This increment array
    // helps us to accomplish that
    int[] pattern = {4,2,4,2,4,6,2,6};
    int pattern_index = 0;
    BigInteger current_test = BigInteger.valueOf(7);
    while(!n.equals(BigInteger.ONE)){
        while(n.mod(current_test).equals(BigInteger.ZERO)){
            factors.add(current_test);
            n = n.divide(current_test);
        }
        current_test = current_test.add(BigInteger.valueOf(pattern[pattern_index]));
        pattern_index = (pattern_index + 1) & 7;
    }
    
    return factors;
}

```

### java_code_5.txt
```java
public static List<BigInteger> primeFactorBig(BigInteger a){
    List<BigInteger> ans = new LinkedList<BigInteger>();

    for(BigInteger divisor = BigInteger.valueOf(2);
        a.compareTo(ONE) > 0; divisor = divisor.add(ONE))
        while(a.mod(divisor).equals(ZERO)){
             ans.add(divisor);
             a = a.divide(divisor);
        }
    return ans;
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

import sys
from itertools import cycle

def is_prime(n):
    return list(zip((True, False), decompose(n)))[-1][0]

class IsPrimeCached(dict):
    def __missing__(self, n):
        r = is_prime(n)
        self[n] = r
        return r

is_prime_cached = IsPrimeCached()

def croft():
    """Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    # Copied from:
    #   https://code.google.com/p/pyprimes/source/browse/src/pyprimes.py
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {}  # Map x*d -> 2*d.
    not_primeroot = tuple(x not in {1,7,11,13,17,19,23,29} for x in range(30))
    q = 1
    for x in cycle((6, 4, 2, 4, 2, 4, 6, 2)):
        # Iterate over prime candidates 7, 11, 13, 17, ...
        q += x
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots.pop(q)
            x = q + p
            while not_primeroot[x % 30] or x in roots:
                x += p
            roots[x] = p
        else:
            roots[q * q] = q + q
            yield q
primes = croft

def decompose(n):
    for p in primes():
        if p*p > n: break
        while n % p == 0:
            yield p
            n //=p
    if n > 1:
        yield n


if __name__ == '__main__':
    # Example: calculate factors of Mersenne numbers to M59 #

    import time

    for m in primes():
        p = 2 ** m - 1
        print( "2**{0:d}-1 = {1:d}, with factors:".format(m, p) )
        start = time.time()
        for factor in decompose(p):
            print(factor, end=' ')
            sys.stdout.flush()

        print( "=> {0:.2f}s".format( time.time()-start ) )
        if m >= 59:
            break

```

### python_code_2.txt
```python
from math import floor, sqrt
try: 
    long
except NameError: 
    long = int

def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = 2 if n % 2 == 0 else 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return [q] + fac(n // q) if q <= maxq else [n]

if __name__ == '__main__':
    import time
    start = time.time()
    tocalc =  2**59-1
    print("%s = %s" % (tocalc, fac(tocalc)))
    print("Needed %ss" % (time.time() - start))

```

