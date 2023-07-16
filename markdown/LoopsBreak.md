# Loops/Break

## Task Link
[Rosetta Code - Loops/Break](https://rosettacode.org/wiki/Loops/Break)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

Random rand = new Random();
while(true){
    int a = rand.nextInt(20);
    System.out.println(a);
    if(a == 10) break;
    int b = rand.nextInt(20);
    System.out.println(b);
}

```

## Python Code
### python_code_1.txt
```python
from random import randrange

while True:
    a = randrange(20)
    print(a)
    if a == 10:
        break
    b = randrange(20)
    print(b)

```

