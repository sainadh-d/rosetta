# Bitcoin/address validation

## Task Link
[Rosetta Code - Bitcoin/address validation](https://rosettacode.org/wiki/Bitcoin/address_validation)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;

public class BitcoinAddressValidator {

    private static final String ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";

    public static boolean validateBitcoinAddress(String addr) {
        if (addr.length() < 26 || addr.length() > 35)
            return false;
        byte[] decoded = decodeBase58To25Bytes(addr);
        if (decoded == null)
            return false;

        byte[] hash1 = sha256(Arrays.copyOfRange(decoded, 0, 21));
        byte[] hash2 = sha256(hash1);

        return Arrays.equals(Arrays.copyOfRange(hash2, 0, 4), Arrays.copyOfRange(decoded, 21, 25));
    }

    private static byte[] decodeBase58To25Bytes(String input) {
        BigInteger num = BigInteger.ZERO;
        for (char t : input.toCharArray()) {
            int p = ALPHABET.indexOf(t);
            if (p == -1)
                return null;
            num = num.multiply(BigInteger.valueOf(58)).add(BigInteger.valueOf(p));
        }

        byte[] result = new byte[25];
        byte[] numBytes = num.toByteArray();
        System.arraycopy(numBytes, 0, result, result.length - numBytes.length, numBytes.length);
        return result;
    }

    private static byte[] sha256(byte[] data) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(data);
            return md.digest();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException(e);
        }
    }

    public static void main(String[] args) {
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i", true);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62j", false);
        assertBitcoin("1Q1pE5vPGEEMqRcVRMbtBK842Y6Pzo6nK9", true);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62X", false);
        assertBitcoin("1ANNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i", false);
        assertBitcoin("1A Na15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i", false);
        assertBitcoin("BZbvjr", false);
        assertBitcoin("i55j", false);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62!", false);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62iz", false);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62izz", false);
        assertBitcoin("1Q1pE5vPGEEMqRcVRMbtBK842Y6Pzo6nJ9", false);
        assertBitcoin("1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62I", false);
    }

    private static void assertBitcoin(String address, boolean expected) {
        boolean actual = validateBitcoinAddress(address);
        if (actual != expected)
            throw new AssertionError(String.format("Expected %s for %s, but got %s.", expected, address, actual));
    }
}

```

## Python Code
### python_code_1.txt
```python
from hashlib import sha256

digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')
def check_bc(bc):
    try:
        bcbytes = decode_base58(bc, 25)
        return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]
    except Exception:
        return False

print(check_bc('1AGNa15ZQXAZUgFiqJ3i7Z2DPU2J6hW62i'))
print(check_bc("17NdbrSGoUotzeGCcMMCqnFkEvLymoou9j"))

```

### python_code_2.txt
```python
>>> n = 2491969579123783355964723219455906992268673266682165637887
>>> length = 25
>>> list( reversed(range(length)) )
[24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> assert n.to_bytes(length, 'big') == bytes( (n >> i*8) & 0xff for i in reversed(range(length)))
>>>

```

