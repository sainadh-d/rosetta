# Terminal control/Preserve screen

## Task Link
[Rosetta Code - Terminal control/Preserve screen](https://rosettacode.org/wiki/Terminal_control/Preserve_screen)

## Java Code
### java_code_1.txt
```java
public class PreserveScreen
{
    public static void main(String[] args) throws InterruptedException {
        System.out.print("\033[?1049h\033[H");
        System.out.println("Alternate screen buffer\n");
        for (int i = 5; i > 0; i--) {
            String s = (i > 1) ? "s" : "";
            System.out.printf("\rgoing back in %d second%s...", i, s);
            Thread.sleep(1000);
        }
        System.out.print("\033[?1049l");
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python

import time

print "\033[?1049h\033[H"
print "Alternate buffer!"

for i in xrange(5, 0, -1):
    print "Going back in:", i
    time.sleep(1)

print "\033[?1049l"

```

