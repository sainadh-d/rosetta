# Walk a directory/Recursively

## Task Link
[Rosetta Code - Walk a directory/Recursively](https://rosettacode.org/wiki/Walk_a_directory/Recursively)

## Java Code
### java_code_1.txt
```java
import java.io.File;

public class MainEntry {
    public static void main(String[] args) {
        walkin(new File("/home/user")); //Replace this with a suitable directory
    }
    
    /**
     * Recursive function to descend into the directory tree and find all the files 
     * that end with ".mp3"
     * @param dir A file object defining the top directory
     **/
    public static void walkin(File dir) {
        String pattern = ".mp3";
        
        File listFile[] = dir.listFiles();
        if (listFile != null) {
            for (int i=0; i<listFile.length; i++) {
                if (listFile[i].isDirectory()) {
                    walkin(listFile[i]);
                } else {
                    if (listFile[i].getName().endsWith(pattern)) {
                        System.out.println(listFile[i].getPath());
                    }
                }
            }
        }
    }
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
 
public class WalkTree {
	public static void main(String[] args) throws IOException {
		Path start = FileSystems.getDefault().getPath("/path/to/file");
		Files.walkFileTree(start, new SimpleFileVisitor<Path>() {
			@Override
			public FileVisitResult visitFile(Path file,
					BasicFileAttributes attrs) throws IOException {
				if (file.toString().endsWith(".mp3")) {
					System.out.println(file);
				}
				return FileVisitResult.CONTINUE;
			}
		});
	}
}

```

### java_code_3.txt
```java
import java.io.IOException;
import java.nio.file.*;

public class WalkTree {
	public static void main(String[] args) throws IOException {
		Path start = FileSystems.getDefault().getPath("/path/to/file");
		Files.walk(start)
		     .filter( path -> path.toFile().isFile())
		     .filter( path -> path.toString().endsWith(".mp3"))
		     .forEach( System.out::println );
	}
}

```

## Python Code
### python_code_1.txt
```python
from pathlib import Path

for path in Path('.').rglob('*.*'):
    print(path)

```

### python_code_2.txt
```python
import fnmatch
import os

rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))

```

### python_code_3.txt
```python
from fnmatch import fnmatch
import os, os.path

def print_fnmatches(pattern, dir, files):
    for filename in files:
        if fnmatch(filename, pattern):
            print os.path.join(dir, filename)

os.path.walk('/', print_fnmatches, '*.mp3')

```

### python_code_4.txt
```python
from path import path

rootPath = '/'
pattern = '*.mp3'

d = path(rootPath)
for f in d.walkfiles(pattern):
  print f

```

