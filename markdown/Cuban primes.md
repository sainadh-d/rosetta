# Cuban primes

## Task Link
[Rosetta Code - Cuban primes](https://rosettacode.org/wiki/Cuban_primes)

## Java Code
### java_code_1.txt
```java
public class CubanPrimes {

    private static int MAX = 1_400_000;
    private static boolean[] primes = new boolean[MAX];
    
    public static void main(String[] args) {
        preCompute();
        cubanPrime(200, true);
        for ( int i = 1 ; i <= 5 ; i++ ) {
            int max = (int) Math.pow(10, i);
            System.out.printf("%,d-th cuban prime = %,d%n", max, cubanPrime(max, false));
        }
    }
    
    private static long cubanPrime(int n, boolean display) {
        int count = 0;
        long result = 0;
        for ( long i = 0 ; count < n ; i++ ) {
            long test = 1l + 3 * i * (i+1);
            if ( isPrime(test) ) {
                count++;
                result = test;
                if ( display ) {
                    System.out.printf("%10s%s", String.format("%,d", test), count % 10 == 0 ? "\n" : "");
                }
            }
        }
        return result;
    }
    
    private static boolean isPrime(long n) {
        if ( n < MAX ) {
            return primes[(int)n];
        }
        int max = (int) Math.sqrt(n);
        for ( int i = 3 ; i <= max ; i++ ) {
            if ( primes[i] && n % i == 0 ) {
                return false;
            }
        }
        return true;
    }

    private static final void preCompute() {
        //  primes
        for ( int i = 2 ; i < MAX ; i++ ) {
            primes[i] = true;            
        }
        for ( int i = 2 ; i < MAX ; i++ ) {
            if ( primes[i] ) {
                for ( int j = 2*i ; j < MAX ; j += i ) {
                    primes[j] = false;
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import datetime
import math

primes = [ 3, 5 ]

cutOff = 200

bigUn =  100_000
chunks = 50
little = bigUn / chunks

tn = " cuban prime"
print ("The first {:,}{}s:".format(cutOff, tn))

c = 0
showEach = True
u = 0
v = 1
st = datetime.datetime.now()

for i in range(1, int(math.pow(2,20))):
	found = False
	u += 6
	v += u
	mx = int(math.sqrt(v))
	
	for item in primes:
		if (item > mx):
			break
		if (v % item == 0):
			found = True
			break
	
	if (found == 0):
		c += 1
		if (showEach):
			z = primes[-1]
			while (z <= v - 2):
				z += 2
				
				fnd = False
				for item in primes:
					if (item > mx):
						break
					if (z % item == 0):
						fnd = True
						break
				
				if (not fnd):
					primes.append(z)
			
			primes.append(v)
			print("{:>11,}".format(v), end='')
			
			if (c % 10 == 0):
				print("");
			if (c == cutOff):
				showEach = False
				print ("Progress to the {:,}th {}:".format(bigUn, tn), end='')
		if (c % little == 0):
			print('.', end='')
		if (c == bigUn):
			break

print("");
print ("The {:,}th{} is {:,}".format(c, tn, v))
print("Computation time was {} seconds".format((datetime.datetime.now() - st).seconds))

```

