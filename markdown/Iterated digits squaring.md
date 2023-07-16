# Iterated digits squaring

## Task Link
[Rosetta Code - Iterated digits squaring](https://rosettacode.org/wiki/Iterated_digits_squaring)

## Java Code
### java_code_1.txt
```java
import java.util.stream.IntStream;

public class IteratedDigitsSquaring {

    public static void main(String[] args) {
        long r = IntStream.range(1, 100_000_000)
                .parallel()
                .filter(n -> calc(n) == 89)
                .count();
        System.out.println(r);
    }

    private static int calc(int n) {
        while (n != 89 && n != 1) {
            int total = 0;
            while (n > 0) {
                total += Math.pow(n % 10, 2);
                n /= 10;
            }
            n = total;
        }
        return n;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> step = lambda x: sum(int(d) ** 2 for d in str(x))
>>> iterate = lambda x: x if x in [1, 89] else iterate(step(x))
>>> [iterate(x) for x in xrange(1, 20)]
[1, 89, 89, 89, 89, 89, 1, 89, 89, 1, 89, 89, 1, 89, 89, 89, 89, 89, 1]

```

### python_code_2.txt
```python
from math import ceil, log10, factorial

def next_step(x):
    result = 0
    while x > 0:
        result += (x % 10) ** 2
        x /= 10
    return result

def check(number):
    candidate = 0
    for n in number:
        candidate = candidate * 10 + n

    while candidate != 89 and candidate != 1:
        candidate = next_step(candidate)

    if candidate == 89:
        digits_count = [0] * 10
        for d in number:
            digits_count[d] += 1

        result = factorial(len(number))
        for c in digits_count:
            result /= factorial(c)
        return result

    return 0

def main():
    limit = 100000000
    cache_size = int(ceil(log10(limit)))
    assert 10 ** cache_size == limit

    number = [0] * cache_size
    result = 0
    i = cache_size - 1

    while True:
        if i == 0 and number[i] == 9:
            break
        if i == cache_size - 1 and number[i] < 9:
            number[i] += 1
            result += check(number)
        elif number[i] == 9:
            i -= 1
        else:
            number[i] += 1
            for j in xrange(i + 1, cache_size):
                number[j] = number[i]
            i = cache_size - 1
            result += check(number)

    print result

main()

```

### python_code_3.txt
```python
from itertools import combinations_with_replacement
from array import array
from time import clock
D = 8
F = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000]
def b(n):
    yield 1
    for g in range(1,n+1):
        gn = g
        res = 0
        while gn > 0:
            gn,rem = divmod(gn,10)
            res += rem**2
        if res==89:
            yield 0
        else:
            yield res
N = array('I',b(81*D))
for n in range(2,len(N)):
    q = N[n]
    while q>1:
        q = N[q]
    N[n] = q

es = clock()
z = 0
for n in combinations_with_replacement(range(10),D):
    t = 0
    for g in n:
        t += g*g
    if N[t] == 0:
        continue
    t = [0,0,0,0,0,0,0,0,0,0]
    for g in n:
        t[g] += 1
    t1 = F[D]
    for g in t:
        t1 /= F[g]
    z += t1
ee = clock() - es
print "\nD==" + str(D) + "\n  " + str(z) + " numbers produce 1 and " + str(10**D-z) + " numbers produce 89"
print "Time ~= " + str(ee) + " secs"

```

### python_code_4.txt
```python
>>> from functools import lru_cache
>>> @lru_cache(maxsize=1024)
def ids(n):
	if n in {1, 89}: return n
	else: return ids(sum(int(d) ** 2 for d in str(n)))

	
>>> ids(15)
89
>>> [ids(x) for x in range(1, 21)]
[1, 89, 89, 89, 89, 89, 1, 89, 89, 1, 89, 89, 1, 89, 89, 89, 89, 89, 1, 89]
>>> sum(ids(x) == 89 for x in range(1, 100000000))
85744333
>>>

```

### python_code_5.txt
```python
>>> from functools import lru_cache
>>> @lru_cache(maxsize=1024)
def _ids(nt):
	if nt in {('1',), ('8', '9')}: return nt
	else: return _ids(tuple(sorted(str(sum(int(d) ** 2 for d in nt)))))

	
>>> def ids(n):
	return int(''.join(_ids(tuple(sorted(str(n))))))

>>> ids(1), ids(15)
(1, 89)
>>> [ids(x) for x in range(1, 21)]
[1, 89, 89, 89, 89, 89, 1, 89, 89, 1, 89, 89, 1, 89, 89, 89, 89, 89, 1, 89]
>>> sum(ids(x) == 89 for x in range(1, 100000000))
85744333
>>> _ids.cache_info()
CacheInfo(hits=99991418, misses=5867462, maxsize=1024, currsize=1024)
>>>

```

### python_code_6.txt
```python
from __future__ import print_function
from itertools import count

def check89(n):
    while True:
        n, t = 0, n
        while t: n, t = n + (t%10)**2, t//10
        if n <= 1: return False
        if n ==89: return True

a, sq, is89 = [1], [x**2 for x in range(1, 10)], [False]
for n in range(1, 500):
    b, a = a, a + [0]*81
    is89 += map(check89, range(len(b), len(a)))

    for i,v in enumerate(b):
        for s in sq: a[i + s] += v

    x = sum(a[i] for i in range(len(a)) if is89[i])
    print("10^%d" % n, x)

```

