# Fusc sequence

## Task Link
[Rosetta Code - Fusc sequence](https://rosettacode.org/wiki/Fusc_sequence)

## Java Code
### java_code_1.txt
```java
public class FuscSequence {

    public static void main(String[] args) {
        System.out.println("Show the first 61 fusc numbers (starting at zero) in a horizontal format");
        for ( int n = 0 ; n < 61 ; n++ ) {
            System.out.printf("%,d ", fusc[n]);
        }
        
        System.out.printf("%n%nShow the fusc number (and its index) whose length is greater than any previous fusc number length.%n");
        int start = 0;
        for (int i = 0 ; i <= 5 ; i++ ) {
            int val = i != 0 ? (int) Math.pow(10, i) : -1;
            for ( int j = start ; j < FUSC_MAX ; j++ ) {
                if ( fusc[j] > val ) {
                    System.out.printf("fusc[%,d] = %,d%n", j, fusc[j] );
                    start = j;
                    break;
                }
            }
        }
    }
    
    private static final int FUSC_MAX = 30000000;
    private static int[] fusc = new int[FUSC_MAX];

    static {
        fusc[0] = 0;
        fusc[1] = 1;
        for ( int n = 2 ; n < FUSC_MAX ; n++ ) {
            fusc[n] = (n % 2 == 0 ? fusc[n/2] : fusc[(n-1)/2] + fusc[(n+1)/2]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import deque
from itertools import islice, count


def fusc():
    q = deque([1])
    yield 0
    yield 1

    while True:
        x = q.popleft()
        q.append(x)
        yield x

        x += q[0]
        q.append(x)
        yield x


def longest_fusc():
    sofar = 0
    for i, f in zip(count(), fusc()):
        if f >= sofar:
            yield(i, f)
            sofar = 10 * sofar or 10


print('First 61:')
print(list(islice(fusc(), 61)))

print('\nLength records:')
for i, f in islice(longest_fusc(), 6):
    print(f'fusc({i}) = {f}')

```

### python_code_2.txt
```python
'''Fusc sequence'''

from itertools import chain, count, islice
from operator import itemgetter


# As an infinite stream of terms,

# infiniteFusc :: [Int]
def infiniteFusc():
    '''Fusc sequence.
       OEIS A2487
    '''
    def go(step):
        isEven, n, xxs = step
        x, xs = xxs[0], xxs[1:]
        if isEven:
            nxt = n + x
            return not isEven, nxt, xxs + [nxt]
        else:
            return not isEven, x, xs + [x]

    return chain(
        [0, 1],
        map(
            itemgetter(1),
            iterate(go)(
                (True, 1, [1])
            )
        )
    )


# Or as a function over an integer:

# fusc :: Int -> Int
def fusc(i):
    '''Fusc sequence'''
    def go(n):
        if 0 == n:
            return (1, 0)
        else:
            x, y = go(n // 2)
            return (x + y, y) if 0 == n % 2 else (
                x, x + y
            )
    return 0 if 1 > i else (
        go(i - 1)[0]
    )


# firstFuscOfEachMagnitude ::
def firstFuscOfEachMagnitude():
    '''Non-finite stream of each term
       in OEIS A2487 that requires an
       unprecedented quantity of decimal digits.
    '''
    a2487 = enumerate(map(fusc, count()))

    def go(e):
        limit = 10 ** e
        return next(
            (i, x) for i, x in a2487
            if limit <= x
        )
    return (
        chain([(0, 0)], map(go, count(1)))
    )


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Tests'''

    print('First 61 terms:')
    print(showList(
        take(61)(
            map(fusc, count())
        )
    ))

    print('\nFirst term of each decimal magnitude:')
    print('(Index, Term):')
    ixs = firstFuscOfEachMagnitude()
    for _ in range(0, 5):
        print(next(ixs))


# -------------------------GENERIC-------------------------

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
    return lambda x: go(x)


# showList :: [a] -> String
def showList(xs):
    '''Compact stringification of a list.'''
    return '[' + ','.join(repr(x) for x in xs) + ']'


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

