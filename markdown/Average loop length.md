# Average loop length

## Task Link
[Rosetta Code - Average loop length](https://rosettacode.org/wiki/Average_loop_length)

## Java Code
### java_code_1.txt
```java
import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class AverageLoopLength {

    private static final int N = 100000;

    //analytical(n) = sum_(i=1)^n (n!/(n-i)!/n**i)
    private static double analytical(int n) {
        double[] factorial = new double[n + 1];
        double[] powers = new double[n + 1];
        powers[0] = 1.0;
        factorial[0] = 1.0;
        for (int i = 1; i <= n; i++) {
            factorial[i] = factorial[i - 1] * i;
            powers[i] = powers[i - 1] * n;
        }
        double sum = 0;
        //memoized factorial and powers
        for (int i = 1; i <= n; i++) {
            sum += factorial[n] / factorial[n - i] / powers[i];
        }
        return sum;
    }

    private static double average(int n) {
        Random rnd = new Random();
        double sum = 0.0;
        for (int a = 0; a < N; a++) {
            int[] random = new int[n];
            for (int i = 0; i < n; i++) {
                random[i] = rnd.nextInt(n);
            }
            Set<Integer> seen = new HashSet<>(n);
            int current = 0;
            int length = 0;
            while (seen.add(current)) {
                length++;
                current = random[current];
            }
            sum += length;
        }
        return sum / N;
    }

    public static void main(String[] args) {
        System.out.println(" N    average    analytical    (error)");
        System.out.println("===  =========  ============  =========");
        for (int i = 1; i <= 20; i++) {
            double avg = average(i);
            double ana = analytical(i);
            System.out.println(String.format("%3d  %9.4f  %12.4f  (%6.2f%%)", i, avg, ana, ((ana - avg) / ana * 100)));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division # Only necessary for Python 2.X
from math import factorial
from random import randrange

MAX_N = 20
TIMES = 1000000

def analytical(n):
	return sum(factorial(n) / pow(n, i) / factorial(n -i) for i in range(1, n+1))

def test(n, times):
    count = 0
    for i in range(times):
        x, bits = 1, 0
        while not (bits & x):
            count += 1
            bits |= x
            x = 1 << randrange(n)
    return count / times

if __name__ == '__main__':
    print(" n\tavg\texp.\tdiff\n-------------------------------")
    for n in range(1, MAX_N+1):
        avg = test(n, TIMES)
        theory = analytical(n)
        diff = (avg / theory - 1) * 100
        print("%2d %8.4f %8.4f %6.3f%%" % (n, avg, theory, diff))

```

