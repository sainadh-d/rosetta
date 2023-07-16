# Sequence of non-squares

## Task Link
[Rosetta Code - Sequence of non-squares](https://rosettacode.org/wiki/Sequence_of_non-squares)

## Java Code
### java_code_1.txt
```java
public class SeqNonSquares {
    public static int nonsqr(int n) {
        return n + (int)Math.round(Math.sqrt(n));
    }
    
    public static void main(String[] args) {
        // first 22 values (as a list) has no squares:
        for (int i = 1; i < 23; i++)
            System.out.print(nonsqr(i) + " ");
        System.out.println();
        
        // The following check shows no squares up to one million:
        for (int i = 1; i < 1000000; i++) {
            double j = Math.sqrt(nonsqr(i));
            assert j != Math.floor(j);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from math import floor, sqrt
>>> def non_square(n):
        return n + floor(1/2 + sqrt(n))

>>> # first 22 values has no squares:
>>> print(*map(non_square, range(1, 23)))
2 3 5 6 7 8 10 11 12 13 14 15 17 18 19 20 21 22 23 24 26 27

>>> # The following check shows no squares up to one million:
>>> def is_square(n):
        return sqrt(n).is_integer()

>>> non_squares = map(non_square, range(1, 10 ** 6))
>>> next(filter(is_square, non_squares))
StopIteration                             Traceback (most recent call last)
<ipython-input-45-f32645fc1c0a> in <module>()
      1 non_squares = map(non_square, range(1, 10 ** 6))
----> 2 next(filter(is_square, non_squares))

StopIteration:

```

### python_code_2.txt
```python
'''Sequence of non-squares'''

from itertools import count, islice
from math import floor, sqrt


# A000037 :: [Int]
def A000037():
    '''A non-finite series of integers.'''
    return map(nonSquare, count(1))


# nonSquare :: Int -> Int
def nonSquare(n):
    '''Nth term in the OEIS A000037 series.'''
    return n + floor(1 / 2 + sqrt(n))


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''OEIS A000037'''

    def first22():
        '''First 22 terms'''
        return take(22)(A000037())

    def squareInFirstMillion():
        '''True if any of the first 10^6 terms are perfect squares'''
        return any(map(
            isPerfectSquare,
            take(10 ** 6)(A000037())
        ))

    print(
        fTable(main.__doc__)(
            lambda f: '\n' + f.__doc__
        )(lambda x: '    ' + showList(x))(
            lambda f: f()
        )([first22, squareInFirstMillion])
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
        return s + '\n' + '\n'.join(map(
            lambda x, y: y + ':\n' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# -------------------------GENERAL-------------------------

# isPerfectSquare :: Int -> Bool
def isPerfectSquare(n):
    '''True if n is a perfect square.'''
    return sqrt(n).is_integer()


# showList :: [a] -> String
def showList(xs):
    '''Compact stringification of any list value.'''
    return '[' + ','.join(repr(x) for x in xs) + ']' if (
        isinstance(xs, list)
    ) else repr(xs)


# take :: Int -> [a] -> [a]
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: list(islice(xs, n))


# MAIN ---
if __name__ == '__main__':
    main()

```

