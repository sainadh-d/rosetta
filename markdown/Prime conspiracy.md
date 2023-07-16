# Prime conspiracy

## Task Link
[Rosetta Code - Prime conspiracy](https://rosettacode.org/wiki/Prime_conspiracy)

## Java Code
### java_code_1.txt
```java
public class PrimeConspiracy {

    public static void main(String[] args) {
        final int limit = 1000_000;
        final int sieveLimit = 15_500_000;

        int[][] buckets = new int[10][10];
        int prevDigit = 2;
        boolean[] notPrime = sieve(sieveLimit);

        for (int n = 3, primeCount = 1; primeCount < limit; n++) {
            if (notPrime[n])
                continue;

            int digit = n % 10;
            buckets[prevDigit][digit]++;
            prevDigit = digit;
            primeCount++;
        }

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (buckets[i][j] != 0) {
                    System.out.printf("%d -> %d : %2f%n", i,
                            j, buckets[i][j] / (limit / 100.0));
                }
            }
        }
    }

    public static boolean[] sieve(int limit) {
        boolean[] composite = new boolean[limit];
        composite[0] = composite[1] = true;

        int max = (int) Math.sqrt(limit);
        for (int n = 2; n <= max; n++) {
            if (!composite[n]) {
                for (int k = n * n; k < limit; k += n) {
                    composite[k] = true;
                }
            }
        }
        return composite;
    }
}

```

## Python Code
### python_code_1.txt
```python
def isPrime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    d = 5
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2

        if n % d == 0:
            return False
        d += 4
    return True

def generatePrimes():
    yield 2
    yield 3

    p = 5
    while p > 0:
        if isPrime(p):
            yield p
        p += 2
        if isPrime(p):
            yield p
        p += 4

g = generatePrimes()
transMap = {}
prev = None
limit = 1000000
for _ in xrange(limit):
    prime = next(g)
    if prev:
        transition = (prev, prime %10)
        if transition in transMap:
            transMap[transition] += 1
        else:
            transMap[transition] = 1
    prev = prime % 10

print "First {:,} primes. Transitions prime % 10 > next-prime % 10.".format(limit)
for trans in sorted(transMap):
    print "{0} -> {1} count {2:5} frequency: {3}%".format(trans[0], trans[1], transMap[trans], 100.0 * transMap[trans] / limit)

```

