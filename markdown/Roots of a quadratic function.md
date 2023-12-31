# Roots of a quadratic function

## Task Link
[Rosetta Code - Roots of a quadratic function](https://rosettacode.org/wiki/Roots_of_a_quadratic_function)

## Java Code
### java_code_1.txt
```java
public class QuadraticRoots {
    private static class Complex {
        double re, im;

        public Complex(double re, double im) {
            this.re = re;
            this.im = im;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == this) {return true;}
            if (!(obj instanceof Complex)) {return false;}
            Complex other = (Complex) obj;
            return (re == other.re) && (im == other.im);
        }

        @Override
        public String toString() {
            if (im == 0.0) {return String.format("%g", re);}
            if (re == 0.0) {return String.format("%gi", im);}
            return String.format("%g %c %gi", re,
                (im < 0.0 ? '-' : '+'), Math.abs(im));
        }
    }

    private static Complex[] quadraticRoots(double a, double b, double c) {
        Complex[] roots = new Complex[2];
        double d = b * b - 4.0 * a * c;  // discriminant
        double aa = a + a;

        if (d < 0.0) {
            double re = -b / aa;
            double im = Math.sqrt(-d) / aa;
            roots[0] = new Complex(re, im);
            roots[1] = new Complex(re, -im);
        } else if (b < 0.0) {
            // Avoid calculating -b - Math.sqrt(d), to avoid any
            // subtractive cancellation when it is near zero.
            double re = (-b + Math.sqrt(d)) / aa;
            roots[0] = new Complex(re, 0.0);
            roots[1] = new Complex(c / (a * re), 0.0);
        } else {
            // Avoid calculating -b + Math.sqrt(d).
            double re = (-b - Math.sqrt(d)) / aa;
            roots[1] = new Complex(re, 0.0);
            roots[0] = new Complex(c / (a * re), 0.0);
        }
        return roots;
    }

    public static void main(String[] args) {
        double[][] equations = {
            {1.0, 22.0, -1323.0},   // two distinct real roots
            {6.0, -23.0, 20.0},     //   with a != 1.0
            {1.0, -1.0e9, 1.0},     //   with one root near zero
            {1.0, 2.0, 1.0},        // one real root (double root)
            {1.0, 0.0, 1.0},        // two imaginary roots
            {1.0, 1.0, 1.0}         // two complex roots
        };
        for (int i = 0; i < equations.length; i++) {
            Complex[] roots = quadraticRoots(
                equations[i][0], equations[i][1], equations[i][2]);
            System.out.format("%na = %g   b = %g   c = %g%n",
                equations[i][0], equations[i][1], equations[i][2]);
            if (roots[0].equals(roots[1])) {
                System.out.format("X1,2 = %s%n", roots[0]);
            } else {
                System.out.format("X1 = %s%n", roots[0]);
                System.out.format("X2 = %s%n", roots[1]);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import math
import cmath
import numpy

def quad_discriminating_roots(a,b,c, entier = 1e-5):
    """For reference, the naive algorithm which shows complete loss of
    precision on the quadratic in question.  (This function also returns a
    characterization of the roots.)"""
    discriminant = b*b - 4*a*c
    a,b,c,d =complex(a), complex(b), complex(c), complex(discriminant)
    root1 = (-b + cmath.sqrt(d))/2./a
    root2 = (-b - cmath.sqrt(d))/2./a
    if abs(discriminant) < entier:
        return "real and equal", abs(root1), abs(root1)
    if discriminant > 0:
        return "real", root1.real, root2.real
    return "complex", root1, root2

def middlebrook(a, b, c):
    try:
        q = math.sqrt(a*c)/b
        f = .5+ math.sqrt(1-4*q*q)/2
    except ValueError:
        q = cmath.sqrt(a*c)/b
        f = .5+ cmath.sqrt(1-4*q*q)/2
    return (-b/a)*f, -c/(b*f)

def whatevery(a, b, c):
    try:
        d = math.sqrt(b*b-4*a*c)
    except ValueError:
        d = cmath.sqrt(b*b-4*a*c)
    if b > 0:
        return div(2*c, (-b-d)), div((-b-d), 2*a)
    else:
        return div((-b+d), 2*a), div(2*c, (-b+d))

def div(n, d):
    """Divide, with a useful interpretation of division by zero."""
    try:
        return n/d
    except ZeroDivisionError:
        if n:
            return n*float('inf')
        return float('nan')

testcases = [
    (3, 4, 4/3),    # real, equal
    (3, 2, -1),     # real, unequal
    (3, 2, 1),      # complex
    (1, -1e9, 1),   # ill-conditioned "quadratic in question" required by task.
    (1, -1e100, 1),
    (1, -1e200, 1),
    (1, -1e300, 1),
]

print('Naive:')
for c in testcases:
    print("{} {:.5} {:.5}".format(*quad_discriminating_roots(*c)))

print('\nMiddlebrook:')
for c in testcases:
    print(("{:.5} "*2).format(*middlebrook(*c)))

print('\nWhat Every...')
for c in testcases:
    print(("{:.5} "*2).format(*whatevery(*c)))

print('\nNumpy:')
for c in testcases:
    print(("{:.5} "*2).format(*numpy.roots(c)))

```

