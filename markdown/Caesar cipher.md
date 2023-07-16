# Caesar cipher

## Task Link
[Rosetta Code - Caesar cipher](https://rosettacode.org/wiki/Caesar_cipher)

## Java Code
### java_code_1.txt
```java
public class Cipher {
    public static void main(String[] args) {

        String str = "The quick brown fox Jumped over the lazy Dog";

        System.out.println( Cipher.encode( str, 12 ));
        System.out.println( Cipher.decode( Cipher.encode( str, 12), 12 ));
    }

    public static String decode(String enc, int offset) {
        return encode(enc, 26-offset);
    }

    public static String encode(String enc, int offset) {
        offset = offset % 26 + 26;
        StringBuilder encoded = new StringBuilder();
        for (char i : enc.toCharArray()) {
            if (Character.isLetter(i)) {
                if (Character.isUpperCase(i)) {
                    encoded.append((char) ('A' + (i - 'A' + offset) % 26 ));
                } else {
                    encoded.append((char) ('a' + (i - 'a' + offset) % 26 ));
                }
            } else {
                encoded.append(i);
            }
        }
        return encoded.toString();
    }
}

```

## Python Code
### python_code_2.txt
```python
def caesar(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
				for i in s.upper()
				if ord(i) >= 65 and ord(i) <= 90 ])

msg = "The quick brown fox jumped over the lazy dogs"
print msg
enc = caesar(msg, 11)
print enc
print caesar(enc, 11, decode = True)

```

### python_code_3.txt
```python
import string
def caesar(s, k, decode = False):
   if decode: k = 26 - k
   return s.translate(
       string.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
           string.ascii_lowercase[k:] + string.ascii_lowercase[:k]
           )
       )
msg = "The quick brown fox jumped over the lazy dogs"
print msg
enc = caesar(msg, 11)
print enc
print caesar(enc, 11, decode = True)

```

### python_code_4.txt
```python
import string
def caesar(s, k = 13, decode = False, *, memo={}):
  if decode: k = 26 - k
  k = k % 26
  table = memo.get(k)
  if table is None:
    table = memo[k] = str.maketrans(
                        string.ascii_uppercase + string.ascii_lowercase,
                        string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
                        string.ascii_lowercase[k:] + string.ascii_lowercase[:k])
  return s.translate(table)

```

### python_code_5.txt
```python
from string import ascii_uppercase as abc

def caesar(s, k, decode = False):
    trans = dict(zip(abc, abc[(k,26-k)[decode]:] + abc[:(k,26-k)[decode]]))
    return ''.join(trans[L] for L in s.upper() if L in abc)

msg = "The quick brown fox jumped over the lazy dogs"
print(caesar(msg, 11))
print(caesar(caesar(msg, 11), 11, True))

```

