# Best shuffle

## Task Link
[Rosetta Code - Best shuffle](https://rosettacode.org/wiki/Best_shuffle)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class BestShuffle {
    private final static Random rand = new Random();

    public static void main(String[] args) {
        String[] words = {"abracadabra", "seesaw", "grrrrrr", "pop", "up", "a"};
        for (String w : words)
            System.out.println(bestShuffle(w));
    }

    public static String bestShuffle(final String s1) {
        char[] s2 = s1.toCharArray();
        shuffle(s2);
        for (int i = 0; i < s2.length; i++) {
            if (s2[i] != s1.charAt(i))
                continue;
            for (int j = 0; j < s2.length; j++) {
                if (s2[i] != s2[j] && s2[i] != s1.charAt(j) && s2[j] != s1.charAt(i)) {
                    char tmp = s2[i];
                    s2[i] = s2[j];
                    s2[j] = tmp;
                    break;
                }
            }
        }
        return s1 + " " + new String(s2) + " (" + count(s1, s2) + ")";
    }

    public static void shuffle(char[] text) {
        for (int i = text.length - 1; i > 0; i--) {
            int r = rand.nextInt(i + 1);
            char tmp = text[i];
            text[i] = text[r];
            text[r] = tmp;
        }
    }

    private static int count(final String s1, final char[] s2) {
        int count = 0;
        for (int i = 0; i < s2.length; i++)
            if (s1.charAt(i) == s2[i])
                count++;
        return count;
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

def count(w1,wnew):
    return sum(c1==c2 for c1,c2 in zip(w1, wnew))

def best_shuffle(w):
    wnew = list(w)
    n = len(w)
    rangelists = (list(range(n)), list(range(n)))
    for r in rangelists:
        random.shuffle(r)
    rangei, rangej = rangelists
    for i in rangei:
        for j in rangej:
            if i != j and wnew[j] != wnew[i] and w[i] != wnew[j] and w[j] != wnew[i]:
                wnew[j], wnew[i] = wnew[i], wnew[j]
                break
    wnew = ''.join(wnew)
    return wnew, count(w, wnew)


if __name__ == '__main__':
    test_words = ('tree abracadabra seesaw elk grrrrrr up a ' 
                  + 'antidisestablishmentarianism hounddogs').split()
    test_words += ['aardvarks are ant eaters', 'immediately', 'abba']
    for w in test_words:
        wnew, c = best_shuffle(w)
        print("%29s, %-29s ,(%i)" % (w, wnew, c))

```

### python_code_2.txt
```python
#!/usr/bin/env python

def best_shuffle(s):
    # Count the supply of characters.
    from collections import defaultdict
    count = defaultdict(int)
    for c in s:
        count[c] += 1

    # Shuffle the characters.
    r = []
    for x in s:
        # Find the best character to replace x.
        best = None
        rankb = -2
        for c, rankc in count.items():
            # Prefer characters with more supply.
            # (Save characters with less supply.)
            # Avoid identical characters.
            if c == x: rankc = -1
            if rankc > rankb:
                best = c
                rankb = rankc

        # Add character to list. Remove it from supply.
        r.append(best)
        count[best] -= 1
        if count[best] >= 0: del count[best]

    # If the final letter became stuck (as "ababcd" became "bacabd",
    # and the final "d" became stuck), then fix it.
    i = len(s) - 1
    if r[i] == s[i]:
        for j in range(i):
            if r[i] != s[j] and r[j] != s[i]:
                r[i], r[j] = r[j], r[i]
                break

    # Convert list to string. PEP 8, "Style Guide for Python Code",
    # suggests that ''.join() is faster than + when concatenating
    # many strings. See http://www.python.org/dev/peps/pep-0008/
    r = ''.join(r)

    score = sum(x == y for x, y in zip(r, s))

    return (r, score)

for s in "abracadabra", "seesaw", "elk", "grrrrrr", "up", "a":
    shuffled, score = best_shuffle(s)
    print("%s, %s, (%d)" % (s, shuffled, score))

```

