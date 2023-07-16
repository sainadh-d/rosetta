# Even or odd

## Task Link
[Rosetta Code - Even or odd](https://rosettacode.org/wiki/Even_or_odd)

## Java Code
### java_code_1.txt
```java
public static boolean isEven(int i){
    return (i & 1) == 0;
}

```

### java_code_2.txt
```java
public static boolean isEven(int i){
    return (i % 2) == 0;
}

```

### java_code_3.txt
```java
public static boolean isEven(BigInteger i){
    return i.and(BigInteger.ONE).equals(BigInteger.ZERO);
}

```

### java_code_4.txt
```java
public static boolean isEven(BigInteger i){
    return !i.testBit(0);
}

```

### java_code_5.txt
```java
public static boolean isEven(BigInteger i){
    return i.mod(BigInteger.valueOf(2)).equals(BigInteger.ZERO);
}

```

## Python Code
### python_code_1.txt
```python
>>> def is_odd(i): return bool(i & 1)

>>> def is_even(i): return not is_odd(i)

>>> [(j, is_odd(j)) for j in range(10)]
[(0, False), (1, True), (2, False), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, True)]
>>> [(j, is_even(j)) for j in range(10)]
[(0, True), (1, False), (2, True), (3, False), (4, True), (5, False), (6, True), (7, False), (8, True), (9, False)]
>>>

```

### python_code_2.txt
```python
>> def is_even(i):
        return (i % 2) == 0

>>> is_even(1)
False
>>> is_even(2)
True
>>>

```

