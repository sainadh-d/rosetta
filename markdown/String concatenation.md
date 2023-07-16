# String concatenation

## Task Link
[Rosetta Code - String concatenation](https://rosettacode.org/wiki/String_concatenation)

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
public class Str{
   public static void main(String[] args){
      String s = "hello";
      System.out.println(s + " literal");
      String s2 = s + " literal";
      System.out.println(s2);
   }
}

```

## Python Code
### python_code_1.txt
```python
s1 = "hello"
print s1 + " world"

s2 = s1 + " world"
print s2

```

### python_code_2.txt
```python
s1 = "hello"
print ", ".join([s1, "world", "mom"])

s2 = ", ".join([s1, "world", "mom"])
print s2

```

