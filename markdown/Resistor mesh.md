# Resistor mesh

## Task Link
[Rosetta Code - Resistor mesh](https://rosettacode.org/wiki/Resistor_mesh)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class ResistorMesh {
    private static final int S = 10;

    private static class Node {
        double v;
        int fixed;

        Node(double v, int fixed) {
            this.v = v;
            this.fixed = fixed;
        }
    }

    private static void setBoundary(List<List<Node>> m) {
        m.get(1).get(1).v = 1.0;
        m.get(1).get(1).fixed = 1;

        m.get(6).get(7).v = -1.0;
        m.get(6).get(7).fixed = -1;
    }

    private static double calcDiff(List<List<Node>> m, List<List<Node>> d, int w, int h) {
        double total = 0.0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                double v = 0.0;
                int n = 0;
                if (i > 0) {
                    v += m.get(i - 1).get(j).v;
                    n++;
                }
                if (j > 0) {
                    v += m.get(i).get(j - 1).v;
                    n++;
                }
                if (i + 1 < h) {
                    v += m.get(i + 1).get(j).v;
                    n++;
                }
                if (j + 1 < w) {
                    v += m.get(i).get(j + 1).v;
                    n++;
                }
                v = m.get(i).get(j).v - v / n;
                d.get(i).get(j).v = v;
                if (m.get(i).get(j).fixed == 0) {
                    total += v * v;
                }
            }
        }
        return total;
    }

    private static double iter(List<List<Node>> m, int w, int h) {
        List<List<Node>> d = new ArrayList<>(h);
        for (int i = 0; i < h; ++i) {
            List<Node> t = new ArrayList<>(w);
            for (int j = 0; j < w; ++j) {
                t.add(new Node(0.0, 0));
            }
            d.add(t);
        }

        double[] cur = new double[3];
        double diff = 1e10;

        while (diff > 1e-24) {
            setBoundary(m);
            diff = calcDiff(m, d, w, h);
            for (int i = 0; i < h; ++i) {
                for (int j = 0; j < w; ++j) {
                    m.get(i).get(j).v -= d.get(i).get(j).v;
                }
            }
        }

        for (int i = 0; i < h; ++i) {
            for (int j = 0; j < w; ++j) {
                int k = 0;
                if (i != 0) k++;
                if (j != 0) k++;
                if (i < h - 1) k++;
                if (j < w - 1) k++;
                cur[m.get(i).get(j).fixed + 1] += d.get(i).get(j).v * k;
            }
        }

        return (cur[2] - cur[0]) / 2.0;
    }

    public static void main(String[] args) {
        List<List<Node>> mesh = new ArrayList<>(S);
        for (int i = 0; i < S; ++i) {
            List<Node> t = new ArrayList<>(S);
            for (int j = 0; j < S; ++j) {
                t.add(new Node(0.0, 0));
            }
            mesh.add(t);
        }

        double r = 2.0 / iter(mesh, S, S);
        System.out.printf("R = %.15f", r);
    }
}

```

## Python Code
### python_code_1.txt
```python
DIFF_THRESHOLD = 1e-40

class Fixed:
    FREE = 0
    A = 1
    B = 2

class Node:
    __slots__ = ["voltage", "fixed"]
    def __init__(self, v=0.0, f=Fixed.FREE):
        self.voltage = v
        self.fixed = f

def set_boundary(m):
    m[1][1] = Node( 1.0, Fixed.A)
    m[6][7] = Node(-1.0, Fixed.B)

def calc_difference(m, d):
    h = len(m)
    w = len(m[0])
    total = 0.0

    for i in xrange(h):
        for j in xrange(w):
            v = 0.0
            n = 0
            if i != 0:  v += m[i-1][j].voltage; n += 1
            if j != 0:  v += m[i][j-1].voltage; n += 1
            if i < h-1: v += m[i+1][j].voltage; n += 1
            if j < w-1: v += m[i][j+1].voltage; n += 1
            v = m[i][j].voltage - v / n

            d[i][j].voltage = v
            if m[i][j].fixed == Fixed.FREE:
                total += v ** 2
    return total

def iter(m):
    h = len(m)
    w = len(m[0])
    difference = [[Node() for j in xrange(w)] for i in xrange(h)]

    while True:
        set_boundary(m) # Enforce boundary conditions.
        if calc_difference(m, difference) < DIFF_THRESHOLD:
            break
        for i, di in enumerate(difference):
            for j, dij in enumerate(di):
                m[i][j].voltage -= dij.voltage

    cur = [0.0] * 3
    for i, di in enumerate(difference):
        for j, dij in enumerate(di):
            cur[m[i][j].fixed] += (dij.voltage *
                (bool(i) + bool(j) + (i < h-1) + (j < w-1)))

    return (cur[Fixed.A] - cur[Fixed.B]) / 2.0

def main():
    w = h = 10
    mesh = [[Node() for j in xrange(w)] for i in xrange(h)]
    print "R = %.16f" % (2 / iter(mesh))

main()

```

### python_code_2.txt
```python
import sys, copy
from fractions import Fraction

def gauss(a, b):
    n, p = len(a), len(a[0])
    for i in range(n):
        t = abs(a[i][i])
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > t:
                t = abs(a[j][i])
                k = j
        if k != i:
            for j in range(i, n):
                a[i][j], a[k][j] = a[k][j], a[i][j]
            b[i], b[k] = b[k], b[i]
        t = 1/a[i][i]
        for j in range(i + 1, n):
            a[i][j] *= t
        b[i] *= t
        for j in range(i + 1, n):
            t = a[j][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            b[j] -= t * b[i]
    for i in range(n - 1, -1, -1):
        for j in range(i):
            b[j] -= a[j][i]*b[i]
    return b

def resistor_grid(p, q, ai, aj, bi, bj):
    n = p*q
    I = Fraction(1, 1)
    v = [0*I]*n
    a = [copy.copy(v) for i in range(n)]
    for i in range(p):
        for j in range(q):
            k = i*q + j
            if i == ai and j == aj:
                a[k][k] = I
            else:
                c = 0
                if i + 1 < p:
                    c += 1
                    a[k][k + q] = -1
                if i >= 1:
                    c += 1
                    a[k][k - q] = -1
                if j + 1 < q:
                    c += 1
                    a[k][k + 1] = -1
                if j >= 1:
                    c += 1
                    a[k][k - 1] = -1
                a[k][k] = c*I
    b = [0*I]*n
    k = bi*q + bj
    b[k] = 1
    return gauss(a, b)[k]

def main(arg):
    r = resistor_grid(int(arg[0]), int(arg[1]), int(arg[2]), int(arg[3]), int(arg[4]), int(arg[5]))
    print(r)
    print(float(r))

main(sys.argv[1:])

# Output:
# python grid.py 10 10 1 1 7 6
# 455859137025721/283319837425200
# 1.6089912417307297

```

