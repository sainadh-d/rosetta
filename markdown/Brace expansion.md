# Brace expansion

## Task Link
[Rosetta Code - Brace expansion](https://rosettacode.org/wiki/Brace_expansion)

## Java Code
### java_code_1.txt
```java
public class BraceExpansion {

    public static void main(String[] args) {
        for (String s : new String[]{"It{{em,alic}iz,erat}e{d,}, please.",
            "~/{Downloads,Pictures}/*.{jpg,gif,png}",
            "{,{,gotta have{ ,\\, again\\, }}more }cowbell!",
            "{}} some }{,{\\\\{ edge, edge} \\,}{ cases, {here} \\\\\\\\\\}"}) {
            System.out.println();
            expand(s);
        }
    }

    public static void expand(String s) {
        expandR("", s, "");
    }

    private static void expandR(String pre, String s, String suf) {
        int i1 = -1, i2 = 0;
        String noEscape = s.replaceAll("([\\\\]{2}|[\\\\][,}{])", "  ");
        StringBuilder sb = null;

        outer:
        while ((i1 = noEscape.indexOf('{', i1 + 1)) != -1) {
            i2 = i1 + 1;
            sb = new StringBuilder(s);
            for (int depth = 1; i2 < s.length() && depth > 0; i2++) {
                char c = noEscape.charAt(i2);
                depth = (c == '{') ? ++depth : depth;
                depth = (c == '}') ? --depth : depth;
                if (c == ',' && depth == 1) {
                    sb.setCharAt(i2, '\u0000');
                } else if (c == '}' && depth == 0 && sb.indexOf("\u0000") != -1)
                    break outer;
            }
        }
        if (i1 == -1) {
            if (suf.length() > 0)
                expandR(pre + s, suf, "");
            else
                System.out.printf("%s%s%s%n", pre, s, suf);
        } else {
            for (String m : sb.substring(i1 + 1, i2).split("\u0000", -1))
                expandR(pre + s.substring(0, i1), m, s.substring(i2 + 1) + suf);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def getitem(s, depth=0):
    out = [""]
    while s:
        c = s[0]
        if depth and (c == ',' or c == '}'):
            return out,s
        if c == '{':
            x = getgroup(s[1:], depth+1)
            if x:
                out,s = [a+b for a in out for b in x[0]], x[1]
                continue
        if c == '\\' and len(s) > 1:
            s, c = s[1:], c + s[1]

        out, s = [a+c for a in out], s[1:]

    return out,s

def getgroup(s, depth):
    out, comma = [], False
    while s:
        g,s = getitem(s, depth)
        if not s: break
        out += g

        if s[0] == '}':
            if comma: return out, s[1:]
            return ['{' + a + '}' for a in out], s[1:]

        if s[0] == ',':
            comma,s = True, s[1:]

    return None

# stolen cowbells from Raku example
for s in '''~/{Downloads,Pictures}/*.{jpg,gif,png}
It{{em,alic}iz,erat}e{d,}, please.
{,{,gotta have{ ,\, again\, }}more }cowbell!
{}} some }{,{\\\\{ edge, edge} \,}{ cases, {here} \\\\\\\\\}'''.split('\n'):
    print "\n\t".join([s] + getitem(s)[0]) + "\n"

```

