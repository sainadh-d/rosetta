# Tau number

## Task Link
[Rosetta Code - Tau number](https://rosettacode.org/wiki/Tau_number)

## Java Code
### java_code_1.txt
```java
public class Tau {
    private static long divisorCount(long n) {
        long total = 1;
        // Deal with powers of 2 first
        for (; (n & 1) == 0; n >>= 1) {
            ++total;
        }
        // Odd prime factors up to the square root
        for (long p = 3; p * p <= n; p += 2) {
            long count = 1;
            for (; n % p == 0; n /= p) {
                ++count;
            }
            total *= count;
        }
        // If n > 1 then it's prime
        if (n > 1) {
            total *= 2;
        }
        return total;
    }

    public static void main(String[] args) {
        final long limit = 100;
        System.out.printf("The first %d tau numbers are:%n", limit);
        long count = 0;
        for (long n = 1; count < limit; ++n) {
            if (n % divisorCount(n) == 0) {
                System.out.printf("%6d", n);
                ++count;
                if (count % 10 == 0) {
                    System.out.println();
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def tau(n):
    assert(isinstance(n, int) and 0 < n)
    ans, i, j = 0, 1, 1
    while i*i <= n:
        if 0 == n%i:
            ans += 1
            j = n//i
            if j != i:
                ans += 1
        i += 1
    return ans

def is_tau_number(n):
    assert(isinstance(n, int))
    if n <= 0:
        return False
    return 0 == n%tau(n)

if __name__ == "__main__":
    n = 1
    ans = []
    while len(ans) < 100:
        if is_tau_number(n):
            ans.append(n)
        n += 1
    print(ans)

```

### python_code_2.txt
```python
'''Tau numbers'''

from operator import mul
from math import floor, sqrt
from functools import reduce
from itertools import (
    accumulate, chain, count,
    groupby, islice, product
)


# tauNumbers :: Generator [Int]
def tauNumbers():
    '''Positive integers divisible by the
       count of their positive divisors.
    '''
    return (
        n for n in count(1)
        if 0 == n % len(divisors(n))
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''The first hundred Tau numbers.
    '''
    xs = take(100)(
        tauNumbers()
    )
    w = len(str(xs[-1]))
    print('\n'.join([
        ' '.join([
            str(cell).rjust(w, ' ') for cell in row
        ])
        for row in chunksOf(10)(xs)
    ]))


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
            accumulate(chain([1], x), mul)
        )]
    return sorted(
        reduce(go, [
            list(g) for _, g
            in groupby(primeFactors(n))
        ], [1])
    ) if 1 < n else [1]


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

