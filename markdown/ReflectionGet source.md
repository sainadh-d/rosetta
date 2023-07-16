# Reflection/Get source

## Task Link
[Rosetta Code - Reflection/Get source](https://rosettacode.org/wiki/Reflection/Get_source)

## Java Code
### java_code_1.txt
```java
public class ReflectionGetSource {

    public static void main(String[] args) {
        new ReflectionGetSource().method1();

    }
    
    public ReflectionGetSource() {}
    
    public void method1() {
        method2();
    }
    
    public void method2() {
        method3();
    }
    
    public void method3() {
        Throwable t = new Throwable();
        for ( StackTraceElement ste : t.getStackTrace() ) {
            System.out.printf("File Name   = %s%n", ste.getFileName());
            System.out.printf("Class Name  = %s%n", ste.getClassName());
            System.out.printf("Method Name = %s%n", ste.getMethodName());
            System.out.printf("Line number = %s%n%n", ste.getLineNumber());
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
import os
os.__file__
# "/usr/local/lib/python3.5/os.pyc"

```

