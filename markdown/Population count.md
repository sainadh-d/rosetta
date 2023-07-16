# Population count

## Task Link
[Rosetta Code - Population count](https://rosettacode.org/wiki/Population_count)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PopCount {
    public static void main(String[] args) {
	{ // with int
	    System.out.print("32-bit integer: ");
	    int n = 1;
	    for (int i = 0; i < 20; i++) {
		System.out.printf("%d ", Integer.bitCount(n));
		n *= 3;
	    }
	    System.out.println();
	}
	{ // with long
	    System.out.print("64-bit integer: ");
	    long n = 1;
	    for (int i = 0; i < 30; i++) {
		System.out.printf("%d ", Long.bitCount(n));
		n *= 3;
	    }
	    System.out.println();
	}
	{ // with BigInteger
	    System.out.print("big integer   : ");
	    BigInteger n = BigInteger.ONE;
	    BigInteger three = BigInteger.valueOf(3);
	    for (int i = 0; i < 30; i++) {
		System.out.printf("%d ", n.bitCount());
		n = n.multiply(three);
	    }
	    System.out.println();
	}

	int[] od = new int[30];
	int ne = 0, no = 0;
	System.out.print("evil   : ");
	for (int n = 0; ne+no < 60; n++) {
	    if ((Integer.bitCount(n) & 1) == 0) {
		if (ne < 30) {
		    System.out.printf("%d ", n);
		    ne++;
		}
	    } else {
		if (no < 30) {
		    od[no++] = n;
		}
	    }
	}
	System.out.println();
	System.out.print("odious : ");
	for (int n : od) {
	    System.out.printf("%d ", n);
	}
	System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def popcount(n): return bin(n).count("1")
... 
>>> [popcount(3**i) for i in range(30)]
[1, 2, 2, 4, 3, 6, 6, 5, 6, 8, 9, 13, 10, 11, 14, 15, 11, 14, 14, 17, 17, 20, 19, 22, 16, 18, 24, 30, 25, 25]
>>> evil, odious, i = [], [], 0
>>> while len(evil) < 30 or len(odious) < 30:
...     p = popcount(i)
...     if p % 2: odious.append(i)
...     else: evil.append(i)
...     i += 1
... 
>>> evil[:30]
[0, 3, 5, 6, 9, 10, 12, 15, 17, 18, 20, 23, 24, 27, 29, 30, 33, 34, 36, 39, 40, 43, 45, 46, 48, 51, 53, 54, 57, 58]
>>> odious[:30]
[1, 2, 4, 7, 8, 11, 13, 14, 16, 19, 21, 22, 25, 26, 28, 31, 32, 35, 37, 38, 41, 42, 44, 47, 49, 50, 52, 55, 56, 59]
>>>

```

### python_code_2.txt
```python
def pop_kernighan(n):
    i = 0
    while n:
        i, n = i + 1, n & (n - 1)
    return i

```

### python_code_3.txt
```python
'''Population count'''

from functools import reduce


# popCount :: Int -> Int
def popCount(n):
    '''The count of non-zero digits in the binary
       representation of the positive integer n.'''
    def go(x):
        return Just(divmod(x, 2)) if 0 < x else Nothing()
    return sum(unfoldl(go)(n))


# -------------------------- TEST --------------------------
def main():
    '''Tests'''

    print('Population count of first 30 powers of 3:')
    print('    ' + showList(
        [popCount(pow(3, x)) for x in enumFromTo(0)(29)]
    ))

    evilNums, odiousNums = partition(
        compose(even, popCount)
    )(enumFromTo(0)(59))

    print("\nFirst thirty 'evil' numbers:")
    print('    ' + showList(evilNums))

    print("\nFirst thirty 'odious' numbers:")
    print('    ' + showList(odiousNums))


# ------------------------ GENERIC -------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    def go(f, g):
        def fg(x):
            return f(g(x))
        return fg
    return reduce(go, fs, lambda x: x)


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    return lambda n: range(m, 1 + n)


# even :: Int -> Bool
def even(x):
    '''True if x is an integer
       multiple of two.
    '''
    return 0 == x % 2


# partition :: (a -> Bool) -> [a] -> ([a], [a])
def partition(p):
    '''The pair of lists of those elements in xs
       which respectively do, and don't
       satisfy the predicate p.
    '''

    def go(a, x):
        ts, fs = a
        return (ts + [x], fs) if p(x) else (ts, fs + [x])
    return lambda xs: reduce(go, xs, ([], []))


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(repr(x) for x in xs) + ']'


# unfoldl(lambda x: Just(((x - 1), x)) if 0 != x else Nothing())(10)
# -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''Dual to reduce or foldl.
       Where these reduce a list to a summary value, unfoldl
       builds a list from a seed value.
       Where f returns Just(a, b), a is appended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        x, r = v, v
        xs = []
        while True:
            mb = f(x)
            if mb.get('Nothing'):
                return xs
            else:
                x, r = mb.get('Just')
                xs.insert(0, r)
        return xs
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

