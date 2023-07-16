# Write entire file

## Task Link
[Rosetta Code - Write entire file](https://rosettacode.org/wiki/Write_entire_file)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class Test {

    public static void main(String[] args) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("test.txt"))) {
            bw.write("abc");
        }
    }
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public final class WriteEntireFile {

	public static void main(String[] aArgs) throws IOException {
		String contents = "Hello World";
		String filePath = "output.txt";
		
		Files.write(Path.of(filePath), contents.getBytes(), StandardOpenOption.CREATE);
	}

}

```

### java_code_3.txt
```java
package com.rosetta.example

import java.io.File
import java.io.PrintStream

class WriteFile {
    def static main( String ... args ) {
        val fout = new PrintStream(new File(args.get(0)))
        fout.println("Some text.")
        fout.close
    }
}

```

## Python Code
### python_code_1.txt
```python
with open(filename, 'w') as f:
    f.write(data)

```

### python_code_2.txt
```python
from pathlib import Path

Path(filename).write_text(any_string)
Path(filename).write_bytes(any_binary_data)

```

