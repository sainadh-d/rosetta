# Loops/Nested

## Task Link
[Rosetta Code - Loops/Nested](https://rosettacode.org/wiki/Loops/Nested)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class NestedLoopTest {
    public static final Random gen = new Random();
    public static void main(String[] args) {
        int[][] a = new int[10][10];
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[i].length; j++)
                a[i][j] = gen.nextInt(20) + 1;

        Outer:for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(" " + a[i][j]);
                if (a[i][j] == 20)
                    break Outer; //adding a label breaks out of all loops up to and including the labelled loop
            }
            System.out.println();
        }
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
from random import randint

def do_scan(mat):
    for row in mat:
        for item in row:
            print item,
            if item == 20:
                print
                return
        print
    print

mat = [[randint(1, 20) for x in xrange(10)] for y in xrange(10)]
do_scan(mat)

```

### python_code_2.txt
```python
from random import randint

class Found20(Exception):
    pass

mat = [[randint(1, 20) for x in xrange(10)] for y in xrange(10)]

try:
    for row in mat:
        for item in row:
            print item,
            if item == 20:
                raise Found20
        print
except Found20:
    print

```

### python_code_3.txt
```python
from random import randint

mat = [[randint(1, 20) for x in xrange(10)] for y in xrange(10)]

found20 = False
for row in mat:
    for item in row:
        print item,
        if item == 20:
            found20 = True
            break
    print
    if found20:
        break

```

