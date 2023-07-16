# Copy a string

## Task Link
[Rosetta Code - Copy a string](https://rosettacode.org/wiki/Copy_a_string)

## Java Code
### java_code_1.txt
```java
String src = "Hello";
String newAlias = src;
String strCopy = new String(src);

//"newAlias == src" is true
//"strCopy == src" is false
//"strCopy.equals(src)" is true

```

### java_code_2.txt
```java
StringBuffer srcCopy = new StringBuffer("Hello");

```

## Python Code
### python_code_1.txt
```python
>>> src = "hello"
>>> a = src
>>> b = src[:]
>>> import copy
>>> c = copy.copy(src)
>>> d = copy.deepcopy(src)
>>> src is a is b is c is d
True

```

### python_code_2.txt
```python
>>> a = 'hello'
>>> b = ''.join(a)
>>> a == b
True
>>> b is a  ### Might be True ... depends on "interning" implementation details!
False

```

