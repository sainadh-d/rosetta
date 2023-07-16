# One-time pad

## Task Link
[Rosetta Code - One-time pad](https://rosettacode.org/wiki/One-time_pad)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class OneTimePad {

    public static void main(String[] args) {
        String controlName = "AtomicBlonde";
        generatePad(controlName, 5, 60, 65, 90);
        String text = "IT WAS THE BEST OF TIMES IT WAS THE WORST OF TIMES";
        String encrypted = parse(true, controlName, text.replaceAll(" ", ""));
        String decrypted = parse(false, controlName, encrypted);
        System.out.println("Input  text    = " + text);
        System.out.println("Encrypted text = " + encrypted);
        System.out.println("Decrypted text = " + decrypted);

        controlName = "AtomicBlondeCaseSensitive";
        generatePad(controlName, 5, 60, 32, 126);
        text = "It was the best of times, it was the worst of times.";
        encrypted = parse(true, controlName, text);
        decrypted = parse(false, controlName, encrypted);
        System.out.println();
        System.out.println("Input text     = " + text);
        System.out.println("Encrypted text = " + encrypted);
        System.out.println("Decrypted text = " + decrypted);
    }
    
    private static String parse(boolean encryptText, String controlName, String text) {
        StringBuilder sb = new StringBuilder();
        int minCh = 0;
        int maxCh = 0;
        Pattern minChPattern = Pattern.compile("^#  MIN_CH = ([\\d]+)$");
        Pattern maxChPattern = Pattern.compile("^#  MAX_CH = ([\\d]+)$");
        boolean validated = false;
        try (BufferedReader in = new BufferedReader(new FileReader(getFileName(controlName))); ) {
            String inLine = null;
            while ( (inLine = in.readLine()) != null ) {
                Matcher minMatcher = minChPattern.matcher(inLine);
                if ( minMatcher.matches() ) {
                    minCh = Integer.parseInt(minMatcher.group(1));
                    continue;
                }
                Matcher maxMatcher = maxChPattern.matcher(inLine);
                if ( maxMatcher.matches() ) {
                    maxCh = Integer.parseInt(maxMatcher.group(1));
                    continue;
                }
                if ( ! validated && minCh > 0 && maxCh > 0 ) {
                    validateText(text, minCh, maxCh);
                    validated = true;
                }
                //  # is comment.  - is used key. 
                if ( inLine.startsWith("#") || inLine.startsWith("-") ) {
                    continue;
                }
                //  Have encryption key.
                String key = inLine;
                if ( encryptText ) {
                    for ( int i = 0 ; i < text.length(); i++) {
                        sb.append((char) (((text.charAt(i) - minCh + key.charAt(i) - minCh) % (maxCh - minCh + 1)) + minCh));
                    }
                }
                else {
                    for ( int i = 0 ; i < text.length(); i++) {
                        int decrypt = text.charAt(i) - key.charAt(i);
                        if ( decrypt < 0 ) {
                            decrypt += maxCh - minCh + 1;
                        }
                        decrypt += minCh;
                        sb.append((char) decrypt);
                    }
                }
                break;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return sb.toString();
    }

    private static void validateText(String text, int minCh, int maxCh) {
        //  Validate text is in range
        for ( char ch : text.toCharArray() ) {
            if ( ch != ' ' && (ch < minCh || ch > maxCh) ) {
                throw new IllegalArgumentException("ERROR 103:  Invalid text.");
            }
        }
        
    }
    
    private static String getFileName(String controlName) {
        return controlName + ".1tp";
    }
    
    private static void generatePad(String controlName, int keys, int keyLength, int minCh, int maxCh) {
        Random random = new Random();
        try ( BufferedWriter writer = new BufferedWriter(new FileWriter(getFileName(controlName), false)); ) {
            writer.write("#  Lines starting with '#' are ignored.");
            writer.newLine();
            writer.write("#  Lines starting with '-' are previously used.");
            writer.newLine();
            writer.write("#  MIN_CH = " + minCh);
            writer.newLine();
            writer.write("#  MAX_CH = " + maxCh);
            writer.newLine();
            for ( int line = 0 ; line < keys ; line++ ) {
                StringBuilder sb = new StringBuilder();
                for ( int ch = 0 ; ch < keyLength ; ch++ ) {
                    sb.append((char) (random.nextInt(maxCh - minCh + 1) + minCh));
                }
                writer.write(sb.toString());
                writer.newLine();
            }
            writer.write("#  EOF");
            writer.newLine();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
"""One-time pad using an XOR cipher. Requires Python >=3.6."""

import argparse
import itertools
import pathlib
import re
import secrets
import sys


# One-time pad file signature.
MAGIC = "#one-time pad"


def make_keys(n, size):
    """Generate ``n`` secure, random keys of ``size`` bytes."""
    # We're generating and storing keys in their hexadecimal form to make
    # one-time pad files a little more human readable and to ensure a key
    # can not start with a hyphen.
    return (secrets.token_hex(size) for _ in range(n))


def make_pad(name, pad_size, key_size):
    """Create a new one-time pad identified by the given name.

    Args:
        name (str): Unique one-time pad identifier.
        pad_size (int): The number of keys (or pages) in the pad.
        key_size (int): The number of bytes per key.
    Returns:
        The new one-time pad as a string.
    """
    pad = [
        MAGIC,
        f"#name={name}",
        f"#size={pad_size}",
        *make_keys(pad_size, key_size),
    ]

    return "\n".join(pad)


def xor(message, key):
    """Return ``message`` XOR-ed with ``key``.

    Args:
        message (bytes): Plaintext or cyphertext to be encrypted or decrypted.
        key (bytes): Encryption and decryption key.
    Returns:
        Plaintext or cyphertext as a byte string.
    """
    return bytes(mc ^ kc for mc, kc in zip(message, itertools.cycle(key)))


def use_key(pad):
    """Use the next available key from the given one-time pad.

    Args:
        pad (str): A one-time pad.
    Returns:
        (str, str) A two-tuple of updated pad and key.
    """
    match = re.search(r"^[a-f0-9]+$", pad, re.MULTILINE)
    if not match:
        error("pad is all used up")

    key = match.group()
    pos = match.start()

    return (f"{pad[:pos]}-{pad[pos:]}", key)


def log(msg):
    """Log a message."""
    sys.stderr.write(msg)
    sys.stderr.write("\n")


def error(msg):
    """Exit with an error message."""
    sys.stderr.write(msg)
    sys.stderr.write("\n")
    sys.exit(1)


def write_pad(path, pad_size, key_size):
    """Write a new one-time pad to the given path.

    Args:
        path (pathlib.Path): Path to write one-time pad to.
        length (int): Number of keys in the pad.
    """
    if path.exists():
        error(f"pad '{path}' already exists")

    with path.open("w") as fd:
        fd.write(make_pad(path.name, pad_size, key_size))

    log(f"New one-time pad written to {path}")


def main(pad, message, outfile):
    """Encrypt or decrypt ``message`` using the given pad.

    Args:
        pad (pathlib.Path): Path to one-time pad.
        message (bytes): Plaintext or ciphertext message to encrypt or decrypt.
        outfile: File-like object to write to.
    """
    if not pad.exists():
        error(f"no such pad '{pad}'")

    with pad.open("r") as fd:
        if fd.readline().strip() != MAGIC:
            error(f"file '{pad}' does not look like a one-time pad")

    # Rewrites the entire one-time pad every time
    with pad.open("r+") as fd:
        updated, key = use_key(fd.read())

        fd.seek(0)
        fd.write(updated)

    outfile.write(xor(message, bytes.fromhex(key)))


if __name__ == "__main__":
    # Command line interface
    parser = argparse.ArgumentParser(description="One-time pad.")

    parser.add_argument(
        "pad",
        help=(
            "Path to one-time pad. If neither --encrypt or --decrypt "
            "are given, will create a new pad."
        ),
    )

    parser.add_argument(
        "--length",
        type=int,
        default=10,
        help="Pad size. Ignored if --encrypt or --decrypt are given. Defaults to 10.",
    )

    parser.add_argument(
        "--key-size",
        type=int,
        default=64,
        help="Key size in bytes. Ignored if --encrypt or --decrypt are given. Defaults to 64.",
    )

    parser.add_argument(
        "-o",
        "--outfile",
        type=argparse.FileType("wb"),
        default=sys.stdout.buffer,
        help=(
            "Write encoded/decoded message to a file. Ignored if --encrypt or "
            "--decrypt is not given. Defaults to stdout."
        ),
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--encrypt",
        metavar="FILE",
        type=argparse.FileType("rb"),
        help="Encrypt FILE using the next available key from pad.",
    )
    group.add_argument(
        "--decrypt",
        metavar="FILE",
        type=argparse.FileType("rb"),
        help="Decrypt FILE using the next available key from pad.",
    )

    args = parser.parse_args()

    if args.encrypt:
        message = args.encrypt.read()
    elif args.decrypt:
        message = args.decrypt.read()
    else:
        message = None

    # Sometimes necessary if message came from stdin
    if isinstance(message, str):
        message = message.encode()

    pad = pathlib.Path(args.pad).with_suffix(".1tp")

    if message:
        main(pad, message, args.outfile)
    else:
        write_pad(pad, args.length, args.key_size)

```

