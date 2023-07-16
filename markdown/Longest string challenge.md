# Longest string challenge

## Task Link
[Rosetta Code - Longest string challenge](https://rosettacode.org/wiki/Longest_string_challenge)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.util.Scanner;

public class LongestStringChallenge {

    public static void main(String[] args) throws Exception {
        String lines = "", longest = "";
        try (Scanner sc = new Scanner(new File("lines.txt"))) {
            while(sc.hasNext()) {
                String line = sc.nextLine();
                if (longer(longest, line))
                    lines = longest = line;
                else if (!longer(line, longest))
                    lines = lines.concat("\n").concat(line);
            }
        }
        System.out.println(lines);
    }

    static boolean longer(String a, String b) {
        try {
            String dummy = a.substring(b.length());
        } catch (StringIndexOutOfBoundsException e) {
            return true;
        }
        return false;
    }
}

```

## Python Code
### python_code_1.txt
```python
import fileinput

# This returns True if the second string has a value on the 
# same index as the last index of the first string. It runs
# faster than trimming the strings because it runs len once
# and is a single index lookup versus slicing both strings 
# one character at a time.
def longer(a, b):
    try:
        b[len(a)-1]
        return False
    except:
        return True

longest, lines = '', ''
for x in fileinput.input():
    if longer(x, longest):
        lines, longest = x, x
    elif not longer(longest, x):
        lines += x

print(lines, end='')

```

