# Call a foreign-language function

## Task Link
[Rosetta Code - Call a foreign-language function](https://rosettacode.org/wiki/Call_a_foreign-language_function)

## Java Code
### java_code_1.txt
```java
public class JNIDemo
{
  static
  {  System.loadLibrary("JNIDemo");  }
  
  public static void main(String[] args)
  {
    System.out.println(callStrdup("Hello World!"));
  }
  
  private static native String callStrdup(String s);
}

```

### java_code_2.txt
```java
import com.stata.sfi.*;

public class HilbertMatrix {
    public static int run(String[] args) {
        int n, i, j;
        n = Integer.parseInt(args[1]);
        Matrix.createMatrix(args[0], n, n, 0.0);
        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                // Unlike Stata and the C API, indices are 0-based in the Java API.
                Matrix.storeMatrixAt(args[0], i, j, 1.0/(double)(i+j+1));
            }
        }
        return 0;
    }
}

```

## Python Code
### python_code_1.txt
```python
import ctypes
libc = ctypes.CDLL("/lib/libc.so.6")
libc.strcmp("abc", "def")     # -1
libc.strcmp("hello", "hello") #  0

```

