# Next highest int from digits

## Task Link
[Rosetta Code - Next highest int from digits](https://rosettacode.org/wiki/Next_highest_int_from_digits)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class NextHighestIntFromDigits {

    public static void main(String[] args) {
        for ( String s : new String[] {"0", "9", "12", "21", "12453", "738440", "45072010", "95322020", "9589776899767587796600", "3345333"} ) {
            System.out.printf("%s -> %s%n", format(s), format(next(s)));
        }
        testAll("12345");
        testAll("11122");
    }

    private static NumberFormat FORMAT = NumberFormat.getNumberInstance();
    
    private static String format(String s) {
        return FORMAT.format(new BigInteger(s));
    }

    private static void testAll(String s) {
        System.out.printf("Test all permutations of:  %s%n", s);
        String sOrig = s;
        String sPrev = s;
        int count = 1;
        
        //  Check permutation order.  Each is greater than the last
        boolean orderOk = true;
        Map <String,Integer> uniqueMap = new HashMap<>();
        uniqueMap.put(s, 1);
        while ( (s = next(s)).compareTo("0") != 0 ) {
            count++;
            if ( Long.parseLong(s) < Long.parseLong(sPrev) ) {
                orderOk = false;
            }
            uniqueMap.merge(s, 1, (v1, v2) -> v1 + v2);
            sPrev = s;
        }
        System.out.printf("    Order:  OK =  %b%n", orderOk);

        //  Test last permutation
        String reverse = new StringBuilder(sOrig).reverse().toString();
        System.out.printf("    Last permutation:  Actual = %s, Expected = %s, OK = %b%n", sPrev, reverse, sPrev.compareTo(reverse) == 0);

        //  Check permutations unique
        boolean unique = true;
        for ( String key : uniqueMap.keySet() ) {
            if ( uniqueMap.get(key) > 1 ) {
                unique = false;
            }
        }
        System.out.printf("    Permutations unique:  OK =  %b%n", unique);
        
        //  Check expected count.
        Map<Character,Integer> charMap = new HashMap<>();
        for ( char c : sOrig.toCharArray() ) {
            charMap.merge(c, 1, (v1, v2) -> v1 + v2);
        }
        long permCount = factorial(sOrig.length());
        for ( char c : charMap.keySet() ) {
            permCount /= factorial(charMap.get(c));
        }
        System.out.printf("    Permutation count:  Actual = %d, Expected = %d, OK = %b%n", count, permCount, count == permCount);
        

    }
    
    private static long factorial(long n) {
        long fact = 1;
        for (long num = 2 ; num <= n ; num++ ) {
            fact *= num;
        }
        return fact;
    }
    
    private static String next(String s) {
        StringBuilder sb = new StringBuilder();
        int index = s.length()-1;
        //  Scan right-to-left through the digits of the number until you find a digit with a larger digit somewhere to the right of it.
        while ( index > 0 && s.charAt(index-1) >= s.charAt(index)) {
            index--;
        }
        //  Reached beginning.  No next number.
        if ( index == 0 ) {
            return "0";
        }

        //  Find digit on the right that is both more than it, and closest to it.
        int index2 = index;
        for ( int i = index + 1 ; i < s.length() ; i++ ) {
            if ( s.charAt(i) < s.charAt(index2) && s.charAt(i) > s.charAt(index-1) ) {
                index2 = i;
            }
        }
        
        //  Found data, now build string
        //  Beginning of String
        if ( index > 1 ) {
            sb.append(s.subSequence(0, index-1));
        }

        //  Append found, place next
        sb.append(s.charAt(index2));
        
        //  Get remaining characters
        List<Character> chars = new ArrayList<>();
        chars.add(s.charAt(index-1));
        for ( int i = index ; i < s.length() ; i++ ) {
            if ( i != index2 ) {
                chars.add(s.charAt(i));
            }
        }
        
        //  Order the digits to the right of this position, after the swap; lowest-to-highest, left-to-right.
        Collections.sort(chars);
        for ( char c : chars ) {
            sb.append(c);
        }
        return sb.toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
def closest_more_than(n, lst):
    "(index of) closest int from lst, to n that is also > n"
    large = max(lst) + 1
    return lst.index(min(lst, key=lambda x: (large if x <= n else x)))

def nexthigh(n):
    "Return nxt highest number from n's digits using scan & re-order"
    assert n == int(abs(n)), "n >= 0"
    this = list(int(digit) for digit in str(int(n)))[::-1]
    mx = this[0]
    for i, digit in enumerate(this[1:], 1):
        if digit < mx:
            mx_index = closest_more_than(digit, this[:i + 1])
            this[mx_index], this[i] = this[i], this[mx_index]
            this[:i] = sorted(this[:i], reverse=True)
            return int(''.join(str(d) for d in this[::-1]))
        elif digit > mx:
            mx, mx_index = digit, i
    return 0


if __name__ == '__main__':
    for x in [0, 9, 12, 21, 12453, 738440, 45072010, 95322020,
              9589776899767587796600]:
        print(f"{x:>12_d} -> {nexthigh(x):>12_d}")

```

### python_code_2.txt
```python
from itertools import permutations


def nexthigh(n):
    "Return next highest number from n's digits using search of all digit perms"
    assert n == int(abs(n)), "n >= 0"
    this = tuple(str(int(n)))
    perms = sorted(permutations(this))
    for perm in perms[perms.index(this):]:
        if perm != this:
            return int(''.join(perm))
    return 0

```

### python_code_3.txt
```python
'''Next highest int from digits'''

from itertools import chain, islice, permutations, tee


# --------------- LAZY STREAM OF SUCCESSORS ----------------

# digitShuffleSuccessors :: Int -> [Int]
def digitShuffleSuccessors(n):
    '''Iterator stream of all digit-shuffle
       successors of n, where 0 <= n.
    '''
    def go(ds):
        delta = int(''.join(ds)) - n
        return [] if 0 >= delta else [delta]
    return map(
        add(n),
        sorted(
            set(concatMap(go)(
                permutations(str(n))
            ))
        )
    )


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Taking up to 5 digit-shuffle successors for each:'''

    def showSuccs(n):
        def go(xs):
            ys, zs = tee(xs)
            harvest = take(n)(ys)
            return (
                repr(len(harvest)) + ' of ' + (
                    repr(len(list(zs))) + ':  '
                )
            ).rjust(12, ' ') + repr(harvest)
        return go

    print(
        fTable(main.__doc__ + '\n')(str)(showSuccs(5))(
            digitShuffleSuccessors
        )([
            0,
            9,
            12,
            21,
            12453,
            738440,
            45072010,
            95322020
        ])
    )


# ------------------------ GENERIC -------------------------

# add (+) :: Num a => a -> a -> a
def add(a):
    '''Curried addition.'''
    def go(b):
        return a + b
    return go


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''The concatenation of a mapping.
       The list monad can be derived by using a function f
       which wraps its output in a list, using an empty
       list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> 
       fx display function -> f -> xs -> tabular string.
    '''
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + (
                            ' -> ' + fxShow(f(x))
                        )
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox


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


# MAIN ---
if __name__ == '__main__':
    main()

```

