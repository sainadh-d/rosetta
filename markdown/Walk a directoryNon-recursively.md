# Walk a directory/Non-recursively

## Task Link
[Rosetta Code - Walk a directory/Non-recursively](https://rosettacode.org/wiki/Walk_a_directory/Non-recursively)

## Java Code
### java_code_1.txt
```java
File dir = new File("/foo/bar");

String[] contents = dir.list();
for (String file : contents)
    if (file.endsWith(".mp3"))
        System.out.println(file);

```

## Python Code
### python_code_1.txt
```python
import glob
for filename in glob.glob('/foo/bar/*.mp3'):
    print(filename)

```

### python_code_2.txt
```python
import os
for filename in os.listdir('/foo/bar'):
    if filename.endswith('.mp3'):
        print(filename)

```

