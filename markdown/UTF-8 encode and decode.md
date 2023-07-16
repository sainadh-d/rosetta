# UTF-8 encode and decode

## Task Link
[Rosetta Code - UTF-8 encode and decode](https://rosettacode.org/wiki/UTF-8_encode_and_decode)

## Java Code
### java_code_1.txt
```java
import java.nio.charset.StandardCharsets;
import java.util.Formatter;

public class UTF8EncodeDecode {

    public static byte[] utf8encode(int codepoint) {
        return new String(new int[]{codepoint}, 0, 1).getBytes(StandardCharsets.UTF_8);
    }

    public static int utf8decode(byte[] bytes) {
        return new String(bytes, StandardCharsets.UTF_8).codePointAt(0);
    }

    public static void main(String[] args) {
        System.out.printf("%-7s %-43s %7s\t%s\t%7s%n",
                "Char", "Name", "Unicode", "UTF-8 encoded", "Decoded");

        for (int codepoint : new int[]{0x0041, 0x00F6, 0x0416, 0x20AC, 0x1D11E}) {
            byte[] encoded = utf8encode(codepoint);
            Formatter formatter = new Formatter();
            for (byte b : encoded) {
                formatter.format("%02X ", b);
            }
            String encodedHex = formatter.toString();
            int decoded = utf8decode(encoded);
            System.out.printf("%-7c %-43s U+%04X\t%-12s\tU+%04X%n",
                    codepoint, Character.getName(codepoint), codepoint, encodedHex, decoded);
        }
    }
}

```

### java_code_2.txt
```java
import java.nio.charset.StandardCharsets;

Integer[] code_points = {0x0041, 0x00F6, 0x0416, 0x20AC, 0x1D11E};

void setup() {
  size(850, 230);
  background(255);
  fill(0);
  textSize(16);
  int tel_1 = 80;
  int tel_2 = 50;
  text("Char     Name                                                            Unicode          UTF-8 (encoding)      Decoded", 40, 40);
  for (int cp : code_points) {  
    byte[] encoded = new String(new int[]{cp}, 0, 1).getBytes(StandardCharsets.UTF_8);
    for (byte b : encoded) {                                                    
      text(hex(b), tel_2+530, tel_1);
      tel_2 += 30;
    }
    text(char(cp), 50, tel_1);
    text(Character.getName(cp), 100, tel_1);
    String unicode = hex(cp);
    while (unicode.length() > 4 && unicode.indexOf("0") == 0) unicode = unicode.substring(1);
    text("U+"+unicode, 450, tel_1);
    Character decoded = char(new String(encoded, StandardCharsets.UTF_8).codePointAt(0));
    text(decoded, 750, tel_1);
    tel_1 += 30;  tel_2 = 50;
  }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3
from unicodedata import name


def unicode_code(ch):
    return 'U+{:04x}'.format(ord(ch))


def utf8hex(ch):
    return " ".join([hex(c)[2:] for c in ch.encode('utf8')]).upper()


if __name__ == "__main__":
    print('{:<11} {:<36} {:<15} {:<15}'.format('Character', 'Name', 'Unicode', 'UTF-8 encoding (hex)'))
    chars = ['A', 'ö', 'Ж', '€', '𝄞']
    for char in chars:
        print('{:<11} {:<36} {:<15} {:<15}'.format(char, name(char), unicode_code(char), utf8hex(char)))

```

