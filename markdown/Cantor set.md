# Cantor set

## Task Link
[Rosetta Code - Cantor set](https://rosettacode.org/wiki/Cantor_set)

## Java Code
### java_code_1.txt
```java
public class App {
    private static final int WIDTH = 81;
    private static final int HEIGHT = 5;

    private static char[][] lines;
    static {
        lines = new char[HEIGHT][WIDTH];
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                lines[i][j] = '*';
            }
        }
    }

    private static void cantor(int start, int len, int index) {
        int seg = len / 3;
        if (seg == 0) return;
        for (int i = index; i < HEIGHT; i++) {
            for (int j = start + seg; j < start + seg * 2; j++) {
                lines[i][j] = ' ';
            }
        }
        cantor(start, seg, index + 1);
        cantor(start + seg * 2, seg, index + 1);
    }

    public static void main(String[] args) {
        cantor(0, WIDTH, 1);
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                System.out.print(lines[i][j]);
            }
            System.out.println();
        }
    }
}

```

### java_code_2.txt
```java
//Aamrun, 1st July 2022

void cantorSet(int x1,int y1,int x2,int y2,int strWt,int gap,int n){
    strokeWeight(strWt);
    line(x1,y1,x2,y2);
  if(n>0){
    cantorSet(x1,gap + y1,(2*x1+x2)/3,gap + (2*y1+y2)/3,strWt,gap,n-1);
    cantorSet((2*x2+x1)/3,gap + (2*y2+y1)/3,x2,gap + y2,strWt,gap,n-1);
  }
}

void setup(){
  size(1000,1000);
  cantorSet(100,10,900,10,1,10,5);
}

```

## Python Code
### python_code_1.txt
```python
WIDTH = 81
HEIGHT = 5

lines=[]
def cantor(start, len, index):
    seg = len / 3
    if seg == 0:
        return None
    for it in xrange(HEIGHT-index):
        i = index + it
        for jt in xrange(seg):
            j = start + seg + jt
            pos = i * WIDTH + j
            lines[pos] = ' '
    cantor(start,           seg, index + 1)
    cantor(start + seg * 2, seg, index + 1)
    return None

lines = ['*'] * (WIDTH*HEIGHT)
cantor(0, WIDTH, 1)

for i in xrange(HEIGHT):
    beg = WIDTH * i
    print ''.join(lines[beg : beg+WIDTH])

```

### python_code_2.txt
```python
'''Cantor set – separating model from display'''

from functools import (reduce)
import itertools


# cantor :: [(Bool, Int)] -> [(Bool, Int)]
def cantor(xs):
    '''A Cantor segmentation step.'''
    def go(tpl):
        (bln, n) = tpl
        m = n // 3
        return [
            (True, m), (False, m), (True, m)
        ] if bln and (1 < n) else [tpl]
    return concatMap(go)(xs)


# cantorLines :: Int -> String
def cantorLines(n):
    '''A text block display of n
       Cantor-segmented lines.
    '''
    m = n - 1
    repeat = itertools.repeat
    return '\n'.join(
        [showCantor(x) for x in (
            reduce(
                lambda a, f: a + [f(a[-1])],
                repeat(cantor, m),
                [[(True, 3 ** m)]]
            )
        )]
    )


# showCantor :: [(Bool, Int)] -> String
def showCantor(xs):
    '''A text block display of a list of
       Cantor line segments.
    '''
    return ''.join(
        concatMap(lambda tpl: tpl[1] * ('█' if tpl[0] else ' '))(
            xs
        )
    )


# main :: IO ()
def main():
    '''Testing to depth 5'''

    print(
        cantorLines(5)
    )


# GENERIC -------------------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    chain = itertools.chain
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''Cantor set – strings as both model and display.'''

from itertools import (chain, islice)


# cantorLines :: Int -> String
def cantorLines(n):
    '''N levels of cantor segmentation,
       obtained and displayed in the
       form of lines of block characters.
    '''
    return '\n'.join(
        [''.join(x) for x in islice(
            iterate(cantor)(
                [3 ** (n - 1) * '█']
            ), n
        )]
    )


# cantor :: [String] -> [String]
def cantor(xs):
    '''A cantor line derived from its predecessor.'''
    def go(s):
        m = len(s) // 3
        blocks = s[0:m]
        return [
            blocks, m * ' ', blocks
        ] if '█' == s[0] else [s]
    return concatMap(go)(xs)


# MAIN ----------------------------------------------------
# main :: IO ()
def main():
    '''Testing cantor line generation to level 5'''

    print(
        cantorLines(5)
    )

# GENERIC -------------------------------------------------


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


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


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
'''A Cantor set generator, and two different
   representations of its output.
'''

from itertools import (islice, chain)
from fractions import Fraction
from functools import (reduce)


# ----------------------- CANTOR SET -----------------------

# cantor :: Generator [[(Fraction, Fraction)]]
def cantor():
    '''A non-finite stream of successive Cantor
       partitions of the line, in the form of
       lists of fraction pairs.
    '''
    def go(xy):
        (x, y) = xy
        third = Fraction(y - x, 3)
        return [(x, x + third), (y - third, y)]

    return iterate(
        concatMap(go)
    )(
        [(0, 1)]
    )


# fractionLists :: [(Fraction, Fraction)] -> String
def fractionLists(xs):
    '''A fraction pair representation of a
       Cantor-partitioned line.
    '''
    def go(xy):
        return ', '.join(map(showRatio, xy))
    return ' '.join('(' + go(x) + ')' for x in xs)


# intervalBars :: [(Fraction, Fraction)] -> String
def intervalBars(w):
    '''A block diagram representation of a
       Cantor-partitioned line.
    '''
    def go(xs):
        def show(a, tpl):
            [x, y] = [int(w * r) for r in tpl]
            return (
                y,
                (' ' * (x - a)) + ('█' * (y - x))
            )
        return mapAccumL(show)(0)(xs)
    return lambda xs: ''.join(go(xs)[1])


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Testing the generation of successive
       Cantor subdivisions of the line, and
       displaying them both as lines of fraction
       pairs and as graphic interval bars.
    '''
    xs = list(islice(cantor(), 4))
    w = max(xy[1].denominator for xy in xs[-1])
    print(
        '\n'.join(map(fractionLists, xs)),
        '\n'
    )
    print(
        '\n'.join(map(intervalBars(w), xs))
    )


# ------------------------ GENERIC -------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


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


# mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a list derived by a
       combined map and fold,
       with accumulation from left to right.
    '''
    def go(a, x):
        tpl = f(a[0], x)
        return (tpl[0], a[1] + [tpl[1]])
    return lambda acc: lambda xs: (
        reduce(go, xs, (acc, []))
    )


# showRatio :: Ratio -> String
def showRatio(r):
    '''String representation of the ratio r.'''
    d = r.denominator
    return str(r.numerator) + (
        '/' + str(d) if 1 != d else ''
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

