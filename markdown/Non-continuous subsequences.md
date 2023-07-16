# Non-continuous subsequences

## Task Link
[Rosetta Code - Non-continuous subsequences](https://rosettacode.org/wiki/Non-continuous_subsequences)

## Java Code
### java_code_1.txt
```java
public class NonContinuousSubsequences {

    public static void main(String args[]) {
        seqR("1234", "", 0, 0);
    }

    private static void seqR(String s, String c, int i, int added) {
        if (i == s.length()) {
            if (c.trim().length() > added)
                System.out.println(c);
        } else {
            seqR(s, c + s.charAt(i), i + 1, added + 1);
            seqR(s, c + ' ', i + 1, added);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def ncsub(seq, s=0):
    if seq:
        x = seq[:1]
        xs = seq[1:]
        p2 = s % 2
        p1 = not p2
        return [x + ys for ys in ncsub(xs, s + p1)] + ncsub(xs, s + p2)
    else:
        return [[]] if s >= 3 else []

```

### python_code_2.txt
```python
from sys import argv
import psyco

def C(n, k):
    result = 1
    for d in xrange(1, k+1):
        result *= n
        n -= 1
        result /= d
    return result

# http://oeis.org/A002662
nsubs = lambda n: sum(C(n, k) for k in xrange(3, n+1))

def ncsub(seq):
    n = len(seq)
    result = [None] * nsubs(n)
    pos = 0

    for i in xrange(1, 2 ** n):
        S  = []
        nc = False
        for j in xrange(n + 1):
            k = i >> j
            if k == 0:
                if nc:
                    result[pos] = S
                    pos += 1
                break
            elif k % 2:
                S.append(seq[j])
            elif S:
                nc = True
    return result

from sys import argv
import psyco
psyco.full()
n = 10 if len(argv) < 2 else int(argv[1])
print len( ncsub(range(1, n)) )

```

