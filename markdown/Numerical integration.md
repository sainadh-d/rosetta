# Numerical integration

## Task Link
[Rosetta Code - Numerical integration](https://rosettacode.org/wiki/Numerical_integration)

## Java Code
### java_code_1.txt
```java
class NumericalIntegration
{

  interface FPFunction
  {
    double eval(double n);
  }
  
  public static double rectangularLeft(double a, double b, int n, FPFunction f)
  {
    return rectangular(a, b, n, f, 0);
  }
  
  public static double rectangularMidpoint(double a, double b, int n, FPFunction f)
  {
    return rectangular(a, b, n, f, 1);
  }
  
  public static double rectangularRight(double a, double b, int n, FPFunction f)
  {
    return rectangular(a, b, n, f, 2);
  }
  
  public static double trapezium(double a, double b, int n, FPFunction f)
  {
    double range = checkParamsGetRange(a, b, n);
    double nFloat = (double)n;
    double sum = 0.0;
    for (int i = 1; i < n; i++)
    {
      double x = a + range * (double)i / nFloat;
      sum += f.eval(x);
    }
    sum += (f.eval(a) + f.eval(b)) / 2.0;
    return sum * range / nFloat;
  }
  
  public static double simpsons(double a, double b, int n, FPFunction f)
  {
    double range = checkParamsGetRange(a, b, n);
    double nFloat = (double)n;
    double sum1 = f.eval(a + range / (nFloat * 2.0));
    double sum2 = 0.0;
    for (int i = 1; i < n; i++)
    {
      double x1 = a + range * ((double)i + 0.5) / nFloat;
      sum1 += f.eval(x1);
      double x2 = a + range * (double)i / nFloat;
      sum2 += f.eval(x2);
    }
    return (f.eval(a) + f.eval(b) + sum1 * 4.0 + sum2 * 2.0) * range / (nFloat * 6.0);
  }
  
  private static double rectangular(double a, double b, int n, FPFunction f, int mode)
  {
    double range = checkParamsGetRange(a, b, n);
    double modeOffset = (double)mode / 2.0;
    double nFloat = (double)n;
    double sum = 0.0;
    for (int i = 0; i < n; i++)
    {
      double x = a + range * ((double)i + modeOffset) / nFloat;
      sum += f.eval(x);
    }
    return sum * range / nFloat;
  }
  
  private static double checkParamsGetRange(double a, double b, int n)
  {
    if (n <= 0)
      throw new IllegalArgumentException("Invalid value of n");
    double range = b - a;
    if (range <= 0)
      throw new IllegalArgumentException("Invalid range");
    return range;
  }
  
  
  private static void testFunction(String fname, double a, double b, int n, FPFunction f)
  {
    System.out.println("Testing function \"" + fname + "\", a=" + a + ", b=" + b + ", n=" + n);
    System.out.println("rectangularLeft: " + rectangularLeft(a, b, n, f));
    System.out.println("rectangularMidpoint: " + rectangularMidpoint(a, b, n, f));
    System.out.println("rectangularRight: " + rectangularRight(a, b, n, f));
    System.out.println("trapezium: " + trapezium(a, b, n, f));
    System.out.println("simpsons: " + simpsons(a, b, n, f));
    System.out.println();
    return;
  }
  
  public static void main(String[] args)
  {
    testFunction("x^3", 0.0, 1.0, 100, new FPFunction() {
        public double eval(double n) {
          return n * n * n;
        }
      }
    );
    
    testFunction("1/x", 1.0, 100.0, 1000, new FPFunction() {
        public double eval(double n) {
          return 1.0 / n;
        }
      }
    );
    
    testFunction("x", 0.0, 5000.0, 5000000, new FPFunction() {
        public double eval(double n) {
          return n;
        }
      }
    );
    
    testFunction("x", 0.0, 6000.0, 6000000, new FPFunction() {
        public double eval(double n) {
          return n;
        }
      }
    );
    
    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction

def left_rect(f,x,h):
  return f(x)
 
def mid_rect(f,x,h):
  return f(x + h/2)
 
def right_rect(f,x,h):
  return f(x+h)
 
def trapezium(f,x,h):
  return (f(x) + f(x+h))/2.0
 
def simpson(f,x,h):
  return (f(x) + 4*f(x + h/2) + f(x+h))/6.0
 
def cube(x):
  return x*x*x
 
def reciprocal(x):
  return 1/x
 
def identity(x):
  return x
 
def integrate( f, a, b, steps, meth):
   h = (b-a)/steps
   ival = h * sum(meth(f, a+i*h, h) for i in range(steps))
   return ival  

# Tests
for a, b, steps, func in ((0., 1., 100, cube), (1., 100., 1000, reciprocal)):
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               integrate( func, a, b, steps, rule)))
    a, b = Fraction.from_float(a), Fraction.from_float(b)
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps and fractions) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               float(integrate( func, a, b, steps, rule))))

# Extra tests (compute intensive)
for a, b, steps, func in ((0., 5000., 5000000, identity),
                          (0., 6000., 6000000, identity)):
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               integrate( func, a, b, steps, rule)))
    a, b = Fraction.from_float(a), Fraction.from_float(b)
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps and fractions) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               float(integrate( func, a, b, steps, rule))))

```

### python_code_2.txt
```python
for a, b, steps, func in ((0., 1., 100, cube), (1., 100., 1000, reciprocal)):
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               integrate( func, a, b, steps, rule)))
    a, b = Fraction.from_float(a), Fraction.from_float(b)
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps and fractions) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               float(integrate( func, a, b, steps, rule))))

# Extra tests (compute intensive)
for a, b, steps, func in ((1., 5000., 5000000, identity),
                          (1., 6000., 6000000, identity)):
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               integrate( func, a, b, steps, rule)))
    a, b = Fraction.from_float(a), Fraction.from_float(b)
    for rule in (left_rect, mid_rect, right_rect, trapezium, simpson):
        print('%s integrated using %s\n  from %r to %r (%i steps and fractions) = %r' %
              (func.__name__, rule.__name__, a, b, steps,
               float(integrate( func, a, b, steps, rule))))

```

### python_code_3.txt
```python
def faster_simpson(f, a, b, steps):
   h = (b-a)/float(steps)
   a1 = a+h/2
   s1 = sum( f(a1+i*h) for i in range(0,steps))
   s2 = sum( f(a+i*h) for i in range(1,steps))
   return (h/6.0)*(f(a)+f(b)+4.0*s1+2.0*s2)

```

