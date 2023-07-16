# Word frequency

## Task Link
[Rosetta Code - Word frequency](https://rosettacode.org/wiki/Word_frequency)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

```

### java_code_2.txt
```java
void printWordFrequency() throws URISyntaxException, IOException {
    URL url = new URI("https://www.gutenberg.org/files/135/135-0.txt").toURL();
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()))) {
        Pattern pattern = Pattern.compile("(\\w+)");
        Matcher matcher;
        String line;
        String word;
        Map<String, Integer> map = new HashMap<>();
        while ((line = reader.readLine()) != null) {
            matcher = pattern.matcher(line);
            while (matcher.find()) {
                word = matcher.group().toLowerCase();
                if (map.containsKey(word)) {
                    map.put(word, map.get(word) + 1);
                } else {
                    map.put(word, 1);
                }
            }
        }
        /* print out top 10 */
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(Map.Entry.comparingByValue());
        Collections.reverse(list);
        int count = 1;
        for (Map.Entry<String, Integer> value : list) {
            System.out.printf("%-20s%,7d%n", value.getKey(), value.getValue());
            if (count++ == 10) break;
        }
    }
}

```

### java_code_3.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class WordCount {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("135-0.txt");
        byte[] bytes = Files.readAllBytes(path);
        String text = new String(bytes);
        text = text.toLowerCase();

        Pattern r = Pattern.compile("\\p{javaLowerCase}+");
        Matcher matcher = r.matcher(text);
        Map<String, Integer> freq = new HashMap<>();
        while (matcher.find()) {
            String word = matcher.group();
            Integer current = freq.getOrDefault(word, 0);
            freq.put(word, current + 1);
        }

        List<Map.Entry<String, Integer>> entries = freq.entrySet()
            .stream()
            .sorted((i1, i2) -> Integer.compare(i2.getValue(), i1.getValue()))
            .limit(10)
            .collect(Collectors.toList());

        System.out.println("Rank  Word  Frequency");
        System.out.println("====  ====  =========");
        int rank = 1;
        for (Map.Entry<String, Integer> entry : entries) {
            String word = entry.getKey();
            Integer count = entry.getValue();
            System.out.printf("%2d    %-4s    %5d\n", rank++, word, count);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import collections
import re
import string
import sys

def main():
  counter = collections.Counter(re.findall(r"\w+",open(sys.argv[1]).read().lower()))
  print counter.most_common(int(sys.argv[2]))

if __name__ == "__main__":
  main()

```

### python_code_2.txt
```python
from collections import Counter
from re import findall

les_mis_file = 'les_mis_135-0.txt'

def _count_words(fname):
    with open(fname) as f:
        text = f.read()
    words = findall(r'\w+', text.lower())
    return Counter(words)

def most_common_words_in_file(fname, n):
    counts = _count_words(fname)
    for word, count in [['WORD', 'COUNT']] + counts.most_common(n):
        print(f'{word:>10} {count:>6}')


if __name__ == "__main__":
    n = int(input('How many?: '))
    most_common_words_in_file(les_mis_file, n)

```

### python_code_3.txt
```python
"""
Word count task from Rosetta Code
http://www.rosettacode.org/wiki/Word_count#Python
"""
from itertools import (groupby,
                       starmap)
from operator import itemgetter
from pathlib import Path
from typing import (Iterable,
                    List,
                    Tuple)


FILEPATH = Path('lesMiserables.txt')
COUNT = 10


def main():
    words_and_counts = most_frequent_words(FILEPATH)
    print(*words_and_counts[:COUNT], sep='\n')


def most_frequent_words(filepath: Path,
                        *,
                        encoding: str = 'utf-8') -> List[Tuple[str, int]]:
    """
    A list of word-frequency pairs sorted by their occurrences.
    The words are read from the given file.
    """
    def word_and_frequency(word: str,
                           words_group: Iterable[str]) -> Tuple[str, int]:
        return word, capacity(words_group)

    file_contents = filepath.read_text(encoding=encoding)
    words = file_contents.lower().split()
    grouped_words = groupby(sorted(words))
    words_and_frequencies = starmap(word_and_frequency, grouped_words)
    return sorted(words_and_frequencies, key=itemgetter(1), reverse=True)


def capacity(iterable: Iterable) -> int:
    """Returns a number of elements in an iterable"""
    return sum(1 for _ in iterable)


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
#!/usr/bin/python3
import collections
import re

count = 10

with open("135-0.txt") as f:
    text = f.read()

word_freq = sorted(
    collections.Counter(sorted(re.split(r"\W+", text.lower()))).items(),
    key=lambda c: c[1],
    reverse=True,
)

for i in range(len(word_freq)):
    print("[{:2d}] {:>10} : {}".format(i + 1, word_freq[i][0], word_freq[i][1]))
    if i == count - 1:
        break

```

