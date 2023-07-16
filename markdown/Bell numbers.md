# Bell numbers

## Task Link
[Rosetta Code - Bell numbers](https://rosettacode.org/wiki/Bell_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class Bell {
    private static class BellTriangle {
        private List<Integer> arr;

        BellTriangle(int n) {
            int length = n * (n + 1) / 2;
            arr = new ArrayList<>(length);
            for (int i = 0; i < length; ++i) {
                arr.add(0);
            }

            set(1, 0, 1);
            for (int i = 2; i <= n; ++i) {
                set(i, 0, get(i - 1, i - 2));
                for (int j = 1; j < i; ++j) {
                    int value = get(i, j - 1) + get(i - 1, j - 1);
                    set(i, j, value);
                }
            }
        }

        private int index(int row, int col) {
            if (row > 0 && col >= 0 && col < row) {
                return row * (row - 1) / 2 + col;
            } else {
                throw new IllegalArgumentException();
            }
        }

        public int get(int row, int col) {
            int i = index(row, col);
            return arr.get(i);
        }

        public void set(int row, int col, int value) {
            int i = index(row, col);
            arr.set(i, value);
        }
    }

    public static void main(String[] args) {
        final int rows = 15;
        BellTriangle bt = new BellTriangle(rows);

        System.out.println("First fifteen Bell numbers:");
        for (int i = 0; i < rows; ++i) {
            System.out.printf("%2d: %d\n", i + 1, bt.get(i + 1, 0));
        }

        for (int i = 1; i <= 10; ++i) {
            System.out.print(bt.get(i, 0));
            for (int j = 1; j < i; ++j) {
                System.out.printf(", %d", bt.get(i, j));
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def bellTriangle(n):
    tri = [None] * n
    for i in xrange(n):
        tri[i] = [0] * i
    tri[1][0] = 1
    for i in xrange(2, n):
        tri[i][0] = tri[i - 1][i - 2]
        for j in xrange(1, i):
            tri[i][j] = tri[i][j - 1] + tri[i - 1][j - 1]
    return tri

def main():
    bt = bellTriangle(51)
    print "First fifteen and fiftieth Bell numbers:"
    for i in xrange(1, 16):
        print "%2d: %d" % (i, bt[i][0])
    print "50:", bt[50][0]
    print
    print "The first ten rows of Bell's triangle:"
    for i in xrange(1, 11):
        print bt[i]

main()

```

### python_code_2.txt
```python
'''Bell numbers'''

from itertools import accumulate, chain, islice
from operator import add, itemgetter
from functools import reduce


# bellNumbers :: [Int]
def bellNumbers():
    '''Bell or exponential numbers.
       A000110
    '''
    return map(itemgetter(0), bellTriangle())


# bellTriangle :: [[Int]]
def bellTriangle():
    '''Bell triangle.'''
    return map(
        itemgetter(1),
        iterate(
            compose(
                bimap(last)(identity),
                list, uncurry(scanl(add))
            )
        )((1, [1]))
    )


# ------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Tests'''
    showIndex = compose(repr, succ, itemgetter(0))
    showValue = compose(repr, itemgetter(1))
    print(
        fTable(
            'First fifteen Bell numbers:'
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(15)(bellNumbers()))
        ))
    )

    print('\nFiftieth Bell number:')
    bells = bellNumbers()
    drop(49)(bells)
    print(
        next(bells)
    )

    print(
        fTable(
            "\nFirst 10 rows of Bell's triangle:"
        )(showIndex)(showValue)(identity)(list(
            enumerate(take(10)(bellTriangle()))
        ))
    )


# ------------------------ GENERIC ------------------------

# bimap :: (a -> b) -> (c -> d) -> (a, c) -> (b, d)
def bimap(f):
    '''Tuple instance of bimap.
       A tuple of the application of f and g to the
       first and second values respectively.
    '''
    def go(g):
        def gox(x):
            return (f(x), g(x))
        return gox
    return go


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, identity)


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


# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + fxShow(f(x))
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox


# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


# last :: [a] -> a
def last(xs):
    '''The last element of a non-empty list.'''
    return xs[-1]


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.
    '''
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple,
       derived from a curried function.
    '''
    def go(tpl):
        return f(tpl[0])(tpl[1])
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

