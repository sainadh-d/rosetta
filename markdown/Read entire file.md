# Read entire file

## Task Link
[Rosetta Code - Read entire file](https://rosettacode.org/wiki/Read_entire_file)

## Java Code
### java_code_1.txt
```java
static Byte[] contentsOf(File file) {
    return file.contents;
}

```

### java_code_2.txt
```java
Byte[] bytes = #./checkmark.ico;
String html  = $/docs/website/index.htm;

```

### java_code_3.txt
```java
File iconFile = ./checkmark.ico;
File htmlFile = /docs/website/index.htm;

Byte[] bytes = iconFile.contents;
String html  = htmlFile.contents.unpackUtf8();

```

### java_code_4.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {
    public static void main(String[] args) throws IOException{
        String fileContents = readEntireFile("./foo.txt");
    }

    private static String readEntireFile(String filename) throws IOException {
        FileReader in = new FileReader(filename);
        StringBuilder contents = new StringBuilder();
        char[] buffer = new char[4096];
        int read = 0;
        do {
            contents.append(buffer, 0, read);
            read = in.read(buffer);
        } while (read >= 0);
        in.close();
        return contents.toString();
    }
}

```

### java_code_5.txt
```java
import java.nio.channels.FileChannel.MapMode;
import java.nio.MappedByteBuffer;
import java.io.RandomAccessFile;
import java.io.IOException;
import java.io.File;

public class MMapReadFile {
	public static void main(String[] args) throws IOException {
		MappedByteBuffer buff = getBufferFor(new File(args[0]));
                String results = new String(buff.asCharBuffer());
	}
	
	public static MappedByteBuffer getBufferFor(File f) throws IOException {  
		RandomAccessFile file = new RandomAccessFile(f, "r");
	
		MappedByteBuffer buffer = file.getChannel().map(MapMode.READ_ONLY, 0, f.length());
		file.close();
		return buffer;
	}
}

```

### java_code_6.txt
```java
String content = new Scanner(new File("foo"), "UTF-8").useDelimiter("\\A").next();

```

### java_code_7.txt
```java
import java.util.List;
import java.nio.charset.Charset;
import java.nio.file.*;

public class ReadAll {
	public static List<String> readAllLines(String filesname){
		Path file = Paths.get(filename);
		return Files.readAllLines(file, Charset.defaultCharset());
	}
	
	public static byte[] readAllBytes(String filename){
		Path file = Paths.get(filename);
		return Files.readAllBytes(file);
	}
}

```

### java_code_8.txt
```java
package com.rosetta.example

import java.io.File
import java.io.PrintStream

class ReadFile {
    def static main( String ... args ) {
        val content = new String(Files.readAllBytes(Paths.get("file.txt")))
    }
}

```

## Python Code
### python_code_1.txt
```python
open(filename).read()

```

### python_code_2.txt
```python
open(filename, encoding='utf-8').read()

```

### python_code_3.txt
```python
with open(filename) as f:
    data = f.read()

```

### python_code_4.txt
```python
from pathlib import Path

any_string = Path(filename).read_text(encoding='utf-8')
any_binary_data = Path(filename).read_bytes()

```

