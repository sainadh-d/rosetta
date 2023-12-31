# Binary digits

## Task Link
[Rosetta Code - Binary digits](https://rosettacode.org/wiki/Binary_digits)

## Java Code
### java_code_2.txt
```java
Integer.toBinaryString(5);

```

### java_code_3.txt
```java
Integer.toBinaryString(50);

```

### java_code_4.txt
```java
Integer.toBinaryString(9000);

```

## Python Code
### python_code_1.txt
```python
>>> for i in range(16): print('{0:b}'.format(i))

0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111

```

### python_code_2.txt
```python
>>> for i in range(16): print(bin(i)[2:])

0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111

```

### python_code_3.txt
```python
>>> oct2bin = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
>>> bin = lambda n: ''.join(oct2bin[octdigit] for octdigit in '%o' % n).lstrip('0') or '0'
>>> for i in range(16): print(bin(i))

0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111

```

### python_code_4.txt
```python
'''Binary strings for integers'''


# showBinary :: Int -> String
def showBinary(n):
    '''Binary string representation of an integer.'''
    def binaryChar(n):
        return '1' if n != 0 else '0'
    return showIntAtBase(2)(binaryChar)(n)('')


# TEST ----------------------------------------------------

# main :: IO()
def main():
    '''Test'''

    print('Mapping showBinary over integer list:')
    print(unlines(map(
        showBinary,
        [5, 50, 9000]
    )))

    print(tabulated(
        '\nUsing showBinary as a display function:'
    )(str)(showBinary)(
        lambda x: x
    )([5, 50, 9000]))


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# showIntAtBase :: Int -> (Int -> String) -> Int -> String -> String
def showIntAtBase(base):
    '''String representing a non-negative integer
       using the base specified by the first argument,
       and the character representation specified by the second.
       The final argument is a (possibly empty) string to which
       the numeric string will be prepended.'''
    def wrap(toChr, n, rs):
        def go(nd, r):
            n, d = nd
            r_ = toChr(d) + r
            return go(divmod(n, base), r_) if 0 != n else r_
        return 'unsupported base' if 1 >= base else (
            'negative number' if 0 > n else (
                go(divmod(n, base), rs))
        )
    return lambda toChr: lambda n: lambda rs: (
        wrap(toChr, n, rs)
    )


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
                f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join(
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


if __name__ == '__main__':
    main()

```

### python_code_5.txt
```python
'''Decomposition of an integer to a string of booleans.'''


# boolsFromInt :: Int -> [Bool]
def boolsFromInt(n):
    '''List of booleans derived by binary
       decomposition of an integer.'''
    def go(x):
        (q, r) = divmod(x, 2)
        return Just((q, bool(r))) if x else Nothing()
    return unfoldl(go)(n)


# stringFromBools :: [Bool] -> String
def stringFromBools(xs):
    '''Binary string representation of a
       list of boolean values.'''
    def oneOrZero(x):
        return '1' if x else '0'
    return ''.join(map(oneOrZero, xs))


# TEST ----------------------------------------------------
# main :: IO()
def main():
    '''Test'''

    binary = compose(stringFromBools)(boolsFromInt)

    print('Mapping a composed function:')
    print(unlines(map(
        binary,
        [5, 50, 9000]
    )))

    print(
        tabulated(
            '\n\nTabulating a string display from binary data:'
        )(str)(stringFromBools)(
            boolsFromInt
        )([5, 50, 9000])
    )


# GENERIC -------------------------------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': True}


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
                f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join(
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


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
       When f returns Nothing, the completed list is returned.'''
    def go(v):
        xr = v, v
        xs = []
        while True:
            mb = f(xr[0])
            if mb.get('Nothing'):
                return xs
            else:
                xr = mb.get('Just')
                xs.insert(0, xr[1])
        return xs
    return lambda x: go(x)


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# MAIN -------------------------------------------------
if __name__ == '__main__':
    main()

```

