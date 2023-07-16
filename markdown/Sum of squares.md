# Sum of squares

## Task Link
[Rosetta Code - Sum of squares](https://rosettacode.org/wiki/Sum_of_squares)

## Java Code
### java_code_1.txt
```java
public class SumSquares
{
 public static void main(final String[] args)
 {
  double sum = 0;
  int[] nums = {1,2,3,4,5};
  for (int i : nums)
   sum += i * i;
  System.out.println("The sum of the squares is: " + sum);
 }
}

```

## Python Code
### python_code_1.txt
```python
sum([1, 2, 3, 4]²)

```

### python_code_2.txt
```python
sum(x * x for x in [1, 2, 3, 4, 5])
# or
sum(x ** 2 for x in [1, 2, 3, 4, 5])
# or
sum(pow(x, 2) for x in [1, 2, 3, 4, 5])

```

### python_code_3.txt
```python
# using lambda and map:
sum(map(lambda x: x * x, [1, 2, 3, 4, 5]))
# or 
sum(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
# or 
sum(map(lambda x: pow(x, 2), [1, 2, 3, 4, 5]))

# using pow and repeat
from itertools import repeat
sum(map(pow, [1, 2, 3, 4, 5], repeat(2)))

# using starmap and mul
from itertools import starmap
from operator import mul
a = [1, 2, 3, 4, 5]
sum(starmap(mul, zip(a, a)))

# using reduce
from functools import reduce
powers_of_two = (x * x for x in [1, 2, 3, 4, 5])
reduce(lambda x, y : x + y, powers_of_two)
# or
from operator import add
powers_of_two = (x * x for x in [1, 2, 3, 4, 5])
reduce(add, powers_of_two)
# or using a bit more complex lambda
reduce(lambda a, x: a + x*x, [1, 2, 3, 4, 5])

```

### python_code_4.txt
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
np.sum(a ** 2)

```

