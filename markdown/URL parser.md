# URL parser

## Task Link
[Rosetta Code - URL parser](https://rosettacode.org/wiki/URL_parser)

## Java Code
### java_code_1.txt
```java
URI uri;
try {
    uri = new URI("foo://example.com:8042/over/there?name=ferret#nose");
} catch (URISyntaxException exception) {
    /* invalid URI */
}

```

### java_code_2.txt
```java
uri.getScheme()

```

### java_code_3.txt
```java
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class MailTo {
    private final To to;
    private List<Field> fields;

    public MailTo(String string) {
        if (string == null)
            throw new NullPointerException();
        if (string.isBlank() || !string.toLowerCase().startsWith("mailto:"))
            throw new IllegalArgumentException("Requires 'mailto' scheme");
        string = string.substring(string.indexOf(':') + 1);
        /* we can use the 'URLDecoder' class to decode any entities */
        string = URLDecoder.decode(string, StandardCharsets.UTF_8);
        /* the address and fields are separated by a '?' */
        int indexOf = string.indexOf('?');
        String[] address;
        if (indexOf == -1)
            address = string.split("@");
        else {
            address = string.substring(0, indexOf).split("@");
            string = string.substring(indexOf + 1);
            /* each field is separated by a '&' */
            String[] fields = string.split("&");
            String[] field;
            this.fields = new ArrayList<>(fields.length);
            for (String value : fields) {
                field = value.split("=");
                this.fields.add(new Field(field[0], field[1]));
            }
        }
        to = new To(address[0], address[1]);
    }

    record To(String user, String host) { }
    record Field(String name, String value) { }
}

```

## Python Code
### python_code_1.txt
```python
import urllib.parse as up # urlparse for Python v2

url = up.urlparse('http://user:pass@example.com:8081/path/file.html;params?query1=1#fragment')

print('url.scheme = ', url.scheme)
print('url.netloc = ', url.netloc)
print('url.hostname = ', url.hostname)
print('url.port = ', url.port)
print('url.path = ', url.path)
print('url.params = ', url.params)
print('url.query = ', url.query)
print('url.fragment = ', url.fragment)
print('url.username = ', url.username)
print('url.password = ', url.password)

```

