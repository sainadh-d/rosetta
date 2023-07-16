# Gamma function

## Task Link
[Rosetta Code - Gamma function](https://rosettacode.org/wiki/Gamma_function)

## Java Code
### java_code_1.txt
```java
public class GammaFunction {

	public double st_gamma(double x){
		return Math.sqrt(2*Math.PI/x)*Math.pow((x/Math.E), x);
	}
	
	public double la_gamma(double x){
		double[] p = {0.99999999999980993, 676.5203681218851, -1259.1392167224028,
			     	  771.32342877765313, -176.61502916214059, 12.507343278686905,
			     	  -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7};
		int g = 7;
		if(x < 0.5) return Math.PI / (Math.sin(Math.PI * x)*la_gamma(1-x));

		x -= 1;
		double a = p[0];
		double t = x+g+0.5;
		for(int i = 1; i < p.length; i++){
			a += p[i]/(x+i);
		}
		
		return Math.sqrt(2*Math.PI)*Math.pow(t, x+0.5)*Math.exp(-t)*a;
	}
	
	public static void main(String[] args) {
		GammaFunction test = new GammaFunction();
		System.out.println("Gamma \t\tStirling \t\tLanczos");
		for(double i = 1; i <= 20; i += 1){
			System.out.println("" + i/10.0 + "\t\t" + test.st_gamma(i/10.0) + "\t" + test.la_gamma(i/10.0));
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
_a =    ( 1.00000000000000000000, 0.57721566490153286061, -0.65587807152025388108,
         -0.04200263503409523553, 0.16653861138229148950, -0.04219773455554433675,
         -0.00962197152787697356, 0.00721894324666309954, -0.00116516759185906511,
         -0.00021524167411495097, 0.00012805028238811619, -0.00002013485478078824,
         -0.00000125049348214267, 0.00000113302723198170, -0.00000020563384169776,
          0.00000000611609510448, 0.00000000500200764447, -0.00000000118127457049,
          0.00000000010434267117, 0.00000000000778226344, -0.00000000000369680562,
          0.00000000000051003703, -0.00000000000002058326, -0.00000000000000534812,
          0.00000000000000122678, -0.00000000000000011813, 0.00000000000000000119,
          0.00000000000000000141, -0.00000000000000000023, 0.00000000000000000002
       )
def gamma (x): 
   y  = float(x) - 1.0;
   sm = _a[-1];
   for an in _a[-2::-1]:
      sm = sm * y + an;
   return 1.0 / sm;
 

if __name__ == '__main__':
    for i in range(1,11):
        print "  %20.14e" % gamma(i/3.0)

```

### python_code_2.txt
```python
'''Gamma function'''

from functools import reduce


# gamma_ :: [Float] -> Float -> Float
def gamma_(tbl):
    '''Gamma function.'''
    def go(x):
        y = float(x) - 1.0
        return 1.0 / reduce(
            lambda a, x: a * y + x,
            tbl[-2::-1],
            tbl[-1]
        )
    return lambda x: go(x)


# TBL :: [Float]
TBL = [
    1.00000000000000000000, 0.57721566490153286061,
    -0.65587807152025388108, -0.04200263503409523553,
    0.16653861138229148950, -0.04219773455554433675,
    -0.00962197152787697356, 0.00721894324666309954,
    -0.00116516759185906511, -0.00021524167411495097,
    0.00012805028238811619, -0.00002013485478078824,
    -0.00000125049348214267, 0.00000113302723198170,
    -0.00000020563384169776, 0.00000000611609510448,
    0.00000000500200764447, -0.00000000118127457049,
    0.00000000010434267117, 0.00000000000778226344,
    -0.00000000000369680562, 0.00000000000051003703,
    -0.00000000000002058326, -0.00000000000000534812,
    0.00000000000000122678, -0.00000000000000011813,
    0.00000000000000000119, 0.00000000000000000141,
    -0.00000000000000000023, 0.00000000000000000002
]


# TEST ----------------------------------------------------
# main :: IO()
def main():
    '''Gamma function over a range of values.'''

    gamma = gamma_(TBL)
    print(
        fTable(' i -> gamma(i/3):\n')(repr)(lambda x: "%0.7e" % x)(
            lambda x: gamma(x / 3.0)
        )(enumFromTo(1)(10))
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# FORMATTING -------------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
from mpmath import mp

mp.dps = 50

def gamma_coef(n):
    a = [mp.mpf(1), mp.mpf(mp.euler)]
    for k in range(3, n + 1):
        s = sum((-1)**j * mp.zeta(j) * a[k - j - 1] for j in range(2, k))
        a.append((s - a[1] * a[k - 2]) / (1 - k * a[0]))
    return a

def horner(a, x):
    y = 0
    for s in reversed(a):
        y = y * x + s
    return y

gc = gamma_coef(30)

def gamma_approx(x):
    y = mp.mpf(1)
    while x < 0.5:
        y /= x
        x += 1
    while x > 1.5:
        x -= 1
        y *= x
    return y / horner(gc, x - 1)

for x in gc:
    print(mp.nstr(x, 25))

```

