# 4-rings or 4-squares puzzle

## Task Link
[Rosetta Code - 4-rings or 4-squares puzzle](https://rosettacode.org/wiki/4-rings_or_4-squares_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class FourSquares {
    public static void main(String[] args) {
        fourSquare(1, 7, true, true);
        fourSquare(3, 9, true, true);
        fourSquare(0, 9, false, false);
    }

    private static void fourSquare(int low, int high, boolean unique, boolean print) {
        int count = 0;

        if (print) {
            System.out.println("a b c d e f g");
        }
        for (int a = low; a <= high; ++a) {
            for (int b = low; b <= high; ++b) {
                if (notValid(unique, a, b)) continue;

                int fp = a + b;
                for (int c = low; c <= high; ++c) {
                    if (notValid(unique, c, a, b)) continue;
                    for (int d = low; d <= high; ++d) {
                        if (notValid(unique, d, a, b, c)) continue;
                        if (fp != b + c + d) continue;

                        for (int e = low; e <= high; ++e) {
                            if (notValid(unique, e, a, b, c, d)) continue;
                            for (int f = low; f <= high; ++f) {
                                if (notValid(unique, f, a, b, c, d, e)) continue;
                                if (fp != d + e + f) continue;

                                for (int g = low; g <= high; ++g) {
                                    if (notValid(unique, g, a, b, c, d, e, f)) continue;
                                    if (fp != f + g) continue;

                                    ++count;
                                    if (print) {
                                        System.out.printf("%d %d %d %d %d %d %d%n", a, b, c, d, e, f, g);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        if (unique) {
            System.out.printf("There are %d unique solutions in [%d, %d]%n", count, low, high);
        } else {
            System.out.printf("There are %d non-unique solutions in [%d, %d]%n", count, low, high);
        }
    }

    private static boolean notValid(boolean unique, int needle, int... haystack) {
        return unique && Arrays.stream(haystack).anyMatch(p -> p == needle);
    }
}

```

## Python Code
### python_code_1.txt
```python
import itertools

def all_equal(a,b,c,d,e,f,g):
    return a+b == b+c+d == d+e+f == f+g

def foursquares(lo,hi,unique,show):
    solutions = 0
    if unique:
        uorn = "unique"
        citer = itertools.combinations(range(lo,hi+1),7)
    else:
        uorn = "non-unique"
        citer =  itertools.combinations_with_replacement(range(lo,hi+1),7)
                    
    for c in citer:
            for p in set(itertools.permutations(c)):
                if all_equal(*p):
                    solutions += 1
                    if show:
                        print str(p)[1:-1]

    print str(solutions)+" "+uorn+" solutions in "+str(lo)+" to "+str(hi)
    print

```

### python_code_2.txt
```python
def foursquares(lo,hi,unique,show):

    def acd_iter():
        """
        Iterates through all the possible valid values of 
        a, c, and d.
        
        a = c + d
        """
        for c in range(lo,hi+1):
            for d in range(lo,hi+1):
                if (not unique) or (c <> d):
                    a = c + d
                    if a >= lo and a <= hi:
                        if (not unique) or (c <> 0 and d <> 0):
                            yield (a,c,d)
                            
    def ge_iter():
        """
        Iterates through all the possible valid values of 
        g and e.
        
        g = d + e
        """
        for e in range(lo,hi+1):
            if (not unique) or (e not in (a,c,d)):
                g = d + e
                if g >= lo and g <= hi:
                    if (not unique) or (g not in (a,c,d,e)):
                        yield (g,e)
                        
    def bf_iter():
        """
        Iterates through all the possible valid values of 
        b and f.
        
        b = e + f - c
        """
        for f in range(lo,hi+1):
            if (not unique) or (f not in (a,c,d,g,e)):
                b = e + f - c
                if b >= lo and b <= hi:
                    if (not unique) or (b not in (a,c,d,g,e,f)):
                        yield (b,f)

    solutions = 0                    
    acd_itr = acd_iter()              
    for acd in acd_itr:
        a,c,d = acd
        ge_itr = ge_iter()
        for ge in ge_itr:
            g,e = ge
            bf_itr = bf_iter()
            for bf in bf_itr:
                b,f = bf
                solutions += 1
                if show:
                    print str((a,b,c,d,e,f,g))[1:-1]
    if unique:
        uorn = "unique"
    else:
        uorn = "non-unique"
               
    print str(solutions)+" "+uorn+" solutions in "+str(lo)+" to "+str(hi)
    print

```

### python_code_3.txt
```python
'''4-rings or 4-squares puzzle'''

from itertools import chain


# rings :: noRepeatedDigits -> DigitList -> Lists of solutions
# rings :: Bool -> [Int] -> [[Int]]
def rings(uniq):
    '''Sets of unique or non-unique integer values
       (drawn from the `digits` argument)
       for each of the seven names [a..g] such that:
       (a + b) == (b + c + d) == (d + e + f) == (f + g)
    '''
    def go(digits):
        ns = sorted(digits, reverse=True)
        h = ns[0]

        # CENTRAL DIGIT :: d
        def central(d):
            xs = list(filter(lambda x: h >= (d + x), ns))

            # LEFT NEIGHBOUR AND LEFTMOST :: c and a
            def left(c):
                a = c + d
                if a > h:
                    return []
                else:
                    # RIGHT NEIGHBOUR AND RIGHTMOST :: e and g
                    def right(e):
                        g = d + e
                        if ((g > h) or (uniq and (g == c))):
                            return []
                        else:
                            agDelta = a - g
                            bfs = difference(ns)(
                                [d, c, e, g, a]
                            ) if uniq else ns

                            # MID LEFT AND RIGHT :: b and f
                            def midLeftRight(b):
                                f = b + agDelta
                                return [[a, b, c, d, e, f, g]] if (
                                    (f in bfs) and (
                                        (not uniq) or (
                                            f not in [a, b, c, d, e, g]
                                        )
                                    )
                                ) else []

    # CANDIDATE DIGITS BOUND TO POSITIONS [a .. g] --------

                            return concatMap(midLeftRight)(bfs)

                    return concatMap(right)(
                        difference(xs)([d, c, a]) if uniq else ns
                    )

            return concatMap(left)(
                delete(d)(xs) if uniq else ns
            )

        return concatMap(central)(ns)

    return lambda digits: go(digits) if digits else []


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Testing unique digits [1..7], [3..9] and unrestricted digits'''

    print(main.__doc__ + ':\n')
    print(unlines(map(
        lambda tpl: '\nrings' + repr(tpl) + ':\n\n' + unlines(
            map(repr, uncurry(rings)(*tpl))
        ), [
            (True, enumFromTo(1)(7)),
            (True, enumFromTo(3)(9))
        ]
    )))
    tpl = (False, enumFromTo(0)(9))
    print(
        '\n\nlen(rings' + repr(tpl) + '):\n\n' +
        str(len(uncurry(rings)(*tpl)))
    )


# GENERIC -------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# delete :: Eq a => a -> [a] -> [a]
def delete(x):
    '''xs with the first of any instances of x removed.'''
    def go(xs):
        xs.remove(x)
        return xs
    return lambda xs: go(list(xs)) if (
        x in xs
    ) else list(xs)


#  difference :: Eq a => [a] -> [a] -> [a]
def difference(xs):
    '''All elements of ys except any also found in xs'''
    def go(ys):
        s = set(ys)
        return [x for x in xs if x not in s]
    return lambda ys: go(ys)


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a pair of arguments,
       derived from a vanilla or curried function.
    '''
    return lambda x, y: f(x)(y)


# unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

