# Numerical integration/Gauss-Legendre Quadrature

## Task Link
[Rosetta Code - Numerical integration/Gauss-Legendre Quadrature](https://rosettacode.org/wiki/Numerical_integration/Gauss-Legendre_Quadrature)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.*;
import java.util.function.Function;

public class Test {
    final static int N = 5;

    static double[] lroots = new double[N];
    static double[] weight = new double[N];
    static double[][] lcoef = new double[N + 1][N + 1];

    static void legeCoef() {
        lcoef[0][0] = lcoef[1][1] = 1;

        for (int n = 2; n <= N; n++) {

            lcoef[n][0] = -(n - 1) * lcoef[n - 2][0] / n;

            for (int i = 1; i <= n; i++) {
                lcoef[n][i] = ((2 * n - 1) * lcoef[n - 1][i - 1]
                        - (n - 1) * lcoef[n - 2][i]) / n;
            }
        }
    }

    static double legeEval(int n, double x) {
        double s = lcoef[n][n];
        for (int i = n; i > 0; i--)
            s = s * x + lcoef[n][i - 1];
        return s;
    }

    static double legeDiff(int n, double x) {
        return n * (x * legeEval(n, x) - legeEval(n - 1, x)) / (x * x - 1);
    }

    static void legeRoots() {
        double x, x1;
        for (int i = 1; i <= N; i++) {
            x = cos(PI * (i - 0.25) / (N + 0.5));
            do {
                x1 = x;
                x -= legeEval(N, x) / legeDiff(N, x);
            } while (x != x1);

            lroots[i - 1] = x;

            x1 = legeDiff(N, x);
            weight[i - 1] = 2 / ((1 - x * x) * x1 * x1);
        }
    }

    static double legeInte(Function<Double, Double> f, double a, double b) {
        double c1 = (b - a) / 2, c2 = (b + a) / 2, sum = 0;
        for (int i = 0; i < N; i++)
            sum += weight[i] * f.apply(c1 * lroots[i] + c2);
        return c1 * sum;
    }

    public static void main(String[] args) {
        legeCoef();
        legeRoots();

        System.out.print("Roots: ");
        for (int i = 0; i < N; i++)
            System.out.printf(" %f", lroots[i]);

        System.out.print("\nWeight:");
        for (int i = 0; i < N; i++)
            System.out.printf(" %f", weight[i]);

        System.out.printf("%nintegrating Exp(x) over [-3, 3]:%n\t%10.8f,%n"
                + "compared to actual%n\t%10.8f%n",
                legeInte(x -> exp(x), -3, 3), exp(3) - exp(-3));
    }
}

```

## Python Code
### python_code_1.txt
```python
from numpy import *
 
##################################################################
# Recursive generation of the Legendre polynomial of order n
def Legendre(n,x):
	x=array(x)
	if (n==0):
		return x*0+1.0
	elif (n==1):
		return x
	else:
		return ((2.0*n-1.0)*x*Legendre(n-1,x)-(n-1)*Legendre(n-2,x))/n
 
##################################################################
# Derivative of the Legendre polynomials
def DLegendre(n,x):
	x=array(x)
	if (n==0):
		return x*0
	elif (n==1):
		return x*0+1.0
	else:
		return (n/(x**2-1.0))*(x*Legendre(n,x)-Legendre(n-1,x))
##################################################################
# Roots of the polynomial obtained using Newton-Raphson method
def LegendreRoots(polyorder,tolerance=1e-20):
	if polyorder<2:
		err=1 # bad polyorder no roots can be found
	else:
		roots=[]
		# The polynomials are alternately even and odd functions. So we evaluate only half the number of roots. 
		for i in range(1,int(polyorder)/2 +1):
			x=cos(pi*(i-0.25)/(polyorder+0.5))
			error=10*tolerance
		        iters=0
		        while (error>tolerance) and (iters<1000):
		                dx=-Legendre(polyorder,x)/DLegendre(polyorder,x)
		                x=x+dx
		                iters=iters+1
		                error=abs(dx)
			roots.append(x)
		# Use symmetry to get the other roots
		roots=array(roots)
		if polyorder%2==0:
			roots=concatenate( (-1.0*roots, roots[::-1]) )
		else:
			roots=concatenate( (-1.0*roots, [0.0], roots[::-1]) )
		err=0 # successfully determined roots
	return [roots, err]
##################################################################
# Weight coefficients
def GaussLegendreWeights(polyorder):
	W=[]
	[xis,err]=LegendreRoots(polyorder)
	if err==0:
		W=2.0/( (1.0-xis**2)*(DLegendre(polyorder,xis)**2) )
		err=0
	else:
		err=1 # could not determine roots - so no weights
	return [W, xis, err]
##################################################################
# The integral value 
# func 		: the integrand
# a, b 		: lower and upper limits of the integral
# polyorder 	: order of the Legendre polynomial to be used
#
def GaussLegendreQuadrature(func, polyorder, a, b):
	[Ws,xs, err]= GaussLegendreWeights(polyorder)
	if err==0:
		ans=(b-a)*0.5*sum( Ws*func( (b-a)*0.5*xs+ (b+a)*0.5 ) )
	else: 
		# (in case of error)
		err=1
		ans=None
	return [ans,err]
##################################################################
# The integrand - change as required
def func(x):
	return exp(x)
##################################################################
# 
 
order=5
[Ws,xs,err]=GaussLegendreWeights(order)
if err==0:
	print "Order    : ", order
	print "Roots    : ", xs
	print "Weights  : ", Ws
else:
	print "Roots/Weights evaluation failed"
 
# Integrating the function
[ans,err]=GaussLegendreQuadrature(func , order, -3,3)
if err==0:
	print "Integral : ", ans
else:
	print "Integral evaluation failed"

```

### python_code_2.txt
```python
import numpy as np

# func is a function that takes a list-like input values
def gauss_legendre_integrate(func, domain, deg):
    x, w = np.polynomial.legendre.leggauss(deg)
    s = (domain[1] - domain[0])/2
    a = (domain[1] + domain[0])/2
    return np.sum(s*w*func(s*x + a))

for d in range(3, 10):
    print(d, gauss_legendre_integrate(np.exp, [-3, 3], d))

```

