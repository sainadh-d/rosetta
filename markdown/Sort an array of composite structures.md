# Sort an array of composite structures

## Task Link
[Rosetta Code - Sort an array of composite structures](https://rosettacode.org/wiki/Sort_an_array_of_composite_structures)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Comparator;

public class SortComp {
    public static class Pair {
        public String name;
        public String value;
        public Pair(String n, String v) {
            name = n;
            value = v;
        }
    }

    public static void main(String[] args) {
        Pair[] pairs = {new Pair("06-07", "Ducks"), new Pair("00-01", "Avalanche"),
            new Pair("02-03", "Devils"), new Pair("01-02", "Red Wings"),
            new Pair("03-04", "Lightning"), new Pair("04-05", "lockout"),
            new Pair("05-06", "Hurricanes"), new Pair("99-00", "Devils"),
            new Pair("07-08", "Red Wings"), new Pair("08-09", "Penguins")};

        sortByName(pairs);
        for (Pair p : pairs) {
            System.out.println(p.name + " " + p.value);
        }
    }

    public static void sortByName(Pair[] pairs) {
        Arrays.sort(pairs, new Comparator<Pair>() {
            public int compare(Pair p1, Pair p2) {
                return p1.name.compareTo(p2.name);
            }
        });
    }
}

```

### java_code_2.txt
```java
    public static void sortByName(Pair[] pairs) {
        Arrays.sort(pairs, (p1, p2) -> p1.name.compareTo(p2.name));
    }

```

### java_code_3.txt
```java
    public static void sortByName(Pair[] pairs) {
        Arrays.sort(pairs, Comparator.comparing(p -> p.name));
    }

```

## Python Code
### python_code_1.txt
```python
people = [('joe', 120), ('foo', 31), ('bar', 51)]
sorted(people)

```

### python_code_2.txt
```python
[('bar', 51), ('foo', 31), ('joe', 120)]

```

### python_code_3.txt
```python
from operator import itemgetter
people = [(120, 'joe'), (31, 'foo'), (51, 'bar')]
people.sort(key=itemgetter(1))

```

### python_code_4.txt
```python
[(51, 'bar'), (31, 'foo'), (120, 'joe')]

```

