# Arithmetic derivative

## Task Link
[Rosetta Code - Arithmetic derivative](https://rosettacode.org/wiki/Arithmetic_derivative)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public final class ArithmeticDerivative {

	public static void main(String[] aArgs) {
        System.out.println("Arithmetic derivatives for -99 to 100 inclusive:");        
		for ( int n = -99, column = 0; n <= 100; n++ ) {
			System.out.print(String.format("%4d%s",
				derivative(BigInteger.valueOf(n)), ( ++column % 10 == 0 ) ? "\n" : " "));
		}
		System.out.println();
		
		final BigInteger seven = BigInteger.valueOf(7);
		for ( int power = 1; power <= 20; power++ ) {
			System.out.println(String.format("%s%2d%s%d",
				"D(10^", power, ") / 7 = ", derivative(BigInteger.TEN.pow(power)).divide(seven)));
		}
	}
	
	private static BigInteger derivative(BigInteger aNumber) {
		if ( aNumber.signum() == -1 ) {
			return derivative(aNumber.negate()).negate();
		}
		if ( aNumber == BigInteger.ZERO || aNumber == BigInteger.ONE ) {
			return BigInteger.ZERO;
		}
		BigInteger divisor = BigInteger.TWO;
		while ( divisor.multiply(divisor).compareTo(aNumber) <= 0 ) {
		    if ( aNumber.mod(divisor).signum() == 0 ) {
		        final BigInteger quotient = aNumber.divide(divisor);
		        return quotient.multiply(derivative(divisor)).add(divisor.multiply(derivative(quotient)));
		    }
		    divisor = divisor.add(BigInteger.ONE);
		}
		return BigInteger.ONE;
	}

}

```

## Python Code
### python_code_1.txt
```python
from sympy.ntheory import factorint

def D(n):
    if n < 0:
        return -D(-n)
    elif n < 2:
        return 0
    else:
        fdict = factorint(n)
        if len(fdict) == 1 and 1 in fdict: # is prime
            return 1
        return sum([n * e // p for p, e in fdict.items()])

for n in range(-99, 101):
    print('{:5}'.format(D(n)), end='\n' if n % 10 == 0 else '')

print()
for m in range(1, 21):
    print('(D for 10**{}) divided by 7 is {}'.format(m, D(10 ** m) // 7))

```

