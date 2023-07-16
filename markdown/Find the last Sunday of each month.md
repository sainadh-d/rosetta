# Find the last Sunday of each month

## Task Link
[Rosetta Code - Find the last Sunday of each month](https://rosettacode.org/wiki/Find_the_last_Sunday_of_each_month)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class LastSunday 
{
	static final String[] months={"January","February","March","April","May","June","July","August","September","October","November","December"};
	
	public static int[] findLastSunday(int year)
	{
		boolean isLeap = isLeapYear(year);
		
		int[] days={31,isLeap?29:28,31,30,31,30,31,31,30,31,30,31};
		int[] lastDay=new int[12];
		
		for(int m=0;i<12;i++)
		{
			int d;
			for(d=days[m]; getWeekDay(year,m,d)!=0; d--)
				;
			lastDay[m]=d;
		}
		
		return lastDay;
	}
	
	private static boolean isLeapYear(int year)
	{
		if(year%4==0)
		{
			if(year%100!=0)
				return true;
			else if (year%400==0)
				return true;
		}
		return false;
	}
	
	private static int getWeekDay(int y, int m, int d)
	{
		int f=y+d+3*m-1;
		m++;
		
		if(m<3)
			y--;
		else
			f-=(int)(0.4*m+2.3);
		
		f+=(int)(y/4)-(int)((y/100+1)*0.75);
		f%=7;
		
		return f;
	}
	
	private static void display(int year, int[] lastDay)
	{
		System.out.println("\nYEAR: "+year);
		for(int m=0;i<12;i++)
			System.out.println(months[m]+": "+lastDay[m]);
	}
	
	public static void main(String[] args) throws Exception
	{
		System.out.print("Enter year: ");
		Scanner s=new Scanner(System.in);
		
		int y=Integer.parseInt(s.next());
		
		int[] lastDay = findLastSunday(y);
		display(y, lastDay);
		
		s.close();
	}
}

```

### java_code_2.txt
```java
import java.time.*;
import java.util.stream.*;
import static java.time.temporal.TemporalAdjusters.*;

public class FindTheLastSundayOfEachMonth {
    public static Stream<LocalDate> lastSundaysOf(int year) {
        return IntStream.rangeClosed(1, 12).mapToObj(month ->
            LocalDate.of(year, month, 1).with(lastDayOfMonth())
            .with(previousOrSame(DayOfWeek.SUNDAY))
        );
    }

    public static java.util.List<LocalDate> listLastSundaysOf(int year) {
        return lastSundaysOf(year).collect(Collectors.toList());
    }

    public static void main(String[] args) throws Exception {
        int year = args.length > 0 ? Integer.parseInt(args[0]) : LocalDate.now().getYear();

        for (LocalDate d : listLastSundaysOf(year)) {
            System.out.println(d);
        };

        String result = lastSundaysOf(2013).map(LocalDate::toString).collect(Collectors.joining("\n"));
        String test = "2013-01-27\n2013-02-24\n2013-03-31\n2013-04-28\n2013-05-26\n2013-06-30\n2013-07-28\n2013-08-25\n2013-09-29\n2013-10-27\n2013-11-24\n2013-12-29";
        if (!test.equals(result)) throw new AssertionError("test failure");
    }

}

```

## Python Code
### python_code_1.txt
```python
import sys
import calendar

year = 2013
if len(sys.argv) > 1:
    try:
        year = int(sys.argv[-1])
    except ValueError:
        pass

for month in range(1, 13):
    last_sunday = max(week[-1] for week in calendar.monthcalendar(year, month))
    print('{}-{}-{:2}'.format(year, calendar.month_abbr[month], last_sunday))

```

