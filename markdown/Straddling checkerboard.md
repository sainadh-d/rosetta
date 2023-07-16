# Straddling checkerboard

## Task Link
[Rosetta Code - Straddling checkerboard](https://rosettacode.org/wiki/Straddling_checkerboard)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;
import java.util.regex.*;

public class StraddlingCheckerboard {

    final static String[] keyvals = {"H:0", "O:1", "L:2", "M:4", "E:5", "S:6",
        "R:8", "T:9", "A:30", "B:31", "C:32", "D:33", "F:34", "G:35", "I:36",
        "J:37", "K:38", "N:39", "P:70", "Q:71", "U:72", "V:73", "W:74", "X:75",
        "Y:76", "Z:77", ".:78", "/:79", "0:790", "1:791", "2:792", "3:793",
        "4:794", "5:795", "6:796", "7:797", "8:798", "9:799"};

    final static Map<String, String> val2key = new HashMap<>();
    final static Map<String, String> key2val = new HashMap<>();

    public static void main(String[] args) {
        for (String keyval : keyvals) {
            String[] kv = keyval.split(":");
            val2key.put(kv[0], kv[1]);
            key2val.put(kv[1], kv[0]);
        }
        String enc = encode("One night-it was on the twentieth of March, "
                + "1888-I was returning");
        System.out.println(enc);
        System.out.println(decode(enc));
    }

    static String encode(String s) {
        StringBuilder sb = new StringBuilder();
        for (String c : s.toUpperCase().split("")) {
            c = val2key.get(c);
            if (c != null)
                sb.append(c);
        }
        return sb.toString();
    }

    static String decode(String s) {
        Matcher m = Pattern.compile("(79.|3.|7.|.)").matcher(s);
        StringBuilder sb = new StringBuilder();
        while (m.find()) {
            String v = key2val.get(m.group(1));
            if (v != null)
                sb.append(v);
        }
        return sb.toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
T = [["79", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
     ["",   "H", "O", "L", "",  "M", "E", "S", "",  "R", "T"],
     ["3",  "A", "B", "C", "D", "F", "G", "I", "J", "K", "N"],
     ["7",  "P", "Q", "U", "V", "W", "X", "Y", "Z", ".", "/"]]

def straddle(s):
    return "".join(L[0]+T[0][L.index(c)] for c in s.upper() for L in T if c in L)

def unstraddle(s):
    s = iter(s)
    for c in s:
        if c in [T[2][0], T[3][0]]:
            i = [T[2][0], T[3][0]].index(c)
            n = T[2 + i][T[0].index(s.next())]
            yield s.next() if n == "/" else n
        else:
            yield T[1][T[0].index(c)]

O = "One night-it was on the twentieth of March, 1888-I was returning"
print "Encoded:", straddle(O)
print "Decoded:", "".join(unstraddle(straddle(O)))

```

