# HTTP

## Task Link
[Rosetta Code - HTTP](https://rosettacode.org/wiki/HTTP)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;

```

### java_code_2.txt
```java
void printContent(String address) throws URISyntaxException, IOException {
    URL url = new URI(address).toURL();
    try (BufferedReader reader = new BufferedReader(new InputStreamReader(url.openStream()))) {
        String line;
        while ((line = reader.readLine()) != null)
            System.out.println(line);
    }
}

```

### java_code_3.txt
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.Charset;

public class Main {
    public static void main(String[] args) {
        var request = HttpRequest.newBuilder(URI.create("https://www.rosettacode.org"))
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

### java_code_4.txt
```java
import org.apache.commons.io.IOUtils;
import java.net.URL;

public class Main {	
    public static void main(String[] args) throws Exception {
        IOUtils.copy(new URL("http://rosettacode.org").openStream(),System.out);    	    	    		    
    }
}

```

## Python Code
### python_code_1.txt
```python
import urllib.request
print(urllib.request.urlopen("http://rosettacode.org").read())

```

### python_code_2.txt
```python
from http.client import HTTPConnection
conn = HTTPConnection("example.com")
# If you need to use set_tunnel, do so here.
conn.request("GET", "/")  
# Alternatively, you can use connect(), followed by the putrequest, putheader and endheaders functions.
result = conn.getresponse()
r1 = result.read() # This retrieves the entire contents.

```

### python_code_3.txt
```python
import urllib
print urllib.urlopen("http://rosettacode.org").read()

```

### python_code_4.txt
```python
import urllib2
print urllib2.urlopen("http://rosettacode.org").read()

```

### python_code_5.txt
```python
import requests
print(requests.get("http://rosettacode.org").text)

```

