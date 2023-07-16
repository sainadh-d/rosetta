# Strip whitespace from a string/Top and tail

## Task Link
[Rosetta Code - Strip whitespace from a string/Top and tail](https://rosettacode.org/wiki/Strip_whitespace_from_a_string/Top_and_tail)

## Java Code
### java_code_1.txt
```java
"    abc".stripLeading()

```

### java_code_2.txt
```java
"abc    ".stripTrailing()

```

### java_code_3.txt
```java
"    abc    ".strip()

```

### java_code_4.txt
```java
"    abc    ".trim()

```

### java_code_5.txt
```java
String removeLeading(String string, char[] characters) {
    int index = 0;
    for (char characterA : string.toCharArray()) {
        for (char characterB : characters) {
            if (characterA != characterB)
                return string.substring(index);
        }
        index++;
    }
    return string;
}

```

### java_code_6.txt
```java
String removeTrailing(String string, char[] characters) {
    for (int index = string.length() - 1; index >= 0; index--) {
        for (char character : characters) {
            if (string.charAt(index) != character)
                return string.substring(0, index + 1);
        }
    }
    return string;
}

```

### java_code_7.txt
```java
public class Trims{
    public static String ltrim(String s) {
        int i = 0;
        while (i < s.length() && Character.isWhitespace(s.charAt(i))) {
            i++;
        }
        return s.substring(i);
    }

    public static String rtrim(String s) {
        int i = s.length() - 1;
        while (i > 0 && Character.isWhitespace(s.charAt(i))) {
            i--;
        }
        return s.substring(0, i + 1);
    }

    public static String trim(String s) {
    	return rtrim(ltrim(s));
    }

    public static void main(String[] args) {
        String s = " \t \r \n String with spaces \u2009 \t  \r  \n  ";
        System.out.printf("[%s]\n", ltrim(s));
        System.out.printf("[%s]\n", rtrim(s));
        System.out.printf("[%s]\n", trim(s));
    }
}

```

### java_code_8.txt
```java
    public static String ltrim(String s) {
        int offset = 0;
        while (offset < s.length()) {
            int codePoint = s.codePointAt(offset);
            if (!Character.isWhitespace(codePoint)) break;
            offset += Character.charCount(codePoint);
        }
        return s.substring(offset);
    }

    public static String rtrim(String s) {
        int offset = s.length();
        while (offset > 0) {
            int codePoint = s.codePointBefore(offset);
            if (!Character.isWhitespace(codePoint)) break;
            offset -= Character.charCount(codePoint);
        }
        return s.substring(0, offset);
    }

```

## Python Code
### python_code_1.txt
```python
>>> s = ' \t \r \n String with spaces  \t  \r  \n  '
>>> s
' \t \r \n String with spaces  \t  \r  \n  '
>>> s.lstrip()
'String with spaces  \t  \r  \n  '
>>> s.rstrip()
' \t \r \n String with spaces'
>>> s.strip()
'String with spaces'
>>>

```

