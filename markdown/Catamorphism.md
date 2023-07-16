# Catamorphism

## Task Link
[Rosetta Code - Catamorphism](https://rosettacode.org/wiki/Catamorphism)

## Java Code
### java_code_1.txt
```java
import java.util.stream.Stream;

public class ReduceTask {

    public static void main(String[] args) {
        System.out.println(Stream.of(1, 2, 3, 4, 5).mapToInt(i -> i).sum());
        System.out.println(Stream.of(1, 2, 3, 4, 5).reduce(1, (a, b) -> a * b));
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> # Python 2.X
>>> from operator import add
>>> listoflists = [['the', 'cat'], ['sat', 'on'], ['the', 'mat']]
>>> help(reduce)
Help on built-in function reduce in module __builtin__:

reduce(...)
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.

>>> reduce(add, listoflists, [])
['the', 'cat', 'sat', 'on', 'the', 'mat']
>>>

```

### python_code_2.txt
```python
# Python 3.X

from functools import reduce
from operator import add, mul

nums = range(1,11)

summation = reduce(add, nums)

product = reduce(mul, nums)

concatenation = reduce(lambda a, b: str(a) + str(b), nums)

print(summation, product, concatenation)

```

