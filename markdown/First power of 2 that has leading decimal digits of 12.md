# First power of 2 that has leading decimal digits of 12

## Task Link
[Rosetta Code - First power of 2 that has leading decimal digits of 12](https://rosettacode.org/wiki/First_power_of_2_that_has_leading_decimal_digits_of_12)

## Java Code
### java_code_1.txt
```java
public class FirstPowerOfTwo {

    public static void main(String[] args) {
        runTest(12, 1);
        runTest(12, 2);
        runTest(123, 45);
        runTest(123, 12345);
        runTest(123, 678910);
    }
    
    private static void runTest(int l, int n) {
        System.out.printf("p(%d, %d) = %,d%n", l, n, p(l, n));
    }
    
    public static int p(int l, int n) {
        int test = 0;
        double log = Math.log(2) / Math.log(10);
        int factor = 1;
        int loop = l;
        while ( loop > 10 ) {
            factor *= 10;
            loop /= 10;
        }
        while ( n > 0) {
            test++;
            int val = (int) (factor * Math.pow(10, test * log % 1));
            if ( val == l ) {
                n--;
            }
        }
        return test;
    }
    
}

```

## Python Code
### python_code_1.txt
```python
from math import log, modf, floor

def p(l, n, pwr=2):
    l = int(abs(l))
    digitcount = floor(log(l, 10))
    log10pwr = log(pwr, 10)
    raised, found = -1, 0
    while found < n:
        raised += 1
        firstdigits = floor(10**(modf(log10pwr * raised)[0] + digitcount))
        if firstdigits == l:
            found += 1
    return raised


if __name__ == '__main__':
    for l, n in [(12, 1), (12, 2), (123, 45), (123, 12345), (123, 678910)]:
        print(f"p({l}, {n}) =", p(l, n))

```

