# Semordnilap

## Task Link
[Rosetta Code - Semordnilap](https://rosettacode.org/wiki/Semordnilap)

## Java Code
### java_code_1.txt
```java
import java.nio.file.*;
import java.util.*;

public class Semordnilap {

    public static void main(String[] args) throws Exception {
        List<String> lst = Files.readAllLines(Paths.get("unixdict.txt"));
        Set<String> seen = new HashSet<>();
        int count = 0;
        for (String w : lst) {
            w = w.toLowerCase();
            String r = new StringBuilder(w).reverse().toString();
            if (seen.contains(r)) {
                if (count++ < 5)
                    System.out.printf("%-10s %-10s\n", w, r);
            } else seen.add(w);
        }
        System.out.println("\nSemordnilap pairs found: " + count);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> with open('unixdict.txt') as f:
	wordset = set(f.read().strip().split())

>>> revlist = (''.join(word[::-1]) for word in wordset)
>>> pairs   = set((word, rev) for word, rev in zip(wordset, revlist) 
                  if word < rev and rev in wordset)
>>> len(pairs)
158
>>> sorted(pairs, key=lambda p: (len(p[0]), p))[-5:]
[('damon', 'nomad'), ('lager', 'regal'), ('leper', 'repel'), ('lever', 'revel'), ('kramer', 'remark')]
>>>

```

### python_code_2.txt
```python
'''Dictionary words paired by equivalence under reversal'''

from functools import (reduce)
from itertools import (chain)
import urllib.request


# semordnilaps :: [String] -> [String]
def semordnilaps(xs):
    '''The subset of words in a list which
       are paired (by equivalence under reversal)
       with other words in that list.
    '''
    def go(tpl, w):
        (s, ws) = tpl
        if w[::-1] in s:
            return (s, ws + [w])
        else:
            s.add(w)
            return (s, ws)
    return reduce(go, xs, (set(), []))[1]


# TEST ----------------------------------------------------
def main():
    '''Test'''

    url = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
    ws = semordnilaps(
        urllib.request.urlopen(
            url
        ).read().splitlines()
    )
    print(
        fTable(
            __doc__ + ':\n\n(longest of ' +
            str(len(ws)) + ' in ' + url + ')\n'
        )(snd)(fst)(identity)(
            sorted(
                concatMap(
                    lambda x: (
                        lambda s=x.decode('utf8'): [
                            (s, s[::-1])
                        ] if 4 < len(x) else []
                    )()
                )(ws),
                key=compose(len)(fst),
                reverse=True
            )
        )
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# FORMATTING ----------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
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


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import sys
import random
import requests
 
URL = 'http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'
 
 
def find_semordnilaps(word_generator):
 
  # Keys in this dict are the words seen so far, reversed.
  # Values are booleans determining whether we have seen (and yielded)
  # the key, so that we don't yield the same word twice.
  seen = {}
 
  for word in word_generator:
    if word not in seen:
      reversed_word = word[::-1]
      seen[reversed_word] = False  # not yielded yet
    else:
      yielded_already = seen[word]
      if not yielded_already:
        yield word
        seen[word] = True  # the word has been yielded
 
 
def url_lines(url):
  with requests.get(url, stream=True) as req:
    yield from req.iter_lines(decode_unicode=True)
 
 
def main(url=URL, num_of_examples=5):
 
  semordnilaps_generator = find_semordnilaps(url_lines(url))
 
  semordnilaps = list(semordnilaps_generator)
 
  example_words = random.choices(semordnilaps, k=int(num_of_examples))
  example_pairs = ((word, word[::-1]) for word in example_words)
 
  print(
    f'found {len(semordnilaps)} semordnilap words:',
    * ['%s %s' % p for p in example_pairs]+['...'],
    sep='\n'
  )
 
  return semordnilaps
 
 
if __name__ == '__main__':
  main(*sys.argv[1:])

```

