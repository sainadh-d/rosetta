# Unix/ls

## Task Link
[Rosetta Code - Unix/ls](https://rosettacode.org/wiki/Unix/ls)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.List;

public class Ls {
    public static void main(String[] args) throws Exception {
        Ls ls = new Ls("/");
        System.out.println(ls);
    }

    private final File directory;
    private final List<File> list;

    public Ls(String path) throws Exception {
        directory = new File(path);
        if (!directory.exists())
            throw new Exception("Path not found '%s'".formatted(directory));
        if (!directory.isDirectory())
            throw new Exception("Not a directory '%s'".formatted(directory));
        list = new ArrayList<>(List.of(directory.listFiles()));
        /* place the directories first */
        list.sort((fileA, fileB) -> {
            if (fileA.isDirectory() && fileB.isFile()) {
                return -1;
            } else if (fileA.isFile() && fileB.isDirectory()) {
                return 1;
            }
            return 0;
        });
    }

    private String size(long bytes) {
        if (bytes > 1E9) {
            return "%.1fG".formatted(bytes / 1E9d);
        } else if (bytes > 1E6) {
            return "%.1fM".formatted(bytes / 1E6d);
        } else if (bytes > 1E3) {
            return "%.1fK".formatted(bytes / 1E3d);
        } else {
            return "%d".formatted(bytes);
        }
    }

    @Override
    public String toString() {
        StringBuilder string = new StringBuilder();
        Formatter formatter = new Formatter(string);
        /* add parent and current directory listings */
        list.add(0, directory.getParentFile());
        list.add(0, directory);
        /* generate total used space value */
        long total = 0;
        for (File file : list) {
            if (file == null) continue;
            total += file.length();
        }
        formatter.format("total %s%n", size(total));
        /* generate output for each entry */
        int index = 0;
        for (File file : list) {
            if (file == null) continue;
            /* generate permission columns */
            formatter.format(file.isDirectory() ? "d" : "-");
            formatter.format(file.canRead() ? "r" : "-");
            formatter.format(file.canWrite() ? "w" : "-");
            formatter.format(file.canExecute() ? "x" : "-");
            /* include size */
            formatter.format("%7s ", size(file.length()));
            /* modification timestamp */
            formatter.format("%tb %1$td %1$tR ", file.lastModified());
            /* file or directory name */
            switch (index) {
                case 0 -> formatter.format(".");
                case 1 -> formatter.format("..");
                default -> formatter.format("%s", file.getName());
            }
            if (file.isDirectory())
                formatter.format(File.separator);
            formatter.format("%n");
            index++;
        }
        formatter.flush();
        return string.toString();
    }
}

```

### java_code_2.txt
```java
package rosetta;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class UnixLS {

	public static void main(String[] args) throws IOException {
		Files.list(Path.of("")).sorted().forEach(System.out::println);
	}
}

```

### java_code_3.txt
```java
Files.list(Path.of("")).map(Path::toString).sorted(String.CASE_INSENSITIVE_ORDER).forEach(System.out::println);

```

## Python Code
### python_code_1.txt
```python
>>> import os
>>> print('\n'.join(sorted(os.listdir('.'))))
DLLs
Doc
LICENSE.txt
Lib
NEWS.txt
README.txt
Scripts
Tools
include
libs
python.exe
pythonw.exe
tcl
>>>

```

