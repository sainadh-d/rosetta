# Ultra useful primes

## Task Link
[Rosetta Code - Ultra useful primes](https://rosettacode.org/wiki/Ultra_useful_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public final class UltraUsefulPrimes {

	public static void main(String[] args) {
		for ( int n = 1; n <= 10; n++ ) {
			showUltraUsefulPrime(n);
		}		
	}
	
	private static void showUltraUsefulPrime(int n) {
		BigInteger prime = BigInteger.ONE.shiftLeft(1 << n);
		BigInteger k = BigInteger.ONE; 
		while ( ! prime.subtract(k).isProbablePrime(20) ) {
			k = k.add(BigInteger.TWO);
		}
		
		System.out.print(k + " ");		   
	}

}

```

## Python Code
### python_code_1.txt
```python
# useful.py by xing216
from gmpy2 import is_prime
def useful(n):
    k = 1
    is_useful = False
    while is_useful == False:
        if is_prime(2**(2**n) - k):
            is_useful = True
            break
        k += 2
    return k
if __name__ == "__main__":
    print("n | k")
    for i in range(1,14):
        print(f"{i:<4}{useful(i)}")

```

