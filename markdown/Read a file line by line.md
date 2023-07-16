# Read a file line by line

## Task Link
[Rosetta Code - Read a file line by line](https://rosettacode.org/wiki/Read_a_file_line_by_line)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;

/**
 * Reads a file line by line, processing each line.
 *
 * @author  $Author$
 * @version $Revision$
 */
public class ReadFileByLines {
    private static void processLine(int lineNo, String line) {
        // ...
    }

    public static void main(String[] args) {
        for (String filename : args) {
            BufferedReader br = null;
            FileReader fr = null;
            try {
                fr = new FileReader(filename);
                br = new BufferedReader(fr);
                String line;
                int lineNo = 0;
                while ((line = br.readLine()) != null) {
                    processLine(++lineNo, line);
                }
            }
            catch (Exception x) {
                x.printStackTrace();
            }
            finally {
                if (fr != null) {
                    try {br.close();} catch (Exception ignoreMe) {}
                    try {fr.close();} catch (Exception ignoreMe) {}
                }
            }
        }
    }
}

```

### java_code_2.txt
```java
for (String filename : args) {
    try (FileReader fr = new FileReader(filename);BufferedReader br = new BufferedReader(fr)){
        String line;
        int lineNo = 0;
        while ((line = br.readLine()) != null) {
            processLine(++lineNo, line);
        }
    }
    catch (Exception x) {
        x.printStackTrace();
    }
}

```

### java_code_3.txt
```java
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.charset.Charset;
import java.io.IOException;
//...other class code
List<String> lines = null;
try{
    lines = Files.readAllLines(Paths.get(filename), Charset.defaultCharset());
}catch(IOException | SecurityException e){
    //problem with the file
}

```

## Python Code
### python_code_1.txt
```python
for line in lines open('input.txt'):
    print line

```

### python_code_2.txt
```python
with open("foobar.txt") as f:
    for line in f:
        process(line)

```

### python_code_3.txt
```python
import fileinput
for line in fileinput.input():
    process(line)

```

