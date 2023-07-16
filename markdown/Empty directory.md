# Empty directory

## Task Link
[Rosetta Code - Empty directory](https://rosettacode.org/wiki/Empty_directory)

## Java Code
### java_code_1.txt
```java
import java.nio.file.Paths;
//... other class code here
public static boolean isEmptyDir(String dirName){
    return Paths.get(dirName).toFile().listFiles().length == 0;
}

```

## Python Code
### python_code_1.txt
```python
import os;
if os.listdir(raw_input("directory")):
    print "not empty"
else:
    print "empty"

```

