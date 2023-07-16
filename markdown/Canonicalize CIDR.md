# Canonicalize CIDR

## Task Link
[Rosetta Code - Canonicalize CIDR](https://rosettacode.org/wiki/Canonicalize_CIDR)

## Java Code
### java_code_1.txt
```java
import java.text.MessageFormat;
import java.text.ParseException;

public class CanonicalizeCIDR {
    public static void main(String[] args) {
        for (String test : TESTS) {
            try {
                CIDR cidr = new CIDR(test);
                System.out.printf("%-18s -> %s\n", test, cidr.toString());
            } catch (Exception ex) {
                System.err.printf("Error parsing '%s': %s\n", test, ex.getLocalizedMessage());
            }
        }
    }

    private static class CIDR {
        private CIDR(int address, int maskLength) {
            this.address = address;
            this.maskLength = maskLength;
        }

        private CIDR(String str) throws Exception {
            Object[] args = new MessageFormat(FORMAT).parse(str);
            int address = 0;
            for (int i = 0; i < 4; ++i) {
                int a = ((Number)args[i]).intValue();
                if (a < 0 || a > 255)
                    throw new Exception("Invalid IP address");
                address <<= 8;
                address += a;
            }
            int maskLength = ((Number)args[4]).intValue();
            if (maskLength < 1 || maskLength > 32)
                throw new Exception("Invalid mask length");
            int mask = ~((1 << (32 - maskLength)) - 1);
            this.address = address & mask;
            this.maskLength = maskLength;
        }

        public String toString() {
            int address = this.address;
            int d = address & 0xFF;
            address >>= 8;
            int c = address & 0xFF;
            address >>= 8;
            int b = address & 0xFF;
            address >>= 8;
            int a = address & 0xFF;
            Object[] args = { a, b, c, d, maskLength };
            return new MessageFormat(FORMAT).format(args);
        }

        private int address;
        private int maskLength;
        private static final String FORMAT = "{0,number,integer}.{1,number,integer}.{2,number,integer}.{3,number,integer}/{4,number,integer}";
    };

    private static final String[] TESTS = {
        "87.70.141.1/22",
        "36.18.154.103/12",
        "62.62.197.11/29",
        "67.137.119.181/4",
        "161.214.74.21/24",
        "184.232.176.184/18"
    };
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# canonicalize a CIDR block specification:
# make sure none of the host bits are set

import sys
from socket import inet_aton, inet_ntoa
from struct import pack, unpack

args = sys.argv[1:]
if len(args) == 0:
    args = sys.stdin.readlines()

for cidr in args:
   # IP in dotted-decimal / bits in network part
   dotted, size_str = cidr.split('/')
   size = int(size_str)

   numeric = unpack('!I', inet_aton(dotted))[0]  # IP as an integer
   binary = f'{numeric:#034b}'                   # then as a padded binary string
   prefix = binary[:size + 2]                    # just the network part
                                                 #   (34 and +2 are to account
                                                 #    for leading '0b')

   canon_binary = prefix + '0' * (32 - size)     # replace host part with all zeroes
   canon_numeric = int(canon_binary, 2)          # convert back to integer
   canon_dotted = inet_ntoa(pack('!I',
                            (canon_numeric)))    # and then to dotted-decimal
   print(f'{canon_dotted}/{size}')               # output result

```

### python_code_2.txt
```python
"""Canonicalize CIDR"""
DIGITS = (24, 16, 8, 0)


def dotted_to_int(dotted: str) -> int:
    digits = [int(digit) for digit in dotted.split(".")]
    return sum(a << b for a, b in zip(digits, DIGITS))


def int_to_dotted(ip: int) -> str:
    digits = [(ip & (255 << d)) >> d for d in DIGITS]
    return ".".join(str(d) for d in digits)


def network_mask(number_of_bits: int) -> int:
    return ((1 << number_of_bits) - 1) << (32 - number_of_bits)


def canonicalize(ip: str) -> str:
    dotted, network_bits = ip.split("/")
    i = dotted_to_int(dotted)
    mask = network_mask(int(network_bits))
    return int_to_dotted(i & mask) + "/" + network_bits


TEST_CASES = [
    ("36.18.154.103/12", "36.16.0.0/12"),
    ("62.62.197.11/29", "62.62.197.8/29"),
    ("67.137.119.181/4", "64.0.0.0/4"),
    ("161.214.74.21/24", "161.214.74.0/24"),
    ("184.232.176.184/18", "184.232.128.0/18"),
]

if __name__ == "__main__":
    for ip, expect in TEST_CASES:
        rv = canonicalize(ip)
        print(f"{ip:<18} -> {rv}")
        assert rv == expect

```

### python_code_3.txt
```python
import ipaddress

def canonicalize(address: str) -> str:
    return str(ipaddress.ip_network(address, strict=False))

TEST_CASES = [
    ("36.18.154.103/12", "36.16.0.0/12"),
    ("62.62.197.11/29", "62.62.197.8/29"),
    ("67.137.119.181/4", "64.0.0.0/4"),
    ("161.214.74.21/24", "161.214.74.0/24"),
    ("184.232.176.184/18", "184.232.128.0/18"),
]

if __name__ == "__main__":
    for ip, expect in TEST_CASES:
        rv = canonicalize(ip)
        print(f"{ip:<18} -> {rv}")
        assert rv == expect, expect

```

