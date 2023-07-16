# Catalan numbers

## Task Link
[Rosetta Code - Catalan numbers](https://rosettacode.org/wiki/Catalan_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CatlanNumbers {

    public static void main(String[] args) {
        Catlan f1 = new Catlan1();
        Catlan f2 = new Catlan2();
        Catlan f3 = new Catlan3();
        System.out.printf("           Formula 1     Formula 2     Formula 3%n");
        for ( int n = 0 ; n <= 15 ; n++ ) {
             System.out.printf("C(%2d) = %,12d  %,12d  %,12d%n", n, f1.catlin(n), f2.catlin(n), f3.catlin(n));
        }
    }
    
    private static interface Catlan {
        public BigInteger catlin(long n);
    }
    
    private static class Catlan1 implements Catlan {

        //  C(n) = (2n)! / (n+1)!n!
        @Override
        public BigInteger catlin(long n) {
            List<Long> numerator = new ArrayList<>();
            for ( long k = n+2 ; k <= 2*n ; k++ ) {
                numerator.add(k);
            }
            
            List<Long> denominator = new ArrayList<>();
            for ( long k = 2 ; k <= n ; k++ ) {
                denominator.add(k);
            }
            
            for ( int i = numerator.size()-1 ; i >= 0  ; i-- ) {
                for ( int j = denominator.size()-1 ; j >= 0  ; j-- ) {
                    if ( denominator.get(j) == 1 ) {
                        continue;
                    }
                    if ( numerator.get(i) % denominator.get(j) == 0 ) {
                        long val = numerator.get(i) / denominator.get(j);
                        numerator.set(i, val);
                        denominator.remove(denominator.get(j));
                        if ( val == 1 ) {
                            break;
                        }
                    }
                }
            }

            BigInteger catlin = BigInteger.ONE;
            for ( int i = 0 ; i < numerator.size() ; i++ ) {
                catlin = catlin.multiply(BigInteger.valueOf(numerator.get(i)));
            }
            for ( int i = 0 ; i < denominator.size() ; i++ ) {
                catlin = catlin.divide(BigInteger.valueOf(denominator.get(i)));
            }
            return catlin;
        }        
    }
    
    private static class Catlan2 implements Catlan {

        private static Map<Long,BigInteger> CACHE = new HashMap<>();
        static {
            CACHE.put(0L, BigInteger.ONE);
        }
        
        //  C(0) = 1, C(n+1) = sum(i=0..n,C(i)*C(n-i))
        @Override
        public BigInteger catlin(long n) {
            if ( CACHE.containsKey(n) ) {
                return CACHE.get(n);
            }
            BigInteger catlin = BigInteger.ZERO;
            n--;
            for ( int i = 0 ; i <= n ; i++ ) {
                //System.out.println("n = " + n + ", i = " + i + ", n-i = " + (n-i));
                catlin = catlin.add(catlin(i).multiply(catlin(n-i)));
            }
            CACHE.put(n+1, catlin);
            return catlin;
        }
    }
    
    private static class Catlan3 implements Catlan {

        private static Map<Long,BigInteger> CACHE = new HashMap<>();
        static {
            CACHE.put(0L, BigInteger.ONE);
        }
        
        //  C(0) = 1, C(n+1) = 2*(2n-1)*C(n-1)/(n+1)
        @Override
        public BigInteger catlin(long n) {
            if ( CACHE.containsKey(n) ) {
                return CACHE.get(n);
            }
            BigInteger catlin = BigInteger.valueOf(2).multiply(BigInteger.valueOf(2*n-1)).multiply(catlin(n-1)).divide(BigInteger.valueOf(n+1));
            CACHE.put(n, catlin);
            return catlin;
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
from math import factorial
import functools


def memoize(func):
    cache = {}

    def memoized(key):
        # Returned, new, memoized version of decorated function
        if key not in cache:
            cache[key] = func(key)
        return cache[key]
    return functools.update_wrapper(memoized, func)


@memoize
def fact(n):
    return factorial(n)


def cat_direct(n):
    return fact(2 * n) // fact(n + 1) // fact(n)


@memoize
def catR1(n):
    return 1 if n == 0 else (
        sum(catR1(i) * catR1(n - 1 - i) for i in range(n))
    )


@memoize
def catR2(n):
    return 1 if n == 0 else (
        ((4 * n - 2) * catR2(n - 1)) // (n + 1)
    )


if __name__ == '__main__':
    def pr(results):
        fmt = '%-10s %-10s %-10s'
        print((fmt % tuple(c.__name__ for c in defs)).upper())
        print(fmt % (('=' * 10,) * 3))
        for r in zip(*results):
            print(fmt % r)

    defs = (cat_direct, catR1, catR2)
    results = [tuple(c(i) for i in range(15)) for c in defs]
    pr(results)

```

### python_code_2.txt
```python
'''Catalan numbers'''

from itertools import accumulate, chain, count, islice


# catalans3 :: [Int]
def catalans3():
    '''Infinite sequence of Catalan numbers
    '''
    def go(c, n):
        return 2 * c * pred(2 * n) // succ(n)

    return accumulate(
        chain([1], count(1)), go
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Catalan numbers, definition 3'''
    print("Catalans 1-15:\n")
    print(
        '\n'.join([
            f'{n:>10}' for n
            in islice(catalans3(), 15)
        ])
    )


# ----------------------- GENERIC ------------------------

# pred :: Int -> Int
def pred(n):
    '''Predecessor function'''
    return n - 1


# succ :: Int -> Int
def succ(n):
    '''Successor function'''
    return 1 + n


# MAIN ---
if __name__ == '__main__':
    main()

```

