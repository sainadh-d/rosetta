# Smith numbers

## Task Link
[Rosetta Code - Smith numbers](https://rosettacode.org/wiki/Smith_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class SmithNumbers {

    public static void main(String[] args) {
        for (int n = 1; n < 10_000; n++) {
            List<Integer> factors = primeFactors(n);
            if (factors.size() > 1) {
                int sum = sumDigits(n);
                for (int f : factors)
                    sum -= sumDigits(f);
                if (sum == 0)
                    System.out.println(n);
            }
        }
    }

    static List<Integer> primeFactors(int n) {
        List<Integer> result = new ArrayList<>();

        for (int i = 2; n % i == 0; n /= i)
            result.add(i);

        for (int i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                result.add(i);
                n /= i;
            }
        }

        if (n != 1)
            result.add(n);

        return result;
    }

    static int sumDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += (n % 10);
            n /= 10;
        }
        return sum;
    }
}

```

## Python Code
### python_code_1.txt
```python
from sys import stdout


def factors(n):
    rt = []
    f = 2
    if n == 1:
        rt.append(1);
    else:
        while 1:
            if 0 == ( n % f ):
                rt.append(f);
                n //= f
                if n == 1:
                    return rt
            else:
                f += 1
    return rt


def sum_digits(n):
    sum = 0
    while n > 0:
        m = n % 10
        sum += m
        n -= m
        n //= 10

    return sum


def add_all_digits(lst):
    sum = 0
    for i in range (len(lst)):
        sum += sum_digits(lst[i])

    return sum


def list_smith_numbers(cnt):
    for i in range(4, cnt):
        fac = factors(i)
        if len(fac) > 1:
            if sum_digits(i) == add_all_digits(fac):
                stdout.write("{0} ".format(i) )

# entry point
list_smith_numbers(10_000)

```

### python_code_2.txt
```python
'''Smith numbers'''

from itertools import dropwhile
from functools import reduce
from math import floor, sqrt


# isSmith :: Int -> Bool
def isSmith(n):
    '''True if n is a Smith number.'''
    pfs = primeFactors(n)
    return (1 < len(pfs) or n != pfs[0]) and (
        sumDigits(n) == reduce(
            lambda a, x: a + sumDigits(x),
            pfs, 0
        )
    )


# primeFactors :: Int -> [Int]
def primeFactors(x):
    '''List of prime factors of x'''
    def go(n):
        fs = list(dropwhile(
            mod(n),
            range(2, 1 + floor(sqrt(n)))
        ))[0:1]

        return fs + go(floor(n / fs[0])) if fs else [n]
    return go(x)


# sumDigits :: Int -> Int
def sumDigits(n):
    '''The sum of the decimal digits of n'''
    def f(x):
        return Just(divmod(x, 10)) if x else Nothing()
    return sum(unfoldl(f)(n))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Count and samples of Smith numbers below 10k'''

    lowSmiths = [x for x in range(2, 10000) if isSmith(x)]
    lowSmithCount = len(lowSmiths)

    print('\n'.join([
        'Count of Smith Numbers below 10k:',
        str(lowSmithCount),
        '\nFirst 15 Smith Numbers:',
        ' '.join(str(x) for x in lowSmiths[0:15]),
        '\nLast 12 Smith Numbers below 10000:',
        ' '.join(str(x) for x in lowSmiths[lowSmithCount - 12:])
    ]))


# GENERIC -------------------------------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# mod :: Int -> Int -> Int
def mod(n):
    '''n modulo d'''
    return lambda d: n % d


# unfoldl(lambda x: Just(((x - 1), x)) if 0 != x else Nothing())(10)
# -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''Dual to reduce or foldl.
       Where these reduce a list to a summary value, unfoldl
       builds a list from a seed value.
       Where f returns Just(a, b), a is appended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        x, r = v, v
        xs = []
        while True:
            mb = f(x)
            if mb.get('Nothing'):
                return xs
            else:
                x, r = mb.get('Just')
                xs.insert(0, r)
        return xs
    return lambda x: go(x)


# MAIN ---
if __name__ == '__main__':
    main()

```

