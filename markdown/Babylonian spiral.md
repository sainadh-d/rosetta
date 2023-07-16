# Babylonian spiral

## Task Link
[Rosetta Code - Babylonian spiral](https://rosettacode.org/wiki/Babylonian_spiral)

## Java Code
### java_code_1.txt
```java
import java.awt.Point;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public final class BabylonianSpiral {

	public static void main(String[] aArgs) throws IOException {
		List<Point> points = babylonianSpiral(10_000);
		System.out.println("The first 40 points of the Babylonian spiral are:");
		for ( int i = 0, column = 0; i < 40; i++ ) {
			System.out.print(String.format("%9s%s",
				"(" + points.get(i).x + ", " + points.get(i).y + ")", ( ++column % 10 == 0 ) ? "\n" : " "));
		}
		System.out.println();
	
		String text = svgText(points, 800);		
		Files.write(Paths.get("C:/Users/psnow/Desktop/BabylonianSpiralJava.svg"), text.getBytes());
	}
	
	private static List<Point> babylonianSpiral(int aStepCount) {
		final double tau = 2 * Math.PI;
		List<Integer> squares = IntStream.rangeClosed(0, aStepCount).map( i -> i * i ).boxed().toList();
		List<Point> points = Stream.of( new Point(0, 0), new Point(0, 1) ).collect(Collectors.toList());
		int norm = 1;
		
		for ( int step = 0; step < aStepCount - 2; step++ ) {
		    Point previousPoint = points.get(points.size() - 1);
		    final double theta = Math.atan2(previousPoint.y, previousPoint.x);
		    Set<Point> candidates = new HashSet<Point>();
		    while ( candidates.isEmpty() ) {
		    	norm += 1;
			    for ( int i = 0; i < aStepCount; i++ ) {
			        int a = squares.get(i);
			        if ( a > norm / 2 ) {
			        	break;
			        }
			        for ( int j = (int) Math.sqrt(norm) + 1; j >= 0; j-- ) {
			        	int b = squares.get(j);	
			        	if ( a + b < norm ) {
			        		break;
			        	}
			        	if ( a + b == norm ) {
			        		candidates.addAll(
			        			List.of( new Point(i, j), new Point(-i, j), new Point(i, -j), new Point(-i, -j),
			        					 new Point(j, i), new Point(-j, i), new Point(j, -i), new Point(-j, -i) ));
			        	}
			        }
			    }
		    }
		    
		    Comparator<Point> comparatorPoint = (one, two) -> Double.compare(
		    	( theta - Math.atan2(one.y, one.x) + tau ) % tau, ( theta - Math.atan2(two.y, two.x) + tau ) % tau);
		    
		    Point minimum = candidates.stream().min(comparatorPoint).get();
		    points.add(minimum);
		}
		
		for ( int i = 0; i < points.size() - 1; i++ ) {
			points.set(i + 1, new Point(points.get(i).x + points.get(i + 1).x, points.get(i).y + points.get(i + 1).y));
		}
		return points;
	}

	private static String svgText(List<Point> aPoints, int aSize) {
    	StringBuilder text = new StringBuilder();
    	text.append("<svg xmlns='http://www.w3.org/2000/svg'");
        text.append(" width='" + aSize + "' height='" + aSize + "'>\n");
        text.append("<rect width='100%' height='100%' fill='cyan'/>\n");
        text.append("<path stroke-width='1' stroke='black' fill='cyan' d='");
        for ( int i = 0; i < aPoints.size(); i++ ) {
        	text.append(( i == 0 ? "M" : "L" ) +
        		( 150 + aPoints.get(i).x / 20 ) + ", " + ( 525 - aPoints.get(i).y / 20 ) + " ");
        }
        text.append("'/>\n</svg>\n");
        
        return text.toString();
    }
	
}

```

## Python Code
### python_code_1.txt
```python
""" Rosetta Code task rosettacode.org/wiki/Babylonian_spiral """

from itertools import accumulate
from math import isqrt, atan2, tau
from matplotlib.pyplot import axis, plot, show


square_cache = []

def babylonian_spiral(nsteps):
    """
    Get the points for each step along a Babylonia spiral of `nsteps` steps.
    Origin is at (0, 0) with first step one unit in the positive direction along
    the vertical (y) axis. The other points are selected to have integer x and y
    coordinates, progressively concatenating the next longest vector with integer
    x and y coordinates on the grid. The direction change of the  new vector is
    chosen to be nonzero and clockwise in a direction that minimizes the change
    in direction from the previous vector.
    
    See also: oeis.org/A256111, oeis.org/A297346, oeis.org/A297347
    """
    if len(square_cache) <= nsteps:
        square_cache.extend([x * x for x in range(len(square_cache), nsteps)])
    xydeltas = [(0, 0), (0, 1)]
    δsquared = 1
    for _ in range(nsteps - 2):
        x, y = xydeltas[-1]
        θ = atan2(y, x)
        candidates = []
        while not candidates:
            δsquared += 1
            for i, a in enumerate(square_cache):
                if a > δsquared // 2:
                    break
                for j in range(isqrt(δsquared) + 1, 0, -1):
                    b = square_cache[j]
                    if a + b < δsquared:
                        break
                    if a + b == δsquared:
                        candidates.extend([(i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i),
                           (j, -i), (-j, -i)])

        p = min(candidates, key=lambda d: (θ - atan2(d[1], d[0])) % tau)
        xydeltas.append(p)

    return list(accumulate(xydeltas, lambda a, b: (a[0] + b[0], a[1] + b[1])))


points10000 = babylonian_spiral(10000)
print("The first 40 Babylonian spiral points are:")
for i, p in enumerate(points10000[:40]):
     print(str(p).ljust(10), end = '\n' if (i + 1) % 10 == 0 else '')

# stretch portion of task
plot(*zip(*points10000), color="navy", linewidth=0.2)
axis('scaled')
show()

```

### python_code_2.txt
```python
from itertools import islice, count
import matplotlib.pyplot as plt
import heapq

def twosquares():
    q, n = [], 1

    while True:
        while not q or n*n <= q[0][0]:
            heapq.heappush(q, (n*n, n, 0))
            n += 1

        s, xy = q[0][0], []

        while q and q[0][0] == s: # pop all vectors with same length
            s, a, b = heapq.heappop(q)
            xy.append((a, b))
            if a > b:
                heapq.heappush(q, (a*a + (b+1)*(b+1), a, b + 1))

        yield tuple(xy)

def gen_dirs():
    d = (0, 1)
    for v in twosquares():
        # include symmetric vectors
        v += tuple((b, a) for a, b in v if a != b)
        v += tuple((a, -b) for a, b in v if b)
        v += tuple((-a, b) for a, b in v if a)

        # filter using dot and cross product
        d = max((a*d[0] + b*d[1], a, b) for a, b in v if a*d[1] - b*d[0] >= 0)[1:]
        yield d

def positions():
    p = (0, 0)
    for d in gen_dirs():
        yield p
        p = (p[0] + d[0], p[1] + d[1])

print(list(islice(positions(), 40)))

plt.plot(*zip(*list(islice(positions(), 100000))), lw=0.4)
plt.gca().set_aspect(1)
plt.show()

```

