# Pick random element

## Task Link
[Rosetta Code - Pick random element](https://rosettacode.org/wiki/Pick_random_element)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
...
int[] array = {1,2,3};
return array[new Random().nextInt(array.length)]; // if done multiple times, the Random object should be re-used

```

## Python Code
### python_code_1.txt
```python
>>> import random
>>> random.choice(['foo', 'bar', 'baz'])
'baz'

```

