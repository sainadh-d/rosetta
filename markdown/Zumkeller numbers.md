# Zumkeller numbers

## Task Link
[Rosetta Code - Zumkeller numbers](https://rosettacode.org/wiki/Zumkeller_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ZumkellerNumbers {

    public static void main(String[] args) {
        int n = 1;
        System.out.printf("First 220 Zumkeller numbers:%n");
        for ( int count = 1 ; count <= 220 ; n += 1 ) {
            if ( isZumkeller(n) ) {
                System.out.printf("%3d  ", n);
                if ( count % 20 == 0 ) {
                    System.out.printf("%n");
                }
                count++;
            }
        }
        
        n = 1;
        System.out.printf("%nFirst 40 odd Zumkeller numbers:%n");
        for ( int count = 1 ; count <= 40 ; n += 2 ) {
            if ( isZumkeller(n) ) {
                System.out.printf("%6d", n);
                if ( count % 10 == 0 ) {
                    System.out.printf("%n");
                }
                count++;
            }
        }
        
        n = 1;
        System.out.printf("%nFirst 40 odd Zumkeller numbers that do not end in a 5:%n");
        for ( int count = 1 ; count <= 40 ; n += 2 ) {
            if ( n % 5 != 0 && isZumkeller(n) ) {
                System.out.printf("%8d", n);
                if ( count % 10 == 0 ) {
                    System.out.printf("%n");
                }
                count++;
            }
        }

    }
    
    private static boolean isZumkeller(int n) {
        //  numbers congruent to 6 or 12 modulo 18 are Zumkeller numbers
        if ( n % 18 == 6 || n % 18 == 12 ) {
            return true;
        }
        
        List<Integer> divisors = getDivisors(n);        
        int divisorSum = divisors.stream().mapToInt(i -> i.intValue()).sum();
        
        //  divisor sum cannot be odd
        if ( divisorSum % 2 == 1 ) {
            return false;
        }
        
        // numbers where n is odd and the abundance is even are Zumkeller numbers
        int abundance = divisorSum - 2 * n;
        if ( n % 2 == 1 && abundance > 0 && abundance % 2 == 0 ) {
            return true;
        }
        
        Collections.sort(divisors);
        int j = divisors.size() - 1;
        int sum = divisorSum/2;
        
        //  Largest divisor larger than sum - then cannot partition and not Zumkeller number
        if ( divisors.get(j) > sum ) {
            return false;
        }
        
        return canPartition(j, divisors, sum, new int[2]);
    }
    
    private static boolean canPartition(int j, List<Integer> divisors, int sum, int[] buckets) {
        if ( j < 0 ) {
            return true;
        }
        for ( int i = 0 ; i < 2 ; i++ ) {
            if ( buckets[i] + divisors.get(j) <= sum ) {
                buckets[i] += divisors.get(j);
                if ( canPartition(j-1, divisors, sum, buckets) ) {
                    return true;
                }
                buckets[i] -= divisors.get(j);
            }
            if( buckets[i] == 0 ) {
                break;
            }
        }
        return false;
    }
    
    private static final List<Integer> getDivisors(int number) {
        List<Integer> divisors = new ArrayList<Integer>();
        long sqrt = (long) Math.sqrt(number);
        for ( int i = 1 ; i <= sqrt ; i++ ) {
            if ( number % i == 0 ) {
                divisors.add(i);
                int div = number / i;
                if ( div != i ) {
                    divisors.add(div);
                }
            }
        }
        return divisors;
    }

}

```

## Python Code
### python_code_1.txt
```python
from sympy import divisors

from sympy.combinatorics.subsets import Subset

def isZumkeller(n):
    d = divisors(n)
    s = sum(d)
    if not s % 2 and max(d) <= s/2:
        for x in range(1, 2**len(d)):
            if sum(Subset.unrank_binary(x, d).subset) == s/2:
                return True

    return False



def printZumkellers(N, oddonly=False):
    nprinted = 0
    for n in range(1, 10**5):
        if (oddonly == False or n % 2) and isZumkeller(n):
            print(f'{n:>8}', end='')
            nprinted += 1
            if nprinted % 10 == 0:
                print()
            if nprinted >= N:
                return


print("220 Zumkeller numbers:")
printZumkellers(220)
print("\n\n40 odd Zumkeller numbers:")
printZumkellers(40, True)

```

### python_code_2.txt
```python
'''Zumkeller numbers'''

from itertools import (
    accumulate, chain, count, groupby, islice, product
)
from functools import reduce
from math import floor, sqrt
import operator


# ---------------------- ZUMKELLER -----------------------

# isZumkeller :: Int -> Bool
def isZumkeller(n):
    '''True if there exists a disjoint partition
       of the divisors of m, such that the two sets have
       the same sum.
       (In other words, if n is in OEIS A083207)
    '''
    ds = divisors(n)
    m = sum(ds)
    if even(m):
        half = m // 2
        return half in ds or (
            all(map(ge(half), ds)) and (
                summable(half, ds)
            )
        )
    else:
        return False


# summable :: Int -> [Int] -> Bool
def summable(x, xs):
    '''True if any subset of the sorted
       list xs sums to x.
    '''
    if xs:
        if x in xs:
            return True
        else:
            t = xs[1:]
            return summable(x - xs[0], t) or summable(x, t)
    else:
        return False


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 220 Zumkeller numbers,
       and first 40 odd Zumkellers.
    '''

    tenColumns = tabulated(10)

    print('First 220 Zumkeller numbers:\n')
    print(tenColumns(
        take(220)(
            filter(isZumkeller, count(1))
        )
    ))
    print('\nFirst 40 odd Zumkeller numbers:\n')
    print(tenColumns(
        take(40)(
            filter(isZumkeller, enumFromThen(1)(3))
        )
    ))


# ---------------------- TABULATION ----------------------

# tabulated :: Int -> [a] -> String
def tabulated(nCols):
    '''String representation of a list
       of values as rows of n columns.
    '''
    def go(xs):
        ts = [str(x) for x in xs]
        w = 1 + max(len(x) for x in ts)
        return '\n'.join([
            ''.join(row) for row
            in chunksOf(nCols)([
                t.rjust(w, ' ') for t in ts
            ])
        ])
    return go


# ----------------------- GENERIC ------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


# divisors :: Int -> [Int]
def divisors(n):
    '''The ordered divisors of n.
    '''
    def go(a, x):
        return [a * b for a, b in product(
            a,
            accumulate(chain([1], x), operator.mul)
        )]
    return sorted(
        reduce(go, [
            list(g) for _, g in groupby(primeFactors(n))
        ], [1])
    ) if 1 < n else [1]


# enumFromThen :: Int -> Int -> [Int]
def enumFromThen(m):
    '''A non-finite stream of integers
       starting at m, and continuing
       at the interval between m and n.
    '''
    return lambda n: count(m, n - m)


# even :: Int -> Bool
def even(x):
    '''True if x is an integer
       multiple of two.
    '''
    return 0 == x % 2


# ge :: Eq a => a -> a -> Bool
def ge(a):
    def go(b):
        return operator.ge(a, b)
    return go


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
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

