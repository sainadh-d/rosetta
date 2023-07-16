# K-d tree

## Task Link
[Rosetta Code - K-d tree](https://rosettacode.org/wiki/K-d_tree)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class KdTree {
    private int dimensions_;
    private Node root_ = null;
    private Node best_ = null;
    private double bestDistance_ = 0;
    private int visited_ = 0;
    
    public KdTree(int dimensions, List<Node> nodes) {
        dimensions_ = dimensions;
        root_ = makeTree(nodes, 0, nodes.size(), 0);
    }
    
    public Node findNearest(Node target) {
        if (root_ == null)
            throw new IllegalStateException("Tree is empty!");
        best_ = null;
        visited_ = 0;
        bestDistance_ = 0;
        nearest(root_, target, 0);
        return best_;
    }
    
    public int visited() {
        return visited_;
    }
    
    public double distance() {
        return Math.sqrt(bestDistance_);
    }
    
    private void nearest(Node root, Node target, int index) {
        if (root == null)
            return;
        ++visited_;
        double d = root.distance(target);
        if (best_ == null || d < bestDistance_) {
            bestDistance_ = d;
            best_ = root;
        }
        if (bestDistance_ == 0)
            return;
        double dx = root.get(index) - target.get(index);
        index = (index + 1) % dimensions_;
        nearest(dx > 0 ? root.left_ : root.right_, target, index);
        if (dx * dx >= bestDistance_)
            return;
        nearest(dx > 0 ? root.right_ : root.left_, target, index);
    }
    
    private Node makeTree(List<Node> nodes, int begin, int end, int index) {
        if (end <= begin)
            return null;
        int n = begin + (end - begin)/2;
        Node node = QuickSelect.select(nodes, begin, end - 1, n, new NodeComparator(index));
        index = (index + 1) % dimensions_;
        node.left_ = makeTree(nodes, begin, n, index);
        node.right_ = makeTree(nodes, n + 1, end, index);
        return node;
    }
    
    private static class NodeComparator implements Comparator<Node> {
        private int index_;

        private NodeComparator(int index) {
            index_ = index;
        }
        public int compare(Node n1, Node n2) {
            return Double.compare(n1.get(index_), n2.get(index_));
        }
    }
    
    public static class Node {
        private double[] coords_;
        private Node left_ = null;
        private Node right_ = null;

        public Node(double[] coords) {
            coords_ = coords;
        }
        public Node(double x, double y) {
            this(new double[]{x, y});
        }
        public Node(double x, double y, double z) {
            this(new double[]{x, y, z});
        }
        double get(int index) {
            return coords_[index];
        }
        double distance(Node node) {
            double dist = 0;
            for (int i = 0; i < coords_.length; ++i) {
                double d = coords_[i] - node.coords_[i];
                dist += d * d;
            }
            return dist;
        }
        public String toString() {
            StringBuilder s = new StringBuilder("(");
            for (int i = 0; i < coords_.length; ++i) {
                if (i > 0)
                    s.append(", ");
                s.append(coords_[i]);
            }
            s.append(')');
            return s.toString();
        }
    }
}

```

### java_code_2.txt
```java
import java.util.*;

//
// Java implementation of quickselect algorithm.
// See https://en.wikipedia.org/wiki/Quickselect
//
public class QuickSelect {
    private static final Random random = new Random();

    public static <T> T select(List<T> list, int n, Comparator<? super T> cmp) {
        return select(list, 0, list.size() - 1, n, cmp);
    }
    
    public static <T> T select(List<T> list, int left, int right, int n, Comparator<? super T> cmp) {
        for (;;) {
            if (left == right)
                return list.get(left);
            int pivot = pivotIndex(left, right);
            pivot = partition(list, left, right, pivot, cmp);
            if (n == pivot)
                return list.get(n);
            else if (n < pivot)
                right = pivot - 1;
            else
                left = pivot + 1;
        }
    }
    
    private static <T> int partition(List<T> list, int left, int right, int pivot, Comparator<? super T> cmp) {
        T pivotValue = list.get(pivot);
        swap(list, pivot, right);
        int store = left;
        for (int i = left; i < right; ++i) {
            if (cmp.compare(list.get(i), pivotValue) < 0) {
                swap(list, store, i);
                ++store;
            }
        }
        swap(list, right, store);
        return store;
    }
    
    private static <T> void swap(List<T> list, int i, int j) {
        T value = list.get(i);
        list.set(i, list.get(j));
        list.set(j, value);
    }

    private static int pivotIndex(int left, int right) {
        return left + random.nextInt(right - left + 1);
    }
}

```

### java_code_3.txt
```java
import java.util.*;

public class KdTreeTest {
    public static void main(String[] args) {
        testWikipedia();
        System.out.println();
        testRandom(1000);
        System.out.println();
        testRandom(1000000);
    }
    
    private static void testWikipedia() {
        double[][] coords = {
            { 2, 3 }, { 5, 4 }, { 9, 6 }, { 4, 7 }, { 8, 1 }, { 7, 2 }
        };
        List<KdTree.Node> nodes = new ArrayList<>();
        for (int i = 0; i < coords.length; ++i)
            nodes.add(new KdTree.Node(coords[i]));
        KdTree tree = new KdTree(2, nodes);
        KdTree.Node nearest = tree.findNearest(new KdTree.Node(9, 2));
        System.out.println("Wikipedia example data:");
        System.out.println("nearest point: " + nearest);
        System.out.println("distance: " + tree.distance());
        System.out.println("nodes visited: " + tree.visited());
    }

