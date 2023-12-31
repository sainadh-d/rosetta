# Deming's funnel

## Task Link
[Rosetta Code - Deming's funnel](https://rosettacode.org/wiki/Deming%27s_funnel)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;
import java.util.Arrays;
import java.util.function.BiFunction;

public class DemingsFunnel {

    public static void main(String[] args) {
        double[] dxs = {
            -0.533, 0.270, 0.859, -0.043, -0.205, -0.127, -0.071, 0.275,
            1.251, -0.231, -0.401, 0.269, 0.491, 0.951, 1.150, 0.001,
            -0.382, 0.161, 0.915, 2.080, -2.337, 0.034, -0.126, 0.014,
            0.709, 0.129, -1.093, -0.483, -1.193, 0.020, -0.051, 0.047,
            -0.095, 0.695, 0.340, -0.182, 0.287, 0.213, -0.423, -0.021,
            -0.134, 1.798, 0.021, -1.099, -0.361, 1.636, -1.134, 1.315,
            0.201, 0.034, 0.097, -0.170, 0.054, -0.553, -0.024, -0.181,
            -0.700, -0.361, -0.789, 0.279, -0.174, -0.009, -0.323, -0.658,
            0.348, -0.528, 0.881, 0.021, -0.853, 0.157, 0.648, 1.774,
            -1.043, 0.051, 0.021, 0.247, -0.310, 0.171, 0.000, 0.106,
            0.024, -0.386, 0.962, 0.765, -0.125, -0.289, 0.521, 0.017,
            0.281, -0.749, -0.149, -2.436, -0.909, 0.394, -0.113, -0.598,
            0.443, -0.521, -0.799, 0.087};

        double[] dys = {
            0.136, 0.717, 0.459, -0.225, 1.392, 0.385, 0.121, -0.395,
            0.490, -0.682, -0.065, 0.242, -0.288, 0.658, 0.459, 0.000,
            0.426, 0.205, -0.765, -2.188, -0.742, -0.010, 0.089, 0.208,
            0.585, 0.633, -0.444, -0.351, -1.087, 0.199, 0.701, 0.096,
            -0.025, -0.868, 1.051, 0.157, 0.216, 0.162, 0.249, -0.007,
            0.009, 0.508, -0.790, 0.723, 0.881, -0.508, 0.393, -0.226,
            0.710, 0.038, -0.217, 0.831, 0.480, 0.407, 0.447, -0.295,
            1.126, 0.380, 0.549, -0.445, -0.046, 0.428, -0.074, 0.217,
            -0.822, 0.491, 1.347, -0.141, 1.230, -0.044, 0.079, 0.219,
            0.698, 0.275, 0.056, 0.031, 0.421, 0.064, 0.721, 0.104,
            -0.729, 0.650, -1.103, 0.154, -1.720, 0.051, -0.385, 0.477,
            1.537, -0.901, 0.939, -0.411, 0.341, -0.411, 0.106, 0.224,
            -0.947, -1.424, -0.542, -1.032};

        experiment("Rule 1:", dxs, dys, (z, dz) -> 0.0);
        experiment("Rule 2:", dxs, dys, (z, dz) -> -dz);
        experiment("Rule 3:", dxs, dys, (z, dz) -> -(z + dz));
        experiment("Rule 4:", dxs, dys, (z, dz) -> z + dz);
    }

    static void experiment(String label, double[] dxs, double[] dys,
            BiFunction<Double, Double, Double> rule) {

        double[] resx = funnel(dxs, rule);
        double[] resy = funnel(dys, rule);
        System.out.println(label);
        System.out.printf("Mean x, y:    %.4f, %.4f%n", mean(resx), mean(resy));
        System.out.printf("Std dev x, y: %.4f, %.4f%n", stdDev(resx), stdDev(resy));
        System.out.println();
    }

    static double[] funnel(double[] input, BiFunction<Double, Double, Double> rule) {
        double x = 0;
        double[] result = new double[input.length];

        for (int i = 0; i < input.length; i++) {
            double rx = x + input[i];
            x = rule.apply(x, input[i]);
            result[i] = rx;
        }
        return result;
    }

    static double mean(double[] xs) {
        return Arrays.stream(xs).sum() / xs.length;
    }

    static double stdDev(double[] xs) {
        double m = mean(xs);
        return sqrt(Arrays.stream(xs).map(x -> pow((x - m), 2)).sum() / xs.length);
    }
}

```

## Python Code
### python_code_1.txt
```python
import math 

dxs = [-0.533, 0.27, 0.859, -0.043, -0.205, -0.127, -0.071, 0.275, 1.251,
       -0.231, -0.401, 0.269, 0.491, 0.951, 1.15, 0.001, -0.382, 0.161, 0.915,
       2.08, -2.337, 0.034, -0.126, 0.014, 0.709, 0.129, -1.093, -0.483, -1.193, 
       0.02, -0.051, 0.047, -0.095, 0.695, 0.34, -0.182, 0.287, 0.213, -0.423,
       -0.021, -0.134, 1.798, 0.021, -1.099, -0.361, 1.636, -1.134, 1.315, 0.201, 
       0.034, 0.097, -0.17, 0.054, -0.553, -0.024, -0.181, -0.7, -0.361, -0.789,
       0.279, -0.174, -0.009, -0.323, -0.658, 0.348, -0.528, 0.881, 0.021, -0.853,
       0.157, 0.648, 1.774, -1.043, 0.051, 0.021, 0.247, -0.31, 0.171, 0.0, 0.106,
       0.024, -0.386, 0.962, 0.765, -0.125, -0.289, 0.521, 0.017, 0.281, -0.749,
       -0.149, -2.436, -0.909, 0.394, -0.113, -0.598, 0.443, -0.521, -0.799, 
       0.087]

dys = [0.136, 0.717, 0.459, -0.225, 1.392, 0.385, 0.121, -0.395, 0.49, -0.682,
       -0.065, 0.242, -0.288, 0.658, 0.459, 0.0, 0.426, 0.205, -0.765, -2.188, 
       -0.742, -0.01, 0.089, 0.208, 0.585, 0.633, -0.444, -0.351, -1.087, 0.199,
       0.701, 0.096, -0.025, -0.868, 1.051, 0.157, 0.216, 0.162, 0.249, -0.007, 
       0.009, 0.508, -0.79, 0.723, 0.881, -0.508, 0.393, -0.226, 0.71, 0.038, 
       -0.217, 0.831, 0.48, 0.407, 0.447, -0.295, 1.126, 0.38, 0.549, -0.445, 
       -0.046, 0.428, -0.074, 0.217, -0.822, 0.491, 1.347, -0.141, 1.23, -0.044, 
       0.079, 0.219, 0.698, 0.275, 0.056, 0.031, 0.421, 0.064, 0.721, 0.104, 
       -0.729, 0.65, -1.103, 0.154, -1.72, 0.051, -0.385, 0.477, 1.537, -0.901, 
       0.939, -0.411, 0.341, -0.411, 0.106, 0.224, -0.947, -1.424, -0.542, -1.032]

def funnel(dxs, rule):
    x, rxs = 0, []
    for dx in dxs:
        rxs.append(x + dx)
        x = rule(x, dx)
    return rxs

def mean(xs): return sum(xs) / len(xs)

def stddev(xs):
    m = mean(xs)
    return math.sqrt(sum((x-m)**2 for x in xs) / len(xs))

def experiment(label, rule):
    rxs, rys = funnel(dxs, rule), funnel(dys, rule)
    print label
    print 'Mean x, y    : %.4f, %.4f' % (mean(rxs), mean(rys))
    print 'Std dev x, y : %.4f, %.4f' % (stddev(rxs), stddev(rys))
    print


experiment('Rule 1:', lambda z, dz: 0)
experiment('Rule 2:', lambda z, dz: -dz)
experiment('Rule 3:', lambda z, dz: -(z+dz))
experiment('Rule 4:', lambda z, dz: z+dz)

```

### python_code_2.txt
```python
from random import gauss
from math import sqrt
from pprint import pprint as pp

NMAX=50

def statscreator():
    sum_ = sum2 = n = 0
    def stats(x):
        nonlocal sum_, sum2, n

        sum_ += x
        sum2 += x*x
        n    += 1.0
        return sum_/n, sqrt(sum2/n - sum_*sum_/n/n)
    return stats

def drop(target, sigma=1.0):
    'Drop ball at target'
    return gauss(target, sigma)

def deming(rule, nmax=NMAX):
    ''' Simulate Demings funnel in 1D. '''
    
    stats = statscreator()
    target = 0
    for i in range(nmax):
        value = drop(target)
        mean, sdev = stats(value)
        target = rule(target, value)
        if i == nmax - 1:
            return mean, sdev

def d1(target, value):
    ''' Keep Funnel over target. '''

    return target


def d2(target, value):
    ''' The new target starts at the center, 0,0 then is adjusted to
    be the previous target _minus_ the offset of the new drop from the
    previous target. '''
    
    return -value   # - (target - (target - value)) = - value

def d3(target, value):
    ''' The new target starts at the center, 0,0 then is adjusted to
    be the previous target _minus_ the offset of the new drop from the
    center, 0.0. '''
    
    return target - value

def d4(target, value):
    ''' (Dumb). The new target is where it last dropped. '''
    
    return value


def printit(rule, trials=5):
    print('\nDeming simulation. %i trials using rule %s:\n %s'
          % (trials, rule.__name__.upper(), rule.__doc__))
    for i in range(trials):
        print('    Mean: %7.3f, Sdev: %7.3f' % deming(rule))


if __name__ == '__main__':
    rcomments = [ (d1, 'Should have smallest deviations ~1.0, and be centered on 0.0'),
                  (d2, 'Should be centred on 0.0 with larger deviations than D1'),
                  (d3, 'Should be centred on 0.0 with larger deviations than D1'),
                  (d4, 'Center wanders all over the place, with deviations to match!'),
                ]
    for rule, comment in rcomments:
        printit(rule)
        print('  %s\n' % comment)

```

