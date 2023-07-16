# Day of the week

## Task Link
[Rosetta Code - Day of the week](https://rosettacode.org/wiki/Day_of_the_week)

## Java Code
### java_code_1.txt
```java
import static java.util.Calendar.*;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class Yuletide{
	public static void main(String[] args) {
		Calendar calendar;
        int count = 1;
        for (int year = 2008; year <= 2121; year++) {
            calendar = new GregorianCalendar(year, DECEMBER, 25);
            if (calendar.get(DAY_OF_WEEK) == SUNDAY) {
                if (count != 1)
                    System.out.print(", ");
                System.out.printf("%d", calendar.get(YEAR));
                count++;
            }
        }
	}
}

```

## Python Code
### python_code_1.txt
```python
from calendar import weekday, SUNDAY

[year for year in range(2008, 2122) if weekday(year, 12, 25) == SUNDAY]

```

### python_code_2.txt
```python
'''Days of the week'''

from datetime import date
from itertools import islice


# xmasIsSunday :: Int -> Bool
def xmasIsSunday(y):
    '''True if Dec 25 in the given year is a Sunday.'''
    return 6 == date(y, 12, 25).weekday()


# main :: IO ()
def main():
    '''Years between 2008 and 2121 with 25 Dec on a Sunday'''

    xs = list(filter(
        xmasIsSunday,
        enumFromTo(2008)(2121)
    ))
    total = len(xs)
    print(
        fTable(main.__doc__ + ':\n\n' + '(Total ' + str(total) + ')\n')(
            lambda i: str(1 + i)
        )(str)(index(xs))(
            enumFromTo(0)(total - 1)
        )
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )



#  FORMATTING ---------------------------------------------
# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN --
if __name__ == '__main__':
    main()

```

