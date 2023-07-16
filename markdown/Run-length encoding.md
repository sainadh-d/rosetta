# Run-length encoding

## Task Link
[Rosetta Code - Run-length encoding](https://rosettacode.org/wiki/Run-length_encoding)

## Java Code
### java_code_1.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

```

### java_code_2.txt
```java
String encode(String string) {
    Pattern pattern = Pattern.compile("(.)\\1*");
    Matcher matcher = pattern.matcher(string);
    StringBuilder encoded = new StringBuilder();
    while (matcher.find()) {
        encoded.append(matcher.group().length());
        encoded.append(matcher.group().charAt(0));
    }
    return encoded.toString();
}

```

### java_code_3.txt
```java
String decode(String string) {
    Pattern pattern = Pattern.compile("(\\d+)(.)");
    Matcher matcher = pattern.matcher(string);
    StringBuilder decoded = new StringBuilder();
    int count;
    while (matcher.find()) {
        count = Integer.parseInt(matcher.group(1));
        decoded.append(matcher.group(2).repeat(count));
    }
    return decoded.toString();
}

```

### java_code_4.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class RunLengthEncoding {

    public static String encode(String source) {
        StringBuffer dest = new StringBuffer();
        for (int i = 0; i < source.length(); i++) {
            int runLength = 1;
            while (i+1 < source.length() && source.charAt(i) == source.charAt(i+1)) {
                runLength++;
                i++;
            }
            dest.append(runLength);
            dest.append(source.charAt(i));
        }
        return dest.toString();
    }

    public static String decode(String source) {
        StringBuffer dest = new StringBuffer();
        Pattern pattern = Pattern.compile("[0-9]+|[a-zA-Z]");
        Matcher matcher = pattern.matcher(source);
        while (matcher.find()) {
            int number = Integer.parseInt(matcher.group());
            matcher.find();
            while (number-- != 0) {
                dest.append(matcher.group());
            }
        }
        return dest.toString();
    }

    public static void main(String[] args) {
        String example = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW";
        System.out.println(encode(example));
        System.out.println(decode("1W1B1W1B1W1B1W1B1W1B1W1B1W1B"));
    }
}

```

### java_code_5.txt
```java
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class RunLengthEncodingTest {
	private RLE = new RunLengthEncoding();

	@Test
	public void encodingTest() {
		assertEquals("1W", RLE.encode("W"));
		assertEquals("4W", RLE.encode("WWWW"));
		assertEquals("5w4i7k3i6p5e4d2i1a",
				RLE.encode("wwwwwiiiikkkkkkkiiippppppeeeeeddddiia"));
		assertEquals("12B1N12B3N24B1N14B",
				RLE.encode("BBBBBBBBBBBBNBBBBBBBBBBBBNNNBBBBBBBBBBBBBBBBBBBBBBBBNBBBBBBBBBBBBBB"));
		assertEquals("12W1B12W3B24W1B14W",
				RLE.encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"));
		assertEquals("1W1B1W1B1W1B1W1B1W1B1W1B1W1B", RLE.encode("WBWBWBWBWBWBWB"));

	}

	@Test
	public void decodingTest() {
		assertEquals("W", RLE.decode("1W"));
		assertEquals("WWWW", RLE.decode("4W"));
		assertEquals("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
				RLE.decode("12W1B12W3B24W1B14W"));
		assertEquals("WBWBWBWBWBWBWB", RLE.decode("1W1B1W1B1W1B1W1B1W1B1W1B1W1B"));
		assertEquals("WBWBWBWBWBWBWB", RLE.decode("1W1B1W1B1W1B1W1B1W1B1W1B1W1B"));

	}
}

```

## Python Code
### python_code_1.txt
```python
def encode(input_string):
    count = 1
    prev = None
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        try:
            entry = (character, count)
            lst.append(entry)
            return (lst, 0)
        except Exception as e:
            print("Exception encountered {e}".format(e=e)) 
            return (e, 1)
 
def decode(lst):
    q = []
    for character, count in lst:
        q.append(character * count)
    return ''.join(q)
 
#Method call
value = encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
if value[1] == 0:
    print("Encoded value is {}".format(value[0]))
    decode(value[0])

```

### python_code_2.txt
```python
from itertools import groupby
def encode(input_string):
    return [(len(list(g)), k) for k,g in groupby(input_string)]

def decode(lst):
    return ''.join(c * n for n,c in lst)

encode("aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa")
decode([(5, 'a'), (6, 'h'), (7, 'm'), (1, 'u'), (7, 'i'), (6, 'a')])

```

### python_code_3.txt
```python
from re import sub

def encode(text):
    '''
    Doctest:
        >>> encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
        '12W1B12W3B24W1B14W'    
    '''
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               text)

def decode(text):
    '''
    Doctest:
        >>> decode('12W1B12W3B24W1B14W')
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    '''
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               text)

textin = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
assert decode(encode(textin)) == textin

```

