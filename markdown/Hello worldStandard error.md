# Hello world/Standard error

## Task Link
[Rosetta Code - Hello world/Standard error](https://rosettacode.org/wiki/Hello_world/Standard_error)

## Java Code
### java_code_1.txt
```java
public class Err{
   public static void main(String[] args){
      System.err.println("Goodbye, World!");
   }
}

```

## Python Code
### python_code_1.txt
```python
import sys

print >> sys.stderr, "Goodbye, World!"

```

### python_code_2.txt
```python
import sys

print("Goodbye, World!", file=sys.stderr)

```

### python_code_3.txt
```python
import sys

sys.stderr.write("Goodbye, World!\n")

```

