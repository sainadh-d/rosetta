# Sierpinski carpet

## Task Link
[Rosetta Code - Sierpinski carpet](https://rosettacode.org/wiki/Sierpinski_carpet)

## Java Code
### java_code_1.txt
```java
public static boolean inCarpet(long x, long y) {
    while (x!=0 && y!=0) {
        if (x % 3 == 1 && y % 3 == 1)
            return false;
        x /= 3;
        y /= 3;
    }
    return true;
}
 
public static void carpet(final int n) {
    final double power = Math.pow(3,n);
    for(long i = 0; i < power; i++) {
        for(long j = 0; j < power; j++) {
            System.out.print(inCarpet(i, j) ? "*" : " ");
        }
        System.out.println();
    }
}

```

### java_code_2.txt
```java
import java.awt.*;
import java.awt.event.ActionEvent;
import javax.swing.*;

public class SierpinskiCarpet extends JPanel {
    private final int dim = 513;
    private final int margin = 20;

    private int limit = dim;

    public SierpinskiCarpet() {
        setPreferredSize(new Dimension(dim + 2 * margin, dim + 2 * margin));
        setBackground(Color.white);
        setForeground(Color.orange);

        new Timer(2000, (ActionEvent e) -> {
            limit /= 3;
            if (limit <= 3)
                limit = dim;
            repaint();
        }).start();
    }

    void drawCarpet(Graphics2D g, int x, int y, int size) {
        if (size < limit)
            return;
        size /= 3;
        for (int i = 0; i < 9; i++) {
            if (i == 4) {
                g.fillRect(x + size, y + size, size, size);
            } else {
                drawCarpet(g, x + (i % 3) * size, y + (i / 3) * size, size);
            }
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        g.translate(margin, margin);
        drawCarpet(g, 0, 0, dim);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Sierpinski Carpet");
            f.setResizable(false);
            f.add(new SierpinskiCarpet(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_3.txt
```java
float delta;

void setup() {
  size(729, 729);
  fill(0);
  background(255);
  noStroke();
  rect(width/3, height/3, width/3, width/3);
  rectangles(width/3, height/3, width/3);
}

void rectangles(int x, int y, int s) {
  if (s < 1) return;
  int xc = x-s;
  int yc = y-s;
  for (int row = 0; row < 3; row++) {
    for (int col = 0; col < 3; col++) {
      if (!(row == 1 && col == 1)) {
        int xx = xc+row*s;
        int yy = yc+col*s;
        delta = s/3;
        rect(xx+delta, yy+delta, delta, delta);
        rectangles(xx+s/3, yy+s/3, s/3);
      }
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    size(729, 729)
    fill(0)
    background(255)
    noStroke()
    rect(width / 3, height / 3, width / 3, width / 3)
    rectangles(width / 3, height / 3, width / 3)

def rectangles(x, y, s):
    if s < 1: return
    xc, yc = x - s, y - s
    for row in range(3):
        for col in range(3):
            if not (row == 1 and col == 1):
                xx, yy = xc + row * s, yc + col * s
                delta = s / 3
                rect(xx + delta, yy + delta, delta, delta)
                rectangles(xx + s / 3, yy + s / 3, s / 3)

```

### python_code_2.txt
```python
def in_carpet(x, y):
    while True:
        if x == 0 or y == 0:
            return True
        elif x % 3 == 1 and y % 3 == 1:
            return False
        
        x /= 3
        y /= 3

def carpet(n):
    for i in xrange(3 ** n):
        for j in xrange(3 ** n):
            if in_carpet(i, j):
                print '*',
            else:
                print ' ',
        print

```

### python_code_3.txt
```python
def sierpinski_carpet(n):
  carpet = ["#"]
  for i in xrange(n):
    carpet = [x + x + x for x in carpet] + \
             [x + x.replace("#"," ") + x for x in carpet] + \
             [x + x + x for x in carpet]
  return "\n".join(carpet)

print sierpinski_carpet(3)

```

### python_code_4.txt
```python
'''Iterations of the Sierpinski carpet'''

from itertools import chain, islice
from inspect import signature
from operator import add


# sierpinskiCarpet :: Int -> [String]
def sierpinskiCarpet(n):
    '''A string representing the nth
       iteration of a Sierpinski carpet.
    '''
    f = zipWith(add)
    g = flip(f)

    # weave :: [String] -> [String]
    def weave(xs):
        return bind([
            xs,
            [' ' * len(s) for s in xs],
            xs
        ])(compose(g(xs))(f(xs)))

    return index(
        iterate(weave)(['▓▓'])
    )(n)


# TEST ----------------------------------------------------
def main():
    '''Test iteration of the Sierpinski carpet'''

    levels = enumFromTo(0)(3)
    t = ' ' * (
        len(' -> ') +
        max(map(compose(len)(str), levels))
    )
    print(
        fTable(__doc__ + ':')(lambda x: '\n' + str(x))(
            lambda xs: xs[0] + '\n' + (
                unlines(map(lambda x: t + x, xs[1:])))
        )
        (sierpinskiCarpet)(levels)
    )


# GENERIC -------------------------------------------------

# bind (>>=) :: [a] -> (a -> [b]) -> [b]
def bind(xs):
    '''List monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.'''
    return lambda f: list(chain.from_iterable(
        map(f, xs)
    ))


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.'''
    if 1 < len(signature(f).parameters):
        return lambda a, b: f(b, a)
    else:
        return lambda a: lambda b: f(b)(a)


# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
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


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    '''A list constructed by zipping with a
       custom function, rather than with the
       default tuple constructor.'''
    return lambda xs: lambda ys: (
        map(f, xs, ys)
    )


# OUTPUT FORMATTING ---------------------------------------

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

