# String length

## Task Link
[Rosetta Code - String length](https://rosettacode.org/wiki/String_length)

## Java Code
### java_code_1.txt
```java
String s = "Hello, world!"; 
int byteCountUTF16 = s.getBytes("UTF-16").length; // Incorrect: it yields 28 (that is with the BOM)
int byteCountUTF16LE = s.getBytes("UTF-16LE").length; // Correct: it yields 26
int byteCountUTF8  = s.getBytes("UTF-8").length; // yields 13

```

### java_code_2.txt
```java
String s = "Hello, world!";
int not_really_the_length = s.length(); // XXX: does not (always) count Unicode characters (code points)!

```

### java_code_3.txt
```java
String str = "\uD834\uDD2A"; //U+1D12A
int not_really__the_length = str.length(); // value is 2, which is not the length in characters
int actual_length = str.codePointCount(0, str.length()); // value is 1, which is the length in characters

```

### java_code_4.txt
```java
import java.text.BreakIterator;

public class Grapheme {
  public static void main(String[] args) {
    printLength("møøse");
    printLength("𝔘𝔫𝔦𝔠𝔬𝔡𝔢");
    printLength("J̲o̲s̲é̲");
  }
  
  public static void printLength(String s) {
    BreakIterator it = BreakIterator.getCharacterInstance();
    it.setText(s);
    int count = 0;
    while (it.next() != BreakIterator.DONE) {
      count++;
    }
    System.out.println("Grapheme length: " + count+ " " + s);
  }
}

```

## Python Code
### python_code_1.txt
```python
print len('ascii')
# 5

```

### python_code_10.txt
```python
print(len("𝔘𝔫𝔦𝔠𝔬𝔡𝔢")) 
# 7

```

### python_code_11.txt
```python
import sys
sys.maxunicode # 1114111 on a wide build, 65535 on a narrow build

```

### python_code_12.txt
```python
print(len('ascii'))
# 5
print(len('\u05d0')) # the letter Alef as unicode literal
# 1

```

### python_code_13.txt
```python
print(len(b'\xd7\x90'.decode('utf-8'))) # Alef encoded as utf-8 byte sequence
# 1

```

### python_code_14.txt
```python
print(hex(sys.maxunicode), len(unichr(0x1F4A9)))
# ('0x10ffff', 1)

```

### python_code_15.txt
```python
print(hex(sys.maxunicode), len(unichr(0x1F4A9)))
# ('0xffff', 2)

```

### python_code_2.txt
```python
# The letter Alef
print len(u'\u05d0'.encode('utf-8'))
# 2
print len(u'\u05d0'.encode('iso-8859-8'))
# 1

```

### python_code_3.txt
```python
#!/bin/env python
# -*- coding: UTF-8 -*-
s = u"møøse"
assert len(s) == 5
assert len(s.encode('UTF-8')) == 7
assert len(s.encode('UTF-16-BE')) == 10 # There are 3 different UTF-16 encodings: LE and BE are little endian and big endian respectively, the third one (without suffix) adds 2 extra leading bytes: the byte-order mark (BOM).

```

### python_code_4.txt
```python
import sys
sys.maxunicode # 1114111 on a wide build, 65535 on a narrow build

```

### python_code_5.txt
```python
print len('ascii')
# 5
print len(u'\u05d0') # the letter Alef as unicode literal
# 1
print len('\xd7\x90'.decode('utf-8')) # Same encoded as utf-8 string
# 1
print hex(sys.maxunicode), len(unichr(0x1F4A9))
# ('0x10ffff', 1)

```

### python_code_6.txt
```python
print hex(sys.maxunicode), len(unichr(0x1F4A9))
# ('0xffff', 2)

```

### python_code_7.txt
```python
print(len(b'Hello, World!'))
# 13

```

### python_code_8.txt
```python
# The letter Alef
print(len('\u05d0'.encode())) # the default encoding is utf-8 in Python3
# 2
print(len('\u05d0'.encode('iso-8859-8')))
# 1

```

### python_code_9.txt
```python
#!/bin/env python
# -*- coding: UTF-8 -*-
s = "møøse"
assert len(s) == 5
assert len(s.encode('UTF-8')) == 7
assert len(s.encode('UTF-16-BE')) == 10 # There are 3 different UTF-16 encodings: LE and BE are little endian and big endian respectively, the third one (without suffix) adds 2 extra leading bytes: the byte-order mark (BOM).
u="𝔘𝔫𝔦𝔠𝔬𝔡𝔢"
assert len(u.encode()) == 28
assert len(u.encode('UTF-16-BE')) == 28

```

