# CUSIP

## Task Link
[Rosetta Code - CUSIP](https://rosettacode.org/wiki/CUSIP)

## Java Code
### java_code_1.txt
```java
import java.util.List;

public class Cusip {
    private static Boolean isCusip(String s) {
        if (s.length() != 9) return false;
        int sum = 0;
        for (int i = 0; i <= 7; i++) {
            char c = s.charAt(i);

            int v;
            if (c >= '0' && c <= '9') {
                v = c - 48;
            } else if (c >= 'A' && c <= 'Z') {
                v = c - 55;  // lower case letters apparently invalid
            } else if (c == '*') {
                v = 36;
            } else if (c == '@') {
                v = 37;
            } else if (c == '#') {
                v = 38;
            } else {
                return false;
            }
            if (i % 2 == 1) v *= 2;  // check if odd as using 0-based indexing
            sum += v / 10 + v % 10;
        }
        return s.charAt(8) - 48 == (10 - (sum % 10)) % 10;
    }

    public static void main(String[] args) {
        List<String> candidates = List.of(
                "037833100", "17275R102", "38259P508", "594918104", "68389X106", "68389X105", "EXTRACRD8",
                "EXTRACRD9", "BADCUSIP!", "683&9X106", "68389x105", "683$9X106", "68389}105", "87264ABE4"
        );
        for (String candidate : candidates) {
            System.out.printf("%s -> %s%n", candidate, isCusip(candidate) ? "correct" : "incorrect");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import math

def cusip_check(cusip):
    if len(cusip) != 9:
        raise ValueError('CUSIP must be 9 characters')

    cusip = cusip.upper()
    total = 0
    for i in range(8):
        c = cusip[i]
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            p = ord(c) - ord('A') + 1
            v = p + 9
        elif c == '*':
            v = 36
        elif c == '@':
            v = 37
        elif c == '#':
            v = 38

        if i % 2 != 0:
            v *= 2

        total += int(v / 10) + v % 10
    check = (10 - (total % 10)) % 10
    return str(check) == cusip[-1]

if __name__ == '__main__':
    codes = [
            '037833100',
            '17275R102',
            '38259P508',
            '594918104',
            '68389X106',
            '68389X105'
            ]
    for code in codes:
        print(f'{code} -> {cusip_check(code)}')

```

### python_code_2.txt
```python
'''CUSIP'''

from itertools import (cycle, islice, starmap)
from functools import (reduce)
from operator import (add)
from enum import (Enum)


# isCusip :: Dict -> String -> Bool
def isCusip(dct):
    '''Test for the validity of a CUSIP string in the
       context of a supplied dictionary of char values'''
    def go(s):
        ns = [dct[c] for c in list(s) if c in dct]
        return 9 == len(ns) and (
            ns[-1] == (
                10 - (
                    sum(zipWith(
                        lambda f, x: add(*divmod(f(x), 10))
                    )(cycle([identity, double]))(
                        take(8)(ns)
                    )) % 10
                )
            ) % 10
        )
    return go


# cusipCharDict :: () -> Dict Char Int
def cusipCharDict():
    '''Dictionary of integer values for CUSIP characters'''
    def kv(a, ic):
        i, c = ic
        a[c] = i
        return a
    return reduce(
        kv,
        enumerate(
            enumFromTo('0')('9') + (
                enumFromTo('A')('Z') + list('*&#')
            )
        ),
        {}
    )


# TEST -------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    # cusipTest :: String -> Bool
    cusipTest = isCusip(cusipCharDict())

    print(
        tabulated('Valid as CUSIP string:')(
            cusipTest
        )([
            '037833100',
            '17275R102',
            '38259P508',
            '594918104',
            '68389X106',
            '68389X105'
        ])
    )

# GENERIC -------------------------------------------------


# double :: Num -> Num
def double(x):
    '''Wrapped here as a function for the zipWith expression'''
    return 2 * x


# enumFromTo :: Enum a => a -> a -> [a]
def enumFromTo(m):
    '''Enumeration of values [m..n]'''
    def go(x, y):
        t = type(m)
        i = fromEnum(x)
        d = 0 if t != float else (x - i)
        return list(map(
            lambda x: toEnum(t)(d + x),
            range(i, 1 + fromEnum(y))
        ) if int != t else range(x, 1 + y))
    return lambda n: go(m, n)


# fromEnum :: Enum a => a -> Int
def fromEnum(x):
    '''Index integer for enumerable value.'''
    return ord(x) if str == type(x) else (
        x.value if isinstance(x, Enum) else int(x)
    )


# mul :: Num -> Num -> Num
def mul(x):
    '''Function version of (*) operator;
       a curried equivalent of operator.mul'''
    return lambda y: x * y


# identity :: a -> a
def identity(x):
    '''The identity function.
       The usual 'id' is reserved in Python.'''
    return x


# tabulated :: String -> (a -> b) -> [a] -> String
def tabulated(s):
    '''heading -> function -> input List -> tabulated output string'''
    def go(f, xs):
        def width(x):
            return len(str(x))
        w = width(max(xs, key=width))
        return s + '\n' + '\n'.join([
            str(x).rjust(w, ' ') + ' -> ' + str(f(x)) for x in xs
        ])
    return lambda f: lambda xs: go(f, xs)


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# toEnum :: Type -> Int -> a
def toEnum(t):
    '''Enumerable value from index integer'''
    dct = {
        int: int,
        float: float,
        str: chr,
        bool: bool
    }
    return lambda x: dct[t](x) if t in dct else t(x)


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    '''Zipping with a custom (rather than tuple) function'''
    return lambda xs: lambda ys: (
        list(starmap(f, zip(xs, ys)))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

