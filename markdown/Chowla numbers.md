# Chowla numbers

## Task Link
[Rosetta Code - Chowla numbers](https://rosettacode.org/wiki/Chowla_numbers)

## Java Code
### java_code_1.txt
```java
public class Chowla {

    public static void main(String[] args) {
        int[] chowlaNumbers = findChowlaNumbers(37);
        for (int i = 0; i < chowlaNumbers.length; i++) {
            System.out.printf("chowla(%d) = %d%n", (i+1), chowlaNumbers[i]);
        }
        System.out.println();

        int[][] primes = countPrimes(100, 10_000_000);
        for (int i = 0; i < primes.length; i++) {
            System.out.printf(Locale.US, "There is %,d primes up to %,d%n", primes[i][1], primes[i][0]);
        }
        System.out.println();

        int[] perfectNumbers = findPerfectNumbers(35_000_000);
        for (int i = 0; i < perfectNumbers.length; i++) {
            System.out.printf("%d is a perfect number%n", perfectNumbers[i]);
        }
        System.out.printf(Locale.US, "There are %d perfect numbers < %,d%n", perfectNumbers.length, 35_000_000);
    }

    public static int chowla(int n) {
        if (n < 0) throw new IllegalArgumentException("n is not positive");
        int sum = 0;
        for (int i = 2, j; i * i <= n; i++)
            if (n % i == 0) sum += i + (i == (j = n / i) ? 0 : j);
        return sum;
    }

    protected static int[][] countPrimes(int power, int limit) {
        int count = 0;
        int[][] num = new int[countMultiplicity(limit, power)][2];
        for (int n = 2, i=0;  n <= limit; n++) {
            if (chowla(n) == 0) count++;
            if (n % power == 0) {
                num[i][0] = power;
                num[i][1] = count;
                i++;
                power *= 10;
            }
        }
        return num;
    }

    protected static int countMultiplicity(int limit, int start) {
        int count = 0;
        int cur = limit;
        while(cur >= start) {
            count++;
            cur = cur/10;
        }
        return count;
    }

    protected static int[] findChowlaNumbers(int limit) {
        int[] num = new int[limit];
        for (int i = 0; i < limit; i++) {
            num[i] = chowla(i+1);
        }
        return num;
    }

    protected static int[] findPerfectNumbers(int limit) {
        int count = 0;
        int[] num = new int[count];

        int k = 2, kk = 3, p;
        while ((p = k * kk) < limit) {
            if (chowla(p) == p - 1) {
                num = increaseArr(num);
                num[count++] = p;
            }
            k = kk + 1;
            kk += k;
        }
        return num;
    }

    private static int[] increaseArr(int[] arr) {
        int[] tmp = new int[arr.length + 1];
        System.arraycopy(arr, 0, tmp, 0, arr.length);
        return tmp;
    }
}

```

## Python Code
### python_code_1.txt
```python
# https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.divisors
from sympy import divisors

def chowla(n):
    return 0 if n < 2 else sum(divisors(n, generator=True)) - 1 -n

def is_prime(n):
    return chowla(n) == 0

def primes_to(n):
    return sum(chowla(i) == 0 for i in range(2, n))

def perfect_between(n, m):
    c = 0
    print(f"\nPerfect numbers between [{n:_}, {m:_})")
    for i in range(n, m):
        if i > 1 and chowla(i) == i - 1:
            print(f"  {i:_}")
            c += 1
    print(f"Found {c} Perfect numbers between [{n:_}, {m:_})")
    

if __name__ == '__main__':
    for i in range(1, 38):
        print(f"chowla({i:2}) == {chowla(i)}")
    for i in range(2, 6):
        print(f"primes_to({10**i:_}) == {primes_to(10**i):_}")
    perfect_between(1, 1_000_000)
    print()
    for i in range(6, 8):
        print(f"primes_to({10**i:_}) == {primes_to(10**i):_}")
    perfect_between(1_000_000, 35_000_000)

```

### python_code_2.txt
```python
from numba import jit

# https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.divisors
from sympy import divisors

@jit
def chowla(n):
    return 0 if n < 2 else sum(divisors(n, generator=True)) - 1 -n

@jit
def is_prime(n):
    return chowla(n) == 0

@jit
def primes_to(n):
    acc = 0
    for i in range(2, n):
        if chowla(i) == 0:
            acc += 1
    return acc

@jit
def _perfect_between(n, m):
    for i in range(n, m):
        if i > 1 and chowla(i) == i - 1:
            yield i

def perfect_between(n, m):
    c = 0
    print(f"\nPerfect numbers between [{n:_}, {m:_})")
    for i in _perfect_between(n, m):
        print(f"  {i:_}")
        c += 1
    print(f"Found {c} Perfect numbers between [{n:_}, {m:_})")

```

