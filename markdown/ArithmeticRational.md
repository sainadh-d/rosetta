# Arithmetic/Rational

## Task Link
[Rosetta Code - Arithmetic/Rational](https://rosettacode.org/wiki/Arithmetic/Rational)

## Java Code
### java_code_1.txt
```java
public class BigRationalFindPerfectNumbers {
    public static void main(String[] args) {
        int MAX_NUM = 1 << 19;
        System.out.println("Searching for perfect numbers in the range [1, " + (MAX_NUM - 1) + "]");

        BigRational TWO = BigRational.valueOf(2);
        for (int i = 1; i < MAX_NUM; i++) {
            BigRational reciprocalSum = BigRational.ONE;
            if (i > 1)
                reciprocalSum = reciprocalSum.add(BigRational.valueOf(i).reciprocal());
            int maxDivisor = (int) Math.sqrt(i);
            if (maxDivisor >= i)
                maxDivisor--;

            for (int divisor = 2; divisor <= maxDivisor; divisor++) {
                if (i % divisor == 0) {
                    reciprocalSum = reciprocalSum.add(BigRational.valueOf(divisor).reciprocal());
                    int dividend = i / divisor;
                    if (divisor != dividend)
                        reciprocalSum = reciprocalSum.add(BigRational.valueOf(dividend).reciprocal());
                }
            }
            if (reciprocalSum.equals(TWO))
                System.out.println(String.valueOf(i) + " is a perfect number");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction

for candidate in range(2, 2**19):
  sum = Fraction(1, candidate)
  for factor in range(2, int(candidate**0.5)+1):
    if candidate % factor == 0:
      sum += Fraction(1, factor) + Fraction(1, candidate // factor)
  if sum.denominator == 1:
    print("Sum of recipr. factors of %d = %d exactly %s" %
           (candidate, int(sum), "perfect!" if sum == 1 else ""))

```

### python_code_2.txt
```python
def lcm(a, b):
    return a // gcd(a,b) * b

def gcd(u, v):
    return gcd(v, u%v) if v else abs(u)

class Fraction:
    def __init__(self, numerator, denominator):
        common = gcd(numerator, denominator)
        self.numerator = numerator//common
        self.denominator = denominator//common
    def __add__(self, frac):
        common = lcm(self.denominator, frac.denominator)
        n = common // self.denominator * self.numerator + common // frac.denominator * frac.numerator
        return Fraction(n, common)
    def __sub__(self, frac):
        return self.__add__(-frac)
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))
    def __mul__(self, frac):
        return Fraction(self.numerator * frac.numerator, self.denominator * frac.denominator)
    def __div__(self, frac):
        return self.__mul__(frac.reciprocal())
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)
    def __cmp__(self, n):
        return int(float(self) - float(n))
    def __float__(self):
        return float(self.numerator / self.denominator)
    def __int__(self):
        return (self.numerator // self.denominator)

```

