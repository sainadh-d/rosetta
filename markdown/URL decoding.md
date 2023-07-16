# URL decoding

## Task Link
[Rosetta Code - URL decoding](https://rosettacode.org/wiki/URL_decoding)

## Java Code
### java_code_1.txt
```java
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;

```

### java_code_2.txt
```java
URLDecoder.decode("http%3A%2F%2Ffoo%20bar%2F", StandardCharsets.UTF_8)

```

### java_code_3.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

```

### java_code_4.txt
```java
String decode(String string) {
    Pattern pattern = Pattern.compile("%([A-Za-z\\d]{2})");
    Matcher matcher = pattern.matcher(string);
    StringBuilder decoded = new StringBuilder(string);
    char character;
    int start, end, offset = 0;
    while (matcher.find()) {
        character = (char) Integer.parseInt(matcher.group(1), 16);
        /* offset the matched index since were adjusting the string */
        start = matcher.start() - offset;
        end = matcher.end() - offset;
        decoded.replace(start, end, String.valueOf(character));
        offset += 2;
    }
    return decoded.toString();
}

```

## Python Code
### python_code_1.txt
```python
#Python 2.X
import urllib
print urllib.unquote("http%3A%2F%2Ffoo%20bar%2F")
#Python 3.5+
from urllib.parse import unquote
print(unquote('http%3A%2F%2Ffoo%20bar%2F'))

```

