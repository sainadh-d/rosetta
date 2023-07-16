# Polynomial regression

## Task Link
[Rosetta Code - Polynomial regression](https://rosettacode.org/wiki/Polynomial_regression)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.function.IntToDoubleFunction;
import java.util.stream.IntStream;

public class PolynomialRegression {
    private static void polyRegression(int[] x, int[] y) {
        int n = x.length;
        double xm = Arrays.stream(x).average().orElse(Double.NaN);
        double ym = Arrays.stream(y).average().orElse(Double.NaN);
        double x2m = Arrays.stream(x).map(a -> a * a).average().orElse(Double.NaN);
        double x3m = Arrays.stream(x).map(a -> a * a * a).average().orElse(Double.NaN);
        double x4m = Arrays.stream(x).map(a -> a * a * a * a).average().orElse(Double.NaN);
        double xym = 0.0;
        for (int i = 0; i < x.length && i < y.length; ++i) {
            xym += x[i] * y[i];
        }
        xym /= Math.min(x.length, y.length);
        double x2ym = 0.0;
        for (int i = 0; i < x.length && i < y.length; ++i) {
            x2ym += x[i] * x[i] * y[i];
        }
        x2ym /= Math.min(x.length, y.length);

        double sxx = x2m - xm * xm;
        double sxy = xym - xm * ym;
        double sxx2 = x3m - xm * x2m;
        double sx2x2 = x4m - x2m * x2m;
        double sx2y = x2ym - x2m * ym;

        double b = (sxy * sx2x2 - sx2y * sxx2) / (sxx * sx2x2 - sxx2 * sxx2);
        double c = (sx2y * sxx - sxy * sxx2) / (sxx * sx2x2 - sxx2 * sxx2);
        double a = ym - b * xm - c * x2m;

        IntToDoubleFunction abc = (int xx) -> a + b * xx + c * xx * xx;

        System.out.println("y = " + a + " + " + b + "x + " + c + "x^2");
        System.out.println(" Input  Approximation");
        System.out.println(" x   y     y1");
        for (int i = 0; i < n; ++i) {
            System.out.printf("%2d %3d  %5.1f\n", x[i], y[i], abc.applyAsDouble(x[i]));
        }
    }

    public static void main(String[] args) {
        int[] x = IntStream.range(0, 11).toArray();
        int[] y = new int[]{1, 6, 17, 34, 57, 86, 121, 162, 209, 262, 321};
        polyRegression(x, y);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> x = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
>>> y = [1,   6,  17,  34,  57,  86, 121, 162, 209, 262, 321]
>>> coeffs = numpy.polyfit(x,y,deg=2)
>>> coeffs
array([ 3.,  2.,  1.])

```

### python_code_2.txt
```python
>>> yf = numpy.polyval(numpy.poly1d(coeffs), x)
>>> yf
array([   1.,    6.,   17.,   34.,   57.,   86.,  121.,  162.,  209., 262.,  321.])

```

### python_code_3.txt
```python
>>> '%.1g' % max(y-yf)
'1e-013'

```

### python_code_4.txt
```python
>>> x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [2.7, 2.8, 31.4, 38.1, 58.0, 76.2, 100.5, 130.0, 149.3, 180.0]

```

### python_code_5.txt
```python
>>> p = numpy.poly1d(numpy.polyfit(x, y, deg=2), variable='N')
>>> print p
       2
1.085 N + 10.36 N - 0.6164

```

