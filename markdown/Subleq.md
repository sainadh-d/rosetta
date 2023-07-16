# Subleq

## Task Link
[Rosetta Code - Subleq](https://rosettacode.org/wiki/Subleq)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class Subleq {

    public static void main(String[] args) {
        int[] mem = {15, 17, -1, 17, -1, -1, 16, 1, -1, 16, 3, -1, 15, 15, 0, 0,
            -1, 72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33, 10, 0};

        Scanner input = new Scanner(System.in);
        int instructionPointer = 0;

        do {
            int a = mem[instructionPointer];
            int b = mem[instructionPointer + 1];

            if (a == -1) {
                mem[b] = input.nextInt();

            } else if (b == -1) {
                System.out.printf("%c", (char) mem[a]);

            } else {

                mem[b] -= mem[a];
                if (mem[b] < 1) {
                    instructionPointer = mem[instructionPointer + 2];
                    continue;
                }
            }

            instructionPointer += 3;

        } while (instructionPointer >= 0);
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys

def subleq(a):
    i = 0
    try:
        while i >= 0:
            if a[i] == -1:
                a[a[i + 1]] = ord(sys.stdin.read(1))
            elif a[i + 1] == -1:
                print(chr(a[a[i]]), end="")
            else:
                a[a[i + 1]] -= a[a[i]]
                if a[a[i + 1]] <= 0:
                    i = a[i + 2]
                    continue
            i += 3
    except (ValueError, IndexError, KeyboardInterrupt):
        print("abort")
        print(a)

subleq([15, 17, -1, 17, -1, -1, 16, 1, -1, 16, 3, -1, 15, 15,
        0, 0, -1, 72, 101, 108, 108, 111, 44, 32, 119, 111,
        114, 108, 100, 33, 10, 0])

```

