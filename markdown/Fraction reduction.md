# Fraction reduction

## Task Link
[Rosetta Code - Fraction reduction](https://rosettacode.org/wiki/Fraction_reduction)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FractionReduction {

    public static void main(String[] args) {
        for ( int size = 2 ; size <= 5 ; size++ ) {
            reduce(size);
        }
    }
    
    private static void reduce(int numDigits) {
        System.out.printf("Fractions with digits of length %d where cancellation is valid.  Examples:%n", numDigits);
        
        //  Generate allowed numerator's and denominator's
        int min = (int) Math.pow(10, numDigits-1);
        int max = (int) Math.pow(10, numDigits) - 1;
        List<Integer> values = new ArrayList<>();
        for ( int number = min ; number <= max ; number++ ) {
            if ( isValid(number) ) {
                values.add(number);
            }
        }
        
        Map<Integer,Integer> cancelCount = new HashMap<>(); 
        int size = values.size();
        int solutions = 0;
        for ( int nIndex = 0 ; nIndex < size - 1 ; nIndex++ ) {
            int numerator = values.get(nIndex);
            //  Must be proper fraction
            for ( int dIndex = nIndex + 1 ; dIndex < size ; dIndex++ ) {
                int denominator = values.get(dIndex);
                for ( int commonDigit : digitsInCommon(numerator, denominator) ) {
                    int numRemoved = removeDigit(numerator, commonDigit);
                    int denRemoved = removeDigit(denominator, commonDigit);
                    if ( numerator * denRemoved == denominator * numRemoved ) {
                        solutions++;
                        cancelCount.merge(commonDigit, 1, (v1, v2) -> v1 + v2);
                        if ( solutions <= 12 ) {
                            System.out.printf("    When %d is removed, %d/%d = %d/%d%n", commonDigit, numerator, denominator, numRemoved, denRemoved);
                        }
                    }
                }
            }
        }
        System.out.printf("Number of fractions where cancellation is valid = %d.%n", solutions);
        List<Integer> sorted = new ArrayList<>(cancelCount.keySet());
        Collections.sort(sorted);
        for ( int removed : sorted ) {
            System.out.printf("    The digit %d was removed %d times.%n", removed, cancelCount.get(removed));
        }
        System.out.println();
    }
    
    private static int[] powers = new int[] {1, 10, 100, 1000, 10000, 100000};
    
    //  Remove the specified digit.
    private static int removeDigit(int n, int removed) {
        int m = 0;
        int pow = 0;
        while ( n > 0 ) {
            int r = n % 10;
            if ( r != removed ) {
                m = m + r*powers[pow];
                pow++;
            }
            n /= 10;
        }
        return m;
    }
        
    //  Assumes no duplicate digits individually in n1 or n2 - part of task
    private static List<Integer> digitsInCommon(int n1, int n2) {
        int[] count = new int[10];
        List<Integer> common = new ArrayList<>();
        while ( n1 > 0 ) {
            int r = n1 % 10;
            count[r] += 1;
            n1 /= 10;
        }
        while ( n2 > 0 ) {
            int r = n2 % 10;
            if ( count[r] > 0 ) {
                common.add(r);
            }
            n2 /= 10;
        }
        return common;
    }
    
    //  No repeating digits, no digit is zero.
    private static boolean isValid(int num) {
        int[] count = new int[10];
        while ( num > 0 ) {
            int r = num % 10;
            if ( r == 0 || count[r] == 1 ) {
                return false;
            }
            count[r] = 1;
            num /= 10;
        }
        return true;
    }

}

```

## Python Code
### python_code_1.txt
```python
def indexOf(haystack, needle):
    idx = 0
    for straw in haystack:
        if straw == needle:
            return idx
        else:
            idx += 1
    return -1

def getDigits(n, le, digits):
    while n > 0:
        r = n % 10
        if r == 0 or indexOf(digits, r) >= 0:
            return False
        le -= 1
        digits[le] = r
        n = int(n / 10)
    return True

def removeDigit(digits, le, idx):
    pows = [1, 10, 100, 1000, 10000]
    sum = 0
    pow = pows[le - 2]
    i = 0
    while i < le:
        if i == idx:
            i += 1
            continue
        sum = sum + digits[i] * pow
        pow = int(pow / 10)
        i += 1
    return sum

def main():
    lims = [ [ 12, 97 ], [ 123, 986 ], [ 1234, 9875 ], [ 12345, 98764 ] ]
    count = [0 for i in range(5)]
    omitted = [[0 for i in range(10)] for j in range(5)]

    i = 0
    while i < len(lims):
        n = lims[i][0]
        while n < lims[i][1]:
            nDigits = [0 for k in range(i + 2)]
            nOk = getDigits(n, i + 2, nDigits)
            if not nOk:
                n += 1
                continue
            d = n + 1
            while d <= lims[i][1] + 1:
                dDigits = [0 for k in range(i + 2)]
                dOk = getDigits(d, i + 2, dDigits)
                if not dOk:
                    d += 1
                    continue
                nix = 0
                while nix < len(nDigits):
                    digit = nDigits[nix]
                    dix = indexOf(dDigits, digit)
                    if dix >= 0:
                        rn = removeDigit(nDigits, i + 2, nix)
                        rd = removeDigit(dDigits, i + 2, dix)
                        if (1.0 * n / d) == (1.0 * rn / rd):
                            count[i] += 1
                            omitted[i][digit] += 1
                            if count[i] <= 12:
                                print "%d/%d = %d/%d by omitting %d's" % (n, d, rn, rd, digit)
                    nix += 1
                d += 1
            n += 1
        print
        i += 1

    i = 2
    while i <= 5:
        print "There are %d %d-digit fractions of which:" % (count[i - 2], i)
        j = 1
        while j <= 9:
            if omitted[i - 2][j] == 0:
                j += 1
                continue
            print "%6s have %d's omitted" % (omitted[i - 2][j], j)
            j += 1
        print
        i += 1
    return None

main()

```

