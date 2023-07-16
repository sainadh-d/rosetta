# Check that file exists

## Task Link
[Rosetta Code - Check that file exists](https://rosettacode.org/wiki/Check_that_file_exists)

## Java Code
### java_code_1.txt
```java
new File("docs/input.txt").exists();
new File("/docs/input.txt").exists();

```

### java_code_2.txt
```java
new File("`Abdu'l-Bahá.txt").exists()

```

### java_code_3.txt
```java
new File("`Abdu'l-Bah\u00E1.txt").exists();

```

### java_code_4.txt
```java
import java.io.File;
public class FileExistsTest {
   public static boolean isFileExists(String filename) {
       boolean exists = new File(filename).exists();
       return exists;
   }
   public static void test(String type, String filename) {
       System.out.println("The following " + type + " called " + filename + 
           (isFileExists(filename) ? " exists." : " not exists.")
       );
   }
   public static void main(String args[]) {
        test("file", "input.txt");
        test("file", File.separator + "input.txt");
        test("directory", "docs");
        test("directory", File.separator + "docs" + File.separator);
   }
}

```

### java_code_5.txt
```java
import java.nio.file.FileSystem;
import java.nio.file.FileSystems;
import java.nio.file.Files;
public class FileExistsTest{
   private static FileSystem defaultFS = FileSystems.getDefault();
   public static boolean isFileExists(String filename){
       return Files.exists(defaultFS.getPath(filename));
   }
   public static void test(String type, String filename){
       System.out.println("The following " + type + " called " + filename + 
           (isFileExists(filename) ? " exists." : " not exists.")
       );
   }
   public static void main(String args[]){
        test("file", "input.txt");
        test("file", defaultFS.getSeparator() + "input.txt");
        test("directory", "docs");
        test("directory", defaultFS.getSeparator() + "docs" + defaultFS.getSeparator());
   }
}

```

## Python Code
### python_code_1.txt
```python
import os

os.path.isfile("input.txt")
os.path.isfile("/input.txt")
os.path.isdir("docs")
os.path.isdir("/docs")

```

