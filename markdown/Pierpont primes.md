# Pierpont primes

## Task Link
[Rosetta Code - Pierpont primes](https://rosettacode.org/wiki/Pierpont_primes)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.List;

public class PierpontPrimes {

    public static void main(String[] args) {
        NumberFormat nf = NumberFormat.getNumberInstance();
        display("First 50 Pierpont primes of the first kind:", pierpontPrimes(50, true));
        display("First 50 Pierpont primes of the second kind:", pierpontPrimes(50, false));
        System.out.printf("250th Pierpont prime of the first kind:     %s%n%n", nf.format(pierpontPrimes(250, true).get(249)));
        System.out.printf("250th Pierpont prime of the second kind: %s%n%n", nf.format(pierpontPrimes(250, false).get(249)));
    }
    
    private static void display(String message, List<BigInteger> primes) {
        NumberFormat nf = NumberFormat.getNumberInstance();
        System.out.printf("%s%n", message);
        for ( int i = 1 ; i <= primes.size() ; i++ ) {
            System.out.printf("%10s  ", nf.format(primes.get(i-1)));
            if ( i % 10 == 0 ) {
                System.out.printf("%n");
            }
        }
        System.out.printf("%n");
    }

    public static List<BigInteger> pierpontPrimes(int n, boolean first) {
        List<BigInteger> primes = new ArrayList<BigInteger>();
        if ( first ) {
            primes.add(BigInteger.valueOf(2));
            n -= 1;
        }

        BigInteger two = BigInteger.valueOf(2);
        BigInteger twoTest = two;
        BigInteger three = BigInteger.valueOf(3);
        BigInteger threeTest = three;
        int twoIndex = 0, threeIndex = 0;
        List<BigInteger> twoSmooth = new ArrayList<BigInteger>();

        BigInteger one = BigInteger.ONE;
        BigInteger mOne = BigInteger.valueOf(-1);
        int count = 0;
        while ( count < n ) {
            BigInteger min = twoTest.min(threeTest);
            twoSmooth.add(min);
            if ( min.compareTo(twoTest) == 0 ) {
                twoTest = two.multiply(twoSmooth.get(twoIndex));
                twoIndex++;
            }
            if ( min.compareTo(threeTest) == 0 ) {
                threeTest = three.multiply(twoSmooth.get(threeIndex));
                threeIndex++;
            }
            BigInteger test = min.add(first ? one : mOne);
            if ( test.isProbablePrime(10) ) {
                primes.add(test);
                count++;
            }
        }
        return primes;
    }
    
}

```

## Python Code
### python_code_1.txt
```python
import random

# Copied from https://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
def is_Prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False

    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  

    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True

def pierpont(ulim, vlim, first):
    p = 0
    p2 = 1
    p3 = 1
    pp = []
    for v in xrange(vlim):
        for u in xrange(ulim):
            p = p2 * p3
            if first:
                p = p + 1
            else:
                p = p - 1
            if is_Prime(p):
                pp.append(p)
            p2 = p2 * 2
        p3 = p3 * 3
        p2 = 1
    pp.sort()
    return pp

def main():
    print "First 50 Pierpont primes of the first kind:"
    pp = pierpont(120, 80, True)
    for i in xrange(50):
        print "%8d " % pp[i],
        if (i - 9) % 10 == 0:
            print
    print "First 50 Pierpont primes of the second kind:"
    pp2 = pierpont(120, 80, False)
    for i in xrange(50):
        print "%8d " % pp2[i],
        if (i - 9) % 10 == 0:
            print
    print "250th Pierpont prime of the first kind:", pp[249]
    print "250th Pierpont prime of the second kind:", pp2[249]

main()

```

