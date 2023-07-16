# String append

## Task Link
[Rosetta Code - String append](https://rosettacode.org/wiki/String_append)

## Java Code
### java_code_1.txt
```java
String string = "abc" + "def";

```

### java_code_2.txt
```java
String string = "abc";
string += "def";

```

### java_code_3.txt
```java
String string = "abc".concat("def");

```

### java_code_4.txt
```java
StringBuilder string = new StringBuilder();
string.append("abc").append("def");

```

### java_code_5.txt
```java
StringBuilder string = new StringBuilder();
string.append("abc");
string.insert(3, "def");

```

### java_code_6.txt
```java
String string = String.format("%s%s", "abc", "def");

```

### java_code_7.txt
```java
String string = "%s%s".formatted("abc", "def");

```

### java_code_8.txt
```java
String sa = "Hello";
sa += ", World!";
System.out.println(sa);

StringBuilder ba = new StringBuilder();
ba.append("Hello");
ba.append(", World!");
System.out.println(ba.toString());

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #

str = "12345678";
str += "9!";
print(str)

```

### python_code_2.txt
```python
s <- "12345678"
s <- (s + "9!")

```

