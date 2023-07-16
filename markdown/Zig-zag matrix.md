# Zig-zag matrix

## Task Link
[Rosetta Code - Zig-zag matrix](https://rosettacode.org/wiki/Zig-zag_matrix)

## Java Code
### java_code_1.txt
```java
public static int[][] Zig_Zag(final int size)
{
 int[][] data = new int[size][size];
 int i = 1;
 int j = 1;
 for (int element = 0; element < size * size; element++)
 {
  data[i - 1][j - 1] = element;
  if ((i + j) % 2 == 0)
  {
   // Even stripes
   if (j < size)
    j++;
   else
    i+= 2;
   if (i > 1)
    i--;
  }
  else
  {
   // Odd stripes
   if (i < size)
    i++;
   else
    j+= 2;
   if (j > 1)
    j--;
  }
 }
 return data;
}

```

## Python Code
### python_code_1.txt
```python
def zigzag(n):
    '''zigzag rows'''
    def compare(xy):
        x, y = xy
        return (x + y, -y if (x + y) % 2 else y)
    xs = range(n)
    return {index: n for n, index in enumerate(sorted(
        ((x, y) for x in xs for y in xs),
        key=compare
    ))}


def printzz(myarray):
    '''show zigzag rows as lines'''
    n = int(len(myarray) ** 0.5 + 0.5)
    xs = range(n)
    print('\n'.join(
        [''.join("%3i" % myarray[(x, y)] for x in xs) for y in xs]
    ))


printzz(zigzag(6))

```

### python_code_2.txt
```python
# pylint: disable=invalid-name
# pylint: disable=unused-argument
"ZigZag iterator."
import sys

if sys.version_info[0] >= 3:
    xrange = range

def move(x, y, columns, rows):
    "Tells us what to do next with x and y."
    if y < (rows - 1):
        return max(0, x-1), y+1
    return x+1, y

def zigzag(rows, columns):
    "ZigZag iterator, yields indices."
    x, y = 0, 0
    size = rows * columns
    for _ in xrange(size):
        yield y, x
        if (x + y) & 1:
            x, y = move(x, y, columns, rows)
        else:
            y, x = move(y, x, rows, columns)

# test code
i, rows, cols = 0, 5, 5
mat = [[0 for x in range(cols)] for y in range(rows)]
for (y, x) in zigzag(rows, cols):
    mat[y][x], i = i, i + 1

from pprint import pprint
pprint(mat)

```

### python_code_3.txt
```python
[[0, 1, 5, 6, 14],
 [2, 4, 7, 13, 15],
 [3, 8, 12, 16, 21],
 [9, 11, 17, 20, 22],
 [10, 18, 19, 23, 24]]

```

### python_code_4.txt
```python
COLS = 9
def CX(x, ran):
  while True:
    x += 2 * next(ran)
    yield x
    x += 1
    yield x
ran = []
d = -1
for V in CX(1,iter(list(range(0,COLS,2)) + list(range(COLS-1-COLS%2,0,-2)))):
  ran.append(iter(range(V, V+COLS*d, d)))
  d *= -1
for x in range(0,COLS):
  for y in range(x, x+COLS):
    print(repr(next(ran[y])).rjust(3), end = ' ')
  print()

```

### python_code_5.txt
```python
from __future__ import print_function

import math


def zigzag( dimension):
    ''' generate the zigzag indexes for a square array
        Exploiting the fact that an array is symmetrical around its
        centre
    '''
    NUMBER_INDEXES = dimension ** 2
    HALFWAY = NUMBER_INDEXES // 2
    KERNEL_ODD = dimension & 1

    xy = [0 for _ in range(NUMBER_INDEXES)]
    # start at 0,0
    ix = 0
    iy = 0
    # 'fake' that we are going up and right
    direction = 1
    # the first index is always 0, so start with the second
    # until halfway 
    for i in range(1, HALFWAY + KERNEL_ODD):
        if direction > 0:
            # going up and right
            if iy == 0:
                # are at top
                ix += 1
                direction = -1
            else:
                ix += 1
                iy -= 1 
        else:
            # going down and left
            if ix == 0:
                # are at left
                iy += 1
                direction = 1
            else:
                ix -= 1
                iy += 1
        # update the index position
        xy[iy * dimension + ix] = i

    # have first half, but they are scattered over the list
    # so find the zeros to replace
    for i in range(1, NUMBER_INDEXES):
        if xy[i] == 0 :
            xy[i] = NUMBER_INDEXES - 1 - xy[NUMBER_INDEXES - 1 - i]

    return xy


def main(dim):
    zz = zigzag(dim)
    print( 'zigzag of {}:'.format(dim))
    width = int(math.ceil(math.log10(dim**2)))
    for j in range(dim):
        for i in range(dim):
            print('{:{width}}'.format(zz[j * dim + i], width=width), end=' ')
        print()


if __name__ == '__main__':
    main(5)

```

