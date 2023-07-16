# Hello world/Line printer

## Task Link
[Rosetta Code - Hello world/Line printer](https://rosettacode.org/wiki/Hello_world/Line_printer)

## Java Code
### java_code_1.txt
```java
import java.io.FileWriter;
import java.io.IOException;
 
public class LinePrinter {
  public static void main(String[] args) {
    try {
      FileWriter lp0 = new FileWriter("/dev/lp0");
      lp0.write("Hello World!");
      lp0.close();
    } catch (IOException ioe) {
      ioe.printStackTrace();
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
lp = open("/dev/lp0")
lp.write("Hello World!\n")
lp.close()

```

### python_code_2.txt
```python
lp = open("/dev/lp0","w")
lp.write("Hello World!\n")
lp.close()

```

