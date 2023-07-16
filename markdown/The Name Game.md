# The Name Game

## Task Link
[Rosetta Code - The Name Game](https://rosettacode.org/wiki/The_Name_Game)

## Java Code
### java_code_1.txt
```java
import java.util.stream.Stream;

public class NameGame {
    private static void printVerse(String name) {
        StringBuilder sb = new StringBuilder(name.toLowerCase());
        sb.setCharAt(0, Character.toUpperCase(sb.charAt(0)));
        String x = sb.toString();
        String y = "AEIOU".indexOf(x.charAt(0)) > -1 ? x.toLowerCase() : x.substring(1);
        String b = "b" + y;
        String f = "f" + y;
        String m = "m" + y;
        switch (x.charAt(0)) {
            case 'B':
                b = y;
                break;
            case 'F':
                f = y;
                break;
            case 'M':
                m = y;
                break;
            default:
                // no adjustment needed
                break;
        }
        System.out.printf("%s, %s, bo-%s\n", x, x, b);
        System.out.printf("Banana-fana fo-%s\n", f);
        System.out.printf("Fee-fi-mo-%s\n", m);
        System.out.printf("%s!\n\n", x);
    }

    public static void main(String[] args) {
        Stream.of("Gary", "Earl", "Billy", "Felix", "Mary", "Steve").forEach(NameGame::printVerse);
    }
}

```

## Python Code
### python_code_1.txt
```python
def print_verse(n):
    l = ['b', 'f', 'm']
    s = n[1:]
    if str.lower(n[0]) in l:
        l[l.index(str.lower(n[0]))] = ''
    elif n[0] in ['A', 'E', 'I', 'O', 'U']:
        s = str.lower(n)
    print('{0}, {0}, bo-{2}{1}\nBanana-fana fo-{3}{1}\nFee-fi-mo-{4}{1}\n{0}!\n'.format(n, s, *l))

# Assume that the names are in title-case and they're more than one character long
for n in ['Gary', 'Earl', 'Billy', 'Felix', 'Mary']:
    print_verse(n)

```

