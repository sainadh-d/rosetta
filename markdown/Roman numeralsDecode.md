# Roman numerals/Decode

## Task Link
[Rosetta Code - Roman numerals/Decode](https://rosettacode.org/wiki/Roman_numerals/Decode)

## Java Code
### java_code_1.txt
```java
/* Parse Roman Numerals
   
   Nigel Galloway March 16th., 2012
*/
grammar ParseRN ;

options {
	language = Java;
}
@members {
int rnValue;
int ONE;
}

parseRN:	({rnValue = 0;} rn NEWLINE {System.out.println($rn.text + " = " + rnValue);})*
	;
	
rn	:	(Thousand {rnValue += 1000;})* hundreds? tens? units?;

hundreds:	{ONE = 0;} (h9 | h5) {if (ONE > 3) System.out.println ("Too many hundreds");};
h9	:	Hundred {ONE += 1;} (FiveHund {rnValue += 400;}| Thousand {rnValue += 900;}|{rnValue += 100;} (Hundred {rnValue += 100; ONE += 1;})*);
h5	:	FiveHund {rnValue += 500;} (Hundred {rnValue += 100; ONE += 1;})*;

tens	:	{ONE = 0;} (t9 | t5) {if (ONE > 3) System.out.println ("Too many tens");};
t9	:	Ten {ONE += 1;} (Fifty {rnValue += 40;}| Hundred {rnValue += 90;}|{rnValue += 10;} (Ten {rnValue += 10; ONE += 1;})*);
t5	:	Fifty {rnValue += 50;} (Ten {rnValue += 10; ONE += 1;})*;
	
units	:	{ONE = 0;} (u9 | u5) {if (ONE > 3) System.out.println ("Too many ones");};
u9	:	One {ONE += 1;} (Five {rnValue += 4;}| Ten {rnValue += 9;}|{rnValue += 1;} (One {rnValue += 1; ONE += 1;})*);
u5	:	Five {rnValue += 5;} (One {rnValue += 1; ONE += 1;})*;
	
One	:	'I';
Five	:	'V';
Ten	:	'X';
Fifty	:	'L';
Hundred:	'C';
FiveHund:	'D';
Thousand:	'M' ;
NEWLINE:	'\r'? '\n' ;

```

### java_code_2.txt
```java
public class Roman {
	private static int decodeSingle(char letter) {
		switch(letter) {
			case 'M': return 1000;
			case 'D': return 500;
			case 'C': return 100;
			case 'L': return 50;
			case 'X': return 10;
			case 'V': return 5;
			case 'I': return 1;
			default: return 0;
		}
	}
	public static int decode(String roman) {
		int result = 0;
		String uRoman = roman.toUpperCase(); //case-insensitive
		for(int i = 0;i < uRoman.length() - 1;i++) {//loop over all but the last character
			//if this character has a lower value than the next character
			if (decodeSingle(uRoman.charAt(i)) < decodeSingle(uRoman.charAt(i+1))) {
				//subtract it
				result -= decodeSingle(uRoman.charAt(i));
			} else {
				//add it
				result += decodeSingle(uRoman.charAt(i));
			}
		}
		//decode the last character, which is always added
		result += decodeSingle(uRoman.charAt(uRoman.length()-1));
		return result;
	}
	
	public static void main(String[] args) {
		System.out.println(decode("MCMXC")); //1990
		System.out.println(decode("MMVIII")); //2008
		System.out.println(decode("MDCLXVI")); //1666
	}
}

```

### java_code_3.txt
```java
import java.util.Set;
import java.util.EnumSet;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public interface RomanNumerals {
  public enum Numeral {
    M(1000), CM(900), D(500), CD(400), C(100), XC(90), L(50), XL(40), X(10), IX(9), V(5), IV(4), I(1);

    public final long weight;

    private static final Set<Numeral> SET = Collections.unmodifiableSet(EnumSet.allOf(Numeral.class));

    private Numeral(long weight) {
      this.weight = weight;
    }

    public static Numeral getLargest(long weight) {
      return SET.stream()
        .filter(numeral -> weight >= numeral.weight)
        .findFirst()
        .orElse(I)
      ;
    }
  };

  public static String encode(long n) {
    return LongStream.iterate(n, l -> l - Numeral.getLargest(l).weight)
      .limit(Numeral.values().length)
      .filter(l -> l > 0)
      .mapToObj(Numeral::getLargest)
      .map(String::valueOf)
      .collect(Collectors.joining())
    ;
  }

  public static long decode(String roman) {
    long result =  new StringBuilder(roman.toUpperCase()).reverse().chars()
      .mapToObj(c -> Character.toString((char) c))
      .map(numeral -> Enum.valueOf(Numeral.class, numeral))
      .mapToLong(numeral -> numeral.weight)
      .reduce(0, (a, b) -> a + (a <= b ? b : -b))
    ;
    if (roman.charAt(0) == roman.charAt(1)) {
      result += 2 * Enum.valueOf(Numeral.class, roman.substring(0, 1)).weight;
    }
    return result;
  }

  public static void test(long n) {
    System.out.println(n + " = " + encode(n));
    System.out.println(encode(n) + " = " + decode(encode(n)));
  }

  public static void main(String[] args) {
    LongStream.of(1999, 25, 944).forEach(RomanNumerals::test);
  }
}

```

## Python Code
### python_code_1.txt
```python
_rdecode = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))

def decode( roman ):
    result = 0
    for r, r1 in zip(roman, roman[1:]):
        rd, rd1 = _rdecode[r], _rdecode[r1]
        result += -rd if rd < rd1 else rd
    return result + _rdecode[roman[-1]]

if __name__ == '__main__':
    for r in 'MCMXC MMVIII MDCLXVI'.split():
        print( r, decode(r) )

```

### python_code_2.txt
```python
roman_values = (('I',1), ('IV',4), ('V',5), ('IX',9),('X',10),('XL',40),('L',50),('XC',90),('C',100),
                    ('CD', 400), ('D', 500), ('CM', 900), ('M',1000))

def roman_value(roman):
    total=0
    for symbol,value in reversed(roman_values):
        while roman.startswith(symbol):
            total += value
            roman = roman[len(symbol):]
    return total

if __name__=='__main__':
    for value in "MCMXC", "MMVIII", "MDCLXVI":
        print('%s = %i' % (value, roman_value(value)))

```

### python_code_3.txt
```python
numerals = { 'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1 }
def romannumeral2number(s):
        return reduce(lambda x, y: -x + y if x < y else x + y, map(lambda x: numerals.get(x, 0), s.upper()))

```

### python_code_4.txt
```python
'''Roman numerals decoded'''

from operator import mul
from functools import reduce
from collections import defaultdict
from itertools import accumulate, chain, cycle


# intFromRoman :: String -> Maybe Int
def intFromRoman(s):
    '''Just the integer represented by a Roman
       numeral string, or Nothing if any
       characters are unrecognised.
    '''
    dct = defaultdict(
        lambda: None,
        zip(
            'IVXLCDM',
            accumulate(chain([1], cycle([5, 2])), mul)
        )
    )

    def go(mb, x):
        '''Just a letter value added to or
           subtracted from a total, or Nothing
           if no letter value is defined.
        '''
        if None in (mb, x):
            return None
        else:
            r, total = mb
            return x, total + (-x if x < r else x)

    return bindMay(reduce(
        go,
        [dct[k.upper()] for k in reversed(list(s))],
        (0, 0)
    ))(snd)


# ------------------------- TEST -------------------------
def main():
    '''Testing a sample of dates.'''

    print(
        fTable(__doc__ + ':\n')(str)(
            maybe('(Contains unknown character)')(str)
        )(
            intFromRoman
        )([
            "MDCLXVI", "MCMXC", "MMVIII",
            "MMXVI", "MMXVIII", "MMZZIII"
        ])
    )


# ----------------------- GENERIC ------------------------

# bindMay (>>=) :: Maybe a -> (a -> Maybe b) -> Maybe b
def bindMay(m):
    '''Injection operator for the Maybe monad.
       If m is Nothing, it is passed straight through.
       If m is Just(x), the result is an application
       of the (a -> Maybe b) function (mf) to x.'''
    return lambda mf: (
        m if None is m else mf(m)
    )


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if None is m else (
        f(m)
    )


# snd :: (a, b) -> b
def snd(ab):
    '''Second member of a pair.'''
    return ab[1]


# ---------------------- FORMATTING ----------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
       fx display function -> f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: (
                f'{y.rjust(w, " ")} -> {fxShow(f(x))}'
            ),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: (
        lambda xs: go(xShow, fxShow, f, xs)
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

