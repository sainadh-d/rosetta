# Five weekends

## Task Link
[Rosetta Code - Five weekends](https://rosettacode.org/wiki/Five_weekends)

## Java Code
### java_code_1.txt
```java
import java.util.Calendar;
import java.util.GregorianCalendar;

public class FiveFSS {
    private static boolean[] years = new boolean[201];
    private static int[] month31 = {Calendar.JANUARY, Calendar.MARCH, Calendar.MAY,
        Calendar.JULY, Calendar.AUGUST, Calendar.OCTOBER, Calendar.DECEMBER};

    public static void main(String[] args) {
        StringBuilder months = new StringBuilder();
        int numMonths = 0;
        for (int year = 1900; year <= 2100; year++) {
            for (int month : month31) {
                Calendar date = new GregorianCalendar(year, month, 1);
                if (date.get(Calendar.DAY_OF_WEEK) == Calendar.FRIDAY) {
                    years[year - 1900] = true;
                    numMonths++;
                    //months are 0-indexed in Calendar
                    months.append((date.get(Calendar.MONTH) + 1) + "-" + year +"\n");
                }
            }
        }
        System.out.println("There are "+numMonths+" months with five weekends from 1900 through 2100:");
        System.out.println(months);
        System.out.println("Years with no five-weekend months:");
        for (int year = 1900; year <= 2100; year++) {
            if(!years[year - 1900]){
                System.out.println(year);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from datetime import (date,
                      timedelta)

DAY = timedelta(days=1)
START, STOP = date(1900, 1, 1), date(2101, 1, 1)
WEEKEND = {6, 5, 4}  # Sunday is day 6
FMT = '%Y %m(%B)'


def five_weekends_per_month(start: date = START,
                            stop: date = STOP) -> list[date]:
    """Compute months with five weekends between dates"""
    current_date = start
    last_month = weekend_days = 0
    five_weekends = []
    while current_date < stop:
        if current_date.month != last_month:
            if weekend_days >= 15:
                five_weekends.append(current_date - DAY)
            weekend_days = 0
            last_month = current_date.month
        if current_date.weekday() in WEEKEND:
            weekend_days += 1
        current_date += DAY
    return five_weekends


dates = five_weekends_per_month()
indent = '  '
print(f"There are {len(dates)} months of which the first and last five are:")
print(indent + ('\n' + indent).join(d.strftime(FMT) for d in dates[:5]))
print(indent + '...')
print(indent + ('\n' + indent).join(d.strftime(FMT) for d in dates[-5:]))

years_without_five_weekends_months = (STOP.year - START.year
                                      - len({d.year for d in dates}))
print(f"\nThere are {years_without_five_weekends_months} years in the "
      f"range that do not have months with five weekends")

```

### python_code_2.txt
```python
LONGMONTHS = (1, 3, 5, 7, 8, 10, 12)  # Jan Mar May Jul Aug Oct Dec


def five_weekends_per_month2(start: date = START,
                             stop: date = STOP) -> list[date]:
    return [last_day
            for year in range(start.year, stop.year)
            for month in LONG_MONTHS
            if (last_day := date(year, month, 31)).weekday() == 6]  # Sunday

dates2 = five_weekends_per_month2()
assert dates2 == dates

```

