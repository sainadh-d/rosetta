# Four is magic

## Task Link
[Rosetta Code - Four is magic](https://rosettacode.org/wiki/Four_is_magic)

## Java Code
### java_code_1.txt
```java
public class FourIsMagic {

    public static void main(String[] args) {
        for ( long n : new long[] {6, 60, 89, 300, 670, 2000, 2467, 20000, 24500,200000, 230000, 246571, 2300000, 2465712, 20000000, 24657123, 230000000, 245000000, -246570000, 123456789712345l, 8777777777777777777L, Long.MAX_VALUE}) {
            String magic = fourIsMagic(n);
            System.out.printf("%d = %s%n", n, toSentence(magic));
        }
    }
    
    private static final String toSentence(String s) {
        return s.substring(0,1).toUpperCase() + s.substring(1) + ".";
    }
    
    private static final String[] nums = new String[] {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    };
    
    private static final String[] tens = new String[] {"zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    private static final String fourIsMagic(long n) {
        if ( n == 4 ) {
            return numToString(n) + " is magic";
        }
        String result = numToString(n);
        return result + " is " + numToString(result.length()) + ", " + fourIsMagic(result.length());
    }
    
    private static final String numToString(long n) {
        if ( n < 0 ) { 
            return "negative " + numToString(-n);
        }
        int index = (int) n;
        if ( n <= 19 ) {
            return nums[index];
        }
        if ( n <= 99 ) {
            return tens[index/10] + (n % 10 > 0 ? " " + numToString(n % 10) : "");
        }
        String label = null;
        long factor = 0;
        if ( n <= 999 ) {
            label = "hundred";
            factor = 100;
        }
        else if ( n <= 999999) {
            label = "thousand";
            factor = 1000;
        }
        else if ( n <= 999999999) {
            label = "million";
            factor = 1000000;
        }
        else if ( n <= 999999999999L) {
            label = "billion";
            factor = 1000000000;
        }
        else if ( n <= 999999999999999L) {
            label = "trillion";
            factor = 1000000000000L;
        }
        else if ( n <= 999999999999999999L) {
            label = "quadrillion";
            factor = 1000000000000000L;
        }
        else {
            label = "quintillion";
            factor = 1000000000000000000L;
        }
        return numToString(n / factor) + " " + label + (n % factor > 0 ? " " + numToString(n % factor ) : "");
    }

}

```

## Python Code
### python_code_1.txt
```python
import random
from collections import OrderedDict

numbers = {  # taken from https://en.wikipedia.org/wiki/Names_of_large_numbers#cite_ref-a_14-3
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    10 ** 6: 'million',
    10 ** 9: 'billion',
    10 ** 12: 'trillion',
    10 ** 15: 'quadrillion',
    10 ** 18: 'quintillion',
    10 ** 21: 'sextillion',
    10 ** 24: 'septillion',
    10 ** 27: 'octillion',
    10 ** 30: 'nonillion',
    10 ** 33: 'decillion',
    10 ** 36: 'undecillion',
    10 ** 39: 'duodecillion',
    10 ** 42: 'tredecillion',
    10 ** 45: 'quattuordecillion',
    10 ** 48: 'quinquadecillion',
    10 ** 51: 'sedecillion',
    10 ** 54: 'septendecillion',
    10 ** 57: 'octodecillion',
    10 ** 60: 'novendecillion',
    10 ** 63: 'vigintillion',
    10 ** 66: 'unvigintillion',
    10 ** 69: 'duovigintillion',
    10 ** 72: 'tresvigintillion',
    10 ** 75: 'quattuorvigintillion',
    10 ** 78: 'quinquavigintillion',
    10 ** 81: 'sesvigintillion',
    10 ** 84: 'septemvigintillion',
    10 ** 87: 'octovigintillion',
    10 ** 90: 'novemvigintillion',
    10 ** 93: 'trigintillion',
    10 ** 96: 'untrigintillion',
    10 ** 99: 'duotrigintillion',
    10 ** 102: 'trestrigintillion',
    10 ** 105: 'quattuortrigintillion',
    10 ** 108: 'quinquatrigintillion',
    10 ** 111: 'sestrigintillion',
    10 ** 114: 'septentrigintillion',
    10 ** 117: 'octotrigintillion',
    10 ** 120: 'noventrigintillion',
    10 ** 123: 'quadragintillion',
    10 ** 153: 'quinquagintillion',
    10 ** 183: 'sexagintillion',
    10 ** 213: 'septuagintillion',
    10 ** 243: 'octogintillion',
    10 ** 273: 'nonagintillion',
    10 ** 303: 'centillion',
    10 ** 306: 'uncentillion',
    10 ** 309: 'duocentillion',
    10 ** 312: 'trescentillion',
    10 ** 333: 'decicentillion',
    10 ** 336: 'undecicentillion',
    10 ** 363: 'viginticentillion',
    10 ** 366: 'unviginticentillion',
    10 ** 393: 'trigintacentillion',
    10 ** 423: 'quadragintacentillion',
    10 ** 453: 'quinquagintacentillion',
    10 ** 483: 'sexagintacentillion',
    10 ** 513: 'septuagintacentillion',
    10 ** 543: 'octogintacentillion',
    10 ** 573: 'nonagintacentillion',
    10 ** 603: 'ducentillion',
    10 ** 903: 'trecentillion',
    10 ** 1203: 'quadringentillion',
    10 ** 1503: 'quingentillion',
    10 ** 1803: 'sescentillion',
    10 ** 2103: 'septingentillion',
    10 ** 2403: 'octingentillion',
    10 ** 2703: 'nongentillion',
    10 ** 3003: 'millinillion'
}
numbers = OrderedDict(sorted(numbers.items(), key=lambda t: t[0], reverse=True))


def string_representation(i: int) -> str:
    """
    Return the english string representation of an integer
    """
    if i == 0:
        return 'zero'

    words = ['negative'] if i < 0 else []
    working_copy = abs(i)

    for key, value in numbers.items():
        if key <= working_copy:
            times = int(working_copy / key)

            if key >= 100:
                words.append(string_representation(times))

            words.append(value)
            working_copy -= times * key

        if working_copy == 0:
            break

    return ' '.join(words)


def next_phrase(i: int):
    """
    Generate all the phrases
    """
    while not i == 4:  # Generate phrases until four is reached
        str_i = string_representation(i)
        len_i = len(str_i)

        yield str_i, 'is', string_representation(len_i)

        i = len_i

    # the last phrase
    yield string_representation(i), 'is', 'magic'


def magic(i: int) -> str:
    phrases = []

    for phrase in next_phrase(i):
        phrases.append(' '.join(phrase))

    return f'{", ".join(phrases)}.'.capitalize()


if __name__ == '__main__':

    for j in (random.randint(0, 10 ** 3) for i in range(5)):
        print(j, ':\n', magic(j), '\n')

    for j in (random.randint(-10 ** 24, 10 ** 24) for i in range(2)):
        print(j, ':\n', magic(j), '\n')

```

