# 9 billion names of God the integer

## Task Link
[Rosetta Code - 9 billion names of God the integer](https://rosettacode.org/wiki/9_billion_names_of_God_the_integer)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.*;
import static java.util.Arrays.asList;
import static java.util.stream.Collectors.toList;
import static java.util.stream.IntStream.range;
import static java.lang.Math.min;

public class Test {

    static List<BigInteger> cumu(int n) {
        List<List<BigInteger>> cache = new ArrayList<>();
        cache.add(asList(BigInteger.ONE));

        for (int L = cache.size(); L < n + 1; L++) {
            List<BigInteger> r = new ArrayList<>();
            r.add(BigInteger.ZERO);
            for (int x = 1; x < L + 1; x++)
                r.add(r.get(r.size() - 1).add(cache.get(L - x).get(min(x, L - x))));
            cache.add(r);
        }
        return cache.get(n);
    }

    static List<BigInteger> row(int n) {
        List<BigInteger> r = cumu(n);
        return range(0, n).mapToObj(i -> r.get(i + 1).subtract(r.get(i)))
                .collect(toList());
    }

    public static void main(String[] args) {
        System.out.println("Rows:");
        for (int x = 1; x < 11; x++)
            System.out.printf("%2d: %s%n", x, row(x));

        System.out.println("\nSums:");
        for (int x : new int[]{23, 123, 1234}) {
            List<BigInteger> c = cumu(x);
            System.out.printf("%s %s%n", x, c.get(c.size() - 1));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
cache = [[1]]
def cumu(n):
    for l in range(len(cache), n+1):
        r = [0]
        for x in range(1, l+1):
            r.append(r[-1] + cache[l-x][min(x, l-x)])
        cache.append(r)
    return cache[n]

def row(n):
    r = cumu(n)
    return [r[i+1] - r[i] for i in range(n)]

print "rows:"
for x in range(1, 11): print "%2d:"%x, row(x)


print "\nsums:"
for x in [23, 123, 1234, 12345]: print x, cumu(x)[-1]

```

### python_code_2.txt
```python
def partitions(N):
    diffs,k,s = [],1,1
    while k * (3*k-1) < 2*N:
        diffs.extend([(2*k - 1, s), (k, s)])
	k,s = k+1,-s

    out = [1] + [0]*N
    for p in range(0, N+1):
        x = out[p]
	for (o,s) in diffs:
           p += o
           if p > N: break
           out[p] += x*s

    return out

p = partitions(12345)
for x in [23,123,1234,12345]: print x, p[x]

```

### python_code_3.txt
```python
def partitions(n):
    partitions.p.append(0)

    for k in xrange(1, n + 1):
        d = n - k * (3 * k - 1) // 2
        if d < 0:
            break

        if k & 1:
            partitions.p[n] += partitions.p[d]
        else:
            partitions.p[n] -= partitions.p[d]

        d -= k
        if d < 0:
            break

        if k & 1:
            partitions.p[n] += partitions.p[d]
        else:
            partitions.p[n] -= partitions.p[d]

    return partitions.p[-1]

partitions.p = [1]

def main():
    ns = set([23, 123, 1234, 12345])
    max_ns = max(ns)

    for i in xrange(1, max_ns + 1):
        if i > max_ns:
            break
        p = partitions(i)
        if i in ns:
            print "%6d: %s" % (i, p)

main()

```

