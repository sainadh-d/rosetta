# Date format

## Task Link
[Rosetta Code - Date format](https://rosettacode.org/wiki/Date_format)

## Java Code
### java_code_1.txt
```java
Datetime dtNow = datetime.now();
String strDt1 = dtNow.format('yyyy-MM-dd');
String strDt2 = dtNow.format('EEEE, MMMM dd, yyyy');
system.debug(strDt1); // "2007-11-10"
system.debug(strDt2); //"Sunday, November 10, 2007"

```

### java_code_2.txt
```java
public static void main(String[] args) {
    long millis = System.currentTimeMillis();
    System.out.printf("%tF%n", millis);
    System.out.printf("%tA, %1$tB %1$td, %1$tY%n", millis);
}

```

### java_code_3.txt
```java
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.text.DateFormatSymbols;
import java.text.DateFormat;
public class Dates{
 public static void main(String[] args){
  Calendar now = new GregorianCalendar(); //months are 0 indexed, dates are 1 indexed
  DateFormatSymbols symbols = new DateFormatSymbols(); //names for our months and weekdays

  //plain numbers way
  System.out.println(now.get(Calendar.YEAR)  + "-" + (now.get(Calendar.MONTH) + 1) + "-" + now.get(Calendar.DATE));

  //words way
  System.out.print(symbols.getWeekdays()[now.get(Calendar.DAY_OF_WEEK)] + ", ");
  System.out.print(symbols.getMonths()[now.get(Calendar.MONTH)] + " ");
  System.out.println(now.get(Calendar.DATE) + ", " + now.get(Calendar.YEAR));
 }
}

```

### java_code_4.txt
```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
public class Dates
{
 public static void main(final String[] args)
 {
  //using DateTimeFormatter
  LocalDate date = LocalDate.now();
  DateTimeFormatter dtFormatter = DateTimeFormatter.ofPattern("yyyy MM dd");

  System.out.println(dtFormatter.format(date));
 }
}

```

### java_code_5.txt
```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateFormat {
    public static void main(String[]args){
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
        SimpleDateFormat formatLong = new SimpleDateFormat("EEEE, MMMM dd, yyyy");
        System.out.println(format.format(new Date()));
        System.out.println(formatLong.format(new Date()));
    }
}

```

## Python Code
### python_code_1.txt
```python
import datetime
today = datetime.date.today()
# The first requested format is a method of datetime objects:
today.isoformat()
# For full flexibility, use the strftime formatting codes from the link above:
today.strftime("%A, %B %d, %Y")
# This mechanism is integrated into the general string formatting system.
# You can do this with positional arguments referenced by number
"The date is {0:%A, %B %d, %Y}".format(d)
# Or keyword arguments referenced by name
"The date is {date:%A, %B %d, %Y}".format(date=d)
# Since Python 3.6, f-strings allow the value to be inserted inline
f"The date is {d:%A, %B %d, %Y}"

```

