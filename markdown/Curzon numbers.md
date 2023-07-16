# Curzon numbers

## Task Link
[Rosetta Code - Curzon numbers](https://rosettacode.org/wiki/Curzon_numbers)

## Java Code
### java_code_1.txt
```java
public final class CurzonNumbers {

	public static void main(String[] aArgs) {
		for ( int k = 2; k <= 10; k += 2 ) {
	        System.out.println("Generalised Curzon numbers with base " + k + ":");
	        int n = 1;
	        int count = 0;
	        while ( count < 50 ) {
	            if ( isGeneralisedCurzonNumber(k, n) ) {
	                System.out.print(String.format("%4d%s", n, ( ++count % 10 == 0 ? "\n" : " " )));
	            }
	            n += 1;
	        }
	        
	        while ( count < 1_000 ) {
	        	if ( isGeneralisedCurzonNumber(k, n) ) {
	        		count += 1;
	        	}
	        	n += 1;
	        }	 
	        System.out.println("1,000th Generalised Curzon number with base " + k + ": " + ( n - 1 ));
	        System.out.println();
	    }
	}
	
	private static boolean isGeneralisedCurzonNumber(int aK, int aN) {
	    final long r = aK * aN;
	    return modulusPower(aK, aN, r + 1) == r;
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
def is_Curzon(n, k):
    r = k * n
    return pow(k, n, r + 1) == r

for k in [2, 4, 6, 8, 10]:
    n, curzons = 1, []
    while len(curzons) < 1000:
        if is_Curzon(n, k):
            curzons.append(n)
        n += 1
    print(f'Curzon numbers with k = {k}:')
    for i, c in enumerate(curzons[:50]):
        print(f'{c: 5,}', end='\n' if (i + 1) % 25 == 0 else '')
    print(f'    Thousandth Curzon with k = {k}: {curzons[999]}.\n')

```

