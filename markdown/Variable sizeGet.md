# Variable size/Get

## Task Link
[Rosetta Code - Variable size/Get](https://rosettacode.org/wiki/Variable_size/Get)

## Java Code
### java_code_1.txt
```java
public final class VariableSize {

	public static void main(String[] aArgs) {		
		System.out.println("A  Byte    variable occupies: " + Byte.SIZE / 8 + " byte");
		System.out.println("A  Char    variable occupies: " + Character.SIZE / 8 + " bytes");
		System.out.println("A  Short   variable occupies: " + Short.SIZE / 8 + " bytes");
		System.out.println("A  Float   variable occupies: " + Float.SIZE / 8 + " bytes");
		System.out.println("An Integer variable occupies: " + Integer.SIZE / 8 + " bytes");
		System.out.println("A  Double  variable occupies: " + Double.SIZE / 8 + " bytes");		
		System.out.println("A  Long    variable occupies: " + Long.SIZE / 8 + " bytes");
	}

}

```

## Python Code
### python_code_1.txt
```python
>>> from array import array
>>> argslist = [('l', []), ('c', 'hello world'), ('u', u'hello \u2641'),
	('l', [1, 2, 3, 4, 5]), ('d', [1.0, 2.0, 3.14])]
>>> for typecode, initializer in argslist:
	a = array(typecode, initializer)
	print a, '\tSize =', a.buffer_info()[1] * a.itemsize
	del a

	
array('l') 	Size = 0
array('c', 'hello world') 	Size = 11
array('u', u'hello \u2641') 	Size = 14
array('l', [1, 2, 3, 4, 5]) 	Size = 20
array('d', [1.0, 2.0, 3.1400000000000001]) 	Size = 24
>>>

```

### python_code_2.txt
```python
import sys
sys.getsizeof(obj)

```

