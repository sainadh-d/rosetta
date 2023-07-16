# Lah numbers

## Task Link
[Rosetta Code - Lah numbers](https://rosettacode.org/wiki/Lah_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class LahNumbers {

    public static void main(String[] args) {
        System.out.println("Show the unsigned Lah numbers up to n = 12:");
        for ( int n = 0 ; n <= 12 ; n++ ) {
            System.out.printf("%5s", n);
            for ( int k = 0 ; k <= n ; k++ ) {
                System.out.printf("%12s", lahNumber(n, k));
            }
            System.out.printf("%n");
        }
        
        System.out.println("Show the maximum value of L(100, k):");
        int n = 100;
        BigInteger max = BigInteger.ZERO;
        for ( int k = 0 ; k <= n ; k++ ) {
            max = max.max(lahNumber(n, k));
        }
        System.out.printf("%s", max);
    }
    
    private static Map<String,BigInteger> CACHE = new HashMap<>();
    
    private static BigInteger lahNumber(int n, int k) {
        String key = n + "," + k;
        if ( CACHE.containsKey(key) ) {
            return CACHE.get(key);
        }
        
        //  L(n,0) = 0;
        BigInteger result;
        if ( n == 0 && k == 0 ) {
            result = BigInteger.ONE;
        }
        else if ( k == 0 ) {
            result = BigInteger.ZERO;
        }
        else if ( k > n ) {
            result = BigInteger.ZERO;
        }
        else if ( n == 1 && k == 1 ) {
            result = BigInteger.ONE;
        }
        else {
            result = BigInteger.valueOf(n-1+k).multiply(lahNumber(n-1,k)).add(lahNumber(n-1,k-1));
        }
        
        CACHE.put(key, result);
        
        return result;
    }

}

```

## Python Code
### python_code_1.txt
```python
from math import (comb,
                  factorial)


def lah(n, k):
    if k == 1:
        return factorial(n)
    if k == n:
        return 1
    if k > n:
        return 0
    if k < 1 or n < 1:
        return 0
    return comb(n, k) * factorial(n - 1) // factorial(k - 1)


def main():
    print("Unsigned Lah numbers: L(n, k):")
    print("n/k ", end='\t')
    for i in range(13):
        print("%11d" % i, end='\t')
    print()
    for row in range(13):
        print("%-4d" % row, end='\t')
        for i in range(row + 1):
            l = lah(row, i)
            print("%11d" % l, end='\t')
        print()
    print("\nMaximum value from the L(100, *) row:")
    max_val = max(lah(100, a) for a in range(100))
    print(max_val)


if __name__ == '__main__':
    main()

```

