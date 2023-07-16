# Prime triangle

## Task Link
[Rosetta Code - Prime triangle](https://rosettacode.org/wiki/Prime_triangle)

## Java Code
### java_code_1.txt
```java
public class PrimeTriangle {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        for (int i = 2; i <= 20; ++i) {
            int[] a = new int[i];
            for (int j = 0; j < i; ++j)
                a[j] = j + 1;
            if (findRow(a, 0, i))
                printRow(a);                
        }
        System.out.println();
        StringBuilder s = new StringBuilder();
        for (int i = 2; i <= 20; ++i) {
            int[] a = new int[i];
            for (int j = 0; j < i; ++j)
                a[j] = j + 1;
            if (i > 2)
                s.append(" ");
            s.append(countRows(a, 0, i));
        }
        System.out.println(s);
        long finish = System.currentTimeMillis();
        System.out.printf("\nElapsed time: %d milliseconds\n", finish - start);
    }

    private static void printRow(int[] a) {
        for (int i = 0; i < a.length; ++i) {
            if (i != 0)
                System.out.print(" ");
            System.out.printf("%2d", a[i]);
        }
        System.out.println();
    }

    private static boolean findRow(int[] a, int start, int length) {
        if (length == 2)
            return isPrime(a[start] + a[start + 1]);
        for (int i = 1; i + 1 < length; i += 2) {
            if (isPrime(a[start] + a[start + i])) {
                swap(a, start + i, start + 1);
                if (findRow(a, start + 1, length - 1))
                    return true;
                swap(a, start + i, start + 1);
            }
        }
        return false;
    }

    private static int countRows(int[] a, int start, int length) {
        int count = 0;
        if (length == 2) {
            if (isPrime(a[start] + a[start + 1]))
                ++count;
        } else {
            for (int i = 1; i + 1 < length; i += 2) {
                if (isPrime(a[start] + a[start + i])) {
                    swap(a, start + i, start + 1);
                    count += countRows(a, start + 1, length - 1);
                    swap(a, start + i, start + 1);
                }
            }
        }
        return count;
    }

    private static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    private static boolean isPrime(int n) {
        return ((1L << n) & 0x28208a20a08a28acL) != 0;
    }
}

```

## Python Code
### python_code_1.txt
```python
from numpy import array
# for Rosetta Code by MG - 20230312
def is_prime(n: int) -> bool:
    assert n < 64
    return ((1 << n) & 0x28208a20a08a28ac) != 0

def prime_triangle_row(a: array, start: int, length: int) -> bool:
    if length == 2:
        return is_prime(a[0] + a[1])
    for i in range(1, length - 1, 1):
        if is_prime(a[start] + a[start + i]):
            a[start + i], a[start + 1] = a[start + 1], a[start + i]
            if prime_triangle_row(a, start + 1, length - 1):
                return True
            a[start + i], a[start + 1] = a[start + 1], a[start + i]
    return False

def prime_triangle_count(a: array, start: int, length: int) -> int:
    count: int = 0
    if length == 2:
        if is_prime(a[start] + a[start + 1]):
            count += 1
    else:
        for i in range(1, length - 1, 1):
            if is_prime(a[start] + a[start + i]):
                a[start + i], a[start + 1] = a[start + 1], a[start + i]
                count += prime_triangle_count(a, start + 1, length - 1)
                a[start + i], a[start + 1] = a[start + 1], a[start + i]
    return count

def print_row(a: array):
    if a == []:
        return
    print("%2d"% a[0], end=" ")
    for x in a[1:]:
        print("%2d"% x, end=" ")
    print()

for n in range(2, 21):
    tr: array = [_ for _ in range(1, n + 1)]
    if prime_triangle_row(tr, 0, n):
        print_row(tr)
print()
for n in range(2, 21):
    tr: array = [_ for _ in range(1, n + 1)]
    if n > 2:
        print(" ", end="")
    print(prime_triangle_count(tr, 0, n), end="")
print()

```

