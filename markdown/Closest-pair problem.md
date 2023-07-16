# Closest-pair problem

## Task Link
[Rosetta Code - Closest-pair problem](https://rosettacode.org/wiki/Closest-pair_problem)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class ClosestPair
{
  public static class Point
  {
    public final double x;
    public final double y;
    
    public Point(double x, double y)
    {
      this.x = x;
      this.y = y;
    }
    
    public String toString()
    {  return "(" + x + ", " + y + ")";  }
  }
  
  public static class Pair
  {
    public Point point1 = null;
    public Point point2 = null;
    public double distance = 0.0;
    
    public Pair()
    {  }
    
    public Pair(Point point1, Point point2)
    {
      this.point1 = point1;
      this.point2 = point2;
      calcDistance();
    }
    
    public void update(Point point1, Point point2, double distance)
    {
      this.point1 = point1;
      this.point2 = point2;
      this.distance = distance;
    }
    
    public void calcDistance()
    {  this.distance = distance(point1, point2);  }
    
    public String toString()
    {  return point1 + "-" + point2 + " : " + distance;  }
  }
  
  public static double distance(Point p1, Point p2)
  {
    double xdist = p2.x - p1.x;
    double ydist = p2.y - p1.y;
    return Math.hypot(xdist, ydist);
  }
  
  public static Pair bruteForce(List<? extends Point> points)
  {
    int numPoints = points.size();
    if (numPoints < 2)
      return null;
    Pair pair = new Pair(points.get(0), points.get(1));
    if (numPoints > 2)
    {
      for (int i = 0; i < numPoints - 1; i++)
      {
        Point point1 = points.get(i);
        for (int j = i + 1; j < numPoints; j++)
        {
          Point point2 = points.get(j);
          double distance = distance(point1, point2);
          if (distance < pair.distance)
            pair.update(point1, point2, distance);
        }
      }
    }
    return pair;
  }
  
  public static void sortByX(List<? extends Point> points)
  {
    Collections.sort(points, new Comparator<Point>() {
        public int compare(Point point1, Point point2)
        {
          if (point1.x < point2.x)
            return -1;
          if (point1.x > point2.x)
            return 1;
          return 0;
        }
      }
    );
  }
  
  public static void sortByY(List<? extends Point> points)
  {
    Collections.sort(points, new Comparator<Point>() {
        public int compare(Point point1, Point point2)
        {
          if (point1.y < point2.y)
            return -1;
          if (point1.y > point2.y)
            return 1;
          return 0;
        }
      }
    );
  }
  
  public static Pair divideAndConquer(List<? extends Point> points)
  {
    List<Point> pointsSortedByX = new ArrayList<Point>(points);
    sortByX(pointsSortedByX);
    List<Point> pointsSortedByY = new ArrayList<Point>(points);
    sortByY(pointsSortedByY);
    return divideAndConquer(pointsSortedByX, pointsSortedByY);
  }
  
  private static Pair divideAndConquer(List<? extends Point> pointsSortedByX, List<? extends Point> pointsSortedByY)
  {
    int numPoints = pointsSortedByX.size();
    if (numPoints <= 3)
      return bruteForce(pointsSortedByX);
    
    int dividingIndex = numPoints >>> 1;
    List<? extends Point> leftOfCenter = pointsSortedByX.subList(0, dividingIndex);
    List<? extends Point> rightOfCenter = pointsSortedByX.subList(dividingIndex, numPoints);
    
    List<Point> tempList = new ArrayList<Point>(leftOfCenter);
    sortByY(tempList);
    Pair closestPair = divideAndConquer(leftOfCenter, tempList);
    
    tempList.clear();
    tempList.addAll(rightOfCenter);
    sortByY(tempList);
    Pair closestPairRight = divideAndConquer(rightOfCenter, tempList);
    
    if (closestPairRight.distance < closestPair.distance)
      closestPair = closestPairRight;
    
    tempList.clear();
    double shortestDistance =closestPair.distance;
    double centerX = rightOfCenter.get(0).x;
    for (Point point : pointsSortedByY)
      if (Math.abs(centerX - point.x) < shortestDistance)
        tempList.add(point);
    
    for (int i = 0; i < tempList.size() - 1; i++)
    {
      Point point1 = tempList.get(i);
      for (int j = i + 1; j < tempList.size(); j++)
      {
        Point point2 = tempList.get(j);
        if ((point2.y - point1.y) >= shortestDistance)
          break;
        double distance = distance(point1, point2);
        if (distance < closestPair.distance)
        {
          closestPair.update(point1, point2, distance);
          shortestDistance = distance;
        }
      }
    }
    return closestPair;
  }
  
  public static void main(String[] args)
  {
    int numPoints = (args.length == 0) ? 1000 : Integer.parseInt(args[0]);
    List<Point> points = new ArrayList<Point>();
    Random r = new Random();
    for (int i = 0; i < numPoints; i++)
      points.add(new Point(r.nextDouble(), r.nextDouble()));
    System.out.println("Generated " + numPoints + " random points");
    long startTime = System.currentTimeMillis();
    Pair bruteForceClosestPair = bruteForce(points);
    long elapsedTime = System.currentTimeMillis() - startTime;
    System.out.println("Brute force (" + elapsedTime + " ms): " + bruteForceClosestPair);
    startTime = System.currentTimeMillis();
    Pair dqClosestPair = divideAndConquer(points);
    elapsedTime = System.currentTimeMillis() - startTime;
    System.out.println("Divide and conquer (" + elapsedTime + " ms): " + dqClosestPair);
    if (bruteForceClosestPair.distance != dqClosestPair.distance)
      System.out.println("MISMATCH");
  }
}

```

## Python Code
### python_code_1.txt
```python
"""
  Compute nearest pair of points using two algorithms
  
  First algorithm is 'brute force' comparison of every possible pair.
  Second, 'divide and conquer', is based on:
    www.cs.iupui.edu/~xkzou/teaching/CS580/Divide-and-conquer-closestPair.ppt 
"""

from random import randint, randrange
from operator import itemgetter, attrgetter

infinity = float('inf')

# Note the use of complex numbers to represent 2D points making distance == abs(P1-P2)

def bruteForceClosestPair(point):
    numPoints = len(point)
    if numPoints < 2:
        return infinity, (None, None)
    return min( ((abs(point[i] - point[j]), (point[i], point[j]))
                 for i in range(numPoints-1)
                 for j in range(i+1,numPoints)),
                key=itemgetter(0))

def closestPair(point):
    xP = sorted(point, key= attrgetter('real'))
    yP = sorted(point, key= attrgetter('imag'))
    return _closestPair(xP, yP)

def _closestPair(xP, yP):
    numPoints = len(xP)
    if numPoints <= 3:
        return bruteForceClosestPair(xP)
    Pl = xP[:numPoints/2]
    Pr = xP[numPoints/2:]
    Yl, Yr = [], []
    xDivider = Pl[-1].real
    for p in yP:
        if p.real <= xDivider:
            Yl.append(p)
        else:
            Yr.append(p)
    dl, pairl = _closestPair(Pl, Yl)
    dr, pairr = _closestPair(Pr, Yr)
    dm, pairm = (dl, pairl) if dl < dr else (dr, pairr)
    # Points within dm of xDivider sorted by Y coord
    closeY = [p for p in yP  if abs(p.real - xDivider) < dm]
    numCloseY = len(closeY)
    if numCloseY > 1:
        # There is a proof that you only need compare a max of 7 next points
        closestY = min( ((abs(closeY[i] - closeY[j]), (closeY[i], closeY[j]))
                         for i in range(numCloseY-1)
                         for j in range(i+1,min(i+8, numCloseY))),
                        key=itemgetter(0))
        return (dm, pairm) if dm <= closestY[0] else closestY
    else:
        return dm, pairm
    
def times():
    ''' Time the different functions
    '''
    import timeit

    functions = [bruteForceClosestPair, closestPair]
    for f in functions:
        print 'Time for', f.__name__, timeit.Timer(
            '%s(pointList)' % f.__name__,
            'from closestpair import %s, pointList' % f.__name__).timeit(number=1)
    


pointList = [randint(0,1000)+1j*randint(0,1000) for i in range(2000)]

if __name__ == '__main__':
    pointList = [(5+9j), (9+3j), (2+0j), (8+4j), (7+4j), (9+10j), (1+9j), (8+2j), 10j, (9+6j)]
    print pointList
    print '  bruteForceClosestPair:', bruteForceClosestPair(pointList)
    print '            closestPair:', closestPair(pointList)
    for i in range(10):
        pointList = [randrange(11)+1j*randrange(11) for i in range(10)]
        print '\n', pointList
        print ' bruteForceClosestPair:', bruteForceClosestPair(pointList)
        print '           closestPair:', closestPair(pointList)
    print '\n'
    times()
    times()
    times()

```

