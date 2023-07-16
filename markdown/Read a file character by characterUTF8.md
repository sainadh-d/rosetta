# Read a file character by character/UTF8

## Task Link
[Rosetta Code - Read a file character by character/UTF8](https://rosettacode.org/wiki/Read_a_file_character_by_character/UTF8)

## Java Code
### java_code_1.txt
```java
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

public class Program {
    private final FileReader reader;

    public Program(String path) throws IOException {
        reader = new FileReader(path, StandardCharsets.UTF_16);
    }

    /** @return integer value from 0 to 0xffff, or -1 for EOS */
    public int nextCharacter() throws IOException {
        return reader.read();
    }

    public void close() throws IOException {
        reader.close();
    }
}

```

### java_code_2.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

public final class ReadFileByCharacter {
	
	public static void main(String[] aArgs) {
		Path path = Path.of("input.txt");
		
		try ( BufferedReader reader = Files.newBufferedReader(path, StandardCharsets.UTF_8) ) {
			int value;
			while ( ( value = reader.read() ) != END_OF_STREAM ) {
				System.out.println((char) value);
			}
		} catch (IOException ioe) {
			ioe.printStackTrace();
		}	
	}
	
	private static final int END_OF_STREAM = -1;

}

```

## Python Code
### python_code_1.txt
```python
def get_next_character(f):
  # note: assumes valid utf-8
  c = f.read(1)
  while c:
    while True:
      try:
        yield c.decode('utf-8')
      except UnicodeDecodeError:
        # we've encountered a multibyte character
        # read another byte and try again
        c += f.read(1)
      else:
        # c was a valid char, and was yielded, continue
        c = f.read(1)
        break

# Usage:
with open("input.txt","rb") as f:
    for c in get_next_character(f):
        print(c)

```

### python_code_2.txt
```python
def get_next_character(f):
    """Reads one character from the given textfile"""
    c = f.read(1)
    while c: 
        yield c
        c = f.read(1)

# Usage: 
with open("input.txt", encoding="utf-8") as f:
    for c in get_next_character(f):
        print(c, sep="", end="")

```

