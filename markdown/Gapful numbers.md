# Gapful numbers

## Task Link
[Rosetta Code - Gapful numbers](https://rosettacode.org/wiki/Gapful_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.List;

public class GapfulNumbers {
    private static String commatize(long n) {
        StringBuilder sb = new StringBuilder(Long.toString(n));
        int le = sb.length();
        for (int i = le - 3; i >= 1; i -= 3) {
            sb.insert(i, ',');
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        List<Long> starts = List.of((long) 1e2, (long) 1e6, (long) 1e7, (long) 1e9, (long) 7123);
        List<Integer> counts = List.of(30, 15, 15, 10, 25);
        for (int i = 0; i < starts.size(); ++i) {
            int count = 0;
            Long j = starts.get(i);
            long pow = 100;
            while (j >= pow * 10) {
                pow *= 10;
            }
            System.out.printf("First %d gapful numbers starting at %s:\n", counts.get(i), commatize(starts.get(i)));
            while (count < counts.get(i)) {
                long fl = (j / pow) * 10 + (j % 10);
                if (j % fl == 0) {
                    System.out.printf("%d ", j);
                    count++;
                }
                j++;
                if (j >= 10 * pow) {
                    pow *= 10;
                }
            }
            System.out.println('\n');
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice, count
for start, n in [(100, 30), (1_000_000, 15), (1_000_000_000, 10)]:
    print(f"\nFirst {n} gapful numbers from {start:_}")
    print(list(islice(( x for x in count(start) 
                        if (x % (int(str(x)[0]) * 10 + (x % 10)) == 0) )
                      , n)))

```

