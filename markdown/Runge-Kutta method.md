# Runge-Kutta method

## Task Link
[Rosetta Code - Runge-Kutta method](https://rosettacode.org/wiki/Runge-Kutta_method)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;
import java.util.function.BiFunction;

public class RungeKutta {

    static void runge(BiFunction<Double, Double, Double> yp_func, double[] t,
            double[] y, double dt) {

        for (int n = 0; n < t.length - 1; n++) {
            double dy1 = dt * yp_func.apply(t[n], y[n]);
            double dy2 = dt * yp_func.apply(t[n] + dt / 2.0, y[n] + dy1 / 2.0);
            double dy3 = dt * yp_func.apply(t[n] + dt / 2.0, y[n] + dy2 / 2.0);
            double dy4 = dt * yp_func.apply(t[n] + dt, y[n] + dy3);
            t[n + 1] = t[n] + dt;
            y[n + 1] = y[n] + (dy1 + 2.0 * (dy2 + dy3) + dy4) / 6.0;
        }
    }

    static double calc_err(double t, double calc) {
        double actual = pow(pow(t, 2.0) + 4.0, 2) / 16.0;
        return abs(actual - calc);
    }

    public static void main(String[] args) {
        double dt = 0.10;
        double[] t_arr = new double[101];
        double[] y_arr = new double[101];
        y_arr[0] = 1.0;

        runge((t, y) -> t * sqrt(y), t_arr, y_arr, dt);

        for (int i = 0; i < t_arr.length; i++)
            if (i % 10 == 0)
                System.out.printf("y(%.1f) = %.8f Error: %.6f%n",
                        t_arr[i], y_arr[i],
                        calc_err(t_arr[i], y_arr[i]));
    }
}

```

## Python Code
### python_code_1.txt
```python
from math import sqrt
 
def rk4(f, x0, y0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy
 
def f(x, y):
    return x * sqrt(y)
 
vx, vy = rk4(f, 0, 1, 10, 100)
for x, y in list(zip(vx, vy))[::10]:
    print("%4.1f %10.5f %+12.4e" % (x, y, y - (4 + x * x)**2 / 16))

 0.0    1.00000  +0.0000e+00
 1.0    1.56250  -1.4572e-07
 2.0    4.00000  -9.1948e-07
 3.0   10.56250  -2.9096e-06
 4.0   24.99999  -6.2349e-06
 5.0   52.56249  -1.0820e-05
 6.0   99.99998  -1.6595e-05
 7.0  175.56248  -2.3518e-05
 8.0  288.99997  -3.1565e-05
 9.0  451.56246  -4.0723e-05
10.0  675.99995  -5.0983e-05

```

