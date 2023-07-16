# Letter frequency

## Task Link
[Rosetta Code - Letter frequency](https://rosettacode.org/wiki/Letter_frequency)

## Java Code
### java_code_1.txt
```java
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

```

### java_code_2.txt
```java
public static void main(String[] args) throws IOException {
    Map<Integer, Integer> frequencies = frequencies("src/LetterFrequency.java");
    System.out.println(print(frequencies));
}

static String print(Map<Integer, Integer> frequencies) {
    StringBuilder string = new StringBuilder();
    int key;
    for (Map.Entry<Integer, Integer> entry : frequencies.entrySet()) {
        key = entry.getKey();
        string.append("%,-8d".formatted(entry.getValue()));
        /* display the hexadecimal value for non-printable characters */
        if ((key >= 0 && key < 32) || key == 127) {
            string.append("%02x%n".formatted(key));
        } else {
            string.append("%s%n".formatted((char) key));
        }
    }
    return string.toString();
}

static Map<Integer, Integer> frequencies(String path) throws IOException {
    try (InputStreamReader reader = new InputStreamReader(new FileInputStream(path))) {
        /* key = character, and value = occurrences */
        Map<Integer, Integer> map = new HashMap<>();
        int value;
        while ((value = reader.read()) != -1) {
            if (map.containsKey(value)) {
                map.put(value, map.get(value) + 1);
            } else {
                map.put(value, 1);
            }
        }
        return map;
    }
}

```

### java_code_3.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class LetterFreq {
	public static int[] countLetters(String filename) throws IOException{
		int[] freqs = new int[26];
		BufferedReader in = new BufferedReader(new FileReader(filename));
		String line;
		while((line = in.readLine()) != null){
			line = line.toUpperCase();
			for(char ch:line.toCharArray()){
				if(Character.isLetter(ch)){
					freqs[ch - 'A']++;
				}
			}
		}
		in.close();
		return freqs;
	}
	
	public static void main(String[] args) throws IOException{
		System.out.println(Arrays.toString(countLetters("filename.txt")));
	}
}

```

### java_code_4.txt
```java
public static int[] countLetters(String filename) throws IOException{
	int[] freqs = new int[26];
	try(BufferedReader in = new BufferedReader(new FileReader(filename))){
		String line;
		while((line = in.readLine()) != null){
			line = line.toUpperCase();
			for(char ch:line.toCharArray()){
				if(Character.isLetter(ch)){
					freqs[ch - 'A']++;
				}
			}
		}
	}
	return freqs;
}

```

### java_code_5.txt
```java
public static Map<Integer, Long> countLetters(String filename) throws IOException {
    return Files.lines(Paths.get(filename))
        .flatMapToInt(String::chars)
        .filter(Character::isLetter)
        .boxed()
        .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
}

```

## Python Code
### python_code_1.txt
```python
import collections, sys

def filecharcount(openfile):
    return sorted(collections.Counter(c for l in openfile for c in l).items())

f = open(sys.argv[1])
print(filecharcount(f))

```

### python_code_2.txt
```python
'''Character counting as a fold'''

from functools import reduce
from itertools import repeat
from os.path import expanduser


# charCounts :: String -> Dict Char Int
def charCounts(s):
    '''A dictionary of
       (character, frequency) mappings
    '''
    def tally(dct, c):
        dct[c] = 1 + dct[c] if c in dct else 1
        return dct
    return reduce(tally, list(s), {})


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Listing in descending order of frequency.'''

    print(
        tabulated(
            'Descending order of frequency:\n'
        )(compose(repr)(fst))(compose(str)(snd))(
            5
        )(stet)(
            sorted(
                charCounts(
                    readFile('~/Code/charCount/readme.txt')
                ).items(),
                key=swap,
                reverse=True
            )
        )
    )


# GENERIC -------------------------------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n,
       subdividing the contents of xs.
       Where the length of xs is not evenly divible,
       the final list will be shorter than n.'''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
       derived by expanding any ~ in fp.'''
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()


# paddedMatrix :: a -> [[a]] -> [[a]]
def paddedMatrix(v):
    ''''A list of rows padded to equal length
        (where needed) with instances of the value v.'''
    def go(rows):
        return paddedRows(
            len(max(rows, key=len))
        )(v)(rows)
    return lambda rows: go(rows) if rows else []


# paddedRows :: Int -> a -> [[a]] -[[a]]
def paddedRows(n):
    '''A list of rows padded (but never truncated)
       to length n with copies of value v.'''
    def go(v, xs):
        def pad(x):
            d = n - len(x)
            return (x + list(repeat(v, d))) if 0 < d else x
        return list(map(pad, xs))
    return lambda v: lambda xs: go(v, xs) if xs else []


# showColumns :: Int -> [String] -> String
def showColumns(n):
    '''A column-wrapped string
       derived from a list of rows.'''
    def go(xs):
        def fit(col):
            w = len(max(col, key=len))

            def pad(x):
                return x.ljust(4 + w, ' ')
            return ''.join(map(pad, col)).rstrip()

        q, r = divmod(len(xs), n)
        return '\n'.join(map(
            fit,
            zip(*paddedMatrix('')(
                chunksOf(q + int(bool(r)))(xs)
            ))
        ))
    return lambda xs: go(xs)


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# stet :: a -> a
def stet(x):
    '''The identity function.
       The usual 'id' is reserved in Python.'''
    return x


# swap :: (a, b) -> (b, a)
def swap(tpl):
    '''The swapped components of a pair.'''
    return (tpl[1], tpl[0])


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        Int ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
          number of columns -> f -> value list -> tabular string.'''
    def go(xShow, fxShow, intCols, f, xs):
        def mxw(fshow, g):
            return max(map(compose(len)(fshow), map(g, xs)))
        w = mxw(xShow, lambda x: x)
        fw = mxw(fxShow, f)
        return s + '\n' + showColumns(intCols)([
            xShow(x).rjust(w, ' ') + ' -> ' + (
                fxShow(f(x)).rjust(fw, ' ')
            )
            for x in xs
        ])
    return lambda xShow: lambda fxShow: lambda nCols: (
        lambda f: lambda xs: go(
            xShow, fxShow, nCols, f, xs
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import string
if hasattr(string, 'ascii_lowercase'):
    letters = string.ascii_lowercase       # Python 2.2 and later
else:
    letters = string.lowercase             # Earlier versions
offset = ord('a')

def countletters(file_handle):
    """Traverse a file and compute the number of occurences of each letter
    return results as a simple 26 element list of integers."""
    results = [0] * len(letters)
    for line in file_handle:
        for char in line:
            char = char.lower()
            if char in letters:
                results[ord(char) - offset] += 1
                # Ordinal minus ordinal of 'a' of any lowercase ASCII letter -> 0..25
    return results

if __name__ == "__main__":
    sourcedata = open(sys.argv[1])
    lettercounts = countletters(sourcedata)
    for i in xrange(len(lettercounts)):
        print "%s=%d" % (chr(i + ord('a')), lettercounts[i]),

```

### python_code_4.txt
```python
...
from collections import defaultdict
def countletters(file_handle):
    """Count occurences of letters and return a dictionary of them
    """
    results = defaultdict(int)
    for line in file_handle:
        for char in line:
            if char.lower() in letters:
                c = char.lower()
                results[c] += 1
    return results

```

### python_code_5.txt
```python
lettercounts = countletters(sourcedata)
for letter,count in lettercounts.iteritems():
    print "%s=%s" % (letter, count),

```

