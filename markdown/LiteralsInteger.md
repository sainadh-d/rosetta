# Literals/Integer

## Task Link
[Rosetta Code - Literals/Integer](https://rosettacode.org/wiki/Literals/Integer)

## Java Code
### java_code_1.txt
```java
public class IntegerLiterals {
    public static void main(String[] args) {
        System.out.println( 727 == 0x2d7 && 
                            727 == 01327   );
    }
}

```

### java_code_2.txt
```java
public class BinaryLiteral {
    public static void main(String[] args) {
        System.out.println( 727 == 0b10_1101_0111 );
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> # Bin(leading 0b or 0B), Oct(leading 0o or 0O), Dec, Hex(leading 0x or 0X), in order:
>>> 0b1011010111 == 0o1327 == 727 == 0x2d7
True
>>>

```

### python_code_2.txt
```python
>>> # Bin(leading 0b or 0B), Oct(leading 0o or 0O, or just 0), Dec, Hex(leading 0x or 0X), in order:
>>> 0b1011010111 == 0o1327 == 01327 == 727 == 0x2d7
True
>>>

```

### python_code_3.txt
```python
>>> # Oct(leading 0), Dec, Hex(leading 0x or 0X), in order:
>>> 01327 == 727 == 0x2d7
True
>>>

```

