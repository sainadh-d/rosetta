# Repeat a string

## Task Link
[Rosetta Code - Repeat a string](https://rosettacode.org/wiki/Repeat_a_string)

## Java Code
### java_code_1.txt
```java
String funny = "ha" * 5;
String stars = '*' * 80;

```

### java_code_2.txt
```java
"ha".repeat(5);

```

### java_code_3.txt
```java
String[] strings = new String[5];
Arrays.fill(strings, "ha");
StringBuilder repeated = new StringBuilder();
for (String string : strings)
    repeated.append(string);

```

### java_code_4.txt
```java
String string = "ha";
StringBuilder repeated = new StringBuilder();
int count = 5;
while (count-- > 0)
    repeated.append(string);

```

### java_code_5.txt
```java
public static String repeat(String str, int times) {
    StringBuilder sb = new StringBuilder(str.length() * times);
    for (int i = 0; i < times; i++)
        sb.append(str);
    return sb.toString();
}

public static void main(String[] args) {
    System.out.println(repeat("ha", 5));
}

```

### java_code_6.txt
```java
public static String repeat(String str, int times) {
   return new String(new char[times]).replace("\0", str);
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    rep = repeat("ha", 5)
    println(rep)

def repeat(s, times):
    return s * times

```

### python_code_2.txt
```python
"ha" * 5  # ==> "hahahahaha"

```

### python_code_3.txt
```python
5 * "ha"  # ==> "hahahahaha"

```

### python_code_4.txt
```python
def repeat(s, times):
    return s * times

print(repeat("ha", 5))

```

### python_code_5.txt
```python
x = lambda a: a * 5
print(x("ha"))

```

