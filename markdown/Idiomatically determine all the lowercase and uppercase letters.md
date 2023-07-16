# Idiomatically determine all the lowercase and uppercase letters

## Task Link
[Rosetta Code - Idiomatically determine all the lowercase and uppercase letters](https://rosettacode.org/wiki/Idiomatically_determine_all_the_lowercase_and_uppercase_letters)

## Java Code
### java_code_1.txt
```java
import java.util.stream.IntStream;

public class Letters {
    public static void main(String[] args) throws Exception {
        System.out.print("Upper case: ");
        IntStream.rangeClosed(0, 0x10FFFF)
                 .filter(Character::isUpperCase)
                 .limit(72)
                 .forEach(n -> System.out.printf("%c", n));
        System.out.println("...");

        System.out.print("Lower case: ");
        IntStream.rangeClosed(0, 0x10FFFF)
                 .filter(Character::isLowerCase)
                 .limit(72)
                 .forEach(n -> System.out.printf("%c", n));
        System.out.println("...");
    }
}

```

## Python Code
### python_code_1.txt
```python
classes = (str.isupper, str.islower, str.isalnum, str.isalpha, str.isdecimal,
           str.isdigit, str.isidentifier, str.isnumeric, str.isprintable,
           str.isspace, str.istitle)

for stringclass in classes:
    chars = ''.join(chr(i) for i in range(0x10FFFF+1) if stringclass(chr(i)))
    print('\nString class %s has %i characters the first of which are:\n  %r'
          % (stringclass.__name__, len(chars), chars[:100]))

```

