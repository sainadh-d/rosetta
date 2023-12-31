# Test integerness

## Task Link
[Rosetta Code - Test integerness](https://rosettacode.org/wiki/Test_integerness)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.util.List;

public class TestIntegerness {
    private static boolean isLong(double d) {
        return isLong(d, 0.0);
    }

    private static boolean isLong(double d, double tolerance) {
        return (d - Math.floor(d)) <= tolerance || (Math.ceil(d) - d) <= tolerance;
    }

    @SuppressWarnings("ResultOfMethodCallIgnored")
    private static boolean isBigInteger(BigDecimal bd) {
        try {
            bd.toBigIntegerExact();
            return true;
        } catch (ArithmeticException ex) {
            return false;
        }
    }

    private static class Rational {
        long num;
        long denom;

        Rational(int num, int denom) {
            this.num = num;
            this.denom = denom;
        }

        boolean isLong() {
            return num % denom == 0;
        }

        @Override
        public String toString() {
            return String.format("%s/%s", num, denom);
        }
    }

    private static class Complex {
        double real;
        double imag;

        Complex(double real, double imag) {
            this.real = real;
            this.imag = imag;
        }

        boolean isLong() {
            return TestIntegerness.isLong(real) && imag == 0.0;
        }

        @Override
        public String toString() {
            if (imag >= 0.0) {
                return String.format("%s + %si", real, imag);
            }
            return String.format("%s - %si", real, imag);
        }
    }

    public static void main(String[] args) {
        List<Double> da = List.of(25.000000, 24.999999, 25.000100);
        for (Double d : da) {
            boolean exact = isLong(d);
            System.out.printf("%.6f is %s integer%n", d, exact ? "an" : "not an");
        }
        System.out.println();

        double tolerance = 0.00001;
        System.out.printf("With a tolerance of %.5f:%n", tolerance);
        for (Double d : da) {
            boolean fuzzy = isLong(d, tolerance);
            System.out.printf("%.6f is %s integer%n", d, fuzzy ? "an" : "not an");
        }
        System.out.println();

        List<Double> fa = List.of(-2.1e120, -5e-2, Double.NaN, Double.POSITIVE_INFINITY);
        for (Double f : fa) {
            boolean exact = !f.isNaN() && !f.isInfinite() && isBigInteger(new BigDecimal(f.toString()));
            System.out.printf("%s is %s integer%n", f, exact ? "an" : "not an");
        }
        System.out.println();

        List<Complex> ca = List.of(new Complex(5.0, 0.0), new Complex(5.0, -5.0));
        for (Complex c : ca) {
            boolean exact = c.isLong();
            System.out.printf("%s is %s integer%n", c, exact ? "an" : "not an");
        }
        System.out.println();

        List<Rational> ra = List.of(new Rational(24, 8), new Rational(-5, 1), new Rational(17, 2));
        for (Rational r : ra) {
            boolean exact = r.isLong();
            System.out.printf("%s is %s integer%n", r, exact ? "an" : "not an");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def isint(f): 
    return complex(f).imag == 0 and complex(f).real.is_integer()

>>> [isint(f) for f in (1.0, 2, (3.0+0.0j), 4.1, (3+4j), (5.6+0j))]
[True, True, True, False, False, False]

>>> # Test cases
...
>>> isint(25.000000)
True
>>> isint(24.999999)
False
>>> isint(25.000100)
False
>>> isint(-2.1e120)
True
>>> isint(-5e-2)
False
>>> isint(float('nan'))
False
>>> isint(float('inf'))
False
>>> isint(5.0+0.0j)
True
>>> isint(5-5j)
False

```

### python_code_2.txt
```python
>>> a = 1.0000000000000001
>>> a
1.0
>>> 1.0 == 1.0000000000000001
True

```

