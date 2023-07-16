# Palindromic gapful numbers

## Task Link
[Rosetta Code - Palindromic gapful numbers](https://rosettacode.org/wiki/Palindromic_gapful_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PalindromicGapfulNumbers {

    public static void main(String[] args) {
        System.out.println("First 20 palindromic gapful numbers ending in:");
        displayMap(getPalindromicGapfulEnding(20, 20));

        System.out.printf("%nLast 15 of first 100 palindromic gapful numbers ending in:%n");
        displayMap(getPalindromicGapfulEnding(15, 100));

        System.out.printf("%nLast 10 of first 1000 palindromic gapful numbers ending in:%n");
        displayMap(getPalindromicGapfulEnding(10, 1000));
    }
    
    private static void displayMap(Map<Integer,List<Long>> map) {
        for ( int key = 1 ; key <= 9 ; key++ ) {
            System.out.println(key + " : " + map.get(key));
        }
    }
    
    public static Map<Integer,List<Long>> getPalindromicGapfulEnding(int countReturned, int firstHowMany) {
        Map<Integer,List<Long>> map = new HashMap<>();
        Map<Integer,Integer> mapCount = new HashMap<>();
        for ( int i = 1 ; i <= 9 ; i++ ) {
            map.put(i, new ArrayList<>());
            mapCount.put(i, 0);
        }
        boolean notPopulated = true;
        for ( long n = 101 ; notPopulated ; n = nextPalindrome(n) ) {
            if ( isGapful(n) ) {
                int index = (int) (n % 10);
                if ( mapCount.get(index) < firstHowMany ) {
                    map.get(index).add(n);
                    mapCount.put(index, mapCount.get(index) + 1);
                    if ( map.get(index).size() > countReturned ) {
                        map.get(index).remove(0);
                    }
                }
                boolean finished = true;
                for ( int i = 1 ; i <= 9 ; i++ ) {
                    if ( mapCount.get(i) < firstHowMany ) {
                        finished = false;
                        break;
                    }
                }
                if ( finished ) {
                    notPopulated = false;
                }
            }
        }
        return map;
    }
    
    public static boolean isGapful(long n) {
        String s = Long.toString(n);
        return n % Long.parseLong("" + s.charAt(0) + s.charAt(s.length()-1)) == 0;
    }
    
    public static int length(long n) {
        int length = 0;
        while ( n > 0 ) {
            length += 1;
            n /= 10;
        }
        return length;
    }
    
    public static long nextPalindrome(long n) {
        int length = length(n);
        if ( length % 2 == 0 ) {
            length /= 2;
            while ( length > 0 ) {
                n /= 10;
                length--;
            }
            n += 1;
            if ( powerTen(n) ) {
                return Long.parseLong(n + reverse(n/10));
            }
            return Long.parseLong(n + reverse(n));
        }
        length = (length - 1) / 2;
        while ( length > 0 ) {
            n /= 10;
            length--;
        }
        n += 1;
        if ( powerTen(n) ) {
            return Long.parseLong(n + reverse(n/100));
        }
        return Long.parseLong(n + reverse(n/10));
    }
    
    private static boolean powerTen(long n) {
        while ( n > 9 && n % 10 == 0 ) {
            n /= 10;
        }
        return n == 1;
    }
        
    private static String reverse(long n) {
        return (new StringBuilder(n + "")).reverse().toString();
    }

}

```

## Python Code
### python_code_1.txt
```python
from itertools import count
from pprint import pformat
import re
import heapq


def pal_part_gen(odd=True):
    for i in count(1):
        fwd = str(i)
        rev = fwd[::-1][1:] if odd else fwd[::-1]
        yield int(fwd + rev)

def pal_ordered_gen():
    yield from heapq.merge(pal_part_gen(odd=True), pal_part_gen(odd=False))

def is_gapful(x):
    return (x % (int(str(x)[0]) * 10 + (x % 10)) == 0)

