# Convert decimal number to rational

## Task Link
[Rosetta Code - Convert decimal number to rational](https://rosettacode.org/wiki/Convert_decimal_number_to_rational)

## Java Code
### java_code_1.txt
```java
double fractionToDecimal(String string) {
    int indexOf = string.indexOf(' ');
    int integer = 0;
    int numerator, denominator;
    if (indexOf != -1) {
        integer = Integer.parseInt(string.substring(0, indexOf));
        string = string.substring(indexOf + 1);
    }
    indexOf = string.indexOf('/');
    numerator = Integer.parseInt(string.substring(0, indexOf));
    denominator = Integer.parseInt(string.substring(indexOf + 1));
    return integer + ((double) numerator / denominator);
}

String decimalToFraction(double value) {
    String string = String.valueOf(value);
    string = string.substring(string.indexOf('.') + 1);
    int numerator = Integer.parseInt(string);
    int denominator = (int) Math.pow(10, string.length());
    int gcf = gcf(numerator, denominator);
    if (gcf != 0) {
        numerator /= gcf;
        denominator /= gcf;
    }
    int integer = (int) value;
    if (integer != 0)
        return "%d %d/%d".formatted(integer, numerator, denominator);
    return "%d/%d".formatted(numerator, denominator);
}

int gcf(int valueA, int valueB) {
    if (valueB == 0) return valueA;
    else return gcf(valueB, valueA % valueB);
}

```

### java_code_2.txt
```java
import org.apache.commons.math3.fraction.BigFraction;

public class Test {

    public static void main(String[] args) {
        double[] n = {0.750000000, 0.518518000, 0.905405400, 0.142857143,
            3.141592654, 2.718281828, -0.423310825, 31.415926536};

        for (double d : n)
            System.out.printf("%-12s : %s%n", d, new BigFraction(d, 0.00000002D, 10000));
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from fractions import Fraction
>>> for d in (0.9054054, 0.518518, 0.75): print(d, Fraction.from_float(d).limit_denominator(100))

0.9054054 67/74
0.518518 14/27
0.75 3/4
>>> for d in '0.9054054 0.518518 0.75'.split(): print(d, Fraction(d))

0.9054054 4527027/5000000
0.518518 259259/500000
0.75 3/4
>>>

```

### python_code_2.txt
```python
'''Approximate rationals from decimals'''

from math import (floor, gcd)
import sys


# approxRatio :: Float -> Float -> Ratio
def approxRatio(epsilon):
    '''The simplest rational approximation to
       n within the margin given by epsilon.
    '''
    def gcde(e, x, y):
        def _gcd(a, b):
            return a if b < e else _gcd(b, a % b)
        return _gcd(abs(x), abs(y))
    return lambda n: (lambda c=(
        gcde(epsilon if 0 < epsilon else (0.0001), 1, n)
    ): ratio(floor(n / c))(floor(1 / c)))()


# main :: IO ()
def main():
    '''Conversions at different levels of precision.'''

    xs = [0.9054054, 0.518518, 0.75]
    print(
        fTable(__doc__ + ' (epsilon of 1/10000):\n')(str)(
            lambda r: showRatio(r) + ' -> ' + repr(fromRatio(r))
        )(
            approxRatio(1 / 10000)
        )(xs)
    )
    print('\n')

    e = minBound(float)
    print(
        fTable(__doc__ + ' (epsilon of ' + repr(e) + '):\n')(str)(
            lambda r: showRatio(r) + ' -> ' + repr(fromRatio(r))
        )(
            approxRatio(e)
        )(xs)
    )


# GENERIC -------------------------------------------------

# fromRatio :: Ratio Int -> Float
def fromRatio(r):
    '''A floating point value derived from a
       a rational value.
    '''
    return r.get('numerator') / r.get('denominator')


# minBound :: Bounded Type -> a
def minBound(t):
    '''Minimum value for a bounded type.'''
    maxsize = sys.maxsize
    float_infomin = sys.float_info.min
    return {
        int: (-maxsize - 1),
        float: float_infomin,
        bool: False,
        str: chr(0)
    }[t]


# ratio :: Int -> Int -> Ratio Int
def ratio(n):
    '''Rational value constructed
       from a numerator and a denominator.
    '''
    def go(n, d):
        g = gcd(n, d)
        return {
            'type': 'Ratio',
            'numerator': n // g, 'denominator': d // g
        }
    return lambda d: go(n * signum(d), abs(d))


# showRatio :: Ratio -> String
def showRatio(r):
    '''String representation of the ratio r.'''
    d = r.get('denominator')
    return str(r.get('numerator')) + (
        ' / ' + str(d) if 1 != d else ''
    )


# signum :: Num -> Num
def signum(n):
    '''The sign of n.'''
    return -1 if 0 > n else (1 if 0 < n else 0)


# DISPLAY -------------------------------------------------

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


# MAIN ---
if __name__ == '__main__':
    main()

```

