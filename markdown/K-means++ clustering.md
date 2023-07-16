# K-means++ clustering

## Task Link
[Rosetta Code - K-means++ clustering](https://rosettacode.org/wiki/K-means%2B%2B_clustering)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class KMeansWithKpp{
		// Variables Needed
		public Point[] points;
		public Point[] centroids;
		Random rand;
		public int n;
		public int k;

		// hide default constructor
		private KMeansWithKpp(){
		}

		KMeansWithKpp(Point[] p, int clusters){
				points = p;
				n = p.length;
				k = Math.max(1, clusters);
				centroids = new Point[k];
				rand = new Random();
		}


		private static double distance(Point a, Point b){
				return (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y);
		}

		private static int nearest(Point pt, Point[] others, int len){
				double minD = Double.MAX_VALUE;
				int index = pt.group;
				len = Math.min(others.length, len);
				double dist;
				for (int i = 0; i < len; i++) {
						if (minD > (dist = distance(pt, others[i]))) {
								minD = dist;
								index = i;
						}
				}
				return index;
		}

		private static double nearestDistance(Point pt, Point[] others, int len){
				double minD = Double.MAX_VALUE;
				len = Math.min(others.length, len);
				double dist;
				for (int i = 0; i < len; i++) {
						if (minD > (dist = distance(pt, others[i]))) {
								minD = dist;
						}
				}
				return minD;
		}

		private void kpp(){
				centroids[0] = points[rand.nextInt(n)];
				double[] dist = new double[n];
				double sum = 0;
				for (int i = 1; i < k; i++) {
						for (int j = 0; j < n; j++) {
								dist[j] = nearestDistance(points[j], centroids, i);
								sum += dist[j];
						}
						sum = (sum * rand.nextInt(Integer.MAX_VALUE)) / Integer.MAX_VALUE;
						for (int j = 0; j < n; j++) {
								if ((sum -= dist[j]) > 0)
										continue;
								centroids[i].x = points[j].x;
								centroids[i].y = points[j].y;
						}
				}
				for (int i = 0; i < n; i++) {
						points[i].group = nearest(points[i], centroids, k);
				}
		}

		public void kMeans(int maxTimes){
				if (k == 1 || n <= 0) {
						return;
				}
				if(k >= n){
						for(int i =0; i < n; i++){
								points[i].group = i;
						}
						return;
				}
				maxTimes = Math.max(1, maxTimes);
				int changed;
				int bestPercent = n/1000;
				int minIndex;
				kpp();
				do {
						for (Point c : centroids) {
								c.x = 0.0;
								c.y = 0.0;
								c.group = 0;
						}
						for (Point pt : points) {
								if(pt.group < 0 || pt.group > centroids.length){
										pt.group = rand.nextInt(centroids.length);
								}
								centroids[pt.group].x += pt.x;
								centroids[pt.group].y = pt.y;
								centroids[pt.group].group++;
						}
						for (Point c : centroids) {
								c.x /= c.group;
								c.y /= c.group;
						}
						changed = 0;
						for (Point pt : points) {
								minIndex = nearest(pt, centroids, k);
								if (k != pt.group) {
										changed++;
										pt.group = minIndex;
								}
						}
						maxTimes--;
				} while (changed > bestPercent && maxTimes > 0);
		}
}


// A class for point(x,y) in plane

class Point{
		public double x;
		public double y;
		public int group;

		Point(){
				x = y = 0.0;
				group = 0;
		}

		/*
			Generates a random points on 2D Plane within given X-axis and Y-axis
		 */
		public Point[] getRandomPlaneData(double minX, double maxX, double minY, double maxY, int size){
				if (size <= 0)
						return null;
				double xdiff, ydiff;
				xdiff = maxX - minX;
				ydiff = maxY - minY;
				if (minX > maxX) {
						xdiff = minX - maxX;
						minX = maxX;
				}
				if (maxY < minY) {
						ydiff = minY - maxY;
						minY = maxY;
				}
				Point[] data = new Point[size];
				Random rand = new Random();
				for (int i = 0; i < size; i++) {
						data[i].x = minX + (xdiff * rand.nextInt(Integer.MAX_VALUE)) / Integer.MAX_VALUE;
						data[i].y = minY + (ydiff * rand.nextInt(Integer.MAX_VALUE)) / Integer.MAX_VALUE;
				}
				return data;
		}

		/*
	             Generate Random Polar Coordinates within given radius
		 */
		public Point[] getRandomPolarData(double radius, int size){
				if (size <= 0) {
						return null;
				}
				Point[] data = new Point[size];
				double radi, arg;
				Random rand = new Random();
				for (int i = 0; i < size; i++) {
						radi = (radius * rand.nextInt(Integer.MAX_VALUE)) / Integer.MAX_VALUE;
						arg = (2 * Math.PI * rand.nextInt(Integer.MAX_VALUE)) / Integer.MAX_VALUE;
						data[i].x = radi * Math.cos(arg);
						data[i].y = radi * Math.sin(arg);
				}
				return data;
		}
		
}

