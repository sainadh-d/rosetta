# Sequence: nth number with exactly n divisors

## Task Link
[Rosetta Code - Sequence: nth number with exactly n divisors](https://rosettacode.org/wiki/Sequence:_nth_number_with_exactly_n_divisors)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class SequenceNthNumberWithExactlyNDivisors {

    public static void main(String[] args) {
        int max = 45;
        smallPrimes(max);
        for ( int n = 1; n <= max ; n++ ) {
            System.out.printf("A073916(%d) = %s%n", n, OEISA073916(n));
        }
    }
    
    private static List<Integer> smallPrimes = new ArrayList<>();
    
    private static void smallPrimes(int numPrimes) {
        smallPrimes.add(2);
        for ( int n = 3, count = 0 ; count < numPrimes ; n += 2 ) {
            if ( isPrime(n) ) {
                smallPrimes.add(n);
                count++;
            }
        }
    }
    
    private static final boolean isPrime(long test) {
        if ( test == 2 ) {
            return true;
        }
        if ( test % 2 == 0 ) {
            return false;
        }
        for ( long d = 3 ; d*d <= test ; d += 2 ) {
            if ( test % d == 0 ) {
                return false;
            }
        }
        return true;
    }

    private static int getDivisorCount(long n) {
        int count = 1;
        while ( n % 2 == 0 ) {
            n /= 2;
            count += 1;
        }
        for ( long d = 3 ; d*d <= n ; d += 2 ) {
            long q = n / d;
            long r = n % d;
            int dc = 0;
            while ( r == 0 ) {
                dc += count;
                n = q;
                q = n / d;
                r = n % d;
            }
            count += dc;
        }
        if ( n != 1 ) {
            count *= 2;
        }
        return count;
    }
    
    private static BigInteger OEISA073916(int n) {
        if ( isPrime(n) ) {
            return BigInteger.valueOf(smallPrimes.get(n-1)).pow(n - 1);
        }
        int count = 0;
        int result = 0;
        for ( int i = 1 ; count < n ; i++ ) {
            if ( n % 2 == 1 ) {
                //  The solution for an odd (non-prime) term is always a square number
                int sqrt = (int) Math.sqrt(i);
                if ( sqrt*sqrt != i ) {
                    continue;
                }
            }
            if ( getDivisorCount(i) == n ) {
                count++;
                result = i;
            }
        }
        return BigInteger.valueOf(result);
    }

}

```

## Python Code
### python_code_1.txt
```python
def divisors(n):
    divs = [1]
    for ii in range(2, int(n ** 0.5) + 3):
        if n % ii == 0:
            divs.append(ii)
            divs.append(int(n / ii))
    divs.append(n)
    return list(set(divs))


def is_prime(n):
    return len(divisors(n)) == 2


def primes():
    ii = 1
    while True:
        ii += 1
        if is_prime(ii):
            yield ii


def prime(n):
    generator = primes()
    for ii in range(n - 1):
        generator.__next__()
    return generator.__next__()


def n_divisors(n):
    ii = 0
    while True:
        ii += 1
        if len(divisors(ii)) == n:
            yield ii


def sequence(max_n=None):
    if max_n is not None:
        for ii in range(1, max_n + 1):
            if is_prime(ii):
                yield prime(ii) ** (ii - 1)
            else:
                generator = n_divisors(ii)
                for jj, out in zip(range(ii - 1), generator):
                    pass
                yield generator.__next__()
    else:
        ii = 1
        while True:
            ii += 1
            if is_prime(ii):
                yield prime(ii) ** (ii - 1)
            else:
                generator = n_divisors(ii)
                for jj, out in zip(range(ii - 1), generator):
                    pass
                yield generator.__next__()


if __name__ == '__main__':
    for item in sequence(15):
        print(item)

```

### python_code_2.txt
```python
1
3
25
14
14641
44
24137569
70
1089
405
819628286980801
160
22563490300366186081
2752
9801

```

