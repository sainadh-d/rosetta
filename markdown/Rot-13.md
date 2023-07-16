# Rot-13

## Task Link
[Rosetta Code - Rot-13](https://rosettacode.org/wiki/Rot-13)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class Rot13 {

    public static void main(String[] args) throws IOException {
        if (args.length >= 1) {
            for (String file : args) {
                try (InputStream in = new BufferedInputStream(new FileInputStream(file))) {
                    rot13(in, System.out);
                }
            }
        } else {
            rot13(System.in, System.out);
        }
    }

    private static void rot13(InputStream in, OutputStream out) throws IOException {
        int ch;
        while ((ch = in.read()) != -1) {
            out.write(rot13((char) ch));
        }
    }

    private static char rot13(char ch) {
        if (ch >= 'A' && ch <= 'Z') {
            return (char) (((ch - 'A') + 13) % 26 + 'A');
        }
        if (ch >= 'a' && ch <= 'z') {
            return (char) (((ch - 'a') + 13) % 26 + 'a');
        }
        return ch;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> u'foo'.encode('rot13')
'sbb'
>>> 'sbb'.decode('rot13')
u'foo'

```

### python_code_2.txt
```python
>>> import codecs
>>> codecs.encode("The quick brown fox jumps over the lazy dog", "rot13")
'Gur dhvpx oebja sbk whzcf bire gur ynml qbt'
>>> codecs.decode(_, "rot13")
'The quick brown fox jumps over the lazy dog'

```

### python_code_3.txt
```python
#!/usr/bin/env python
import string

TRANSLATION_TABLE = str.maketrans(
    string.ascii_uppercase + string.ascii_lowercase,
    string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
    string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
)


def rot13(s):
    """Return the rot-13 encoding of s."""
    return s.translate(TRANSLATION_TABLE)


if __name__ == "__main__":
    """rot-13 encode the input files, or stdin if no files are provided."""
    import fileinput
    for line in fileinput.input():
        print(rot13(line), end="")

```

### python_code_4.txt
```python
#!/usr/bin/env python
from __future__ import print_function
import string
lets = string.ascii_lowercase
key = {x:y for (x,y) in zip(lets[13:]+lets[:14], lets)}
key.update({x.upper():key[x].upper() for x in key.keys()})
encode = lambda x: ''.join((key.get(c,c) for c in x))
if __name__ == '__main__':
   """Peform line-by-line rot-13 encoding on any files listed on our
      command line or act as a standard UNIX filter (if no arguments
      specified).
   """
   import fileinput
   for line in fileinput.input():
      print(encode(line), end="")

```

### python_code_6.txt
```python
(rot13 "Moron")
=> "Zbeba"

```

