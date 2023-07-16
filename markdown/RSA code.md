# RSA code

## Task Link
[Rosetta Code - RSA code](https://rosettacode.org/wiki/RSA_code)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args) {
    /*
    This is probably not the best method...or even the most optimized way...however it works since n and d are too big to be ints or longs
    This was also only tested with 'Rosetta Code' and 'Hello World'
    It's also pretty limited on plainText size (anything bigger than the above will fail)
    */
    BigInteger n = new BigInteger("9516311845790656153499716760847001433441357");
    BigInteger e = new BigInteger("65537");
    BigInteger d = new BigInteger("5617843187844953170308463622230283376298685");
    Charset c = Charsets.UTF_8;
    String plainText = "Rosetta Code";
    System.out.println("PlainText : " + plainText);
    byte[] bytes = plainText.getBytes();
    BigInteger plainNum = new BigInteger(bytes);
    System.out.println("As number : " + plainNum);
    BigInteger Bytes = new BigInteger(bytes);
    if (Bytes.compareTo(n) == 1) {
        System.out.println("Plaintext is too long");
        return;
    }
    BigInteger enc = plainNum.modPow(e, n);
    System.out.println("Encoded: " + enc);
    BigInteger dec = enc.modPow(d, n);
    System.out.println("Decoded: " + dec);
    String decText = new String(dec.toByteArray(), c);
    System.out.println("As text: " + decText);
}

```

### java_code_2.txt
```java
import java.math.BigInteger;
import java.util.Random;

public class rsaCode {
    public static void main(String[]args){
        //Size of primes
        int BIT_LENGTH = 4096;
        Random rand = new Random();
        //Generate primes and other necessary values
        BigInteger p = BigInteger.probablePrime(BIT_LENGTH / 2, rand);
        BigInteger q = BigInteger.probablePrime(BIT_LENGTH / 2, rand);
        BigInteger n = p.multiply(q);
        BigInteger phi = p.subtract(BigInteger.valueOf(1)).multiply(q.subtract(BigInteger.valueOf(1)));
        BigInteger e;
        BigInteger d;
        do {
            e = new BigInteger(phi.bitLength(), rand);
        } while (e.compareTo(BigInteger.valueOf(1)) <= 0 || e.compareTo(phi) >= 0 || !e.gcd(phi).equals(BigInteger.valueOf(1)));
        d = e.modInverse(phi);
        //Convert message to byte array and then to a BigInteger
        BigInteger message = new BigInteger("Hello World! - From Rosetta Code".getBytes());
        BigInteger cipherText = message.modPow(e, n);
        BigInteger decryptedText = cipherText.modPow(d, n);
        System.out.println("Message: " + message);
        System.out.println("Prime 1: " + p);
        System.out.println("Prime 2: " + q);
        System.out.println("Phi p1 * p2: " + phi);
        System.out.println("p1 * p2: " + n);
        System.out.println("Public key: " + e);
        System.out.println("Private key: " + d);
        System.out.println("Ciphertext: " + cipherText);
        System.out.println("Decrypted message(number form): " + decryptedText);
        //Convert BigInteger to byte array then to String
        System.out.println("Decrypted message(string): " + new String(decryptedText.toByteArray()));
    }
}

```

## Python Code
### python_code_1.txt
```python
import binascii

n = 9516311845790656153499716760847001433441357    # p*q = modulus
e = 65537
d = 5617843187844953170308463622230283376298685

message='Rosetta Code!'
print('message                 ', message)

hex_data   = binascii.hexlify(message.encode())
print('hex data                ', hex_data)

plain_text = int(hex_data, 16)
print('plain text integer      ', plain_text)

if plain_text > n:
  raise Exception('plain text too large for key')

encrypted_text = pow(plain_text,     e, n)
print('encrypted text integer  ', encrypted_text)

decrypted_text = pow(encrypted_text, d, n)
print('decrypted text integer  ', decrypted_text)

print('message                 ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())     # [2:] slicing, to strip the 0x part

```

