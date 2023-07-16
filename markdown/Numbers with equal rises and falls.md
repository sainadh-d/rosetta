# Numbers with equal rises and falls

## Task Link
[Rosetta Code - Numbers with equal rises and falls](https://rosettacode.org/wiki/Numbers_with_equal_rises_and_falls)

## Java Code
### java_code_1.txt
```java
public class EqualRisesFalls {
    public static void main(String[] args) {
        final int limit1 = 200;
        final int limit2 = 10000000;
        System.out.printf("The first %d numbers in the sequence are:\n", limit1);
        int n = 0;
        for (int count = 0; count < limit2; ) {
            if (equalRisesAndFalls(++n)) {
                ++count;
                if (count <= limit1)
                    System.out.printf("%3d%c", n, count % 20 == 0 ? '\n' : ' ');
            }
        }
        System.out.printf("\nThe %dth number in the sequence is %d.\n", limit2, n);
    }

    private static boolean equalRisesAndFalls(int n) {
        int total = 0;
        for (int previousDigit = -1; n > 0; n /= 10) {
            int digit = n % 10;
            if (previousDigit > digit)
                ++total;
            else if (previousDigit >= 0 && previousDigit < digit)
                --total;
            previousDigit = digit;
        }
        return total == 0;
    }
}

```

## Python Code
### python_code_1.txt
```python
import itertools

def riseEqFall(num):
    """Check whether a number belongs to sequence A296712."""
    height = 0
    d1 = num % 10
    num //= 10
    while num:
        d2 = num % 10
        height += (d1<d2) - (d1>d2)
        d1 = d2
        num //= 10
    return height == 0
    
def sequence(start, fn):
    """Generate a sequence defined by a function"""
    num=start-1
    while True:
        num += 1
        while not fn(num): num += 1
        yield num

a296712 = sequence(1, riseEqFall)

# Generate the first 200 numbers
print("The first 200 numbers are:")
print(*itertools.islice(a296712, 200))

# Generate the 10,000,000th number
print("The 10,000,000th number is:")
print(*itertools.islice(a296712, 10000000-200-1, 10000000-200))
# It is necessary to subtract 200 from the index, because 200 numbers
# have already been consumed.

```

