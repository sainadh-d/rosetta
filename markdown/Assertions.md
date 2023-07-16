# Assertions

## Task Link
[Rosetta Code - Assertions](https://rosettacode.org/wiki/Assertions)

## Java Code
### java_code_1.txt
```java
assert valueA == valueB;

```

### java_code_2.txt
```java
if (valueA != valueB)
    throw new AssertionError();

```

### java_code_3.txt
```java
assert valueA == valueB : "valueA is not 42";

```

### java_code_4.txt
```java
assert valueA == valueB : valueA;

```

## Python Code
### python_code_1.txt
```python
a = 5
#...input or change a here
assert a == 42 # throws an AssertionError when a is not 42
assert a == 42, "Error message" # throws an AssertionError
       # when a is not 42 with "Error message" for the message
       # the error message can be any expression

```

