# CRC-32

## Task Link
[Rosetta Code - CRC-32](https://rosettacode.org/wiki/CRC-32)

## Java Code
### java_code_1.txt
```java
import java.util.zip.CRC32;

```

### java_code_2.txt
```java
public static void main(String[] args) throws IOException {
    String string = "The quick brown fox jumps over the lazy dog";
    CRC32 crc = new CRC32();
    crc.update(string.getBytes());
    System.out.printf("%x", crc.getValue());
}

```

## Python Code
### python_code_1.txt
```python
>>> s = 'The quick brown fox jumps over the lazy dog'
>>> import zlib
>>> hex(zlib.crc32(s))
'0x414fa339'

>>> import binascii
>>> hex(binascii.crc32(s))
'0x414fa339'

```

### python_code_2.txt
```python
def create_table():
    a = []
    for i in range(256):
        k = i
        for j in range(8):
            if k & 1:
                k ^= 0x1db710640
            k >>= 1
        a.append(k)
    return a

def crc_update(buf, crc):
    crc ^= 0xffffffff
    for k in buf:
        crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ k]
    return crc ^ 0xffffffff
    
crc_table = create_table()
print(hex(crc_update(b"The quick brown fox jumps over the lazy dog", 0)))

```

### python_code_3.txt
```python
'''CRC-32 checksums for ascii strings'''

from functools import (reduce)
from itertools import (islice)


# crc32 :: String -> Int
def crc32(s):
    '''CRC-32 checksum for an ASCII encoded string'''
    def go(x):
        x2 = x >> 1
        return 0xedb88320 ^ x2 if x & 1 else x2
    table = [
        index(iterate(go)(n))(8)
        for n in range(0, 256)
    ]
    return reduce(
        lambda a, c: (a >> 8) ^ table[
            (a ^ ord(c)) & 0xff
        ],
        s,
        (0xffffffff)
    ) ^ 0xffffffff


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Test'''
    print(
        format(
            crc32('The quick brown fox jumps over the lazy dog'),
            '02x'
        )
    )


# ----------------------- GENERIC ------------------------

# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


if __name__ == '__main__':
    main()

```

