# Regular expressions

## Task Link
[Rosetta Code - Regular expressions](https://rosettacode.org/wiki/Regular_expressions)

## Java Code
### java_code_1.txt
```java
/* match entire string against a pattern */
boolean isNumber = "-1234.567".matches("-?\\d+(?:\\.\\d+)?");

/* substitute part of string using a pattern */
String reduceSpaces = "a  b c   d e  f".replaceAll(" +", " ");

```

### java_code_2.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
...
/* group capturing example */
Pattern pattern = Pattern.compile("(?:(https?)://)?([^/]+)/(?:([^#]+)(?:#(.+))?)?");
Matcher matcher = pattern.matcher("https://rosettacode.org/wiki/Regular_expressions#Java");
if (matcher.find()) {
    String protocol = matcher.group(1);
    String authority = matcher.group(2);
    String path = matcher.group(3);
    String fragment = matcher.group(4);
}

```

### java_code_3.txt
```java
/* split a string using a pattern */
String[] strings = "abc\r\ndef\r\nghi".split("\r\n?");

```

### java_code_4.txt
```java
String str = "I am a string";
if (str.matches(".*string")) { // note: matches() tests if the entire string is a match
  System.out.println("ends with 'string'");
}

```

### java_code_5.txt
```java
import java.util.regex.*;
Pattern p = Pattern.compile("a*b");
Matcher m = p.matcher(str);
while (m.find()) {
  // use m.group() to extract matches
}

```

### java_code_6.txt
```java
String orig = "I am the original string";
String result = orig.replaceAll("original", "modified");
// result is now "I am the modified string"

```

## Python Code
### python_code_1.txt
```python
import re

string = "This is a string"

if re.search('string$', string):
    print("Ends with string.")

string = re.sub(" a ", " another ", string)
print(string)

```

