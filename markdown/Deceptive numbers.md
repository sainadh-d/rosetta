# Deceptive numbers

## Task Link
[Rosetta Code - Deceptive numbers](https://rosettacode.org/wiki/Deceptive_numbers)

## Java Code
### java_code_1.txt
```java
public final class DeceptiveNumbers {

	public static void main(String[] aArgs) {
		int n = 7;
		int count = 0;
		while ( count < 100 ) {
			if ( isDeceptive(n) ) {
				System.out.print(String.format("%6d%s", n, ( ++count % 10 == 0 ? "\n" : " " )));
			}
			n += 1;
		}
	}
	
	private static boolean isDeceptive(int aN) {
		if ( aN % 2 != 0 && aN % 3 != 0 && aN % 5 != 0 && modulusPower(10, aN - 1, aN) == 1 ) {
			for ( int divisor = 7; divisor < Math.sqrt(aN); divisor += 6 ) {
				if ( aN % divisor == 0 || aN % ( divisor + 4 ) == 0 ) {
					return true;
				}
			}
		}
		return false;
	}
	
	private static long modulusPower(long aBase, long aExponent, long aModulus) {
	    if ( aModulus == 1 ) {
	        return 0;
	    }	    
	    
	    aBase %= aModulus;
	    long result = 1;
	    while ( aExponent > 0 ) {
	        if ( ( aExponent  & 1 ) == 1 ) {
	            result = ( result * aBase ) % aModulus;
	        }
	        aBase = ( aBase * aBase ) % aModulus;
	        aExponent >>= 1;
	    }
	    return result;
	}
	
}

```

## Python Code
### python_code_1.txt
```python
from itertools import count, islice
from math import isqrt

def is_deceptive(n):
    if n & 1 and n % 3 and n % 5 and pow(10, n - 1, n) == 1:
        for d in range(7, isqrt(n) + 1, 6):
            if not (n % d and n % (d + 4)): return True
    return False

print(*islice(filter(is_deceptive, count()), 100))

```

