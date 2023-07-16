# Proper divisors

## Task Link
[Rosetta Code - Proper divisors](https://rosettacode.org/wiki/Proper_divisors)

## Java Code
### java_code_1.txt
```java
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Proper{
    public static List<Integer> properDivs(int n){
        List<Integer> divs = new LinkedList<Integer>();
        if(n == 1) return divs;
        divs.add(1);
        for(int x = 2; x < n; x++){
            if(n % x == 0) divs.add(x);
        }
        
        Collections.sort(divs);
        
        return divs;
    }
    
    public static void main(String[] args){
        for(int x = 1; x <= 10; x++){
            System.out.println(x + ": " + properDivs(x));
        }
        
        int x = 0, count = 0;
        for(int n = 1; n <= 20000; n++){
            if(properDivs(n).size() > count){
                x = n;
                count = properDivs(n).size();
            }
        }
        System.out.println(x + ": " + count);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def proper_divs2(n):
...     return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}
... 
>>> [proper_divs2(n) for n in range(1, 11)]
[set(), {1}, {1}, {1, 2}, {1}, {1, 2, 3}, {1}, {1, 2, 4}, {1, 3}, {1, 2, 5}]
>>> 
>>> n, length = max(((n, len(proper_divs2(n))) for n in range(1, 20001)), key=lambda pd: pd[1])
>>> n
15120
>>> length
79
>>>

```

### python_code_2.txt
```python
from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product


MUL = int.__mul__


def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)

@lru_cache(maxsize=None)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]


def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())


if __name__ == '__main__':
    rangemax = 20000
    
    print([proper_divs(n) for n in range(1, 11)])
    print(*max(((n, len(proper_divs(n))) for n in range(1, 20001)), key=lambda pd: pd[1]))

```

### python_code_3.txt
```python
'''Proper divisors'''

from itertools import accumulate, chain, groupby, product
from functools import reduce
from math import floor, sqrt
from operator import mul


# properDivisors :: Int -> [Int]
def properDivisors(n):
    '''The ordered divisors of n, excluding n itself.
    '''
    def go(a, group):
        return [x * y for x, y in product(
            a,
            accumulate(chain([1], group), mul)
        )]
    return sorted(
        reduce(go, [
            list(g) for _, g in groupby(primeFactors(n))
        ], [1])
    )[:-1] if 1 < n else []


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Tests'''

    print(
        fTable('Proper divisors of [1..10]:')(str)(str)(
            properDivisors
        )(range(1, 1 + 10))
    )

    print('\nExample of maximum divisor count in the range [1..20000]:')
    print(
        max(
            [(n, len(properDivisors(n))) for n in range(1, 1 + 20000)],
            key=snd
        )
    )


# -------------------------DISPLAY-------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# -------------------------GENERIC-------------------------

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


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


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

### python_code_4.txt
```python
def pd(num):
	factors = []
	for divisor in range(1,1+num//2):
		if num % divisor == 0: factors.append(divisor)
	return factors

def pdc(num):
	count = 0
	for divisor in range(1,1+num//2):
		if num % divisor == 0: count += 1
	return count

def fmtres(title, lmt, best, bestc):
	return "The " + title + " number up to and including " + str(lmt) + " with the highest number of proper divisors is " + str(best) + ", which has " + str(bestc)

def showcount(limit):
	best, bestc, bh, bhc = 0, 0, 0, 0
	for i in range(limit+1):
		divc = pdc(i)
		if divc > bestc: bestc, best = divc, i
		if divc >= bhc: bhc, bh = divc, i
	if best == bh:
		print(fmtres("only", limit, best, bestc))
	else:
		print(fmtres("lowest", limit, best, bestc))
		print(fmtres("highest", limit, bh, bhc))
	print()

lmt = 10
for i in range(1, lmt + 1):
	divs = pd(i)
	if len(divs) == 0:
		print("There are no proper divisors of", i)
	elif len(divs) == 1:
		print(divs[0], "is the only proper divisor of", i)
	else:
		print(divs, "are the proper divisors of", i)
print()
showcount(20000)
showcount(25000)

```

