# Generic swap

## Task Link
[Rosetta Code - Generic swap](https://rosettacode.org/wiki/Generic_swap)

## Java Code
### java_code_1.txt
```java
class Pair<T> {
    T first;
    T second;
}
public static <T> void swap(Pair<T> p) {
   T temp = p.first;
   p.first = p.second;
   p.second = temp;
}

```

## Python Code
### python_code_1.txt
```python
a, b = b, a

```

### python_code_2.txt
```python
def swap(a, b):
    return b, a

```

