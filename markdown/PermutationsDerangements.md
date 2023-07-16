# Permutations/Derangements

## Task Link
[Rosetta Code - Permutations/Derangements](https://rosettacode.org/wiki/Permutations/Derangements)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Derangement {

    public static void main(String[] args) {
        System.out.println("derangements for n = 4\n");
        for (Object d  : (ArrayList)(derangements(4, false)[0])) {
            System.out.println(Arrays.toString((int[])d));
        }
        
        System.out.println("\ntable of n vs counted vs calculated derangements\n");
        for (int i = 0; i < 10; i++) {
            int d = ((Integer)derangements(i, true)[1]).intValue();
            System.out.printf("%d  %-7d %-7d\n", i, d, subfact(i));
        }
        
        System.out.printf ("\n!20 = %20d\n", subfact(20L));
    }

    static Object[] derangements(int n, boolean countOnly) {
        int[] seq = iota(n);
        int[] ori = Arrays.copyOf(seq, n);
        long tot = fact(n);

        List<int[]> all = new ArrayList<int[]>();
        int cnt = n == 0 ? 1 : 0;

        while (--tot > 0) {
            int j = n - 2;
            while (seq[j] > seq[j + 1]) {
                j--;
            }
            int k = n - 1;
            while (seq[j] > seq[k]) {
                k--;
            }
            swap(seq, k, j);

            int r = n - 1;
            int s = j + 1;
            while (r > s) {
                swap(seq, s, r);
                r--;
                s++;
            }

            j = 0;
            while (j < n && seq[j] != ori[j]) {
                j++;
            }
            if (j == n) {
                if (countOnly) {
                    cnt++;
                } else {
                    all.add(Arrays.copyOf(seq, n));
                }
            }
        }
        return new Object[]{all, cnt};
    }

    static long fact(long n) {
        long result = 1;
        for (long i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    static long subfact(long n) {
        if (0 <= n && n <= 2) {
            return n != 1 ? 1 : 0;
        }
        return (n - 1) * (subfact(n - 1) + subfact(n - 2));
    }

    static void swap(int[] arr, int lhs, int rhs) {
        int tmp = arr[lhs];
        arr[lhs] = arr[rhs];
        arr[rhs] = tmp;
    }

    static int[] iota(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("iota cannot accept < 0");
        }
        int[] r = new int[n];
        for (int i = 0; i < n; i++) {
            r[i] = i;
        }
        return r;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations
import math


def derangements(n):
    'All deranged permutations of the integers 0..n-1 inclusive'
    return ( perm for perm in permutations(range(n))
             if all(indx != p for indx, p in enumerate(perm)) )

def subfact(n):
    if n == 2 or n == 0:
        return 1
    elif n == 1:
        return 0
    elif  1 <= n <=18:
        return round(math.factorial(n) / math.e)
    elif n.imag == 0 and n.real == int(n.real) and n > 0:
        return (n-1) * ( subfact(n - 1) + subfact(n - 2) )
    else:
        raise ValueError()

def _iterlen(iter):
    'length of an iterator without taking much memory'
    l = 0
    for x in iter:
        l += 1
    return l

if __name__ == '__main__':
    n = 4
    print("Derangements of %s" % (tuple(range(n)),))
    for d in derangements(n):
        print("  %s" % (d,))

    print("\nTable of n vs counted vs calculated derangements")
    for n in range(10):
        print("%2i %-5i %-5i" %
              (n, _iterlen(derangements(n)), subfact(n)))

    n = 20
    print("\n!%i = %i" % (n, subfact(n)))

```

