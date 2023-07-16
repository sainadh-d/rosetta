# Arithmetic-geometric mean/Calculate Pi

## Task Link
[Rosetta Code - Arithmetic-geometric mean/Calculate Pi](https://rosettacode.org/wiki/Arithmetic-geometric_mean/Calculate_Pi)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.math.MathContext;
import java.util.Objects;

public class Calculate_Pi {
    private static final MathContext con1024 = new MathContext(1024);
    private static final BigDecimal bigTwo = new BigDecimal(2);
    private static final BigDecimal bigFour = new BigDecimal(4);

    private static BigDecimal bigSqrt(BigDecimal bd, MathContext con) {
        BigDecimal x0 = BigDecimal.ZERO;
        BigDecimal x1 = BigDecimal.valueOf(Math.sqrt(bd.doubleValue()));
        while (!Objects.equals(x0, x1)) {
            x0 = x1;
            x1 = bd.divide(x0, con).add(x0).divide(bigTwo, con);
        }
        return x1;
    }

    public static void main(String[] args) {
        BigDecimal a = BigDecimal.ONE;
        BigDecimal g = a.divide(bigSqrt(bigTwo, con1024), con1024);
        BigDecimal t;
        BigDecimal sum = BigDecimal.ZERO;
        BigDecimal pow = bigTwo;
        while (!Objects.equals(a, g)) {
            t = a.add(g).divide(bigTwo, con1024);
            g = bigSqrt(a.multiply(g), con1024);
            a = t;
            pow = pow.multiply(bigTwo);
            sum = sum.add(a.multiply(a).subtract(g.multiply(g)).multiply(pow));
        }
        BigDecimal pi = bigFour.multiply(a.multiply(a)).divide(BigDecimal.ONE.subtract(sum), con1024);
        System.out.println(pi);
    }
}

```

## Python Code
### python_code_1.txt
```python
from decimal import *

D = Decimal
getcontext().prec = 100
a = n = D(1)
g, z, half = 1 / D(2).sqrt(), D(0.25), D(0.5)
for i in range(18):
    x = [(a + g) * half, (a * g).sqrt()]
    var = x[0] - a
    z -= var * var * n
    n += n
    a, g = x    
print(a * a / z)

```

