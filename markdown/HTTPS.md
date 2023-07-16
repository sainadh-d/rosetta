# HTTPS

## Task Link
[Rosetta Code - HTTPS](https://rosettacode.org/wiki/HTTPS)

## Java Code
### java_code_1.txt
```java
URL url = new URL("https://sourceforge.net");
HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
Scanner scanner = new Scanner(connection.getInputStream());

while (scanner.hasNext()) {
    System.out.println(scanner.next());
}

```

### java_code_2.txt
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.Charset;

public class Main {
    public static void main(String[] args) {
        var request = HttpRequest.newBuilder(URI.create("https://sourceforge.net"))
                .GET()
                .build();

        HttpClient.newHttpClient()
                .sendAsync(request, HttpResponse.BodyHandlers.ofString(Charset.defaultCharset()))
                .thenApply(HttpResponse::body)
                .thenAccept(System.out::println)
                .join();
    }
}

```

## Python Code
### python_code_1.txt
```python
import urllib.request
print(urllib.request.urlopen("https://sourceforge.net/").read())

```

