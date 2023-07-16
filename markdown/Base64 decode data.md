# Base64 decode data

## Task Link
[Rosetta Code - Base64 decode data](https://rosettacode.org/wiki/Base64_decode_data)

## Java Code
### java_code_2.txt
```java
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Base64;

```

### java_code_3.txt
```java
void decodeToFile(String path, byte[] bytes) throws IOException {
    try (FileOutputStream stream = new FileOutputStream(path)) {
        byte[] decoded = Base64.getDecoder().decode(bytes);
        stream.write(decoded, 0, decoded.length);
    }
}

```

### java_code_4.txt
```java
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class Decode {
    public static void main(String[] args) {
        String data = "VG8gZXJyIGlzIGh1bWFuLCBidXQgdG8gcmVhbGx5IGZvdWwgdGhpbmdzIHVwIHlvdSBuZWVkIGEgY29tcHV0ZXIuCiAgICAtLSBQYXVsIFIuIEVocmxpY2g=";
        Base64.Decoder decoder = Base64.getDecoder();
        byte[] decoded = decoder.decode(data);
        String decodedStr = new String(decoded, StandardCharsets.UTF_8);
        System.out.println(decodedStr);
    }
}

```

## Python Code
### python_code_1.txt
```python
import base64
data = 'VG8gZXJyIGlzIGh1bWFuLCBidXQgdG8gcmVhbGx5IGZvdWwgdGhpbmdzIHVwIHlvdSBuZWVkIGEgY29tcHV0ZXIuCiAgICAtLSBQYXVsIFIuIEVocmxpY2g='
print(base64.b64decode(data).decode('utf-8'))

```

