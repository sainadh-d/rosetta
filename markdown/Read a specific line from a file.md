# Read a specific line from a file

## Task Link
[Rosetta Code - Read a specific line from a file](https://rosettacode.org/wiki/Read_a_specific_line_from_a_file)

## Java Code
### java_code_1.txt
```java
package linenbr7;

import java.io.*;

public class LineNbr7 {

    public static void main(String[] args) throws Exception {
        File f = new File(args[0]);
        if (!f.isFile() || !f.canRead())
            throw new IOException("can't read " + args[0]);

        BufferedReader br = new BufferedReader(new FileReader(f));
        try (LineNumberReader lnr = new LineNumberReader(br)) {
            String line = null;
            int lnum = 0;
            while ((line = lnr.readLine()) != null
                    && (lnum = lnr.getLineNumber()) < 7) {
            }

            switch (lnum) {
                case 0:
                    System.out.println("the file has zero length");
                    break;
                case 7:
                    boolean empty = "".equals(line);
                    System.out.println("line 7: " + (empty ? "empty" : line));
                    break;
                default:
                    System.out.println("the file has only " + lnum + " line(s)");
            }
        }
    }
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public final class ReadSpecificLineFromFile {

	public static void main(String[] aArgs) throws IOException {
		String fileName = "input.txt";
		Path filePath = Path.of(fileName);
		
		String seventhLine = Files.lines(filePath).skip(6).findFirst().orElse(ERROR_TOO_FEW_LINES);
		
		String messageToUser = seventhLine.isBlank() ? ERROR_EMPTY_LINE : seventhLine;
		System.out.println(messageToUser);		
	}	
	
	private static final String ERROR_TOO_FEW_LINES = "File has fewer than 7 lines";
	private static final String ERROR_EMPTY_LINE = "Line 7 is empty";

}

```

## Python Code
### python_code_1.txt
```python
with open('xxx.txt') as f:
    for i, line in enumerate(f):
        if i == 6:
            break
    else:
        print('Not 7 lines in file')
        line = None

```

### python_code_2.txt
```python
from itertools import islice

with open('xxx.txt') as f:
    try:
        line = next(islice(f, 6, 7))
    except StopIteration:
        print('Not 7 lines in file')

```

### python_code_3.txt
```python
print open('xxx.txt').readlines()[:7][-1]

```

