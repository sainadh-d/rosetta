# Create a file on magnetic tape

## Task Link
[Rosetta Code - Create a file on magnetic tape](https://rosettacode.org/wiki/Create_a_file_on_magnetic_tape)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;

public class CreateFile {
    public static void main(String[] args) throws IOException {
        String os = System.getProperty("os.name");
        if (os.contains("Windows")) {
            Path path = Paths.get("tape.file");
            Files.write(path, Collections.singletonList("Hello World!"));
        } else {
            Path path = Paths.get("/dev/tape");
            Files.write(path, Collections.singletonList("Hello World!"));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> with open('/dev/tape', 'w') as t: t.write('Hi Tape!\n')
... 
>>>

```

