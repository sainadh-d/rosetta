# Program termination

## Task Link
[Rosetta Code - Program termination](https://rosettacode.org/wiki/Program_termination)

## Java Code
### java_code_1.txt
```java
if(problem){
   System.exit(integerErrorCode); 
   //conventionally, error code 0 is the code for "OK",
   // while anything else is an actual problem
   //optionally: Runtime.getRuntime().exit(integerErrorCode);
}

```

### java_code_2.txt
```java
if(problem){
   Runtime.getRuntime().halt(integerErrorCode); 
   //conventionally, error code 0 is the code for "OK",
   // while anything else is an actual problem
}

```

## Python Code
### python_code_1.txt
```python
import sys
if problem:
    sys.exit(1)

```

### python_code_2.txt
```python
import os
if problem:
    os.abort()

```

