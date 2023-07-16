# Integer sequence

## Task Link
[Rosetta Code - Integer sequence](https://rosettacode.org/wiki/Integer_sequence)

## Java Code
### java_code_1.txt
```java
public class Count{
    public static void main(String[] args){
        for(long i = 1; ;i++) System.out.println(i);
    }
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

public class Count{
    public static void main(String[] args){
        for(BigInteger i = BigInteger.ONE; ;i = i.add(BigInteger.ONE)) System.out.println(i);
    }
}

```

## Python Code
### python_code_1.txt
```python
i=1
while i:
    print(i)
    i += 1

```

### python_code_2.txt
```python
from itertools import count

for i in count(): 
    print(i)

```

