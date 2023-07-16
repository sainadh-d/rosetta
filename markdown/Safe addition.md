# Safe addition

## Task Link
[Rosetta Code - Safe addition](https://rosettacode.org/wiki/Safe_addition)

## Java Code
### java_code_1.txt
```java
public class SafeAddition {
    private static double stepDown(double d) {
        return Math.nextAfter(d, Double.NEGATIVE_INFINITY);
    }

    private static double stepUp(double d) {
        return Math.nextUp(d);
    }

    private static double[] safeAdd(double a, double b) {
        return new double[]{stepDown(a + b), stepUp(a + b)};
    }

    public static void main(String[] args) {
        double a = 1.2;
        double b = 0.03;
        double[] result = safeAdd(a, b);
        System.out.printf("(%.2f + %.2f) is in the range %.16f..%.16f", a, b, result[0], result[1]);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
0.9999999999999999
>>> from math import fsum
>>> fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
1.0

```

