# Circles of given radius through two points

## Task Link
[Rosetta Code - Circles of given radius through two points](https://rosettacode.org/wiki/Circles_of_given_radius_through_two_points)

## Java Code
### java_code_1.txt
```java
import java.util.Objects;

public class Circles {
    private static class Point {
        private final double x, y;

        public Point(Double x, Double y) {
            this.x = x;
            this.y = y;
        }

        public double distanceFrom(Point other) {
            double dx = x - other.x;
            double dy = y - other.y;
            return Math.sqrt(dx * dx + dy * dy);
        }

        @Override
        public boolean equals(Object other) {
            if (this == other) return true;
            if (other == null || getClass() != other.getClass()) return false;
            Point point = (Point) other;
            return x == point.x && y == point.y;
        }

        @Override
        public String toString() {
            return String.format("(%.4f, %.4f)", x, y);
        }
    }

    private static Point[] findCircles(Point p1, Point p2, double r) {
        if (r < 0.0) throw new IllegalArgumentException("the radius can't be negative");
        if (r == 0.0 && p1 != p2) throw new IllegalArgumentException("no circles can ever be drawn");
        if (r == 0.0) return new Point[]{p1, p1};
        if (Objects.equals(p1, p2)) throw new IllegalArgumentException("an infinite number of circles can be drawn");
        double distance = p1.distanceFrom(p2);
        double diameter = 2.0 * r;
        if (distance > diameter) throw new IllegalArgumentException("the points are too far apart to draw a circle");
        Point center = new Point((p1.x + p2.x) / 2.0, (p1.y + p2.y) / 2.0);
        if (distance == diameter) return new Point[]{center, center};
        double mirrorDistance = Math.sqrt(r * r - distance * distance / 4.0);
        double dx = (p2.x - p1.x) * mirrorDistance / distance;
        double dy = (p2.y - p1.y) * mirrorDistance / distance;
        return new Point[]{
            new Point(center.x - dy, center.y + dx),
            new Point(center.x + dy, center.y - dx)
        };
    }

    public static void main(String[] args) {
        Point[] p = new Point[]{
            new Point(0.1234, 0.9876),
            new Point(0.8765, 0.2345),
            new Point(0.0000, 2.0000),
            new Point(0.0000, 0.0000)
        };
        Point[][] points = new Point[][]{
            {p[0], p[1]},
            {p[2], p[3]},
            {p[0], p[0]},
            {p[0], p[1]},
            {p[0], p[0]},
        };
        double[] radii = new double[]{2.0, 1.0, 2.0, 0.5, 0.0};
        for (int i = 0; i < radii.length; ++i) {
            Point p1 = points[i][0];
            Point p2 = points[i][1];
            double r = radii[i];
            System.out.printf("For points %s and %s with radius %f\n", p1, p2, r);
            try {
                Point[] circles = findCircles(p1, p2, r);
                Point c1 = circles[0];
                Point c2 = circles[1];
                if (Objects.equals(c1, c2)) {
                    System.out.printf("there is just one circle with center at %s\n", c1);
                } else {
                    System.out.printf("there are two circles with centers at %s and %s\n", c1, c2);
                }
            } catch (IllegalArgumentException ex) {
                System.out.println(ex.getMessage());
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple
from math import sqrt

Pt = namedtuple('Pt', 'x, y')
Circle = Cir = namedtuple('Circle', 'x, y, r')

def circles_from_p1p2r(p1, p2, r):
    'Following explanation at http://mathforum.org/library/drmath/view/53027.html'
    if r == 0.0:
        raise ValueError('radius of zero')
    (x1, y1), (x2, y2) = p1, p2
    if p1 == p2:
        raise ValueError('coincident points gives infinite number of Circles')
    # delta x, delta y between points
    dx, dy = x2 - x1, y2 - y1
    # dist between points
    q = sqrt(dx**2 + dy**2)
    if q > 2.0*r:
        raise ValueError('separation of points > diameter')
    # halfway point
    x3, y3 = (x1+x2)/2, (y1+y2)/2
    # distance along the mirror line
    d = sqrt(r**2-(q/2)**2)
    # One answer
    c1 = Cir(x = x3 - d*dy/q,
             y = y3 + d*dx/q,
             r = abs(r))
    # The other answer
    c2 = Cir(x = x3 + d*dy/q,
             y = y3 - d*dx/q,
             r = abs(r))
    return c1, c2

if __name__ == '__main__':
    for p1, p2, r in [(Pt(0.1234, 0.9876), Pt(0.8765, 0.2345), 2.0),
                      (Pt(0.0000, 2.0000), Pt(0.0000, 0.0000), 1.0),
                      (Pt(0.1234, 0.9876), Pt(0.1234, 0.9876), 2.0),
                      (Pt(0.1234, 0.9876), Pt(0.8765, 0.2345), 0.5),
                      (Pt(0.1234, 0.9876), Pt(0.1234, 0.9876), 0.0)]:
        print('Through points:\n  %r,\n  %r\n  and radius %f\nYou can construct the following circles:'
              % (p1, p2, r))
        try:
            print('  %r\n  %r\n' % circles_from_p1p2r(p1, p2, r))
        except ValueError as v:
            print('  ERROR: %s\n' % (v.args[0],))

```

