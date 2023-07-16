# Interactive programming (repl)

## Task Link
[Rosetta Code - Interactive programming (repl)](https://rosettacode.org/wiki/Interactive_programming_(repl))

## Java Code
### java_code_1.txt
```java
public static void main(String[] args) {
    System.out.println(concat("Rosetta", "Code", ":"));
}

public static String concat(String a, String b, String c) {
   return a + c + c + b;
}

Rosetta::Code

```

## Python Code
### python_code_1.txt
```python
python
Python 2.6.1 (r261:67517, Dec  4 2008, 16:51:00) [MSC v.1500 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def f(string1, string2, separator):
	return separator.join([string1, '', string2])

>>> f('Rosetta', 'Code', ':')
'Rosetta::Code'
>>>

```

