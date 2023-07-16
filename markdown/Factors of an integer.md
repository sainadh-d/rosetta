# Factors of an integer

## Task Link
[Rosetta Code - Factors of an integer](https://rosettacode.org/wiki/Factors_of_an_integer)

## Java Code
### java_code_1.txt
```java
public static TreeSet<Long> factors(long n)
{
 TreeSet<Long> factors = new TreeSet<Long>();
 factors.add(n);
 factors.add(1L);
 for(long test = n - 1; test >= Math.sqrt(n); test--)
  if(n % test == 0)
  {
   factors.add(test);
   factors.add(n / test);
  }
 return factors;
}

```

## Python Code
### python_code_1.txt
```python
>>> def factors(n):
      return [i for i in range(1, n + 1) if not n%i]

```

### python_code_2.txt
```python
>>> def factors(n):
      return [i for i in range(1, n//2 + 1) if not n%i] + [n]

>>> factors(45)
[1, 3, 5, 9, 15, 45]

```

### python_code_3.txt
```python
from math import isqrt
def factor(n):
    factors1, factors2 = [], []
    for x in range(1, isqrt(n)):
        if n % x == 0:
            factors1.append(x)
            factors2.append(n // x)
    x += 1
    if x * x == n:
        factors1.append(x)
    factors1.extend(reversed(factors2))
    return factors1

for i in 45, 53, 64:
    print("%i: factors: %s" % (i, factor(i)))

```

### python_code_4.txt
```python
from itertools import chain, cycle, accumulate # last of which is Python 3 only

def factors(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r

```

