# Comma quibbling

## Task Link
[Rosetta Code - Comma quibbling](https://rosettacode.org/wiki/Comma_quibbling)

## Java Code
### java_code_1.txt
```java
public class Quibbler {

	public static String quibble(String[] words) {
		String qText = "{";
		for(int wIndex = 0; wIndex < words.length; wIndex++) {
			qText += words[wIndex] + (wIndex == words.length-1 ? "" : 
						  wIndex == words.length-2 ? " and " :
						  ", ";
		}
		qText += "}";
		return qText;
	}
	
	public static void main(String[] args) {
		System.out.println(quibble(new String[]{}));
		System.out.println(quibble(new String[]{"ABC"}));
		System.out.println(quibble(new String[]{"ABC", "DEF"}));
		System.out.println(quibble(new String[]{"ABC", "DEF", "G"}));
		System.out.println(quibble(new String[]{"ABC", "DEF", "G", "H"}));
	}
}

```

## Python Code
### python_code_2.txt
```python
>>> def strcat(sequence):
    return '{%s}' % ', '.join(sequence)[::-1].replace(',', 'dna ', 1)[::-1]

>>> for seq in ([], ["ABC"], ["ABC", "DEF"], ["ABC", "DEF", "G", "H"]):
    print('Input: %-24r -> Output: %r' % (seq, strcat(seq)))

	
Input: []                       -> Output: '{}'
Input: ['ABC']                  -> Output: '{ABC}'
Input: ['ABC', 'DEF']           -> Output: '{ABC and DEF}'
Input: ['ABC', 'DEF', 'G', 'H'] -> Output: '{ABC, DEF, G and H}'
>>>

```

### python_code_3.txt
```python
def commaQuibble(s):
    return '{%s}' % ' and '.join(s).replace(' and ', ', ', len(s) - 2)

for seq in ([], ["ABC"], ["ABC", "DEF"], ["ABC", "DEF", "G", "H"]):
	print('Input: %-24r -> Output: %r' % (seq, commaQuibble(seq)))

```

### python_code_4.txt
```python
>>> def quibble(s):
    return ('{' +
                (', '.join(s[:-1]) + ' and ' if len(s) > 1 else '') +
	        (s[-1] if s else '') +
	    '}')

>>> for seq in ([], ["ABC"], ["ABC", "DEF"], ["ABC", "DEF", "G", "H"]):
	print('Input: %-24r -> Output: %r' % (seq, quibble(seq)))

	
Input: []                       -> Output: '{}'
Input: ['ABC']                  -> Output: '{ABC}'
Input: ['ABC', 'DEF']           -> Output: '{ABC and DEF}'
Input: ['ABC', 'DEF', 'G', 'H'] -> Output: '{ABC, DEF, G and H}'
>>>

```

