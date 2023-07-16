# Copy stdin to stdout

## Task Link
[Rosetta Code - Copy stdin to stdout](https://rosettacode.org/wiki/Copy_stdin_to_stdout)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class CopyStdinToStdout {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in);) {
            String s;
            while ( (s = scanner.nextLine()).compareTo("") != 0 ) {
                System.out.println(s);
            }
        }
    }

}

```

## Python Code
