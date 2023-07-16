# Bitwise IO

## Task Link
[Rosetta Code - Bitwise IO](https://rosettacode.org/wiki/Bitwise_IO)

## Java Code
## Python Code
### python_code_1.txt
```python
class BitWriter(object):
    def __init__(self, f):
        self.accumulator = 0
        self.bcount = 0
        self.out = f

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()

    def __del__(self):
        try:
            self.flush()
        except ValueError:   # I/O operation on closed file.
            pass

    def _writebit(self, bit):
        if self.bcount == 8:
            self.flush()
        if bit > 0:
            self.accumulator |= 1 << 7-self.bcount
        self.bcount += 1

    def writebits(self, bits, n):
        while n > 0:
            self._writebit(bits & 1 << n-1)
            n -= 1

    def flush(self):
        self.out.write(bytearray([self.accumulator]))
        self.accumulator = 0
        self.bcount = 0


class BitReader(object):
    def __init__(self, f):
        self.input = f
        self.accumulator = 0
        self.bcount = 0
        self.read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _readbit(self):
        if not self.bcount:
            a = self.input.read(1)
            if a:
                self.accumulator = ord(a)
            self.bcount = 8
            self.read = len(a)
        rv = (self.accumulator & (1 << self.bcount-1)) >> self.bcount-1
        self.bcount -= 1
        return rv

    def readbits(self, n):
        v = 0
        while n > 0:
            v = (v << 1) | self._readbit()
            n -= 1
        return v

if __name__ == '__main__':
    import os
    import sys
    # Determine this module's name from it's file name and import it.
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    bitio = __import__(module_name)

    with open('bitio_test.dat', 'wb') as outfile:
        with bitio.BitWriter(outfile) as writer:
            chars = '12345abcde'
            for ch in chars:
                writer.writebits(ord(ch), 7)

    with open('bitio_test.dat', 'rb') as infile:
        with bitio.BitReader(infile) as reader:
            chars = []
            while True:
                x = reader.readbits(7)
                if not reader.read:  # End-of-file?
                    break
                chars.append(chr(x))
            print(''.join(chars))

```

### python_code_2.txt
```python
import sys
import bitio

o = bitio.BitWriter(sys.stdout)
c = sys.stdin.read(1)
while len(c) > 0:
    o.writebits(ord(c), 7)
    c = sys.stdin.read(1)
o.flush()

```

### python_code_3.txt
```python
import sys
import bitio

r = bitio.BitReader(sys.stdin)
while True:
    x = r.readbits(7)
    if not r.read:  # nothing read
        break
    sys.stdout.write(chr(x))

```

