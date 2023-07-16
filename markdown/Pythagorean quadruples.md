# Pythagorean quadruples

## Task Link
[Rosetta Code - Pythagorean quadruples](https://rosettacode.org/wiki/Pythagorean_quadruples)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class PythagoreanQuadruples {

    public static void main(String[] args) {
        long d = 2200;
        System.out.printf("Values of d < %d where a, b, and c are non-zero and a^2 + b^2 + c^2 = d^2 has no solutions:%n%s%n", d, getPythagoreanQuadruples(d));
    }

    //  See:  https://oeis.org/A094958
    private static List<Long> getPythagoreanQuadruples(long max) {
        List<Long> list = new ArrayList<>();
        long n = -1;
        long m = -1;
        while ( true ) {
            long nTest = (long) Math.pow(2, n+1);
            long mTest = (long) (5L * Math.pow(2, m+1));
            long test = 0;
            if ( nTest > mTest ) {
                test = mTest;
                m++;
            }
            else {
                test = nTest;
                n++;
            }
            if ( test < max ) {
                list.add(test);
            }
            else {
                break;
            }
        }
        return list;
    }

}

```

## Python Code
### python_code_1.txt
```python
def quad(top=2200):
    r = [False] * top
    ab = [False] * (top * 2)**2
    for a in range(1, top):
        for b in range(a, top):
            ab[a * a + b * b] = True
    s = 3
    for c in range(1, top):
        s1, s, s2 = s, s + 2, s + 2
        for d in range(c + 1, top):
            if ab[s1]:
                r[d] = True
            s1 += s2
            s2 += 2
    return [i for i, val in enumerate(r) if not val and i]
    
if __name__ == '__main__':
    n = 2200
    print(f"Those values of d in 1..{n} that can't be represented: {quad(n)}")

```

### python_code_2.txt
```python
'''Pythagorean Quadruples'''

from itertools import islice, takewhile


# unrepresentables :: () -> [Int]
def unrepresentables():
    '''A non-finite stream of powers of two which can
       not be represented as a Pythagorean quadruple.
    '''
    return merge(
        powersOfTwo()
    )(
        5 * x for x in powersOfTwo()
    )


# powersOfTwo :: Gen [Int]
def powersOfTwo():
    '''A non-finite stream of successive powers of two.
    '''
    def double(x):
        return 2 * x

    return iterate(double)(1)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''For positive integers up to 2,200 (inclusive)
    '''
    def p(x):
        return 2200 >= x

    print(
        list(
            takewhile(p, unrepresentables())
        )
    )


# ----------------------- GENERIC ------------------------

# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


# merge :: Gen [Int] -> Gen [Int] -> Gen [Int]
def merge(ga):
    '''An ordered stream of values drawn from two
       other ordered streams.
    '''
    def go(gb):
        def f(ma, mb):
            a, b = ma, mb
            while a and b:
                ta, tb = a, b
                if ta[0] < tb[0]:
                    yield ta[0]
                    a = uncons(ta[1])
                else:
                    yield tb[0]
                    b = uncons(tb[1])
        return f(uncons(ga), uncons(gb))
    return go


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


# uncons :: [a] -> Maybe (a, [a])
def uncons(xs):
    '''The deconstruction of a non-empty list
       (or generator stream) into two parts:
       a head value, and the remaining values.
    '''
    if isinstance(xs, list):
        return (xs[0], xs[1:]) if xs else None
    else:
        nxt = take(1)(xs)
        return (nxt[0], xs) if nxt else None


# MAIN ---
if __name__ == '__main__':
    main()

```

