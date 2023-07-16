# Faulhaber's formula

## Task Link
[Rosetta Code - Faulhaber's formula](https://rosettacode.org/wiki/Faulhaber%27s_formula)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.stream.IntStream;

public class FaulhabersFormula {
    private static long gcd(long a, long b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    private static class Frac implements Comparable<Frac> {
        private long num;
        private long denom;

        public static final Frac ZERO = new Frac(0, 1);
        public static final Frac ONE = new Frac(1, 1);

        public Frac(long n, long d) {
            if (d == 0) throw new IllegalArgumentException("d must not be zero");
            long nn = n;
            long dd = d;
            if (nn == 0) {
                dd = 1;
            } else if (dd < 0) {
                nn = -nn;
                dd = -dd;
            }
            long g = Math.abs(gcd(nn, dd));
            if (g > 1) {
                nn /= g;
                dd /= g;
            }
            num = nn;
            denom = dd;
        }

        public Frac plus(Frac rhs) {
            return new Frac(num * rhs.denom + denom * rhs.num, rhs.denom * denom);
        }

        public Frac unaryMinus() {
            return new Frac(-num, denom);
        }

        public Frac minus(Frac rhs) {
            return this.plus(rhs.unaryMinus());
        }

        public Frac times(Frac rhs) {
            return new Frac(this.num * rhs.num, this.denom * rhs.denom);
        }

        @Override
        public int compareTo(Frac o) {
            double diff = toDouble() - o.toDouble();
            return Double.compare(diff, 0.0);
        }

        @Override
        public boolean equals(Object obj) {
            return null != obj && obj instanceof Frac && this.compareTo((Frac) obj) == 0;
        }

        @Override
        public String toString() {
            if (denom == 1) {
                return Long.toString(num);
            }
            return String.format("%d/%d", num, denom);
        }

        private double toDouble() {
            return (double) num / denom;
        }
    }

    private static Frac bernoulli(int n) {
        if (n < 0) throw new IllegalArgumentException("n may not be negative or zero");
        Frac[] a = new Frac[n + 1];
        Arrays.fill(a, Frac.ZERO);
        for (int m = 0; m <= n; ++m) {
            a[m] = new Frac(1, m + 1);
            for (int j = m; j >= 1; --j) {
                a[j - 1] = a[j - 1].minus(a[j]).times(new Frac(j, 1));
            }
        }
        // returns 'first' Bernoulli number
        if (n != 1) return a[0];
        return a[0].unaryMinus();
    }

    private static int binomial(int n, int k) {
        if (n < 0 || k < 0 || n < k) throw new IllegalArgumentException();
        if (n == 0 || k == 0) return 1;
        int num = IntStream.rangeClosed(k + 1, n).reduce(1, (a, b) -> a * b);
        int den = IntStream.rangeClosed(2, n - k).reduce(1, (acc, i) -> acc * i);
        return num / den;
    }

    private static void faulhaber(int p) {
        System.out.printf("%d : ", p);
        Frac q = new Frac(1, p + 1);
        int sign = -1;
        for (int j = 0; j <= p; ++j) {
            sign *= -1;
            Frac coeff = q.times(new Frac(sign, 1)).times(new Frac(binomial(p + 1, j), 1)).times(bernoulli(j));
            if (Frac.ZERO.equals(coeff)) continue;
            if (j == 0) {
                if (!Frac.ONE.equals(coeff)) {
                    if (Frac.ONE.unaryMinus().equals(coeff)) {
                        System.out.print("-");
                    } else {
                        System.out.print(coeff);
                    }
                }
            } else {
                if (Frac.ONE.equals(coeff)) {
                    System.out.print(" + ");
                } else if (Frac.ONE.unaryMinus().equals(coeff)) {
                    System.out.print(" - ");
                } else if (coeff.compareTo(Frac.ZERO) > 0) {
                    System.out.printf(" + %s", coeff);
                } else {
                    System.out.printf(" - %s", coeff.unaryMinus());
                }
            }
            int pwr = p + 1 - j;
            if (pwr > 1)
                System.out.printf("n^%d", pwr);
            else
                System.out.print("n");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        for (int i = 0; i <= 9; ++i) {
            faulhaber(i);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction

def nextu(a):
    n = len(a)
    a.append(1)
    for i in range(n - 1, 0, -1):
        a[i] = i * a[i] + a[i - 1]
    return a

def nextv(a):
    n = len(a) - 1
    b = [(1 - n) * x for x in a]
    b.append(1)
    for i in range(n):
        b[i + 1] += a[i]
    return b

def sumpol(n):
    u = [0, 1]
    v = [[1], [1, 1]]
    yield [Fraction(0), Fraction(1)]
    for i in range(1, n):
        v.append(nextv(v[-1]))
        t = [0] * (i + 2)
        p = 1
        for j, r in enumerate(u):
            r = Fraction(r, j + 1)
            for k, s in enumerate(v[j + 1]):
                t[k] += r * s
        yield t
        u = nextu(u)

def polstr(a):
    s = ""
    q = False
    n = len(a) - 1
    for i, x in enumerate(reversed(a)):
        i = n - i
        if i < 2:
            m = "n" if i == 1 else ""
        else:
            m = "n^%d" % i
        c = str(abs(x))
        if i > 0:
            if c == "1":
                c = ""
            else:
                m = " " + m
        if x != 0:
            if q:
                t = " + " if x > 0 else " - "
                s += "%s%s%s" % (t, c, m)
            else:
                t = "" if x > 0 else "-"
                s = "%s%s%s" % (t, c, m)
                q = True
    if q:
        return s
    else:
        return "0"

for i, p in enumerate(sumpol(10)):
    print(i, ":", polstr(p))

```

