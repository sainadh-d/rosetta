# Find palindromic numbers in both binary and ternary bases

## Task Link
[Rosetta Code - Find palindromic numbers in both binary and ternary bases](https://rosettacode.org/wiki/Find_palindromic_numbers_in_both_binary_and_ternary_bases)

## Java Code
### java_code_1.txt
```java
public class Pali23 {
	public static boolean isPali(String x){
		return x.equals(new StringBuilder(x).reverse().toString());
	}
	
	public static void main(String[] args){
		
		for(long i = 0, count = 0; count < 6;i++){
			if((i & 1) == 0 && (i != 0)) continue; //skip non-zero evens, nothing that ends in 0 in binary can be in this sequence
			//maybe speed things up through short-circuit evaluation by putting toString in the if
			//testing up to 10M, base 2 has slightly fewer palindromes so do that one first
			if(isPali(Long.toBinaryString(i)) && isPali(Long.toString(i, 3))){
				System.out.println(i + ", " + Long.toBinaryString(i) + ", " + Long.toString(i, 3));
				count++;
			}
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

digits = "0123456789abcdefghijklmnopqrstuvwxyz"

def baseN(num,b):
  if num == 0: return "0"
  result = ""
  while num != 0:
    num, d = divmod(num, b)
    result += digits[d]
  return result[::-1] # reverse

def pal2(num):
    if num == 0 or num == 1: return True
    based = bin(num)[2:]
    return based == based[::-1]

def pal_23():
    yield 0
    yield 1
    n = 1
    while True:
        n += 1
        b = baseN(n, 3)
        revb = b[::-1]
        #if len(b) > 12: break
        for trial in ('{0}{1}'.format(b, revb), '{0}0{1}'.format(b, revb),
                      '{0}1{1}'.format(b, revb), '{0}2{1}'.format(b, revb)):
            t = int(trial, 3)
            if pal2(t):
                yield t

for pal23 in islice(pal_23(), 6):
    print(pal23, baseN(pal23, 3), baseN(pal23, 2))

```

### python_code_2.txt
```python
'''Numbers with palindromic digit strings in both binary and ternary'''

from itertools import (islice)


# palinBoth :: Generator [Int]
def palinBoth():
    '''Non finite stream of dually palindromic integers.'''
    yield 0, '0', '0'
    ibt = 1, '1', '1'

    yield ibt
    while True:
        ibt = until(isBoth)(psucc)(psucc(ibt))
        yield int(ibt[2], 3), ibt[1], ibt[2]


# isBoth :: (Int, String, String) -> Bool
def isBoth(ibt):
    '''True if the binary string is palindromic (as
       the ternary string is already known to be).
    '''
    b = ibt[1]
    return b == b[::-1]


# psucc :: (Int, String, String) -> (Int, String, String)
def psucc(ibt):
    '''The next triple of index, binary
       and (palindromic) ternary string
    '''
    d = 1 + ibt[0]
    s = showBase3(d)
    pal = s + '1' + s[::-1]
    return d, bin(int(pal, 3))[2:], pal


# showBase3 :: Int -> String
def showBase3(n):
    '''Ternary digit string for integer n.'''
    return showIntAtBase(3)(
        lambda i: '012'[i]
    )(n)('')


# ------------------------- TEST -------------------------
def main():
    '''Integers with palindromic digits in
       both binary and ternary bases.
    '''

    xs = take(6)(palinBoth())
    d, b, t = xs[-1]
    bw = len(b)
    tw = len(t)

    print(
        fTable(
            label('rjust')(('Decimal', len(str(d)))) +
            ''.join(map(
                label('center'),
                [('Binary', bw), ('Ternary', tw)]
            )) + '\n'
        )(compose(str)(fst))(
            lambda p: p[1].center(bw, ' ') +
            '    ' + p[2].center(tw, ' ')
        )(identity)(xs)
    )


# ----------------------- GENERIC ------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# showIntAtBase :: Int -> (Int -> String) -> Int -> String -> String
def showIntAtBase(base):
    '''String representation of an integer in a given base,
       using a supplied function for the string representation
       of digits.
    '''
    def wrap(toChr, n, rs):
        def go(nd, r):
            n, d = nd
            r_ = toChr(d) + r
            return go(divmod(n, base), r_) if 0 != n else r_
        return 'unsupported base' if 1 >= base else (
            'negative number' if 0 > n else (
                go(divmod(n, base), rs))
        )
    return lambda toChr: lambda n: lambda rs: (
        wrap(toChr, n, rs)
    )


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f):
        def g(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return g
    return go


# ---------------------- FORMATTING ----------------------

# label :: Method String -> (String, Int)
def label(k):
    '''Stringification, using the named justification
       method (ljust|centre|rjust) of the label,
       and the specified amount of white space.
    '''
    def go(sw):
        s, w = sw
        return getattr(s, k)(w, ' ') + '    '
    return go


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

