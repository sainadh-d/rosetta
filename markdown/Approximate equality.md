# Approximate equality

## Task Link
[Rosetta Code - Approximate equality](https://rosettacode.org/wiki/Approximate_equality)

## Java Code
### java_code_1.txt
```java
public class Approximate {
    private static boolean approxEquals(double value, double other, double epsilon) {
        return Math.abs(value - other) < epsilon;
    }

    private static void test(double a, double b) {
        double epsilon = 1e-18;
        System.out.printf("%f, %f => %s\n", a, b, approxEquals(a, b, epsilon));
    }

    public static void main(String[] args) {
        test(100000000000000.01, 100000000000000.011);
        test(100.01, 100.011);
        test(10000000000000.001 / 10000.0, 1000000000.0000001000);
        test(0.001, 0.0010000001);
        test(0.000000000000000000000101, 0.0);
        test(Math.sqrt(2.0) * Math.sqrt(2.0), 2.0);
        test(-Math.sqrt(2.0) * Math.sqrt(2.0), -2.0);
        test(3.14159265358979323846, 3.14159265358979324);
    }
}

```

## Python Code
### python_code_1.txt
```python
from numpy import sqrt
from math import isclose

testvalues = [[100000000000000.01,           100000000000000.011],
              [100.01,                       100.011],
              [10000000000000.001 / 10000.0, 1000000000.0000001000],
              [0.001,                        0.0010000001],
              [0.000000000000000000000101,   0.0],
              [sqrt(2) * sqrt(2),            2.0],
              [-sqrt(2) * sqrt(2),          -2.0],
              [3.14159265358979323846,       3.14159265358979324]]

for (x, y) in testvalues:
    maybenot = "is" if isclose(x, y) else "is NOT"
    print(x, maybenot, "approximately equal to ", y)

```

