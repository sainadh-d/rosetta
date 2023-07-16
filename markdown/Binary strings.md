# Binary strings

## Task Link
[Rosetta Code - Binary strings](https://rosettacode.org/wiki/Binary_strings)

## Java Code
### java_code_2.txt
```java
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class MutableByteString {

    private byte[] bytes;
    private int length;

    public MutableByteString(byte... bytes) {
        setInternal(bytes);
    }

    public int length() {
        return length;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public byte get(int index) {
        return bytes[check(index)];
    }

    public void set(byte[] bytes) {
        setInternal(bytes);
    }

    public void set(int index, byte b) {
        bytes[check(index)] = b;
    }

    public void append(byte b) {
        if (length >= bytes.length) {
            int len = 2 * bytes.length;
            if (len < 0)
                len = Integer.MAX_VALUE;
            bytes = Arrays.copyOf(bytes, len);
        }
        bytes[length] = b;
        length++;
    }

    public MutableByteString substring(int from, int to) {
        return new MutableByteString(Arrays.copyOfRange(bytes, from, to));
    }

    public void replace(byte[] from, byte[] to) {
        ByteArrayOutputStream copy = new ByteArrayOutputStream();
        if (from.length == 0) {
            for (byte b : bytes) {
                copy.write(to, 0, to.length);
                copy.write(b);
            }
            copy.write(to, 0, to.length);
        } else {
            for (int i = 0; i < length; i++) {
                if (regionEquals(i, from)) {
                    copy.write(to, 0, to.length);
                    i += from.length - 1;
                } else {
                    copy.write(bytes[i]);
                }
            }
        }
        set(copy.toByteArray());
    }

    public boolean regionEquals(int offset, MutableByteString other, int otherOffset, int len) {
        if (Math.max(offset, otherOffset) + len < 0)
            return false;
        if (offset + len > length || otherOffset + len > other.length())
            return false;
        for (int i = 0; i < len; i++) {
            if (bytes[offset + i] != other.get(otherOffset + i))
                return false;
        }
        return true;
    }

    public String toHexString() {
        char[] hex = new char[2 * length];
        for (int i = 0; i < length; i++) {
            hex[2 * i] = "0123456789abcdef".charAt(bytes[i] >> 4 & 0x0F);
            hex[2 * i + 1] = "0123456789abcdef".charAt(bytes[i] & 0x0F);
        }
        return new String(hex);
    }

    public String toStringUtf8() {
        return new String(bytes, 0, length, StandardCharsets.UTF_8);
    }

    private void setInternal(byte[] bytes) {
        this.bytes = bytes.clone();
        this.length = bytes.length;
    }

    private boolean regionEquals(int offset, byte[] other) {
        int len = other.length;
        if (offset < 0 || offset + len < 0)
            return false;
        if (offset + len > length)
            return false;
        for (int i = 0; i < len; i++) {
            if (bytes[offset + i] != other[i])
                return false;
        }
        return true;
    }

    private int check(int index) {
        if (index < 0 || index >= length)
            throw new IndexOutOfBoundsException(String.valueOf(index));
        return index;
    }
}

```

### java_code_3.txt
```java
import static org.hamcrest.CoreMatchers.is;

import java.nio.charset.StandardCharsets;
import org.junit.Assert;
import org.junit.Test;

public class MutableByteStringTest {

    @Test
    public void testReplaceEmpty() {
        MutableByteString str = new MutableByteString("hello".getBytes(StandardCharsets.UTF_8));
        str.replace(new byte[]{}, new byte[]{'-'});

        Assert.assertThat(str.toStringUtf8(), is("-h-e-l-l-o-"));
    }

    @Test
    public void testReplaceMultiple() {
        MutableByteString str = new MutableByteString("hello".getBytes(StandardCharsets.UTF_8));
        str.replace(new byte[]{'l'}, new byte[]{'1', '2', '3'});

        Assert.assertThat(str.toStringUtf8(), is("he123123o"));
    }

    @Test
    public void testToHexString() {
        MutableByteString str = new MutableByteString("hello".getBytes(StandardCharsets.UTF_8));

        Assert.assertThat(str.toHexString(), is("68656c6c6f"));
    }

    @Test
    public void testAppend() {
        MutableByteString str = new MutableByteString("hello".getBytes(StandardCharsets.UTF_8));
        str.append((byte) ',');
        str.append((byte) ' ');
        str.append((byte) 'w');
        str.append((byte) 'o');
        str.append((byte) 'r');
        str.append((byte) 'l');
        str.append((byte) 'd');

        Assert.assertThat(str.toStringUtf8(), is("hello, world"));
    }
    @Test
    public void testSubstring() {
        MutableByteString str = new MutableByteString("hello, world".getBytes(StandardCharsets.UTF_8));

        Assert.assertThat(str.substring(0, 5).toStringUtf8(), is("hello"));
        Assert.assertThat(str.substring(7, 12).toStringUtf8(), is("world"));
    }

    @Test
    public void testRegionEquals() {
        MutableByteString str = new MutableByteString("hello".getBytes(StandardCharsets.UTF_8));

        Assert.assertThat(str.regionEquals(0, new MutableByteString(new byte[]{'h'}), 0, 1), is(true));
        Assert.assertThat(str.regionEquals(0, new MutableByteString(new byte[]{'h'}), 0, 2), is(false));
    }
}

```

## Python Code
### python_code_1.txt
```python
s1 = "A 'string' literal \n"
s2 = 'You may use any of \' or " as delimiter'
s3 = """This text 
   goes over several lines
       up to the closing triple quote"""

```

### python_code_10.txt
```python
items = ["Smith", "John", "417 Evergreen Av", "Chimichurri", "481-3172"]
joined = ",".join(items)
print joined
# output:
# Smith,John,417 Evergreen Av,Chimichurri,481-3172

```

### python_code_11.txt
```python
line = "Smith,John,417 Evergreen Av,Chimichurri,481-3172"
fields = line.split(',')
print fields
# output:
# ['Smith', 'John', '417 Evergreen Av', 'Chimichurri', '481-3172']

```

### python_code_12.txt
```python
s1 = b"A 'byte string' literal \n"
s2 = b'You may use any of \' or " as delimiter'
s3 = b"""This text 
   goes over several lines
       up to the closing triple quote"""

```

### python_code_13.txt
```python
x = b'abc'
x[0] # evaluates to 97

```

### python_code_14.txt
```python
x = b'abc'
list(x) # evaluates to [97, 98, 99]
bytes([97, 98, 99]) # evaluates to b'abc'

```

### python_code_2.txt
```python
s = "Hello "
t = "world!"
u = s + t   # + concatenates

```

### python_code_3.txt
```python
assert "Hello" == 'Hello'
assert '\t' == '\x09'
assert "one" < "two"
assert "two" >= "three"

```

### python_code_4.txt
```python
if x=='': print "Empty string"
if not x: print "Empty string, provided you know x is a string"

```

### python_code_5.txt
```python
txt = "Some text"
txt += '\x07'
# txt refers now to a new string having "Some text\x07"

```

### python_code_6.txt
```python
txt = "Some more text"
assert txt[4] == " "
assert txt[0:4] == "Some"
assert txt[:4] == "Some" # you can omit the starting index if 0
assert txt[5:9] == "more"
assert txt[5:] == "more text" # omitting the second index means "to the end"

```

### python_code_7.txt
```python
txt = "Some more text"
assert txt[-1] == "t"
assert txt[-4:] == "text"

```

### python_code_8.txt
```python
v1 = "hello world"
v2 = v1.replace("l", "L")
print v2 # prints heLLo worLd

```

### python_code_9.txt
```python
v1 = "hello" 
v2 = "world"
msg = v1 + " " + v2

```

