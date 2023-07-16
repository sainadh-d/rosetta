# Undefined values

## Task Link
[Rosetta Code - Undefined values](https://rosettacode.org/wiki/Undefined_values)

## Java Code
### java_code_1.txt
```java
String string = null;        // the variable string is undefined
System.out.println(string);           //prints "null" to std out
System.out.println(string.length());  // dereferencing null throws java.lang.NullPointerException

```

### java_code_2.txt
```java
int i = null;      // compilation error: incompatible types, required: int, found: <nulltype>
if (i == null) {   // compilation error: incomparable types: int and <nulltype>
    i = 1;
}

```

### java_code_3.txt
```java
Integer i = null;  // variable i is undefined
if (i == null) {
    i = 1;
}

```

## Python Code
### python_code_1.txt
```python
# Check to see whether a name is defined
try: name
except NameError: print "name is undefined at first check"

# Create a name, giving it a string value
name = "Chocolate"

# Check to see whether the name is defined now.
try: name
except NameError: print "name is undefined at second check"

# Remove the definition of the name.
del name

# Check to see whether it is defined after the explicit removal.
try: name
except NameError: print "name is undefined at third check"

# Recreate the name, giving it a value of 42
name = 42

# Check to see whether the name is defined now.
try: name
except NameError: print "name is undefined at fourth check"

# Because most of the output is conditional, this serves as
# a clear indicator that the program has run to completion.
print "Done"

```

