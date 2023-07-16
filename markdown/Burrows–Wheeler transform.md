# Burrows–Wheeler transform

## Task Link
[Rosetta Code - Burrows–Wheeler transform](https://rosettacode.org/wiki/Burrows%E2%80%93Wheeler_transform)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class BWT {
    private static final String STX = "\u0002";
    private static final String ETX = "\u0003";

    private static String bwt(String s) {
        if (s.contains(STX) || s.contains(ETX)) {
            throw new IllegalArgumentException("String cannot contain STX or ETX");
        }

        String ss = STX + s + ETX;
        List<String> table = new ArrayList<>();
        for (int i = 0; i < ss.length(); i++) {
            String before = ss.substring(i);
            String after = ss.substring(0, i);
            table.add(before + after);
        }
        table.sort(String::compareTo);

        StringBuilder sb = new StringBuilder();
        for (String str : table) {
            sb.append(str.charAt(str.length() - 1));
        }
        return sb.toString();
    }

    private static String ibwt(String r) {
        int len = r.length();
        List<String> table = new ArrayList<>();
        for (int i = 0; i < len; ++i) {
            table.add("");
        }
        for (int j = 0; j < len; ++j) {
            for (int i = 0; i < len; ++i) {
                table.set(i, r.charAt(i) + table.get(i));
            }
            table.sort(String::compareTo);
        }
        for (String row : table) {
            if (row.endsWith(ETX)) {
                return row.substring(1, len - 1);
            }
        }
        return "";
    }

    private static String makePrintable(String s) {
        // substitute ^ for STX and | for ETX to print results
        return s.replace(STX, "^").replace(ETX, "|");
    }

    public static void main(String[] args) {
        List<String> tests = List.of(
            "banana",
            "appellee",
            "dogwood",
            "TO BE OR NOT TO BE OR WANT TO BE OR NOT?",
            "SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES",
            "\u0002ABC\u0003"
        );
        for (String test : tests) {
            System.out.println(makePrintable(test));
            System.out.print(" --> ");
            String t = "";
            try {
                t = bwt(test);
                System.out.println(makePrintable(t));
            } catch (IllegalArgumentException e) {
                System.out.println("ERROR: " + e.getMessage());
            }
            String r = ibwt(t);
            System.out.printf(" --> %s\n\n", r);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
    s = "\002" + s + "\003"  # Add start and end of text marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string


def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
    return s.rstrip("\003").strip("\002")  # Get rid of start and end markers

```

