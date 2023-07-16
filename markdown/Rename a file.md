# Rename a file

## Task Link
[Rosetta Code - Rename a file](https://rosettacode.org/wiki/Rename_a_file)

## Java Code
### java_code_1.txt
```java
import java.io.File;
public class FileRenameTest {
   public static boolean renameFile(String oldname, String newname) {
       // File (or directory) with old name
       File file = new File(oldname);
   
       // File (or directory) with new name
       File file2 = new File(newname);
   
       // Rename file (or directory)
       boolean success = file.renameTo(file2);
       return success;
   }
   public static void test(String type, String oldname, String newname) {
       System.out.println("The following " + type + " called " + oldname +
           ( renameFile(oldname, newname) ? " was renamed as " : " could not be renamed into ")
           + newname + "."
       );
   }
   public static void main(String args[]) {
        test("file", "input.txt", "output.txt");
        test("file", File.separator + "input.txt", File.separator + "output.txt");
        test("directory", "docs", "mydocs");
        test("directory", File.separator + "docs" + File.separator, File.separator + "mydocs" + File.separator);
   }
}

```

## Python Code
### python_code_1.txt
```python
from java.io import File

def setup():
    # rename local file
    sketchfile = rename(sketchPath("input.txt"), sketchPath("output.txt"))
    # rename local folder
    sketchfold = rename(sketchPath("docs"), sketchPath("mydocs"))
    # rename root file (if permitted)
    rootfile = rename("input.txt", "output.txt")
    # rename root folder (if permitted)
    rootfold = rename("docs", "mydocs")

    # display results of four operations: True=success, False=fail
    println(str(sketchfile) + ' ' +
            str(sketchfold) + ' ' +
            str(rootfile) +  ' ' +
            str(rootfold)) 
    # output:
    #     True True False False


def rename(oldname, newname):
    # File (or directory) with old name
    file = File(oldname)
    # File (or directory) with new name
    file2 = File(newname)
    # Rename file (or directory)
    success = file.renameTo(file2)
    return success

```

### python_code_2.txt
```python
import os

os.rename("input.txt", "output.txt")
os.rename("docs", "mydocs")

os.rename(os.sep + "input.txt", os.sep + "output.txt")
os.rename(os.sep + "docs", os.sep + "mydocs")

```

### python_code_3.txt
```python
import shutil

shutil.move("input.txt", "output.txt")
shutil.move("docs", "mydocs")

shutil.move("/input.txt", "/output.txt")
shutil.move("/docs", "/mydocs")

```

