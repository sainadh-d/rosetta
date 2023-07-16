# Fermat numbers

## Task Link
[Rosetta Code - Fermat numbers](https://rosettacode.org/wiki/Fermat_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class FermatNumbers {

    public static void main(String[] args) {
        System.out.println("First 10 Fermat numbers:");
        for ( int i = 0 ; i < 10 ; i++ ) {
            System.out.printf("F[%d] = %s\n", i, fermat(i));
        }
        System.out.printf("%nFirst 12 Fermat numbers factored:%n");
        for ( int i = 0 ; i < 13 ; i++ ) {
            System.out.printf("F[%d] = %s\n", i, getString(getFactors(i, fermat(i))));
        }
    }
    
    private static String getString(List<BigInteger> factors) {
        if ( factors.size() == 1 ) {
            return factors.get(0) + " (PRIME)";
        }
        return factors.stream().map(v -> v.toString()).map(v -> v.startsWith("-") ? "(C" + v.replace("-", "") + ")" : v).collect(Collectors.joining(" * "));
    }

    private static Map<Integer, String> COMPOSITE = new HashMap<>();
    static {
        COMPOSITE.put(9, "5529");
        COMPOSITE.put(10, "6078");
        COMPOSITE.put(11, "1037");
        COMPOSITE.put(12, "5488");
        COMPOSITE.put(13, "2884");
    }

    private static List<BigInteger> getFactors(int fermatIndex, BigInteger n) {
        List<BigInteger> factors = new ArrayList<>();
        BigInteger factor = BigInteger.ONE;
        while ( true ) {
            if ( n.isProbablePrime(100) ) {
                factors.add(n);
                break;
            }
            else {
                if ( COMPOSITE.containsKey(fermatIndex) ) {
                    String stop = COMPOSITE.get(fermatIndex);
                    if ( n.toString().startsWith(stop) ) {
                        factors.add(new BigInteger("-" + n.toString().length()));
                        break;
                    }
                }
                factor = pollardRhoFast(n);
                if ( factor.compareTo(BigInteger.ZERO) == 0 ) {
                    factors.add(n);
                    break;
                }
                else {
                    factors.add(factor);
                    n = n.divide(factor);
                }
            }
        }
        return factors;
    }
    
    private static final BigInteger TWO = BigInteger.valueOf(2);
    
    private static BigInteger fermat(int n) {
        return TWO.pow((int)Math.pow(2, n)).add(BigInteger.ONE);
    }
        
    //  See:  https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    @SuppressWarnings("unused")
    private static BigInteger pollardRho(BigInteger n) {
        BigInteger x = BigInteger.valueOf(2);
        BigInteger y = BigInteger.valueOf(2);
        BigInteger d = BigInteger.ONE;
        while ( d.compareTo(BigInteger.ONE) == 0 ) {
            x = pollardRhoG(x, n);
            y = pollardRhoG(pollardRhoG(y, n), n);
            d = x.subtract(y).abs().gcd(n);
        }
        if ( d.compareTo(n) == 0 ) {
            return BigInteger.ZERO;
        }
        return d;
    }
    
    //  Includes Speed Up of 100 multiples and 1 GCD, instead of 100 multiples and 100 GCDs.
    //  See Variants section of Wikipedia article.
    //  Testing F[8] = 1238926361552897 * Prime 
    //    This variant = 32 sec.
    //    Standard algorithm = 107 sec.
    private static BigInteger pollardRhoFast(BigInteger n) {
        long start = System.currentTimeMillis();
        BigInteger x = BigInteger.valueOf(2);
        BigInteger y = BigInteger.valueOf(2);
        BigInteger d = BigInteger.ONE;
        int count = 0;
        BigInteger z = BigInteger.ONE;
        while ( true ) {
            x = pollardRhoG(x, n);
            y = pollardRhoG(pollardRhoG(y, n), n);
            d = x.subtract(y).abs();
            z = z.multiply(d).mod(n);
            count++;
            if ( count == 100 ) {
                d = z.gcd(n);
                if ( d.compareTo(BigInteger.ONE) != 0 ) {
                    break;
                }
                z = BigInteger.ONE;
                count = 0;
            }
        }
        long end = System.currentTimeMillis();
        System.out.printf("    Pollard rho try factor %s elapsed time = %d ms (factor = %s).%n", n, (end-start), d);
        if ( d.compareTo(n) == 0 ) {
            return BigInteger.ZERO;
        }
        return d;
    }

    private static BigInteger pollardRhoG(BigInteger x, BigInteger n) {
        return x.multiply(x).add(BigInteger.ONE).mod(n);
    }

}

```

## Python Code
### python_code_1.txt
```python
def factors(x):
    factors = []
    i = 2
    s = int(x ** 0.5)
    while i < s:
        if x % i == 0:
            factors.append(i)
            x = int(x / i)
            s = int(x ** 0.5)
        i += 1
    factors.append(x)
    return factors

print("First 10 Fermat numbers:")
for i in range(10):
    fermat = 2 ** 2 ** i + 1
    print("F{} = {}".format(chr(i + 0x2080) , fermat))

print("\nFactors of first few Fermat numbers:")
for i in range(10):
    fermat = 2 ** 2 ** i + 1
    fac = factors(fermat)
    if len(fac) == 1:
        print("F{} -> IS PRIME".format(chr(i + 0x2080)))
    else:
        print("F{} -> FACTORS: {}".format(chr(i + 0x2080), fac))

```

### python_code_2.txt
```python
'''Fermat numbers'''

from itertools import count, islice
from math import floor, sqrt


# fermat :: Int -> Int
def fermat(n):
    '''Nth Fermat number.
       Nth term of OEIS A000215.
    '''
    return 1 + (2 ** (2 ** n))


# fermats :: () -> [Int]
def fermats():
    '''Non-finite series of Fermat numbers.
       OEIS A000215.
    '''
    return (fermat(x) for x in enumFrom(0))


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''First 10 Fermats, and factors of first 7.'''

    print(
        fTable('First ten Fermat numbers:')(str)(str)(
            fermat
        )(enumFromTo(0)(9))
    )

    print(
        fTable('\n\nFactors of first seven:')(str)(
            lambda xs: repr(xs) if 1 < len(xs) else '(prime)'
        )(primeFactors)(
            take(7)(fermats())
        )
    )


# -------------------------DISPLAY-------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# -------------------------GENERIC-------------------------

# enumFrom :: Enum a => a -> [a]
def enumFrom(x):
    '''A non-finite stream of enumerable values,
       starting from the given value.
    '''
    return count(x) if isinstance(x, int) else (
        map(chr, count(ord(x)))
    )


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    def go(n):
        return list(range(m, 1 + n))
    return lambda n: go(n)


# primeFactors :: Int -> [Int]
def primeFactors(n):
    '''A list of the prime factors of n.
    '''
    def f(qr):
        r = qr[1]
        return step(r), 1 + r

    def step(x):
        return 1 + (x << 2) - ((x >> 1) << 1)

    def go(x):
        root = floor(sqrt(x))

        def p(qr):
            q = qr[0]
            return root < q or 0 == (x % q)

        q = until(p)(f)(
            (2 if 0 == x % 2 else 3, 1)
        )[0]
        return [x] if q > root else [q] + go(x // q)

    return go(n)


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


# MAIN ---
if __name__ == '__main__':
    main()

```

