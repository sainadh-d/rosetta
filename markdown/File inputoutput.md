# File input/output

## Task Link
[Rosetta Code - File input/output](https://rosettacode.org/wiki/File_input/output)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class FileIODemo {
  public static void main(String[] args) {
    try {
      FileInputStream in = new FileInputStream("input.txt");
      FileOutputStream out = new FileOutputStream("ouput.txt");
      int c;
      while ((c = in.read()) != -1) {
        out.write(c);
      }
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (IOException e){
      e.printStackTrace();
    }
  }
}

```

### java_code_2.txt
```java
import java.io.*;

public class FileIODemo2 {
  public static void main(String args[]) {
    try {
      // Probably should wrap with a BufferedInputStream
      final InputStream in = new FileInputStream("input.txt");
      try {
        // Probably should wrap with a BufferedOutputStream
        final OutputStream out = new FileOutputStream("output.txt");
        try {
          int c;
          while ((c = in.read()) != -1) {
            out.write(c);
          }
        }
        finally {
          out.close();
        }
      }
      finally {
        in.close();
      }
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    } catch (IOException e){
      e.printStackTrace();
    }
  }
}

```

### java_code_3.txt
```java
import java.io.*;
import java.nio.channels.*;

public class FileIODemo3 {
  public static void main(String args[]) {
    try {
      final FileChannel in = new FileInputStream("input.txt").getChannel();
      try {
        final FileChannel out = new FileOutputStream("output.txt").getChannel();
        try {
          out.transferFrom(in, 0, in.size());
        }
        finally {
          out.close();
        }
      }
      finally {
        in.close();
      }
    }
    catch (Exception e) {
      System.err.println("Exception while trying to copy: "+e);
      e.printStackTrace(); // stack trace of place where it happened
    }
  }
}

```

### java_code_4.txt
```java
import java.io.*;
public class Test {
  public static void main (String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new FileReader("input.txt"));
    BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"));
    String line;
    while ((line = br.readLine()) != null) {
      bw.write(line);
      bw.newLine();
    }
    br.close();
    bw.close();
  }
}

```

### java_code_5.txt
```java
import java.nio.file.*;
public class Copy{
   public static void main(String[] args) throws Exception{
      FileSystem fs = FileSystems.getDefault();
      Path in = fs.getPath("input.txt");
      Path out = fs.getPath("output.txt");
      Files.copy(in, out, StandardCopyOption.REPLACE_EXISTING);
   }
}

```

## Python Code
### python_code_1.txt
```python
import shutil
shutil.copyfile('input.txt', 'output.txt')

```

### python_code_2.txt
```python
infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')
for line in infile:
   outfile.write(line)
outfile.close()
infile.close()

```

### python_code_3.txt
```python
import sys
try:
    infile = open('input.txt', 'r')
except IOError:
    print >> sys.stderr, "Unable to open input.txt for input"
    sys.exit(1)
try:
    outfile = open('output.txt', 'w')
except IOError:
    print >> sys.stderr, "Unable to open output.txt for output"
    sys.exit(1)
try:  # for finally
    try: # for I/O
        for line in infile:
            outfile.write(line)
    except IOError, e:
        print >> sys.stderr, "Some I/O Error occurred (reading from input.txt or writing to output.txt)"
finally:
    infile.close()
    outfile.close()

```

### python_code_4.txt
```python
import sys
try:
    with open('input.txt') as infile:
        with open('output.txt', 'w') as outfile:
            for line in infile:
                outfile.write(line)
except IOError:
    print >> sys.stderr, "Some I/O Error occurred"
    sys.exit(1)

```