```

## Python Code
### python_code_1.txt
```python
from math import pi, sin, cos
from collections import namedtuple
from random import random, choice
from copy import copy

try:
    import psyco
    psyco.full()
except ImportError:
    pass


FLOAT_MAX = 1e100


class Point:
    __slots__ = ["x", "y", "group"]
    def __init__(self, x=0.0, y=0.0, group=0):
        self.x, self.y, self.group = x, y, group


def generate_points(npoints, radius):
    points = [Point() for _ in xrange(npoints)]

    # note: this is not a uniform 2-d distribution
    for p in points:
        r = random() * radius
        ang = random() * 2 * pi
        p.x = r * cos(ang)
        p.y = r * sin(ang)

    return points


def nearest_cluster_center(point, cluster_centers):
    """Distance and index of the closest cluster center"""
    def sqr_distance_2D(a, b):
        return (a.x - b.x) ** 2  +  (a.y - b.y) ** 2

    min_index = point.group
    min_dist = FLOAT_MAX

    for i, cc in enumerate(cluster_centers):
        d = sqr_distance_2D(cc, point)
        if min_dist > d:
            min_dist = d
            min_index = i

    return (min_index, min_dist)


def kpp(points, cluster_centers):
    cluster_centers[0] = copy(choice(points))
    d = [0.0 for _ in xrange(len(points))]

    for i in xrange(1, len(cluster_centers)):
        sum = 0
        for j, p in enumerate(points):
            d[j] = nearest_cluster_center(p, cluster_centers[:i])[1]
            sum += d[j]

        sum *= random()

        for j, di in enumerate(d):
            sum -= di
            if sum > 0:
                continue
            cluster_centers[i] = copy(points[j])
            break

    for p in points:
        p.group = nearest_cluster_center(p, cluster_centers)[0]


def lloyd(points, nclusters):
    cluster_centers = [Point() for _ in xrange(nclusters)]

    # call k++ init
    kpp(points, cluster_centers)

    lenpts10 = len(points) >> 10

    changed = 0
    while True:
        # group element for centroids are used as counters
        for cc in cluster_centers:
            cc.x = 0
            cc.y = 0
            cc.group = 0

        for p in points:
            cluster_centers[p.group].group += 1
            cluster_centers[p.group].x += p.x
            cluster_centers[p.group].y += p.y

        for cc in cluster_centers:
            cc.x /= cc.group
            cc.y /= cc.group

        # find closest centroid of each PointPtr
        changed = 0
        for p in points:
            min_i = nearest_cluster_center(p, cluster_centers)[0]
            if min_i != p.group:
                changed += 1
                p.group = min_i

        # stop when 99.9% of points are good
        if changed <= lenpts10:
            break

    for i, cc in enumerate(cluster_centers):
        cc.group = i

    return cluster_centers


def print_eps(points, cluster_centers, W=400, H=400):
    Color = namedtuple("Color", "r g b");

    colors = []
    for i in xrange(len(cluster_centers)):
        colors.append(Color((3 * (i + 1) % 11) / 11.0,
                            (7 * i % 11) / 11.0,
                            (9 * i % 11) / 11.0))

    max_x = max_y = -FLOAT_MAX
    min_x = min_y = FLOAT_MAX

    for p in points:
        if max_x < p.x: max_x = p.x
        if min_x > p.x: min_x = p.x
        if max_y < p.y: max_y = p.y
        if min_y > p.y: min_y = p.y

    scale = min(W / (max_x - min_x),
                H / (max_y - min_y))
    cx = (max_x + min_x) / 2
    cy = (max_y + min_y) / 2

    print "%%!PS-Adobe-3.0\n%%%%BoundingBox: -5 -5 %d %d" % (W + 10, H + 10)

    print ("/l {rlineto} def /m {rmoveto} def\n" +
           "/c { .25 sub exch .25 sub exch .5 0 360 arc fill } def\n" +
           "/s { moveto -2 0 m 2 2 l 2 -2 l -2 -2 l closepath " +
           "   gsave 1 setgray fill grestore gsave 3 setlinewidth" +
           " 1 setgray stroke grestore 0 setgray stroke }def")

    for i, cc in enumerate(cluster_centers):
        print ("%g %g %g setrgbcolor" %
               (colors[i].r, colors[i].g, colors[i].b))

        for p in points:
            if p.group != i:
                continue
            print ("%.3f %.3f c" % ((p.x - cx) * scale + W / 2,
                                    (p.y - cy) * scale + H / 2))

        print ("\n0 setgray %g %g s" % ((cc.x - cx) * scale + W / 2,
                                        (cc.y - cy) * scale + H / 2))

    print "\n%%%%EOF"


def main():
    npoints = 30000
    k = 7 # # clusters

    points = generate_points(npoints, 10)
    cluster_centers = lloyd(points, k)
    print_eps(points, cluster_centers)


main()

```

