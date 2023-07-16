# Quaternion type

## Task Link
[Rosetta Code - Quaternion type](https://rosettacode.org/wiki/Quaternion_type)

## Java Code
### java_code_1.txt
```java
public class Quaternion {
    private final double a, b, c, d;

    public Quaternion(double a, double b, double c, double d) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }
    public Quaternion(double r) {
        this(r, 0.0, 0.0, 0.0);
    }

    public double norm() {
        return Math.sqrt(a * a + b * b + c * c + d * d);
    }

    public Quaternion negative() {
        return new Quaternion(-a, -b, -c, -d);
    }

    public Quaternion conjugate() {
        return new Quaternion(a, -b, -c, -d);
    }

    public Quaternion add(double r) {
        return new Quaternion(a + r, b, c, d);
    }
    public static Quaternion add(Quaternion q, double r) {
        return q.add(r);
    }
    public static Quaternion add(double r, Quaternion q) {
        return q.add(r);
    }
    public Quaternion add(Quaternion q) {
        return new Quaternion(a + q.a, b + q.b, c + q.c, d + q.d);
    }
    public static Quaternion add(Quaternion q1, Quaternion q2) {
        return q1.add(q2);
    }

    public Quaternion times(double r) {
        return new Quaternion(a * r, b * r, c * r, d * r);
    }
    public static Quaternion times(Quaternion q, double r) {
        return q.times(r);
    }
    public static Quaternion times(double r, Quaternion q) {
        return q.times(r);
    }
    public Quaternion times(Quaternion q) {
        return new Quaternion(
            a * q.a - b * q.b - c * q.c - d * q.d,
            a * q.b + b * q.a + c * q.d - d * q.c,
            a * q.c - b * q.d + c * q.a + d * q.b,
            a * q.d + b * q.c - c * q.b + d * q.a
        );
    }
    public static Quaternion times(Quaternion q1, Quaternion q2) {
        return q1.times(q2);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Quaternion)) return false;
        final Quaternion other = (Quaternion) obj;
        if (Double.doubleToLongBits(this.a) != Double.doubleToLongBits(other.a)) return false;
        if (Double.doubleToLongBits(this.b) != Double.doubleToLongBits(other.b)) return false;
        if (Double.doubleToLongBits(this.c) != Double.doubleToLongBits(other.c)) return false;
        if (Double.doubleToLongBits(this.d) != Double.doubleToLongBits(other.d)) return false;
        return true;
    }
    @Override
    public String toString() {
        return String.format("%.2f + %.2fi + %.2fj + %.2fk", a, b, c, d).replaceAll("\\+ -", "- ");
    }

    public String toQuadruple() {
        return String.format("(%.2f, %.2f, %.2f, %.2f)", a, b, c, d);
    }

    public static void main(String[] args) {
        Quaternion q = new Quaternion(1.0, 2.0, 3.0, 4.0);
        Quaternion q1 = new Quaternion(2.0, 3.0, 4.0, 5.0);
        Quaternion q2 = new Quaternion(3.0, 4.0, 5.0, 6.0);
        double r = 7.0;
        System.out.format("q       = %s%n", q);
        System.out.format("q1      = %s%n", q1);
        System.out.format("q2      = %s%n", q2);
        System.out.format("r       = %.2f%n%n", r);
        System.out.format("\u2016q\u2016     = %.2f%n", q.norm());
        System.out.format("-q      = %s%n", q.negative());
        System.out.format("q*      = %s%n", q.conjugate());
        System.out.format("q + r   = %s%n", q.add(r));
        System.out.format("q1 + q2 = %s%n", q1.add(q2));
        System.out.format("q \u00d7 r   = %s%n", q.times(r));
        Quaternion q1q2 = q1.times(q2);
        Quaternion q2q1 = q2.times(q1);
        System.out.format("q1 \u00d7 q2 = %s%n", q1q2);
        System.out.format("q2 \u00d7 q1 = %s%n", q2q1);
        System.out.format("q1 \u00d7 q2 %s q2 \u00d7 q1%n", (q1q2.equals(q2q1) ? "=" : "\u2260"));
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple
import math

class Q(namedtuple('Quaternion', 'real, i, j, k')):
    'Quaternion type: Q(real=0.0, i=0.0, j=0.0, k=0.0)' 

    __slots__ = () 

    def __new__(_cls, real=0.0, i=0.0, j=0.0, k=0.0):
        'Defaults all parts of quaternion to zero'
        return super().__new__(_cls, float(real), float(i), float(j), float(k))

    def conjugate(self):
        return Q(self.real, -self.i, -self.j, -self.k)

    def _norm2(self):
        return sum( x*x for x in self)

    def norm(self):
        return math.sqrt(self._norm2())

    def reciprocal(self):
        n2 = self._norm2()
        return Q(*(x / n2 for x in self.conjugate())) 

    def __str__(self):
        'Shorter form of Quaternion as string'
        return 'Q(%g, %g, %g, %g)' % self

    def __neg__(self):
        return Q(-self.real, -self.i, -self.j, -self.k)

    def __add__(self, other):
        if type(other) == Q:
            return Q( *(s+o for s,o in zip(self, other)) )
        try:
            f = float(other)
        except:
            return NotImplemented
        return Q(self.real + f, self.i, self.j, self.k)

    def __radd__(self, other):
        return Q.__add__(self, other)

    def __mul__(self, other):
        if type(other) == Q:
            a1,b1,c1,d1 = self
            a2,b2,c2,d2 = other
            return Q(
                 a1*a2 - b1*b2 - c1*c2 - d1*d2,
                 a1*b2 + b1*a2 + c1*d2 - d1*c2,
                 a1*c2 - b1*d2 + c1*a2 + d1*b2,
                 a1*d2 + b1*c2 - c1*b2 + d1*a2 )
        try:
            f = float(other)
        except:
            return NotImplemented
        return Q(self.real * f, self.i * f, self.j * f, self.k * f)

    def __rmul__(self, other):
        return Q.__mul__(self, other)

    def __truediv__(self, other):
        if type(other) == Q:
            return self.__mul__(other.reciprocal())
        try:
            f = float(other)
        except:
            return NotImplemented
        return Q(self.real / f, self.i / f, self.j / f, self.k / f)

    def __rtruediv__(self, other):
        return other * self.reciprocal()

    __div__, __rdiv__ = __truediv__, __rtruediv__

Quaternion = Q       

q  = Q(1, 2, 3, 4)
q1 = Q(2, 3, 4, 5)
q2 = Q(3, 4, 5, 6)
r  = 7

```

### python_code_2.txt
```python
>>> q
Quaternion(real=1.0, i=2.0, j=3.0, k=4.0)
>>> q1
Quaternion(real=2.0, i=3.0, j=4.0, k=5.0)
>>> q2
Quaternion(real=3.0, i=4.0, j=5.0, k=6.0)
>>> r
7
>>> q.norm()
5.477225575051661
>>> q1.norm()
7.3484692283495345
>>> q2.norm()
9.273618495495704
>>> -q
Quaternion(real=-1.0, i=-2.0, j=-3.0, k=-4.0)
>>> q.conjugate()
Quaternion(real=1.0, i=-2.0, j=-3.0, k=-4.0)
>>> r + q
Quaternion(real=8.0, i=2.0, j=3.0, k=4.0)
>>> q + r
Quaternion(real=8.0, i=2.0, j=3.0, k=4.0)
>>> q1 + q2
Quaternion(real=5.0, i=7.0, j=9.0, k=11.0)
>>> q2 + q1
Quaternion(real=5.0, i=7.0, j=9.0, k=11.0)
>>> q * r
Quaternion(real=7.0, i=14.0, j=21.0, k=28.0)
>>> r * q
Quaternion(real=7.0, i=14.0, j=21.0, k=28.0)
>>> q1 * q2
Quaternion(real=-56.0, i=16.0, j=24.0, k=26.0)
>>> q2 * q1
Quaternion(real=-56.0, i=18.0, j=20.0, k=28.0)
>>> assert q1 * q2 != q2 * q1
>>> 
>>> i, j, k = Q(0,1,0,0), Q(0,0,1,0), Q(0,0,0,1)
>>> i*i
Quaternion(real=-1.0, i=0.0, j=0.0, k=0.0)
>>> j*j
Quaternion(real=-1.0, i=0.0, j=0.0, k=0.0)
>>> k*k
Quaternion(real=-1.0, i=0.0, j=0.0, k=0.0)
>>> i*j*k
Quaternion(real=-1.0, i=0.0, j=0.0, k=0.0)
>>> q1 / q2
Quaternion(real=0.7906976744186047, i=0.023255813953488358, j=-2.7755575615628914e-17, k=0.046511627906976744)
>>> q1 / q2 * q2
Quaternion(real=2.0000000000000004, i=3.0000000000000004, j=4.000000000000001, k=5.000000000000001)
>>> q2 * q1 / q2
Quaternion(real=2.0, i=3.465116279069768, j=3.906976744186047, k=4.767441860465116)
>>> q1.reciprocal() * q1
Quaternion(real=0.9999999999999999, i=0.0, j=0.0, k=0.0)
>>> q1 * q1.reciprocal()
Quaternion(real=0.9999999999999999, i=0.0, j=0.0, k=0.0)
>>>

```

