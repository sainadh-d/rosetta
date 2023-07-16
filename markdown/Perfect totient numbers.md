# Perfect totient numbers

## Task Link
[Rosetta Code - Perfect totient numbers](https://rosettacode.org/wiki/Perfect_totient_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class PerfectTotientNumbers {

    public static void main(String[] args) {
        computePhi();
        int n = 20;
        System.out.printf("The first %d perfect totient numbers:%n%s%n", n, perfectTotient(n));
    }
    
    private static final List<Integer> perfectTotient(int n) {
        int test = 2;
        List<Integer> results = new ArrayList<Integer>();
        for ( int i = 0 ; i < n ; test++ ) {
            int phiLoop = test;
            int sum = 0;
            do {
                phiLoop = phi[phiLoop];
                sum += phiLoop;
            } while ( phiLoop > 1);
            if ( sum == test ) {
                i++;
                results.add(test);
            }
        }
        return results;
    }

    private static final int max = 100000;
    private static final int[] phi = new int[max+1];

    private static final void computePhi() {
        for ( int i = 1 ; i <= max ; i++ ) {
            phi[i] = i;
        }
        for ( int i = 2 ; i <= max ; i++ ) {
            if (phi[i] < i) continue;
            for ( int j = i ; j <= max ; j += i ) {
                phi[j] -= phi[j] / i;
            }
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
from math import gcd
from functools import lru_cache
from itertools import islice, count

@lru_cache(maxsize=None)
def  φ(n):
    return sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)

def perfect_totient():
    for n0 in count(1):
        parts, n = 0, n0
        while n != 1:
            n = φ(n)
            parts += n
        if parts == n0:
            yield n0
        

if __name__ == '__main__':
    print(list(islice(perfect_totient(), 20)))

```

### python_code_2.txt
```python
'''Perfect totient numbers'''

from functools import lru_cache
from itertools import count, islice
from math import gcd
import operator


# perfectTotients :: () -> [Int]
def perfectTotients():
    '''An unbounded sequence of perfect totients.
       OEIS A082897
    '''
    def p(x):
        return x == 1 + sum(
            iterateUntil(eq(1))(
                phi
            )(x)[1:]
        )
    return filter(p, count(2))


@lru_cache(maxsize=None)
def phi(n):
    '''Euler's totient function.
       The count of integers up to n which
       are relatively prime to n.
    '''
    return len([
        x for x in enumFromTo(1)(n)
        if 1 == gcd(n, x)
    ])


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''First twenty perfect totient numbers'''
    print(
        take(20)(
            perfectTotients()
        )
    )


# GENERIC -------------------------------------------------

# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.
    '''
    return lambda x: lambda y: f(x, y)


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    return lambda n: range(m, 1 + n)


# eq (==) :: Eq a => a -> a -> Bool
eq = curry(operator.eq)
'''True if a and b are comparable and a equals b.'''


# iterateUntil :: (a -> Bool) -> (a -> a) -> a -> [a]
def iterateUntil(p):
    '''A list of the results of repeated
       applications of f, until p matches.
    '''
    def go(f, x):
        vs = []
        v = x
        while True:
            if p(v):
                break
            vs.append(v)
            v = f(v)
        return vs

    return lambda f: lambda x: go(f, x)


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


# MAIN ---
if __name__ == '__main__':
    main()

```

