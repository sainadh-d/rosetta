# String prepend

## Task Link
[Rosetta Code - String prepend](https://rosettacode.org/wiki/String_prepend)

## Java Code
### java_code_1.txt
```java
String string = "def";
string = "abc" + string;

```

### java_code_2.txt
```java
String string = "def";
string = "abc".concat(string);

```

### java_code_3.txt
```java
StringBuilder string = new StringBuilder();
string.append("def");
string.insert(0, "abc");

```

### java_code_4.txt
```java
String string = "def";
string = String.format("abc%s", string);

```

### java_code_5.txt
```java
String string = "def";
string = "abc%s".formatted(string);

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = "12345678"
s = "0" + s  # by concatenation
print(s)

```

### python_code_2.txt
```python
s <- "12345678"
s <- ("0" + s)

```

