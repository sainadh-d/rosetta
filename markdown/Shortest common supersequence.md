# Shortest common supersequence

## Task Link
[Rosetta Code - Shortest common supersequence](https://rosettacode.org/wiki/Shortest_common_supersequence)

## Java Code
### java_code_1.txt
```java
public class ShortestCommonSuperSequence {
    private static boolean isEmpty(String s) {
        return null == s || s.isEmpty();
    }

    private static String scs(String x, String y) {
        if (isEmpty(x)) {
            return y;
        }
        if (isEmpty(y)) {
            return x;
        }

        if (x.charAt(0) == y.charAt(0)) {
            return x.charAt(0) + scs(x.substring(1), y.substring(1));
        }

        if (scs(x, y.substring(1)).length() <= scs(x.substring(1), y).length()) {
            return y.charAt(0) + scs(x, y.substring(1));
        } else {
            return x.charAt(0) + scs(x.substring(1), y);
        }
    }

    public static void main(String[] args) {
        System.out.println(scs("abcbdab", "bdcaba"));
    }
}

```

## Python Code
### python_code_1.txt
```python
# Use the Longest Common Subsequence algorithm

def shortest_common_supersequence(a, b):
    lcs = longest_common_subsequence(a, b)
    scs = ""
    # Consume lcs
    while len(lcs) > 0:
        if a[0]==lcs[0] and b[0]==lcs[0]:
        # Part of the LCS, so consume from all strings
            scs += lcs[0]
            lcs = lcs[1:]
            a = a[1:]
            b = b[1:]
        elif a[0]==lcs[0]:
            scs += b[0]
            b = b[1:]
        else:
            scs += a[0]
            a = a[1:]
    # append remaining characters
    return scs + a + b

```

