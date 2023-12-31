# Sequence: smallest number with exactly n divisors

## Task Link
[Rosetta Code - Sequence: smallest number with exactly n divisors](https://rosettacode.org/wiki/Sequence:_smallest_number_with_exactly_n_divisors)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class OEIS_A005179 {

    static int count_divisors(int n) {
        int count = 0;
        for (int i = 1; i * i <= n; ++i) {
            if (n % i == 0) {
                if (i == n / i)
                    count++;
                else
                    count += 2;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        final int max = 15;
        int[] seq = new int[max];
        System.out.printf("The first %d terms of the sequence are:\n", max);
        for (int i = 1, n = 0; n < max; ++i) {
            int k = count_divisors(i);
            if (k <= max && seq[k - 1] == 0) {        
                seq[k- 1] = i;
                n++;
            }
        }
        System.out.println(Arrays.toString(seq));
    }
}

```

## Python Code
### python_code_1.txt
```python
def divisors(n):
    divs = [1]
    for ii in range(2, int(n ** 0.5) + 3):
        if n % ii == 0:
            divs.append(ii)
            divs.append(int(n / ii))
    divs.append(n)
    return list(set(divs))


def sequence(max_n=None):
    n = 0
    while True:
        n += 1
        ii = 0
        if max_n is not None:
            if n > max_n:
                break
        while True:
            ii += 1
            if len(divisors(ii)) == n:
                yield ii
                break


if __name__ == '__main__':
    for item in sequence(15):
        print(item)

```

### python_code_2.txt
```python
'''Smallest number with exactly n divisors'''

from itertools import accumulate, chain, count, groupby, islice, product
from functools import reduce
from math import sqrt, floor
from operator import mul


# a005179 :: () -> [Int]
def a005179():
    '''Integer sequence: smallest number with exactly n divisors.'''
    return (
        next(
            x for x in count(1)
            if n == 1 + len(properDivisors(x))
        ) for n in count(1)
    )


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''First 15 terms of a005179'''
    print(main.__doc__ + ':\n')
    print(
        take(15)(
            a005179()
        )
    )


# -------------------------GENERIC-------------------------

# properDivisors :: Int -> [Int]
def properDivisors(n):
    '''The ordered divisors of n, excluding n itself.
    '''
    def go(a, x):
        return [a * b for a, b in product(
            a,
            accumulate(chain([1], x), mul)
        )]
    return sorted(
        reduce(go, [
            list(g) for _, g in groupby(primeFactors(n))
        ], [1])
    )[:-1] if 1 < n else []


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

