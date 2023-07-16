# N-queens problem

## Task Link
[Rosetta Code - N-queens problem](https://rosettacode.org/wiki/N-queens_problem)

## Java Code
### java_code_1.txt
```java
public class NQueens {

  private static int[] b = new int[8];
  private static int s = 0;

  static boolean unsafe(int y) {
    int x = b[y];
    for (int i = 1; i <= y; i++) {
      int t = b[y - i];
      if (t == x ||
          t == x - i ||
          t == x + i) {
        return true;
      }
    }

    return false;
  }

  public static void putboard() {
    System.out.println("\n\nSolution " + (++s));
    for (int y = 0; y < 8; y++) {
      for (int x = 0; x < 8; x++) {
        System.out.print((b[y] == x) ? "|Q" : "|_");
      }
      System.out.println("|");
    }
  }

  public static void main(String[] args) {
    int y = 0;
    b[0] = -1;
    while (y >= 0) {
      do {
        b[y]++;
      } while ((b[y] < 8) && unsafe(y));
      if (b[y] < 8) {
        if (y < 7) {
          b[++y] = -1;
        } else {
          putboard();
        }
      } else {
        y--;
      }
    }
  }
}

```

### java_code_2.txt
```java
int n = 8;
int[] b = new int[n];
int s = 0;
int y = 0;

void setup() {
  size(400, 400);
  textAlign(CENTER, CENTER);
  textFont(createFont("DejaVu Sans", 44));
  b[0] = -1;
}

void draw() {
  if (y >= 0) {
    do {
      b[y]++;
    } while ((b[y] < n) && unsafe(y));
    if (b[y] < n) {
      if (y < (n-1)) {
        b[++y] = -1;
      } else {
        drawBoard();
      }
    } else {
      y--;
    }
  } else { 
    textSize(18);
    text("Press any key to restart", width / 2, height - 20);
  }
} 


boolean unsafe(int y) {
  int x = b[y];
  for (int i = 1; i <= y; i++) {
    int t = b[y - i];
    if (t == x ||
      t == x - i ||
      t == x + i) {
      return true;
    }
  }
  return false;
}

void drawBoard() {
  float w = width / n;
  for (int y = 0; y < n; y++) {
    for (int x = 0; x < n; x++) {
      fill(255 * ((x + y) % 2));
      square(x * w, y * w, w);
      if (b[y] == x) {
        fill(255 - 255 * ((x + y) % 2));
        textSize(42);
        text("♕", w / 2 +  x *w, w /2 + y * w);
      }
    }
  }
  fill(255, 0, 0);
  textSize(18);
  text("Solution " + (++s), width / 2, height / 90);
}

void keyPressed() {
  b = new int[n];
  s = 0;
  y = 0;
  b[0] = -1;
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations, product

n = 8
cols = range(n)
i = 0  # solution shown

solutions = [vec for vec in permutations(cols)
             if n == len(set(vec[i] + i for i in cols))
                  == len(set(vec[i] - i for i in cols))]

def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    textFont(createFont("DejaVu Sans", 44))

def draw():
    background(0)
    w = width / n
    for x, y in product(range(n), range(n)):
        fill(255 * ((x + y) % 2))
        square(x * w, y * w, w)
        if solutions[i][y] == x:
            fill(255 - 255 * ((x + y) % 2))
            text(u'♕', w / 2 + x * w, w / 3 + y * w)

def keyPressed():  # show next solution
    global i
    i = (i + 1) % len(solutions)

```

### python_code_10.txt
```python
'''N Queens problem'''

from functools import reduce
from itertools import chain


# queenPuzzle :: Int -> Int -> [[Int]]
def queenPuzzle(nCols):
    '''All board patterns of this dimension
       in which no two Queens share a row,
       column, or diagonal.
    '''
    def go(nRows):
        lessRows = nRows - 1
        return reduce(
            lambda a, xys: a + reduce(
                lambda b, iCol: b + [xys + [iCol]] if (
                    safe(lessRows, iCol, xys)
                ) else b,
                enumFromTo(1)(nCols),
                []
            ),
            go(lessRows),
            []
        ) if 0 < nRows else [[]]
    return go


# safe :: Int -> Int -> [Int] -> Bool
def safe(iRow, iCol, pattern):
    '''True if no two queens in the pattern
       share a row, column or diagonal.
    '''
    def p(sc, sr):
        return (iCol == sc) or (
            sc + sr == (iCol + iRow)
        ) or (sc - sr == (iCol - iRow))
    return not any(map(p, pattern, range(0, iRow)))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Number of solutions for boards of various sizes'''

    n = 5
    xs = queenPuzzle(n)(n)

    print(
        str(len(xs)) + ' solutions for a {n} * {n} board:\n'.format(n=n)
    )
    print(showBoards(10)(xs))

    print(
        fTable(
            '\n\n' + main.__doc__ + ':\n'
        )(str)(lambda n: str(n).rjust(3, ' '))(
            lambda n: len(queenPuzzle(n)(n))
        )(enumFromTo(1)(10))
    )


# ---------------------- FORMATTING ----------------------

# showBoards :: Int -> [[Int]] -> String
def showBoards(nCols):
    '''String representation, with N columns
       of a set of board patterns.
    '''
    def showBlock(b):
        return '\n'.join(map(intercalate('  '), zip(*b)))

    def go(bs):
        return '\n\n'.join(map(
            showBlock,
            chunksOf(nCols)([
                showBoard(b) for b in bs
            ])
        ))
    return go


# showBoard :: [Int] -> String
def showBoard(xs):
    '''String representation of a Queens board.'''
    lng = len(xs)

    def showLine(n):
        return ('.' * (n - 1)) + '♛' + ('.' * (lng - n))
    return map(showLine, xs)


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


# ----------------------- GENERIC ------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# intercalate :: [a] -> [[a]] -> [a]
# intercalate :: String -> [String] -> String
def intercalate(x):
    '''The concatenation of xs
       interspersed with copies of x.
    '''
    return lambda xs: x.join(xs) if isinstance(x, str) else list(
        chain.from_iterable(
            reduce(lambda a, v: a + [x, v], xs[1:], [xs[0]])
        )
    ) if xs else []


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
from itertools import permutations

n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        print ( vec )

```

### python_code_3.txt
```python
def board(vec):
    print ("\n".join('.' * i + 'Q' + '.' * (n-i-1) for i in vec) + "\n===\n")

```

### python_code_4.txt
```python
# From: http://wiki.python.org/moin/SimplePrograms, with permission from the author, Steve Howell
BOARD_SIZE = 8

def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution+[i+1]
                       for solution in solutions
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution)]
    return solutions

for answer in solve(BOARD_SIZE): print(list(enumerate(answer, start=1)))

```

### python_code_5.txt
```python
BOARD_SIZE = 8

def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution+[i+1]
                       for solution in solutions # first for clause is evaluated immediately,
                                                 # so "solutions" is correctly captured
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution))
    return solutions

answers = solve(BOARD_SIZE)
first_answer = next(answers)
print(list(enumerate(first_answer, start=1)))

```

### python_code_6.txt
```python
def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

for solution in queens(8, 0, [], [], []):
    print(solution)

```

### python_code_7.txt
```python
def queens(x, i, a, b, c):
    if a:  # a is not empty
        for j in a:
            if i + j not in b and i - j not in c:
                yield from queens(x + [j], i + 1, a - {j}, b | {i + j}, c | {i - j})
    else:
        yield x

for solution in queens([], 0, set(range(8)), set(), set()):
    print(solution)

```

### python_code_8.txt
```python
def queens(n):
    a = list(range(n))
    up = [True]*(2*n - 1)
    down = [True]*(2*n - 1)
    def sub(i):
        if i == n:
            yield tuple(a)
        else:
            for k in range(i, n):
                j = a[k]
                p = i + j
                q = i - j + n - 1
                if up[p] and down[q]:
                    up[p] = down[q] = False
                    a[i], a[k] = a[k], a[i]
                    yield from sub(i + 1)
                    up[p] = down[q] = True
                    a[i], a[k] = a[k], a[i]
    yield from sub(0)

#Count solutions for n=8:
sum(1 for p in queens(8))
92

```

### python_code_9.txt
```python
def queens_lex(n):
    a = list(range(n))
    up = [True]*(2*n - 1)
    down = [True]*(2*n - 1)
    def sub(i):
        if i == n:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                j = a[i]
                p = i + j
                q = i - j + n - 1
                if up[p] and down[q]:
                    up[p] = down[q] = False
                    yield from sub(i + 1)
                    up[p] = down[q] = True
            x = a[i]
            for k in range(i + 1, n):
                a[k - 1] = a[k]
            a[n - 1] = x
    yield from sub(0)

next(queens(31))
(0, 2, 4, 1, 3, 8, 10, 12, 14, 6, 17, 21, 26, 28, 25, 27, 24, 30, 7, 5, 29, 15, 13, 11, 9, 18, 22, 19, 23, 16, 20)

next(queens_lex(31))
(0, 2, 4, 1, 3, 8, 10, 12, 14, 5, 17, 22, 25, 27, 30, 24, 26, 29, 6, 16, 28, 13, 9, 7, 19, 11, 15, 18, 21, 23, 20)

#Compare to A065188
#1, 3, 5, 2, 4, 9, 11, 13, 15, 6, 8, 19, 7, 22, 10, 25, 27, 29, 31, 12, 14, 35, 37, ...

```