    private static KdTree.Node randomPoint(Random random) {
        double x = random.nextDouble();
        double y = random.nextDouble();
        double z = random.nextDouble();
        return new KdTree.Node(x, y, z);
    }

    private static void testRandom(int points) {
        Random random = new Random();
        List<KdTree.Node> nodes = new ArrayList<>();
        for (int i = 0; i < points; ++i)
            nodes.add(randomPoint(random));
        KdTree tree = new KdTree(3, nodes);
        KdTree.Node target = randomPoint(random);
        KdTree.Node nearest = tree.findNearest(target);
        System.out.println("Random data (" + points + " points):");
        System.out.println("target: " + target);
        System.out.println("nearest point: " + nearest);
        System.out.println("distance: " + tree.distance());
        System.out.println("nodes visited: " + tree.visited());
    }
}

```

## Python Code
### python_code_1.txt
```python
from random import seed, random
from time import time
from operator import itemgetter
from collections import namedtuple
from math import sqrt
from copy import deepcopy


def sqd(p1, p2):
    return sum((c1 - c2) ** 2 for c1, c2 in zip(p1, p2))


class KdNode(object):
    __slots__ = ("dom_elt", "split", "left", "right")

    def __init__(self, dom_elt, split, left, right):
        self.dom_elt = dom_elt
        self.split = split
        self.left = left
        self.right = right


class Orthotope(object):
    __slots__ = ("min", "max")

    def __init__(self, mi, ma):
        self.min, self.max = mi, ma


class KdTree(object):
    __slots__ = ("n", "bounds")

    def __init__(self, pts, bounds):
        def nk2(split, exset):
            if not exset:
                return None
            exset.sort(key=itemgetter(split))
            m = len(exset) // 2
            d = exset[m]
            while m + 1 < len(exset) and exset[m + 1][split] == d[split]:
                m += 1
            d = exset[m]


            s2 = (split + 1) % len(d)  # cycle coordinates
            return KdNode(d, split, nk2(s2, exset[:m]),
                                    nk2(s2, exset[m + 1:]))
        self.n = nk2(0, pts)
        self.bounds = bounds

T3 = namedtuple("T3", "nearest dist_sqd nodes_visited")


def find_nearest(k, t, p):
    def nn(kd, target, hr, max_dist_sqd):
        if kd is None:
            return T3([0.0] * k, float("inf"), 0)

        nodes_visited = 1
        s = kd.split
        pivot = kd.dom_elt
        left_hr = deepcopy(hr)
        right_hr = deepcopy(hr)
        left_hr.max[s] = pivot[s]
        right_hr.min[s] = pivot[s]

        if target[s] <= pivot[s]:
            nearer_kd, nearer_hr = kd.left, left_hr
            further_kd, further_hr = kd.right, right_hr
        else:
            nearer_kd, nearer_hr = kd.right, right_hr
            further_kd, further_hr = kd.left, left_hr

        n1 = nn(nearer_kd, target, nearer_hr, max_dist_sqd)
        nearest = n1.nearest
        dist_sqd = n1.dist_sqd
        nodes_visited += n1.nodes_visited

        if dist_sqd < max_dist_sqd:
            max_dist_sqd = dist_sqd
        d = (pivot[s] - target[s]) ** 2
        if d > max_dist_sqd:
            return T3(nearest, dist_sqd, nodes_visited)
        d = sqd(pivot, target)
        if d < dist_sqd:
            nearest = pivot
            dist_sqd = d
            max_dist_sqd = dist_sqd

        n2 = nn(further_kd, target, further_hr, max_dist_sqd)
        nodes_visited += n2.nodes_visited
        if n2.dist_sqd < dist_sqd:
            nearest = n2.nearest
            dist_sqd = n2.dist_sqd

        return T3(nearest, dist_sqd, nodes_visited)

    return nn(t.n, p, t.bounds, float("inf"))


def show_nearest(k, heading, kd, p):
    print(heading + ":")
    print("Point:           ", p)
    n = find_nearest(k, kd, p)
    print("Nearest neighbor:", n.nearest)
    print("Distance:        ", sqrt(n.dist_sqd))
    print("Nodes visited:   ", n.nodes_visited, "\n")


def random_point(k):
    return [random() for _ in range(k)]


def random_points(k, n):
    return [random_point(k) for _ in range(n)]

if __name__ == "__main__":
    seed(1)
    P = lambda *coords: list(coords)
    kd1 = KdTree([P(2, 3), P(5, 4), P(9, 6), P(4, 7), P(8, 1), P(7, 2)],
                  Orthotope(P(0, 0), P(10, 10)))
    show_nearest(2, "Wikipedia example data", kd1, P(9, 2))

    N = 400000
    t0 = time()
    kd2 = KdTree(random_points(3, N), Orthotope(P(0, 0, 0), P(1, 1, 1)))
    t1 = time()
    text = lambda *parts: "".join(map(str, parts))
    show_nearest(2, text("k-d tree with ", N,
                         " random 3D points (generation time: ",
                         t1-t0, "s)"),
                 kd2, random_point(3))

```

