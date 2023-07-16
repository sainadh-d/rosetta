# Elliptic curve arithmetic

## Task Link
[Rosetta Code - Elliptic curve arithmetic](https://rosettacode.org/wiki/Elliptic_curve_arithmetic)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;
import java.util.Locale;

public class Test {

    public static void main(String[] args) {
        Pt a = Pt.fromY(1);
        Pt b = Pt.fromY(2);
        System.out.printf("a = %s%n", a);
        System.out.printf("b = %s%n", b);
        Pt c = a.plus(b);
        System.out.printf("c = a + b = %s%n", c);
        Pt d = c.neg();
        System.out.printf("d = -c = %s%n", d);
        System.out.printf("c + d = %s%n", c.plus(d));
        System.out.printf("a + b + d = %s%n", a.plus(b).plus(d));
        System.out.printf("a * 12345 = %s%n", a.mult(12345));
    }
}

class Pt {
    final static int bCoeff = 7;

    double x, y;

    Pt(double x, double y) {
        this.x = x;
        this.y = y;
    }

    static Pt zero() {
        return new Pt(Double.POSITIVE_INFINITY, Double.POSITIVE_INFINITY);
    }

    boolean isZero() {
        return this.x > 1e20 || this.x < -1e20;
    }

    static Pt fromY(double y) {
        return new Pt(cbrt(pow(y, 2) - bCoeff), y);
    }

    Pt dbl() {
        if (isZero())
            return this;
        double L = (3 * this.x * this.x) / (2 * this.y);
        double x2 = pow(L, 2) - 2 * this.x;
        return new Pt(x2, L * (this.x - x2) - this.y);
    }

    Pt neg() {
        return new Pt(this.x, -this.y);
    }

    Pt plus(Pt q) {
        if (this.x == q.x && this.y == q.y)
            return dbl();

        if (isZero())
            return q;

        if (q.isZero())
            return this;

        double L = (q.y - this.y) / (q.x - this.x);
        double xx = pow(L, 2) - this.x - q.x;
        return new Pt(xx, L * (this.x - xx) - this.y);
    }

    Pt mult(int n) {
        Pt r = Pt.zero();
        Pt p = this;
        for (int i = 1; i <= n; i <<= 1) {
            if ((i & n) != 0)
                r = r.plus(p);
            p = p.dbl();
        }
        return r;
    }

    @Override
    public String toString() {
        if (isZero())
            return "Zero";
        return String.format(Locale.US, "(%.3f,%.3f)", this.x, this.y);
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

class Point:
    b = 7
    def __init__(self, x=float('inf'), y=float('inf')):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def is_zero(self):
        return self.x > 1e20 or self.x < -1e20

    def neg(self):
        return Point(self.x, -self.y)

    def dbl(self):
        if self.is_zero():
            return self.copy()
        try:
            L = (3 * self.x * self.x) / (2 * self.y)
        except ZeroDivisionError:
            return Point()
        x = L * L - 2 * self.x
        return Point(x, L * (self.x - x) - self.y)

    def add(self, q):
        if self.x == q.x and self.y == q.y:
            return self.dbl()
        if self.is_zero():
            return q.copy()
        if q.is_zero():
            return self.copy()
        try:
            L = (q.y - self.y) / (q.x - self.x)
        except ZeroDivisionError:
            return Point()
        x = L * L - self.x - q.x
        return Point(x, L * (self.x - x) - self.y)

    def mul(self, n):
        p = self.copy()
        r = Point()
        i = 1
        while i <= n:
            if i&n:
                r = r.add(p)
            p = p.dbl()
            i <<= 1
        return r

    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)

def show(s, p):
    print(s, "Zero" if p.is_zero() else p)

def from_y(y):
    n = y * y - Point.b
    x = n**(1./3) if n>=0 else -((-n)**(1./3))
    return Point(x, y)

# demonstrate
a = from_y(1)
b = from_y(2)
show("a =", a)
show("b =", b)
c = a.add(b)
show("c = a + b =", c)
d = c.neg()
show("d = -c =", d)
show("c + d =", c.add(d))
show("a + b + d =", a.add(b.add(d)))
show("a * 12345 =", a.mul(12345))

```

