# Move-to-front algorithm

## Task Link
[Rosetta Code - Move-to-front algorithm](https://rosettacode.org/wiki/Move-to-front_algorithm)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;
import java.util.List;

public class MTF{
	public static List<Integer> encode(String msg, String symTable){
		List<Integer> output = new LinkedList<Integer>();
		StringBuilder s = new StringBuilder(symTable);
		for(char c : msg.toCharArray()){
			int idx = s.indexOf("" + c);
			output.add(idx);
			s = s.deleteCharAt(idx).insert(0, c);
		}
		return output;
	}
	
	public static String decode(List<Integer> idxs, String symTable){
		StringBuilder output = new StringBuilder();
		StringBuilder s = new StringBuilder(symTable);
		for(int idx : idxs){
			char c = s.charAt(idx);
			output = output.append(c);
			s = s.deleteCharAt(idx).insert(0, c);
		}
		return output.toString();
	}
	
	private static void test(String toEncode, String symTable){
		List<Integer> encoded = encode(toEncode, symTable);
		System.out.println(toEncode + ": " + encoded);
		String decoded = decode(encoded, symTable);
		System.out.println((toEncode.equals(decoded) ? "" : "in") + "correctly decoded to " + decoded);
	}
	
	public static void main(String[] args){
		String symTable = "abcdefghijklmnopqrstuvwxyz";
		test("broood", symTable);
		test("bananaaa", symTable);
		test("hiphophiphop", symTable);
	}
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
from string import ascii_lowercase

SYMBOLTABLE = list(ascii_lowercase)

def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence

def move2front_decode(sequence, symboltable):
    chars, pad = [], symboltable[::]
    for indx in sequence:
        char = pad[indx]
        chars.append(char)
        pad = [pad.pop(indx)] + pad
    return ''.join(chars)

if __name__ == '__main__':
    for s in ['broood', 'bananaaa', 'hiphophiphop']:
        encode = move2front_encode(s, SYMBOLTABLE)
        print('%14r encodes to %r' % (s, encode), end=', ')
        decode = move2front_decode(encode, SYMBOLTABLE)
        print('which decodes back to %r' % decode)
        assert s == decode, 'Whoops!'

```

### python_code_2.txt
```python
def m2f_e(s, st):
    return [[st.index(ch), st.insert(0, st.pop(st.index(ch)))][0] for ch in s]

def m2f_d(sq, st):
    return ''.join([st[i], st.insert(0, st.pop(i))][0] for i in sq)

ST = list('abcdefghijklmnopqrstuvwxyz')
for s in ['broood', 'bananaaa', 'hiphophiphop']:
    encode = m2f_e(s, ST[::])
    print('%14r encodes to %r' % (s, encode), end=', ')
    decode = m2f_d(encode, ST[::])
    print('decodes back to %r' % decode)
    assert s == decode, 'Whoops!'

```

