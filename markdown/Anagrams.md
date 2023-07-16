# Anagrams

## Task Link
[Rosetta Code - Anagrams](https://rosettacode.org/wiki/Anagrams)

## Java Code
### java_code_1.txt
```java
import java.net.*;
import java.io.*;
import java.util.*;
 
public class WordsOfEqChars {
    public static void main(String[] args) throws IOException {
        URL url = new URL("http://wiki.puzzlers.org/pub/wordlists/unixdict.txt");
        InputStreamReader isr = new InputStreamReader(url.openStream());
        BufferedReader reader = new BufferedReader(isr);

        Map<String, Collection<String>> anagrams = new HashMap<String, Collection<String>>();
        String word;
        int count = 0;
        while ((word = reader.readLine()) != null) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (!anagrams.containsKey(key))
                anagrams.put(key, new ArrayList<String>());
            anagrams.get(key).add(word);
            count = Math.max(count, anagrams.get(key).size());
        }

        reader.close();

        for (Collection<String> ana : anagrams.values())
            if (ana.size() >= count)
                System.out.println(ana);
    }   
}

```

### java_code_2.txt
```java
import java.net.*;
import java.io.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;

public interface Anagram {
  public static <AUTOCLOSEABLE extends AutoCloseable, OUTPUT> Supplier<OUTPUT> tryWithResources(Callable<AUTOCLOSEABLE> callable, Function<AUTOCLOSEABLE, Supplier<OUTPUT>> function, Supplier<OUTPUT> defaultSupplier) {
    return () -> {
      try (AUTOCLOSEABLE autoCloseable = callable.call()) {
        return function.apply(autoCloseable).get();
      } catch (Throwable throwable) {
        return defaultSupplier.get();
      }
    };
  }

  public static <INPUT, OUTPUT> Function<INPUT, OUTPUT> function(Supplier<OUTPUT> supplier) {
    return i -> supplier.get();
  }

  public static void main(String... args) {
    Map<String, Collection<String>> anagrams = new ConcurrentSkipListMap<>();
    int count = tryWithResources(
      () -> new BufferedReader(
        new InputStreamReader(
          new URL(
            "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt"
          ).openStream()
        )
      ),
      reader -> () -> reader.lines()
        .parallel()
        .mapToInt(word -> {
          char[] chars = word.toCharArray();
          Arrays.parallelSort(chars);
          String key = Arrays.toString(chars);
          Collection<String> collection = anagrams.computeIfAbsent(
            key, function(ArrayList::new)
          );
          collection.add(word);
          return collection.size();
        })
        .max()
        .orElse(0),
      () -> 0
    ).get();
    anagrams.values().stream()
      .filter(ana -> ana.size() >= count)
      .forEach(System.out::println)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> import urllib.request
>>> from collections import defaultdict
>>> words = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
>>> anagram = defaultdict(list) # map sorted chars to anagrams
>>> for word in words:
	anagram[tuple(sorted(word))].append( word )

	
>>> count = max(len(ana) for ana in anagram.values())
>>> for ana in anagram.values():
	if len(ana) >= count:
		print ([x.decode() for x in ana])

```

### python_code_2.txt
```python
>>> import urllib
>>> from collections import defaultdict
>>> words = urllib.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
>>> len(words)
25104
>>> anagram = defaultdict(list) # map sorted chars to anagrams
>>> for word in words:
	anagram[tuple(sorted(word))].append( word )

	
>>> count = max(len(ana) for ana in anagram.itervalues())
>>> for ana in anagram.itervalues():
	if len(ana) >= count:
		print ana

		
['angel', 'angle', 'galen', 'glean', 'lange']
['alger', 'glare', 'lager', 'large', 'regal']
['caret', 'carte', 'cater', 'crate', 'trace']
['evil', 'levi', 'live', 'veil', 'vile']
['elan', 'lane', 'lean', 'lena', 'neal']
['abel', 'able', 'bale', 'bela', 'elba']
>>> count
5
>>>

```

### python_code_3.txt
```python
>>> import urllib, itertools
>>> words = urllib.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
>>> len(words)
25104
>>> anagrams = [list(g) for k,g in itertools.groupby(sorted(words, key=sorted), key=sorted)]


>>> count = max(len(ana) for ana in anagrams)
>>> for ana in anagrams:
	if len(ana) >= count:
		print ana

		
['abel', 'able', 'bale', 'bela', 'elba']
['caret', 'carte', 'cater', 'crate', 'trace']
['angel', 'angle', 'galen', 'glean', 'lange']
['alger', 'glare', 'lager', 'large', 'regal']
['elan', 'lane', 'lean', 'lena', 'neal']
['evil', 'levi', 'live', 'veil', 'vile']
>>> count
5
>>>

```

### python_code_4.txt
```python
'''Largest anagram groups found in list of words.'''

from os.path import expanduser
from itertools import groupby
from operator import eq


# main :: IO ()
def main():
    '''Largest anagram groups in local unixdict.txt'''

    print(unlines(
        largestAnagramGroups(
            lines(readFile('unixdict.txt'))
        )
    ))


# largestAnagramGroups :: [String] -> [[String]]
def largestAnagramGroups(ws):
    '''A list of the anagram groups of
       of the largest size found in a
       given list of words.
    '''

    # wordChars :: String -> (String, String)
    def wordChars(w):
        '''A word paired with its
           AZ sorted characters
        '''
        return (''.join(sorted(w)), w)

    groups = list(map(
        compose(list)(snd),
        groupby(
            sorted(
                map(wordChars, ws),
                key=fst
            ),
            key=fst
        )
    ))

    intMax = max(map(len, groups))
    return list(map(
        compose(unwords)(curry(map)(snd)),
        filter(compose(curry(eq)(intMax))(len), groups)
    ))


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# lines :: String -> [String]
def lines(s):
    '''A list of strings,
       (containing no newline characters)
       derived from a single new-line delimited string.'''
    return s.splitlines()


# from os.path import expanduser
# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
       derived by expanding any ~ in fp.'''
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from
       a list of words.'''
    return ' '.join(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

