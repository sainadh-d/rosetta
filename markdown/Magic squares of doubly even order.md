# Magic squares of doubly even order

## Task Link
[Rosetta Code - Magic squares of doubly even order](https://rosettacode.org/wiki/Magic_squares_of_doubly_even_order)

## Java Code
### java_code_1.txt
```java
public class MagicSquareDoublyEven {

    public static void main(String[] args) {
        int n = 8;
        for (int[] row : magicSquareDoublyEven(n)) {
            for (int x : row)
                System.out.printf("%2s ", x);
            System.out.println();
        }
        System.out.printf("\nMagic constant: %d ", (n * n + 1) * n / 2);
    }

    static int[][] magicSquareDoublyEven(final int n) {
        if (n < 4 || n % 4 != 0)
            throw new IllegalArgumentException("base must be a positive "
                    + "multiple of 4");

        // pattern of count-up vs count-down zones
        int bits = 0b1001_0110_0110_1001;
        int size = n * n;
        int mult = n / 4;  // how many multiples of 4

        int[][] result = new int[n][n];

        for (int r = 0, i = 0; r < n; r++) {
            for (int c = 0; c < n; c++, i++) {
                int bitPos = c / mult + (r / mult) * 4;
                result[r][c] = (bits & (1 << bitPos)) != 0 ? i + 1 : size - i;
            }
        }
        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
def MagicSquareDoublyEven(order):
    sq = [range(1+n*order,order + (n*order)+1) for n in range(order) ]
    n1 = order/4
    for r in range(n1):
        r1 = sq[r][n1:-n1]
        r2 = sq[order -r - 1][n1:-n1]
        r1.reverse()
        r2.reverse()
        sq[r][n1:-n1] = r2
        sq[order -r - 1][n1:-n1] = r1
    for r in range(n1, order-n1):
        r1 = sq[r][:n1]
        r2 = sq[order -r - 1][order-n1:]
        r1.reverse()
        r2.reverse()
        sq[r][:n1] = r2
        sq[order -r - 1][order-n1:] = r1
    return sq

def printsq(s):
    n = len(s)
    bl = len(str(n**2))+1
    for i in range(n):
        print ''.join( [ ("%"+str(bl)+"s")%(str(x)) for x in s[i]] )
    print "\nMagic constant = %d"%sum(s[0])

printsq(MagicSquareDoublyEven(8))

```

### python_code_2.txt
```python
'''Magic squares of doubly even order'''

from itertools import chain, repeat
from functools import reduce
from math import log


# doublyEvenMagicSquare :: Int -> [[Int]]
def doublyEvenMagicSquare(n):
    '''Magic square of order n'''

    # magic :: Int -> [Bool]
    def magic(n):
        '''Truth-table series'''
        if 0 < n:
            xs = magic(n - 1)
            return xs + [not x for x in xs]
        else:
            return [True]

    sqr = n * n
    power = log(sqr, 2)
    scale = replicate(n / 4)
    return chunksOf(n)([
        succ(i) if bln else sqr - i for i, bln in
        enumerate(magic(power) if isInteger(power) else (
            flatten(scale(
                map(scale, chunksOf(4)(magic(4)))
            ))
        ))
    ])


# TEST ----------------------------------------------------
# main :: IO()
def main():
    '''Tests'''

    order = 8
    magicSquare = doublyEvenMagicSquare(order)

    print(
        'Row sums: ',
        [sum(xs) for xs in magicSquare],
        '\nCol sums:',
        [sum(xs) for xs in transpose(magicSquare)],
        '\n1st diagonal sum:',
        sum(magicSquare[i][i] for i in range(0, order)),
        '\n2nd diagonal sum:',
        sum(magicSquare[i][(order - 1) - i] for i in range(0, order)),
        '\n'
    )
    print(wikiTable({
        'class': 'wikitable',
        'style': cssFromDict({
            'text-align': 'center',
            'color': '#605B4B',
            'border': '2px solid silver'
        }),
        'colwidth': '3em'
    })(magicSquare))


# GENERIC -------------------------------------------------


# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n,
       subdividing the contents of xs.
       Where the length of xs is not evenly divible
       the final list will be shorter than n.'''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''Concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output a in list
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# cssFromDict :: Dict -> String
def cssFromDict(dct):
    '''CSS string serialized from key values in a Dictionary.'''
    return reduce(
        lambda a, k: a + k + ':' + dct[k] + '; ', dct.keys(), ''
    )


# flatten :: NestedList a -> [a]
def flatten(x):
    '''A list of atoms resulting from fully flattening
       an arbitrarily nested list.'''
    return concatMap(flatten)(x) if isinstance(x, list) else [x]


# isInteger :: Num -> Bool
def isInteger(n):
    '''Divisible by one without remainder ?'''
    return 0 == (n - int(n))


# replicate :: Int -> a -> [a]
def replicate(n):
    '''A list of length n in which every element
       has the value x.'''
    return lambda x: list(repeat(x, n))


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value. For numeric types, (1 +).'''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


# transpose :: Matrix a -> Matrix a
def transpose(m):
    '''The rows and columns of the argument transposed.
       (The matrix containers and rows can be lists or tuples).'''
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m


# wikiTable :: Dict -> [[a]] -> String
def wikiTable(opts):
    '''List of lists rendered as a wiki table string.'''
    def colWidth():
        return 'width:' + opts['colwidth'] + '; ' if (
            'colwidth' in opts
        ) else ''

    def cellStyle():
        return opts['cell'] if 'cell' in opts else ''

    return lambda rows: '{| ' + reduce(
        lambda a, k: (
            a + k + '="' + opts[k] + '" ' if k in opts else a
        ),
        ['class', 'style'],
        ''
    ) + '\n' + '\n|-\n'.join(
        '\n'.join(
            ('|' if (0 != i and ('cell' not in opts)) else (
                '|style="' + colWidth() + cellStyle() + '"|'
            )) + (
                str(x) or ' '
            ) for x in row
        ) for i, row in enumerate(rows)
    ) + '\n|}\n\n'


if __name__ == '__main__':
    main()

```

