# Logistic curve fitting in epidemiology

## Task Link
[Rosetta Code - Logistic curve fitting in epidemiology](https://rosettacode.org/wiki/Logistic_curve_fitting_in_epidemiology)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.function.Function;

public class LogisticCurveFitting {
    private static final double K = 7.8e9;
    private static final int N0 = 27;

    private static final List<Double> ACTUAL = List.of(
        27.0, 27.0, 27.0, 44.0, 44.0, 59.0, 59.0, 59.0, 59.0, 59.0, 59.0, 59.0, 59.0, 60.0, 60.0,
        61.0, 61.0, 66.0, 83.0, 219.0, 239.0, 392.0, 534.0, 631.0, 897.0, 1350.0, 2023.0, 2820.0,
        4587.0, 6067.0, 7823.0, 9826.0, 11946.0, 14554.0, 17372.0, 20615.0, 24522.0, 28273.0,
        31491.0, 34933.0, 37552.0, 40540.0, 43105.0, 45177.0, 60328.0, 64543.0, 67103.0,
        69265.0, 71332.0, 73327.0, 75191.0, 75723.0, 76719.0, 77804.0, 78812.0, 79339.0,
        80132.0, 80995.0, 82101.0, 83365.0, 85203.0, 87024.0, 89068.0, 90664.0, 93077.0,
        95316.0, 98172.0, 102133.0, 105824.0, 109695.0, 114232.0, 118610.0, 125497.0,
        133852.0, 143227.0, 151367.0, 167418.0, 180096.0, 194836.0, 213150.0, 242364.0,
        271106.0, 305117.0, 338133.0, 377918.0, 416845.0, 468049.0, 527767.0, 591704.0,
        656866.0, 715353.0, 777796.0, 851308.0, 928436.0, 1000249.0, 1082054.0, 1174652.0
    );

    private static double f(double r) {
        var sq = 0.0;
        var len = ACTUAL.size();
        for (int i = 0; i < len; i++) {
            var eri = Math.exp(r * i);
            var guess = (N0 * eri) / (1.0 + N0 * (eri - 1.0) / K);
            var diff = guess - ACTUAL.get(i);
            sq += diff * diff;
        }
        return sq;
    }

    private static double solve(Function<Double, Double> fn) {
        return solve(fn, 0.5, 0.0);
    }

    private static double solve(Function<Double, Double> fn, double guess, double epsilon) {
        double delta;
        if (guess != 0.0) {
            delta = guess;
        } else {
            delta = 1.0;
        }

        var f0 = fn.apply(guess);
        var factor = 2.0;

        while (delta > epsilon && guess != guess - delta) {
            var nf = fn.apply(guess - delta);
            if (nf < f0) {
                f0 = nf;
                guess -= delta;
            } else {
                nf = fn.apply(guess + delta);
                if (nf < f0) {
                    f0 = nf;
                    guess += delta;
                } else {
                    factor = 0.5;
                }
            }

            delta *= factor;
        }

        return guess;
    }

    public static void main(String[] args) {
        var r = solve(LogisticCurveFitting::f);
        var r0 = Math.exp(12.0 * r);
        System.out.printf("r = %.16f, R0 = %.16f\n", r, r0);
    }
}

```

## Python Code
### python_code_1.txt
```python
import numpy as np
import scipy.optimize as opt

n0, K = 27, 7_800_000_000

def f(t, r):
    return (n0 * np.exp(r * t)) / (( 1 + n0 * (np.exp(r * t) - 1) / K))

y = [
27, 27, 27, 44, 44, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60,
61, 61, 66, 83, 219, 239, 392, 534, 631, 897, 1350, 2023,
2820, 4587, 6067, 7823, 9826, 11946, 14554, 17372, 20615,
24522, 28273, 31491, 34933, 37552, 40540, 43105, 45177,
60328, 64543, 67103, 69265, 71332, 73327, 75191, 75723,
76719, 77804, 78812, 79339, 80132, 80995, 82101, 83365,
85203, 87024, 89068, 90664, 93077, 95316, 98172, 102133,
105824, 109695, 114232, 118610, 125497, 133852, 143227,
151367, 167418, 180096, 194836, 213150, 242364, 271106,
305117, 338133, 377918, 416845, 468049, 527767, 591704,
656866, 715353, 777796, 851308, 928436, 1000249, 1082054,
1174652,
]
x = np.linspace(0.0, 96, 97)

r, cov = opt.curve_fit(f, x, y, [0.5])

# Our answer for r given the world data and simplistic model
print("The r for the world Covid-19 data is:", r,
    ", with covariance of", cov)   
print("The calculated R0 is then", np.exp(12 * r))

```

