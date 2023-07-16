# Globally replace text in several files

## Task Link
[Rosetta Code - Globally replace text in several files](https://rosettacode.org/wiki/Globally_replace_text_in_several_files)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.nio.file.*;

public class GloballyReplaceText {

    public static void main(String[] args) throws IOException {

        for (String fn : new String[]{"test1.txt", "test2.txt"}) {
            String s = new String(Files.readAllBytes(Paths.get(fn)));
            s = s.replace("Goodbye London!", "Hello New York!");
            try (FileWriter fw = new FileWriter(fn)) {
                fw.write(s);
            }
        }
    }
}

```

### java_code_2.txt
```java
for (String fn : List.of("file1.txt","file2.txt")) {
	Path path = Path.of(fn);
	Files.writeString(path, 
		Files.readString(path).replace("Goodbye London!", "Hello New York!"));
}

```

## Python Code
### python_code_1.txt
```python
import fileinput

for line in fileinput.input(inplace=True):
    print(line.replace('Goodbye London!', 'Hello New York!'), end='')

```

