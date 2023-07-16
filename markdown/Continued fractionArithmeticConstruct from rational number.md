# Continued fraction/Arithmetic/Construct from rational number

## Task Link
[Rosetta Code - Continued fraction/Arithmetic/Construct from rational number](https://rosettacode.org/wiki/Continued_fraction/Arithmetic/Construct_from_rational_number)

## Java Code
### java_code_1.txt
```java
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class ConstructFromRationalNumber {
    private static class R2cf implements Iterator<Integer> {
        private int num;
        private int den;

        R2cf(int num, int den) {
            this.num = num;
            this.den = den;
        }

        @Override
        public boolean hasNext() {
            return den != 0;
        }

        @Override
        public Integer next() {
            int div = num / den;
            int rem = num % den;
            num = den;
            den = rem;
            return div;
        }
    }

    private static void iterate(R2cf generator) {
        generator.forEachRemaining(n -> System.out.printf("%d ", n));
        System.out.println();
    }

    public static void main(String[] args) {
        List<Map.Entry<Integer, Integer>> fracs = List.of(
                Map.entry(1, 2),
                Map.entry(3, 1),
                Map.entry(23, 8),
                Map.entry(13, 11),
                Map.entry(22, 7),
                Map.entry(-151, 77)
        );
        for (Map.Entry<Integer, Integer> frac : fracs) {
            System.out.printf("%4d / %-2d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }

        System.out.println("\nSqrt(2) ->");
        List<Map.Entry<Integer, Integer>> root2 = List.of(
                Map.entry(    14_142,     10_000),
                Map.entry(   141_421,    100_000),
                Map.entry( 1_414_214,  1_000_000),
                Map.entry(14_142_136, 10_000_000)
        );
        for (Map.Entry<Integer, Integer> frac : root2) {
            System.out.printf("%8d / %-8d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }

        System.out.println("\nPi ->");
        List<Map.Entry<Integer, Integer>> pi = List.of(
                Map.entry(         31,        10),
                Map.entry(        314,       100),
                Map.entry(      3_142,      1_000),
                Map.entry(     31_428,     10_000),
                Map.entry(    314_285,    100_000),
                Map.entry(  3_142_857,   1_000_000),
                Map.entry( 31_428_571,  10_000_000),
                Map.entry(314_285_714, 100_000_000)
        );
        for (Map.Entry<Integer, Integer> frac : pi) {
            System.out.printf("%9d / %-9d = ", frac.getKey(), frac.getValue());
            iterate(new R2cf(frac.getKey(), frac.getValue()));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def r2cf(n1,n2):
  while n2:
    n1, (t1, n2) = n2, divmod(n1, n2)
    yield t1

print(list(r2cf(1,2)))    # => [0, 2]
print(list(r2cf(3,1)))    # => [3]
print(list(r2cf(23,8)))    # => [2, 1, 7]
print(list(r2cf(13,11)))    # => [1, 5, 2]
print(list(r2cf(22,7)))    # => [3, 7]
print(list(r2cf(14142,10000)))    # => [1, 2, 2, 2, 2, 2, 1, 1, 29]
print(list(r2cf(141421,100000)))    # => [1, 2, 2, 2, 2, 2, 2, 3, 1, 1, 3, 1, 7, 2]
print(list(r2cf(1414214,1000000)))    # => [1, 2, 2, 2, 2, 2, 2, 2, 3, 6, 1, 2, 1, 12]
print(list(r2cf(14142136,10000000)))    # => [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 1, 2, 4, 1, 1, 2]

```

### python_code_2.txt
```python
def real2cf(x):
    while True:
        t1, f = divmod(x, 1)
        yield int(t1)
        if not f:
            break
        x = 1/f

from fractions import Fraction
from itertools import islice

print(list(real2cf(Fraction(13, 11))))    # => [1, 5, 2]
print(list(islice(real2cf(2 ** 0.5), 20)))    # => [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

```

