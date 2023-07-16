# MD5

## Task Link
[Rosetta Code - MD5](https://rosettacode.org/wiki/MD5)

## Java Code
### java_code_1.txt
```java
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Digester {

    public static void main(String[] args) {
        System.out.println(hexDigest("Rosetta code", "MD5"));
    }

    static String hexDigest(String str, String digestName) {
        try {
            MessageDigest md = MessageDigest.getInstance(digestName);
            byte[] digest = md.digest(str.getBytes(StandardCharsets.UTF_8));
            char[] hex = new char[digest.length * 2];
            for (int i = 0; i < digest.length; i++) {
                hex[2 * i] = "0123456789abcdef".charAt((digest[i] & 0xf0) >> 4);
                hex[2 * i + 1] = "0123456789abcdef".charAt(digest[i] & 0x0f);
            }
            return new String(hex);
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException(e);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import hashlib
>>> # RFC 1321    test suite:
>>> tests = (
  (b"", 'd41d8cd98f00b204e9800998ecf8427e'),
  (b"a", '0cc175b9c0f1b6a831c399e269772661'),
  (b"abc", '900150983cd24fb0d6963f7d28e17f72'),
  (b"message digest", 'f96b697d7cb7938d525a2f31aaf161d0'),
  (b"abcdefghijklmnopqrstuvwxyz", 'c3fcd3d76192e4007dfb496cca67e13b'),
  (b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 'd174ab98d277d9f5a5611c2c9f419d9f'),
  (b"12345678901234567890123456789012345678901234567890123456789012345678901234567890", '57edf4a22be3c955ac49da2e2107b67a') )
>>> for text, golden in tests: assert hashlib.md5(text).hexdigest() == golden

>>>

```

### python_code_2.txt
```python
>>> import hashlib
>>> print hashlib.md5("The quick brown fox jumped over the lazy dog's back").hexdigest()
e38ca1d920c4b8b8d3946b2c72f01680

```

### python_code_3.txt
```python
>>> import md5
>>> print md5.md5("The quick brown fox jumped over the lazy dog's back").hexdigest()
e38ca1d920c4b8b8d3946b2c72f01680

```

