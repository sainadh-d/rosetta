# Esthetic numbers

## Task Link
[Rosetta Code - Esthetic numbers](https://rosettacode.org/wiki/Esthetic_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class EstheticNumbers {
    interface RecTriConsumer<A, B, C> {
        void accept(RecTriConsumer<A, B, C> f, A a, B b, C c);
    }

    private static boolean isEsthetic(long n, long b) {
        if (n == 0) {
            return false;
        }
        var i = n % b;
        var n2 = n / b;
        while (n2 > 0) {
            var j = n2 % b;
            if (Math.abs(i - j) != 1) {
                return false;
            }
            n2 /= b;
            i = j;
        }
        return true;
    }

    private static void listEsths(long n, long n2, long m, long m2, int perLine, boolean all) {
        var esths = new ArrayList<Long>();
        var dfs = new RecTriConsumer<Long, Long, Long>() {
            public void accept(Long n, Long m, Long i) {
                accept(this, n, m, i);
            }

            @Override
            public void accept(RecTriConsumer<Long, Long, Long> f, Long n, Long m, Long i) {
                if (n <= i && i <= m) {
                    esths.add(i);
                }
                if (i == 0 || i > m) {
                    return;
                }
                var d = i % 10;
                var i1 = i * 10 + d - 1;
                var i2 = i1 + 2;
                if (d == 0) {
                    f.accept(f, n, m, i2);
                } else if (d == 9) {
                    f.accept(f, n, m, i1);
                } else {
                    f.accept(f, n, m, i1);
                    f.accept(f, n, m, i2);
                }
            }
        };

        LongStream.range(0, 10).forEach(i -> dfs.accept(n2, m2, i));

        var le = esths.size();
        System.out.printf("Base 10: %d esthetic numbers between %d and %d:%n", le, n, m);
        if (all) {
            for (int i = 0; i < esths.size(); i++) {
                System.out.printf("%d ", esths.get(i));
                if ((i + 1) % perLine == 0) {
                    System.out.println();
                }
            }
        } else {
            for (int i = 0; i < perLine; i++) {
                System.out.printf("%d ", esths.get(i));
            }
            System.out.println();
            System.out.println("............");
            for (int i = le - perLine; i < le; i++) {
                System.out.printf("%d ", esths.get(i));
            }
        }
        System.out.println();
        System.out.println();
    }

    public static void main(String[] args) {
        IntStream.rangeClosed(2, 16).forEach(b -> {
            System.out.printf("Base %d: %dth to %dth esthetic numbers:%n", b, 4 * b, 6 * b);
            var n = 1L;
            var c = 0L;
            while (c < 6 * b) {
                if (isEsthetic(n, b)) {
                    c++;
                    if (c >= 4 * b) {
                        System.out.printf("%s ", Long.toString(n, b));
                    }
                }
                n++;
            }
            System.out.println();
        });
        System.out.println();

        // the following all use the obvious range limitations for the numbers in question
        listEsths(1000, 1010, 9999, 9898, 16, true);
        listEsths((long) 1e8, 101_010_101, 13 * (long) 1e7, 123_456_789, 9, true);
        listEsths((long) 1e11, 101_010_101_010L, 13 * (long) 1e10, 123_456_789_898L, 7, false);
        listEsths((long) 1e14, 101_010_101_010_101L, 13 * (long) 1e13, 123_456_789_898_989L, 5, false);
        listEsths((long) 1e17, 101_010_101_010_101_010L, 13 * (long) 1e16, 123_456_789_898_989_898L, 4, false);
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import deque
from itertools import dropwhile, islice, takewhile
from textwrap import wrap
from typing import Iterable, Iterator


Digits = str  # Alias for the return type of to_digits()


def esthetic_nums(base: int) -> Iterator[int]:
    """Generate the esthetic number sequence for a given base

    >>> list(islice(esthetic_nums(base=10), 20))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65]
    """
    queue: deque[tuple[int, int]] = deque()
    queue.extendleft((d, d) for d in range(1, base))
    while True:
        num, lsd = queue.pop()
        yield num
        new_lsds = (d for d in (lsd - 1, lsd + 1) if 0 <= d < base)
        num *= base  # Shift num left one digit
        queue.extendleft((num + d, d) for d in new_lsds)


def to_digits(num: int, base: int) -> Digits:
    """Return a representation of an integer as digits in a given base

    >>> to_digits(0x3def84f0ce, base=16)
    '3def84f0ce'
    """
    digits: list[str] = []
    while num:
        num, d = divmod(num, base)
        digits.append("0123456789abcdef"[d])
    return "".join(reversed(digits)) if digits else "0"


def pprint_it(it: Iterable[str], indent: int = 4, width: int = 80) -> None:
    """Pretty print an iterable which returns strings

    >>> pprint_it(map(str, range(20)), indent=0, width=40)
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19
    <BLANKLINE>
    """
    joined = ", ".join(it)
    lines = wrap(joined, width=width - indent)
    for line in lines:
        print(f"{indent*' '}{line}")
    print()


def task_2() -> None:
    nums: Iterator[int]
    for base in range(2, 16 + 1):
        start, stop = 4 * base, 6 * base
        nums = esthetic_nums(base)
        nums = islice(nums, start - 1, stop)  # start and stop are 1-based indices
        print(
            f"Base-{base} esthetic numbers from "
            f"index {start} through index {stop} inclusive:\n"
        )
        pprint_it(to_digits(num, base) for num in nums)


def task_3(lower: int, upper: int, base: int = 10) -> None:
    nums: Iterator[int] = esthetic_nums(base)
    nums = dropwhile(lambda num: num < lower, nums)
    nums = takewhile(lambda num: num <= upper, nums)
    print(
        f"Base-{base} esthetic numbers with "
        f"magnitude between {lower:,} and {upper:,}:\n"
    )
    pprint_it(to_digits(num, base) for num in nums)


if __name__ == "__main__":
    print("======\nTask 2\n======\n")
    task_2()

    print("======\nTask 3\n======\n")
    task_3(1_000, 9_999)

    print("======\nTask 4\n======\n")
    task_3(100_000_000, 130_000_000)

```

### python_code_2.txt
```python
'''Esthetic numbers'''

from functools import reduce
from itertools import (
    accumulate, chain, count, dropwhile,
    islice, product, takewhile
)
from operator import add
from string import digits, ascii_lowercase
from textwrap import wrap


# estheticNumbersInBase :: Int -> [Int]
def estheticNumbersInBase(b):
    '''Infinite stream of numbers which are
       esthetic in a given base.
    '''
    return concatMap(
        compose(
            lambda deltas: concatMap(
                lambda headDigit: concatMap(
                    compose(
                        fromBaseDigits(b),
                        scanl(add)(headDigit)
                    )
                )(deltas)
            )(range(1, b)),
            replicateList([-1, 1])
        )
    )(count(0))


# ------------------------ TESTS -------------------------
def main():
    '''Specified tests'''
    def samples(b):
        i, j = b * 4, b * 6
        return '\n'.join([
            f'Esthetics [{i}..{j}] for base {b}:',
            unlines(wrap(
                unwords([
                    showInBase(b)(n) for n in compose(
                        drop(i - 1), take(j)
                    )(
                        estheticNumbersInBase(b)
                    )
                ]), 60
            ))
        ])

    def takeInRange(a, b):
        return compose(
            dropWhile(lambda x: x < a),
            takeWhile(lambda x: x <= b)
        )

    print(
        '\n\n'.join([
            samples(b) for b in range(2, 1 + 16)
        ])
    )
    for (lo, hi) in [(1000, 9999), (100_000_000, 130_000_000)]:
        print(f'\nBase 10 Esthetics in range [{lo}..{hi}]:')
        print(
            unlines(wrap(
                unwords(
                    str(x) for x in takeInRange(lo, hi)(
                        estheticNumbersInBase(10)
                    )
                ), 60
            ))
        )


# ------------------- BASES AND DIGITS -------------------

# fromBaseDigits :: Int -> [Int] -> [Int]
def fromBaseDigits(b):
    '''An empty list if any digits are out of range for
       the base. Otherwise a list containing an integer.
    '''
    def go(digitList):
        maybeNum = reduce(
            lambda r, d: None if r is None or (
                0 > d or d >= b
            ) else r * b + d,
            digitList, 0
        )
        return [] if None is maybeNum else [maybeNum]
    return go


# toBaseDigits :: Int -> Int -> [Int]
def toBaseDigits(b):
    '''A list of the digits of n in base b.
    '''
    def f(x):
        return None if 0 == x else (
            divmod(x, b)[::-1]
        )
    return lambda n: list(reversed(unfoldr(f)(n)))


# showInBase :: Int -> Int -> String
def showInBase(b):
    '''String representation of n in base b.
    '''
    charSet = digits + ascii_lowercase
    return lambda n: ''.join([
        charSet[i] for i in toBaseDigits(b)(n)
    ])


# ----------------------- GENERIC ------------------------

# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been
       mapped.
       The list monad can be derived by using a function f
       which wraps its output in a list, (using an empty
       list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return go


# dropWhile :: (a -> Bool) -> [a] -> [a]
# dropWhile :: (Char -> Bool) -> String -> String
def dropWhile(p):
    '''The suffix remainining after takeWhile p xs.
    '''
    return lambda xs: list(
        dropwhile(p, xs)
    )


# replicateList :: [a] -> Int -> [[a]]
def replicateList(xs):
    '''All distinct lists of length n that
       consist of elements drawn from xs.
    '''
    def rep(n):
        def go(x):
            return [[]] if 1 > x else [
                ([a] + b) for (a, b) in product(
                    xs, go(x - 1)
                )
            ]
        return go(n)
    return rep


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but defines a succession of
       intermediate values, building from the left.
    '''
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return list(islice(xs, n))
    return go


# takeWhile :: (a -> Bool) -> [a] -> [a]
# takeWhile :: (Char -> Bool) -> String -> String
def takeWhile(p):
    '''The longest (possibly empty) prefix of xs
       in which all elements satisfy p.
    '''
    return lambda xs: list(
        takewhile(p, xs)
    )


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Dual to reduce or foldr.
       Where catamorphism reduces a list to a summary value,
       the anamorphic unfoldr builds a list from a seed value.
       As long as f returns (a, b) a is prepended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns None, the completed list is returned.
    '''
    def go(v):
        xr = v, v
        xs = []
        while True:
            xr = f(xr[1])
            if None is not xr:
                xs.append(xr[0])
            else:
                return xs
    return go


# unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived
       from a list of words.
    '''
    return ' '.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

