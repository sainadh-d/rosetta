# Least common multiple

## Task Link
[Rosetta Code - Least common multiple](https://rosettacode.org/wiki/Least_common_multiple)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class LCM{
   public static void main(String[] args){
      Scanner aScanner = new Scanner(System.in);
   
      //prompts user for values to find the LCM for, then saves them to m and n
      System.out.print("Enter the value of m:");
      int m = aScanner.nextInt();
      System.out.print("Enter the value of n:");
      int n = aScanner.nextInt();
      int lcm = (n == m || n == 1) ? m :(m == 1 ? n : 0);
      /* this section increases the value of mm until it is greater  
      / than or equal to nn, then does it again when the lesser 
      / becomes the greater--if they aren't equal. If either value is 1,
      / no need to calculate*/
      if (lcm == 0) {
         int mm = m, nn = n;
         while (mm != nn) {
             while (mm < nn) { mm += m; }
             while (nn < mm) { nn += n; }
         }  
         lcm = mm;
      }
      System.out.println("lcm(" + m + ", " + n + ") = " + lcm);
   }
}

```

## Python Code
### python_code_1.txt
```python
>>> import fractions
>>> def lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0

>>> lcm(12, 18)
36
>>> lcm(-6, 14)
42
>>> assert lcm(0, 2) == lcm(2, 0) == 0
>>>

```

### python_code_2.txt
```python
'''Least common multiple'''

from inspect import signature


# lcm :: Int -> Int -> Int
def lcm(x):
    '''The smallest positive integer divisible
       without remainder by both x and y.
    '''
    return lambda y: 0 if 0 in (x, y) else abs(
        y * (x // gcd_(x)(y))
    )


# gcd_ :: Int -> Int -> Int
def gcd_(x):
    '''The greatest common divisor in terms of
       the divisibility preordering.
    '''
    def go(a, b):
        return go(b, a % b) if 0 != b else a
    return lambda y: go(abs(x), abs(y))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    print(
        fTable(
            __doc__ + 's of 60 and [12..20]:'
        )(repr)(repr)(
            lcm(60)
        )(enumFromTo(12)(20))
    )

    pairs = [(0, 2), (2, 0), (-6, 14), (12, 18)]
    print(
        fTable(
            '\n\n' + __doc__ + 's of ' + repr(pairs) + ':'
        )(repr)(repr)(
            uncurry(lcm)
        )(pairs)
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple, derived from
       a vanilla or curried function.
    '''
    if 1 < len(signature(f).parameters):
        return lambda xy: f(*xy)
    else:
        return lambda xy: f(xy[0])(xy[1])


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# FORMATTING ----------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
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


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
from prime_decomposition import decompose
try:
    reduce
except NameError:
    from functools import reduce
    
def lcm(a, b):
    mul = int.__mul__
    if a and b:
        da = list(decompose(abs(a)))
        db = list(decompose(abs(b)))
        merge= da
        for d in da:
            if d in db: db.remove(d)
        merge += db
        return reduce(mul, merge, 1)
    return 0
 
if __name__ == '__main__':
    print( lcm(12, 18) )    # 36
    print( lcm(-6, 14) )    # 42
    assert lcm(0, 2) == lcm(2, 0) == 0

```

### python_code_4.txt
```python
>>> def lcm(*values):
	values = set([abs(int(v)) for v in values])
	if values and 0 not in values:
		n = n0 = max(values)
		values.remove(n)
		while any( n % m for m in values ):
			n += n0
		return n
	return 0

>>> lcm(-6, 14)
42
>>> lcm(2, 0)
0
>>> lcm(12, 18)
36
>>> lcm(12, 18, 22)
396
>>>

```

### python_code_5.txt
```python
>>> def lcm(p,q):
	p, q = abs(p), abs(q)
	m = p * q
	if not m: return 0
	while True:
		p %= q
		if not p: return m // q
		q %= p
		if not q: return m // p

		
>>> lcm(-6, 14)
42
>>> lcm(12, 18)
36
>>> lcm(2, 0)
0
>>>

```

