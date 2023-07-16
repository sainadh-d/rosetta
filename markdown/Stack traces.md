# Stack traces

## Task Link
[Rosetta Code - Stack traces](https://rosettacode.org/wiki/Stack_traces)

## Java Code
### java_code_1.txt
```java
public class StackTracer {
    public static void printStackTrace() {
	StackTraceElement[] elems = Thread.currentThread().getStackTrace();

	System.out.println("Stack trace:");
	for (int i = elems.length-1, j = 2 ; i >= 3 ; i--, j+=2) {
	    System.out.printf("%" + j + "s%s.%s%n", "",
		    elems[i].getClassName(), elems[i].getMethodName());
	}
    }
}

```

### java_code_2.txt
```java
public class StackTraceDemo {
    static void inner() {
	StackTracer.printStackTrace();
    }
    static void middle() {
	inner();
    }
    static void outer() {
	middle();
    }
    public static void main(String[] args) {
	outer();
    }
}

```

## Python Code
### python_code_1.txt
```python
import traceback

def f(): return g()
def g(): traceback.print_stack()

f()

```

