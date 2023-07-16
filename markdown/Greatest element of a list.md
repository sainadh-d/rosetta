# Greatest element of a list

## Task Link
[Rosetta Code - Greatest element of a list](https://rosettacode.org/wiki/Greatest_element_of_a_list)

## Java Code
### java_code_1.txt
```java
int max(int[] values) {
    int max = values[0];
    for (int value : values)
        if (max < value) max = value;
    return max;
}

```

### java_code_2.txt
```java
public static float max(float[] values) throws NoSuchElementException {
    if (values.length == 0)
        throw new NoSuchElementException();
    float themax = values[0];
    for (int idx = 1; idx < values.length; ++idx) {
        if (values[idx] > themax)
            themax = values[idx];
    }
    return themax;
}

```

### java_code_3.txt
```java
public static float max(float[] values) throws NoSuchElementException {
    if (values.length == 0)
        throw new NoSuchElementException();
    Arrays.sort(values);//sorts the values in ascending order
    return values[values.length-1];
}

```

### java_code_4.txt
```java
import java.util.List;
import java.util.Collections;
import java.util.Arrays;

public static <T extends Comparable<? super T>> T max(List<T> values) {
    return Collections.max(values);
}

public static <T extends Comparable<? super T>> T max(T[] values) {
    return Collections.max(Arrays.asList(values));
}

```

## Python Code
### python_code_1.txt
```python
max(values)

```

### python_code_2.txt
```python
>>> floatstrings = ['1\n', ' 2.3\n', '4.5e-1\n', '0.01e4\n', '-1.2']
>>> max(floatstrings, key = float)
'0.01e4\n'
>>>

```

### python_code_3.txt
```python
>>> max(float(x) for x in floatstrings)
100.0
>>>

```

### python_code_4.txt
```python
>>> mylist = [47, 11, 42, 102, 13]
>>> reduce(lambda a,b: a if (a > b) else b, mylist)
102

```

### python_code_5.txt
```python
max(list(map(int,input("").split(","))))

```

### python_code_6.txt
```python
'''Non-numeric maxima'''

print(
    f'max a-z: "{max(["epsilon", "zeta", "eta", "theta"])}"'
)
print(
    f'max length: "{max(["epsilon", "zeta", "eta", "theta"], key=len)}"'
)
print(
    'max property k by a-z: ' + str(max([
        {"k": "epsilon", "v": 2},
        {"k": "zeta", "v": 4},
        {"k": "eta", "v": 32},
        {"k": "theta", "v": 16}], key=lambda x: x["k"]))
)
print(
    'max property k by length: ' + str(max([
        {"k": "epsilon", "v": 2},
        {"k": "zeta", "v": 4},
        {"k": "eta", "v": 32},
        {"k": "theta", "v": 16}], key=lambda x: len(x["k"])))
)
print(
    'max property v: ' + str(max([
        {"k": "epsilon", "v": 2},
        {"k": "zeta", "v": 4},
        {"k": "eta", "v": 32},
        {"k": "theta", "v": 16}], key=lambda x: x["v"]))
)

```

### python_code_7.txt
```python
def (best f seq)
  if seq
    ret winner car.seq
      each elem cdr.seq
        if (f elem winner)
          winner <- elem

def (max ... args)
  (best (>) args)

```

