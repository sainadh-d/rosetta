# Vigenère cipher

## Task Link
[Rosetta Code - Vigenère cipher](https://rosettacode.org/wiki/Vigen%C3%A8re_cipher)

## Java Code
### java_code_1.txt
```java
public class VigenereCipher {
    public static void main(String[] args) {
        String key = "VIGENERECIPHER";
        String ori = "Beware the Jabberwock, my son! The jaws that bite, the claws that catch!";
        String enc = encrypt(ori, key);
        System.out.println(enc);
        System.out.println(decrypt(enc, key));
    }

    static String encrypt(String text, final String key) {
        String res = "";
        text = text.toUpperCase();
        for (int i = 0, j = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c < 'A' || c > 'Z') continue;
            res += (char)((c + key.charAt(j) - 2 * 'A') % 26 + 'A');
            j = ++j % key.length();
        }
        return res;
    }

    static String decrypt(String text, final String key) {
        String res = "";
        text = text.toUpperCase();
        for (int i = 0, j = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c < 'A' || c > 'Z') continue;
            res += (char)((c - key.charAt(j) + 26) % 26 + 'A');
            j = ++j % key.length();
        }
        return res;
    }
}

```

### java_code_2.txt
```java
import com.google.common.collect.Streams;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import static java.nio.charset.StandardCharsets.US_ASCII;

public class VigenereCipher {
    private final static int LOWER = 'A';
    private final static int UPPER = 'Z';
    private final static int SIZE = UPPER - LOWER + 1;
    private final Supplier<Stream<Character>> maskStream;

    public VigenereCipher(final String key) {
        final String mask = new String(key.getBytes(US_ASCII)).toUpperCase();
        maskStream = () ->
                Stream.iterate(0, i -> (i+1) % mask.length()).map(mask::charAt);
    }

    private String transform(final String text, final boolean encode) {
        final Stream<Integer> textStream = text.toUpperCase().chars().boxed()
                .filter(i -> i >= LOWER && i <= UPPER);
        return Streams.zip(textStream, maskStream.get(), (c, m) ->
                encode ? c + m - 2 * LOWER : c - m + SIZE)
            .map(c -> Character.toString(c % SIZE + LOWER))
            .collect(Collectors.joining());
    }

    public String encrypt(final String plaintext) {
        return transform(plaintext,true);
    }

    public String decrypt(final String ciphertext) {
        return transform(ciphertext,false);
    }
}

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class VigenereCipherTest {
    private static final VigenereCipher Vigenere = new VigenereCipher("VIGENERECIPHER");

    @Test
    @DisplayName("encipher/decipher round-trip succeeds")
    void vigenereCipherTest() {
        final String input = "Beware the Jabberwock, my son! The jaws that bite, the claws that catch!";
        final String expectEncrypted = "WMCEEIKLGRPIFVMEUGXQPWQVIOIAVEYXUEKFKBTALVXTGAFXYEVKPAGY";
        final String expectDecrypted = "BEWARETHEJABBERWOCKMYSONTHEJAWSTHATBITETHECLAWSTHATCATCH";

        final String ciphertext = Vigenere.encrypt(input);
        assertEquals(expectEncrypted, ciphertext);

        final String plaintext = Vigenere.decrypt(ciphertext);
        assertEquals(expectDecrypted, plaintext);
    }

}

```

## Python Code
### python_code_1.txt
```python
'''Vigenere encryption and decryption'''

from itertools import starmap, cycle


def encrypt(message, key):
    '''Vigenere encryption of message using key.'''

    # Converted to uppercase.
    # Non-alpha characters stripped out.
    message = filter(str.isalpha, message.upper())

    def enc(c, k):
        '''Single letter encryption.'''

        return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(enc, zip(message, cycle(key))))


def decrypt(message, key):
    '''Vigenere decryption of message using key.'''

    def dec(c, k):
        '''Single letter decryption.'''

        return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))

    return ''.join(starmap(dec, zip(message, cycle(key))))


def main():
    '''Demonstration'''

    text = 'Beware the Jabberwock, my son! The jaws that bite, ' + (
           'the claws that catch!'
    )
    key = 'VIGENERECIPHER'

    encr = encrypt(text, key)
    decr = decrypt(encr, key)

    print(text)
    print(encr)
    print(decr)


if __name__ == '__main__':
    main()

```

