# Selectively replace multiple instances of a character within a string

## Task Link
[Rosetta Code - Selectively replace multiple instances of a character within a string](https://rosettacode.org/wiki/Selectively_replace_multiple_instances_of_a_character_within_a_string)

## Java Code
### java_code_1.txt
```java
int findNth(String s, char c, int n) {
    if (n == 1) return s.indexOf(c);
    return s.indexOf(c, findNth(s, c, n - 1) + 1);
}

String selectiveReplace(String s, Set... ops) {
    char[] chars = s.toCharArray();
    for (Set set : ops)
        chars[findNth(s, set.old, set.n)] = set.rep;
    return new String(chars);
}

record Set(int n, char old, char rep) { }

```

### java_code_2.txt
```java
selectiveReplace("abracadabra",
    new Set(1, 'a', 'A'),
    new Set(2, 'a', 'B'),
    new Set(4, 'a', 'C'),
    new Set(5, 'a', 'D'),
    new Set(1, 'b', 'E'),
    new Set(2, 'r', 'F'));

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict

rep = {'a' : {1 : 'A', 2 : 'B', 4 : 'C', 5 : 'D'}, 'b' : {1 : 'E'}, 'r' : {2 : 'F'}}
 
def trstring(oldstring, repdict):
    seen, newchars = defaultdict(lambda:1, {}), []
    for c in oldstring:
        i = seen[c]
        newchars.append(repdict[c][i] if c in repdict and i in repdict[c] else c)
        seen[c] += 1
    return ''.join(newchars)

print('abracadabra ->', trstring('abracadabra', rep))

```

### python_code_2.txt
```python
import functools

from typing import Iterable
from typing import Tuple


@functools.cache
def find_nth(s: str, sub: str, n: int) -> int:
    assert n >= 1
    if n == 1:
        return s.find(sub)
    return s.find(sub, find_nth(s, sub, n - 1) + 1)


def selective_replace(s: str, ops: Iterable[Tuple[int, str, str]]) -> str:
    chars = list(s)
    for n, old, new in ops:
        chars[find_nth(s, old, n)] = new
    return "".join(chars)


print(
    selective_replace(
        "abracadabra",
        [
            (1, "a", "A"),  # the first 'a' with 'A'
            (2, "a", "B"),  # the second 'a' with 'B'
            (4, "a", "C"),  # the fourth 'a' with 'C'
            (5, "a", "D"),  # the fifth 'a' with 'D'
            (1, "b", "E"),  # the first 'b' with 'E'
            (2, "r", "F"),  # the second 'r' with 'F'
        ],
    )
)

```

### python_code_3.txt
```python
'''Instance-specific character replacement rules'''

from functools import reduce


# nthInstanceReplaced :: Dict Char [(None | Char)] ->
# String -> String
def nthInstanceReplaced(ruleMap):
    def go(a, c):
        ds = a.get(c, None)
        return (
            dict(a, **{c: ds[1:]}),
            ds[0] or c
        ) if ds else (a, c)

    return lambda s: ''.join(
        mapAccumL(go)(ruleMap)(s)[1]
    )


# ------------------------- TEST -------------------------
def main():
    '''Rule-set applied to a given string.'''

    print(
        nthInstanceReplaced({
            'a': ['A', 'B', None, 'C', 'D'],
            'b': ['E'],
            'r': [None, 'F']
        })(
            "abracadabra"
        )
    )


# ----------------------- GENERIC ------------------------

# mapAccumL :: (acc -> x -> (acc, y)) ->
# acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a map
       with accumulation from left to right.
    '''
    def go(a, x):
        return second(lambda v: a[1] + [v])(
            f(a[0], x)
        )
    return lambda acc: lambda xs: reduce(
        go, xs, (acc, [])
    )


# second :: (a -> b) -> ((c, a) -> (c, b))
def second(f):
    '''A simple function lifted to a function over a tuple,
       with f applied only to the second of two values.
    '''
    return lambda xy: (xy[0], f(xy[1]))


# MAIN ---
if __name__ == '__main__':
    main()

```

