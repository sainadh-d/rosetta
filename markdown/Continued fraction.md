# Continued fraction

## Task Link
[Rosetta Code - Continued fraction](https://rosettacode.org/wiki/Continued_fraction)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.pow;
import java.util.*;
import java.util.function.Function;

public class Test {
    static double calc(Function<Integer, Integer[]> f, int n) {
        double temp = 0;

        for (int ni = n; ni >= 1; ni--) {
            Integer[] p = f.apply(ni);
            temp = p[1] / (double) (p[0] + temp);
        }
        return f.apply(0)[0] + temp;
    }

    public static void main(String[] args) {
        List<Function<Integer, Integer[]>> fList = new ArrayList<>();
        fList.add(n -> new Integer[]{n > 0 ? 2 : 1, 1});
        fList.add(n -> new Integer[]{n > 0 ? n : 2, n > 1 ? (n - 1) : 1});
        fList.add(n -> new Integer[]{n > 0 ? 6 : 3, (int) pow(2 * n - 1, 2)});

        for (Function<Integer, Integer[]> f : fList)
            System.out.println(calc(f, 200));
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction
import itertools
try: zip = itertools.izip
except: pass
 
# The Continued Fraction
def CF(a, b, t):
  terms = list(itertools.islice(zip(a, b), t))
  z = Fraction(1,1)
  for a, b in reversed(terms):
    z = a + b / z
  return z
 
# Approximates a fraction to a string
def pRes(x, d):
  q, x = divmod(x, 1)
  res = str(q)
  res += "."
  for i in range(d):
    x *= 10
    q, x = divmod(x, 1)
    res += str(q)
  return res
 
# Test the Continued Fraction for sqrt2
def sqrt2_a():
  yield 1
  for x in itertools.repeat(2):
    yield x
 
def sqrt2_b():
  for x in itertools.repeat(1):
    yield x
 
cf = CF(sqrt2_a(), sqrt2_b(), 950)
print(pRes(cf, 200))
#1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206057147
 
 
# Test the Continued Fraction for Napier's Constant
def Napier_a():
  yield 2
  for x in itertools.count(1):
    yield x
 
def Napier_b():
  yield 1
  for x in itertools.count(1):
    yield x
 
cf = CF(Napier_a(), Napier_b(), 950)
print(pRes(cf, 200))
#2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639193200305992181741359662904357290033429526059563073813232862794349076323382988075319525101901
 
# Test the Continued Fraction for Pi
def Pi_a():
  yield 3
  for x in itertools.repeat(6):
    yield x
 
def Pi_b():
  for x in itertools.count(1,2):
    yield x*x
 
cf = CF(Pi_a(), Pi_b(), 950)
print(pRes(cf, 10))
#3.1415926532

```

### python_code_2.txt
```python
from decimal import Decimal, getcontext

def calc(fun, n):
    temp = Decimal("0.0")

    for ni in xrange(n+1, 0, -1):
        (a, b) = fun(ni)
        temp = Decimal(b) / (a + temp)

    return fun(0)[0] + temp

def fsqrt2(n):
    return (2 if n > 0 else 1, 1)

def fnapier(n):
    return (n if n > 0 else 2, (n - 1) if n > 1 else 1)

def fpi(n):
    return (6 if n > 0 else 3, (2 * n - 1) ** 2)

getcontext().prec = 50
print calc(fsqrt2, 200)
print calc(fnapier, 200)
print calc(fpi, 200)

```

