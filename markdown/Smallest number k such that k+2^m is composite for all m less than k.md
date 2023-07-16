# Smallest number k such that k+2^m is composite for all m less than k

## Task Link
[Rosetta Code - Smallest number k such that k+2^m is composite for all m less than k](https://rosettacode.org/wiki/Smallest_number_k_such_that_k%2B2%5Em_is_composite_for_all_m_less_than_k)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public final class SmallestNumberK {

	public static void main(String[] aArgs) {
		int count = 0;
		int k = 3;
		while ( count < 5 ) {
		    if ( isA033919(k) ) {
		    	System.out.print(k + " ");
		    	count += 1;
		    }		    
		    k += 2;
		}
		System.out.println();
	}
	
	private static boolean isA033919(int aK) {
		final BigInteger bigK = BigInteger.valueOf(aK);
		for ( int m = 1; m < aK; m++ ) {
		    if ( bigK.add(BigInteger.ONE.shiftLeft(m)).isProbablePrime(20) ) {
		      return false;
		    }
		}
		return true;
	}

}

```

## Python Code
