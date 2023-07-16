# Order by pair comparisons

## Task Link
[Rosetta Code - Order by pair comparisons](https://rosettacode.org/wiki/Order_by_pair_comparisons)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class SortComp1 {
    public static void main(String[] args) {
        List<String> items = Arrays.asList("violet", "red", "green", "indigo", "blue", "yellow", "orange");
        List<String> sortedItems = new ArrayList<>();
        Comparator<String> interactiveCompare = new Comparator<String>() {
                int count = 0;
                Scanner s = new Scanner(System.in);
                public int compare(String s1, String s2) {
                    System.out.printf("(%d) Is %s <, =, or > %s. Answer -1, 0, or 1: ", ++count, s1, s2);
                    return s.nextInt();
                }
            };
        for (String item : items) {
            System.out.printf("Inserting '%s' into %s\n", item, sortedItems);
            int spotToInsert = Collections.binarySearch(sortedItems, item, interactiveCompare);
            // when item does not equal an element in sortedItems,
            // it returns bitwise complement of insertion point
            if (spotToInsert < 0) spotToInsert = ~spotToInsert;
            sortedItems.add(spotToInsert, item);
        }
        System.out.println(sortedItems);
    }
}

```

### java_code_2.txt
```java
import java.util.*;

public class OrderByPair {
    public static void main(String[] args) {
        List<String> items = Arrays.asList("violet", "red", "green", "indigo", "blue", "yellow", "orange");
        Collections.sort(items, new Comparator<String>() {
                int count = 0;
                Scanner s = new Scanner(System.in);
                public int compare(String s1, String s2) {
                    System.out.printf("(%d) Is %s <, =, or > %s. Answer -1, 0, or 1: ", ++count, s1, s2);
                    return s.nextInt();
                }
            });
        System.out.println(items);
    }
}

```

## Python Code
### python_code_1.txt
```python
def _insort_right(a, x, q):
    """
    Insert item x in list a, and keep it sorted assuming a is sorted.
    If x is already in a, insert it to the right of the rightmost x.
    """

    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo+hi)//2
        q += 1
        less = input(f"{q:2}: IS {x:>6} LESS-THAN {a[mid]:>6} ? y/n: ").strip().lower() == 'y'
        if less: hi = mid
        else: lo = mid+1
    a.insert(lo, x)
    return q

def order(items):
    ordered, q = [], 0
    for item in items:
        q = _insort_right(ordered, item, q)
    return ordered, q

if __name__ == '__main__':
    items = 'violet red green indigo blue yellow orange'.split()
    ans, questions = order(items)
    print('\n' + ' '.join(ans))

```

### python_code_2.txt
```python
from functools import cmp_to_key

def user_cmp(a, b):
    return int(input(f"IS {a:>6} <, ==, or > {b:>6}  answer -1, 0 or 1:"))

if __name__ == '__main__':
    items = 'violet red green indigo blue yellow orange'.split()
    ans = sorted(items, key=cmp_to_key(user_cmp))
    print('\n' + ' '.join(ans))

```

