# Spinning rod animation/Text

## Task Link
[Rosetta Code - Spinning rod animation/Text](https://rosettacode.org/wiki/Spinning_rod_animation/Text)

## Java Code
### java_code_1.txt
```java
public class SpinningRod
{
    public static void main(String[] args) throws InterruptedException {
        String a = "|/-\\";
        System.out.print("\033[2J");   // hide the cursor
        long start = System.currentTimeMillis();
        while (true) {
            for (int i = 0; i < 4; i++) {
                System.out.print("\033[2J");     // clear terminal
                System.out.print("\033[0;0H");   // place cursor at top left corner
                for (int j = 0; j < 80; j++) {   // 80 character terminal width, say
                    System.out.print(a.charAt(i));
                }
                Thread.sleep(250);
            }
            long now = System.currentTimeMillis();
            // stop after 20 seconds, say
            if (now - start >= 20000) break;
        }
        System.out.print("\033[?25h"); // restore the cursor
    }
}

```

## Python Code
### python_code_1.txt
```python
from time import sleep
while True:
    for rod in r'\|/-':
        print(rod, end='\r')
        sleep(0.25)

```

