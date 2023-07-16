# Spiral matrix

## Task Link
[Rosetta Code - Spiral matrix](https://rosettacode.org/wiki/Spiral_matrix)

## Java Code
### java_code_1.txt
```java
public class Blah {

  public static void main(String[] args) {
    print2dArray(getSpiralArray(5));
  }

  public static int[][] getSpiralArray(int dimension) {
    int[][] spiralArray = new int[dimension][dimension];

    int numConcentricSquares = (int) Math.ceil((dimension) / 2.0);

    int j;
    int sideLen = dimension;
    int currNum = 0;

    for (int i = 0; i < numConcentricSquares; i++) {
      // do top side
      for (j = 0; j < sideLen; j++) {
        spiralArray[i][i + j] = currNum++;
      }

      // do right side
      for (j = 1; j < sideLen; j++) {
        spiralArray[i + j][dimension - 1 - i] = currNum++;
      }

      // do bottom side
      for (j = sideLen - 2; j > -1; j--) {
        spiralArray[dimension - 1 - i][i + j] = currNum++;
      }

      // do left side
      for (j = sideLen - 2; j > 0; j--) {
        spiralArray[i + j][i] = currNum++;
      }

      sideLen -= 2;
    }

    return spiralArray;
  }

  public static void print2dArray(int[][] array) {
    for (int[] row : array) {
      for (int elem : row) {
        System.out.printf("%3d", elem);
      }
      System.out.println();
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
def spiral(n):
    dx,dy = 1,0            # Starting increments
    x,y = 0,0              # Starting location
    myarray = [[None]* n for j in range(n)]
    for i in xrange(n**2):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray

def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print "%2i" % myarray[x][y],
        print

printspiral(spiral(5))

```

### python_code_2.txt
```python
def spiral(n):
    def spiral_part(x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x+1) and x < (n // 2):
            return spiral_part(x-1, y-1, n-1) + 4*(n-y)
        if x < (n-y) and y <= x:
            return spiral_part(y-1, y, n) + (x-y) + 1
        if x >= (n-y) and y <= x:
            return spiral_part(x, y-1, n) + 1
        if x >= (n-y) and y > x:
            return spiral_part(x+1, y, n) + 1
        if x < (n-y) and y > x:
            return spiral_part(x, y-1, n) - 1

    array = [[0] * n for j in xrange(n)]
    for x in xrange(n):
        for y in xrange(n):
            array[x][y] = spiral_part(y, x, n)
    return array

for row in spiral(5):
    print " ".join("%2s" % x for x in row)

```

### python_code_3.txt
```python
def rot_right(a):
    return zip(*a[::-1])

def sp(m, n, start = 0):
    """ Generate number range spiral of dimensions m x n
    """
    if n == 0:
        yield ()
    else:
        yield tuple(range(start, m + start))
        for row in rot_right(list(sp(n - 1, m, m + start))):
            yield row

def spiral(m):
    return sp(m, m)

for row in spiral(5):
    print(''.join('%3i' % i for i in row))

```

### python_code_4.txt
```python
def spiral(n):
    dat = [[None] * n for i in range(n)]
    le = [[i + 1, i + 1] for i in reversed(range(n))]
    le = sum(le, [])[1:]  # for n = 5 le will be [5, 4, 4, 3, 3, 2, 2, 1, 1]
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]] * ((len(le) + 4) / 4)  # long enough
    x, y, val = -1, 0, -1
    for steps, (dx, dy) in zip(le, dxdy):
        x, y, val = x + dx, y + dy, val + 1
        for j in range(steps):
            dat[y][x] = val
            if j != steps-1:
                x, y, val = x + dx, y + dy, val + 1
    return dat

for row in spiral(5): # calc spiral and print it
    print ' '.join('%3s' % x for x in row)

```

### python_code_5.txt
```python
import itertools

concat = itertools.chain.from_iterable
def partial_sums(items):
    s = 0
    for x in items:
        s += x
        yield s

grade = lambda xs: sorted(range(len(xs)), key=xs.__getitem__)
values = lambda n: itertools.cycle([1,n,-1,-n])
counts = lambda n: concat([i,i-1] for i in range(n,0,-1))
reshape = lambda n, xs: zip(*([iter(xs)] * n))

spiral = lambda n: reshape(n, grade(list(partial_sums(concat(
                       [v]*c for c,v in zip(counts(n), values(n)))))))

for row in spiral(5):
    print(' '.join('%3s' % x for x in row))

```

### python_code_6.txt
```python
'''Spiral Matrix'''


# spiral :: Int -> [[Int]]
def spiral(n):
    '''The rows of a spiral matrix of order N.
    '''
    def go(rows, cols, x):
        return [range(x, x + cols)] + [
            reversed(x) for x
            in zip(*go(cols, rows - 1, x + cols))
        ] if 0 < rows else [[]]
    return go(n, n, 0)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Spiral matrix of order 5, in wiki table markup.
    '''
    print(
        wikiTable(spiral(5))
    )


# ---------------------- FORMATTING ----------------------

# wikiTable :: [[a]] -> String
def wikiTable(rows):
    '''Wiki markup for a no-frills tabulation of rows.'''
    return '{| class="wikitable" style="' + (
        'width:12em;height:12em;table-layout:fixed;"|-\n'
    ) + '\n|-\n'.join(
        '| ' + ' || '.join(
            str(cell) for cell in row
        )
        for row in rows
    ) + '\n|}'


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_7.txt
```python
def spiral_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m
for i in spiral_matrix(5): print(*i)

```

