# Find the intersection of two lines

## Task Link
[Rosetta Code - Find the intersection of two lines](https://rosettacode.org/wiki/Find_the_intersection_of_two_lines)

## Java Code
### java_code_1.txt
```java
public class Intersection {
    private static class Point {
        double x, y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return String.format("{%f, %f}", x, y);
        }
    }

    private static class Line {
        Point s, e;

        Line(Point s, Point e) {
            this.s = s;
            this.e = e;
        }
    }

    private static Point findIntersection(Line l1, Line l2) {
        double a1 = l1.e.y - l1.s.y;
        double b1 = l1.s.x - l1.e.x;
        double c1 = a1 * l1.s.x + b1 * l1.s.y;

        double a2 = l2.e.y - l2.s.y;
        double b2 = l2.s.x - l2.e.x;
        double c2 = a2 * l2.s.x + b2 * l2.s.y;

        double delta = a1 * b2 - a2 * b1;
        return new Point((b2 * c1 - b1 * c2) / delta, (a1 * c2 - a2 * c1) / delta);
    }

    public static void main(String[] args) {
        Line l1 = new Line(new Point(4, 0), new Point(6, 10));
        Line l2 = new Line(new Point(0, 3), new Point(10, 7));
        System.out.println(findIntersection(l1, l2));

        l1 = new Line(new Point(0, 0), new Point(1, 1));
        l2 = new Line(new Point(1, 2), new Point(4, 5));
        System.out.println(findIntersection(l1, l2));
    }
}

```

### java_code_2.txt
```java
void setup() {
  // test lineIntersect() with visual and textual output
  float lineA[] = {4, 0, 6, 10};  // try 4, 0, 6, 4
  float lineB[] = {0, 3, 10, 7};  // for non intersecting test
  PVector pt = lineInstersect(lineA[0], lineA[1], lineA[2], lineA[3], 
                              lineB[0], lineB[1], lineB[2], lineB[3]);
  scale(9);
  line(lineA[0], lineA[1], lineA[2], lineA[3]);
  line(lineB[0], lineB[1], lineB[2], lineB[3]);
  if (pt != null) {
    stroke(255);
    point(pt.x, pt.y);
    println(pt.x, pt.y);
  } else {
    println("No point");
  }
}

PVector lineInstersect(float Ax1, float Ay1, float Ax2, float Ay2, 
  float  Bx1, float By1, float Bx2, float By2) {
  // returns null if there is no intersection
  float uA, uB;
  float d = ((By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1));
  if (d != 0) {
    uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d;         
    uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d;
  } else {
    return null;
  }
  if (0 > uA || uA > 1 || 0 > uB || uB > 1) {
    return null;
  }
  float x = Ax1 + uA * (Ax2 - Ax1);
  float y = Ay1 + uA * (Ay2 - Ay1);
  return new PVector(x, y);
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division

def setup():
    """ test line_intersect() with visual and textual output """
    (a, b), (c, d) = (4, 0), (6, 10)  # try (4, 0), (6, 4)
    (e, f), (g, h) = (0, 3), (10, 7)  # for non intersecting test
    pt = line_instersect(a, b, c, d, e, f, g, h)
    scale(9)
    line(a, b, c, d)
    line(e, f, g, h)
    if pt:
        x, y = pt
        stroke(255)
        point(x, y)
    println(pt)  # prints x, y coordinates or 'None'

def line_instersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    return x, y

```

### python_code_2.txt
```python
def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    """ returns a (x, y) tuple or None if there is no intersection """
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    
    return x, y

if __name__ == '__main__':
    (a, b), (c, d) = (4, 0), (6, 10)  # try (4, 0), (6, 4)
    (e, f), (g, h) = (0, 3), (10, 7)  # for non intersecting test
    pt = line_intersect(a, b, c, d, e, f, g, h)
    print(pt)

```

### python_code_3.txt
```python
'''The intersection of two lines.'''

from itertools import product


# intersection :: Line -> Line -> Either String Point
def intersection(ab):
    '''Either the point at which the lines ab and pq
       intersect, or a message string indicating that
       they are parallel and have no intersection.'''
    def delta(f):
        return lambda x: f(fst(x)) - f(snd(x))

    def prodDiff(abcd):
        [a, b, c, d] = abcd
        return (a * d) - (b * c)

    def go(pq):
        [abDX, pqDX, abDY, pqDY] = apList(
            [delta(fst), delta(snd)]
        )([ab, pq])
        determinant = prodDiff([abDX, abDY, pqDX, pqDY])

        def point():
            [abD, pqD] = map(
                lambda xy: prodDiff(
                    apList([fst, snd])([fst(xy), snd(xy)])
                ), [ab, pq]
            )
            return apList(
                [lambda abpq: prodDiff(
                    [abD, fst(abpq), pqD, snd(abpq)]) / determinant]
            )(
                [(abDX, pqDX), (abDY, pqDY)]
            )
        return Right(point()) if 0 != determinant else Left(
            '( Parallel lines - no intersection )'
        )

    return lambda pq: bindLR(go(pq))(
        lambda xs: Right((fst(xs), snd(xs)))
    )


# --------------------------TEST---------------------------
# main :: IO()
def main():
    '''Test'''

    # Left(message - no intersection) or Right(point)
    # lrPoint :: Either String Point
    lrPoint = intersection(
        ((4.0, 0.0), (6.0, 10.0))
    )(
        ((0.0, 3.0), (10.0, 7.0))
    )
    print(
        lrPoint['Left'] or lrPoint['Right']
    )


# --------------------GENERIC FUNCTIONS--------------------

# Left :: a -> Either a b
def Left(x):
    '''Constructor for an empty Either (option type) value
       with an associated string.'''
    return {'type': 'Either', 'Right': None, 'Left': x}


# Right :: b -> Either a b
def Right(x):
    '''Constructor for a populated Either (option type) value'''
    return {'type': 'Either', 'Left': None, 'Right': x}


# apList (<*>) :: [(a -> b)] -> [a] -> [b]
def apList(fs):
    '''The application of each of a list of functions,
       to each of a list of values.
    '''
    def go(fx):
        f, x = fx
        return f(x)
    return lambda xs: [
        go(x) for x
        in product(fs, xs)
    ]


# bindLR (>>=) :: Either a -> (a -> Either b) -> Either b
def bindLR(m):
    '''Either monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.'''
    return lambda mf: (
        mf(m.get('Right')) if None is m.get('Left') else m
    )


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
from shapely.geometry import LineString

if __name__ == "__main__":
    line1 = LineString([(4, 0), (6, 10)])
    line2 = LineString([(0, 3), (10, 7)])
    print(line1.intersection(line2))

```

