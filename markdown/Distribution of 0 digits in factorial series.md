# Distribution of 0 digits in factorial series

## Task Link
[Rosetta Code - Distribution of 0 digits in factorial series](https://rosettacode.org/wiki/Distribution_of_0_digits_in_factorial_series)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.List;

public final class DistributionInFactorials {

	public static void main(String[] aArgs) {
		List<Integer> limits = List.of( 100, 1_000, 10_000 );
		for ( Integer limit : limits ) {
			meanFactorialDigits(limit);
		}
	}
	
	private static void meanFactorialDigits(Integer aLimit) {
		BigInteger factorial = BigInteger.ONE;
		double proportionSum = 0.0;
		double proportionMean = 0.0;
		
		for ( int n = 1; n <= aLimit; n++ ) {
	        factorial = factorial.multiply(BigInteger.valueOf(n));
	        String factorialString = factorial.toString();
	        int digitCount = factorialString.length();	        
	        long zeroCount = factorialString.chars().filter( ch -> ch == '0' ).count();      
	        proportionSum += (double) zeroCount / digitCount;
	        proportionMean = proportionSum / n;	        
		}
		
		String result = String.format("%.8f", proportionMean);
		System.out.println("Mean proportion of zero digits in factorials from 1 to " + aLimit + " is " + result);
	}	

}

```

## Python Code
### python_code_1.txt
```python
def facpropzeros(N, verbose = True):
    proportions = [0.0] * N
    fac, psum = 1, 0.0
    for i in range(N):
        fac *= i + 1
        d = list(str(fac))
        psum += sum(map(lambda x: x == '0', d)) / len(d)
        proportions[i] = psum / (i + 1)

    if verbose:
        print("The mean proportion of 0 in factorials from 1 to {} is {}.".format(N, psum / N))

    return proportions


for n in [100, 1000, 10000]:
    facpropzeros(n)

props = facpropzeros(47500, False)
n = (next(i for i in reversed(range(len(props))) if props[i] > 0.16))

print("The mean proportion dips permanently below 0.16 at {}.".format(n + 2))

```

### python_code_2.txt
```python
import matplotlib.pyplot as plt
plt.plot([i+1 for i in range(len(props))], props)

```

### python_code_3.txt
```python
def zinit():
    zc = [0] * 999
    for x in range(1, 10):
        zc[x - 1] = 2        # 00x
        zc[10 * x - 1] = 2   # 0x0
        zc[100 * x - 1] = 2  # x00
        for y in range(10, 100, 10):
            zc[y + x - 1] = 1           # 0yx
            zc[10 * y + x - 1] = 1      # y0x
            zc[10 * (y + x) - 1] = 1    # yx0

    return zc

def meanfactorialdigits():
    zc = zinit()
    rfs = [1]
    total, trail, first = 0.0, 1, 0
    for f in range(2, 50000):
        carry, d999, zeroes = 0, 0, (trail - 1) * 3
        j, l = trail, len(rfs)
        while j <= l or carry != 0:
            if j <= l:
                carry = rfs[j-1] * f + carry

            d999 = carry % 1000
            if j <= l:
                rfs[j-1] = d999
            else:
                rfs.append(d999)

            zeroes += 3 if d999 == 0 else zc[d999-1]
            carry //= 1000
            j += 1

        while rfs[trail-1] == 0:
            trail += 1

        # d999 is a quick correction for length and zeros
        d999 = rfs[-1]
        d999 = 0 if d999 >= 100 else 2 if d999 < 10 else 1

        zeroes -= d999
        digits = len(rfs) * 3 - d999
        total += zeroes / digits
        ratio = total / f
        if f in [100, 1000, 10000]:
            print("The mean proportion of zero digits in factorials to {} is {}".format(f, ratio))
            
        if ratio >= 0.16:
            first = 0
        elif first == 0:
            first = f

    print("The mean proportion dips permanently below 0.16 at {}.".format(first))



import time
TIME0 = time.perf_counter()
meanfactorialdigits()
print("\nTotal time:", time.perf_counter() - TIME0, "seconds.")

```

