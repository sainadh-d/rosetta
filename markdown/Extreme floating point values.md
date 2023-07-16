# Extreme floating point values

## Task Link
[Rosetta Code - Extreme floating point values](https://rosettacode.org/wiki/Extreme_floating_point_values)

## Java Code
### java_code_1.txt
```java
public class Extreme {
    public static void main(String[] args) {
        double negInf = -1.0 / 0.0; //also Double.NEGATIVE_INFINITY
        double inf = 1.0 / 0.0; //also Double.POSITIVE_INFINITY
        double nan = 0.0 / 0.0; //also Double.NaN
        double negZero = -2.0 / inf;

        System.out.println("Negative inf: " + negInf);
        System.out.println("Positive inf: " + inf);
        System.out.println("NaN: " + nan);
        System.out.println("Negative 0: " + negZero);
        System.out.println("inf + -inf: " + (inf + negInf));
        System.out.println("0 * NaN: " + (0 * nan));
        System.out.println("NaN == NaN: " + (nan == nan));
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> # Extreme values from expressions
>>> inf = 1e234 * 1e234
>>> _inf = 1e234 * -1e234
>>> _zero = 1 / _inf
>>> nan = inf + _inf
>>> inf, _inf, _zero, nan
(inf, -inf, -0.0, nan)
>>> # Print
>>> for value in (inf, _inf, _zero, nan): print (value)

inf
-inf
-0.0
nan
>>> # Extreme values from other means
>>> float('nan')
nan
>>> float('inf')
inf
>>> float('-inf')
-inf
>>> -0.
-0.0
>>> # Some arithmetic
>>> nan == nan
False
>>> nan is nan
True
>>> 0. == -0.
True
>>> 0. is -0.
False
>>> inf + _inf
nan
>>> 0.0 * nan
nan
>>> nan * 0.0
nan
>>> 0.0 * inf
nan
>>> inf * 0.0
nan

```

### python_code_2.txt
```python
>>> # But note!
>>> 1 / -0.0

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    1 / -0.0
ZeroDivisionError: float division by zero
>>> # (Not minus infinity)

```

