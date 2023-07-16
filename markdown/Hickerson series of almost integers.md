# Hickerson series of almost integers

## Task Link
[Rosetta Code - Hickerson series of almost integers](https://rosettacode.org/wiki/Hickerson_series_of_almost_integers)

## Java Code
### java_code_1.txt
```java
import java.math.*;

public class Hickerson {

    final static String LN2 = "0.693147180559945309417232121458";

    public static void main(String[] args) {
        for (int n = 1; n <= 17; n++)
            System.out.printf("%2s is almost integer: %s%n", n, almostInteger(n));
    }

    static boolean almostInteger(int n) {
        BigDecimal a = new BigDecimal(LN2);
        a = a.pow(n + 1).multiply(BigDecimal.valueOf(2));

        long f = n;
        while (--n > 1)
            f *= n;

        BigDecimal b = new BigDecimal(f);
        b = b.divide(a, MathContext.DECIMAL128);

        BigInteger c = b.movePointRight(1).toBigInteger().mod(BigInteger.TEN);

        return c.toString().matches("0|9");
    }
}

```

## Python Code
### python_code_1.txt
```python
from decimal import Decimal
import math

def h(n):
    'Simple, reduced precision calculation'
    return math.factorial(n) / (2 * math.log(2) ** (n + 1))
    
def h2(n):
    'Extended precision Hickerson function'
    return Decimal(math.factorial(n)) / (2 * Decimal(2).ln() ** (n + 1))

for n in range(18):
    x = h2(n)
    norm = str(x.normalize())
    almostinteger = (' Nearly integer' 
                     if 'E' not in norm and ('.0' in norm or '.9' in norm) 
                     else ' NOT nearly integer!')
    print('n:%2i h:%s%s' % (n, norm, almostinteger))

```

