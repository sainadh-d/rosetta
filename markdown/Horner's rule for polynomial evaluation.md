# Horner's rule for polynomial evaluation

## Task Link
[Rosetta Code - Horner's rule for polynomial evaluation](https://rosettacode.org/wiki/Horner%27s_rule_for_polynomial_evaluation)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Horner {
    public static void main(String[] args){
        List<Double> coeffs = new ArrayList<Double>();
        coeffs.add(-19.0);
        coeffs.add(7.0);
        coeffs.add(-4.0);
        coeffs.add(6.0);
        System.out.println(polyEval(coeffs, 3));
    }

    public static double polyEval(List<Double> coefficients, double x) {
        Collections.reverse(coefficients);
        Double accumulator = coefficients.get(0);
        for (int i = 1; i < coefficients.size(); i++) {
            accumulator = (accumulator * x) + (Double) coefficients.get(i);
        }
        return accumulator;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def horner(coeffs, x):
	acc = 0
	for c in reversed(coeffs):
		acc = acc * x + c
	return acc

>>> horner( (-19, 7, -4, 6), 3)
128

```

### python_code_2.txt
```python
>>> try: from functools import reduce
except: pass

>>> def horner(coeffs, x):
	return reduce(lambda acc, c: acc * x + c, reversed(coeffs), 0)

>>> horner( (-19, 7, -4, 6), 3)
128

```

### python_code_3.txt
```python
>>> import numpy
>>> numpy.polynomial.polynomial.polyval(3, (-19, 7, -4, 6))
128.0

```

