# Reverse words in a string

## Task Link
[Rosetta Code - Reverse words in a string](https://rosettacode.org/wiki/Reverse_words_in_a_string)

## Java Code
### java_code_1.txt
```java
public class ReverseWords {

    static final String[] lines = {
        " ----------- Ice and Fire ----------- ",
        "                                      ",
        " fire, in end will world the say Some ",
        " ice. in say Some                     ",
        " desire of tasted I've what From      ",
        " fire. favor who those with hold I    ",
        "                                      ",
        " ... elided paragraph last ...        ",
        " Frost Robert ----------------------- "};

    public static void main(String[] args) {
        for (String line : lines) {
            String[] words = line.split("\\s");
            for (int i = words.length - 1; i >= 0; i--)
                System.out.printf("%s ", words[i]);
            System.out.println();
        }
    }
}

```

### java_code_2.txt
```java
package string;

import static java.util.Arrays.stream;

public interface ReverseWords {
  public static final String[] LINES = {
    " ----------- Ice and Fire ----------- ",
    "                                      ",
    " fire, in end will world the say Some ",
    " ice. in say Some                     ",
    " desire of tasted I've what From      ",
    " fire. favor who those with hold I    ",
    "                                      ",
    " ... elided paragraph last ...        ",
    " Frost Robert ----------------------- "
  };

  public static String[] reverseWords(String[] lines) {
    return stream(lines)
      .parallel()
      .map(l -> l.split("\\s"))
      .map(ws -> stream(ws)
        .parallel()
        .map(w -> " " + w)
        .reduce(
          "",
          (w1, w2) -> w2 + w1
        )
      )
      .toArray(String[]::new)
    ;
  }
 
  public static void main(String... arguments) {
    stream(reverseWords(LINES))
      .forEach(System.out::println)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
 text = '''\
---------- Ice and Fire ------------

fire, in end will world the say Some
ice. in say Some
desire of tasted I've what From
fire. favor who those with hold I

... elided paragraph last ...

Frost Robert -----------------------'''

for line in text.split('\n'): print(' '.join(line.split()[::-1]))

```

