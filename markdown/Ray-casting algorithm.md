# Ray-casting algorithm

## Task Link
[Rosetta Code - Ray-casting algorithm](https://rosettacode.org/wiki/Ray-casting_algorithm)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;

public class RayCasting {

    static boolean intersects(int[] A, int[] B, double[] P) {
        if (A[1] > B[1])
            return intersects(B, A, P);

        if (P[1] == A[1] || P[1] == B[1])
            P[1] += 0.0001;

        if (P[1] > B[1] || P[1] < A[1] || P[0] >= max(A[0], B[0]))
            return false;

        if (P[0] < min(A[0], B[0]))
            return true;

        double red = (P[1] - A[1]) / (double) (P[0] - A[0]);
        double blue = (B[1] - A[1]) / (double) (B[0] - A[0]);
        return red >= blue;
    }

    static boolean contains(int[][] shape, double[] pnt) {
        boolean inside = false;
        int len = shape.length;
        for (int i = 0; i < len; i++) {
            if (intersects(shape[i], shape[(i + 1) % len], pnt))
                inside = !inside;
        }
        return inside;
    }

    public static void main(String[] a) {
        double[][] testPoints = {{10, 10}, {10, 16}, {-20, 10}, {0, 10},
        {20, 10}, {16, 10}, {20, 20}};

        for (int[][] shape : shapes) {
            for (double[] pnt : testPoints)
                System.out.printf("%7s ", contains(shape, pnt));
            System.out.println();
        }
    }

    final static int[][] square = {{0, 0}, {20, 0}, {20, 20}, {0, 20}};

    final static int[][] squareHole = {{0, 0}, {20, 0}, {20, 20}, {0, 20},
    {5, 5}, {15, 5}, {15, 15}, {5, 15}};

    final static int[][] strange = {{0, 0}, {5, 5}, {0, 20}, {5, 15}, {15, 15},
    {20, 20}, {20, 0}};

    final static int[][] hexagon = {{6, 0}, {14, 0}, {20, 10}, {14, 20},
    {6, 20}, {0, 10}};

    final static int[][][] shapes = {square, squareHole, strange, hexagon};
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple
from pprint import pprint as pp
import sys

Pt = namedtuple('Pt', 'x, y')               # Point
Edge = namedtuple('Edge', 'a, b')           # Polygon edge from a to b
Poly = namedtuple('Poly', 'name, edges')    # Polygon

_eps = 0.00001
_huge = sys.float_info.max
_tiny = sys.float_info.min

def rayintersectseg(p, edge):
    ''' takes a point p=Pt() and an edge of two endpoints a,b=Pt() of a line segment returns boolean
    '''
    a,b = edge
    if a.y > b.y:
        a,b = b,a
    if p.y == a.y or p.y == b.y:
        p = Pt(p.x, p.y + _eps)

    intersect = False

    if (p.y > b.y or p.y < a.y) or (
        p.x > max(a.x, b.x)):
        return False

    if p.x < min(a.x, b.x):
        intersect = True
    else:
        if abs(a.x - b.x) > _tiny:
            m_red = (b.y - a.y) / float(b.x - a.x)
        else:
            m_red = _huge
        if abs(a.x - p.x) > _tiny:
            m_blue = (p.y - a.y) / float(p.x - a.x)
        else:
            m_blue = _huge
        intersect = m_blue >= m_red
    return intersect

def _odd(x): return x%2 == 1

def ispointinside(p, poly):
    ln = len(poly)
    return _odd(sum(rayintersectseg(p, edge)
                    for edge in poly.edges ))

def polypp(poly):
    print ("\n  Polygon(name='%s', edges=(" % poly.name)
    print ('   ', ',\n    '.join(str(e) for e in poly.edges) + '\n    ))')

if __name__ == '__main__':
    polys = [
      Poly(name='square', edges=(
        Edge(a=Pt(x=0, y=0), b=Pt(x=10, y=0)),
        Edge(a=Pt(x=10, y=0), b=Pt(x=10, y=10)),
        Edge(a=Pt(x=10, y=10), b=Pt(x=0, y=10)),
        Edge(a=Pt(x=0, y=10), b=Pt(x=0, y=0))
        )),
      Poly(name='square_hole', edges=(
        Edge(a=Pt(x=0, y=0), b=Pt(x=10, y=0)),
        Edge(a=Pt(x=10, y=0), b=Pt(x=10, y=10)),
        Edge(a=Pt(x=10, y=10), b=Pt(x=0, y=10)),
        Edge(a=Pt(x=0, y=10), b=Pt(x=0, y=0)),
        Edge(a=Pt(x=2.5, y=2.5), b=Pt(x=7.5, y=2.5)),
        Edge(a=Pt(x=7.5, y=2.5), b=Pt(x=7.5, y=7.5)),
        Edge(a=Pt(x=7.5, y=7.5), b=Pt(x=2.5, y=7.5)),
        Edge(a=Pt(x=2.5, y=7.5), b=Pt(x=2.5, y=2.5))
        )),
      Poly(name='strange', edges=(
        Edge(a=Pt(x=0, y=0), b=Pt(x=2.5, y=2.5)),
        Edge(a=Pt(x=2.5, y=2.5), b=Pt(x=0, y=10)),
        Edge(a=Pt(x=0, y=10), b=Pt(x=2.5, y=7.5)),
        Edge(a=Pt(x=2.5, y=7.5), b=Pt(x=7.5, y=7.5)),
        Edge(a=Pt(x=7.5, y=7.5), b=Pt(x=10, y=10)),
        Edge(a=Pt(x=10, y=10), b=Pt(x=10, y=0)),
        Edge(a=Pt(x=10, y=0), b=Pt(x=2.5, y=2.5))
        )),
      Poly(name='exagon', edges=(
        Edge(a=Pt(x=3, y=0), b=Pt(x=7, y=0)),
        Edge(a=Pt(x=7, y=0), b=Pt(x=10, y=5)),
        Edge(a=Pt(x=10, y=5), b=Pt(x=7, y=10)),
        Edge(a=Pt(x=7, y=10), b=Pt(x=3, y=10)),
        Edge(a=Pt(x=3, y=10), b=Pt(x=0, y=5)),
        Edge(a=Pt(x=0, y=5), b=Pt(x=3, y=0))
        )),
      ]
    testpoints = (Pt(x=5, y=5), Pt(x=5, y=8),
                  Pt(x=-10, y=5), Pt(x=0, y=5),
                  Pt(x=10, y=5), Pt(x=8, y=5),
                  Pt(x=10, y=10))
    
    print ("\n TESTING WHETHER POINTS ARE WITHIN POLYGONS")
    for poly in polys:
        polypp(poly)
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[:3]))
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[3:6]))
        print ('   ', '\t'.join("%s: %s" % (p, ispointinside(p, poly))
                               for p in testpoints[6:]))

