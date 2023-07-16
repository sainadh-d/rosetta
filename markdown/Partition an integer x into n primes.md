# Partition an integer x into n primes

## Task Link
[Rosetta Code - Partition an integer x into n primes](https://rosettacode.org/wiki/Partition_an_integer_x_into_n_primes)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.stream.IntStream;

public class PartitionInteger {
    private static final int[] primes = IntStream.concat(IntStream.of(2), IntStream.iterate(3, n -> n + 2))
        .filter(PartitionInteger::isPrime)
        .limit(50_000)
        .toArray();

    private static boolean isPrime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        if (n % 3 == 0) return n == 3;
        int d = 5;
        while (d * d <= n) {
            if (n % d == 0) return false;
            d += 2;
            if (n % d == 0) return false;
            d += 4;
        }
        return true;
    }

    private static boolean findCombo(int k, int x, int m, int n, int[] combo) {
        boolean foundCombo = false;
        if (k >= m) {
            if (Arrays.stream(combo).map(i -> primes[i]).sum() == x) {
                String s = m > 1 ? "s" : "";
                System.out.printf("Partitioned %5d with %2d prime%s: ", x, m, s);
                for (int i = 0; i < m; ++i) {
                    System.out.print(primes[combo[i]]);
                    if (i < m - 1) System.out.print('+');
                    else System.out.println();
                }
                foundCombo = true;
            }
        } else {
            for (int j = 0; j < n; ++j) {
                if (k == 0 || j > combo[k - 1]) {
                    combo[k] = j;
                    if (!foundCombo) {
                        foundCombo = findCombo(k + 1, x, m, n, combo);
                    }
                }
            }
        }
        return foundCombo;
    }

    private static void partition(int x, int m) {
        if (x < 2 || m < 1 || m >= x) {
            throw new IllegalArgumentException();
        }
        int[] filteredPrimes = Arrays.stream(primes).filter(it -> it <= x).toArray();
        int n = filteredPrimes.length;
        if (n < m) throw new IllegalArgumentException("Not enough primes");
        int[] combo = new int[m];
        boolean foundCombo = findCombo(0, x, m, n, combo);
        if (!foundCombo) {
            String s = m > 1 ? "s" : " ";
            System.out.printf("Partitioned %5d with %2d prime%s: (not possible)\n", x, m, s);
        }
    }

    public static void main(String[] args) {
        partition(99809, 1);
        partition(18, 2);
        partition(19, 3);
        partition(20, 4);
        partition(2017, 24);
        partition(22699, 1);
        partition(22699, 2);
        partition(22699, 3);
        partition(22699, 4);
        partition(40355, 3);
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations as cmb


def isP(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % x > 0 for x in range(3, int(n ** 0.5) + 1, 2))


def genP(n):
    p = [2]
    p.extend([x for x in range(3, n + 1, 2) if isP(x)])
    return p


data = [
    (99809, 1), (18, 2), (19, 3), (20, 4), (2017, 24),
    (22699, 1), (22699, 2), (22699, 3), (22699, 4), (40355, 3)]


for n, cnt in data:
    ci = iter(cmb(genP(n), cnt))
    while True:
        try:
            c = next(ci)
            if sum(c) == n:
                print(' '.join(
                    [repr((n, cnt)), "->", '+'.join(str(s) for s in c)]
                ))
                break
        except StopIteration:
            print(repr((n, cnt)) + " -> Not possible")
            break

```

