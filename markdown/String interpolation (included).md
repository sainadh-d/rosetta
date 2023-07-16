# String interpolation (included)

## Task Link
[Rosetta Code - String interpolation (included)](https://rosettacode.org/wiki/String_interpolation_(included))

## Java Code
### java_code_1.txt
```java
String adjective = "little";
String lyric = String.format("Mary had a %s lamb", adjective);

```

### java_code_2.txt
```java
String adjective = "little";
String lyric = "Mary had a %s lamb".formatted(adjective);

```

### java_code_3.txt
```java
String adjective = "little";
System.out.printf("Mary had a %s lamb", adjective);

```

### java_code_4.txt
```java
StringBuilder string = new StringBuilder();
Formatter formatter = new Formatter(string);
String adjective = "little";
formatter.format("Mary had a %s lamb", adjective);
formatter.flush();

```

### java_code_5.txt
```java
String original = "Mary had a X lamb";
String little = "little";
String replaced = original.replace("X", little); //does not change the original String
System.out.println(replaced);
//Alternative:
System.out.printf("Mary had a %s lamb.", little);
//Alternative:
String formatted = String.format("Mary had a %s lamb.", little);
System.out.println(formatted);

```

## Python Code
### python_code_1.txt
```python
>>> original = 'Mary had a %s lamb.'
>>> extra = 'little'
>>> original % extra
'Mary had a little lamb.'

```

### python_code_2.txt
```python
>>> original = 'Mary had a {extra} lamb.'
>>> extra = 'little'
>>> original.format(**locals())
'Mary had a little lamb.'

```

### python_code_3.txt
```python
>>> original = 'Mary had a {0} lamb.'
>>> extra = 'little'
>>> original.format(extra)
'Mary had a little lamb.'

```

### python_code_4.txt
```python
>>> from string import Template
>>> original = Template('Mary had a $extra lamb.')
>>> extra = 'little'
>>> original.substitute(**locals())
'Mary had a little lamb.'

```

### python_code_5.txt
```python
>>> extra = 'little'
>>> f'Mary had a {extra} lamb.'
'Mary had a little lamb.'
>>>

```

