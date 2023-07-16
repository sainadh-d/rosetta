# Tau function

## Task Link
[Rosetta Code - Tau function](https://rosettacode.org/wiki/Tau_function)

## Java Code
### java_code_1.txt
```java
public class TauFunction {
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
        final int limit = 100;
        System.out.printf("Count of divisors for the first %d positive integers:\n", limit);
        for (long n = 1; n <= limit; ++n) {
            System.out.printf("%3d", divisorCount(n));
            if (n % 20 == 0) {
                System.out.println();
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def factorize(n):
    assert(isinstance(n, int))
    if n < 0: 
        n = -n 
    if n < 2: 
        return 
    k = 0 
    while 0 == n%2: 
        k += 1 
        n //= 2 
    if 0 < k: 
        yield (2,k) 
    p = 3 
    while p*p <= n: 
        k = 0 
        while 0 == n%p: 
            k += 1 
            n //= p 
        if 0 < k: 
            yield (p,k)
        p += 2 
    if 1 < n: 
        yield (n,1) 

def tau(n): 
    assert(n != 0) 
    ans = 1 
    for (p,k) in factorize(n): 
        ans *= 1 + k
    return ans

if __name__ == "__main__":
    print(*map(tau, range(1, 101)))

```

### python_code_2.txt
```python
def tau(n):
    assert(isinstance(n, int) and 0 < n)
    t = (n - 1 ^ n).bit_length()
    n >>= t - 1
    p = 3
    while p * p <= n:
        a = t
        while n % p == 0:
            t += a
            n //= p
        p += 2
    if n != 1:
        t += t
    return t

if __name__ == "__main__":
    print(*map(tau, range(1, 101)))

```

### python_code_3.txt
```python
'''The number of divisors of n'''

from itertools import count, islice
from math import floor, sqrt


# oeisA000005 :: [Int]
def oeisA000005():
    '''tau(n) (also called d(n) or sigma_0(n)),
       the number of divisors of n.
    '''
    return map(tau, count(1))


# tau :: Int -> Int
def tau(n):
    '''The number of divisors of n.
    '''
    return len(divisors(n))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''The first 100 terms of OEIS A000005.
       (Shown in rows of 10)
    '''
    terms = take(100)(
        oeisA000005()
    )
    columnWidth = 1 + len(str(max(terms)))

    print(
        '\n'.join(
            ''.join(
                str(term).rjust(columnWidth)
                for term in row
            )
            for row in chunksOf(10)(terms)
        )
    )


# ----------------------- GENERIC ------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    def go(xs):
        return [
            xs[i:n + i] for i in range(0, len(xs), n)
        ] if 0 < n else None
    return go


# divisors :: Int -> [Int]
def divisors(n):
    '''List of all divisors of n including n itself.
    '''
    root = floor(sqrt(n))
    lows = [x for x in range(1, 1 + root) if 0 == n % x]
    return lows + [n // x for x in reversed(lows)][
        (1 if n == (root * root) else 0):
    ]


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


# MAIN ---
if __name__ == '__main__':
    main()

```

