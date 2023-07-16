# Knuth shuffle

## Task Link
[Rosetta Code - Knuth shuffle](https://rosettacode.org/wiki/Knuth_shuffle)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public static final Random gen = new Random();

// version for array of ints
public static void shuffle (int[] array) {
    int n = array.length;
    while (n > 1) {
        int k = gen.nextInt(n--); //decrements after using the value
        int temp = array[n];
        array[n] = array[k];
        array[k] = temp;
    }
}
// version for array of references
public static void shuffle (Object[] array) {
    int n = array.length;
    while (n > 1) {
        int k = gen.nextInt(n--); //decrements after using the value
        Object temp = array[n];
        array[n] = array[k];
        array[k] = temp;
    }
}

```

## Python Code
### python_code_1.txt
```python
from random import randrange

def knuth_shuffle(x):
    for i in range(len(x)-1, 0, -1):
        j = randrange(i + 1)
        x[i], x[j] = x[j], x[i]

x = list(range(10))
knuth_shuffle(x)
print("shuffled:", x)

```

### python_code_2.txt
```python
'''Knuth shuffle as a fold'''

from functools import reduce
from random import randint


# knuthShuffle :: [a] -> IO [a]
def knuthShuffle(xs):
    '''A pseudo-random shuffle of the elements in xs.'''
    return reduce(
        swapped,
        enumerate(randoms(len(xs))), xs
    )


# swapped :: (Int, Int) -> [a] -> [a]
def swapped(xs, ij):
    '''New list in which the elements at indices
       i and j of xs are swapped.
    '''
    def go(a, b):
        if a != b:
            m, n = (a, b) if b > a else (b, a)
            l, ht = splitAt(m)(xs)
            ys, zs = splitAt((n - m) - 1)(ht[1:])
            return l + [zs[0]] + ys + [ht[0]] + zs[1:]
        else:
            return xs
    i, j = ij
    z = len(xs) - 1
    return xs if i > z or j > z else go(i, j)


# randoms :: Int -> IO [Int]
def randoms(n):
    '''Pseudo-random list of n - 1 indices.
    '''
    return list(map(randomRInt(0)(n - 1), range(1, n)))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Repeated Knuth shuffles of ['a' .. 'k']'''

    print(
        fTable(main.__doc__ + ':\n')(str)(lambda x: ''.join(x))(
            lambda _: knuthShuffle(list('abcdefghijk'))
        )(range(1, 11))
    )


# GENERIC -------------------------------------------------

# randomRInt :: Int -> Int -> IO () -> Int
def randomRInt(m):
    '''The return value of randomRInt is itself
       a function. The returned function, whenever
       called, yields a a new pseudo-random integer
       in the range [m..n].
    '''
    return lambda n: lambda _: randint(m, n)


# splitAt :: Int -> [a] -> ([a], [a])
def splitAt(n):
    '''A tuple pairing the prefix of length n
       with the rest of xs.
    '''
    return lambda xs: (xs[0:n], xs[n:])


# FORMATTING -----------------------------------------------------------

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


# MAIN ---
if __name__ == '__main__':
    main()

```

