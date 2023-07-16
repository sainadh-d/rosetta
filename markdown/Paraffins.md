# Paraffins

## Task Link
[Rosetta Code - Paraffins](https://rosettacode.org/wiki/Paraffins)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.Arrays;

class Test {
    final static int nMax = 250;
    final static int nBranches = 4;

    static BigInteger[] rooted = new BigInteger[nMax + 1];
    static BigInteger[] unrooted = new BigInteger[nMax + 1];
    static BigInteger[] c = new BigInteger[nBranches];

    static void tree(int br, int n, int l, int inSum, BigInteger cnt) {
        int sum = inSum;
        for (int b = br + 1; b <= nBranches; b++) {
            sum += n;

            if (sum > nMax || (l * 2 >= sum && b >= nBranches))
                return;

            BigInteger tmp = rooted[n];
            if (b == br + 1) {
                c[br] = tmp.multiply(cnt);
            } else {
                c[br] = c[br].multiply(tmp.add(BigInteger.valueOf(b - br - 1)));
                c[br] = c[br].divide(BigInteger.valueOf(b - br));
            }

            if (l * 2 < sum)
                unrooted[sum] = unrooted[sum].add(c[br]);

            if (b < nBranches)
                rooted[sum] = rooted[sum].add(c[br]);

            for (int m = n - 1; m > 0; m--)
                tree(b, m, l, sum, c[br]);
        }
    }

    static void bicenter(int s) {
        if ((s & 1) == 0) {
            BigInteger tmp = rooted[s / 2];
            tmp = tmp.add(BigInteger.ONE).multiply(rooted[s / 2]);
            unrooted[s] = unrooted[s].add(tmp.shiftRight(1));
        }
    }

    public static void main(String[] args) {
        Arrays.fill(rooted, BigInteger.ZERO);
        Arrays.fill(unrooted, BigInteger.ZERO);
        rooted[0] = rooted[1] = BigInteger.ONE;
        unrooted[0] = unrooted[1] = BigInteger.ONE;

        for (int n = 1; n <= nMax; n++) {
            tree(0, n, n, 1, BigInteger.ONE);
            bicenter(n);
            System.out.printf("%d: %s%n", n, unrooted[n]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
try:
    import psyco
    psyco.full()
except ImportError:
    pass

MAX_N = 300
BRANCH = 4

ra = [0] * MAX_N
unrooted = [0] * MAX_N

def tree(br, n, l, sum = 1, cnt = 1):
    global ra, unrooted, MAX_N, BRANCH
    for b in xrange(br + 1, BRANCH + 1):
        sum += n
        if sum >= MAX_N:
            return

        # prevent unneeded long math
        if l * 2 >= sum and b >= BRANCH:
            return

        if b == br + 1:
            c = ra[n] * cnt
        else:
            c = c * (ra[n] + (b - br - 1)) / (b - br)

        if l * 2 < sum:
            unrooted[sum] += c

        if b < BRANCH:
            ra[sum] += c;
            for m in range(1, n):
                tree(b, m, l, sum, c)

def bicenter(s):
    global ra, unrooted
    if not (s & 1):
        aux = ra[s / 2]
        unrooted[s] += aux * (aux + 1) / 2


def main():
    global ra, unrooted, MAX_N
    ra[0] = ra[1] = unrooted[0] = unrooted[1] = 1

    for n in xrange(1, MAX_N):
        tree(0, n, n)
        bicenter(n)
        print "%d: %d" % (n, unrooted[n])

main()

```

### python_code_2.txt
```python
from itertools import count, chain, tee, islice, cycle
from fractions import Fraction
from sys import setrecursionlimit
setrecursionlimit(5000)

def frac(a,b): return a//b if a%b == 0 else Fraction(a,b)

# infinite polynomial class
class Poly:
    def __init__(self, gen = None):
        self.gen, self.source = (None, gen) if type(gen) is Poly \
            else (gen, None)

    def __iter__(self):
        # We're essentially tee'ing it everytime the iterator
        # is, well, iterated.  This may be excessive.
        return Poly(self)

    def getsource(self):
        if self.gen == None:
            s = self.source
            s.getsource()
            s.gen, self.gen = tee(s.gen, 2)

    def next(self):
        self.getsource()
        return next(self.gen)

    __next__ = next

    # Overload "<<" as stream input operator. Hey, C++ does it.
    def __lshift__(self, a): self.gen = a

    # The other operators are pretty much what one would expect
    def __neg__(self): return Poly(-x for x in self)

    def __sub__(a, b): return a + (-b)

    def __rsub__(a, n):
        a = Poly(a)
        def gen():
            yield(n - next(a))
            for x in a: yield(-x)
        return Poly(gen())

    def __add__(a, b):
        if type(b) is Poly:
            return Poly(x + y for (x,y) in zip(a,b))

        a = Poly(a)
        def gen():
            yield(next(a) + b)
            for x in a: yield(x)

        return Poly(gen())

    def __radd__(a,b):
        return a + b

    def __mul__(a,b):
        if not type(b) is Poly:
            return Poly(x*b for x in a)

        def gen():
            s = Poly(cycle([0]))
            for y in b:
                s += y*a
                yield(next(s))

        return Poly(gen())

    def __rmul__(a,b): return a*b

    def __truediv__(a,b):
        if not type(b) is Poly:
            return Poly(frac(x, b) for x in a)

        a, b = Poly(a), Poly(b)
        def gen():
            r, bb = a,next(b)
            while True:
                aa = next(r)
                q = frac(aa, bb)
                yield(q)
                r -= q*b

        return Poly(gen())

    def repl(self, n):
        def gen():
            for x in self:
                yield(x)
                for i in range(n-1): yield(0)
        return Poly(gen())

    def __pow__(self, n):
        return Poly(self) if n == 1 else self * self**(n-1)

def S2(a,b): return (a*a + b)/2
def S4(a,b,c,d): return a**4/24 + a**2*b/4 + a*c/3 + b**2/8 + d/4

x1 = Poly()
x2 = x1.repl(2)
x3 = x1.repl(3)
x4 = x1.repl(4)
x1 << chain([1], (x1**3 + 3*x1*x2 + 2*x3)/6)

a598 = x1
a678 = Poly(chain([0], S4(x1, x2, x3, x4)))
a599 = S2(x1 - 1, x2 - 1)
a602 = a678 - a599 + x2

for n,x in zip(count(0), islice(a602, 500)): print(n,x)

```

### python_code_3.txt
```python
#!/usr/bin/python3

from functools import lru_cache

def Z_S(n, f, k):
    """
    The cycle index of the symmetric group has recurrence
        Z(S_n, f(x)) = 1/n \sum_{i=1}^n f(x^i) Z(S_{n-i}, f(x)).
    This function finds the coefficient of x^k in Z(S_n, f(x))
    """
    # Special case to avoid division by zero
    if n == 0:
        return 1 if k == 0 else 0
    # Special case as a speed optimisation
    if n == 1:
        return f(k)
    return sum(
        sum(f(ij // i) * Z_S(n-i, f, k - ij) for ij in range(0, k+1, i))
        for i in range(1, n+1)
    ) // n

@lru_cache(maxsize=None)
def A000598(k): return 1 if k == 0 else Z_S(3, A000598, k-1)

@lru_cache(maxsize=None)
def A000642(k): return Z_S(2, A000598, k)

def A000631(k): return Z_S(2, A000642, k)

def A000602(k): return A000642(k) + (A000642((k-1) // 2) if k % 2 == 1 else 0) - A000631(k-1)

for k in range(500): print(k, A000602(k))

```

