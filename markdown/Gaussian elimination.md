# Gaussian elimination

## Task Link
[Rosetta Code - Gaussian elimination](https://rosettacode.org/wiki/Gaussian_elimination)

## Java Code
### java_code_1.txt
```java
import java.util.Locale;

public class GaussianElimination {
    public static double solve(double[][] a, double[][] b) {
        if (a == null || b == null || a.length == 0 || b.length == 0) {
            throw new IllegalArgumentException("Invalid dimensions");
        }
        
        int n = b.length, p = b[0].length;
        if (a.length != n || a[0].length != n) {
            throw new IllegalArgumentException("Invalid dimensions");
        }

        double det = 1.0;
        
        for (int i = 0; i < n - 1; i++) {
            int k = i;
            for (int j = i + 1; j < n; j++) {
                if (Math.abs(a[j][i]) > Math.abs(a[k][i])) {
                    k = j;
                }
            }
            
            if (k != i) {
                det = -det;
                
                for (int j = i; j < n; j++) {
                    double s = a[i][j];
                    a[i][j] = a[k][j];
                    a[k][j] = s;
                }

                for (int j = 0; j < p; j++) {
                    double s = b[i][j];
                    b[i][j] = b[k][j];
                    b[k][j] = s;
                }
            }
            
            for (int j = i + 1; j < n; j++) {
                double s = a[j][i] / a[i][i];
                for (k = i + 1; k < n; k++) {
                    a[j][k] -= s * a[i][k];
                }
                
                for (k = 0; k < p; k++) {
                    b[j][k] -= s * b[i][k];
                }
            }
        }
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                double s = a[i][j];
                for (int k = 0; k < p; k++) {
                    b[i][k] -= s * b[j][k];
                }
            }
            double s = a[i][i];
            det *= s;
            for (int k = 0; k < p; k++) {
                b[i][k] /= s;
            }
        }
        
        return det;
    }
    
    public static void main(String[] args) {
        double[][] a = new double[][] {{4.0, 1.0, 0.0, 0.0, 0.0},
                                       {1.0, 4.0, 1.0, 0.0, 0.0},
                                       {0.0, 1.0, 4.0, 1.0, 0.0},
                                       {0.0, 0.0, 1.0, 4.0, 1.0},
                                       {0.0, 0.0, 0.0, 1.0, 4.0}};

        double[][] b = new double[][] {{1.0 / 2.0},
                                       {2.0 / 3.0},
                                       {3.0 / 4.0},
                                       {4.0 / 5.0},
                                       {5.0 / 6.0}};
                                       
        double[] x = {39.0 / 400.0,
                      11.0 / 100.0,
                      31.0 / 240.0,
                      37.0 / 300.0,
                      71.0 / 400.0};
                                       
        System.out.println("det: " + solve(a, b));
        

        for (int i = 0; i < 5; i++) {
            System.out.printf(Locale.US, "%12.8f %12.4e\n", b[i][0], b[i][0] - x[i]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# The 'gauss' function takes two matrices, 'a' and 'b', with 'a' square, and it return the determinant of 'a' and a matrix 'x' such that a*x = b.
# If 'b' is the identity, then 'x' is the inverse of 'a'.

import copy
from fractions import Fraction

def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
            
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
                
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b

def zeromat(p, q):
    return [[0]*q for i in range(p)]

def matmul(a, b):
    n, p = len(a), len(a[0])
    p1, q = len(b), len(b[0])
    if p != p1:
        raise ValueError("Incompatible dimensions")
    c = zeromat(n, q)
    for i in range(n):
        for j in range(q):
                c[i][j] = sum(a[i][k]*b[k][j] for k in range(p))
    return c


def mapmat(f, a):
    return [list(map(f, v)) for v in a]

def ratmat(a):
    return mapmat(Fraction, a)

# As an example, compute the determinant and inverse of 3x3 magic square

a = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
det, c = gauss(a, b)

det
-360.0

c
[[-0.10277777777777776, 0.18888888888888888, -0.019444444444444438],
[0.10555555555555554, 0.02222222222222223, -0.061111111111111116],
[0.0638888888888889, -0.14444444444444446, 0.14722222222222223]]

# Check product
matmul(a, c)
[[1.0, 0.0, 0.0], [5.551115123125783e-17, 1.0, 0.0],
[1.1102230246251565e-16, -2.220446049250313e-16, 1.0]]

# Same with fractions, so the result is exact

det, c = gauss(ratmat(a), ratmat(b))

det
Fraction(-360, 1)

c
[[Fraction(-37, 360), Fraction(17, 90), Fraction(-7, 360)],
[Fraction(19, 180), Fraction(1, 45), Fraction(-11, 180)],
[Fraction(23, 360), Fraction(-13, 90), Fraction(53, 360)]]

matmul(a, c)
[[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)],
[Fraction(0, 1), Fraction(1, 1), Fraction(0, 1)],
[Fraction(0, 1), Fraction(0, 1), Fraction(1, 1)]]

```

