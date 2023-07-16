# Generate lower case ASCII alphabet

## Task Link
[Rosetta Code - Generate lower case ASCII alphabet](https://rosettacode.org/wiki/Generate_lower_case_ASCII_alphabet)

## Java Code
### java_code_1.txt
```java
char[] lowerAlphabet() {
    char[] letters = new char[26];
    for (int code = 97; code < 123; code++)
        letters[code - 97] = (char) code;
    return letters;
}

```

### java_code_2.txt
```java
public class LowerAscii {

    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder(26);
        for (char ch = 'a'; ch <= 'z'; ch++)
            sb.append(ch);
        System.out.printf("lower ascii: %s, length: %s", sb, sb.length());
    }
}

```

## Python Code
### python_code_1.txt
```python
# From the standard library:
from string import ascii_lowercase

# Generation:
lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]

```

### python_code_2.txt
```python
'''Enumeration a-z'''

from inspect import signature
import enum


# TEST ----------------------------------------------------
def main():
    '''Testing particular instances of a general pattern:
    '''
    print(
        fTable(__doc__ + ':\n')(repr)(showList)(
            uncurry(enumFromTo)
        )([
            ('a', 'z'),
            ('α', 'ω'),
            ('א', 'ת'),
            (1, 10),
            (round((5**(1 / 2) - 1) / 2, 5), 5),
            ('🌱', '🍂')
        ])
    )


# GENERIC -------------------------------------------------

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
    Enum = enum.Enum
    return ord(x) if isinstance(x, str) else (
        x.value if isinstance(x, Enum) else int(x)
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


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple, derived from
       a vanilla or curried function.
    '''
    if 1 < len(signature(f).parameters):
        return lambda xy: f(*xy)
    else:
        return lambda xy: f(xy[0])(xy[1])


# FORMATTING -------------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(str(x) for x in xs) + ']'


# MAIN ---
if __name__ == '__main__':
    main()

```

