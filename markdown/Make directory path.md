# Make directory path

## Task Link
[Rosetta Code - Make directory path](https://rosettacode.org/wiki/Make_directory_path)

## Java Code
### java_code_1.txt
```java
import java.io.File;

public interface Test {

    public static void main(String[] args) {
        try {
            File f = new File("C:/parent/test");
            if (f.mkdirs())
                System.out.println("path successfully created");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from errno import EEXIST
from os import mkdir, curdir
from os.path import split, exists

def mkdirp(path, mode=0777):
    head, tail = split(path)
    if not tail:
        head, tail = split(head)
    if head and tail and not exists(head):
        try:
            mkdirp(head, mode)
        except OSError as e:
            # be happy if someone already created the path
            if e.errno != EEXIST:
                raise
        if tail == curdir:  # xxx/newdir/. exists if xxx/newdir exists
            return
    try:
        mkdir(path, mode)
    except OSError as e:
        # be happy if someone already created the path
        if e.errno != EEXIST:
            raise

```

### python_code_2.txt
```python
def mkdirp(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

```

### python_code_3.txt
```python
def mkdirp(path):
    os.makedirs(path, exist_ok=True)

```

