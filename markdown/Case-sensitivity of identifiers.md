# Case-sensitivity of identifiers

## Task Link
[Rosetta Code - Case-sensitivity of identifiers](https://rosettacode.org/wiki/Case-sensitivity_of_identifiers)

## Java Code
### java_code_1.txt
```java
String dog = "Benjamin"; // convention: lower camelCase for variable and property names
String Dog = "Samba";    // convention: upper CamelCase for class, type, and constant names
String DOG = "Bernie";   // convention: all-caps only for constants

@Inject Console console;
console.print($"There are three dogs named {dog}, {Dog}, and {DOG}");

```

### java_code_2.txt
```java
String dog = "Benjamin";
String Dog = "Samba"; //in general, identifiers that start with capital letters are class names
String DOG = "Bernie"; //in general, identifiers in all caps are constants
//the conventions listed in comments here are not enforced by the language
System.out.println("There are three dogs named " + dog + ", " + Dog + ", and " + DOG + "'");

```

## Python Code
### python_code_1.txt
```python
dog = 'Benjamin'
Dog = 'Samba'
DOG = 'Bernie'

print(f"The three dogs are named {dog}, {Dog} and {DOG}.")

```

