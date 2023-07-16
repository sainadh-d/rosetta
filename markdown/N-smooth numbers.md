# N-smooth numbers

## Task Link
[Rosetta Code - N-smooth numbers](https://rosettacode.org/wiki/N-smooth_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class NSmoothNumbers {

    public static void main(String[] args) {
        System.out.printf("show the first 25 n-smooth numbers for n = 2 through n = 29%n");
        int max = 25;
        List<BigInteger> primes = new ArrayList<>();
        for ( int n = 2 ; n <= 29 ; n++ ) {
            if ( isPrime(n) ) {
                primes.add(BigInteger.valueOf(n));
                System.out.printf("The first %d %d-smooth numbers:%n", max, n);
                BigInteger[] humble = nSmooth(max, primes.toArray(new BigInteger[0]));
                for ( int i = 0 ; i < max ; i++ ) {
                    System.out.printf("%s ", humble[i]);
                }
                System.out.printf("%n%n");
            }
        }
        
        System.out.printf("show three numbers starting with 3,000 for n-smooth numbers for n = 3 through n = 29%n");
        int count = 3;
        max = 3000 + count - 1;
        primes = new ArrayList<>();
        primes.add(BigInteger.valueOf(2));
        for ( int n = 3 ; n <= 29 ; n++ ) {
            if ( isPrime(n) ) {
                primes.add(BigInteger.valueOf(n));
                System.out.printf("The %d through %d %d-smooth numbers:%n", max-count+1, max, n);
                BigInteger[] nSmooth = nSmooth(max, primes.toArray(new BigInteger[0]));
                for ( int i = max-count ; i < max ; i++ ) {
                    System.out.printf("%s ", nSmooth[i]);
                }
                System.out.printf("%n%n");
            }
        }
        
        System.out.printf("Show twenty numbers starting with 30,000 n-smooth numbers for n=503 through n=521%n");
        count = 20;
        max = 30000 + count - 1;
        primes = new ArrayList<>();
        for ( int n = 2 ; n <= 521 ; n++ ) {
            if ( isPrime(n) ) {
                primes.add(BigInteger.valueOf(n));
                if ( n >= 503 && n <= 521 ) {
                    System.out.printf("The %d through %d %d-smooth numbers:%n", max-count+1, max, n);
                    BigInteger[] nSmooth = nSmooth(max, primes.toArray(new BigInteger[0]));
                    for ( int i = max-count ; i < max ; i++ ) {
                        System.out.printf("%s ", nSmooth[i]);
                    }
                    System.out.printf("%n%n");
                }
            }
        }

    }

    private static final boolean isPrime(long test) {
        if ( test == 2 ) {
            return true;
        }
        if ( test % 2 == 0 ) return false;
        for ( long i = 3 ; i <= Math.sqrt(test) ; i += 2 ) {
            if ( test % i == 0 ) {
                return false;
            }
        }
        return true;
    }

    private static BigInteger[] nSmooth(int n, BigInteger[] primes) {
        int size = primes.length;
        BigInteger[] test = new BigInteger[size];
        for ( int i = 0 ; i < size ; i++ ) {
            test[i] = primes[i];
        }
        BigInteger[] results = new BigInteger[n];
        results[0] = BigInteger.ONE;
        
        int[] indexes = new int[size];
        for ( int i = 0 ; i < size ; i++ ) {
            indexes[i] = 0;
        }
        
        for ( int index = 1 ; index < n ; index++ ) {
            BigInteger min = test[0];
            for ( int i = 1 ; i < size ; i++ ) {
                min = min.min(test[i]);
            }
            results[index] = min;
            
            for ( int i = 0 ; i < size ; i++ ) {
                if ( results[index].compareTo(test[i]) == 0 ) {
                    indexes[i] = indexes[i] + 1;
                    test[i] = primes[i].multiply(results[indexes[i]]);
                }
            }
        }
        return results;
    }

}

```

## Python Code
### python_code_1.txt
```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def isPrime(n):
    if n < 2:
        return False

    for i in primes:
        if n == i:
            return True
        if n % i == 0:
            return False
        if i * i > n:
            return True
    print "Oops,", n, " is too large"

def init():
    s = 24
    while s < 600:
        if isPrime(s - 1) and s - 1 > primes[-1]:
            primes.append(s - 1)
        if isPrime(s + 1) and s + 1 > primes[-1]:
            primes.append(s + 1)
        s += 6

def nsmooth(n, size):
    if n < 2 or n > 521:
        raise Exception("n")
    if size < 1:
        raise Exception("n")

    bn = n
    ok = False
    for prime in primes:
        if bn == prime:
            ok = True
            break
    if not ok:
        raise Exception("must be a prime number: n")

    ns = [0] * size
    ns[0] = 1

    next = []
    for prime in primes:
        if prime > bn:
            break
        next.append(prime)

    indicies = [0] * len(next)
    for m in xrange(1, size):
        ns[m] = min(next)
        for i in xrange(0, len(indicies)):
            if ns[m] == next[i]:
                indicies[i] += 1
                next[i] = primes[i] * ns[indicies[i]]

    return ns

def main():
    init()

    for p in primes:
        if p >= 30:
            break
        print "The first", p, "-smooth numbers are:"
        print nsmooth(p, 25)
        print

    for p in primes[1:]:
        if p >= 30:
            break
        print "The 3000 to 3202", p, "-smooth numbers are:"
        print nsmooth(p, 3002)[2999:]
        print

    for p in [503, 509, 521]:
        print "The 30000 to 3019", p, "-smooth numbers are:"
        print nsmooth(p, 30019)[29999:]
        print

main()

```

