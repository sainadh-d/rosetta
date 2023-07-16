# Create a file

## Task Link
[Rosetta Code - Create a file](https://rosettacode.org/wiki/Create_a_file)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.io.IOException;

```

### java_code_2.txt
```java
void create() throws IOException {
    File file = new File("output.txt");
    /* create an empty file */
    file.createNewFile();
    File directory = new File("docs/");
    /* create all parent directories */
    directory.mkdirs();
    File rootDirectory = new File("/docs/");
    rootDirectory.mkdirs();
}

```

### java_code_3.txt
```java
import java.io.*;
public class CreateFileTest {
	public static void main(String args[]) {
		try {
			new File("output.txt").createNewFile();
			new File(File.separator + "output.txt").createNewFile();
			new File("docs").mkdir();
			new File(File.separator + "docs").mkdir();
		} catch (IOException e) {
			System.err.println(e.getMessage());
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
import os
for directory in ['/', './']:
  open(directory + 'output.txt', 'w').close()  # create /output.txt, then ./output.txt
  os.mkdir(directory + 'docs')                 # create directory /docs, then ./docs

```

### python_code_2.txt
```python
from __future__ import with_statement
import os
def create(directory):
    with open(os.path.join(directory, "output.txt"), "w"):
        pass
    os.mkdir(os.path.join(directory, "docs"))
   
create(".") # current directory
create("/") # root directory

```

