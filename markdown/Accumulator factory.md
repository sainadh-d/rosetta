# Accumulator factory

## Task Link
[Rosetta Code - Accumulator factory](https://rosettacode.org/wiki/Accumulator_factory)

## Java Code
### java_code_1.txt
```java
public class Accumulator
    //implements java.util.function.UnaryOperator<Number> // Java 8
{
    private Number sum;

    public Accumulator(Number sum0) {
	sum = sum0;
    }

    public Number apply(Number n) {
	// Acts like sum += n, but chooses long or double.
	// Converts weird types (like BigInteger) to double.
	return (longable(sum) && longable(n)) ?
	    (sum = sum.longValue() + n.longValue()) :
	    (sum = sum.doubleValue() + n.doubleValue());
    }

    private static boolean longable(Number n) {
	return n instanceof Byte || n instanceof Short ||
	    n instanceof Integer || n instanceof Long;
    }

    public static void main(String[] args) {
	Accumulator x = new Accumulator(1);
	x.apply(5);
	new Accumulator(3);
	System.out.println(x.apply(2.3));
    }
}

```

### java_code_2.txt
```java
import java.util.function.UnaryOperator;

public class AccumulatorFactory {

    public static UnaryOperator<Number> accumulator(Number sum0) {
	// Allows sum[0] = ... inside lambda.
	Number[] sum = { sum0 };

	// Acts like n -> sum[0] += n, but chooses long or double.
	// Converts weird types (like BigInteger) to double.
	return n -> (longable(sum[0]) && longable(n)) ?
	    (sum[0] = sum[0].longValue() + n.longValue()) :
	    (sum[0] = sum[0].doubleValue() + n.doubleValue());
    }

    private static boolean longable(Number n) {
	return n instanceof Byte || n instanceof Short ||
	    n instanceof Integer || n instanceof Long;
    }

    public static void main(String[] args) {
	UnaryOperator<Number> x = accumulator(1);
	x.apply(5);
	accumulator(3);
	System.out.println(x.apply(2.3));
    }
}

```

## Python Code
### python_code_2.txt
```python
>>> def accumulator(sum):
  def f(n):
    f.sum += n
    return f.sum
  f.sum = sum
  return f

>>> x = accumulator(1)
>>> x(5)
6
>>> x(2.3)
8.3000000000000007
>>> x = accumulator(1)
>>> x(5)
6
>>> x(2.3)
8.3000000000000007
>>> x2 = accumulator(3)
>>> x2(5)
8
>>> x2(3.3)
11.300000000000001
>>> x(0)
8.3000000000000007
>>> x2(0)
11.300000000000001

```

### python_code_3.txt
```python
def accumulator(sum):
  def f(n):
    nonlocal sum
    sum += n
    return sum
  return f

x = accumulator(1)
x(5)
print(accumulator(3))
print(x(2.3))

```

### python_code_4.txt
```python
def accumulator(sum):
  while True:
    sum += yield sum

x = accumulator(1)
x.send(None)
x.send(5)
print(accumulator(3))
print(x.send(2.3))

```

### python_code_5.txt
```python
def (accumulator n)
  (fn() ++n)

```

