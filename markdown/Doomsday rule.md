# Doomsday rule

## Task Link
[Rosetta Code - Doomsday rule](https://rosettacode.org/wiki/Doomsday_rule)

## Java Code
### java_code_1.txt
```java
class Doom {
    public static void main(String[] args) {
        final Date[] dates = {
            new Date(1800,1,6),
            new Date(1875,3,29),
            new Date(1915,12,7),
            new Date(1970,12,23),
            new Date(2043,5,14),
            new Date(2077,2,12),
            new Date(2101,4,2)
        };
        
        for (Date d : dates)
            System.out.println(
                String.format("%s: %s", d.format(), d.weekday()));
    }
}

class Date {
    private int year, month, day;
    
    private static final int[] leapdoom = {4,1,7,4,2,6,4,1,5,3,7,5};
    private static final int[] normdoom = {3,7,7,4,2,6,4,1,5,3,7,5};
    public static final String[] weekdays = {
        "Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"
    };
    
    public Date(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }
    
    public boolean isLeapYear() {
        return year%4 == 0 && (year%100 != 0 || year%400 == 0);
    }
    
    public String format() {
        return String.format("%02d/%02d/%04d", month, day, year);
    }
    
    public String weekday() {
        final int c = year/100;
        final int r = year%100;
        final int s = r/12;
        final int t = r%12;
        
        final int c_anchor = (5 * (c%4) + 2) % 7;
        final int doom = (s + t + t/4 + c_anchor) % 7;
        final int anchor = 
            isLeapYear() ? leapdoom[month-1] : normdoom[month-1];
        
        return weekdays[(doom + day - anchor + 7) % 7];
    }
}

```

## Python Code
### python_code_1.txt
```python
from datetime import date
from calendar import isleap

def weekday(d):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"]
    dooms = [
        [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5],
        [4, 1, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    ]
    
    c = d.year // 100
    r = d.year % 100
    s = r // 12
    t = r % 12
    c_anchor = (5 * (c % 4) + 2) % 7
    doomsday = (s + t + (t // 4) + c_anchor) % 7
    anchorday = dooms[isleap(d.year)][d.month - 1]
    weekday = (doomsday + d.day - anchorday + 7) % 7
    return days[weekday]

dates = [date(*x) for x in
    [(1800, 1, 6), (1875, 3, 29), (1915, 12, 7), (1970, 12, 23),
     (2043, 5, 14), (2077, 2, 12), (2101, 4, 2)]
]

for d in dates:
    tense = "was" if d < date.today() else "is" if d == date.today() else "will be"
    print("{} {} a {}".format(d.strftime("%B %d, %Y"), tense, weekday(d)))

```

