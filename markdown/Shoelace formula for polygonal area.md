# Shoelace formula for polygonal area

## Task Link
[Rosetta Code - Shoelace formula for polygonal area](https://rosettacode.org/wiki/Shoelace_formula_for_polygonal_area)

## Java Code
### java_code_1.txt
```java
import java.util.List;

public class ShoelaceFormula {
    private static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", x, y);
        }
    }

    private static double shoelaceArea(List<Point> v) {
        int n = v.size();
        double a = 0.0;
        for (int i = 0; i < n - 1; i++) {
            a += v.get(i).x * v.get(i + 1).y - v.get(i + 1).x * v.get(i).y;
        }
        return Math.abs(a + v.get(n - 1).x * v.get(0).y - v.get(0).x * v.get(n - 1).y) / 2.0;
    }

    public static void main(String[] args) {
        List<Point> v = List.of(
            new Point(3, 4),
            new Point(5, 11),
            new Point(12, 8),
            new Point(9, 5),
            new Point(5, 6)
        );
        double area = shoelaceArea(v);
        System.out.printf("Given a polygon with vertices %s,%n", v);
        System.out.printf("its area is %f,%n", area);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def area_by_shoelace(x, y):
    "Assumes x,y points go around the polygon in one direction"
    return abs( sum(i * j for i, j in zip(x,             y[1:] + y[:1]))
               -sum(i * j for i, j in zip(x[1:] + x[:1], y            ))) / 2

>>> points = [(3,4), (5,11), (12,8), (9,5), (5,6)]
>>> x, y = zip(*points)
>>> area_by_shoelace(x, y)
30.0
>>>

```

### python_code_2.txt
```python
# Even simpler:
# In python we can take an advantage of that x[-1] refers to the last element in an array, same as x[N-1].
# Introducing the index i=[0,1,2,...,N-1]; i-1=[-1,0,...,N-2]; N is the number of vertices of a polygon.
# Thus x[i] is a sequence of the x-coordinate of the polygon vertices, x[i-1] is the sequence shifted by 1 index.
# Note that the shift must be negative. The positive shift x[i+1] results in an error: x[N] index out of bound.

import numpy as np
# x,y are arrays containing coordinates of the polygon vertices
x=np.array([3,5,12,9,5]) 
y=np.array([4,11,8,5,6]) 
i=np.arange(len(x))
#Area=np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5 # signed area, positive if the vertex sequence is counterclockwise
Area=np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5) # one line of code for the shoelace formula

# Remember that applying the Shoelace formula
# will result in a loss of precision if x,y have big offsets.
# Remove the offsets first, e.g. 
# x=x-np.mean(x);y=y-np.mean(y)
# or
# x=x-x[0];y=y-y[0]
# before applying the Shoelace formula.

```

### python_code_3.txt
```python
'''Polygonal area by shoelace formula'''

from itertools import cycle, islice
from functools import reduce
from operator import sub

# --------- SHOELACE FORMULA FOR POLYGONAL AREA ----------

# shoelaceArea :: [(Float, Float)] -> Float
def shoelaceArea(xys):
    '''Area of polygon with vertices
       at (x, y) points in xys.
    '''
    def go(a, tpl):
        l, r = a
        (x, y), (dx, dy) = tpl
        return l + x * dy, r + y * dx

    return abs(sub(*reduce(
        go,
        zip(
            xys,
            islice(cycle(xys), 1, None)
        ),
        (0, 0)
    ))) / 2


# ------------------------- TEST -------------------------
# main :: IO()
def main():
    '''Sample calculation'''

    ps = [(3, 4), (5, 11), (12, 8), (9, 5), (5, 6)]
    print(__doc__ + ':')
    print(repr(ps) + '  ->  ' + str(shoelaceArea(ps)))


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
>>> def area_by_shoelace2(x, y):
	return abs(sum(x[i-1]*y[i]-x[i]*y[i-1] for i in range(len(x)))) / 2.

>>> points = [(3,4), (5,11), (12,8), (9,5), (5,6)]
>>> x, y = zip(*points)
>>> area_by_shoelace2(x, y)
30.0
>>>

```

