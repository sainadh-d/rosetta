# Long year

## Task Link
[Rosetta Code - Long year](https://rosettacode.org/wiki/Long_year)

## Java Code
### java_code_1.txt
```java
import java.time.LocalDate;
import java.time.temporal.WeekFields;

public class LongYear {

    public static void main(String[] args) {
        System.out.printf("Long years this century:%n");
        for (int year = 2000 ; year < 2100 ; year++ ) {
            if ( longYear(year) ) {
                System.out.print(year + "  ");
            }
        }
    }
    
    private static boolean longYear(int year) {
        return LocalDate.of(year, 12, 28).get(WeekFields.ISO.weekOfYear()) == 53;
    }

}

```

## Python Code
### python_code_1.txt
```python
'''Long Year ?'''

from datetime import date


# longYear :: Year Int -> Bool
def longYear(y):
    '''True if the ISO year y has 53 weeks.'''
    return 52 < date(y, 12, 28).isocalendar()[1]


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Longer (53 week) years in the range 2000-2100'''
    for year in [
            x for x in range(2000, 1 + 2100)
            if longYear(x)
    ]:
        print(year)


# MAIN ---
if __name__ == '__main__':
    main()

```

