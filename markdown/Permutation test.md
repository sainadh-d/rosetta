# Permutation test

## Task Link
[Rosetta Code - Permutation test](https://rosettacode.org/wiki/Permutation_test)

## Java Code
### java_code_1.txt
```java
public class PermutationTest {
    private static final int[] data = new int[]{
        85, 88, 75, 66, 25, 29, 83, 39, 97,
        68, 41, 10, 49, 16, 65, 32, 92, 28, 98
    };

    private static int pick(int at, int remain, int accu, int treat) {
        if (remain == 0) return (accu > treat) ? 1 : 0;
        return pick(at - 1, remain - 1, accu + data[at - 1], treat)
            + ((at > remain) ? pick(at - 1, remain, accu, treat) : 0);
    }

    public static void main(String[] args) {
        int treat = 0;
        double total = 1.0;
        for (int i = 0; i <= 8; ++i) {
            treat += data[i];
        }
        for (int i = 19; i >= 11; --i) {
            total *= i;
        }
        for (int i = 9; i >= 1; --i) {
            total /= i;
        }
        int gt = pick(19, 9, 0, treat);
        int le = (int) (total - gt);
        System.out.printf("<= : %f%%  %d\n", 100.0 * le / total, le);
        System.out.printf(" > : %f%%  %d\n", 100.0 * gt / total, gt);
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations as comb

def statistic(ab, a):
    sumab, suma = sum(ab), sum(a)
    return ( suma / len(a) -
             (sumab -suma) / (len(ab) - len(a)) )

def permutationTest(a, b):
    ab = a + b
    Tobs = statistic(ab, a)
    under = 0
    for count, perm in enumerate(comb(ab, len(a)), 1):
        if statistic(ab, perm) <= Tobs:
            under += 1
    return under * 100. / count

treatmentGroup = [85, 88, 75, 66, 25, 29, 83, 39, 97]
controlGroup   = [68, 41, 10, 49, 16, 65, 32, 92, 28, 98]
under = permutationTest(treatmentGroup, controlGroup)
print("under=%.2f%%, over=%.2f%%" % (under, 100. - under))

```

### python_code_2.txt
```python
from itertools import combinations as comb

def permutationTest(a, b):
    ab = a + b
    Tobs = sum(a)
    under = 0
    for count, perm in enumerate(comb(ab, len(a)), 1):
        if sum(perm) <= Tobs:
            under += 1
    return under * 100. / count

treatmentGroup = [85, 88, 75, 66, 25, 29, 83, 39, 97]
controlGroup   = [68, 41, 10, 49, 16, 65, 32, 92, 28, 98]
under = permutationTest(treatmentGroup, controlGroup)
print("under=%.2f%%, over=%.2f%%" % (under, 100. - under))

```

