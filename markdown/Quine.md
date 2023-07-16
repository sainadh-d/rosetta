# Quine

## Task Link
[Rosetta Code - Quine](https://rosettacode.org/wiki/Quine)

## Java Code
### java_code_2.txt
```java
class S{public static void main(String[]a){String s="class S{public static void main(String[]a){String s=;char c=34;System.out.println(s.substring(0,52)+c+s+c+s.substring(52));}}";char c=34;System.out.println(s.substring(0,52)+c+s+c+s.substring(52));}}

```

### java_code_3.txt
```java
class S{public static void main(String[]a){String p="class S{public static void main(String[]a){String p=%c%s%1$c;System.out.printf(p,34,p);}}";System.out.printf(p,34,p);}}

```

## Python Code
### python_code_1.txt
```python
w = "print('w = ' + chr(34) + w + chr(34) + chr(10) + w)"
print('w = ' + chr(34) + w + chr(34) + chr(10) + w)

```

### python_code_10.txt
```python
data = (
	'ZGF0YSA9ICgKCSc=',
	'JywKCSc=',
	'JwopCnByZWZpeCwgc2VwYXJhdG9yLCBzdWZmaXggPSAoZC5kZWNvZGUoJ2Jhc2U2NCcpIGZvciBkIGluIGRhdGEpCnByaW50IHByZWZpeCArIGRhdGFbMF0gKyBzZXBhcmF0b3IgKyBkYXRhWzFdICsgc2VwYXJhdG9yICsgZGF0YVsyXSArIHN1ZmZpeA=='
)
prefix, separator, suffix = (d.decode('base64') for d in data)
print prefix + data[0] + separator + data[1] + separator + data[2] + suffix

```

### python_code_11.txt
```python
def applyToOwnSourceCode(functionBody):
	print "def applyToOwnSourceCode(functionBody):"
	print functionBody
	print "applyToOwnSourceCode(" + repr(functionBody) + ")"
applyToOwnSourceCode('\tprint "def applyToOwnSourceCode(functionBody):"\n\tprint functionBody\n\tprint "applyToOwnSourceCode(" + repr(functionBody) + ")"')

```

### python_code_2.txt
```python
x = 'x = %r\nprint(x %% x)'
print(x % x)

```

### python_code_3.txt
```python
x = 'x = {!r};print(x.format(x))';print(x.format(x))

```

### python_code_4.txt
```python
import sys; sys.stdout.write(open(sys.argv[0]).read())

```

### python_code_5.txt
```python
import sys,inspect;sys.stdout.write(inspect.getsource(inspect.currentframe()))

```

### python_code_6.txt
```python
exec(c:="print(f'exec(c:={chr(34)+c+chr(34)})')")

```

### python_code_7.txt
```python
print(__file__[:-3])

```

### python_code_8.txt
```python
x = """x = {0}{1}{0}
print x.format(chr(34)*3,x)"""
print x.format(chr(34)*3,x)

```

### python_code_9.txt
```python
a = 'YSA9ICcnCmIgPSBhLmRlY29kZSgnYmFzZTY0JykKcHJpbnQgYls6NV0rYStiWzU6XQ=='
b = a.decode('base64')
print b[:5]+a+b[5:]

```

