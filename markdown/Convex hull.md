# Convex hull

## Task Link
[Rosetta Code - Convex hull](https://rosettacode.org/wiki/Convex_hull)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import static java.util.Collections.emptyList;

public class ConvexHull {
    private static class Point implements Comparable<Point> {
        private int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point o) {
            return Integer.compare(x, o.x);
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", x, y);
        }
    }

    private static List<Point> convexHull(List<Point> p) {
        if (p.isEmpty()) return emptyList();
        p.sort(Point::compareTo);
        List<Point> h = new ArrayList<>();

        // lower hull
        for (Point pt : p) {
            while (h.size() >= 2 && !ccw(h.get(h.size() - 2), h.get(h.size() - 1), pt)) {
                h.remove(h.size() - 1);
            }
            h.add(pt);
        }

        // upper hull
        int t = h.size() + 1;
        for (int i = p.size() - 1; i >= 0; i--) {
            Point pt = p.get(i);
            while (h.size() >= t && !ccw(h.get(h.size() - 2), h.get(h.size() - 1), pt)) {
                h.remove(h.size() - 1);
            }
            h.add(pt);
        }

        h.remove(h.size() - 1);
        return h;
    }

    // ccw returns true if the three points make a counter-clockwise turn
    private static boolean ccw(Point a, Point b, Point c) {
        return ((b.x - a.x) * (c.y - a.y)) > ((b.y - a.y) * (c.x - a.x));
    }

    public static void main(String[] args) {
        List<Point> points = Arrays.asList(new Point(16, 3),
                                           new Point(12, 17),
                                           new Point(0, 6),
                                           new Point(-4, -6),
                                           new Point(16, 6),

                                           new Point(16, -7),
                                           new Point(16, -3),
                                           new Point(17, -4),
                                           new Point(5, 19),
                                           new Point(19, -8),

                                           new Point(3, 16),
                                           new Point(12, 13),
                                           new Point(3, -4),
                                           new Point(17, 5),
                                           new Point(-3, 15),

                                           new Point(-3, -9),
                                           new Point(0, 11),
                                           new Point(-9, -3),
                                           new Point(-4, -2),
                                           new Point(12, 10));

        List<Point> hull = convexHull(points);
        System.out.printf("Convex Hull: %s\n", hull);
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
from shapely.geometry import MultiPoint

if __name__=="__main__":
	pts = MultiPoint([(16,3), (12,17), (0,6), (-4,-6), (16,6), (16,-7), (16,-3), (17,-4), (5,19), (19,-8), (3,16), (12,13), (3,-4), (17,5), (-3,15), (-3,-9), (0,11), (-9,-3), (-4,-2), (12,10)])
	print (pts.convex_hull)

```

