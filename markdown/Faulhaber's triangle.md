# Faulhaber's triangle

## Task Link
[Rosetta Code - Faulhaber's triangle](https://rosettacode.org/wiki/Faulhaber%27s_triangle)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.math.MathContext;
import java.util.Arrays;
import java.util.stream.LongStream;

public class FaulhabersTriangle {
    private static final MathContext MC = new MathContext(256);

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

        public double toDouble() {
            return (double) num / denom;
        }

        public BigDecimal toBigDecimal() {
            return BigDecimal.valueOf(num).divide(BigDecimal.valueOf(denom), MC);
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

    private static long binomial(int n, int k) {
        if (n < 0 || k < 0 || n < k) throw new IllegalArgumentException();
        if (n == 0 || k == 0) return 1;
        long num = LongStream.rangeClosed(k + 1, n).reduce(1, (a, b) -> a * b);
        long den = LongStream.rangeClosed(2, n - k).reduce(1, (acc, i) -> acc * i);
        return num / den;
    }

    private static Frac[] faulhaberTriangle(int p) {
        Frac[] coeffs = new Frac[p + 1];
        Arrays.fill(coeffs, Frac.ZERO);
        Frac q = new Frac(1, p + 1);
        int sign = -1;
        for (int j = 0; j <= p; ++j) {
            sign *= -1;
            coeffs[p - j] = q.times(new Frac(sign, 1)).times(new Frac(binomial(p + 1, j), 1)).times(bernoulli(j));
        }
        return coeffs;
    }

    public static void main(String[] args) {
        for (int i = 0; i <= 9; ++i) {
            Frac[] coeffs = faulhaberTriangle(i);
            for (Frac coeff : coeffs) {
                System.out.printf("%5s  ", coeff);
            }
            System.out.println();
        }
        System.out.println();
        // get coeffs for (k + 1)th row
        int k = 17;
        Frac[] cc = faulhaberTriangle(k);
        int n = 1000;
        BigDecimal nn = BigDecimal.valueOf(n);
        BigDecimal np = BigDecimal.ONE;
        BigDecimal sum = BigDecimal.ZERO;
        for (Frac c : cc) {
            np = np.multiply(nn);
            sum = sum.add(np.multiply(c.toBigDecimal()));
        }
        System.out.println(sum.toBigInteger());
    }
}

```

## Python Code
### python_code_1.txt
```python
'''Faulhaber's triangle'''

from itertools import accumulate, chain, count, islice
from fractions import Fraction


# faulhaberTriangle :: Int -> [[Fraction]]
def faulhaberTriangle(m):
    '''List of rows of Faulhaber fractions.'''
    def go(rs, n):
        def f(x, y):
            return Fraction(n, x) * y
        xs = list(map(f, islice(count(2), m), rs))
        return [Fraction(1 - sum(xs), 1)] + xs

    return list(accumulate(
        [[]] + list(islice(count(0), 1 + m)),
        go
    ))[1:]


# faulhaberSum :: Integer -> Integer -> Integer
def faulhaberSum(p, n):
    '''Sum of the p-th powers of the first n
       positive integers.
    '''
    def go(x, y):
        return y * (n ** x)

    return sum(
        map(go, count(1), faulhaberTriangle(p)[-1])
    )


# ------------------------- TEST -------------------------
def main():
    '''Tests'''

    fs = faulhaberTriangle(9)
    print(
        fTable(__doc__ + ':\n')(str)(
            compose(concat)(
                fmap(showRatio(3)(3))
            )
        )(
            index(fs)
        )(range(0, len(fs)))
    )
    print('')
    print(
        faulhaberSum(17, 1000)
    )


# ----------------------- DISPLAY ------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
       fx display function -> f -> xs -> tabular string.
    '''
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + (
                            fxShow(f(x))
                        )
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox


# ----------------------- GENERIC ------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.
    '''
    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs

    return (
        f(xs) if isinstance(xs, list) else (
            chain.from_iterable(xs)
        )
    ) if xs else []


# fmap :: (a -> b) -> [a] -> [b]
def fmap(f):
    '''fmap over a list.
       f lifted to a function over a list.
    '''
    def go(xs):
        return list(map(f, xs))

    return go


# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )


# showRatio :: Int -> Int -> Ratio -> String
def showRatio(m):
    '''Left and right aligned string
       representation of the ratio r.
    '''
    def go(n):
        def f(r):
            d = r.denominator
            return str(r.numerator).rjust(m, ' ') + (
                ('/' + str(d).ljust(n, ' ')) if 1 != d else (
                    ' ' * (1 + n)
                )
            )
        return f
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

