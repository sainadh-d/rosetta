# Matrix transposition

## Task Link
[Rosetta Code - Matrix transposition](https://rosettacode.org/wiki/Matrix_transposition)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
public class Transpose{
       public static void main(String[] args){
               double[][] m = {{1, 1, 1, 1},
                               {2, 4, 8, 16},
                               {3, 9, 27, 81},
                               {4, 16, 64, 256},
                               {5, 25, 125, 625}};
               double[][] ans = new double[m[0].length][m.length];
               for(int rows = 0; rows < m.length; rows++){
                       for(int cols = 0; cols < m[0].length; cols++){
                               ans[cols][rows] = m[rows][cols];
                       }
               }
               for(double[] i:ans){//2D arrays are arrays of arrays
                       System.out.println(Arrays.toString(i));
               }
       }
}

```

## Python Code
### python_code_1.txt
```python
m=((1,  1,  1,   1),
   (2,  4,  8,  16),
   (3,  9, 27,  81),
   (4, 16, 64, 256),
   (5, 25,125, 625))
print(zip(*m))
# in Python 3.x, you would do:
# print(list(zip(*m)))

```

### python_code_2.txt
```python
# transpose :: Matrix a -> Matrix a
def transpose(m):
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m


if __name__ == '__main__':

    # TRANSPOSING FOUR BASIC TYPES OF PYTHON MATRIX
    # Cartesian product of (Outer, Inner) with (List, Tuple)

    # Matrix any = Tuple of Tuples of any type
    tts = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

    # Matrix any = Tuple of Lists of any  type
    tls = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

    emptyTuple = ()

    # Matrix any = List of Lists of any type
    lls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Matrix any = List of Tuples of any type
    lts = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    emptyList = []

    print('transpose function :: (Transposition without type change):\n')
    for m in [emptyTuple, tts, tls, emptyList, lls, lts]:
        tm = transpose(m)
        print (
            type(tm).__name__ + (
                (' of ' + type(tm[0]).__name__) if m else ''
            ) + ' :: ' + str(m) + ' -> ' + str(tm)
        )

```

### python_code_3.txt
```python
# Uneven list of lists
uls = [[10, 11], [20], [], [30, 31, 32]]

print (
    list(zip(*uls))
)

#  --> []

```

### python_code_4.txt
```python
'''Transposition of row sets with possible gaps'''

from collections import defaultdict


# listTranspose :: [[a]] -> [[a]]
def listTranspose(xss):
    '''Transposition of a matrix which may
       contain gaps.
    '''
    def go(xss):
        if xss:
            h, *t = xss
            return (
                [[h[0]] + [xs[0] for xs in t if xs]] + (
                    go([h[1:]] + [xs[1:] for xs in t])
                )
            ) if h and isinstance(h, list) else go(t)
        else:
            return []
    return go(xss)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests with various lists of rows or non-row data.'''

    def labelledList(kxs):
        k, xs = kxs
        return k + ': ' + showList(xs)

    print(
        fTable(
            __doc__ + ':\n'
        )(labelledList)(fmapFn(showList)(snd))(
            fmapTuple(listTranspose)
        )([
            ('Square', [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            ('Rectangle', [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
            ('Rows with gaps', [[10, 11], [20], [], [31, 32, 33]]),
            ('Single row', [[1, 2, 3]]),
            ('Single row, one cell', [[1]]),
            ('Not rows', [1, 2, 3]),
            ('Nothing', [])
        ])
    )


# TEST RESULT FORMATTING ----------------------------------

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


# fmapFn :: (a -> b) -> (r -> a) -> r -> b
def fmapFn(f):
    '''The application of f to the result of g.
       fmap over a function is composition.
    '''
    return lambda g: lambda x: f(g(x))


# fmapTuple :: (a -> b) -> (c, a) -> (c, b)
def fmapTuple(f):
    '''A pair in which f has been
       applied to the second item.
    '''
    return lambda ab: (ab[0], f(ab[1])) if (
        2 == len(ab)
    ) else None


# show :: a -> String
def show(x):
    '''Stringification of a value.'''
    def go(v):
        return defaultdict(lambda: repr, [
            ('list', showList)
            # ('Either', showLR),
            # ('Maybe', showMaybe),
            # ('Tree', drawTree)
        ])[
            typeName(v)
        ](v)
    return go(x)


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(show(x) for x in xs) + ']'


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# typeName :: a -> String
def typeName(x):
    '''Name string for a built-in or user-defined type.
       Selector for type-specific instances
       of polymorphic functions.
    '''
    if isinstance(x, dict):
        return x.get('type') if 'type' in x else 'dict'
    else:
        return 'iter' if hasattr(x, '__next__') else (
            type(x).__name__
        )

# MAIN ---
if __name__ == '__main__':
    main()

```

