# Take notes on the command line

## Task Link
[Rosetta Code - Take notes on the command line](https://rosettacode.org/wiki/Take_notes_on_the_command_line)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import java.nio.channels.*;
import java.util.Date;

public class TakeNotes {
    public static void main(String[] args) throws IOException {
        if (args.length > 0) {
            PrintStream ps = new PrintStream(new FileOutputStream("notes.txt", true));
            ps.println(new Date());
            ps.print("\t" + args[0]);
            for (int i = 1; i < args.length; i++)
                ps.print(" " + args[i]);
            ps.println();
            ps.close();
        } else {
            FileChannel fc = new FileInputStream("notes.txt").getChannel();
            fc.transferTo(0, fc.size(), Channels.newChannel(System.out));
            fc.close();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys, datetime, shutil

if len(sys.argv) == 1:
    try:
        with open("notes.txt", "r") as f:
            shutil.copyfileobj(f, sys.stdout)
    except IOError:
        pass
else:
    with open("notes.txt", "a") as f:
        f.write(datetime.datetime.now().isoformat() + "\n")
        f.write("\t%s\n" % ' '.join(sys.argv[1:]))

```

