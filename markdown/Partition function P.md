# Partition function P

## Task Link
[Rosetta Code - Partition function P](https://rosettacode.org/wiki/Partition_function_P)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PartitionFunction {
    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        BigInteger result = partitions(6666);
        long end = System.currentTimeMillis();
        System.out.println("P(6666) = " + result);
        System.out.printf("elapsed time: %d milliseconds\n", end - start);
    }

    private static BigInteger partitions(int n) {
        BigInteger[] p = new BigInteger[n + 1];
        p[0] = BigInteger.ONE;
        for (int i = 1; i <= n; ++i) {
            p[i] = BigInteger.ZERO;
            for (int k = 1; ; ++k) {
                int j = (k * (3 * k - 1))/2;
                if (j > i)
                    break;
                if ((k & 1) != 0)
                    p[i] = p[i].add(p[i - j]);
                else
                    p[i] = p[i].subtract(p[i - j]);
                j += k;
                if (j > i)
                    break;
                if ((k & 1) != 0)
                    p[i] = p[i].add(p[i - j]);
                else
                    p[i] = p[i].subtract(p[i - j]);
            }
        }
        return p[n];
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

def posd():
    "diff between position numbers. 1, 2, 3... interleaved with  3, 5, 7..."
    count, odd = 1, 3
    while True:
        yield count
        yield odd
        count, odd = count + 1, odd + 2

def pos_gen():
    "position numbers. 1 3 2 5 7 4 9 ..."
    val = 1
    diff = posd()
    while True:
        yield val
        val += next(diff)
                
def plus_minus():
    "yield (list_offset, sign) or zero for Partition calc"
    n, sign = 0, [1, 1]
    p_gen = pos_gen()
    out_on = next(p_gen)
    while True:
        n += 1
        if n == out_on:
            next_sign = sign.pop(0)
            if not sign:
                sign = [-next_sign] * 2
            yield -n, next_sign
            out_on = next(p_gen)
        else:
            yield 0
            
def part(n):
    "Partition numbers"
    p = [1]
    p_m = plus_minus()
    mods = []
    for _ in range(n):
        next_plus_minus = next(p_m)
        if next_plus_minus:
            mods.append(next_plus_minus)
        p.append(sum(p[offset] * sign for offset, sign in mods))
    return p[-1]
        
print("(Intermediaries):")
print("    posd:", list(islice(posd(), 10)))
print("    pos_gen:", list(islice(pos_gen(), 10)))
print("    plus_minus:", list(islice(plus_minus(), 15)))
print("\nPartitions:", [part(x) for x in range(15)])

```

### python_code_2.txt
```python
def par_primes():
    "Prime number generator from the partition machine"
    p = [1]
    p_m = plus_minus()
    mods = []
    n = 0
    while True:
        n += 1
        next_plus_minus = next(p_m)
        if next_plus_minus:
            mods.append(next_plus_minus)
        p.append(sum(p[offset] * sign for offset, sign in mods))
        if p[0] + 1 == p[-1]:
            yield p[0]
        p[0] += 1
    yield p

print("\nPrimes:", list(islice(par_primes(), 15)))

```

### python_code_3.txt
```python
from typing import List


def partitions(n: int) -> int:
    """Count partitions."""
    p: List[int] = [1] + [0] * n
    for i in range(1, n + 1):
        k: int = 0
        while True:
            k += 1
            j: int = (k * (3*k - 1)) // 2
            if (j > i):
                break
            if (k & 1):
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]
            j = (k * (3*k + 1)) // 2
            if (j > i):
                break
            if (k & 1):
                p[i] += p[i - j]
            else:
                p[i] -= p[i - j]

    return p[n]


if __name__ == '__main__':
    print("\nPartitions:", [partitions(x) for x in range(15)])

```

