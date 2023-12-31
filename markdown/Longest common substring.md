# Longest common substring

## Task Link
[Rosetta Code - Longest common substring](https://rosettacode.org/wiki/Longest_common_substring)

## Java Code
### java_code_1.txt
```java
public class LongestCommonSubstring {

    public static void main(String[] args) {
        System.out.println(lcs("testing123testing", "thisisatest"));
        System.out.println(lcs("test", "thisisatest"));
        System.out.println(lcs("testing", "sting"));
        System.out.println(lcs("testing", "thisisasting"));
    }

    static String lcs(String a, String b) {
        if (a.length() > b.length())
            return lcs(b, a);

        String res = "";
        for (int ai = 0; ai < a.length(); ai++) {
            for (int len = a.length() - ai; len > 0; len--) {

                for (int bi = 0; bi <= b.length() - len; bi++) {

                    if (a.regionMatches(ai, b, bi, len) && len > res.length()) {
                        res = a.substring(ai, ai + len);
                    }
                }
            }
        }
        return res;
    }
}

```

## Python Code
### python_code_1.txt
```python
s1 = "thisisatest"
s2 = "testing123testing"
len1, len2 = len(s1), len(s2)
ir, jr = 0, -1
for i1 in range(len1):
    i2 = s2.find(s1[i1])
    while i2 >= 0:
        j1, j2 = i1, i2
        while j1 < len1 and j2 < len2 and s2[j2] == s1[j1]:
            if j1-i1 >= jr-ir:
                ir, jr = i1, j1
            j1 += 1; j2 += 1
        i2 = s2.find(s1[i1], i2+1)
print (s1[ir:jr+1])

```

### python_code_2.txt
```python
def _set_of_substrings(s:str) -> set:
    "_set_of_substrings('ABBA') == {'A', 'AB', 'ABB', 'ABBA', 'B', 'BA', 'BB', 'BBA'}"
    len_s = len(s)
    return {s[m: n] for m in range(len_s) for n in range(m+1, len_s +1)}

def _set_of_common_substrings(s:str, common: set) -> set:
    "Substrings of s that are also in common"
    len_s = len(s)
    return {this for m in range(len_s) for n in range(m+1, len_s +1)
            if (this := s[m:n]) in common}

def lcs_ss(*strings):
    "longest of the common substrings of all substrings of each string"
    strings_iter  = (s for s in strings)
    common = _set_of_substrings(next(strings_iter)) # First string substrings
    for s in strings_iter:
        if not common:
            break
        common = _set_of_common_substrings(s, common) # Accumulate the common

    return max(common, key= lambda x: len(x)) if common else ''


s0 = "thisisatest_stinger"
s1 = "testing123testingthing"
s2 = "thisis"

ans = lcs_ss(s0, s1)
print(f"\n{repr(s0)}, {repr(s1)} ->> {repr(ans)}")
ans = lcs_ss(s0, s2)
print(f"\n{repr(s0)}, {repr(s2)} ->> {repr(ans)}")
ans = lcs_ss(s1, s2)
print(f"\n{repr(s1)}, {repr(s2)} ->> {repr(ans)}")
ans = lcs_ss(s0, s1, s2)
print(f"\n{repr(s0)}, {repr(s1)}, {repr(s2)} ->> {repr(ans)}")

```

### python_code_3.txt
```python
'''Longest common substring'''

from itertools import accumulate, chain
from functools import reduce


# longestCommon :: String -> String -> String
def longestCommon(s1):
    '''The longest common substring of
       two given strings.
    '''
    def go(s2):
        return max(intersect(
            *map(lambda s: map(
                concat,
                concatMap(tails)(
                    compose(tail, list, inits)(s)
                )
            ), [s1, s2])
        ), key=len)
    return go


# ------------------------- TEST -------------------------
def main():
    '''Test'''
    print(
        longestCommon(
            "testing123testing"
        )(
            "thisisatest"
        )
    )


# ----------------------- GENERIC ------------------------

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


# concat :: [String] -> String
def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.
    '''
    return ''.join(xs)


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been
       mapped.
       The list monad can be derived by using a function f
       which wraps its output in a list, (using an empty
       list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# inits :: [a] -> [[a]]
def inits(xs):
    '''all initial segments of xs, shortest first.'''
    return accumulate(chain([[]], xs), lambda a, x: a + [x])


# intersect :: [a] -> [a] -> [a]
def intersect(xs, ys):
    '''The ordered intersection of xs and ys.
       intersect([1,2,2,3,4])([6,4,4,2]) -> [2,2,4]
    '''
    s = set(ys)
    return (x for x in xs if x in s)


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but defines a succession of
       intermediate values, building from the left.
    '''
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go


# tail :: [a] -> [a]
# tail :: Gen [a] -> [a]
def tail(xs):
    '''The elements following the head of a
       (non-empty) list.
    '''
    return xs[1:]


# tails :: [a] -> [[a]]
def tails(xs):
    '''All final segments of xs,
       longest first.
    '''
    return [
        xs[i:] for i in
        range(0, 1 + len(xs))
    ]


# MAIN ---
main()

```

