# Abundant, deficient and perfect number classifications

## Task Link
[Rosetta Code - Abundant, deficient and perfect number classifications](https://rosettacode.org/wiki/Abundant,_deficient_and_perfect_number_classifications)

## Java Code
### java_code_1.txt
```java
import java.util.stream.LongStream;

public class NumberClassifications {
 
    public static void main(String[] args) {
        int deficient = 0;
        int perfect = 0;
        int abundant = 0;
 
        for (long i = 1; i <= 20_000; i++) {
            long sum = properDivsSum(i);
            if (sum < i)
                deficient++;
            else if (sum == i)
                perfect++;
            else
                abundant++;
        }
        System.out.println("Deficient: " + deficient);
        System.out.println("Perfect: " + perfect);
        System.out.println("Abundant: " + abundant);
    }
 
    public static long properDivsSum(long n) {
        return LongStream.rangeClosed(1, (n + 1) / 2).filter(i -> n != i && n % i == 0).sum();
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from proper_divisors import proper_divs
>>> from collections import Counter
>>> 
>>> rangemax = 20000
>>> 
>>> def pdsum(n):
...     return sum(proper_divs(n))
... 
>>> def classify(n, p):
...     return 'perfect' if n == p else 'abundant' if p > n else 'deficient'
... 
>>> classes = Counter(classify(n, pdsum(n)) for n in range(1, 1 + rangemax))
>>> classes.most_common()
[('deficient', 15043), ('abundant', 4953), ('perfect', 4)]
>>>

```

### python_code_2.txt
```python
'''Abundant, deficient and perfect number classifications'''

from itertools import accumulate, chain, groupby, product
from functools import reduce
from math import floor, sqrt
from operator import mul


# deficientPerfectAbundantCountsUpTo :: Int -> (Int, Int, Int)
def deficientPerfectAbundantCountsUpTo(n):
    '''Counts of deficient, perfect, and abundant
       integers in the range [1..n].
    '''
    def go(dpa, x):
        deficient, perfect, abundant = dpa
        divisorSum = sum(properDivisors(x))
        return (
            succ(deficient), perfect, abundant
        ) if x > divisorSum else (
            deficient, perfect, succ(abundant)
        ) if x < divisorSum else (
            deficient, succ(perfect), abundant
        )
    return reduce(go, range(1, 1 + n), (0, 0, 0))


# --------------------------TEST--------------------------
# main :: IO ()
def main():
    '''Size of each sub-class of integers drawn from [1..20000]:'''

    print(main.__doc__)
    print(
        '\n'.join(map(
            lambda a, b: a.rjust(10) + ' -> ' + str(b),
            ['Deficient', 'Perfect', 'Abundant'],
            deficientPerfectAbundantCountsUpTo(20000)
        ))
    )


# ------------------------GENERIC-------------------------

# primeFactors :: Int -> [Int]
def primeFactors(n):
    '''A list of the prime factors of n.
    '''
    def f(qr):
        r = qr[1]
        return step(r), 1 + r

    def step(x):
        return 1 + (x << 2) - ((x >> 1) << 1)

    def go(x):
        root = floor(sqrt(x))

        def p(qr):
            q = qr[0]
            return root < q or 0 == (x % q)

        q = until(p)(f)(
            (2 if 0 == x % 2 else 3, 1)
        )[0]
        return [x] if q > root else [q] + go(x // q)

    return go(n)


# properDivisors :: Int -> [Int]
def properDivisors(n):
    '''The ordered divisors of n, excluding n itself.
    '''
    def go(a, x):
        return [a * b for a, b in product(
            a,
            accumulate(chain([1], x), mul)
        )]
    return sorted(
        reduce(go, [
            list(g) for _, g in groupby(primeFactors(n))
        ], [1])
    )[:-1] if 1 < n else []


# succ :: Int -> Int
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
# nthArrow :: (a -> b) -> Tuple -> Int -> Tuple
def nthArrow(f):
    '''A simple function lifted to one which applies to a
       tuple, transforming only its nth value.
    '''
    def go(v, n):
        m = n - 1
        return v if n > len(v) else [
            x if m != i else f(x) for i, x in enumerate(v)
        ]
    return lambda tpl: lambda n: tuple(go(tpl, n))

```

### python_code_4.txt
```python
# deficientPerfectAbundantCountsUpTo :: Int -> (Int, Int, Int)
def deficientPerfectAbundantCountsUpTo(n):
    '''Counts of deficient, perfect, and abundant
       integers in the range [1..n].
    '''
    def go(dpa, x):
        divisorSum = sum(properDivisors(x))
        return nthArrow(succ)(dpa)(
            1 if x > divisorSum else (
                3 if x < divisorSum else 2
            )
        )
    return reduce(go, range(1, 1 + n), (0, 0, 0))

```

### python_code_5.txt
```python
pn = 0
an = 0
dn = 0
tt = []
num = 20000
for n in range(1, num+1):
	for x in range(1,1+n//2):
		if n%x == 0:
			tt.append(x)
	if sum(tt) == n:
		pn += 1
	elif sum(tt) > n:
		an += 1
	elif sum(tt) < n:
		dn += 1
	tt = []

print(str(pn) + " Perfect Numbers")
print(str(an) + " Abundant Numbers")
print(str(dn) + " Deficient Numbers")

```

### python_code_6.txt
```python
from time import time
st = time()
pn, an, dn = 0, 0, 0
tt = []
num = 20000
for n in range(1, num + 1):
	for x in range(1, 1 + n // 2):
		if n % x == 0: tt.append(x)
	if sum(tt) == n: pn += 1
	elif sum(tt) > n: an += 1
	elif sum(tt) < n: dn += 1
	tt = []
et1 = time() - st
print(str(pn) + " Perfect Numbers")
print(str(an) + " Abundant Numbers")
print(str(dn) + " Deficient Numbers")
print(et1, "sec\n")

st = time()
pn, an, dn = 0, 0, 1
sum = 1
r = 1
num = 20000
for n in range(2, num + 1):
	d = r * r - n
	if d < 0: r += 1
	for x in range(2, r):
		if n % x == 0: sum += x + n // x
	if d == 0: sum += r
	if sum == n: pn += 1
	elif sum > n: an += 1
	elif sum < n: dn += 1
	sum = 1
et2 = time() - st
print(str(pn) + " Perfect Numbers")
print(str(an) + " Abundant Numbers")
print(str(dn) + " Deficient Numbers")
print(et2 * 1000, "ms\n")
print (et1 / et2,"times faster")

```

