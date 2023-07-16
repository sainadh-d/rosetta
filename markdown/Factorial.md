# Factorial

## Task Link
[Rosetta Code - Factorial](https://rosettacode.org/wiki/Factorial)

## Java Code
### java_code_2.txt
```java
package programas;

import java.math.BigInteger;
import java.util.InputMismatchException;
import java.util.Scanner;

public class IterativeFactorial {

  public BigInteger factorial(BigInteger n) {
    if ( n == null ) {
      throw new IllegalArgumentException();
    }
    else if ( n.signum() == - 1 ) {
      // negative
      throw new IllegalArgumentException("Argument must be a non-negative integer");
    }
    else {
      BigInteger factorial = BigInteger.ONE;
      for ( BigInteger i = BigInteger.ONE; i.compareTo(n) < 1; i = i.add(BigInteger.ONE) ) {
        factorial = factorial.multiply(i);
      }
      return factorial;
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    BigInteger number, result;
    boolean error = false;
    System.out.println("FACTORIAL OF A NUMBER");
    do {
      System.out.println("Enter a number:");
      try {
        number = scanner.nextBigInteger();
        result = new IterativeFactorial().factorial(number);
        error = false;
        System.out.println("Factorial of " + number + ": " + result);
      }
      catch ( InputMismatchException e ) {
        error = true;
        scanner.nextLine();
      }

      catch ( IllegalArgumentException e ) {
        error = true;
        scanner.nextLine();
      }
    }
    while ( error );
    scanner.close();
  }

}

```

### java_code_3.txt
```java
package programas;

import java.math.BigInteger;
import java.util.InputMismatchException;
import java.util.Scanner;

public class RecursiveFactorial {

  public BigInteger factorial(BigInteger n) {
    if ( n == null ) {
      throw new IllegalArgumentException();
    }

    else if ( n.equals(BigInteger.ZERO) ) {
      return BigInteger.ONE;
    }
    else if ( n.signum() == - 1 ) {
      // negative
      throw new IllegalArgumentException("Argument must be a non-negative integer");
    }
    else {
      return n.equals(BigInteger.ONE)
          ? BigInteger.ONE
          : factorial(n.subtract(BigInteger.ONE)).multiply(n);
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    BigInteger number, result;
    boolean error = false;
    System.out.println("FACTORIAL OF A NUMBER");
    do {
      System.out.println("Enter a number:");
      try {
        number = scanner.nextBigInteger();
        result = new RecursiveFactorial().factorial(number);
        error = false;
        System.out.println("Factorial of " + number + ": " + result);
      }
      catch ( InputMismatchException e ) {
        error = true;
        scanner.nextLine();
      }

      catch ( IllegalArgumentException e ) {
        error = true;
        scanner.nextLine();
      }
    }
    while ( error );
    scanner.close();

  }

}

```

## Python Code
### python_code_1.txt
```python
import math
math.factorial(n)

```

### python_code_10.txt
```python
def (fact n)
  if (n = 0)
    1
    (n * (fact n-1))

```

### python_code_11.txt
```python
def (fact n)
  (n * (fact n-1))

def (fact 0)
  1

```

### python_code_12.txt
```python
def (fact n)
  ret result 1
    for i 1 (i <= n) ++i
      result <- result*i

```

### python_code_13.txt
```python
# a useful helper to generate all the natural numbers until n
def (nums n)
  collect+for i 1 (i <= n) ++i
    yield i

def (fact n)
  (reduce (*) nums.n 1)

```

### python_code_2.txt
```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

```

### python_code_3.txt
```python
from operator import mul
from functools import reduce

def factorial(n):
    return reduce(mul, range(1,n+1), 1)

```

### python_code_4.txt
```python
from itertools import (accumulate, chain)
from operator import mul

# factorial :: Integer
def factorial(n):
    return list(
        accumulate(chain([1], range(1, 1 + n)), mul)
    )[-1]

```

### python_code_5.txt
```python
from itertools import (accumulate, chain)
from operator import mul


# factorials :: [Integer]
def factorials(n):
    return list(
        accumulate(chain([1], range(1, 1 + n)), mul)
    )

print(factorials(5))

# -> [1, 1, 2, 6, 24, 120]

```

### python_code_6.txt
```python
from numpy import prod

def factorial(n):
    return prod(range(1, n + 1), dtype=int)

```

### python_code_7.txt
```python
def factorial(n):
    z=1
    if n>1:
        z=n*factorial(n-1)
    return z

```

### python_code_8.txt
```python
def factorial(n):
    return n * factorial(n - 1) if n else 1

```

### python_code_9.txt
```python
from cmath import *

# Coefficients used by the GNU Scientific Library
g = 7
p = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
     771.32342877765313, -176.61502916214059, 12.507343278686905,
     -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7]

def gamma(z):
  z = complex(z)
  # Reflection formula
  if z.real < 0.5:
    return pi / (sin(pi*z)*gamma(1-z))
  else:
    z -= 1
    x = p[0]
    for i in range(1, g+2):
      x += p[i]/(z+i)
    t = z + g + 0.5
    return sqrt(2*pi) * t**(z+0.5) * exp(-t) * x

def factorial(n):
  return gamma(n+1)

print "factorial(-0.5)**2=",factorial(-0.5)**2
for i in range(10):
  print "factorial(%d)=%s"%(i,factorial(i))

```

