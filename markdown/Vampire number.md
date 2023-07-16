# Vampire number

## Task Link
[Rosetta Code - Vampire number](https://rosettacode.org/wiki/Vampire_number)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.HashSet;

public class VampireNumbers{
    private static int numDigits(long num){
        return Long.toString(Math.abs(num)).length();
    }

    private static boolean fangCheck(long orig, long fang1, long fang2){
        if(Long.toString(fang1).endsWith("0") && Long.toString(fang2).endsWith("0")) return false;

        int origLen = numDigits(orig);
        if(numDigits(fang1) != origLen / 2 || numDigits(fang2) != origLen / 2) return false;

        byte[] origBytes = Long.toString(orig).getBytes();
        byte[] fangBytes = (Long.toString(fang1) + Long.toString(fang2)).getBytes();
        Arrays.sort(origBytes);
        Arrays.sort(fangBytes);
        return Arrays.equals(origBytes, fangBytes);
    }

    public static void main(String[] args){
        HashSet<Long> vamps = new HashSet<Long>();
        for(long i = 10; vamps.size() <= 25; i++ ){
            if((numDigits(i) % 2) != 0) {i = i * 10 - 1; continue;}
            for(long fang1 = 2; fang1 <= Math.sqrt(i) + 1; fang1++){
                if(i % fang1 == 0){
                    long fang2 = i / fang1;
                    if(fangCheck(i, fang1, fang2) && fang1 <= fang2){
                        vamps.add(i);
                        System.out.println(i + ": [" + fang1 + ", " + fang2 +"]");
                    }
                }
            }
        }
        Long[] nums = {16758243290880L, 24959017348650L, 14593825548650L};
        for(Long i : nums){
            for(long fang1 = 2; fang1 <= Math.sqrt(i) + 1; fang1++){
                if(i % fang1 == 0){
                    long fang2 = i / fang1;
                    if(fangCheck(i, fang1, fang2) && fang1 <= fang2){
                        System.out.println(i + ": [" + fang1 + ", " + fang2 +"]");
                    }
                }
            }
        }
    }
}

```

### java_code_2.txt
```java
public class VampireNumber {

    public static void main(String args[]) {

        // scan only the ranges that have an even number of digits
        // for instance: 10 .. 99, 1000 .. 9999 etc
        long countVamps = 0, start = 10, tens = 10;
        outer:
        for (int numDigits = 2; numDigits <= 18; numDigits += 2) {
            long end = start * 10;
            for (long i = start; i < end; i++) {
                if (countFangs(i, tens) > 0) {
                    if (++countVamps >= 26)
                        break outer;
                }
            }
            start *= 100;
            tens *= 10;
        }
        System.out.println();

        long[] bigs = {16758243290880L, 24959017348650L,
            14593825548650L};

        for (long b : bigs)
            countFangs(b, 10000000L);
    }

    private static int countFangs(long n, long tens) {
        int countFangs = 0;

        // limit the search space for factors (as in C example)
        long lo = Math.max(tens / 10, (n + tens - 2) / (tens - 1));
        long hi = Math.min(n / lo, (long) Math.sqrt(n));

        long nTally = tallyDigits(n);

        for (long a = lo; a <= hi; a++) {
            long b = n / a;

            if (a * b != n)
                continue;

            // check for mod 9 congruence
            if (n % 9 != (a + b) % 9)
                continue;

            if (a % 10 == 0 && b % 10 == 0)
                continue;

            if (nTally == tallyDigits(a) + tallyDigits(b)) {
                if (countFangs == 0)
                    System.out.printf("\n%d : ", n);
                System.out.printf("[%d, %d]", a, b);
                countFangs++;
            }
        }
        return countFangs;
    }

    // sum to a unique number to represent set of digits (as in C example)
    private static long tallyDigits(long n) {
        long total = 0;
        while (n > 0) {
            total += 1L << ((n % 10) * 6);
            n /= 10;
        }
        return total;
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division

import math
from operator import mul
from itertools import product
from functools import reduce


def fac(n):
    '''\
    return the prime factors for n
    >>> fac(600)
    [5, 5, 3, 2, 2, 2]
    >>> fac(1000)
    [5, 5, 5, 2, 2, 2]
    >>>  
    '''
    step = lambda x: 1 + x*4 - (x//2)*2
    maxq = int(math.floor(math.sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    res = []
    if q <= maxq:
        res.extend(fac(n//q))
        res.extend(fac(q)) 
    else: res=[n]
    return res

def fact(n):
    '''\
    return the prime factors and their multiplicities for n
    >>> fact(600)
    [(2, 3), (3, 1), (5, 2)]
    >>> fact(1000)
    [(2, 3), (5, 3)]
    >>> 
    '''
    res = fac(n)
    return [(c, res.count(c)) for c in set(res)]

def divisors(n):
    'Returns all the divisors of n'
    factors = fact(n)   # [(primefactor, multiplicity), ...]
    primes, maxpowers = zip(*factors)
    powerranges = (range(m+1) for m in maxpowers)
    powers = product(*powerranges)
    return (
        reduce(mul,
               (prime**power for prime, power in zip(primes, powergroup)),
               1)
        for powergroup in powers)
    
def vampire(n):
    fangsets = set( frozenset([d, n//d])
                    for d in divisors(n)
                    if (len(str(d)) == len(str(n))/2.
                        and sorted(str(d) + str(n//d)) == sorted(str(n))
                        and (str(d)[-1] == 0) + (str(n//d)[-1] == 0) <=1) )
    return sorted(tuple(sorted(fangs)) for fangs in fangsets)
    

if __name__ == '__main__':
    print('First 25 vampire numbers')
    count = n = 0
    while count <25:
        n += 1
        fangpairs = vampire(n)
        if fangpairs:
            count += 1
            print('%i: %r' % (n, fangpairs))
    print('\nSpecific checks for fangpairs')
    for n in (16758243290880, 24959017348650, 14593825548650):
        fangpairs = vampire(n)
        print('%i: %r' % (n, fangpairs))

```

### python_code_2.txt
```python
from math import sqrt
from itertools import imap, ifilter, islice, count

def factor_pairs(n):
    return ((x, n // x) for x in xrange(2, int(sqrt(n))) if n % x == 0)

def fangs(n):
    dlen = lambda x: len(str(x))
    half = dlen(n) // 2
    digits = lambda (x, y): sorted(str(x) + str(y))
    halvesQ = lambda xs: all(y == half for y in imap(dlen, xs))
    dn = sorted(str(n))
    return [p for p in factor_pairs(n) if halvesQ(p) and dn==digits(p)]

def vampiricQ(n):
    fn = fangs(n)
    return (n, fn) if fn else None

for v in islice(ifilter(None, imap(vampiricQ, count())), 0, 25):
    print v

for n in [16758243290880, 24959017348650, 14593825548650]:
    print vampiricQ(n) or str(n) + " is not vampiric."

```

