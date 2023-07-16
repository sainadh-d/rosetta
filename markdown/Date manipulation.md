# Date manipulation

## Task Link
[Rosetta Code - Date manipulation](https://rosettacode.org/wiki/Date_manipulation)

## Java Code
### java_code_1.txt
```java
import java.time.*;
import java.time.format.*;

class Main {  
  public static void main(String args[]) { 
    String dateStr = "March 7 2009 7:30pm EST";

    DateTimeFormatter df = new DateTimeFormatterBuilder()
				.parseCaseInsensitive()
				.appendPattern("MMMM d yyyy h:mma zzz")
				.toFormatter();
		
    ZonedDateTime after12Hours = ZonedDateTime.parse(dateStr, df).plusHours(12);
  
    System.out.println("Date: " + dateStr);
    System.out.println("+12h: " + after12Hours.format(df));

    ZonedDateTime after12HoursInCentralEuropeTime = after12Hours.withZoneSameInstant(ZoneId.of("CET"));
    System.out.println("+12h (in Central Europe): " + after12HoursInCentralEuropeTime.format(df));
  }
}

```

## Python Code
### python_code_1.txt
```python
import datetime

def mt():
	datime1="March 7 2009 7:30pm EST"
	formatting = "%B %d %Y %I:%M%p "
	datime2 = datime1[:-3]  # format can't handle "EST" for some reason
	tdelta = datetime.timedelta(hours=12)		# twelve hours..
	s3 = datetime.datetime.strptime(datime2, formatting)
	datime2 = s3+tdelta
	print datime2.strftime("%B %d %Y %I:%M%p %Z") + datime1[-3:]

mt()

```

