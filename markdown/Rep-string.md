# Rep-string

## Task Link
[Rosetta Code - Rep-string](https://rosettacode.org/wiki/Rep-string)

## Java Code
### java_code_1.txt
```java
public class RepString {

    static final String[] input = {"1001110011", "1110111011", "0010010010",
        "1010101010", "1111111111", "0100101101", "0100100", "101", "11",
        "00", "1", "0100101"};

    public static void main(String[] args) {
        for (String s : input)
            System.out.printf("%s : %s%n", s, repString(s));
    }

    static String repString(String s) {
        int len = s.length();
        outer:
        for (int part = len / 2; part > 0; part--) {
            int tail = len % part;
            if (tail > 0 && !s.substring(0, tail).equals(s.substring(len - tail)))
                continue;
            for (int j = 0; j < len / part - 1; j++) {
                int a = j * part;
                int b = (j + 1) * part;
                int c = (j + 2) * part;
                if (!s.substring(a, b).equals(s.substring(b, c)))
                    continue outer;
            }
            return s.substring(0, part);
        }
        return "none";
    }
}

```

## Python Code
### python_code_1.txt
```python
def is_repeated(text):
    'check if the first part of the string is repeated throughout the string'
    for x in range(len(text)//2, 0, -1):
        if text.startswith(text[x:]): return x
    return 0

matchstr = """\
1001110011
1110111011
0010010010
1010101010
1111111111
0100101101
0100100
101
11
00
1
"""
for line in matchstr.split():
    ln = is_repeated(line)
    print('%r has a repetition length of %i i.e. %s' 
           % (line, ln, repr(line[:ln]) if ln else '*not* a rep-string'))

```

### python_code_2.txt
```python
>>> def reps(text):
    return [text[:x] for x in range(1, 1 + len(text) // 2)
            if text.startswith(text[x:])]

>>> matchstr = """\
1001110011
1110111011
0010010010
1010101010
1111111111
0100101101
0100100
101
11
00
1
"""
>>> print('\n'.join('%r has reps %r' % (line, reps(line)) for line in matchstr.split()))
'1001110011' has reps ['10011']
'1110111011' has reps ['1110']
'0010010010' has reps ['001']
'1010101010' has reps ['10', '1010']
'1111111111' has reps ['1', '11', '111', '1111', '11111']
'0100101101' has reps []
'0100100' has reps ['010']
'101' has reps []
'11' has reps ['1']
'00' has reps ['0']
'1' has reps []
>>>

```

### python_code_3.txt
```python
'''Rep-strings'''

from itertools import (accumulate, chain, cycle, islice)


# repCycles :: String -> [String]
def repCycles(s):
    '''Repeated sequences of characters in s.'''
    n = len(s)
    cs = list(s)

    return [
        x for x in
        tail(inits(take(n // 2)(s)))
        if cs == take(n)(cycle(x))
    ]


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests - longest cycle (if any) in each string.'''
    print(
        fTable('Longest cycles:\n')(repr)(
            lambda xs: ''.join(xs[-1]) if xs else '(none)'
        )(repCycles)([
            '1001110011',
            '1110111011',
            '0010010010',
            '1010101010',
            '1111111111',
            '0100101101',
            '0100100',
            '101',
            '11',
            '00',
            '1',
        ])
    )


# GENERIC -------------------------------------------------

# inits :: [a] -> [[a]]
def inits(xs):
    '''all initial segments of xs, shortest first.'''
    return accumulate(chain([[]], xs), lambda a, x: a + [x])


# tail :: [a] -> [a]
# tail :: Gen [a] -> [a]
def tail(xs):
    '''The elements following the head of a
       (non-empty) list or generator stream.'''
    if isinstance(xs, list):
        return xs[1:]
    else:
        list(islice(xs, 1))  # First item dropped.
        return xs


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# OUTPUT FORMATTING ---------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
                 fx display function ->
          f -> value list -> tabular string.
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

### python_code_4.txt
```python
import re

matchstr = """\
1001110011
1110111011
0010010010
1010101010
1111111111
0100101101
0100100
101
11
00
1"""

def _checker(matchobj):
    g0, (g1, g2, g3, g4) = matchobj.group(0), matchobj.groups()
    if not g4 and g1 and g1.startswith(g3):
        return '%r repeats %r' % (g0, g1)
    return '%r is not a rep-string' % (g0,)

def checkit(txt):
    print(re.sub(r'(.+)(\1+)(.*)|(.*)', _checker, txt))

checkit(matchstr)

```

