# Secure temporary file

## Task Link
[Rosetta Code - Secure temporary file](https://rosettacode.org/wiki/Secure_temporary_file)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.io.IOException;

public class CreateTempFile {
    public static void main(String[] args)  {
        try {
            //create a temp file
            File temp = File.createTempFile("temp-file-name", ".tmp");
            System.out.println("Temp file : " + temp.getAbsolutePath());
        }
        catch(IOException e) {
            e.printStackTrace();
    	}
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import tempfile
>>> invisible = tempfile.TemporaryFile()
>>> invisible.name
'<fdopen>'
>>> visible = tempfile.NamedTemporaryFile()
>>> visible.name
'/tmp/tmpZNfc_s'
>>> visible.close()
>>> invisible.close()

```

### python_code_2.txt
```python
fd, path = tempfile.mkstemp()
try:
    # use the path or the file descriptor
finally:
    os.close(fd)

```

