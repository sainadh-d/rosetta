# Calculating the value of e

## Task Link
[Rosetta Code - Calculating the value of e](https://rosettacode.org/wiki/Calculating_the_value_of_e)

## Java Code
### java_code_1.txt
```java
double e(long limit) {
    double e = 1;
    for (long term = 1; term <= limit; term++)
        e += 1d / factorial(term);
    return e;
}

long factorial(long value) {
    return value == 1 ? value : value * factorial(--value);
}

```

### java_code_2.txt
```java
import static java.math.RoundingMode.HALF_UP;
import java.math.BigDecimal;
import java.math.BigInteger;

```

### java_code_3.txt
```java
BigDecimal e(BigInteger limit, int scale) {
    BigDecimal e = BigDecimal.ONE.setScale(scale, HALF_UP);
    BigDecimal n;
    BigInteger term = BigInteger.ONE;
    while (term.compareTo(limit) <= 0) {
        n = new BigDecimal(String.valueOf(factorial(term)));
        e = e.add(BigDecimal.ONE.divide(n, scale, HALF_UP));
        term = term.add(BigInteger.ONE);
    }
    return e;
}

BigInteger factorial(BigInteger value) {
    if (value.compareTo(BigInteger.ONE) > 0) {
        return value.multiply(factorial(value.subtract(BigInteger.ONE)));
    } else {
        return BigInteger.ONE;
    }
}

```

### java_code_4.txt
```java
BigDecimal e = e(BigInteger.valueOf(100), 1000);

```

### java_code_5.txt
```java
public class CalculateE {
    public static final double EPSILON = 1.0e-15;

    public static void main(String[] args) {
        long fact = 1;
        double e = 2.0;
        int n = 2;
        double e0;
        do {
            e0 = e;
            fact *= n++;
            e += 1.0 / fact;
        } while (Math.abs(e - e0) >= EPSILON);
        System.out.printf("e = %.15f\n", e);
    }
}

```

### java_code_6.txt
```java
void setup() {
  double e = 0;
  long factorial = 1;
  int iterations = 11;
  for (int i = 0; i < iterations; i++) {
    e += (double) (2 * i + 1) / factorial;
    factorial *= (2 * i + 1) * (2 * i + 2);
  }
  println("After " + iterations + " iterations");
  println("Computed value: " + e);
  println("Real value: " + Math.E);
  println("Error: " + (e - Math.E));
  
  iterations = 21;
  for (int i = 11; i < iterations; i++) {
    e += (double) (2 * i + 1) / factorial;
    factorial *= (2 * i + 1) * (2 * i + 2);
  }
  println("After " + iterations + " iterations");
  println("Computed value: " + e);
  println("Real value: " + Math.E);
  println("Error: " + (e - Math.E));
}

```

## Python Code
### python_code_1.txt
```python
import math
#Implementation of Brother's formula
e0 = 0
e = 2
n = 0
fact = 1
while(e-e0 > 1e-15):
	e0 = e
	n += 1
	fact *= 2*n*(2*n+1)
	e += (2.*n+2)/fact

print "Computed e = "+str(e)
print "Real e = "+str(math.e)
print "Error = "+str(math.e-e)
print "Number of iterations = "+str(n)

```

### python_code_2.txt
```python
e = rfct = 10 ** 1000
n = 1
while rfct:
    n += 1
    e += rfct
    rfct //= n
print(f"{e}\n...in {n} steps")

```

### python_code_3.txt
```python
'''Calculating an approximate value for e'''

from itertools import (accumulate, chain)
from functools import (reduce)
from operator import (mul)


# eApprox :: () -> Float
def eApprox():
    '''Approximation to the value of e.'''
    return reduce(
        lambda a, x: a + 1 / x,
        scanl(mul)(1)(
            range(1, 18)
        ),
        0
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''

    print(
        eApprox()
    )


# GENERIC ABSTRACTIONS ------------------------------------

# scanl is like reduce, but returns a succession of
# intermediate values, building from the left.
# See, for example, under `scan` in the Lists chapter of
# the language-independent Bird & Wadler 1988.

# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.'''
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
'''Approximation of E'''

from functools import reduce


# eApprox :: Int -> Float
def eApprox(n):
    '''Approximation of E obtained after N iterations.
    '''
    def go(efl, x):
        e, fl = efl
        flx = fl * x
        return e + 1 / flx, flx

    return reduce(
        go,
        range(1, 1 + n),
        (1, 1)
    )[0]


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Approximation of E obtained after 20 iterations.'''

    print(eApprox(20))


# MAIN ---
if __name__ == '__main__':
    main()

```

