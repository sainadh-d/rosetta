# Fibonacci sequence

## Task Link
[Rosetta Code - Fibonacci sequence](https://rosettacode.org/wiki/Fibonacci_sequence)

## Java Code
### java_code_1.txt
```java
public static long itFibN(int n)
{
 if (n < 2)
  return n;
 long ans = 0;
 long n1 = 0;
 long n2 = 1;
 for(n--; n > 0; n--)
 {
  ans = n1 + n2;
  n1 = n2;
  n2 = ans;
 }
 return ans;
}

```

### java_code_2.txt
```java
/**
 * O(log(n))
 */
public static long fib(long n) {
    if (n <= 0)
	return 0;

    long i = (int) (n - 1);
    long a = 1, b = 0, c = 0, d = 1, tmp1,tmp2;

    while (i > 0) {
	if (i % 2 != 0) {
            tmp1 = d * b + c * a;
	    tmp2 = d * (b + a) + c * b;
	    a = tmp1;
	    b = tmp2;
	}

        tmp1 = (long) (Math.pow(c, 2) + Math.pow(d, 2));
        tmp2 = d * (2 * c + d);
			
        c = tmp1;
        d = tmp2;

        i = i / 2;
    }
    return a + b;
}

```

### java_code_3.txt
```java
public static long recFibN(final int n)
{
 return (n < 2) ? n : recFibN(n - 1) + recFibN(n - 2);
}

```

### java_code_4.txt
```java
public class Fibonacci {

    static final Map<Integer, Long> cache = new HashMap<>();
    static {
        cache.put(1, 1L);
        cache.put(2, 1L);
    }

    public static long get(int n)
    {
        return (n < 2) ? n : impl(n);
    }
    
    private static long impl(int n)
    {
        return cache.computeIfAbsent(n, k -> impl(k-1) + impl(k-2));
    }
}

```

### java_code_5.txt
```java
public static long anFibN(final long n)
{
 double p = (1 + Math.sqrt(5)) / 2;
 double q = 1 / p;
 return (long) ((Math.pow(p, n) + Math.pow(q, n)) / Math.sqrt(5));
}

```

### java_code_6.txt
```java
public static long fibTailRec(final int n)
{
 return fibInner(0, 1, n);
}

private static long fibInner(final long a, final long b, final int n)
{
 return n < 1 ? a : n == 1 ?  b : fibInner(b, a + b, n - 1);
}

```

### java_code_7.txt
```java
import java.util.function.LongUnaryOperator;
import java.util.stream.LongStream;

public class FibUtil {
 public static LongStream fibStream() {
  return LongStream.iterate( 1l, new LongUnaryOperator() {
   private long lastFib = 0;
   @Override public long applyAsLong( long operand ) {
    long ret = operand + lastFib;
    lastFib = operand;
    return ret;
   }
  });
 }
 public static long fib(long n) {
  return fibStream().limit( n ).reduce((prev, last) -> last).getAsLong();
 }
}

```

## Python Code
### python_code_1.txt
```python
from math import *

def analytic_fibonacci(n):
  sqrt_5 = sqrt(5);
  p = (1 + sqrt_5) / 2;
  q = 1/p;
  return int( (p**n + q**n) / sqrt_5 + 0.5 )

for i in range(1,31):
  print analytic_fibonacci(i),

```

### python_code_10.txt
```python
def fib(n, c={0:1, 1:1}):
    if n not in c:
        x = n // 2
        c[n] = fib(x-1) * fib(n-x-1) + fib(x) * fib(n - x)
    return c[n]

fib(10000000)  # calculating it takes a few seconds, printing it takes eons

```

### python_code_11.txt
```python
F = {0: 0, 1: 1, 2: 1}
def fib(n):
    if n in F:
        return F[n]
    f1 = fib(n // 2 + 1)
    f2 = fib((n - 1) // 2)
    F[n] = (f1 * f1 + f2 * f2 if n & 1 else f1 * f1 - f2 * f2)
    return F[n]

```

### python_code_12.txt
```python
def fib():
    """Yield fib[n+1] + fib[n]"""
    yield 1  # have to start somewhere
    lhs, rhs = fib(), fib()
    yield next(lhs) # move lhs one iteration ahead
    while True:
        yield next(lhs)+next(rhs)

f=fib()
print [next(f) for _ in range(9)]

```

### python_code_13.txt
```python
from itertools import islice

def fib():
    yield 0
    yield 1
    a, b = fib(), fib()
    next(b)
    while True:
        yield next(a)+next(b)
 
print(tuple(islice(fib(), 10)))

```

### python_code_14.txt
```python
'''Fibonacci accumulation'''

from itertools import accumulate, chain
from operator import add


# fibs :: Integer :: [Integer]
def fibs(n):
    '''An accumulation of the first n integers in
       the Fibonacci series. The accumulator is a
       pair of the two preceding numbers.
    '''
    def go(ab, _):
        return ab[1], add(*ab)

    return [xy[1] for xy in accumulate(
        chain(
            [(0, 1)],
            range(1, n)
        ),
        go
    )]


# MAIN ---
if __name__ == '__main__':
    print(
        'First twenty: ' + repr(
            fibs(20)
        )
    )

```

### python_code_15.txt
```python
'''Nth Fibonacci term (by folding)'''

from functools import reduce
from operator import add


# nthFib :: Integer -> Integer
def nthFib(n):
    '''Nth integer in the Fibonacci series.'''
    def go(ab, _):
        return ab[1], add(*ab)
    return reduce(go, range(1, n), (0, 1))[1]


# MAIN ---
if __name__ == '__main__':
    print(
        '1000th term: ' + repr(
            nthFib(1000)
        )
    )

```

### python_code_16.txt
```python
def fib(n):
    from functools import reduce
    return reduce(lambda x, y: (x[1], x[0] + x[1]), range(n), (0, 1))[0]

```

### python_code_17.txt
```python
fibseq = [1,1,]
fiblength = 21
for x in range(1,fiblength-1):
	xcount = fibseq[x-1] + fibseq[x]
	fibseq.append(xcount)
print(xcount)

```

### python_code_18.txt
```python
fi1=fi2=fi3=1 # FIB Russia rextester.com/FEEJ49204
for da in range(1, 88): # Danilin
    print("."*(20-len(str(fi3))), end=' ')
    print(fi3)
    fi3 = fi2+fi1
    fi1 = fi2
    fi2 = fi3

```

### python_code_19.txt
```python
fib=function(n,x=c(0,1)) {
   if (abs(n)>1) for (i in seq(abs(n)-1)) x=c(x[2],sum(x))
   if (n<0) return(x[2]*(-1)^(abs(n)-1)) else if (n) return(x[2]) else return(0)
}  

sapply(seq(-31,31),fib)

```

### python_code_2.txt
```python
def fibIter(n):
    if n < 2:
        return n
    fibPrev = 1
    fib = 1
    for _ in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib

```

### python_code_20.txt
```python
def (fib n)
  if (n < 2)
    n
    (+ (fib n-1) (fib n-2))

```

### python_code_21.txt
```python
def (fib n)
  (+ (fib n-1) (fib n-2))

def (fib n) :case (n < 2)
  n

```

### python_code_22.txt
```python
def (fib n saved)
  # all args in Wart are optional, and we expect callers to not provide `saved`
  default saved :to (table 0 0 1 1)  # pre-populate base cases
  default saved.n :to
    (+ (fib n-1 saved) (fib n-2 saved))
  saved.n

```

### python_code_3.txt
```python
def fib(n,x=[0,1]):
   for i in range(abs(n)-1): x=[x[1],sum(x)]
   return x[1]*pow(-1,abs(n)-1) if n<0 else x[1] if n else 0

for i in range(-30,31): print fib(i),

```

### python_code_4.txt
```python
def fibRec(n):
    if n < 2:
        return n
    else:
        return fibRec(n-1) + fibRec(n-2)

```

### python_code_5.txt
```python
def fibMemo():
    pad = {0:0, 1:1}
    def func(n):
        if n not in pad:
            pad[n] = func(n-1) + func(n-2)
        return pad[n]
    return func

fm = fibMemo()
for i in range(1,31):
    print fm(i),

```

### python_code_6.txt
```python
def fibFastRec(n):
    def fib(prvprv, prv, c):
        if c < 1: 
            return prvprv
        else: 
            return fib(prv, prvprv + prv, c - 1) 
    return fib(0, 1, n)

```

### python_code_7.txt
```python
def fibGen(n):
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1

```

### python_code_8.txt
```python
>>> [i for i in fibGen(11)]

[0,1,1,2,3,5,8,13,21,34,55]

```

### python_code_9.txt
```python
def prevPowTwo(n):
    'Gets the power of two that is less than or equal to the given input'
    if ((n & -n) == n):
        return n
    else:
        n -= 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        n += 1
        return (n/2)

def crazyFib(n):
    'Crazy fast fibonacci number calculation'
    powTwo = prevPowTwo(n)
    
    q = r = i = 1
    s = 0
    
    while(i < powTwo):
        i *= 2
        q, r, s = q*q + r*r, r * (q + s), (r*r + s*s)
        
    while(i < n):
        i += 1
        q, r, s = q+r, q, r
        
    return q

```

