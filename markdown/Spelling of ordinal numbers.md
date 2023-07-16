# Spelling of ordinal numbers

## Task Link
[Rosetta Code - Spelling of ordinal numbers](https://rosettacode.org/wiki/Spelling_of_ordinal_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;

public class SpellingOfOrdinalNumbers {

    public static void main(String[] args) {
        for ( long test : new long[] {1,  2,  3,  4,  5,  11,  65,  100,  101,  272,  23456,  8007006005004003L} ) {
            System.out.printf("%d = %s%n", test, toOrdinal(test));
        }
    }

    private static Map<String,String> ordinalMap = new HashMap<>();
    static {
        ordinalMap.put("one", "first");
        ordinalMap.put("two", "second");
        ordinalMap.put("three", "third");
        ordinalMap.put("five", "fifth");
        ordinalMap.put("eight", "eighth");
        ordinalMap.put("nine", "ninth");
        ordinalMap.put("twelve", "twelfth");
    }
    
    private static String toOrdinal(long n) {
        String spelling = numToString(n);
        String[] split = spelling.split(" ");
        String last = split[split.length - 1];
        String replace = "";
        if ( last.contains("-") ) {
            String[] lastSplit = last.split("-");
            String lastWithDash = lastSplit[1];
            String lastReplace = "";
            if ( ordinalMap.containsKey(lastWithDash) ) {
                lastReplace = ordinalMap.get(lastWithDash);
            }
            else if ( lastWithDash.endsWith("y") ) {
                lastReplace = lastWithDash.substring(0, lastWithDash.length() - 1) + "ieth";
            }
            else {
                lastReplace = lastWithDash + "th";
            }
            replace = lastSplit[0] + "-" + lastReplace;
        }
        else {
            if ( ordinalMap.containsKey(last) ) {
                replace = ordinalMap.get(last);
            }
            else if ( last.endsWith("y") ) {
                replace = last.substring(0, last.length() - 1) + "ieth";
            }
            else {
                replace = last + "th";
            }
        }
        split[split.length - 1] = replace;
        return String.join(" ", split);
    }

    private static final String[] nums = new String[] {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    };
    
    private static final String[] tens = new String[] {"zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    private static final String numToString(long n) {
        return numToStringHelper(n);
    }
    
    private static final String numToStringHelper(long n) {
        if ( n < 0 ) {
            return "negative " + numToStringHelper(-n);
        }
        int index = (int) n;
        if ( n <= 19 ) {
            return nums[index];
        }
        if ( n <= 99 ) {
            return tens[index/10] + (n % 10 > 0 ? "-" + numToStringHelper(n % 10) : "");
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
        return numToStringHelper(n / factor) + " " + label + (n % factor > 0 ? " " + numToStringHelper(n % factor ) : "");
    }

}

```

## Python Code
### python_code_1.txt
```python
irregularOrdinals = {
	"one":    "first",
	"two":    "second",
	"three":  "third",
	"five":   "fifth",
	"eight":  "eighth",
	"nine":   "ninth",
	"twelve": "twelfth",
}

def num2ordinal(n):
    conversion = int(float(n))
    num = spell_integer(conversion)
    hyphen = num.rsplit("-", 1)
    num = num.rsplit(" ", 1)
    delim = " "
    if len(num[-1]) > len(hyphen[-1]):
        num = hyphen
        delim = "-"
    
    if num[-1] in irregularOrdinals:
        num[-1] = delim + irregularOrdinals[num[-1]]
    elif num[-1].endswith("y"):
        num[-1] = delim + num[-1][:-1] + "ieth"
    else:
        num[-1] = delim + num[-1] + "th"
    return "".join(num)
    
if __name__ == "__main__":
    tests = "1  2  3  4  5  11  65  100  101  272  23456  8007006005004003 123   00123.0   1.23e2".split()
    for num in tests:
        print("{} => {}".format(num, num2ordinal(num)))


#This is a copy of the code from https://rosettacode.org/wiki/Number_names#Python

TENS = [None, None, "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"]
SMALL = ["zero", "one", "two", "three", "four", "five",
         "six", "seven", "eight", "nine", "ten", "eleven",
         "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
HUGE = [None, None] + [h + "illion" 
                       for h in ("m", "b", "tr", "quadr", "quint", "sext", 
                                  "sept", "oct", "non", "dec")]
 
def nonzero(c, n, connect=''):
    return "" if n == 0 else connect + c + spell_integer(n)
 
def last_and(num):
    if ',' in num:
        pre, last = num.rsplit(',', 1)
        if ' and ' not in last:
            last = ' and' + last
        num = ''.join([pre, ',', last])
    return num
 
def big(e, n):
    if e == 0:
        return spell_integer(n)
    elif e == 1:
        return spell_integer(n) + " thousand"
    else:
        return spell_integer(n) + " " + HUGE[e]
 
def base1000_rev(n):
    # generates the value of the digits of n in base 1000
    # (i.e. 3-digit chunks), in reverse.
    while n != 0:
        n, r = divmod(n, 1000)
        yield r
 
def spell_integer(n):
    if n < 0:
        return "minus " + spell_integer(-n)
    elif n < 20:
        return SMALL[n]
    elif n < 100:
        a, b = divmod(n, 10)
        return TENS[a] + nonzero("-", b)
    elif n < 1000:
        a, b = divmod(n, 100)
        return SMALL[a] + " hundred" + nonzero(" ", b, ' and')
    else:
        num = ", ".join([big(e, x) for e, x in
                         enumerate(base1000_rev(n)) if x][::-1])
        return last_and(num)

```

