# Compare a list of strings

## Task Link
[Rosetta Code - Compare a list of strings](https://rosettacode.org/wiki/Compare_a_list_of_strings)

## Java Code
### java_code_1.txt
```java
boolean allEqual(String[] strings) {
    String stringA = strings[0];
    for (String string : strings) {
        if (!string.equals(stringA))
            return false;
    }
    return true;
}

```

### java_code_2.txt
```java
boolean isAscending(String[] strings) {
    String previous = strings[0];
    int index = 0;
    for (String string : strings) {
        if (index++ == 0)
            continue;
        if (string.compareTo(previous) < 0)
            return false;
        previous = string;
    }
    return true;
}

```

### java_code_3.txt
```java
import java.util.Arrays;

public class CompareListOfStrings {

    public static void main(String[] args) {
        String[][] arr = {{"AA", "AA", "AA", "AA"}, {"AA", "ACB", "BB", "CC"}};
        for (String[] a : arr) {
            System.out.println(Arrays.toString(a));
            System.out.println(Arrays.stream(a).distinct().count() < 2);
            System.out.println(Arrays.equals(Arrays.stream(a).distinct().sorted().toArray(), a));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
all(a == nexta for a, nexta in zip(strings, strings[1:])) # All equal
all(a < nexta for a, nexta in zip(strings, strings[1:])) # Strictly ascending

len(set(strings)) == 1  # Concise all equal
sorted(strings, reverse=True) == strings  # Concise (but not particularly efficient) ascending

```

### python_code_2.txt
```python
from operator import (eq, lt)


xs = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta",
      "eta", "theta", "iota", "kappa", "lambda", "mu"]

ys = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta",
      "eta", "theta", "iota", "kappa", "lambda", "mu"]

az = sorted(xs)

print (
    all(map(eq, xs, ys)),

    all(map(lt, xs, xs[1:])),

    all(map(lt, az, az[1:]))
)

```

