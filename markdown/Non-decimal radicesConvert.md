# Non-decimal radices/Convert

## Task Link
[Rosetta Code - Non-decimal radices/Convert](https://rosettacode.org/wiki/Non-decimal_radices/Convert)

## Java Code
### java_code_1.txt
```java
public static long backToTen(String num, int oldBase){
   return Long.parseLong(num, oldBase); //takes both uppercase and lowercase letters
}

public static String tenToBase(long num, int newBase){
   return Long.toString(num, newBase);//add .toUpperCase() for capital letters
}

```

### java_code_2.txt
```java
public static BigInteger backToTenBig(String num, int oldBase){
   return new BigInteger(num, oldBase); //takes both uppercase and lowercase letters
}

public static String tenBigToBase(BigInteger num, int newBase){
   return num.toString(newBase);//add .toUpperCase() for capital letters
}

```

## Python Code
### python_code_1.txt
```python
i = int('1a',16)  # returns the integer 26

```

### python_code_2.txt
```python
digits = "0123456789abcdefghijklmnopqrstuvwxyz"
def baseN(num, b):
    return digits[num] if num < b else baseN(num // b, b) + digits[num % b]

```

### python_code_3.txt
```python
digits = "0123456789abcdefghijklmnopqrstuvwxyz"

def baseN(num, b):
    result = []
    while num >= b:
        num, d = divmod(num, b)
        result.append(digits[d])
    result.append(digits[num])
    return ''.join(result[::-1])

```

