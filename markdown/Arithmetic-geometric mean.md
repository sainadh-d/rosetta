# Arithmetic-geometric mean

## Task Link
[Rosetta Code - Arithmetic-geometric mean](https://rosettacode.org/wiki/Arithmetic-geometric_mean)

## Java Code
### java_code_1.txt
```java
/*
 * Arithmetic-Geometric Mean of 1 & 1/sqrt(2)
 * Brendan Shaklovitz
 * 5/29/12
 */
public class ArithmeticGeometricMean {

    public static double agm(double a, double g) {
        double a1 = a;
        double g1 = g;
        while (Math.abs(a1 - g1) >= 1.0e-14) {
            double arith = (a1 + g1) / 2.0;
            double geom = Math.sqrt(a1 * g1);
            a1 = arith;
            g1 = geom;
        }
        return a1;
    }

    public static void main(String[] args) {
        System.out.println(agm(1.0, 1.0 / Math.sqrt(2.0)));
    }
}

```

## Python Code
### python_code_1.txt
```python
from math import sqrt

def agm(a0, g0, tolerance=1e-10):
    """
    Calculating the arithmetic-geometric mean of two numbers a0, g0.

    tolerance     the tolerance for the converged 
                  value of the arithmetic-geometric mean
                  (default value = 1e-10)
    """
    an, gn = (a0 + g0) / 2.0, sqrt(a0 * g0)
    while abs(an - gn) > tolerance:
        an, gn = (an + gn) / 2.0, sqrt(an * gn)
    return an

print agm(1, 1 / sqrt(2))

```

### python_code_2.txt
```python
from decimal import Decimal, getcontext

def agm(a, g, tolerance=Decimal("1e-65")):
    while True:
        a, g = (a + g) / 2, (a * g).sqrt()
        if abs(a - g) < tolerance:
            return a

getcontext().prec = 70
print agm(Decimal(1), 1 / Decimal(2).sqrt())

```

