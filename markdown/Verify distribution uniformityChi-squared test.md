# Verify distribution uniformity/Chi-squared test

## Task Link
[Rosetta Code - Verify distribution uniformity/Chi-squared test](https://rosettacode.org/wiki/Verify_distribution_uniformity/Chi-squared_test)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.pow;
import java.util.Arrays;
import static java.util.Arrays.stream;
import org.apache.commons.math3.special.Gamma;

public class Test {

    static double x2Dist(double[] data) {
        double avg = stream(data).sum() / data.length;
        double sqs = stream(data).reduce(0, (a, b) -> a + pow((b - avg), 2));
        return sqs / avg;
    }

    static double x2Prob(double dof, double distance) {
        return Gamma.regularizedGammaQ(dof / 2, distance / 2);
    }

    static boolean x2IsUniform(double[] data, double significance) {
        return x2Prob(data.length - 1.0, x2Dist(data)) > significance;
    }

    public static void main(String[] a) {
        double[][] dataSets = {{199809, 200665, 199607, 200270, 199649},
        {522573, 244456, 139979, 71531, 21461}};

        System.out.printf(" %4s %12s  %12s %8s   %s%n",
                "dof", "distance", "probability", "Uniform?", "dataset");

        for (double[] ds : dataSets) {
            int dof = ds.length - 1;
            double dist = x2Dist(ds);
            double prob = x2Prob(dof, dist);
            System.out.printf("%4d %12.3f  %12.8f    %5s    %6s%n",
                    dof, dist, prob, x2IsUniform(ds, 0.05) ? "YES" : "NO",
                    Arrays.toString(ds));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import math
import random

def GammaInc_Q( a, x):
    a1 = a-1
    a2 = a-2
    def f0( t ):
        return t**a1*math.exp(-t)

    def df0(t):
        return (a1-t)*t**a2*math.exp(-t)
    
    y = a1
    while f0(y)*(x-y) >2.0e-8 and y < x: y += .3
    if y > x: y = x

    h = 3.0e-4
    n = int(y/h)
    h = y/n
    hh = 0.5*h
    gamax = h * sum( f0(t)+hh*df0(t) for t in ( h*j for j in xrange(n-1, -1, -1)))

    return gamax/gamma_spounge(a)

c = None
def gamma_spounge( z):
    global c
    a = 12

    if c is None:
       k1_factrl = 1.0
       c = []
       c.append(math.sqrt(2.0*math.pi))
       for k in range(1,a):
          c.append( math.exp(a-k) * (a-k)**(k-0.5) / k1_factrl )
          k1_factrl *= -k
    
    accm = c[0]
    for k in range(1,a):
        accm += c[k] / (z+k)
    accm *= math.exp( -(z+a)) * (z+a)**(z+0.5)
    return accm/z;

def chi2UniformDistance( dataSet ):
    expected = sum(dataSet)*1.0/len(dataSet)
    cntrd = (d-expected for d in dataSet)
    return sum(x*x for x in cntrd)/expected

def chi2Probability(dof, distance):
    return 1.0 - GammaInc_Q( 0.5*dof, 0.5*distance)

def chi2IsUniform(dataSet, significance):
    dof = len(dataSet)-1
    dist = chi2UniformDistance(dataSet)
    return chi2Probability( dof, dist ) > significance

dset1 = [ 199809, 200665, 199607, 200270, 199649 ]
dset2 = [ 522573, 244456, 139979,  71531,  21461 ]

for ds in (dset1, dset2):
    print "Data set:", ds
    dof = len(ds)-1
    distance =chi2UniformDistance(ds)
    print "dof: %d distance: %.4f" % (dof, distance),
    prob = chi2Probability( dof, distance)
    print "probability: %.4f"%prob,
    print "uniform? ", "Yes"if chi2IsUniform(ds,0.05) else "No"

```

### python_code_2.txt
```python
from scipy.stats import chisquare


if __name__ == '__main__':
    dataSets = [[199809, 200665, 199607, 200270, 199649],
                [522573, 244456, 139979,  71531,  21461]]
    print(f"{'Distance':^12} {'pvalue':^12} {'Uniform?':^8} {'Dataset'}")
    for ds in dataSets:
        dist, pvalue = chisquare(ds)
        uni = 'YES' if pvalue > 0.05 else 'NO'
        print(f"{dist:12.3f} {pvalue:12.8f} {uni:^8} {ds}")

```

