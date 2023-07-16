# Strip control codes and extended characters from a string

## Task Link
[Rosetta Code - Strip control codes and extended characters from a string](https://rosettacode.org/wiki/Strip_control_codes_and_extended_characters_from_a_string)

## Java Code
### java_code_1.txt
```java
import java.util.function.IntPredicate;

public class StripControlCodes {

    public static void main(String[] args) {
        String s = "\u0000\n abc\u00E9def\u007F";
        System.out.println(stripChars(s, c -> c > '\u001F' && c != '\u007F'));
        System.out.println(stripChars(s, c -> c > '\u001F' && c < '\u007F'));
    }

    static String stripChars(String s, IntPredicate include) {
        return s.codePoints().filter(include::test).collect(StringBuilder::new,
                StringBuilder::appendCodePoint, StringBuilder::append).toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)

print(stripped("\ba\x00b\n\rc\fd\xc3"))

```

