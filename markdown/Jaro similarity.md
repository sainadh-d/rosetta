# Jaro similarity

## Task Link
[Rosetta Code - Jaro similarity](https://rosettacode.org/wiki/Jaro_similarity)

## Java Code
### java_code_1.txt
```java
public class JaroDistance {
    public static double jaro(String s, String t) {
        int s_len = s.length();
        int t_len = t.length();

        if (s_len == 0 && t_len == 0) return 1;

        int match_distance = Integer.max(s_len, t_len) / 2 - 1;

        boolean[] s_matches = new boolean[s_len];
        boolean[] t_matches = new boolean[t_len];

        int matches = 0;
        int transpositions = 0;

        for (int i = 0; i < s_len; i++) {
            int start = Integer.max(0, i-match_distance);
            int end = Integer.min(i+match_distance+1, t_len);

            for (int j = start; j < end; j++) {
                if (t_matches[j]) continue;
                if (s.charAt(i) != t.charAt(j)) continue;
                s_matches[i] = true;
                t_matches[j] = true;
                matches++;
                break;
            }
        }

        if (matches == 0) return 0;

        int k = 0;
        for (int i = 0; i < s_len; i++) {
            if (!s_matches[i]) continue;
            while (!t_matches[k]) k++;
            if (s.charAt(i) != t.charAt(k)) transpositions++;
            k++;
        }

        return (((double)matches / s_len) +
                ((double)matches / t_len) +
                (((double)matches - transpositions/2.0) / matches)) / 3.0;
    }

    public static void main(String[] args) {
        System.out.println(jaro(   "MARTHA",      "MARHTA"));
        System.out.println(jaro(    "DIXON",    "DICKSONX"));
        System.out.println(jaro("JELLYFISH",  "SMELLYFISH"));
    }
}

```

## Python Code
### python_code_1.txt
```python
'''Jaro distance'''

from __future__ import division


def jaro(s, t):
    '''Jaro distance between two strings.'''
    s_len = len(s)
    t_len = len(t)

    if s_len == 0 and t_len == 0:
        return 1

    match_distance = (max(s_len, t_len) // 2) - 1

    s_matches = [False] * s_len
    t_matches = [False] * t_len

    matches = 0
    transpositions = 0

    for i in range(s_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, t_len)

        for j in range(start, end):
            if t_matches[j]:
                continue
            if s[i] != t[j]:
                continue
            s_matches[i] = True
            t_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0

    k = 0
    for i in range(s_len):
        if not s_matches[i]:
            continue
        while not t_matches[k]:
            k += 1
        if s[i] != t[k]:
            transpositions += 1
        k += 1

    return ((matches / s_len) +
            (matches / t_len) +
            ((matches - transpositions / 2) / matches)) / 3


def main():
    '''Tests'''

    for s, t in [('MARTHA', 'MARHTA'),
                 ('DIXON', 'DICKSONX'),
                 ('JELLYFISH', 'SMELLYFISH')]:
        print("jaro(%r, %r) = %.10f" % (s, t, jaro(s, t)))


if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
'''Jaro distance between two strings'''

from functools import reduce
import itertools


# --------------------- JARO FUNCTION ----------------------

# jaro :: String -> String -> Float
def jaro(x):
    '''The Jaro distance between two strings.'''
    def go(s1, s2):
        m, t = ap(compose(Tuple, len))(
            transpositionSum
        )(matches(s1, s2))
        return 0 if 0 == m else (
            (1 / 3) * ((m / len(s1)) + (
                m / len(s2)
            ) + ((m - t) / m))
        )
    return lambda y: go(x, y)


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Sample word pairs'''

    print(
        fTable('Jaro distances:\n')(str)(
            showPrecision(3)
        )(
            uncurry(jaro)
        )([
            ("DWAYNE", "DUANE"),
            ("MARTHA", "MARHTA"),
            ("DIXON", "DICKSONX"),
            ("JELLYFISH", "SMELLYFISH")
        ])
    )


# ----------------- JARO HELPER FUNCTIONS ------------------

# transpositionSum :: [(Int, Char)] -> Int
def transpositionSum(xs):
    '''A count of the transpositions in xs.'''
    def f(a, xy):
        x, y = xy
        return 1 + a if fst(x) > fst(y) else a
    return reduce(f, zip(xs, xs[1:]), 0)


# matches :: String -> String -> [(Int, Char)]
def matches(s1, s2):
    '''A list of (Index, Char) correspondences
       between the two strings s1 and s2.'''

    [(_, xs), (l2, ys)] = sorted(map(
        ap(compose(Tuple, len))(list), [s1, s2]
    ))
    r = l2 // 2 - 1

    # match :: (Int, (Char, Int)) -> (Int, Char)
    def match(a, nc):
        n, c = nc
        offset = max(0, n - (1 + r))

        def indexChar(x):
            return a + [(offset + x, c)]

        return maybe(a)(indexChar)(
            elemIndex(c)(
                drop(offset)(take(n + r)(ys))
            )
        )
    return reduce(match, enumerate(xs), [])


# ------------------- GENERIC FUNCTIONS --------------------

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


# Tuple (,) :: a -> b -> (a, b)
def Tuple(x):
    '''Constructor for a pair of values,
       possibly of two different types.
    '''
    def go(y):
        return (
            x + (y,)
        ) if isinstance(x, tuple) else (x, y)
    return go


# ap :: (a -> b -> c) -> (a -> b) -> a -> c
def ap(f):
    '''Applicative instance for functions.
    '''
    def go(g):
        def fxgx(x):
            return f(x)(
                g(x)
            )
        return fxgx
    return go


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


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return go


# elemIndex :: Eq a => a -> [a] -> Maybe Int
def elemIndex(x):
    '''Just the index of the first element in xs
       which is equal to x,
       or Nothing if there is no such element.
    '''
    def go(xs):
        try:
            return Just(xs.index(x))
        except ValueError:
            return Nothing()
    return go


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if (
        None is m or m.get('Nothing')
    ) else f(m.get('Just'))


# showPrecision Int -> Float -> String
def showPrecision(n):
    '''A string showing a floating point number
       at a given degree of precision.'''
    return lambda x: str(round(x, n))


# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
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
    islice = itertools.islice

    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    '''A function over a tuple derived from a curried function.'''
    return lambda xy: f(xy[0])(
        xy[1]
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

