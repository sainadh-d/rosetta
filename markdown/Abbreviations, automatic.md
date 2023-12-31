# Abbreviations, automatic

## Task Link
[Rosetta Code - Abbreviations, automatic](https://rosettacode.org/wiki/Abbreviations,_automatic)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Abbreviations {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("days_of_week.txt");
        List<String> readAllLines = Files.readAllLines(path);
        for (int i = 0; i < readAllLines.size(); i++) {
            String line = readAllLines.get(i);
            if (line.length() == 0) continue;

            String[] days = line.split(" ");
            if (days.length != 7) throw new RuntimeException("There aren't 7 days on line " + (i + 1));

            Map<String, Integer> temp = new HashMap<>();
            for (String day : days) {
                Integer count = temp.getOrDefault(day, 0);
                temp.put(day, count + 1);
            }
            if (temp.size() < 7) {
                System.out.print(" ∞  ");
                System.out.println(line);
                continue;
            }

            int len = 1;
            while (true) {
                temp.clear();
                for (String day : days) {
                    String sd;
                    if (len >= day.length()) {
                        sd = day;
                    } else {
                        sd = day.substring(0, len);
                    }
                    Integer count = temp.getOrDefault(sd, 0);
                    temp.put(sd, count + 1);
                }
                if (temp.size() == 7) {
                    System.out.printf("%2d  %s\n", len, line);
                    break;
                }
                len++;
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def shortest_abbreviation_length(line, list_size):
    words = line.split()
    word_count = len(words)
    # Can't give true answer with unexpected number of entries
    if word_count != list_size:
        raise ValueError(f'Not enough entries, expected {list_size} found {word_count}')

    # Find the small slice length that gives list_size unique values
    abbreviation_length = 1
    abbreviations = set()
    while(True):
        abbreviations = {word[:abbreviation_length] for word in words}
        if len(abbreviations) == list_size:
            return abbreviation_length
        abbreviation_length += 1
        abbreviations.clear()

def automatic_abbreviations(filename, words_per_line):
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if len(line) > 0:
                length = shortest_abbreviation_length(line, words_per_line)
                print(f'{length:2} {line}')
            else:
                print()

automatic_abbreviations('daysOfWeek.txt', 7)

```

### python_code_2.txt
```python
import operator
from itertools import (accumulate,
                       repeat)
from pathlib import Path
from typing import (Iterator,
                    List,
                    Tuple)


FILEPATH = Path('days_of_week.txt')


def read_lines(path: Path) -> Iterator[str]:
    with path.open() as file:
        yield from file


def cumulative_letters(word: str) -> Iterator[str]:
    """For a word 'foo' yields 'f', 'fo', 'foo', 'foo', 'foo', ..."""
    yield from accumulate(word, operator.add)
    yield from repeat(word)


def words_cumulative_letters(words: List[str]) -> Iterator[Tuple[str, ...]]:
    """Yields cumulative letters for several words at the same time"""
    yield from zip(*map(cumulative_letters, words))


def longest_string_length(strings: Tuple[str, ...]) -> int:
    return max(map(len, strings))


def min_abbreviation_length(words: List[str]) -> int:
    def are_unique(abbreviations: Tuple[str, ...]) -> bool:
        return len(set(abbreviations)) == len(words)

    unique_abbreviations = filter(are_unique, words_cumulative_letters(words))

    return longest_string_length(next(unique_abbreviations))


def main():
    for line in read_lines(FILEPATH):
        words = line.split()
        if not words:
            print()
            continue

        count = min_abbreviation_length(words)
        print(f'{count} {line}', end='')


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''Automatic abbreviations'''

from itertools import (accumulate, chain)
from os.path import expanduser


# abbrevLen :: [String] -> Int
def abbrevLen(xs):
    '''The minimum length of prefix required to obtain
       a unique abbreviation for each string in xs.'''
    n = len(xs)

    return next(
        len(a[0]) for a in map(
            compose(nub)(map_(concat)),
            transpose(list(map(inits, xs)))
        ) if n == len(a)
    )


# TEST ----------------------------------------------------
def main():
    '''Test'''

    xs = map_(strip)(
        lines(readFile('weekDayNames.txt'))
    )
    for i, n in enumerate(map(compose(abbrevLen)(words), xs)):
        print(n, '  ', xs[i])


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [String] -> String
def concat(xs):
    '''The concatenation of a list of strings.'''
    return ''.join(xs)


# inits :: [a] -> [[a]]
def inits(xs):
    '''all initial segments of xs, shortest first.'''
    return list(scanl(lambda a, x: a + [x])(
        []
    )(list(xs)))


# lines :: String -> [String]
def lines(s):
    '''A list of strings,
       (containing no newline characters)
       derived from a single new-line delimited string.'''
    return s.splitlines()


# map :: (a -> b) -> [a] -> [b]
def map_(f):
    '''The list obtained by applying f
       to each element of xs.'''
    return lambda xs: list(map(f, xs))


# nub :: [a] -> [a]
def nub(xs):
    '''A list containing the same elements as xs,
       without duplicates, in the order of their
       first occurrence.'''
    return list(dict.fromkeys(xs))


# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
       derived by expanding any ~ in fp.'''
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.'''
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )


# strip :: String -> String
def strip(s):
    '''A copy of s without any leading or trailling
       white space.'''
    return s.strip()


# transpose :: Matrix a -> Matrix a
def transpose(m):
    '''The rows and columns of the argument transposed.
       (The matrix containers and rows can be lists or tuples).'''
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m


# words :: String -> [String]
def words(s):
    '''A list of words delimited by characters
       representing white space.'''
    return s.split()


# MAIN ---
if __name__ == '__main__':
    main()

```

