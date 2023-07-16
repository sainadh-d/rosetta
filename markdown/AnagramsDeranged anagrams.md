# Anagrams/Deranged anagrams

## Task Link
[Rosetta Code - Anagrams/Deranged anagrams](https://rosettacode.org/wiki/Anagrams/Deranged_anagrams)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
 
public class DerangedAnagrams {
 
    public static void main(String[] args) throws IOException {
        List<String> words = Files.readAllLines(new File("unixdict.txt").toPath());
        printLongestDerangedAnagram(words);
    }
 
    private static void printLongestDerangedAnagram(List<String> words) {
        words.sort(Comparator.comparingInt(String::length).reversed().thenComparing(String::toString));

        Map<String, ArrayList<String>> map = new HashMap<>();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);

            List<String> anagrams = map.computeIfAbsent(key, k -> new ArrayList<>());
            for (String anagram : anagrams) {
                if (isDeranged(word, anagram)) {
                    System.out.printf("%s %s%n", anagram, word);
                    return;
                }
            }
            anagrams.add(word);
        }
        System.out.println("no result");
    }

    private static boolean isDeranged(String word1, String word2) {
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) == word2.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
import urllib.request
from collections import defaultdict
from itertools import combinations

def getwords(url='http://www.puzzlers.org/pub/wordlists/unixdict.txt'):
    return list(set(urllib.request.urlopen(url).read().decode().split()))

def find_anagrams(words):
    anagram = defaultdict(list) # map sorted chars to anagrams
    for word in words:
        anagram[tuple(sorted(word))].append( word )
    return dict((key, words) for key, words in anagram.items()
                if len(words) > 1)

def is_deranged(words):
    'returns pairs of words that have no character in the same position'
    return [ (word1, word2)
             for word1,word2 in combinations(words, 2)
             if all(ch1 != ch2 for ch1, ch2 in zip(word1, word2)) ]

def largest_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(),
                              key=lambda x:(-len(x[0]), x[0]))
    for _, words in ordered_anagrams:
        deranged_pairs = is_deranged(words)
        if deranged_pairs:
            return deranged_pairs
    return []

if __name__ == '__main__':
    words = getwords('http://www.puzzlers.org/pub/wordlists/unixdict.txt')
    print("Word count:", len(words))

    anagrams = find_anagrams(words)
    print("Anagram count:", len(anagrams),"\n")

    print("Longest anagrams with no characters in the same position:")
    print('  ' + '\n  '.join(', '.join(pairs)
                             for pairs in largest_deranged_ana(anagrams)))

```

### python_code_2.txt
```python
def most_deranged_ana(anagrams):
    ordered_anagrams = sorted(anagrams.items(),
                              key=lambda x:(-len(x[0]), x[0]))
    many_anagrams = [anas for _, anas in ordered_anagrams if len(anas) > 2]
    d_of_anas = [is_deranged(ana_group) for ana_group in many_anagrams]
    d_of_anas = [d_group for d_group in d_of_anas if d_group]
    d_of_anas.sort(key=lambda d_group:(-len(d_group), -len(d_group[0])))
    mx = len(d_of_anas[0])
    most = [sorted(d_group) for d_group in d_of_anas if len(d_group) == mx]
    return most

if __name__ == '__main__':
    most = most_deranged_ana(anagrams)
    print(f"\nThere are {len(most)} groups of anagrams all containing" 
          f" a max {len(most[0])} deranged word-pairs:")
    for pairs in most:
        print()
        print('  ' + '\n  '.join(', '.join(p) for p in pairs))

```

### python_code_3.txt
```python
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import (Callable,
                    Dict,
                    Iterable,
                    Iterator,
                    List,
                    Optional,
                    Tuple,
                    TypeVar)

WORDS_FILE = 'unixdict.txt'

T1 = TypeVar('T1')
T2 = TypeVar('T2')


def main():
    words = read_words(Path(WORDS_FILE))
    anagram = longest_deranged_anagram(words)
    if anagram:
        print('The longest deranged anagram is: {}, {}'.format(*anagram))
    else:
        print('No deranged anagrams were found')


def read_words(path: Path) -> Iterator[str]:
    """Yields words from file at specified path"""
    with path.open() as file:
        for word in file:
            yield word.strip()


def longest_deranged_anagram(words: Iterable[str]
                             ) -> Optional[Tuple[str, str]]:
    """
    Returns the longest pair of words
    that have no character in the same position
    """
    words_by_lengths = mapping_by_function(len, words)
    decreasing_lengths = sorted(words_by_lengths, reverse=True)
    for length in decreasing_lengths:
        words = words_by_lengths[length]
        anagrams_by_letters = mapping_by_function(sort_str, words)
        for anagrams in anagrams_by_letters.values():
            deranged_pair = next(deranged_word_pairs(anagrams), None)
            if deranged_pair is not None:
                return deranged_pair
    return None


def mapping_by_function(function: Callable[..., T2],
                        iterable: Iterable[T1]) -> Dict[T2, List[T1]]:
    """
    Constructs a dictionary with keys
    obtained from applying an input function
    to items of an iterable,
    and the values filled from the same iterable
    """
    mapping = defaultdict(list)
    for item in iterable:
        mapping[function(item)].append(item)
    return mapping


def sort_str(string: str) -> str:
    """Sorts input string alphabetically"""
    return ''.join(sorted(string))


def deranged_word_pairs(words: Iterable[str]) -> Iterator[Tuple[str, str]]:
    """Yields deranged words from an input list of words"""
    pairs = combinations(words, 2)  # type: Iterator[Tuple[str, str]]
    yield from filter(is_deranged, pairs)


def is_deranged(word_pair: Tuple[str, str]) -> bool:
    """
    Checks if all corresponding letters are different,
    assuming that words have the same length
    """
    return all(a != b for a, b in zip(*word_pair))


if __name__ == '__main__':
    main()

```

