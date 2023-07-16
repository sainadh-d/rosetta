# Euler's constant 0.5772...

## Task Link
[Rosetta Code - Euler's constant 0.5772...](https://rosettacode.org/wiki/Euler%27s_constant_0.5772...)

## Java Code
### java_code_1.txt
```java
/**
 * Using a simple formula derived from Hurwitz zeta function,
 * as described on https://en.wikipedia.org/wiki/Euler%27s_constant,
 * gives a result accurate to 12 decimal places.
 */
public class EulerConstant {

	public static void main(String[] args) {		
		System.out.println(gamma(1_000_000));
	}

    private static double gamma(int N) {
		double gamma = 0.0;
		
		for ( int n = 1; n <= N; n++ ) {
			gamma += 1.0 / n;
		}
		
		gamma -= Math.log(N) + 1.0 / ( 2 * N );
		
		return gamma;
	}
	
}

```

## Python Code
### python_code_1.txt
```python
# /**************************************************
# Subject: Computation of Euler's constant 0.5772...
#          with Euler's Zeta Series.
# tested : Python 3.11 
# -------------------------------------------------*/

from scipy import special as s

def eulers_constant(n):
    k = 2
    euler = 0
    while k <= n:
        euler += (s.zeta(k) - 1)/k
        k += 1
    return 1 - euler

print(eulers_constant(47))

```