if __name__ == '__main__':
    start = 100
    for mx, last in [(20, 20), (100, 15), (1_000, 10)]:
        print(f"\nLast {last} of the first {mx} binned-by-last digit " 
              f"gapful numbers >= {start}")
        bin = {i: [] for i in range(1, 10)}
        gen = (i for i in pal_ordered_gen() if i >= start and is_gapful(i))
        while any(len(val) < mx for val in bin.values()):
            g = next(gen)
            val = bin[g % 10]
            if len(val) < mx:
                val.append(g)
        b = {k:v[-last:] for k, v in bin.items()}
        txt = pformat(b, width=220)
        print('', re.sub(r"[{},\[\]]", '', txt))

```

### python_code_2.txt
```python
'''Palindromic gapful numbers'''

from itertools import chain, count, islice, tee
from functools import reduce


# palindromicGapfuls :: () -> [Int]
def palindromicGapfuls():
    '''A non-finite series of gapful palindromic numbers.
    '''
    def derived(digitsEven):
        '''A palindrome of an even or odd number of digits,
           obtained by appending either all or just the tail
           of the reversed digits of n.
        '''
        def go(x):
            s = str(x)
            r = s[::-1]
            return int((s + r) if digitsEven else (s + r[1:]))
        return go

    return filter(
        lambda n: 0 == n % (int(str(n)[0]) * 10 + (n % 10)),
        mergeInOrder(
            map(derived(False), count(10))
        )(map(derived(True), count(10)))
    )


# --------------------------TESTS--------------------------
# main :: IO ()
def main():
    '''Various samples of gapful palindromes grouped by final digit.'''

    tpl = tee(palindromicGapfuls(), 9)

    # sample :: (String, Int, Int) -> String
    def sample(label, dropped, taken):
        return fTable(label)(compose(cons(' '), str))(
            compose(unwords, map_(str))
        )(
            compose(
                take(taken),
                drop(dropped),
                lambda i: filter(
                    lambda x: i == x % 10,
                    tpl[i - 1]
                )
            )
        )(enumFromTo(1)(9))

    print(
        '\n\n'.join(map(lambda x: sample(*x), [
            ('First 20 samples of gapful palindromes ' +
             '(> 100) by last digit:', 0, 20),

            ('Last 15 of first 100 gapful palindromes ' +
             '(> 100) by last digit:', 65, 15),

            ('Last 10 of first 1000 gapful palindromes ' +
             '(> 100) by last digit:', 890, 10)
        ]))
    )

# ------------------------DISPLAY -------------------------


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
            lambda x, y: y.rjust(w, ' ') + ': ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# ------------------------GENERIC--------------------------

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
        return lambda x: f(g(x))
    return reduce(go, fs, lambda x: x)


# cons :: a -> [a] -> [a]
def cons(x):
    '''A list string or iterator constructed
       from x as head, and xs as tail.
    '''
    return lambda xs: [x] + xs if (
        isinstance(xs, list)
    ) else x + xs if (
        isinstance(xs, str)
    ) else chain([x], xs)


# drop :: Int -> [a] -> [a]
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        take(n)(xs)
        return xs
    return go


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    def go(n):
        return list(range(m, 1 + n))
    return go


# map :: (a -> b) -> [a] -> [b]
def map_(f):
    '''The list obtained by applying f
       to each element of xs.
    '''
    return lambda xs: [f(x) for x in xs]


# mergeInOrder :: Gen [Int] -> Gen [Int] -> Gen [Int]
def mergeInOrder(ga):
    '''An ordered, non-finite, stream of integers
       obtained by merging two other such streams.
    '''
    def go(ma, mb):
        a = ma
        b = mb
        while not a['Nothing'] and not b['Nothing']:
            (a1, a2) = a['Just']
            (b1, b2) = b['Just']
            if a1 < b1:
                yield a1
                a = uncons(a2)
            else:
                yield b1
                b = uncons(b2)

    return lambda gb: go(uncons(ga), uncons(gb))


# take :: Int -> [a] -> [a]
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: list(islice(xs, n))


# uncons :: [a] -> Maybe (a, [a])
def uncons(xs):
    '''The deconstruction of a non-empty list
       (or generator stream) into two parts:
       a head value, and the remaining values.
    '''
    nxt = take(1)(xs)
    return Just((nxt[0], xs)) if nxt else Nothing()


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived
       from a list of words.
    '''
    return ' '.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

