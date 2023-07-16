# Variable-length quantity

## Task Link
[Rosetta Code - Variable-length quantity](https://rosettacode.org/wiki/Variable-length_quantity)

## Java Code
### java_code_1.txt
```java
public class VLQCode
{
  public static byte[] encode(long n)
  {
    int numRelevantBits = 64 - Long.numberOfLeadingZeros(n);
    int numBytes = (numRelevantBits + 6) / 7;
    if (numBytes == 0)
      numBytes = 1;
    byte[] output = new byte[numBytes];
    for (int i = numBytes - 1; i >= 0; i--)
    {
      int curByte = (int)(n & 0x7F);
      if (i != (numBytes - 1))
        curByte |= 0x80;
      output[i] = (byte)curByte;
      n >>>= 7;
    }
    return output;
  }
  
  public static long decode(byte[] b)
  {
    long n = 0;
    for (int i = 0; i < b.length; i++)
    {
      int curByte = b[i] & 0xFF;
      n = (n << 7) | (curByte & 0x7F);
      if ((curByte & 0x80) == 0)
        break;
    }
    return n;
  }
  
  public static String byteArrayToString(byte[] b)
  {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < b.length; i++)
    {
      if (i > 0)
        sb.append(", ");
      String s = Integer.toHexString(b[i] & 0xFF);
      if (s.length() < 2)
        s = "0" + s;
      sb.append(s);
    }
    return sb.toString();
  }
  
  public static void main(String[] args)
  {
    long[] testNumbers = { 2097152, 2097151, 1, 127, 128, 589723405834L };
    for (long n : testNumbers)
    {
      byte[] encoded = encode(n);
      long decoded = decode(encoded);
      System.out.println("Original input=" + n + ", encoded = [" + byteArrayToString(encoded) + "], decoded=" + decoded + ", " + ((n == decoded) ? "OK" : "FAIL"));
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
def tobits(n, _group=8, _sep='_', _pad=False):
    'Express n as binary bits with separator'
    bits = '{0:b}'.format(n)[::-1]
    if _pad:
        bits = '{0:0{1}b}'.format(n,
                                  ((_group+len(bits)-1)//_group)*_group)[::-1]
        answer = _sep.join(bits[i:i+_group]
                                 for i in range(0, len(bits), _group))[::-1]
        answer = '0'*(len(_sep)-1) + answer
    else:
        answer = _sep.join(bits[i:i+_group]
                           for i in range(0, len(bits), _group))[::-1]
    return answer

def tovlq(n):
    return tobits(n, _group=7, _sep='1_', _pad=True)

def toint(vlq):
    return int(''.join(vlq.split('_1')), 2)    

def vlqsend(vlq):
    for i, byte in enumerate(vlq.split('_')[::-1]):
        print('Sent byte {0:3}: {1:#04x}'.format(i, int(byte,2)))

```

### python_code_2.txt
```python
>>> for n in (254, 255, 256, 257, -2+(1<<16), -1+(1<<16), 1<<16, 1+(1<<16), 0x200000, 0x1fffff ):
    print('int: %7i bin: %26s vlq: %35s vlq->int: %7i' % (n, tobits(n,_pad=True), tovlq(n), toint(tovlq(n))))

    
int:     254 bin:                   11111110 vlq:                   00000001_11111110 vlq->int:     254
int:     255 bin:                   11111111 vlq:                   00000001_11111111 vlq->int:     255
int:     256 bin:          00000001_00000000 vlq:                   00000010_10000000 vlq->int:     256
int:     257 bin:          00000001_00000001 vlq:                   00000010_10000001 vlq->int:     257
int:   65534 bin:          11111111_11111110 vlq:          00000011_11111111_11111110 vlq->int:   65534
int:   65535 bin:          11111111_11111111 vlq:          00000011_11111111_11111111 vlq->int:   65535
int:   65536 bin: 00000001_00000000_00000000 vlq:          00000100_10000000_10000000 vlq->int:   65536
int:   65537 bin: 00000001_00000000_00000001 vlq:          00000100_10000000_10000001 vlq->int:   65537
int: 2097152 bin: 00100000_00000000_00000000 vlq: 00000001_10000000_10000000_10000000 vlq->int: 2097152
int: 2097151 bin: 00011111_11111111_11111111 vlq:          01111111_11111111_11111111 vlq->int: 2097151
>>> vlqsend(tovlq(0x200000))
Sent byte   0: 0x80
Sent byte   1: 0x80
Sent byte   2: 0x80
Sent byte   3: 0x01
>>> vlqsend(tovlq(0x1fffff))
Sent byte   0: 0xff
Sent byte   1: 0xff
Sent byte   2: 0x7f
>>>

```

