# Sleep

## Task Link
[Rosetta Code - Sleep](https://rosettacode.org/wiki/Sleep)

## Java Code
### java_code_1.txt
```java
import java.util.InputMismatchException;
import java.util.Scanner;

public class Sleep {
    public static void main(final String[] args) throws InterruptedException {
        try {
            int ms = new Scanner(System.in).nextInt(); //Java's sleep method accepts milliseconds
            System.out.println("Sleeping...");
            Thread.sleep(ms);
            System.out.println("Awake!");
        } catch (InputMismatchException inputMismatchException) {
            System.err.println("Exception: " + inputMismatchException);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import time

seconds = float(raw_input())
print "Sleeping..."
time.sleep(seconds) # number is in seconds ... but accepts fractions
print "Awake!"

```

