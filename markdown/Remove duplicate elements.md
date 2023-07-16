# Remove duplicate elements

## Task Link
[Rosetta Code - Remove duplicate elements](https://rosettacode.org/wiki/Remove_duplicate_elements)

## Java Code
### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

```

### java_code_3.txt
```java
int[] removeDuplicates(int[] values) {
    /* use a LinkedHashSet to preserve order */
    Set<Integer> set = new LinkedHashSet<>();
    for (int value : values)
        set.add(value);
    values = new int[set.size()];
    Iterator<Integer> iterator = set.iterator();
    int index = 0;
    while (iterator.hasNext())
        values[index++] = iterator.next();
    return values;
}

```

### java_code_4.txt
```java
int[] removeDuplicates(int[] values) {
    List<Integer> list = new ArrayList<>();
    for (int value : values)
        if (!list.contains(value)) list.add(value);
    values = new int[list.size()];
    int index = 0;
    for (int value : list)
        values[index++] = value;
    return values;
}

```

### java_code_5.txt
```java
import java.util.*;

class Test {

    public static void main(String[] args) {

        Object[] data = {1, 1, 2, 2, 3, 3, 3, "a", "a", "b", "b", "c", "d"};
        Set<Object> uniqueSet = new HashSet<Object>(Arrays.asList(data));
        for (Object o : uniqueSet)
            System.out.printf("%s ", o);
    }
}

```

### java_code_6.txt
```java
import java.util.*;

class Test {

    public static void main(String[] args) {

        Object[] data = {1, 1, 2, 2, 3, 3, 3, "a", "a", "b", "b", "c", "d"};
        Arrays.stream(data).distinct().forEach((o) -> System.out.printf("%s ", o));
    }
}

```

## Python Code
### python_code_1.txt
```python
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique = list(set(items))

```

### python_code_2.txt
```python
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique = []
helperset = set()
for x in items:
    if x not in helperset:
        unique.append(x)
        helperset.add(x)

```

### python_code_3.txt
```python
import itertools
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique = [k for k,g in itertools.groupby(sorted(items))]

```

### python_code_4.txt
```python
items = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']
unique = []
for x in items:
    if x not in unique:
        unique.append(x)

```

### python_code_5.txt
```python
from collections import OrderedDict as od

print(list(od.fromkeys([1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']).keys()))

```

### python_code_6.txt
```python
from itertools import (groupby)


# nubByKey :: (a -> b) -> [a] -> [a]
def nubByKey(k, xs):
    return list(list(v)[0] for _, v in groupby(sorted(xs, key=k), key=k))


xs = [
    'apple', 'apple',
    'ampersand', 'aPPLE', 'Apple',
    'orange', 'ORANGE', 'Orange', 'orange', 'apple'
]
for k in [
    id,                      # default case sensitive uniqueness
    lambda x: x.lower(),     # case-insensitive uniqueness
    lambda x: x[0],          # unique first character (case-sensitive)
    lambda x: x[0].lower(),  # unique first character (case-insensitive)
]:
    print (
        nubByKey(k, xs)
    )

```

### python_code_7.txt
```python
# nubByEq :: (a -> a -> Bool) -> [a] -> [a]
def nubByEq(eq, xs):
    def go(yys, xxs):
        if yys:
            y = yys[0]
            ys = yys[1:]
            return go(ys, xxs) if (
                elemBy(eq, y, xxs)
            ) else (
                [y] + go(ys, [y] + xxs)
            )
        else:
            return []
    return go(xs, [])


# elemBy :: (a -> a -> Bool) -> a -> [a] -> Bool
def elemBy(eq, x, xs):
    if xs:
        return eq(x, xs[0]) or elemBy(eq, x, xs[1:])
    else:
        return False


xs = [
    'apple', 'apple',
    'ampersand', 'aPPLE', 'Apple',
    'orange', 'ORANGE', 'Orange', 'orange', 'apple'
]
for eq in [
    lambda a, b: a == b,                   # default case sensitive uniqueness
    lambda a, b: a.lower() == b.lower(),   # case-insensitive uniqueness
    lambda a, b: a[0] == b[0],             # unique first char (case-sensitive)
    lambda a, b: a[0].lower() == b[0].lower(),   # unique first char (any case)
]:
    print (
        nubByEq(eq, xs)
    )

```

### python_code_8.txt
```python
# nubBy :: (a -> a -> Bool) -> [a] -> [a]
def nubBy(p, xs):
    def go(xs):
        if xs:
            x = xs[0]
            return [x] + go(
                list(filter(
                    lambda y: not p(x, y),
                    xs[1:]
                ))
            )
        else:
            return []
    return go(xs)

```

