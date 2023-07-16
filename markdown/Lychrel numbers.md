# Lychrel numbers

## Task Link
[Rosetta Code - Lychrel numbers](https://rosettacode.org/wiki/Lychrel_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.*;

public class Lychrel {

    static Map<BigInteger, Tuple> cache = new HashMap<>();

    static class Tuple {
        final Boolean flag;
        final BigInteger bi;

        Tuple(boolean f, BigInteger b) {
            flag = f;
            bi = b;
        }
    }

    static BigInteger rev(BigInteger bi) {
        String s = new StringBuilder(bi.toString()).reverse().toString();
        return new BigInteger(s);
    }

    static Tuple lychrel(BigInteger n) {
        Tuple res;
        if ((res = cache.get(n)) != null)
            return res;

        BigInteger r = rev(n);
        res = new Tuple(true, n);
        List<BigInteger> seen = new ArrayList<>();

        for (int i = 0; i < 500; i++) {
            n = n.add(r);
            r = rev(n);

            if (n.equals(r)) {
                res = new Tuple(false, BigInteger.ZERO);
                break;
            }

            if (cache.containsKey(n)) {
                res = cache.get(n);
                break;
            }

            seen.add(n);
        }

        for (BigInteger bi : seen)
            cache.put(bi, res);

        return res;
    }

    public static void main(String[] args) {

        List<BigInteger> seeds = new ArrayList<>();
        List<BigInteger> related = new ArrayList<>();
        List<BigInteger> palin = new ArrayList<>();

        for (int i = 1; i <= 10_000; i++) {
            BigInteger n = BigInteger.valueOf(i);

            Tuple t = lychrel(n);

            if (!t.flag)
                continue;

            if (n.equals(t.bi))
                seeds.add(t.bi);
            else
                related.add(t.bi);

            if (n.equals(t.bi))
                palin.add(t.bi);
        }

        System.out.printf("%d Lychrel seeds: %s%n", seeds.size(), seeds);
        System.out.printf("%d Lychrel related%n", related.size());
        System.out.printf("%d Lychrel palindromes: %s%n", palin.size(), palin);
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

def add_reverse(num, max_iter=1000):
    i, nums = 0, {num}
    while True:
        i, num = i+1, num + reverse_int(num)
        nums.add(num)
        if reverse_int(num) == num or i >= max_iter:
            break
    return nums
    
#@functools.lru_cache(maxsize=2**20)
def reverse_int(num):
    return int(str(num)[::-1])

def split_roots_from_relateds(roots_and_relateds):
    roots = roots_and_relateds[::]
    i = 1
    while i < len(roots):
        this = roots[i]
        if any(this.intersection(prev) for prev in roots[:i]):
            del roots[i]
        else:
            i += 1
    root = [min(each_set) for each_set in roots]
    related = [min(each_set) for each_set in roots_and_relateds]
    related = [n for n in related if n not in root]
    return root, related

def find_lychrel(maxn, max_reversions):
    'Lychrel number generator'
    series = [add_reverse(n, max_reversions*2) for n in range(1, maxn + 1)]
    roots_and_relateds = [s for s in series if len(s) > max_reversions]
    return split_roots_from_relateds(roots_and_relateds)


if __name__ == '__main__':
    maxn, reversion_limit = 10000, 500
    print("Calculations using n = 1..%i and limiting each search to 2*%i reverse-digits-and-adds"
          % (maxn, reversion_limit))
    lychrel, l_related = find_lychrel(maxn, reversion_limit)
    print('  Number of Lychrel numbers:', len(lychrel))
    print('    Lychrel numbers:', ', '.join(str(n) for n in lychrel))
    print('  Number of Lychrel related:', len(l_related))
    #print('    Lychrel related:', ', '.join(str(n) for n in l_related))
    pals = [x for x in lychrel + l_related  if x == reverse_int(x)]
    print('  Number of Lychrel palindromes:', len(pals))
    print('    Lychrel palindromes:', ', '.join(str(n) for n in pals))

```

### python_code_2.txt
```python
from __future__ import print_function

def rev(n): return int(str(n)[::-1])

def lychel(n, cache = {}):
    if n in cache: return cache[n]

    n0, r = n, rev(n)
    res, seen = (True, n), []
    for i in range(1000):
        n += r
        r = rev(n)
        if n == r:
            res = (False, 0)
            break
        if n in cache:
            res = cache[n]
            break
        seen.append(n)

    for x in seen: cache[x] = res
    return res

seeds, related, palin = [], [], []

for i in range(1, 1000000):
    tf, s = lychel(i)
    if not tf: continue
    (seeds if i == s else related).append(i)
    if i == rev(i): palin.append(i)

print("%d Lychel seeds:"%len(seeds), seeds)
print("%d Lychel related" % len(related))
print("%d Lychel palindromes:" % len(palin), palin)

```

