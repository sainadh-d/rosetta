# Leap year

## Task Link
[Rosetta Code - Leap year](https://rosettacode.org/wiki/Leap_year)

## Java Code
### java_code_1.txt
```java
import java.util.GregorianCalendar;
import java.text.MessageFormat;

public class Leapyear{
        public static void main(String[] argv){
                int[] yrs = {1800,1900,1994,1998,1999,2000,2001,2004,2100};
                GregorianCalendar cal = new GregorianCalendar();
                for(int year : yrs){
                        System.err.println(MessageFormat.format("The year {0,number,#} is leaper: {1} / {2}.",
                                                                 year, cal.isLeapYear(year), isLeapYear(year)));
                }

        }
        public static boolean isLeapYear(int year){
                return (year % 100 == 0) ? (year % 400 == 0) : (year % 4 == 0);
        }
}

```

### java_code_2.txt
```java
import java.time.Year;

public class IsLeap {

    public static void main(String[] args) {
        System.out.println(Year.isLeap(2004));
    }
}

```

## Python Code
### python_code_1.txt
```python
import calendar
calendar.isleap(year)

```

### python_code_2.txt
```python
def is_leap_year(year):
    return not year % (4 if year % 100 else 400)

```

### python_code_3.txt
```python
import datetime

def is_leap_year(year):
    try:
        datetime.date(year, 2, 29)
    except ValueError:
        return False
    return True

```

