# Jacobsthal numbers

## Task Link
[Rosetta Code - Jacobsthal numbers](https://rosettacode.org/wiki/Jacobsthal_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public final class JacobsthalNumbers {

	public static void main(String[] aArgs) {
		System.out.println("The first 30 Jacobsthal Numbers:");
		for ( int i = 0; i < 6; i++ ) {
			for ( int k = 0; k < 5; k++ ) {
				System.out.print(String.format("%15s", jacobsthalNumber(i * 5 + k)));
			}
			System.out.println();
		}
		System.out.println();
		
		System.out.println("The first 30 Jacobsthal-Lucas Numbers:");
		for ( int i = 0; i < 6; i++ ) {
			for ( int k = 0; k < 5; k++ ) {
				System.out.print(String.format("%15s", jacobsthalLucasNumber(i * 5 + k)));
			}
			System.out.println();
		}
		System.out.println();		
		
		System.out.println("The first 20 Jacobsthal oblong Numbers:");
		for ( int i = 0; i < 4; i++ ) {
			for ( int k = 0; k < 5; k++ ) {
				System.out.print(String.format("%15s", jacobsthalOblongNumber(i * 5 + k)));
			}
			System.out.println();
		}
		System.out.println();		
		
		System.out.println("The first 10 Jacobsthal Primes:");
		for ( int i = 0; i < 10; i++ ) {
			System.out.println(jacobsthalPrimeNumber(i));
		}
	}
	
	private static BigInteger jacobsthalNumber(int aIndex) {
		BigInteger value = BigInteger.valueOf(parityValue(aIndex));
		return BigInteger.ONE.shiftLeft(aIndex).subtract(value).divide(THREE);
	}
	
	private static long jacobsthalLucasNumber(int aIndex) {
		return ( 1 << aIndex ) + parityValue(aIndex);
	}
	
	private static long jacobsthalOblongNumber(int aIndex) {
		long nextJacobsthal =  jacobsthalNumber(aIndex + 1).longValueExact();
		long result = currentJacobsthal * nextJacobsthal;
		currentJacobsthal = nextJacobsthal;		
		return result;
	}
	
	private static long jacobsthalPrimeNumber(int aIndex) {
		BigInteger candidate = jacobsthalNumber(latestIndex++);
		while ( ! candidate.isProbablePrime(CERTAINTY) ) {
			candidate = jacobsthalNumber(latestIndex++);
		}		
		return candidate.longValueExact();		
	}
	
	private static int parityValue(int aIndex) {
		return ( aIndex & 1 ) == 0 ? +1 : -1;
	}
	
	private static long currentJacobsthal = 0;
	private static int latestIndex = 0;
	
	private static final BigInteger THREE = BigInteger.valueOf(3);
	private static final int CERTAINTY = 20;
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python
from math import floor, pow

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False        
    return True

def odd(n):
    return n and 1 != 0
    
def jacobsthal(n):
    return floor((pow(2,n)+odd(n))/3)

def jacobsthal_lucas(n):
    return int(pow(2,n)+pow(-1,n))

def jacobsthal_oblong(n):
    return jacobsthal(n)*jacobsthal(n+1)


if __name__ == '__main__':
    print("First 30 Jacobsthal numbers:")
    for j in range(0, 30):
        print(jacobsthal(j), end="  ")

    print("\n\nFirst 30 Jacobsthal-Lucas numbers: ")
    for j in range(0, 30):
        print(jacobsthal_lucas(j), end = '\t')

    print("\n\nFirst 20 Jacobsthal oblong numbers: ")
    for j in range(0, 20):
        print(jacobsthal_oblong(j), end="  ")

    print("\n\nFirst 10 Jacobsthal primes: ")
    for j in range(3, 33):
        if isPrime(jacobsthal(j)):
            print(jacobsthal(j))

```

### python_code_2.txt
```python
'''Jacobsthal numbers'''

from itertools import islice
from operator import mul


# jacobsthal :: [Integer]
def jacobsthal():
    '''Infinite sequence of terms of OEIS A001045
    '''
    return jacobsthalish(0, 1)


# jacobsthalish :: (Int, Int) -> [Int]
def jacobsthalish(*xy):
    '''Infinite sequence of jacobsthal-type series
       beginning with a, b
    '''
    def go(ab):
        a, b = ab
        return a, (b, 2 * a + b)

    return unfoldr(go)(xy)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 15 terms each n-step Fibonacci(n) series
       where n is drawn from [2..8]
    '''
    print('\n\n'.join([
        fShow(*x) for x in [
            (
                'terms of the Jacobsthal sequence',
                30, jacobsthal()),
            (
                'Jacobsthal-Lucas numbers',
                30, jacobsthalish(2, 1)
            ),
            (
                'Jacobsthal oblong numbers',
                20, map(
                    mul, jacobsthal(),
                    drop(1)(jacobsthal())
                )
            ),
            (
                'primes in the Jacobsthal sequence',
                10, filter(isPrime, jacobsthal())
            )
        ]
    ]))


# fShow :: (String, Int, [Integer]) -> String
def fShow(k, n, xs):
    '''N tabulated terms of XS, prefixed by the label K
    '''
    return f'{n} {k}:\n' + spacedTable(
        list(chunksOf(5)(
            [str(t) for t in take(n)(xs)]
        ))
    )


# ----------------------- GENERIC ------------------------

# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return go


# isPrime :: Int -> Bool
def isPrime(n):
    '''True if n is prime.'''
    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    def p(x):
        return 0 == n % x or 0 == n % (2 + x)

    return not any(map(p, range(5, 1 + int(n ** 0.5), 6)))


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Generic anamorphism.
       A lazy (generator) list unfolded from a seed value by
       repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None, or just (value, residue).
       For a strict output value, wrap in list().
    '''
    def go(x):
        valueResidue = f(x)
        while None is not valueResidue:
            yield valueResidue[0]
            valueResidue = f(valueResidue[1])
    return go


# ---------------------- FORMATTING ----------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divisible, the final list will be shorter than n.
    '''
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


# spacedTable :: [[String]] -> String
def spacedTable(rows):
    '''Tabulated stringification of rows'''
    columnWidths = [
        max([len(x) for x in col])
        for col in zip(*rows)
    ]
    return '\n'.join([
        ' '.join(
            map(
                lambda x, w: x.rjust(w, ' '),
                row, columnWidths
            )
        )
        for row in rows
    ])


# MAIN ---
if __name__ == '__main__':
    main()

```

