# QR decomposition

## Task Link
[Rosetta Code - QR decomposition](https://rosettacode.org/wiki/QR_decomposition)

## Java Code
### java_code_1.txt
```java
import Jama.Matrix;
import Jama.QRDecomposition;

public class Decompose {
    public static void main(String[] args) {
        var matrix = new Matrix(new double[][] {
            {12, -51,   4},
            { 6, 167, -68},
            {-4,  24, -41},
        });

        var qr = new QRDecomposition(matrix);
        qr.getQ().print(10, 4);
        qr.getR().print(10, 4);
    }
}

```

### java_code_2.txt
```java
import cern.colt.matrix.impl.DenseDoubleMatrix2D;
import cern.colt.matrix.linalg.QRDecomposition;

public class Decompose {
    public static void main(String[] args) {
        var a = new DenseDoubleMatrix2D(new double[][] {
            {12, -51,   4},
            { 6, 167, -68},
            {-4,  24, -41}
        });
        var qr = new QRDecomposition(a);
        System.out.println(qr.getQ());
        System.out.println();
        System.out.println(qr.getR());
    }
}

```

### java_code_3.txt
```java
import java.util.Locale;

import org.apache.commons.math3.linear.Array2DRowRealMatrix;
import org.apache.commons.math3.linear.QRDecomposition;
import org.apache.commons.math3.linear.RealMatrix;

public class Decompose {
    public static void main(String[] args) {
        var a = new Array2DRowRealMatrix(new double[][] {
            {12, -51,   4},
            { 6, 167, -68},
            {-4,  24, -41}
        });
                                                         
        var qr = new QRDecomposition(a);
        print(qr.getQ());
        System.out.println();
        print(qr.getR());
    }
    
    public static void print(RealMatrix a) {
        for (double[] u: a.getData()) {
            System.out.print("[ ");
            for (double x: u) {
                System.out.printf(Locale.ROOT, "%10.4f ", x);
            }
            System.out.println("]");
        }
    }
}

```

### java_code_4.txt
```java
import org.la4j.Matrix;
import org.la4j.decomposition.QRDecompositor;

public class Decompose {
    public static void main(String[] args) {
        var a = Matrix.from2DArray(new double[][] {
            {12, -51,   4},
            { 6, 167, -68},
            {-4,  24, -41},
        });
        
        Matrix[] qr = new QRDecompositor(a).decompose();
        System.out.println(qr[0]);
        System.out.println(qr[1]);
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import numpy as np

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A

def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H

# task 1: show qr decomp of wp example
a = np.array(((
    (12, -51,   4),
    ( 6, 167, -68),
    (-4,  24, -41),
)))

q, r = qr(a)
print('q:\n', q.round(6))
print('r:\n', r.round(6))

# task 2: use qr decomp for polynomial regression example
def polyfit(x, y, n):
    return lsqr(x[:, None]**np.arange(n + 1), y.T)

def lsqr(a, b):
    q, r = qr(a)
    _, n = r.shape
    return np.linalg.solve(r[:n, :], np.dot(q.T, b)[:n])

x = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
y = np.array((1, 6, 17, 34, 57, 86, 121, 162, 209, 262, 321))

print('\npolyfit:\n', polyfit(x, y, 2))

```

