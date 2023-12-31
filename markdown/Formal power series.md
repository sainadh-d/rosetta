# Formal power series

## Task Link
[Rosetta Code - Formal power series](https://rosettacode.org/wiki/Formal_power_series)

## Java Code
## Python Code
### python_code_1.txt
```python
''' \
For a discussion on pipe() and head() see
  http://paddy3118.blogspot.com/2009/05/pipe-fitting-with-python-generators.html
'''

from itertools import islice
from fractions import Fraction
from functools import reduce
try:
    from itertools import izip as zip # for 2.6
except:
    pass

def head(n):
    ''' return a generator that passes through at most n items
    '''
    return lambda seq: islice(seq, n)

def pipe(gen, *cmds):
    ''' pipe(a,b,c,d, ...) -> yield from ...d(c(b(a)))
    '''
    return reduce(lambda gen, cmd: cmd(gen), cmds, gen)

def sinepower():
    n = 0
    fac = 1
    sign = +1
    zero = 0
    yield zero
    while True:
        n +=1
        fac *= n
        yield Fraction(1, fac*sign)
        sign = -sign
        n +=1
        fac *= n
        yield zero
def cosinepower():
    n = 0
    fac = 1
    sign = +1
    yield Fraction(1,fac)
    zero = 0
    while True:
        n +=1
        fac *= n
        yield zero
        sign = -sign
        n +=1
        fac *= n
        yield Fraction(1, fac*sign)
def pluspower(*powergenerators):
    for elements in zip(*powergenerators):
        yield sum(elements)
def minuspower(*powergenerators):
    for elements in zip(*powergenerators):
        yield elements[0] - sum(elements[1:])
def mulpower(fgen,ggen):
    'From: http://en.wikipedia.org/wiki/Power_series#Multiplication_and_division'
    a,b = [],[]
    for f,g in zip(fgen, ggen):
        a.append(f)
        b.append(g)
        yield sum(f*g for f,g in zip(a, reversed(b)))
def constpower(n):
    yield n
    while True:
        yield 0
def diffpower(gen):
    'differentiatiate power series'
    next(gen)
    for n, an in enumerate(gen, start=1):
        yield an*n
def intgpower(k=0):
    'integrate power series with constant k'
    def _intgpower(gen):
        yield k
        for n, an in enumerate(gen, start=1):
            yield an * Fraction(1,n)
    return _intgpower


print("cosine")
c = list(pipe(cosinepower(), head(10)))
print(c)
print("sine")
s = list(pipe(sinepower(), head(10)))
print(s)
# integrate cosine
integc = list(pipe(cosinepower(),intgpower(0), head(10)))
# 1 - (integrate sine)
integs1 = list(minuspower(pipe(constpower(1), head(10)),
                          pipe(sinepower(),intgpower(0), head(10))))

assert s == integc, "The integral of cos should be sin"
assert c == integs1, "1 minus the integral of sin should be cos"

```

### python_code_2.txt
```python
from itertools import islice, tee
from fractions import Fraction
try:
    from itertools import izip as zip # for 2.6
except:
    pass

def pluspower(*powergenerators):
    for elements in zip(*powergenerators):
        yield sum(elements)
def minuspower(*powergenerators):
    for elements in zip(*powergenerators):
        yield elements[0] - sum(elements[1:])
def mulpower(fgen,ggen):
    'From: http://en.wikipedia.org/wiki/Power_series#Multiplication_and_division'
    a,b = [],[]
    for f,g in zip(fgen, ggen):
        a.append(f)
        b.append(g)
        yield sum(f*g for f,g in zip(a, reversed(b)))
def constpower(n):
    yield n
    while True:
        yield 0
def diffpower(gen):
    'differentiatiate power series'
    next(gen)
    for n, an in enumerate(gen, start=1):
        yield an*n
def intgpower(gen):
    'integrate power series with bounds from 0 to x'
    yield 0
    for n, an in enumerate(gen, start=1):
        yield an * Fraction(1,n)


def sine_cosine_series():
    def deferred_sin():
        for i in sinx_temp:
            yield i
    def deferred_cos():
        for i in cosx_temp:
            yield i

    sinx_result, sinx_copy1 = tee(deferred_sin(), 2)
    cosx_result, cosx_copy1 = tee(deferred_cos(), 2)

    sinx_temp = intgpower(cosx_copy1)
    cosx_temp = minuspower(constpower(1), intgpower(sinx_copy1))

    return sinx_result, cosx_result

sinx, cosx = sine_cosine_series()

print("cosine")
print(list(islice(sinx, 10)))
print("sine")
print(list(islice(cosx, 10)))

```

### python_code_3.txt
```python
from itertools import count, chain, tee, islice, cycle
from fractions import Fraction

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
            (a,b) = tee(s.gen, 2)
            s.gen = a
            self.gen = b

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
            return Poly(Fraction(x, b) for x in a)

        a, b = Poly(a), Poly(b)
        def gen():
            r, bb = a,next(b)
            while True:
                aa = next(r)
                q = Fraction(aa, bb)
                yield(q)
                r -= q*b

        return Poly(gen())

# these two would probably be better as class methods
def inte(a):
    def gen():
        yield(0)
        for (x,n) in zip(a, count(1)):
            yield(Fraction(x,n))
    return Poly(gen())

def diff(a):
    def gen():
        for (x, n) in zip(a, count(0)):
            if n: yield(x*n)
    return Poly(gen())


# all that for the syntactic sugar
sinx, cosx, tanx, expx = Poly(), Poly(), Poly(), Poly()

sinx << inte(cosx)
cosx << 1 - inte(sinx)
tanx << sinx / cosx        # "=" would also work here
expx << 1 + inte(expx)

for n,x in zip(("sin", "cos", "tan", "exp"), (sinx, cosx, tanx, expx)):
    print(n, ', '.join(map(str, list(islice(x, 10)))))

```

