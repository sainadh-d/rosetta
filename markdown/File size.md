# File size

## Task Link
[Rosetta Code - File size](https://rosettacode.org/wiki/File_size)

## Java Code
### java_code_1.txt
```java
import java.io.File;

```

### java_code_2.txt
```java
public static void main(String[] args) {
    File fileA = new File("file.txt");
    System.out.printf("%,d B%n", fileA.length());
    File fileB = new File("/file.txt");
    System.out.printf("%,d B%n", fileB.length());
}

```

## Python Code
### python_code_1.txt
```python
import os

size = os.path.getsize('input.txt')
size = os.path.getsize('/input.txt')

```

