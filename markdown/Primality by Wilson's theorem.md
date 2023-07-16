# Primality by Wilson's theorem

## Task Link
[Rosetta Code - Primality by Wilson's theorem](https://rosettacode.org/wiki/Primality_by_Wilson%27s_theorem)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class PrimaltyByWilsonsTheorem {

    public static void main(String[] args) {
        System.out.printf("Primes less than 100 testing by Wilson's Theorem%n");
        for ( int i = 0 ; i <= 100 ; i++ ) {
            if ( isPrime(i) ) {
                System.out.printf("%d ", i);
            }
        }
    }
    
    
    private static boolean isPrime(long p) {
        if ( p <= 1) {
            return false;
        }
        return fact(p-1).add(BigInteger.ONE).mod(BigInteger.valueOf(p)).compareTo(BigInteger.ZERO) == 0;
    }
    
    private static BigInteger fact(long n) {
        BigInteger fact = BigInteger.ONE;
        for ( int i = 2 ; i <= n ; i++ ) {
            fact = fact.multiply(BigInteger.valueOf(i));
        }
        return fact;
    }

}

```

## Python Code
### python_code_1.txt
```python
from math import factorial

def is_wprime(n):
    return n == 2 or (
        n > 1
        and n % 2 != 0
        and (factorial(n - 1) + 1) % n == 0
    )

if __name__ == '__main__':
    c = int(input('Enter upper limit: '))
    print(f'Primes under {c}:')
    print([n for n in range(c) if is_wprime(n)])

```

