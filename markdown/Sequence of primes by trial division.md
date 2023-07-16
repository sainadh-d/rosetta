# Sequence of primes by trial division

## Task Link
[Rosetta Code - Sequence of primes by trial division](https://rosettacode.org/wiki/Sequence_of_primes_by_trial_division)

## Java Code
### java_code_1.txt
```java
import java.util.stream.IntStream;

public class Test {

    static IntStream getPrimes(int start, int end) {
        return IntStream.rangeClosed(start, end).filter(n -> isPrime(n));
    }

    public static boolean isPrime(long x) {
        if (x < 3 || x % 2 == 0)
            return x == 2;

        long max = (long) Math.sqrt(x);
        for (long n = 3; n <= max; n += 2) {
            if (x % n == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        getPrimes(0, 100).forEach(p -> System.out.printf("%d, ", p));
    }
}

```

## Python Code
### python_code_1.txt
```python
def prime(a):
    return not (a < 2 or any(a % x == 0 for x in xrange(2, int(a**0.5) + 1)))

def primes_below(n):
    return [i for i in range(n) if prime(i)]

```

### python_code_2.txt
```python
limiter = 100
primelist = []
def primer(n):
	for d in primelist:
		if d * d > n:
			break
		if n % d == 0:
			return
	primelist.append(n)

for vv in range(2, limiter):
	primer(vv)

print(len(primelist))
print(*primelist)

```

