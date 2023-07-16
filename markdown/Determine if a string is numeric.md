# Determine if a string is numeric

## Task Link
[Rosetta Code - Determine if a string is numeric](https://rosettacode.org/wiki/Determine_if_a_string_is_numeric)

## Java Code
### java_code_1.txt
```java
Integer.parseInt("12345")

```

### java_code_2.txt
```java
Float.parseFloat("123.456")

```

### java_code_3.txt
```java
public static void main(String[] args) {
    String value;
    value = "1234567";
    System.out.printf("%-10s %b%n", value, isInteger(value));
    value = "12345abc";
    System.out.printf("%-10s %b%n", value, isInteger(value));
    value = "-123.456";
    System.out.printf("%-10s %b%n", value, isFloatingPoint(value));
    value = "-.456";
    System.out.printf("%-10s %b%n", value, isFloatingPoint(value));
    value = "123.";
    System.out.printf("%-10s %b%n", value, isFloatingPoint(value));
    value = "123.abc";
    System.out.printf("%-10s %b%n", value, isFloatingPoint(value));
}

static boolean isInteger(String string) {
    String digits = "0123456789";
    for (char character : string.toCharArray()) {
        if (!digits.contains(String.valueOf(character)))
            return false;
    }
    return true;
}

static boolean isFloatingPoint(String string) {
    /* at least one decimal-point */
    int indexOf = string.indexOf('.');
    if (indexOf == -1)
        return false;
    /* assure only 1 decimal-point */
    if (indexOf != string.lastIndexOf('.'))
        return false;
    if (string.charAt(0) == '-' || string.charAt(0) == '+') {
        string = string.substring(1);
        indexOf--;
    }
    String integer = string.substring(0, indexOf);
    if (!integer.isEmpty()) {
        if (!isInteger(integer))
            return false;
    }
    String decimal = string.substring(indexOf + 1);
    if (!decimal.isEmpty())
        return isInteger(decimal);
    return true;
}

```

### java_code_4.txt
```java
public boolean isNumeric(String input) {
  try {
    Integer.parseInt(input);
    return true;
  }
  catch (NumberFormatException e) {
    // s is not numeric
    return false;
  }
}

```

### java_code_5.txt
```java
private static final boolean isNumeric(final String s) {
  if (s == null || s.isEmpty()) return false;
  for (int x = 0; x < s.length(); x++) {
    final char c = s.charAt(x);
    if (x == 0 && (c == '-')) continue;  // negative
    if ((c >= '0') && (c <= '9')) continue;  // 0 - 9
    return false; // invalid
  }
  return true; // valid
}

```

### java_code_6.txt
```java
public static boolean isNumeric(String inputData) {
  return inputData.matches("[-+]?\\d+(\\.\\d+)?");
}

```

### java_code_7.txt
```java
public static boolean isNumeric(String inputData) {
  NumberFormat formatter = NumberFormat.getInstance();
  ParsePosition pos = new ParsePosition(0);
  formatter.parse(inputData, pos);
  return inputData.length() == pos.getIndex();
}

```

### java_code_8.txt
```java
public static boolean isNumeric(String inputData) {
  Scanner sc = new Scanner(inputData);
  return sc.hasNextInt();
}

```

## Python Code
### python_code_1.txt
```python
def is_numeric(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False

is_numeric('123.0')

```

### python_code_2.txt
```python
'123'.isdigit()

```

### python_code_3.txt
```python
def is_numeric(literal):
    """Return whether a literal can be parsed as a numeric value"""
    castings = [int, float, complex,
        lambda s: int(s,2),  #binary
        lambda s: int(s,8),  #octal
        lambda s: int(s,16)] #hex
    for cast in castings:
        try:
            cast(literal)
            return True
        except ValueError:
            pass
    return False

```

### python_code_4.txt
```python
def numeric(literal):
    """Return value of numeric literal or None if can't parse a value"""
    castings = [int, float, complex,
        lambda s: int(s,2),  #binary
        lambda s: int(s,8),  #octal
        lambda s: int(s,16)] #hex
    for cast in castings:
        try:
            return cast(literal)
        except ValueError:
            pass
    return None


tests = [
    '0', '0.', '00', '123', '0123', '+123', '-123', '-123.', '-123e-4', '-.8E-04',
    '0.123', '(5)', '-123+4.5j', '0b0101', ' +0B101 ', '0o123', '-0xABC', '0x1a1',
    '12.5%', '1/2', '½', '3¼', 'π', 'Ⅻ', '1,000,000', '1 000', '- 001.20e+02', 
    'NaN', 'inf', '-Infinity']

for s in tests:
    print("%14s -> %-14s %-20s is_numeric: %-5s  str.isnumeric: %s" % (
        '"'+s+'"', numeric(s), type(numeric(s)), is_numeric(s), s.isnumeric() ))

```

### python_code_5.txt
```python
import re
numeric = re.compile('[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
is_numeric = lambda x: numeric.fullmatch(x) != None

is_numeric('123.0')

```

