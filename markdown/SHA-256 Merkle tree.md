# SHA-256 Merkle tree

## Task Link
[Rosetta Code - SHA-256 Merkle tree](https://rosettacode.org/wiki/SHA-256_Merkle_tree)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.security.*;
import java.util.*;

public class SHA256MerkleTree {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("missing file argument");
            System.exit(1);
        }
        try (InputStream in = new BufferedInputStream(new FileInputStream(args[0]))) {
            byte[] digest = sha256MerkleTree(in, 1024);
            if (digest != null)
                System.out.println(digestToString(digest));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static String digestToString(byte[] digest) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < digest.length; ++i)
            result.append(String.format("%02x", digest[i]));
        return result.toString();
    }

    private static byte[] sha256MerkleTree(InputStream in, int blockSize) throws Exception {
        byte[] buffer = new byte[blockSize];
        int bytes;
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        List<byte[]> digests = new ArrayList<>();
        while ((bytes = in.read(buffer)) > 0) {
            md.reset();
            md.update(buffer, 0, bytes);
            digests.add(md.digest());
        }
        int length = digests.size();
        if (length == 0)
            return null;
        while (length > 1) {
            int j = 0;
            for (int i = 0; i < length; i += 2, ++j) {
                byte[] digest1 = digests.get(i);
                if (i + 1 < length) {
                    byte[] digest2 = digests.get(i + 1);
                    md.reset();
                    md.update(digest1);
                    md.update(digest2);
                    digests.set(j, md.digest());
                } else {
                    digests.set(j, digest1);
                }
            }
            length = j;
        }
        return digests.get(0);
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# compute the root label for a SHA256 Merkle tree built on blocks of a given
# size (default 1MB) taken from the given file(s)
import argh
import hashlib  
import sys
  
@argh.arg('filename', nargs='?', default=None)
def main(filename, block_size=1024*1024):
    if filename:
        fin = open(filename, 'rb')
    else: 
        fin = sys.stdin
    
    stack = []
    block = fin.read(block_size)
    while block:
        # a node is a pair: ( tree-level, hash )
        node = (0, hashlib.sha256(block).digest())
        stack.append(node)

        # concatenate adjacent pairs at the same level
        while len(stack) >= 2 and stack[-2][0] == stack[-1][0]:
            a = stack[-2]
            b = stack[-1]
            l = a[0]
            stack[-2:] = [(l+1, hashlib.sha256(a[1] + b[1]).digest())]

        block = fin.read(block_size)
    
    while len(stack) > 1:
        # at the end we have to concatenate even across levels
        a = stack[-2]
        b = stack[-1]
        al = a[0]
        bl = b[0]
        stack[-2:] = [(max(al, bl)+1, hashlib.sha256(a[1] + b[1]).digest())]

    print(stack[0][1].hex())


argh.dispatch_command(main)

```

