# Harmonic series

## Task Link
[Rosetta Code - Harmonic series](https://rosettacode.org/wiki/Harmonic_series)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class HarmonicSeries {
	
	public static void main(String[] aArgs) {
		
		System.out.println("The first twenty Harmonic numbers:");
		for ( int i = 1; i <= 20; i++ ) {
			System.out.println(String.format("%2s", i) + ": " + harmonicNumber(i));
		}		
		
		System.out.println();
		for ( int i = 1; i <= 10; i++ ) {
			System.out.print("The first term greater than ");
			System.out.println(String.format("%2s%s%5s", i, " is Term ", indexedHarmonic(i)));
		}

	}

    private static Rational harmonicNumber(int aNumber) {
		Rational result = Rational.ZERO;
		for ( int i = 1; i <= aNumber; i++ ) {
			result = result.add( new Rational(BigInteger.ONE, BigInteger.valueOf(i)) );
		}
		
		return result;
	}
	
	private static int indexedHarmonic(int aTarget) {
		BigInteger target = BigInteger.valueOf(aTarget);
		Rational harmonic = Rational.ZERO;
		BigInteger next = BigInteger.ZERO;
		
		while ( harmonic.numerator.compareTo(target.multiply(harmonic.denominator)) <= 0 ) {
			next = next.add(BigInteger.ONE);
			harmonic = harmonic.add( new Rational(BigInteger.ONE, next) );						
		}
		
		return next.intValueExact();
	}	
	
	private static class Rational {
		
		private Rational(BigInteger aNumerator, BigInteger aDenominator) {
			numerator = aNumerator;
			denominator = aDenominator;
			
	    	BigInteger gcd = numerator.gcd(denominator);	    	
	    	numerator = numerator.divide(gcd);
	    	denominator = denominator.divide(gcd);
	    }
		
		@Override
		public String toString() {
			return numerator + " / " + denominator;
		}
		
		private Rational add(Rational aRational) {
			BigInteger numer = numerator.multiply(aRational.denominator)
                .add(aRational.numerator.multiply(denominator));
			BigInteger denom = aRational.denominator.multiply(denominator);
			
			return new Rational(numer, denom);
		}	
		
		private BigInteger numerator;
		private BigInteger denominator;
		
		private static final Rational ZERO = new Rational(BigInteger.ZERO, BigInteger.ONE);
		
	}

}

```

## Python Code
### python_code_1.txt
```python
from  fractions import Fraction

def harmonic_series():
    n, h = Fraction(1), Fraction(1)
    while True:
        yield h
        h += 1 / (n + 1)
        n += 1

if __name__ == '__main__':
    from itertools import islice
    for n, d in (h.as_integer_ratio() for h in islice(harmonic_series(), 20)):
        print(n, '/', d)

```

### python_code_2.txt
```python
'''Harmonic series'''

from fractions import Fraction
from itertools import accumulate, count, islice
from operator import add


# harmonic :: [Fraction]
def harmonic():
    '''Non finite stream of the terms
       of the Harmonic series.
    '''
    return accumulate(
        (1 / Fraction(x) for x in count(1)),
        add
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tests of the harmonic series function'''

    print('First 20 terms of the harmonic series:')
    print('\n'.join([
        showFraction(nd) for nd in islice(harmonic(), 20)
    ]))

    print('\n100th term:')
    print(
        showFraction(
            next(islice(harmonic(), 99, None))
        )
    )

    print('')
    print(
        'One-based indices of terms above threshold values:'
    )
    indexedHarmonic = enumerate(harmonic())
    print('\n'.join([
        next(
            showFirstLimit(n)(x) for x
            in indexedHarmonic if n < x[1]
        ) for n in range(1, 1 + 10)
    ]))


# ------------------ DISPLAY FORMATTING ------------------

# showFraction :: Fraction -> String
def showFraction(nd):
    '''String representation of the fraction nd.
    '''
    n, d = nd.as_integer_ratio()

    return f'{n} / {d}'


# showFirstLimit :: Int -> (Int, Fraction) -> String
def showFirstLimit(n):
    '''Report of 1-based index of first term
       with a value over n
    '''
    def go(indexedFraction):
        i = indexedFraction[0]

        return f'Term {1 + i} is the first above {n}'

    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

