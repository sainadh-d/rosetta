# Averages/Root mean square

## Task Link
[Rosetta Code - Averages/Root mean square](https://rosettacode.org/wiki/Averages/Root_mean_square)

## Java Code
### java_code_1.txt
```java
public class RootMeanSquare {

    public static double rootMeanSquare(double... nums) {
        double sum = 0.0;
        for (double num : nums)
            sum += num * num;
        return Math.sqrt(sum / nums.length);
    }

    public static void main(String[] args) {
        double[] nums = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0};
        System.out.println("The RMS of the numbers from 1 to 10 is " + rootMeanSquare(nums));
    }
}

```

## Python Code
### python_code_1.txt
```python
sqrt(mean(x²))

```

### python_code_2.txt
```python
>>> from math import sqrt
>>> def qmean(num):
	return sqrt(sum(n*n for n in num)/len(num))

>>> qmean(range(1,11))
6.2048368229954285

```

### python_code_3.txt
```python
from functools import (reduce)
from math import (sqrt)


# rootMeanSquare :: [Num] -> Float
def rootMeanSquare(xs):
    return sqrt(reduce(lambda a, x: a + x * x, xs, 0) / len(xs))


print(
    rootMeanSquare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
)

```

