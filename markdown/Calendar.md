# Calendar

## Task Link
[Rosetta Code - Calendar](https://rosettacode.org/wiki/Calendar)

## Java Code
### java_code_1.txt
```java
import java.text.*;
import java.util.*;

public class CalendarTask {

    public static void main(String[] args) {
        printCalendar(1969, 3);
    }

    static void printCalendar(int year, int nCols) {
        if (nCols < 1 || nCols > 12)
            throw new IllegalArgumentException("Illegal column width.");

        Calendar date = new GregorianCalendar(year, 0, 1);

        int nRows = (int) Math.ceil(12.0 / nCols);
        int offs = date.get(Calendar.DAY_OF_WEEK) - 1;
        int w = nCols * 24;

        String[] monthNames = new DateFormatSymbols(Locale.US).getMonths();

        String[][] mons = new String[12][8];
        for (int m = 0; m < 12; m++) {

            String name = monthNames[m];
            int len = 11 + name.length() / 2;
            String format = MessageFormat.format("%{0}s%{1}s", len, 21 - len);

            mons[m][0] = String.format(format, name, "");
            mons[m][1] = " Su Mo Tu We Th Fr Sa";
            int dim = date.getActualMaximum(Calendar.DAY_OF_MONTH);

            for (int d = 1; d < 43; d++) {
                boolean isDay = d > offs && d <= offs + dim;
                String entry = isDay ? String.format(" %2s", d - offs) : "   ";
                if (d % 7 == 1)
                    mons[m][2 + (d - 1) / 7] = entry;
                else
                    mons[m][2 + (d - 1) / 7] += entry;
            }
            offs = (offs + dim) % 7;
            date.add(Calendar.MONTH, 1);
        }

        System.out.printf("%" + (w / 2 + 10) + "s%n", "[Snoopy Picture]");
        System.out.printf("%" + (w / 2 + 4) + "s%n%n", year);

        for (int r = 0; r < nRows; r++) {
            for (int i = 0; i < 8; i++) {
                for (int c = r * nCols; c < (r + 1) * nCols && c < 12; c++)
                    System.out.printf("   %s", mons[c][i]);
                System.out.println();
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import calendar
>>> help(calendar.prcal)
Help on method pryear in module calendar:

pryear(self, theyear, w=0, l=0, c=6, m=3) method of calendar.TextCalendar instance
    Print a years calendar.

>>> calendar.prcal(1969)
                                  1969

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
                                                    31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                1  2  3  4                         1
 7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
28 29 30 31               25 26 27 28 29 30 31      29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
27 28 29 30 31            24 25 26 27 28 29 30      29 30 31

```

