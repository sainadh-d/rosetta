# Last Friday of each month

## Task Link
[Rosetta Code - Last Friday of each month](https://rosettacode.org/wiki/Last_Friday_of_each_month)

## Java Code
### java_code_1.txt
```java
import java.text.*;
import java.util.*;

public class LastFridays {

    public static void main(String[] args) throws Exception {
        int year = Integer.parseInt(args[0]);
        GregorianCalendar c = new GregorianCalendar(year, 0, 1);

        for (String mon : new DateFormatSymbols(Locale.US).getShortMonths()) {
            if (!mon.isEmpty()) {
                int totalDaysOfMonth = c.getActualMaximum(Calendar.DAY_OF_MONTH);
                c.set(Calendar.DAY_OF_MONTH, totalDaysOfMonth);

                int daysToRollBack = (c.get(Calendar.DAY_OF_WEEK) + 1) % 7;

                int day = totalDaysOfMonth - daysToRollBack;
                c.set(Calendar.DAY_OF_MONTH, day);

                System.out.printf("%d %s %d\n", year, mon, day);

                c.set(year, c.get(Calendar.MONTH) + 1, 1);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import calendar

def last_fridays(year):
    for month in range(1, 13):
        last_friday = max(week[calendar.FRIDAY]
            for week in calendar.monthcalendar(year, month))
        print('{:4d}-{:02d}-{:02d}'.format(year, month, last_friday))

```

### python_code_2.txt
```python
import calendar
c=calendar.Calendar()
fridays={}
year=raw_input("year")
for item in c.yeardatescalendar(int(year)):
    for i1 in item:
        for i2 in i1:
            for i3 in i2:
                if "Fri" in i3.ctime() and year in i3.ctime():
                    month,day=str(i3).rsplit("-",1)
                    fridays[month]=day

for item in sorted((month+"-"+day for month,day in fridays.items()),
                   key=lambda x:int(x.split("-")[1])):
    print item

```

### python_code_3.txt
```python
import calendar
c=calendar.Calendar()
fridays={}
year=raw_input("year")
add=list.__add__
for day in reduce(add,reduce(add,reduce(add,c.yeardatescalendar(int(year))))):

    if "Fri" in day.ctime() and year in day.ctime():
        month,day=str(day).rsplit("-",1)
        fridays[month]=day

for item in sorted((month+"-"+day for month,day in fridays.items()),
                   key=lambda x:int(x.split("-")[1])):
    print item

```

### python_code_4.txt
```python
import calendar
from itertools import chain
f=chain.from_iterable
c=calendar.Calendar()
fridays={}
year=raw_input("year")
add=list.__add__

for day in f(f(f(c.yeardatescalendar(int(year))))):

    if "Fri" in day.ctime() and year in day.ctime():
        month,day=str(day).rsplit("-",1)
        fridays[month]=day

for item in sorted((month+"-"+day for month,day in fridays.items()),
                   key=lambda x:int(x.split("-")[1])):
    print item

```

