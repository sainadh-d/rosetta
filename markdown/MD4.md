# MD4

## Task Link
[Rosetta Code - MD4](https://rosettacode.org/wiki/MD4)

## Java Code
### java_code_1.txt
```java
import org.bouncycastle.crypto.digests.MD4Digest;
import org.bouncycastle.util.encoders.Hex;

public class RosettaMD4
{
    public static void main (String[] argv) throws Exception
    {
        byte[] r = "Rosetta Code".getBytes("US-ASCII");
        MD4Digest d = new MD4Digest();
        d.update (r, 0, r.length);
        byte[] o = new byte[d.getDigestSize()];
        d.doFinal (o, 0);
        Hex.encode (o, System.out);
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
import hashlib
print hashlib.new("md4",raw_input().encode('utf-16le')).hexdigest().upper()

```

