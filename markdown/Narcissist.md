# Narcissist

## Task Link
[Rosetta Code - Narcissist](https://rosettacode.org/wiki/Narcissist)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Narcissist {
    private static final String SOURCE = "import java.io.BufferedReader;%nimport java.io.IOException;%nimport java.io.InputStreamReader;%n%npublic class Narcissist {%n    private static final String SOURCE = %c%s%c;%n    private static final char QUOTE = 0x22;%n%n    public static void main(String[] args) throws IOException {%n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));%n        StringBuilder sb = new StringBuilder();%n%n        while (true) {%n            String line = br.readLine();%n            if (null == line) break;%n            sb.append(line).append(System.lineSeparator());%n        }%n%n        String program = String.format(SOURCE, QUOTE, SOURCE, QUOTE, QUOTE, QUOTE, QUOTE, QUOTE);%n        if (program.equals(sb.toString())) {%n            System.out.println(%caccept%c);%n        } else {%n            System.out.println(%creject%c);%n        }%n    }%n}%n";
    private static final char QUOTE = 0x22;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            String line = br.readLine();
            if (null == line) break;
            sb.append(line).append(System.lineSeparator());
        }

        String program = String.format(SOURCE, QUOTE, SOURCE, QUOTE, QUOTE, QUOTE, QUOTE, QUOTE);
        if (program.equals(sb.toString())) {
            System.out.println("accept");
        } else {
            System.out.println("reject");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys
with open(sys.argv[0]) as quine:
    code = raw_input("Enter source code: ")
    if code == quine.read():
        print("Accept")
    else:
        print("Reject")

```

### python_code_2.txt
```python
_='_=%r;print (_%%_==input())';print (_%_==input())

```

