# The Twelve Days of Christmas

## Task Link
[Rosetta Code - The Twelve Days of Christmas](https://rosettacode.org/wiki/The_Twelve_Days_of_Christmas)

## Java Code
### java_code_1.txt
```java
public class TwelveDaysOfChristmas {

    final static String[] gifts = {
        "A partridge in a pear tree.", "Two turtle doves and",
        "Three french hens", "Four calling birds",
        "Five golden rings", "Six geese a-laying",
        "Seven swans a-swimming", "Eight maids a-milking",
        "Nine ladies dancing", "Ten lords a-leaping",
        "Eleven pipers piping", "Twelve drummers drumming",
        "And a partridge in a pear tree.", "Two turtle doves"
    };

    final static String[] days = {
        "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "eighth", "ninth", "tenth", "eleventh", "Twelfth"
    };

    public static void main(String[] args) {
        for (int i = 0; i < days.length; i++) {
            System.out.printf("%nOn the %s day of Christmas%n", days[i]);
            System.out.println("My true love gave to me:");
            for (int j = i; j >= 0; j--)
                System.out.println(gifts[i == 11 && j < 2 ? j + 12 : j]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
gifts = '''\
A partridge in a pear tree.
Two turtle doves
Three french hens
Four calling birds
Five golden rings
Six geese a-laying
Seven swans a-swimming
Eight maids a-milking
Nine ladies dancing
Ten lords a-leaping
Eleven pipers piping
Twelve drummers drumming'''.split('\n')

days = '''first second third fourth fifth
          sixth seventh eighth ninth tenth
          eleventh twelfth'''.split()

for n, day in enumerate(days, 1):
    g = gifts[:n][::-1]
    print(('\nOn the %s day of Christmas\nMy true love gave to me:\n' % day) +
          '\n'.join(g[:-1]) +
          (' and\n' + g[-1] if n > 1 else g[-1].capitalize()))

```

