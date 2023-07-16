# Jaro-Winkler distance

## Task Link
[Rosetta Code - Jaro-Winkler distance](https://rosettacode.org/wiki/Jaro-Winkler_distance)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.util.*;

public class JaroWinkler {
    public static void main(String[] args) {
        try {
            List<String> words = loadDictionary("linuxwords.txt");
            String[] strings = {
                "accomodate", "definately", "goverment", "occured",
                "publically", "recieve", "seperate", "untill", "wich"
            };
            for (String string : strings) {
                System.out.printf("Close dictionary words (distance < 0.15 using Jaro-Winkler distance) to '%s' are:\n"
                                    + "        Word   |  Distance\n", string);
                for (StringDistance s : withinDistance(words, 0.15, string, 5)) {
                    System.out.printf("%14s | %.4f\n", s.word, s.distance);
                }
                System.out.println();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static class StringDistance implements Comparable<StringDistance> {
        private StringDistance(String word, double distance) {
            this.word = word;
            this.distance = distance;
        }
        public int compareTo(StringDistance s) {
            return Double.compare(distance, s.distance);
        }
        private String word;
        private double distance;
    }

    private static List<StringDistance> withinDistance(List<String> words,
                        double maxDistance, String string, int max) {
        List<StringDistance> result = new ArrayList<>();
        for (String word : words) {
            double distance = jaroWinklerDistance(word, string);
            if (distance <= maxDistance)
                result.add(new StringDistance(word, distance));
        }
        Collections.sort(result);
        if (result.size() > max)
            result = result.subList(0, max);
        return result;
    }

    private static double jaroWinklerDistance(String string1, String string2) {
        int len1 = string1.length();
        int len2 = string2.length();
        if (len1 < len2) {
            String s = string1;
            string1 = string2;
            string2 = s;
            int tmp = len1;
            len1 = len2;
            len2 = tmp;
        }
        if (len2 == 0)
            return len1 == 0 ? 0.0 : 1.0;
        int delta = Math.max(1, len1 / 2) - 1;
        boolean[] flag = new boolean[len2];
        Arrays.fill(flag, false);
        char[] ch1Match = new char[len1];
        int matches = 0;
        for (int i = 0; i < len1; ++i) {
            char ch1 = string1.charAt(i);
            for (int j = 0; j < len2; ++j) {
                char ch2 = string2.charAt(j);
                if (j <= i + delta && j + delta >= i && ch1 == ch2 && !flag[j]) {
                    flag[j] = true;
                    ch1Match[matches++] = ch1;
                    break;
                }
            }
        }
        if (matches == 0)
            return 1.0;
        int transpositions = 0;
        for (int i = 0, j = 0; j < len2; ++j) {
            if (flag[j]) {
                if (string2.charAt(j) != ch1Match[i])
                    ++transpositions;
                ++i;
            }
        }
        double m = matches;
        double jaro = (m / len1 + m / len2 + (m - transpositions / 2.0) / m) / 3.0;
        int commonPrefix = 0;
        len2 = Math.min(4, len2);
        for (int i = 0; i < len2; ++i) {
            if (string1.charAt(i) == string2.charAt(i))
                ++commonPrefix;
        }
        return 1.0 - (jaro + commonPrefix * 0.1 * (1.0 - jaro));
    }

    private static List<String> loadDictionary(String path) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            List<String> words = new ArrayList<>();
            String word;
            while ((word = reader.readLine()) != null)
                words.add(word);
            return words;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
"""
Test Jaro-Winkler distance metric.
linuxwords.txt is from http://users.cs.duke.edu/~ola/ap/linuxwords
"""

WORDS = [s.strip() for s in open("linuxwords.txt").read().split()]
MISSPELLINGS = [
    "accomodate​",
    "definately​",
    "goverment",
    "occured",
    "publically",
    "recieve",
    "seperate",
    "untill",
    "wich",
]

def jaro_winkler_distance(st1, st2):
    """
    Compute Jaro-Winkler distance between two strings.
    """
    if len(st1) < len(st2):
        st1, st2 = st2, st1
    len1, len2 = len(st1), len(st2)
    if len2 == 0:
        return 0.0
    delta = max(0, len2 // 2 - 1)
    flag = [False for _ in range(len2)]  # flags for possible transpositions
    ch1_match = []
    for idx1, ch1 in enumerate(st1):
        for idx2, ch2 in enumerate(st2):
            if idx2 <= idx1 + delta and idx2 >= idx1 - delta and ch1 == ch2 and not flag[idx2]:
                flag[idx2] = True
                ch1_match.append(ch1)
                break

    matches = len(ch1_match)
    if matches == 0:
        return 1.0
    transpositions, idx1 = 0, 0
    for idx2, ch2 in enumerate(st2):
        if flag[idx2]:
            transpositions += (ch2 != ch1_match[idx1])
            idx1 += 1

    jaro = (matches / len1 + matches / len2 + (matches - transpositions/2) / matches) / 3.0
    commonprefix = 0
    for i in range(min(4, len2)):
        commonprefix += (st1[i] == st2[i])

    return 1.0 - (jaro + commonprefix * 0.1 * (1 - jaro))

def within_distance(maxdistance, stri, maxtoreturn):
    """
    Find words in WORDS of closeness to stri within maxdistance, return up to maxreturn of them.
    """
    arr = [w for w in WORDS if jaro_winkler_distance(stri, w) <= maxdistance]
    arr.sort(key=lambda x: jaro_winkler_distance(stri, x))
    return arr if len(arr) <= maxtoreturn else arr[:maxtoreturn]

for STR in MISSPELLINGS:
    print('\nClose dictionary words ( distance < 0.15 using Jaro-Winkler distance) to "',
          STR, '" are:\n        Word   |  Distance')
    for w in within_distance(0.15, STR, 5):
        print('{:>14} | {:6.4f}'.format(w, jaro_winkler_distance(STR, w)))

```