```

### python_code_2.txt
```python
def _convert_fortran_shapes():
    point = Pt
    pts = (point(0,0), point(10,0), point(10,10), point(0,10), 
           point(2.5,2.5), point(7.5,2.5), point(7.5,7.5), point(2.5,7.5), 
           point(0,5), point(10,5), 
           point(3,0), point(7,0), point(7,10), point(3,10))
    p = (point(5,5), point(5, 8), point(-10, 5), point(0,5), point(10,5),
         point(8,5), point(10,10) )
 
    def create_polygon(pts,vertexindex):
        return [tuple(Edge(pts[vertexindex[i]-1], pts[vertexindex[i+1]-1])
                       for i in range(0, len(vertexindex), 2) )]
    polys=[]
    polys += create_polygon(pts, ( 1,2, 2,3, 3,4, 4,1 ) )
    polys += create_polygon(pts, ( 1,2, 2,3, 3,4, 4,1, 5,6, 6,7, 7,8, 8,5 ) )
    polys += create_polygon(pts, ( 1,5, 5,4, 4,8, 8,7, 7,3, 3,2, 2,5 ) )
    polys += create_polygon(pts, ( 11,12, 12,10, 10,13, 13,14, 14,9, 9,11 ) )

    names = ( "square", "square_hole", "strange", "exagon" )
    polys = [Poly(name, edges)
             for name, edges in zip(names, polys)]
    print 'polys = ['
    for p in polys:
        print "  Poly(name='%s', edges=(" % p.name
        print '   ', ',\n    '.join(str(e) for e in p.edges) + '\n    )),'
    print '  ]'
 _convert_fortran_shapes()

```

