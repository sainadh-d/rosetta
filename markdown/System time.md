# System time

## Task Link
[Rosetta Code - System time](https://rosettacode.org/wiki/System_time)

## Java Code
### java_code_1.txt
```java
public class SystemTime{
    public static void main(String[] args){
        System.out.format("%tc%n", System.currentTimeMillis());
    }
}

```

### java_code_2.txt
```java
import java.util.Date;

public class SystemTime{
   public static void main(String[] args){
      Date now = new Date();
      System.out.println(now); // string representation

      System.out.println(now.getTime()); // Unix time (# of milliseconds since Jan 1 1970)
      //System.currentTimeMillis() returns the same value
   }
}

```

## Python Code
### python_code_1.txt
```python
import time
print time.ctime()

```

