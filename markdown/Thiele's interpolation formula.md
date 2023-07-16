# Thiele's interpolation formula

## Task Link
[Rosetta Code - Thiele's interpolation formula](https://rosettacode.org/wiki/Thiele%27s_interpolation_formula)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;

public class Test {
    final static int N = 32;
    final static int N2 = (N * (N - 1) / 2);
    final static double STEP = 0.05;

    static double[] xval = new double[N];
    static double[] t_sin = new double[N];
    static double[] t_cos = new double[N];
    static double[] t_tan = new double[N];

    static double[] r_sin = new double[N2];
    static double[] r_cos = new double[N2];
    static double[] r_tan = new double[N2];

    static double rho(double[] x, double[] y, double[] r, int i, int n) {
        if (n < 0)
            return 0;

        if (n == 0)
            return y[i];

        int idx = (N - 1 - n) * (N - n) / 2 + i;
        if (r[idx] != r[idx])
            r[idx] = (x[i] - x[i + n])
                    / (rho(x, y, r, i, n - 1) - rho(x, y, r, i + 1, n - 1))
                    + rho(x, y, r, i + 1, n - 2);

        return r[idx];
    }

    static double thiele(double[] x, double[] y, double[] r, double xin, int n) {
        if (n > N - 1)
            return 1;
        return rho(x, y, r, 0, n) - rho(x, y, r, 0, n - 2)
                + (xin - x[n]) / thiele(x, y, r, xin, n + 1);
    }

    public static void main(String[] args) {
        for (int i = 0; i < N; i++) {
            xval[i] = i * STEP;
            t_sin[i] = sin(xval[i]);
            t_cos[i] = cos(xval[i]);
            t_tan[i] = t_sin[i] / t_cos[i];
        }

        for (int i = 0; i < N2; i++)
            r_sin[i] = r_cos[i] = r_tan[i] = Double.NaN;

        System.out.printf("%16.14f%n", 6 * thiele(t_sin, xval, r_sin, 0.5, 0));
        System.out.printf("%16.14f%n", 3 * thiele(t_cos, xval, r_cos, 0.5, 0));
        System.out.printf("%16.14f%n", 4 * thiele(t_tan, xval, r_tan, 1.0, 0));
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import math

def thieleInterpolator(x, y):
    ρ = [[yi]*(len(y)-i) for i, yi in enumerate(y)]
    for i in range(len(ρ)-1):
        ρ[i][1] = (x[i] - x[i+1]) / (ρ[i][0] - ρ[i+1][0])
    for i in range(2, len(ρ)):
        for j in range(len(ρ)-i):
            ρ[j][i] = (x[j]-x[j+i]) / (ρ[j][i-1]-ρ[j+1][i-1]) + ρ[j+1][i-2]
    ρ0 = ρ[0]
    def t(xin):
        a = 0
        for i in range(len(ρ0)-1, 1, -1):
            a = (xin - x[i-1]) / (ρ0[i] - ρ0[i-2] + a)
        return y[0] + (xin-x[0]) / (ρ0[1]+a)
    return t

# task 1: build 32 row trig table
xVal = [i*.05 for i in range(32)]
tSin = [math.sin(x) for x in xVal]
tCos = [math.cos(x) for x in xVal]
tTan = [math.tan(x) for x in xVal]
# task 2: define inverses
iSin = thieleInterpolator(tSin, xVal)
iCos = thieleInterpolator(tCos, xVal)
iTan = thieleInterpolator(tTan, xVal)
# task 3: demonstrate identities
print('{:16.14f}'.format(6*iSin(.5)))
print('{:16.14f}'.format(3*iCos(.5)))
print('{:16.14f}'.format(4*iTan(1)))

```

