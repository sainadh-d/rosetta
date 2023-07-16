# Loops/With multiple ranges

## Task Link
[Rosetta Code - Loops/With multiple ranges](https://rosettacode.org/wiki/Loops/With_multiple_ranges)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class LoopsWithMultipleRanges {

    private static long sum = 0;
    private static long prod = 1;
    
    public static void main(String[] args) {
        long x = 5;
        long y = -5;
        long z = -2;
        long one = 1;
        long three = 3;
        long seven = 7;
        
        List<Long> jList = new ArrayList<>();
        for ( long j = -three     ; j <= pow(3, 3)        ; j += three )  jList.add(j);
        for ( long j = -seven     ; j <= seven            ; j += x )      jList.add(j);
        for ( long j = 555        ; j <= 550-y            ; j += 1 )      jList.add(j);
        for ( long j = 22         ; j >= -28              ; j += -three ) jList.add(j);
        for ( long j = 1927       ; j <= 1939             ; j += 1 )      jList.add(j);
        for ( long j = x          ; j >= y                ; j += z )      jList.add(j);
        for ( long j = pow(11, x) ; j <= pow(11, x) + one ; j += 1 )      jList.add(j);

        List<Long> prodList = new ArrayList<>();
        for ( long j : jList ) {
            sum += Math.abs(j);
            if ( Math.abs(prod) < pow(2, 27) && j != 0 ) {
                prodList.add(j);
                prod *= j;
            }            
        }
        
        System.out.printf(" sum        = %,d%n", sum);
        System.out.printf("prod        = %,d%n", prod);
        System.out.printf("j values    = %s%n", jList);
        System.out.printf("prod values = %s%n", prodList);
    }
    
    private static long pow(long base, long exponent) {
        return (long) Math.pow(base, exponent);
    }
    
}

```

## Python Code
### python_code_1.txt
```python
from itertools import chain

prod, sum_, x, y, z, one,three,seven = 1, 0, 5, -5, -2, 1, 3, 7

def _range(x, y, z=1):
    return range(x, y + (1 if z > 0 else -1), z)

print(f'list(_range(x, y, z)) = {list(_range(x, y, z))}')
print(f'list(_range(-seven, seven, x)) = {list(_range(-seven, seven, x))}')

for j in chain(_range(-three, 3**3, three), _range(-seven, seven, x), 
               _range(555, 550 - y), _range(22, -28, -three),
               _range(1927, 1939), _range(x, y, z),
               _range(11**x, 11**x + 1)):
    sum_ += abs(j)
    if abs(prod) < 2**27 and (j != 0):
        prod *= j
print(f' sum= {sum_}\nprod= {prod}')

```

