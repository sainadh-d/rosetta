# URL encoding

## Task Link
[Rosetta Code - URL encoding](https://rosettacode.org/wiki/URL_encoding)

## Java Code
### java_code_1.txt
```java
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

```

### java_code_2.txt
```java
URLEncoder.encode("http://foo bar/", StandardCharsets.UTF_8)

```

### java_code_3.txt
```java
String encode(String string) {
    StringBuilder encoded = new StringBuilder();
    for (char character : string.toCharArray()) {
        switch (character) {
            /* rfc3986 and html5 */
            case '-', '.', '_', '~', '*' -> encoded.append(character);
            case ' ' -> encoded.append('+');
            default -> {
                if (alphanumeric(character))
                    encoded.append(character);
                else {
                    encoded.append("%");
                    encoded.append("%02x".formatted((int) character));
                }
            }
        }
    }
    return encoded.toString();
}

boolean alphanumeric(char character) {
    return (character >= 'A' && character <= 'Z')
        || (character >= 'a' && character <= 'z')
        || (character >= '0' && character <= '9');
}

```

## Python Code
### python_code_1.txt
```python
import urllib
s = 'http://foo/bar/'
s = urllib.quote(s)

```

