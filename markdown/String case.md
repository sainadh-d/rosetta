# String case

## Task Link
[Rosetta Code - String case](https://rosettacode.org/wiki/String_case)

## Java Code
### java_code_1.txt
```java
String string = "alphaBETA".toUpperCase();

```

### java_code_2.txt
```java
String string = "alphaBETA".toLowerCase();

```

### java_code_3.txt
```java
String str = "alphaBETA";
System.out.println(str.toUpperCase());
System.out.println(str.toLowerCase());
//Also works with non-English characters with no modification
System.out.println("äàâáçñßæεбế".toUpperCase());
System.out.println("ÄÀÂÁÇÑSSÆΕБẾ".toLowerCase()); //does not transalate "SS" to "ß"

```

## Python Code
### python_code_1.txt
```python
s = "alphaBETA"
print s.upper() # => "ALPHABETA"
print s.lower() # => "alphabeta"

print s.swapcase() # => "ALPHAbeta"

print "fOo bAR".capitalize() # => "Foo bar"
print "fOo bAR".title() # => "Foo Bar"

import string
print string.capwords("fOo bAR") # => "Foo Bar"

```

### python_code_2.txt
```python
print "foo's bar".title()          # => "Foo'S Bar"
print string.capwords("foo's bar") # => "Foo's Bar"

```

