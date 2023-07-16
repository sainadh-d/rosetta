# Total circles area

## Task Link
[Rosetta Code - Total circles area](https://rosettacode.org/wiki/Total_circles_area)

## Java Code
### java_code_1.txt
```java
public class CirclesTotalArea {

    /*
     * Rectangles are given as 4-element arrays [tx, ty, w, h].
     * Circles are given as 3-element arrays [cx, cy, r].
     */
    
    private static double distSq(double x1, double y1, double x2, double y2) {
        return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
    }
    
    private static boolean rectangleFullyInsideCircle(double[] rect, double[] circ) {
        double r2 = circ[2] * circ[2];
        // Every corner point of rectangle must be inside the circle.
        return distSq(rect[0], rect[1], circ[0], circ[1]) <= r2 &&
          distSq(rect[0] + rect[2], rect[1], circ[0], circ[1]) <= r2 &&
          distSq(rect[0], rect[1] - rect[3], circ[0], circ[1]) <= r2 &&
          distSq(rect[0] + rect[2], rect[1] - rect[3], circ[0], circ[1]) <= r2;
    }
    
    private static boolean rectangleSurelyOutsideCircle(double[] rect, double[] circ) {
        // Circle center point inside rectangle?
        if(rect[0] <= circ[0] && circ[0] <= rect[0] + rect[2] &&
          rect[1] - rect[3] <= circ[1] && circ[1] <= rect[1]) { return false; }
        // Otherwise, check that each corner is at least (r + Max(w, h)) away from circle center.
        double r2 = circ[2] + Math.max(rect[2], rect[3]);
        r2 = r2 * r2;
        return distSq(rect[0], rect[1], circ[0], circ[1]) >= r2 &&
          distSq(rect[0] + rect[2], rect[1], circ[0], circ[1]) >= r2 &&
          distSq(rect[0], rect[1] - rect[3], circ[0], circ[1]) >= r2 &&
          distSq(rect[0] + rect[2], rect[1] - rect[3], circ[0], circ[1]) >= r2;
    }
    
    private static boolean[] surelyOutside;
    
    private static double totalArea(double[] rect, double[][] circs, int d) {    
        // Check if we can get a quick certain answer.
        int surelyOutsideCount = 0;
        for(int i = 0; i < circs.length; i++) {
            if(rectangleFullyInsideCircle(rect, circs[i])) { return rect[2] * rect[3]; }
            if(rectangleSurelyOutsideCircle(rect, circs[i])) {
                surelyOutside[i] = true;
                surelyOutsideCount++;
            }
            else { surelyOutside[i] = false; }
        }
        // Is this rectangle surely outside all circles?
        if(surelyOutsideCount == circs.length) { return 0; }
        // Are we deep enough in the recursion?
        if(d < 1) { 
            return rect[2] * rect[3] / 3;  // Best guess for overlapping portion
        }
        // Throw out all circles that are surely outside this rectangle.
        if(surelyOutsideCount > 0) {
            double[][] newCircs = new double[circs.length - surelyOutsideCount][3];
            int loc = 0;
            for(int i = 0; i < circs.length; i++) {
                if(!surelyOutside[i]) { newCircs[loc++] = circs[i]; }
            }
            circs = newCircs;
        }
        // Subdivide this rectangle recursively and add up the recursively computed areas.
        double w = rect[2] / 2; // New width
        double h = rect[3] / 2; // New height
        double[][] pieces = {
            { rect[0], rect[1], w, h }, // NW
            { rect[0] + w, rect[1], w, h }, // NE
            { rect[0], rect[1] - h, w, h }, // SW
            { rect[0] + w, rect[1] - h, w, h } // SE
        };
        double total = 0;
        for(double[] piece: pieces) { total += totalArea(piece, circs, d - 1); }
        return total;
    }
    
    public static double totalArea(double[][] circs, int d) {
        double maxx = Double.NEGATIVE_INFINITY;
        double minx = Double.POSITIVE_INFINITY;
        double maxy = Double.NEGATIVE_INFINITY;
        double miny = Double.POSITIVE_INFINITY;
        // Find the extremes of x and y for this set of circles.
        for(double[] circ: circs) {
            if(circ[0] + circ[2] > maxx) { maxx = circ[0] + circ[2]; }
            if(circ[0] - circ[2] < minx) { minx = circ[0] - circ[2]; }
            if(circ[1] + circ[2] > maxy) { maxy = circ[1] + circ[2]; }
            if(circ[1] - circ[2] < miny) { miny = circ[1] - circ[2]; }
        }
        double[] rect = { minx, maxy, maxx - minx, maxy - miny };
        surelyOutside = new boolean[circs.length];
        return totalArea(rect, circs, d);
    }
    
    public static void main(String[] args) {
        double[][] circs = {
            { 1.6417233788, 1.6121789534, 0.0848270516 },
            {-1.4944608174, 1.2077959613, 1.1039549836 },
            { 0.6110294452, -0.6907087527, 0.9089162485 },
            { 0.3844862411, 0.2923344616, 0.2375743054 },
            {-0.2495892950, -0.3832854473, 1.0845181219 },
            {1.7813504266, 1.6178237031, 0.8162655711 },
            {-0.1985249206, -0.8343333301, 0.0538864941 },
            {-1.7011985145, -0.1263820964, 0.4776976918 },
            {-0.4319462812, 1.4104420482, 0.7886291537 },
            {0.2178372997, -0.9499557344, 0.0357871187 },
            {-0.6294854565, -1.3078893852, 0.7653357688 },
            {1.7952608455, 0.6281269104, 0.2727652452 },
            {1.4168575317, 1.0683357171, 1.1016025378 },
            {1.4637371396, 0.9463877418, 1.1846214562 },
            {-0.5263668798, 1.7315156631, 1.4428514068 },
            {-1.2197352481, 0.9144146579, 1.0727263474 },
            {-0.1389358881, 0.1092805780, 0.7350208828 },
            {1.5293954595, 0.0030278255, 1.2472867347 },
            {-0.5258728625, 1.3782633069, 1.3495508831 },
            {-0.1403562064, 0.2437382535, 1.3804956588 },
            {0.8055826339, -0.0482092025, 0.3327165165 },
            {-0.6311979224, 0.7184578971, 0.2491045282 },
            {1.4685857879, -0.8347049536, 1.3670667538 },
            {-0.6855727502, 1.6465021616, 1.0593087096 },
            {0.0152957411, 0.0638919221, 0.9771215985 }
        };
        double ans = totalArea(circs, 24);
        System.out.println("Approx. area is " + ans);
        System.out.println("Error is " + Math.abs(21.56503660 - ans));
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple

Circle = namedtuple("Circle", "x y r")

circles = [
    Circle( 1.6417233788,  1.6121789534, 0.0848270516),
    Circle(-1.4944608174,  1.2077959613, 1.1039549836),
    Circle( 0.6110294452, -0.6907087527, 0.9089162485),
    Circle( 0.3844862411,  0.2923344616, 0.2375743054),
    Circle(-0.2495892950, -0.3832854473, 1.0845181219),
    Circle( 1.7813504266,  1.6178237031, 0.8162655711),
    Circle(-0.1985249206, -0.8343333301, 0.0538864941),
    Circle(-1.7011985145, -0.1263820964, 0.4776976918),
    Circle(-0.4319462812,  1.4104420482, 0.7886291537),
    Circle( 0.2178372997, -0.9499557344, 0.0357871187),
    Circle(-0.6294854565, -1.3078893852, 0.7653357688),
    Circle( 1.7952608455,  0.6281269104, 0.2727652452),
    Circle( 1.4168575317,  1.0683357171, 1.1016025378),
    Circle( 1.4637371396,  0.9463877418, 1.1846214562),
    Circle(-0.5263668798,  1.7315156631, 1.4428514068),
    Circle(-1.2197352481,  0.9144146579, 1.0727263474),
    Circle(-0.1389358881,  0.1092805780, 0.7350208828),
    Circle( 1.5293954595,  0.0030278255, 1.2472867347),
    Circle(-0.5258728625,  1.3782633069, 1.3495508831),
    Circle(-0.1403562064,  0.2437382535, 1.3804956588),
    Circle( 0.8055826339, -0.0482092025, 0.3327165165),
    Circle(-0.6311979224,  0.7184578971, 0.2491045282),
    Circle( 1.4685857879, -0.8347049536, 1.3670667538),
    Circle(-0.6855727502,  1.6465021616, 1.0593087096),
    Circle( 0.0152957411,  0.0638919221, 0.9771215985)]

def main():
    # compute the bounding box of the circles
    x_min = min(c.x - c.r for c in circles)
    x_max = max(c.x + c.r for c in circles)
    y_min = min(c.y - c.r for c in circles)
    y_max = max(c.y + c.r for c in circles)

    box_side = 500

    dx = (x_max - x_min) / box_side
    dy = (y_max - y_min) / box_side

    count = 0

    for r in xrange(box_side):
        y = y_min + r * dy
        for c in xrange(box_side):
            x = x_min + c * dx
            if any((x-circle.x)**2 + (y-circle.y)**2 <= (circle.r ** 2)
                   for circle in circles):
                count += 1

    print "Approximated area:", count * dx * dy

main()

```

### python_code_2.txt
```python
from math import floor, ceil, sqrt

def area_scan(prec, circs):
    def sect((cx, cy, r), y):
        dr = sqrt(r ** 2 - (y - cy) ** 2)
        return (cx - dr, cx + dr)

    ys = [a[1] + a[2] for a in circs] + [a[1] - a[2] for a in circs]
    mins = int(floor(min(ys) / prec))
    maxs = int(ceil(max(ys) / prec))

    total = 0
    for y in (prec * x for x in xrange(mins, maxs + 1)):
        right = -float("inf")

        for (x0, x1) in sorted(sect((cx, cy, r), y)
                               for (cx, cy, r) in circs
                               if abs(y - cr) < r):
            if x1 <= right:
                continue
            total += x1 - max(x0, right)
            right = x1

    return total * prec

def main():
    circles = [
        ( 1.6417233788,  1.6121789534, 0.0848270516),
        (-1.4944608174,  1.2077959613, 1.1039549836),
        ( 0.6110294452, -0.6907087527, 0.9089162485),
        ( 0.3844862411,  0.2923344616, 0.2375743054),
        (-0.2495892950, -0.3832854473, 1.0845181219),
        ( 1.7813504266,  1.6178237031, 0.8162655711),
        (-0.1985249206, -0.8343333301, 0.0538864941),
        (-1.7011985145, -0.1263820964, 0.4776976918),
        (-0.4319462812,  1.4104420482, 0.7886291537),
        ( 0.2178372997, -0.9499557344, 0.0357871187),
        (-0.6294854565, -1.3078893852, 0.7653357688),
        ( 1.7952608455,  0.6281269104, 0.2727652452),
        ( 1.4168575317,  1.0683357171, 1.1016025378),
        ( 1.4637371396,  0.9463877418, 1.1846214562),
        (-0.5263668798,  1.7315156631, 1.4428514068),
        (-1.2197352481,  0.9144146579, 1.0727263474),
        (-0.1389358881,  0.1092805780, 0.7350208828),
        ( 1.5293954595,  0.0030278255, 1.2472867347),
        (-0.5258728625,  1.3782633069, 1.3495508831),
        (-0.1403562064,  0.2437382535, 1.3804956588),
        ( 0.8055826339, -0.0482092025, 0.3327165165),
        (-0.6311979224,  0.7184578971, 0.2491045282),
        ( 1.4685857879, -0.8347049536, 1.3670667538),
        (-0.6855727502,  1.6465021616, 1.0593087096),
        ( 0.0152957411,  0.0638919221, 0.9771215985)]

    p = 1e-3
    print "@stepsize", p, "area = %.4f" % area_scan(p, circles)

main()

```

### python_code_3.txt
```python
from __future__ import division
from math import sqrt
from itertools import count
from pprint import pprint as pp
try:
    from itertools import izip as zip
except:
    pass

# Remove duplicates and sort, largest first.
circles = sorted(set([
   #  xcenter       ycenter      radius
   (1.6417233788,  1.6121789534, 0.0848270516),
  (-1.4944608174,  1.2077959613, 1.1039549836),
   (0.6110294452, -0.6907087527, 0.9089162485),
   (0.3844862411,  0.2923344616, 0.2375743054),
  (-0.2495892950, -0.3832854473, 1.0845181219),
   (1.7813504266,  1.6178237031, 0.8162655711),
  (-0.1985249206, -0.8343333301, 0.0538864941),
  (-1.7011985145, -0.1263820964, 0.4776976918),
  (-0.4319462812,  1.4104420482, 0.7886291537),
   (0.2178372997, -0.9499557344, 0.0357871187),
  (-0.6294854565, -1.3078893852, 0.7653357688),
   (1.7952608455,  0.6281269104, 0.2727652452),
   (1.4168575317,  1.0683357171, 1.1016025378),
   (1.4637371396,  0.9463877418, 1.1846214562),
  (-0.5263668798,  1.7315156631, 1.4428514068),
  (-1.2197352481,  0.9144146579, 1.0727263474),
  (-0.1389358881,  0.1092805780, 0.7350208828),
   (1.5293954595,  0.0030278255, 1.2472867347),
  (-0.5258728625,  1.3782633069, 1.3495508831),
  (-0.1403562064,  0.2437382535, 1.3804956588),
   (0.8055826339, -0.0482092025, 0.3327165165),
  (-0.6311979224,  0.7184578971, 0.2491045282),
   (1.4685857879, -0.8347049536, 1.3670667538),
  (-0.6855727502,  1.6465021616, 1.0593087096),
   (0.0152957411,  0.0638919221, 0.9771215985),
   ]), key=lambda x: -x[-1])

def vdcgen(base=2):
    'Van der Corput sequence generator'
    for n in count():
        vdc, denom = 0,1
        while n:
            denom *= base
            n, remainder = divmod(n, base)
            vdc += remainder / denom
        yield vdc

def vdc_2d():
    'Two dimensional Van der Corput sequence generator'
    for x, y in zip(vdcgen(base=2), vdcgen(base=3)):
        yield x, y

def bounding_box(circles):
    'Return minx, maxx, miny, maxy'
    return (min(x - r for x,y,r in circles),
            max(x + r for x,y,r in circles),
            min(y - r for x,y,r in circles),
            max(y + r for x,y,r in circles)
           )
def circle_is_in_circle(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2) <= r1 - r2

def remove_covered_circles(circles):
    'Takes circles in decreasing radius order. Removes those covered by others'
    covered = []
    for i, c1 in enumerate(circles):
        eliminate = [c2 for c2 in circles[i+1:]
                        if circle_is_in_circle(c1, c2)]
        if eliminate: covered += [c1, eliminate]
        for c in eliminate: circles.remove(c)
    #pp(covered)    

def main(circles):
    print('Originally %i circles' % len(circles))
    print('Bounding box: %r' % (bounding_box(circles),))
    remove_covered_circles(circles)
    print('  down to %i  due to some being wholly covered by others' % len(circles))
    minx, maxx, miny, maxy = bounding_box(circles)
    # Shift to 0,0 and compute r**2 once
    circles2 = [(x - minx, y - miny, r*r) for x, y, r in circles]
    scalex, scaley = abs(maxx - minx), abs(maxy - miny)
    pcount, inside, last = 0, 0, ''
    for px, py in vdc_2d():
        pcount += 1
        px *= scalex; py *= scaley
        if any((px-cx)**2 + (py-cy)**2 <= cr2 for cx, cy, cr2 in circles2):
            inside += 1
        if not pcount % 100000:
            area = (inside/pcount) * scalex * scaley
            print('Points: %8i, Area estimate: %r' 
                  % (pcount, area))
            # Hack to check if precision OK
            this = '%.4f' % area
            if this == last:
                break
            else:
                last = this
    print('The value has settled to %s' % this)


if __name__ == '__main__': 
    main(circles)

```

### python_code_4.txt
```python
from collections import namedtuple
from functools import partial
from itertools import repeat, imap, izip
from decimal import Decimal, getcontext

# Requires the egg: https://pypi.python.org/pypi/dmath/
from dmath import atan2, asin, sin, cos, pi as piCompute

getcontext().prec = 40 # Set FP precision.
sqrt = Decimal.sqrt
pi = piCompute()
D2 = Decimal(2)

Vec = namedtuple("Vec", "x y")
vcross = lambda (a, b), (c, d): a*d - b*c
vdot   = lambda (a, b), (c, d): a*c + b*d
vadd   = lambda (a, b), (c, d): Vec(a + c, b + d)
vsub   = lambda (a, b), (c, d): Vec(a - c, b - d)
vlen   = lambda x: sqrt(vdot(x, x))
vdist  = lambda a, b: vlen(vsub(a, b))
vscale = lambda s, (x, y): Vec(x * s, y * s)

def vnorm(v):
    l = vlen(v)
    return Vec(v.x / l, v.y / l)

vangle = lambda (x, y): atan2(y, x)

def anorm(a):
    if a > pi:  return a - pi * D2
    if a < -pi: return a + pi * D2
    return             a

Circle = namedtuple("Circle", "x y r")

def circle_cross((x0, y0, r0), (x1, y1, r1)):
    d = vdist(Vec(x0, y0), Vec(x1, y1))
    if d >= r0 + r1 or d <= abs(r0 - r1):
        return []

    s = (r0 + r1 + d) / D2
    a = sqrt(s * (s - d) * (s - r0) * (s - r1))
    h = D2 * a / d
    dr = Vec(x1 - x0, y1 - y0)
    dx = vscale(sqrt(r0 ** 2 - h ** 2), vnorm(dr))
    ang = vangle(dr) if \
          r0 ** 2 + d ** 2 > r1 ** 2 \
          else pi + vangle(dr)
    da = asin(h / r0)
    return map(anorm, [ang - da, ang + da])

# Angles of the start and end points of the circle arc.
Angle2 = namedtuple("Angle2", "a1 a2")

Arc = namedtuple("Arc", "c aa")

arcPoint = lambda (x, y, r), a: \
    vadd(Vec(x, y), Vec(r * cos(a), r * sin(a)))

arc_start  = lambda (c, (a0, a1)):  arcPoint(c, a0)
arc_mid    = lambda (c, (a0, a1)):  arcPoint(c, (a0 + a1) / D2)
arc_end    = lambda (c, (a0, a1)):  arcPoint(c, a1)
arc_center = lambda ((x, y, r), _): Vec(x, y)

arc_area = lambda ((_0, _1, r), (a0, a1)):  r ** 2 * (a1 - a0) / D2

def split_circles(cs):
    cSplit = lambda (c, angs): \
        imap(Arc, repeat(c), imap(Angle2, angs, angs[1:]))

    # If an arc that was part of one circle is inside *another* circle,
    # it will not be part of the zero-winding path, so reject it.
    in_circle = lambda ((x0, y0), c), (x, y, r): \
        c != Circle(x, y, r) and vdist(Vec(x0, y0), Vec(x, y)) < r

    def in_any_circle(arc):
        return any(in_circle((arc_mid(arc), arc.c), c) for c in cs)

    concat_map = lambda f, xs: [y for x in xs for y in f(x)]

    f = lambda c: \
        (c, sorted([-pi, pi] +
                   concat_map(partial(circle_cross, c), cs)))
    cAngs = map(f, cs)
    arcs = concat_map(cSplit, cAngs)
    return filter(lambda ar: not in_any_circle(ar), arcs)

# Given a list of arcs, build sets of closed paths from them.
# If one arc's end point is no more than 1e-4 from another's
# start point, they are considered connected.  Since these
# start/end points resulted from intersecting circles earlier,
# they *should* be exactly the same, but floating point
# precision may cause small differences, hence the 1e-4 error
# margin.  When there are genuinely different intersections
# closer than this margin, the method will backfire, badly.
def make_paths(arcs):
    eps = Decimal("0.0001")
    def join_arcs(a, xxs):
        if not xxs:
            return [a]
        x, xs = xxs[0], xxs[1:]
        if not a:
            return join_arcs([x], xs)
        if vdist(arc_start(a[0]), arc_end(a[-1])) < eps:
            return [a] + join_arcs([], xxs)
        if vdist(arc_end(a[-1]), arc_start(x)) < eps:
            return join_arcs(a + [x], xs)
        return join_arcs(a, xs + [x])
    return join_arcs([], arcs)

# Slice N-polygon into N-2 triangles.
def polyline_area(vvs):
    tri_area = lambda a, b, c: vcross(vsub(b, a), vsub(c, b)) / D2
    v, vs = vvs[0], vvs[1:]
    return sum(tri_area(v, v1, v2) for v1, v2 in izip(vs, vs[1:]))

def path_area(arcs):
    f = lambda (a, e), arc: \
        (a + arc_area(arc), e + [arc_center(arc), arc_end(arc)])
    (a, e) = reduce(f, arcs, (0, []))
    return a + polyline_area(e)

circles_area = lambda cs: \
    sum(imap(path_area, make_paths(split_circles(cs))))

def main():
    raw_circles = """\
         1.6417233788  1.6121789534 0.0848270516
        -1.4944608174  1.2077959613 1.1039549836
         0.6110294452 -0.6907087527 0.9089162485
         0.3844862411  0.2923344616 0.2375743054
        -0.2495892950 -0.3832854473 1.0845181219
         1.7813504266  1.6178237031 0.8162655711
        -0.1985249206 -0.8343333301 0.0538864941
        -1.7011985145 -0.1263820964 0.4776976918
        -0.4319462812  1.4104420482 0.7886291537
         0.2178372997 -0.9499557344 0.0357871187
        -0.6294854565 -1.3078893852 0.7653357688
         1.7952608455  0.6281269104 0.2727652452
         1.4168575317  1.0683357171 1.1016025378
         1.4637371396  0.9463877418 1.1846214562
        -0.5263668798  1.7315156631 1.4428514068
        -1.2197352481  0.9144146579 1.0727263474
        -0.1389358881  0.1092805780 0.7350208828
         1.5293954595  0.0030278255 1.2472867347
        -0.5258728625  1.3782633069 1.3495508831
        -0.1403562064  0.2437382535 1.3804956588
         0.8055826339 -0.0482092025 0.3327165165
        -0.6311979224  0.7184578971 0.2491045282
         1.4685857879 -0.8347049536 1.3670667538
        -0.6855727502  1.6465021616 1.0593087096
         0.0152957411  0.0638919221 0.9771215985""".splitlines()

    circles = [Circle(*imap(Decimal, row.split()))
               for row in raw_circles]
    print "Total Area:", circles_area(circles)

main()

```

