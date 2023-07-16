# Roman numerals/Encode

## Task Link
[Rosetta Code - Roman numerals/Encode](https://rosettacode.org/wiki/Roman_numerals/Encode)

## Java Code
### java_code_1.txt
```java
public class RN {

    enum Numeral {
        I(1), IV(4), V(5), IX(9), X(10), XL(40), L(50), XC(90), C(100), CD(400), D(500), CM(900), M(1000);
        int weight;

        Numeral(int weight) {
            this.weight = weight;
        }
    };

    public static String roman(long n) {
        
        if( n <= 0) {
            throw new IllegalArgumentException();
        }
        
        StringBuilder buf = new StringBuilder();

        final Numeral[] values = Numeral.values();
        for (int i = values.length - 1; i >= 0; i--) {
            while (n >= values[i].weight) {
                buf.append(values[i]);
                n -= values[i].weight;
            }
        }
        return buf.toString();
    }

    public static void test(long n) {
        System.out.println(n + " = " + roman(n));
    }

    public static void main(String[] args) {
        test(1999);
        test(25);
        test(944);
        test(0);
    }

}

```

### java_code_2.txt
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
import roman
print(roman.toRoman(2022))

```

### python_code_2.txt
```python
def toRoman(n):
    res=''		#converts int to str(Roman numeral)
    reg=n		#using the numerals (M,D,C,L,X,V,I)
    if reg<4000:#no more than three repetitions
        while reg>=1000:	#thousands up to MMM
            res+='M'		#MAX is MMMCMXCIX
            reg-=1000		
        if reg>=900:		#nine hundreds in 900-999
            res+='CM'
            reg-=900
        if reg>=500:		#five hudreds in 500-899
            res+='D'
            reg-=500
        if reg>=400:		#four hundreds in 400-499
            res+='CD'
            reg-=400
        while reg>=100:		#hundreds in 100-399
            res+='C'
            reg-=100
        if reg>=90:			#nine tens in 90-99
            res+='XC'
            reg-=90
        if reg>=50:			#five Tens in 50-89
            res+='L'
            reg-=50
        if reg>=40:
            res+='XL'		#four Tens
            reg-=40
        while reg>=10:
            res+="X"		#tens
            reg-=10
        if reg>=9:
            res+='IX'		#nine Units
            reg-=9
        if reg>=5:
            res+='V'		#five Units
            reg-=5
        if reg>=4:
            res+='IV'		#four Units
            reg-=4
        while reg>0:		#three or less Units
            res+='I'
            reg-=1
    return res

```

### python_code_3.txt
```python
roman =        "MDCLXVmdclxvi"; # UPPERCASE for thousands #
adjust_roman = "CCXXmmccxxii";
arabic =       (1000000, 500000, 100000, 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1);
adjust_arabic = (100000, 100000,  10000, 10000,  1000, 1000,  100, 100,  10, 10,  1, 1, 0);

def arabic_to_roman(dclxvi):
  org = dclxvi; # 666 #
  out = "";
  for scale,arabic_scale  in enumerate(arabic): 
    if org == 0: break
    multiples = org / arabic_scale;
    org -= arabic_scale * multiples;
    out += roman[scale] * multiples;
    if org >= -adjust_arabic[scale] + arabic_scale: 
      org -= -adjust_arabic[scale] + arabic_scale;
      out +=  adjust_roman[scale] +  roman[scale]
  return out
 
if __name__ == "__main__": 
  test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,50,60,69,70,
     80,90,99,100,200,300,400,500,600,666,700,800,900,1000,1009,1444,1666,1945,1997,1999,
     2000,2008,2500,3000,4000,4999,5000,6666,10000,50000,100000,500000,1000000);
  for val in test: 
    print '%d - %s'%(val, arabic_to_roman(val))

```

### python_code_4.txt
```python
romanDgts= 'ivxlcdmVXLCDM_'

def ToRoman(num):
   namoR = ''
   if num >=4000000:
      print 'Too Big -'
      return '-----'
   for rdix in range(0, len(romanDgts), 2):
      if num==0: break
      num,r = divmod(num,10)
      v,r = divmod(r, 5)
      if r==4:
         namoR += romanDgts[rdix+1+v] + romanDgts[rdix]
      else:
         namoR += r*romanDgts[rdix] + (romanDgts[rdix+1] if(v==1) else '')
   return namoR[-1::-1]

