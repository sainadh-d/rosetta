# Largest number divisible by its digits

## Task Link
[Rosetta Code - Largest number divisible by its digits](https://rosettacode.org/wiki/Largest_number_divisible_by_its_digits)

## Java Code
### java_code_1.txt
```java
public class LynchBell {
    
    static String s = "";
    
    public static void main(String args[]) {
        //Highest number with unique digits (no 0 or 5)
        int i = 98764321;
        boolean isUnique = true;
        boolean canBeDivided = true;
        while (i>0) {
            s = String.valueOf(i);
            isUnique = uniqueDigits(i);
            if (isUnique) {
                //Number has unique digits
                canBeDivided = testNumber(i);
                if(canBeDivided) {
                    System.out.println("Number found: " + i);
                    i=0;
                }
            }
            i--;
        }
    }
    
    public static boolean uniqueDigits(int i) {
        //returns true, if unique digits, false otherwise
        for (int k = 0; k<s.length();k++) {
            for(int l=k+1; l<s.length();l++) {
                if(s.charAt(l)=='0' || s.charAt(l)=='5') {
                    //0 or 5 is a digit
                    return false;
                }
                if(s.charAt(k) == s.charAt(l)) {
                    //non-unique digit
                    return false;
                }
            }
        }
        return true;
    }
    
    public static boolean testNumber(int i) {
        //Tests, if i is divisible by all its digits (0 is not a digit already)
        int j = 0;
        boolean divisible = true;
        // TODO: divisible by all its digits 
        for (char ch: s.toCharArray()) {
            j = Character.getNumericValue(ch);
            divisible = ((i%j)==0);
            if (!divisible) {
                return false;
            }
        }       
        return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
'''Largest number divisible by its digits'''

from itertools import (chain, permutations)
from functools import (reduce)
from math import (gcd)


# main :: IO ()
def main():
    '''Tests'''

    # (Division by zero is not an option, so 0 and 5 are omitted)
    digits = [1, 2, 3, 4, 6, 7, 8, 9]

    # Least common multiple of the digits above
    lcmDigits = reduce(lcm, digits)

    # Any 7 items drawn from the digits above,
    # including any two of [1, 4, 7]
    sevenDigits = ((delete)(digits)(x) for x in [1, 4, 7])

    print(
        max(
            (
                intFromDigits(x) for x
                in concatMap(permutations)(sevenDigits)
            ),
            key=lambda n: n if 0 == n % lcmDigits else 0
        )
    )


# intFromDigits :: [Int] -> Int
def intFromDigits(xs):
    '''An integer derived from an
       ordered list of digits.
    '''
    return reduce(lambda a, x: a * 10 + x, xs, 0)


# ----------------------- GENERIC ------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been
       mapped. The list monad can be derived by using a
       function f which wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# delete :: Eq a => [a] -> a -> [a]
def delete(xs):
    '''xs with the first instance of
       x removed.
    '''
    def go(x):
        ys = xs.copy()
        ys.remove(x)
        return ys
    return go


# lcm :: Int -> Int -> Int
def lcm(x, y):
    '''The smallest positive integer divisible
       without remainder by both x and y.
    '''
    return 0 if (0 == x or 0 == y) else abs(
        y * (x // gcd(x, y))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
'''Largest number divisible by its hex digits'''

from functools import (reduce)
from math import (gcd)


# main :: IO ()
def main():
    '''First integer evenly divisible by each of its
       hex digits, none of which appear more than once.
    '''

    # Least common multiple of digits [1..15]
    # ( -> 360360 )
    lcmDigits = foldl1(lcm)(
        enumFromTo(1)(15)
    )
    allDigits = 0xfedcba987654321

    # ( -> 1147797409030632360 )
    upperLimit = allDigits - (allDigits % lcmDigits)

    # Possible numbers
    xs = enumFromThenToNext(upperLimit)(
        upperLimit - lcmDigits
    )(1)

    print(
        hex(
            until(lambda x: 15 == len(set(showHex(x))))(
                lambda _: next(xs)
            )(next(xs))
        )
    )   # --> 0xfedcb59726a1348


# ------------------ GENERIC FUNCTIONS -------------------

# enumFromThenToNext :: Int -> Int -> Int -> Gen [Int]
def enumFromThenToNext(m):
    '''Non-finite series of integer values enumerated
       from m to n with a step size defined by nxt-m.
    '''
    def go(m, nxt):
        d = nxt - m
        v = m
        while True:
            yield v
            v = d + v
    return lambda nxt: lambda n: go(m, nxt)


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


# foldl1 :: (a -> a -> a) -> [a] -> a
def foldl1(f):
    '''Left to right reduction of the
       non-empty list xs, using the binary
       operator f, with the head of xs
       as the initial acccumulator value.
    '''
    return lambda xs: reduce(
        lambda a, x: f(a)(x), xs[1:], xs[0]
    ) if xs else None


# lcm :: Int -> Int -> Int
def lcm(x):
    '''The smallest positive integer divisible
       without remainder by both x and y.
    '''
    return lambda y: (
        0 if (0 == x or 0 == y) else abs(
            y * (x // gcd(x, y))
        )
    )


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


# showHex :: Int -> String
def showHex(n):
    '''Hexadecimal string representation
       of an integer value.
    '''
    return hex(n)[2:]


# MAIN --
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
from time import time
st = time()
stp = 9 * 8 * 7
for n in range((9876312 // stp) * stp, 0, -stp):
    s = str(n)
    if "0" in s or "5" in s or len(set(s)) < len(s): continue
    print("Base 10 =", n, "in %.3f" % (1e6 * (time() - st)), "μs");
    break;
st = time()
stp = 15 * 14 * 13 * 12 * 11
for n in range((0xfedcba976543218 // stp) * stp, 0, -stp):
    s = hex(n)[2:]
    if "0" in s or len(set(s)) < len(s): continue
    print("Base 16 =", hex(n), "in %.3f" % (1e3 * (time() - st)), end = "ms")
    break;

```

