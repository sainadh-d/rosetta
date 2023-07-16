# Catalan numbers/Pascal's triangle

## Task Link
[Rosetta Code - Catalan numbers/Pascal's triangle](https://rosettacode.org/wiki/Catalan_numbers/Pascal%27s_triangle)

## Java Code
### java_code_1.txt
```java
public class Test {
    public static void main(String[] args) {
        int N = 15;
        int[] t = new int[N + 2];
        t[1] = 1;

        for (int i = 1; i <= N; i++) {

            for (int j = i; j > 1; j--)
                t[j] = t[j] + t[j - 1];

            t[i + 1] = t[i];

            for (int j = i + 1; j > 1; j--)
                t[j] = t[j] + t[j - 1];

            System.out.printf("%d ", t[i + 1] - t[i]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> n = 15
>>> t = [0] * (n + 2)
>>> t[1] = 1
>>> for i in range(1, n + 1):
	for j in range(i, 1, -1): t[j] += t[j - 1]
	t[i + 1] = t[i]
	for j in range(i + 1, 1, -1): t[j] += t[j - 1]
	print(t[i+1] - t[i], end=' ')

	
1 2 5 14 42 132 429 1430 4862 16796 58786 208012 742900 2674440 9694845 
>>>

```

### python_code_2.txt
```python
def catalan_number(n):
    nm = dm = 1
    for k in range(2, n+1):
      nm, dm = ( nm*(n+k), dm*k )
    return nm/dm
 
print [catalan_number(n) for n in range(1, 16)]
 
[1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845]

```

### python_code_3.txt
```python
'''Catalan numbers from Pascal's triangle'''

from itertools import (islice)
from operator import (add)


# nCatalans :: Int -> [Int]
def nCatalans(n):
    '''The first n Catalan numbers,
       derived from Pascal's triangle.'''

    # diff :: [Int] -> Int
    def diff(xs):
        '''Difference between the first two items in the list,
           if its length is more than one.
           Otherwise, the first (only) item in the list.'''
        return (
            xs[0] - (xs[1] if 1 < len(xs) else 0)
        ) if xs else None
    return list(map(
        compose(diff)(uncurry(drop)),
        enumerate(map(fst, take(n)(
            everyOther(
                pascalTriangle()
            )
        )))
    ))


# pascalTriangle :: Gen [[Int]]
def pascalTriangle():
    '''A non-finite stream of
       Pascal's triangle rows.'''
    return iterate(nextPascal)([1])


# nextPascal :: [Int] -> [Int]
def nextPascal(xs):
    '''A row of Pascal's triangle
       derived from a preceding row.'''
    return zipWith(add)([0] + xs)(xs + [0])


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''First 16 Catalan numbers.'''

    print(
        nCatalans(16)
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.'''
    def go(xs):
        if isinstance(xs, list):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)


# everyOther :: Gen [a] -> Gen [a]
def everyOther(g):
    '''Every other item of a generator stream.'''
    while True:
        yield take(1)(g)
        take(1)(g)      # Consumed, not yielded.


# fst :: (a, b) -> a
def fst(tpl):
    '''First component of a pair.'''
    return tpl[0]


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated applications of f to x.'''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)


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


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple
       derived from a curried function.'''
    return lambda xy: f(xy[0])(
        xy[1]
    )


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    '''A list constructed by zipping with a
       custom function, rather than with the
       default tuple constructor.'''
    return lambda xs: lambda ys: (
        list(map(f, xs, ys))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

