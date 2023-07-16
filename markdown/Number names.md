# Number names

## Task Link
[Rosetta Code - Number names](https://rosettacode.org/wiki/Number_names)

## Java Code
### java_code_2.txt
```java
public enum IntToWords {
    ;

    private static final String[] small = {
            "", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    private static final String[] tens = {
            "", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"};
    private static final String[] big = {
            "", "thousand", "million", "billion", "trillion",
            "quadrillion", "quintillion"};

    public static void main(String[] args) {
        System.out.println(int2Text(0));
        System.out.println(int2Text(10));
        System.out.println(int2Text(30));
        System.out.println(int2Text(47));
        System.out.println(int2Text(100));
        System.out.println(int2Text(999));
        System.out.println(int2Text(1000));
        System.out.println(int2Text(9999));
        System.out.println(int2Text(123_456));
        System.out.println(int2Text(900_000_001));
        System.out.println(int2Text(1_234_567_890));
        System.out.println(int2Text(-987_654_321));
        System.out.println(int2Text(Long.MAX_VALUE));
        System.out.println(int2Text(Long.MIN_VALUE));
    }

    public static String int2Text(long number) {
        StringBuilder sb = new StringBuilder();

        if (number == 0) {
            return "zero";
        }

        long num = -Math.abs(number);

        int unit = 1;
        while (true) {
            int rem100 = (int) -(num % 100);
            if (rem100 >= 20) {
                if (rem100 % 10 == 0) {
                    sb.insert(0, tens[rem100 / 10] + " ");
                } else {
                    sb.insert(0, tens[rem100 / 10] + "-" + small[rem100 % 10] + " ");
                }
            } else if (rem100 != 0) {
                sb.insert(0, small[rem100] + " ");
            }

            int hundreds = (int) -(num % 1000) / 100;
            if (hundreds != 0) {
                sb.insert(0, small[hundreds] + " hundred ");
            }

            num /= 1000;
            if (num == 0) {
                break;
            }

            int rem1000 = (int) -(num % 1000);
            if (rem1000 != 0) {
                sb.insert(0, big[unit] + " ");
            }
            unit++;
        }

        if (number < 0) {
            sb.insert(0, "negative ");
        }

        return sb.toString().trim();
    }
}

```

### java_code_3.txt
```java
public class NumberToWordsConverter { // works upto 9999999

	final private  static String[] units = {"Zero","One","Two","Three","Four",
		"Five","Six","Seven","Eight","Nine","Ten",
		"Eleven","Twelve","Thirteen","Fourteen","Fifteen",
		"Sixteen","Seventeen","Eighteen","Nineteen"};
	final private static String[] tens = {"","","Twenty","Thirty","Forty","Fifty",
		"Sixty","Seventy","Eighty","Ninety"};

	public static String convert(Integer i) {
		//
		if( i < 20)  return units[i];
		if( i < 100) return tens[i/10] + ((i % 10 > 0)? " " + convert(i % 10):"");
		if( i < 1000) return units[i/100] + " Hundred" + ((i % 100 > 0)?" and " + convert(i % 100):"");
		if( i < 1000000) return convert(i / 1000) + " Thousand " + ((i % 1000 > 0)? " " + convert(i % 1000):"") ;
		return convert(i / 1000000) + " Million " + ((i % 1000000 > 0)? " " + convert(i % 1000000):"") ;
	}
}

```

## Python Code
### python_code_1.txt
```python
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

if __name__ == '__main__':
    # examples
    for n in (0, -3, 5, -7, 11, -13, 17, -19, 23, -29):
        print('%+4i -> %s' % (n, spell_integer(n)))
    print('')  
    
    n = 201021002001
    while n:
        print('%-12i -> %s' % (n, spell_integer(n)))
        n //= -10
    print('%-12i -> %s' % (n, spell_integer(n)))
    print('')

```

### python_code_2.txt
```python
def int_to_english(n):
    if n < 0: return "minus " + int_to_english(-n)
    if n < 10:
        return ["zero", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine"][n]
    if n < 20:
        return ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"][n-10]
    if n < 100:
        tens = ["twenty", "thirty", "forty", "fifty", "sixty",
                "seventy", "eighty", "ninety"][(n // 10 - 2)%10]
        if n % 10 != 0:
            return tens + "-" + int_to_english(n % 10)
        else:
            return tens
    if n < 1000:
        if n % 100 == 0:
            return int_to_english(n // 100) + " hundred"
        else:
            return int_to_english(n // 100) + " hundred and " +\
               int_to_english(n % 100)
    # http://www.isthe.com/chongo/tech/math/number/tenpower.html
    powers = [("thousand", 3), ("million", 6),
              ("billion", 9), ("trillion", 12), ("quadrillion", 15),
              ("quintillion", 18), ("sextillion", 21), ("septillion", 24),
              ("octillion", 27), ("nonillion", 30), ("decillion", 33),
              ("undecillion", 36), ("duodecillion", 39), ("tredecillion", 42),
              ("quattuordecillion", 45), ("quindecillion", 48),
              ("sexdecillion", 51), ("eptendecillion", 54),
              ("octadecillion", 57), ("novemdecillion", 61),
              ("vigintillion", 64)]
    ns = str(n)
    idx = len(powers) - 1
    while True:
        d = powers[idx][1]
        if len(ns) > d:
            first = int_to_english(int(ns[:-d]))
            second = int_to_english(int(ns[-d:]))
            if second == "zero":
                return first + " " + powers[idx][0]
            else:
                return first + " " + powers[idx][0] + " " + second
        idx = idx - 1
                    
if __name__ == "__main__":
    print(int_to_english(42))
    print(int_to_english(3 ** 7))
    print(int_to_english(2 ** 100))
    print(int_to_english(10 ** (2*64)))

```

