# Unbias a random generator

## Task Link
[Rosetta Code - Unbias a random generator](https://rosettacode.org/wiki/Unbias_a_random_generator)

## Java Code
### java_code_1.txt
```java
public class Bias {
    public static boolean biased(int n) {
        return Math.random() < 1.0 / n;
    }

    public static boolean unbiased(int n) {
        boolean a, b;
        do {
            a = biased(n);
            b = biased(n);
        } while (a == b);
        return a;
    }

    public static void main(String[] args) {
        final int M = 50000;
        for (int n = 3; n < 7; n++) {
            int c1 = 0, c2 = 0;
            for (int i = 0; i < M; i++) {
                c1 += biased(n) ? 1 : 0;
                c2 += unbiased(n) ? 1 : 0;
            }
            System.out.format("%d: %2.2f%%  %2.2f%%\n",
                              n, 100.0*c1/M, 100.0*c2/M);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
import random

def randN(N):
    " 1,0 random generator factory with 1 appearing 1/N'th of the time"
    return lambda: random.randrange(N) == 0

def unbiased(biased):
    'uses a biased() generator of 1 or 0, to create an unbiased one'
    this, that = biased(), biased()
    while this == that: # Loop until 10 or 01
        this, that = biased(), biased()
    return this         # return the first

if __name__ == '__main__':
    from collections import namedtuple

    Stats = namedtuple('Stats', 'count1 count0 percent')

    for N in range(3, 7):
        biased = randN(N)
        v = [biased() for x in range(1000000)]
        v1, v0 = v.count(1), v.count(0)
        print ( "Biased(%i)  = %r" % (N, Stats(v1, v0, 100. * v1/(v1 + v0))) )

        v = [unbiased(biased) for x in range(1000000)]
        v1, v0 = v.count(1), v.count(0)
        print ( "  Unbiased = %r" % (Stats(v1, v0, 100. * v1/(v1 + v0)), ) )

```

