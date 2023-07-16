# Combinations and permutations

## Task Link
[Rosetta Code - Combinations and permutations](https://rosettacode.org/wiki/Combinations_and_permutations)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class CombinationsAndPermutations {

    public static void main(String[] args) {
        System.out.println(Double.MAX_VALUE);
        System.out.println("A sample of permutations from 1 to 12 with exact Integer arithmetic:");
        for ( int n = 1 ; n <= 12 ; n++ ) {
            int k = n / 2;
            System.out.printf("%d P %d = %s%n", n, k, permutation(n, k));
        }

        System.out.println();
        System.out.println("A sample of combinations from 10 to 60 with exact Integer arithmetic:");
        for ( int n = 10 ; n <= 60 ; n += 5 ) {
            int k = n / 2;
            System.out.printf("%d C %d = %s%n", n, k, combination(n, k));
        }
        
        System.out.println();
        System.out.println("A sample of permutations from 5 to 15000 displayed in floating point arithmetic:");
        System.out.printf("%d P %d = %s%n", 5, 2, display(permutation(5, 2), 50));
        for ( int n = 1000 ; n <= 15000 ; n += 1000 ) {
            int k = n / 2;
            System.out.printf("%d P %d = %s%n", n, k, display(permutation(n, k), 50));
        }
        
        System.out.println();
        System.out.println("A sample of combinations from 100 to 1000 displayed in floating point arithmetic:");
        for ( int n = 100 ; n <= 1000 ; n += 100 ) {
            int k = n / 2;
            System.out.printf("%d C %d = %s%n", n, k, display(combination(n, k), 50));
        }

    }
    
    private static String display(BigInteger val, int precision) {
        String s = val.toString();
        precision = Math.min(precision, s.length());
        StringBuilder sb = new StringBuilder();
        sb.append(s.substring(0, 1));
        sb.append(".");
        sb.append(s.substring(1, precision));
        sb.append(" * 10^");
        sb.append(s.length()-1);
        return sb.toString();
    }
    
    public static BigInteger combination(int n, int k) {
        //  Select value with smallest intermediate results
        //    combination(n, k) = combination(n, n-k) 
        if ( n-k < k ) {
            k = n-k;
        }
        BigInteger result = permutation(n, k);
        while ( k > 0 ) {
            result = result.divide(BigInteger.valueOf(k));
            k--;
        }
        return result;
    }
    
    public static BigInteger permutation(int n, int k) {
        BigInteger result = BigInteger.ONE;
        for ( int i = n ; i >= n-k+1 ; i-- ) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }
    
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

from scipy.misc import factorial as fact
from scipy.misc import comb

def perm(N, k, exact=0):
    return comb(N, k, exact) * fact(k, exact)

exact=True
print('Sample Perms 1..12')
for N in range(1, 13):
    k = max(N-2, 1)
    print('%iP%i =' % (N, k), perm(N, k, exact), end=', ' if N % 5 else '\n')
          
print('\n\nSample Combs 10..60')
for N in range(10, 61, 10):
    k = N-2
    print('%iC%i =' % (N, k), comb(N, k, exact), end=', ' if N % 50 else '\n')

exact=False
print('\n\nSample Perms 5..1500 Using FP approximations')
for N in [5, 15, 150, 1500, 15000]:
    k = N-2
    print('%iP%i =' % (N, k), perm(N, k, exact))
          
print('\nSample Combs 100..1000 Using FP approximations')
for N in range(100, 1001, 100):
    k = N-2
    print('%iC%i =' % (N, k), comb(N, k, exact))

```

