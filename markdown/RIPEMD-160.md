# RIPEMD-160

## Task Link
[Rosetta Code - RIPEMD-160](https://rosettacode.org/wiki/RIPEMD-160)

## Java Code
### java_code_1.txt
```java
import org.bouncycastle.crypto.digests.RIPEMD160Digest;
import org.bouncycastle.util.encoders.Hex;

public class RosettaRIPEMD160
{
    public static void main (String[] argv) throws Exception
    {
        byte[] r = "Rosetta Code".getBytes("US-ASCII");
        RIPEMD160Digest d = new RIPEMD160Digest();
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
Python 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import hashlib
>>> h = hashlib.new('ripemd160')
>>> h.update(b"Rosetta Code")
>>> h.hexdigest()
'b3be159860842cebaa7174c8fff0aa9e50a5199f'
>>>

```

