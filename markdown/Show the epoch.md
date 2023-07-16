# Show the epoch

## Task Link
[Rosetta Code - Show the epoch](https://rosettacode.org/wiki/Show_the_epoch)

## Java Code
### java_code_1.txt
```java
import java.text.DateFormat;
import java.util.Date;
import java.util.TimeZone;

public class DateTest{
    public static void main(String[] args) {
        Date date = new Date(0);
        DateFormat format = DateFormat.getDateTimeInstance();
        format.setTimeZone(TimeZone.getTimeZone("UTC"));
        System.out.println(format.format(date));
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import time
>>> time.asctime(time.gmtime(0))
'Thu Jan  1 00:00:00 1970'
>>>

```

