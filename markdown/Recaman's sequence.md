# Recaman's sequence

## Task Link
[Rosetta Code - Recaman's sequence](https://rosettacode.org/wiki/Recaman%27s_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class RecamanSequence {
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>();
        a.add(0);

        Set<Integer> used = new HashSet<>();
        used.add(0);

        Set<Integer> used1000 = new HashSet<>();
        used1000.add(0);

        boolean foundDup = false;
        int n = 1;
        while (n <= 15 || !foundDup || used1000.size() < 1001) {
            int next = a.get(n - 1) - n;
            if (next < 1 || used.contains(next)) {
                next += 2 * n;
            }
            boolean alreadyUsed = used.contains(next);
            a.add(next);
            if (!alreadyUsed) {
                used.add(next);
                if (0 <= next && next <= 1000) {
                    used1000.add(next);
                }
            }
            if (n == 14) {
                System.out.printf("The first 15 terms of the Recaman sequence are : %s\n", a);
            }
            if (!foundDup && alreadyUsed) {
                System.out.printf("The first duplicate term is a[%d] = %d\n", n, next);
                foundDup = true;
            }
            if (used1000.size() == 1001) {
                System.out.printf("Terms up to a[%d] are needed to generate 0 to 1000\n", n);
            }
            n++;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

class Recamans():
    "Recamán's sequence generator callable class"
    def __init__(self):
        self.a = None   # Set of results so far
        self.n = None   # n'th term (counting from zero)
    
    def __call__(self):
        "Recamán's sequence  generator"
        nxt = 0
        a, n = {nxt}, 0
        self.a = a
        self.n = n
        yield nxt
        while True:
            an1, n = nxt, n + 1
            nxt = an1 - n
            if nxt < 0 or nxt in a:
                nxt = an1 + n
            a.add(nxt)
            self.n = n
            yield nxt

if __name__ == '__main__':
    recamans = Recamans()
    print("First fifteen members of Recamans sequence:", 
          list(islice(recamans(), 15)))

    so_far = set()
    for term in recamans():
        if term in so_far:
            print(f"First duplicate number in series is: a({recamans.n}) = {term}")
            break
        so_far.add(term)
    
    n = 1_000
    setn = set(range(n + 1))    # The target set of numbers to be covered
    for _ in recamans():
        if setn.issubset(recamans.a):
            print(f"Range 0 ..{n} is covered by terms up to a({recamans.n})")
            break

```

### python_code_2.txt
```python
'''Recaman sequence'''


# recamanUntil :: (Int -> Set Int > [Int] -> Bool) -> [Int]
def recamanUntil(p):
    '''All terms of the Recaman series before the
       first term for which the predicate p holds.'''
    n = 1
    r = 0  # First term of series
    rs = [r]
    seen = set(rs)
    blnNew = True
    while not p(seen, n, r, blnNew):
        r = recamanSucc(seen, n, r)
        blnNew = r not in seen
        seen.add(r)
        rs.append(r)
        n = 1 + n
    return rs


# recamanSucc :: Set Int -> Int -> Int
def recamanSucc(seen, n, r):
    '''The successor for a given Recaman term,
       given the set of Recaman terms seen so far.'''
    back = r - n
    return n + r if 0 > back or (back in seen) else back


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Test'''
    print(
        'First 15 Recaman:\r',
        recamanUntil(
            lambda seen, n, r, _: 15 == n
        )
    )
    print(
        'First duplicated Recaman:\r',
        recamanUntil(
            lambda seen, n, r, blnNew: not blnNew
        )[-1]
    )
    setK = set(enumFromTo(0)(1000))
    print(
        'Number of Recaman terms needed to generate',
        'all integers from [0..1000]:\r',
        len(recamanUntil(
            lambda seen, n, r, blnNew: (
                blnNew and 1001 > r and setK.issubset(seen)
            )
        )) - 1
    )


# ----------------------- GENERIC ------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''Recaman by iteration of a function over a tuple.'''

from itertools import (islice)


# recamanTupleSucc :: Set Int -> (Int, Int, Bool) -> (Int, Int, Bool)
def recamanTupleSucc(seen):
    '''The Nth in a series of Recaman tuples,
       (N, previous term, boolPreviouslySeen?)
       given the set of all terms seen so far.'''
    def go(n, r, _):
        back = r - n
        nxt = n + r if 0 > back or (back in seen) else back
        bln = nxt in seen
        seen.add(nxt)
        return (1 + n, nxt, bln)
    return lambda tpl: go(*tpl)


# ------------------------- TEST -------------------------
# main :: IO()
def main():
    '''First 15, and first duplicated Recaman.'''
    f = recamanTupleSucc(set([0]))
    print(
        'First 15 Recaman:\n',
        list(map(
            snd,
            take(15)(iterate(f)((1, 0, False)))
        ))
    )
    f = recamanTupleSucc(set([0]))
    print(
        'First duplicated Recaman:\n',
        until(lambda x: x[2])(f)(
            (1, 0, False)
        )[1]
    )

    sk = set(enumFromTo(0)(1000))
    sr = set([0])
    f = recamanTupleSucc(sr)
    print(
        'Number of Recaman terms needed to generate',
        'all integers from [0..1000]:\n',
        until(
            lambda x: not x[2] and 1001 > x[1] and sk.issubset(sr)
        )(f)(
            (1, 0, False)
        )[0] - 1
    )


# ----------------- GENERIC ABSTRACTIONS -----------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


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


# snd :: (a, b) -> b
def snd(tpl):
    '''Second component of a tuple.'''
    return tpl[1]


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else islice(xs, n)
    )


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


# MAIN ---
if __name__ == '__main__':
    main()

```

