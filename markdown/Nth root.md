# Nth root

## Task Link
[Rosetta Code - Nth root](https://rosettacode.org/wiki/Nth_root)

## Java Code
### java_code_1.txt
```java
public static double nthroot(int n, double A) {
	return nthroot(n, A, .001);
}
public static double nthroot(int n, double A, double p) {
	if(A < 0) {
		System.err.println("A < 0");// we handle only real positive numbers
		return -1;
	} else if(A == 0) {
		return 0;
	}
	double x_prev = A;
	double x = A / n;  // starting "guessed" value...
	while(Math.abs(x - x_prev) > p) {
		x_prev = x;
		x = ((n - 1.0) * x + A / Math.pow(x, n - 1.0)) / n;
	}
	return x;
}

```

### java_code_2.txt
```java
public static double nthroot(int n, double x) {
  assert (n > 1 && x > 0);
  int np = n - 1;
  double g1 = x;
  double g2 = iter(g1, np, n, x);
  while (g1 != g2) {
    g1 = iter(g1, np, n, x);
    g2 = iter(iter(g2, np, n, x), np, n, x);
  }
  return g1;
}

private static double iter(double g, int np, int n, double x) {
  return (np * g + x / Math.pow(g, np)) / n;
}

```

## Python Code
### python_code_1.txt
```python
from decimal import Decimal, getcontext

def nthroot (n, A, precision):
    getcontext().prec = precision
    
    n = Decimal(n)
    x_0 = A / n #step 1: make a while guess.
    x_1 = 1     #need it to exist before step 2
    while True:
        #step 2:
        x_0, x_1 = x_1, (1 / n)*((n - 1)*x_0 + (A / (x_0 ** (n - 1))))
        if x_0 == x_1:
            return x_1

```

### python_code_2.txt
```python
print nthroot(5, 34, 10)
print nthroot(10,42, 20)
print nthroot(2, 5, 400)

```

### python_code_3.txt
```python
'''Nth Root'''

from decimal import Decimal, getcontext
from operator import eq


# nthRoot :: Int -> Int -> Int -> Real
def nthRoot(precision):
    '''The nth root of x at the given precision.'''
    def go(n, x):
        getcontext().prec = precision
        dcn = Decimal(n)

        def same(ab):
            return eq(*ab)

        def step(ab):
            a, b = ab
            predn = pred(dcn)
            return (
                b,
                reciprocal(dcn) * (
                    predn * a + (
                        x / (a ** predn)
                    )
                )
            )
        return until(same)(step)(
            (x / dcn, 1)
        )[0]
    return lambda n: lambda x: go(n, x)


# --------------------------TEST---------------------------
def main():
    '''Nth roots at various precisions'''

    def xShow(tpl):
        p, n, x = tpl
        return rootName(n) + (
            ' of ' + str(x) + ' at precision ' + str(p)
        )

    def f(tpl):
        p, n, x = tpl
        return nthRoot(p)(n)(x)

    print(
        fTable(main.__doc__ + ':\n')(xShow)(str)(f)(
            [(10, 5, 34), (20, 10, 42), (30, 2, 5)]
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

# rootName :: Int -> String
def rootName(n):
    '''English ordinal suffix.'''
    return ['identity', 'square root', 'cube root'][n - 1] if (
        4 > n or 1 > n
    ) else (str(n) + 'th root')


# pred ::  Enum a => a -> a
def pred(x):
    '''The predecessor of a value. For numeric types, (- 1).'''
    return x - 1


# reciprocal :: Num -> Num
def reciprocal(x):
    '''Arithmetic reciprocal of x.'''
    return 1 / x


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


if __name__ == '__main__':
    main()

```

