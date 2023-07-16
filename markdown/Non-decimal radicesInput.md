# Non-decimal radices/Input

## Task Link
[Rosetta Code - Non-decimal radices/Input](https://rosettacode.org/wiki/Non-decimal_radices/Input)

## Java Code
### java_code_1.txt
```java
Scanner sc = new Scanner(System.in); //or any other InputStream or String
sc.useRadix(base); //any number from Character.MIN_RADIX (2) to CHARACTER.MAX_RADIX (36)
sc.nextInt(); //read in a value

```

### java_code_2.txt
```java
int number = Integer.parseInt(stringNum, base);

```

### java_code_3.txt
```java
Integer.decode("0xabcf123"); // hex
Integer.decode("07651");     // octal
Integer.decode("123459");    // decimal

```

## Python Code
### python_code_1.txt
```python
>>> text = '100'
>>> for base in range(2,21):
    print ("String '%s' in base %i is  %i in base 10" 
           % (text, base, int(text, base)))

  
String '100' in base 2 is  4 in base 10
String '100' in base 3 is  9 in base 10
String '100' in base 4 is  16 in base 10
String '100' in base 5 is  25 in base 10
String '100' in base 6 is  36 in base 10
String '100' in base 7 is  49 in base 10
String '100' in base 8 is  64 in base 10
String '100' in base 9 is  81 in base 10
String '100' in base 10 is  100 in base 10
String '100' in base 11 is  121 in base 10
String '100' in base 12 is  144 in base 10
String '100' in base 13 is  169 in base 10
String '100' in base 14 is  196 in base 10
String '100' in base 15 is  225 in base 10
String '100' in base 16 is  256 in base 10
String '100' in base 17 is  289 in base 10
String '100' in base 18 is  324 in base 10
String '100' in base 19 is  361 in base 10
String '100' in base 20 is  400 in base 10

```

