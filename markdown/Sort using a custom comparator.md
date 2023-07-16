# Sort using a custom comparator

## Task Link
[Rosetta Code - Sort using a custom comparator](https://rosettacode.org/wiki/Sort_using_a_custom_comparator)

## Java Code
### java_code_1.txt
```java
import java.util.Comparator;
import java.util.Arrays;

public class Test {
  public static void main(String[] args) {
    String[] strings = {"Here", "are", "some", "sample", "strings", "to", "be", "sorted"};

    Arrays.sort(strings, new Comparator<String>() {
      public int compare(String s1, String s2) {
        int c = s2.length() - s1.length();
        if (c == 0)
          c = s1.compareToIgnoreCase(s2);
        return c;
      }
    });

    for (String s: strings)
      System.out.print(s + " ");
  }
}

```

### java_code_2.txt
```java
import java.util.Comparator;
import java.util.Arrays;

public class ComparatorTest {
  public static void main(String[] args) {
    String[] strings = {"Here", "are", "some", "sample", "strings", "to", "be", "sorted"};

    Arrays.sort(strings, (s1, s2) -> {
      int c = s2.length() - s1.length();
      if (c == 0)
        c = s1.compareToIgnoreCase(s2);
      return c;
    });

    for (String s: strings)
      System.out.print(s + " ");
  }
}

```

## Python Code
### python_code_1.txt
```python
strings = "here are Some sample strings to be sorted".split()

def mykey(x):
    return -len(x), x.upper()

print sorted(strings, key=mykey)

```

### python_code_2.txt
```python
['strings', 'sample', 'sorted', 'here', 'Some', 'are', 'be', 'to']

```

### python_code_3.txt
```python
def mycmp(s1, s2):
    return cmp(len(s2), len(s1)) or cmp(s1.upper(), s2.upper())

print sorted(strings, cmp=mycmp)

```