```

### python_code_5.txt
```python
anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M CM D CD C XC L XL X IX V IV I".split()

def to_roman(x):
    ret = []
    for a,r in zip(anums, rnums):
        n,x = divmod(x,a)
        ret.append(r*n)
    return ''.join(ret)
        
if __name__ == "__main__":
    test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,
            50,60,69,70,80,90,99,100,200,300,400,500,600,666,700,800,900,
            1000,1009,1444,1666,1945,1997,1999,2000,2008,2010,2011,2500,
            3000,3999)
    
    for val in test:
        print '%d - %s'%(val, to_roman(val))

```

### python_code_6.txt
```python
def arabic_to_roman(dclxvi):
#===========================
  '''Convert an integer from the decimal notation to the Roman notation'''
  org = dclxvi; # 666 #
  out = "";
  for scale, arabic_scale  in enumerate(arabic):
    if org == 0: break
    multiples = org // arabic_scale;
    org -= arabic_scale * multiples;
    out += roman[scale] * multiples;
    if (org >= -adjust_arabic[scale] + arabic_scale):
      org -= -adjust_arabic[scale] + arabic_scale;
      out +=  adjust_roman[scale] +  roman[scale]
  return out

if __name__ == "__main__": 
  test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,50,60,69,70,
     80,90,99,100,200,300,400,500,600,666,700,800,900,1000,1009,1444,1666,1945,1997,1999,
     2000,2008,2500,3000,4000,4999,5000,6666,10000,50000,100000,500000,1000000);
  
  for val in test: 
    print("%8d %s" %(val, arabic_to_roman(val)))

```

### python_code_7.txt
```python
rnl = [ { '4' : 'MMMM', '3' : 'MMM', '2' : 'MM', '1' : 'M', '0' : '' }, { '9' : 'CM', '8' : 'DCCC', '7' : 'DCC',
          '6' : 'DC', '5' : 'D', '4' : 'CD', '3' : 'CCC', '2' : 'CC', '1' : 'C', '0' : '' }, { '9' : 'XC',
          '8' : 'LXXX', '7' : 'LXX', '6' : 'LX', '5' : 'L', '4' : 'XL', '3' : 'XXX', '2' : 'XX', '1' : 'X',
          '0' : '' }, { '9' : 'IX', '8' : 'VIII', '7' : 'VII', '6' : 'VI', '5' : 'V', '4' : 'IV', '3' : 'III',
          '2' : 'II', '1' : 'I', '0' : '' }]
# Option 1
def number2romannumeral(n):
    return ''.join([rnl[x][y] for x, y in zip(range(4), str(n).zfill(4)) if n < 5000 and n > -1])
# Option 2
def number2romannumeral(n):
    return reduce(lambda x, y: x + y, map(lambda x, y: rnl[x][y], range(4), str(n).zfill(4))) if -1 < n < 5000 else None

```

### python_code_8.txt
```python
'''Encoding Roman Numerals'''

from functools import reduce
from itertools import chain


# romanFromInt ::  Int -> String
def romanFromInt(n):
    '''A string of Roman numerals encoding an integer.'''
    def go(a, ms):
        m, s = ms
        q, r = divmod(a, m)
        return (r, s * q)

    return concat(snd(mapAccumL(go)(n)(
        zip([
            1000, 900, 500, 400, 100, 90, 50,
            40, 10, 9, 5, 4, 1
        ], [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
            'XL', 'X', 'IX', 'V', 'IV', 'I'
        ])
    )))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Sample of years'''
    for s in [
            romanFromInt(x) for x in [
                1666, 1990, 2008, 2016, 2018, 2020
            ]
    ]:
        print(s)


# ------------------ GENERIC FUNCTIONS -------------------

# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xxs):
    '''The concatenation of all the elements in a list.'''
    xs = list(chain.from_iterable(xxs))
    unit = '' if isinstance(xs, str) else []
    return unit if not xs else (
        ''.join(xs) if isinstance(xs[0], str) else xs
    )


# mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a list derived by a
       combined map and fold,
       with accumulation from left to right.'''
    def go(a, x):
        tpl = f(a[0], x)
        return (tpl[0], a[1] + [tpl[1]])
    return lambda acc: lambda xs: (
        reduce(go, xs, (acc, []))
    )


# snd :: (a, b) -> b
def snd(tpl):
    '''Second component of a tuple.'''
    return tpl[1]


# MAIN ---
if __name__ == '__main__':
    main()

```

