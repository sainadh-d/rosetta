# Steffensen's method

## Task Link
[Rosetta Code - Steffensen's method](https://rosettacode.org/wiki/Steffensen%27s_method)

## Java Code
### java_code_1.txt
```java
import java.util.Optional;

public class Steffensen {
    static double aitken(double p0) {
        double p1 = f(p0);
        double p2 = f(p1);
        double p1m0 = p1 - p0;
        return p0 - p1m0 * p1m0 / (p2 - 2.0 * p1 + p0);
    }

    static Optional<Double> steffensenAitken(double pinit, double tol, int maxiter) {
        double p0 = pinit;
        double p = aitken(p0);
        int iter = 1;
        while (Math.abs(p - p0) > tol && iter < maxiter) {
            p0 = p;
            p = aitken(p0);
            iter++;
        }
        if (Math.abs(p - p0) > tol) return Optional.empty();
        return Optional.of(p);
    }

    static double deCasteljau(double c0, double c1, double c2, double t) {
        double s = 1.0 - t;
        double c01 = s * c0 + t * c1;
        double c12 = s * c1 + t * c2;
        return s * c01 + t * c12;
    }

    static double xConvexLeftParabola(double t) {
        return deCasteljau(2.0, -8.0, 2.0, t);
    }

    static double yConvexRightParabola(double t) {
        return deCasteljau(1.0, 2.0, 3.0, t);
    }

    static double implicitEquation(double x, double y) {
        return 5.0 * x * x + y - 5.0;
    }

    static double f(double t) {
        double x = xConvexLeftParabola(t);
        double y = yConvexRightParabola(t);
        return implicitEquation(x, y) + t;
    }

    public static void main(String[] args) {
        double t0 = 0.0;
        for (int i = 0; i < 11; ++i) {
            System.out.printf("t0 = %3.1f : ", t0);
            Optional<Double> t = steffensenAitken(t0, 0.00000001, 1000);
            if (!t.isPresent()) {
                System.out.println("no answer");
            } else {
                double x = xConvexLeftParabola(t.get());
                double y = yConvexRightParabola(t.get());
                if (Math.abs(implicitEquation(x, y)) <= 0.000001) {
                    System.out.printf("intersection at (%f, %f)\n", x, y);
                } else {
                    System.out.println("spurious solution");
                }
            }
            t0 += 0.1;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from math import nan, isnan
from numpy import arange


def aitken(f, p0):
    """ Aitken's extrapolation """
    p1 = f(p0)
    p2 = f(p1)
    return p0 - (p1 - p0)**2 / (p2 - 2 * p1 + p0)

def steffensen_aitken(f, pinit, tol, maxiter):
    """ Steffensen's method using Aitken """
    p0 = pinit
    p = aitken(f, p0)
    iter = 1
    while abs(p - p0) > tol and iter < maxiter:
        p0 = p
        p = aitken(f, p0)
        iter += 1
    return nan if abs(p - p0) > tol else p

def deCasteljau(c0, c1, c2, t):
    """ deCasteljau function """
    s = 1.0 - t
    return s * (s * c0 + t * c1) + t * (s * c1 + t * c2)

def xConvexLeftParabola(t): return deCasteljau(2, -8, 2, t)
def yConvexRightParabola(t): return deCasteljau(1, 2, 3, t)
def implicit_equation(x, y): return 5 * x**2 + y - 5

def f(t):
    """ Outside of NumPy arithmetic may return NoneType on overflow """
    if type(t) == type(None):
        return nan
    return implicit_equation(xConvexLeftParabola(t), yConvexRightParabola(t)) + t

def test_steffensen(tol=0.00000001, iters=1000, stepsize=0.1):
    """ test the example """
    for t0 in arange(0, 1.1, stepsize):
        print(f't0 = {t0:0.1f} : ', end='')
        t = steffensen_aitken(f, t0, tol, iters)
        if isnan(t):
            print('no answer')
        else:
            x = xConvexLeftParabola(t)
            y = yConvexRightParabola(t)
            if abs(implicit_equation(x, y)) <= tol:
                print(f'intersection at ({x}, {y})')
            else:
                print('spurious solution')
    return 0


if __name__ == '__main__':

    test_steffensen()

```

