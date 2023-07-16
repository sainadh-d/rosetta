# Almkvist-Giullera formula for pi

## Task Link
[Rosetta Code - Almkvist-Giullera formula for pi](https://rosettacode.org/wiki/Almkvist-Giullera_formula_for_pi)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.math.RoundingMode;

public final class AlmkvistGiulleraFormula {

	public static void main(String[] aArgs) {
		System.out.println("n                                   Integer part");
		System.out.println("================================================");
		for ( int n = 0; n <= 9; n++ ) {
			System.out.println(String.format("%d%47s", n, almkvistGiullera(n).toString()));
		}
		
		final int decimalPlaces = 70;
		final MathContext mathContext = new MathContext(decimalPlaces + 1, RoundingMode.HALF_EVEN);
		final BigDecimal epsilon = BigDecimal.ONE.divide(BigDecimal.TEN.pow(decimalPlaces));		
		BigDecimal previous = BigDecimal.ONE;		
		BigDecimal sum = BigDecimal.ZERO;
		BigDecimal pi = BigDecimal.ZERO;
		int n = 0;
		
		while ( pi.subtract(previous).abs().compareTo(epsilon) >= 0 ) {
			BigDecimal nextTerm = new BigDecimal(almkvistGiullera(n)).divide(BigDecimal.TEN.pow(6 * n + 3));			
			sum = sum.add(nextTerm);			
			previous = pi;
			n += 1;
			pi = BigDecimal.ONE.divide(sum, mathContext).sqrt(mathContext);
		}
		
		System.out.println(System.lineSeparator() + "pi to " + decimalPlaces + " decimal places:");
		System.out.println(pi);
	}	
	
	// The integer part of the n'th term of Almkvist-Giullera series.
	private static BigInteger almkvistGiullera(int aN) {
	    BigInteger term1 = factorial(6 * aN).multiply(BigInteger.valueOf(32));
	    BigInteger term2 = BigInteger.valueOf(532 * aN * aN + 126 * aN + 9);
	    BigInteger term3 = factorial(aN).pow(6).multiply(BigInteger.valueOf(3));
	    return term1.multiply(term2).divide(term3);
	}

	private static BigInteger factorial(int aNumber) {
	    BigInteger result = BigInteger.ONE;
	    for ( int i = 2; i <= aNumber; i++ ) {
	    	result = result.multiply(BigInteger.valueOf(i));
	    }
	    return result;
	}
	
}

```

## Python Code
### python_code_1.txt
```python
import mpmath as mp

with mp.workdps(72):

    def integer_term(n):
        p = 532 * n * n + 126 * n + 9
        return (p * 2**5 * mp.factorial(6 * n)) / (3 * mp.factorial(n)**6)

    def exponent_term(n):
        return -(mp.mpf("6.0") * n + 3)

    def nthterm(n):
        return integer_term(n) * mp.mpf("10.0")**exponent_term(n)


    for n in range(10):
        print("Term ", n, '  ', int(integer_term(n)))


    def almkvist_guillera(floatprecision):
        summed, nextadd = mp.mpf('0.0'), mp.mpf('0.0')
        for n in range(100000000):
            nextadd = summed + nthterm(n)
            if abs(nextadd - summed) < 10.0**(-floatprecision):
                break

            summed = nextadd

        return nextadd


    print('\nπ to 70 digits is ', end='')
    mp.nprint(mp.mpf(1.0 / mp.sqrt(almkvist_guillera(70))), 71)
    print('mpmath π is       ', end='')
    mp.nprint(mp.pi, 71)

```

