# Command-line arguments

## Task Link
[Rosetta Code - Command-line arguments](https://rosettacode.org/wiki/Command-line_arguments)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args)

```

### java_code_2.txt
```java
public class Arguments {
  public static void main(String[] args) {
     System.out.println("There are " + args.length + " arguments given.");
     for(int i = 0; i < args.length; i++) 
        System.out.println("The argument #" + (i+1) + " is " + args[i] + " and is at index " + i);
  }
}

```

## Python Code
### python_code_1.txt
```python
import sys
program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

```

