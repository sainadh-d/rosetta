# Attractive numbers

## Task Link
[Rosetta Code - Attractive numbers](https://rosettacode.org/wiki/Attractive_numbers)

## Java Code
### java_code_1.txt
```java
public class Attractive {

    static boolean is_prime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        if (n % 3 == 0) return n == 3;
        int d = 5;
        while (d *d <= n) {
            if (n % d == 0) return false;
            d += 2;
            if (n % d == 0) return false;
            d += 4;
        }
        return true;
    }

    static int count_prime_factors(int n) {
        if (n == 1) return 0;
        if (is_prime(n)) return 1;
        int count = 0, f = 2;
        while (true) {
            if (n % f == 0) {
                count++;
                n /= f;
                if (n == 1) return count;
                if (is_prime(n)) f = n;
            }
            else if (f >= 3) f += 2;
            else f = 3;
        }
    }

    public static void main(String[] args) {
        final int max = 120;
        System.out.printf("The attractive numbers up to and including %d are:\n", max);
        for (int i = 1, count = 0; i <= max; ++i) {
            int n = count_prime_factors(i);
            if (is_prime(n)) {
                System.out.printf("%4d", i);
                if (++count % 20 == 0) System.out.println();
            }
        }
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
from sympy import sieve # library for primes

def get_pfct(n): 
	i = 2; factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return len(factors) 

sieve.extend(110) # first 110 primes...
primes=sieve._list

pool=[]

for each in xrange(0,121):
	pool.append(get_pfct(each))

for i,each in enumerate(pool):
	if each in primes:
		print i,

```

### python_code_2.txt
```python
'''Attractive numbers'''

from itertools import chain, count, takewhile
from functools import reduce


# attractiveNumbers :: () -> [Int]
def attractiveNumbers():
    '''A non-finite stream of attractive numbers.
       (OEIS A063989)
    '''
    return filter(
        compose(
            isPrime,
            len,
            primeDecomposition
        ),
        count(1)
    )


# TEST ----------------------------------------------------
def main():
    '''Attractive numbers drawn from the range [1..120]'''
    for row in chunksOf(15)(list(
            takewhile(
                lambda x: 120 >= x,
                attractiveNumbers()
            )
    )):
        print(' '.join(map(
            compose(justifyRight(3)(' '), str),
            row
        )))


# GENERAL FUNCTIONS ---------------------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    return lambda x: reduce(
        lambda a, f: f(a),
        fs[::-1], x
    )


# We only need light implementations
# of prime functions here:

# primeDecomposition :: Int -> [Int]
def primeDecomposition(n):
    '''List of integers representing the
       prime decomposition of n.
    '''
    def go(n, p):
        return [p] + go(n // p, p) if (
            0 == n % p
        ) else []
    return list(chain.from_iterable(map(
        lambda p: go(n, p) if isPrime(p) else [],
        range(2, 1 + n)
    )))


# isPrime :: Int -> Bool
def isPrime(n):
    '''True if n is prime.'''
    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    return not any(map(
        lambda x: 0 == n % x or 0 == n % (2 + x),
        range(5, 1 + int(n ** 0.5), 6)
    ))


# justifyRight :: Int -> Char -> String -> String
def justifyRight(n):
    '''A string padded at left to length n,
       using the padding character c.
    '''
    return lambda c: lambda s: s.rjust(n, c)


# MAIN ---
if __name__ == '__main__':
    main()

```

