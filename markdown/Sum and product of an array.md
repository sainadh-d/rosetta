# Sum and product of an array

## Task Link
[Rosetta Code - Sum and product of an array](https://rosettacode.org/wiki/Sum_and_product_of_an_array)

## Java Code
### java_code_1.txt
```java
public class SumProd
{
 public static void main(final String[] args)
 {
  int sum = 0;
  int prod = 1;
  int[] arg = {1,2,3,4,5};
  for (int i : arg)
  {
   sum += i;
   prod *= i;
  }
 }
}

```

### java_code_2.txt
```java
import java.util.Arrays;

public class SumProd
{
 public static void main(final String[] args)
 {
  int[] arg = {1,2,3,4,5};
  System.out.printf("sum = %d\n", Arrays.stream(arg).sum());
  System.out.printf("sum = %d\n", Arrays.stream(arg).reduce(0, (a, b) -> a + b));
  System.out.printf("product = %d\n", Arrays.stream(arg).reduce(1, (a, b) -> a * b));
 }
}

```

## Python Code
### python_code_1.txt
```python
numbers = [1, 2, 3]
total = sum(numbers)

product = 1
for i in numbers:
    product *= i

```

### python_code_2.txt
```python
from operator import mul, add
sum = reduce(add, numbers) # note: this version doesn't work with empty lists
sum = reduce(add, numbers, 0)
product = reduce(mul, numbers) # note: this version doesn't work with empty lists
product = reduce(mul, numbers, 1)

```

### python_code_3.txt
```python
from numpy import r_
numbers = r_[1:4]
total = numbers.sum()
product = numbers.prod()

```

### python_code_4.txt
```python
import math
total = math.fsum(floats)

```

