# Jacobi symbol

## Task Link
[Rosetta Code - Jacobi symbol](https://rosettacode.org/wiki/Jacobi_symbol)

## Java Code
### java_code_1.txt
```java
public class JacobiSymbol {

    public static void main(String[] args) {
        int max = 30;
        System.out.printf("n\\k ");
        for ( int k = 1 ; k <= max ; k++ ) {
            System.out.printf("%2d  ", k);
        }
        System.out.printf("%n");
        for ( int n = 1 ; n <= max ; n += 2 ) {
            System.out.printf("%2d  ", n);
            for ( int k = 1 ; k <= max ; k++ ) {
                System.out.printf("%2d  ", jacobiSymbol(k, n));
            }
            System.out.printf("%n");
        }
    }
    
    
    //  Compute (k n), where k is numerator
    private static int jacobiSymbol(int k, int n) {
        if ( k < 0 || n % 2 == 0 ) {
            throw new IllegalArgumentException("Invalid value. k = " + k + ", n = " + n);
        }
        k %= n;
        int jacobi = 1;
        while ( k > 0 ) {
            while ( k % 2 == 0 ) {
                k /= 2;
                int r = n % 8;
                if ( r == 3 || r == 5 ) {
                    jacobi = -jacobi;
                }
            }
            int temp = n;
            n = k;
            k = temp;
            if ( k % 4 == 3 && n % 4 == 3 ) {
                jacobi = -jacobi;
            }
            k %= n;
        }
        if ( n == 1 ) {
            return jacobi;
        }
        return 0;
    }

}

```

## Python Code
### python_code_1.txt
```python
def jacobi(a, n):
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    if n % 2 == 0:
        raise ValueError("'n' must be odd.")
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0

```

