# Smarandache prime-digital sequence

## Task Link
[Rosetta Code - Smarandache prime-digital sequence](https://rosettacode.org/wiki/Smarandache_prime-digital_sequence)

## Java Code
### java_code_1.txt
```java
public class SmarandachePrimeDigitalSequence {

    public static void main(String[] args) {
        long s = getNextSmarandache(7);
        System.out.printf("First 25 Smarandache prime-digital sequence numbers:%n2 3 5 7 ");
        for ( int count = 1 ; count <= 21 ; s = getNextSmarandache(s) ) {
            if ( isPrime(s) ) {
                System.out.printf("%d ", s);
                count++;
            }
        }
        System.out.printf("%n%n");
        for (int i = 2 ; i <=5 ; i++ ) {
            long n = (long) Math.pow(10, i);
            System.out.printf("%,dth Smarandache prime-digital sequence number = %d%n", n, getSmarandachePrime(n));
        }
    }
    
    private static final long getSmarandachePrime(long n) {
        if ( n < 10 ) {
            switch ((int) n) {
            case 1:  return 2;
            case 2:  return 3;
            case 3:  return 5;
            case 4:  return 7;
            }
        }
        long s = getNextSmarandache(7);
        long result = 0;
        for ( int count = 1 ; count <= n-4 ; s = getNextSmarandache(s) ) {
            if ( isPrime(s) ) {
                count++;
                result = s;
            }
        }
        return result;
    }
    
    private static final boolean isPrime(long test) {
        if ( test % 2 == 0 ) return false;
        for ( long i = 3 ; i <= Math.sqrt(test) ; i += 2 ) {
            if ( test % i == 0 ) {
                return false;
            }
        }
        return true;
    }

    private static long getNextSmarandache(long n) {
        //  If 3, next is 7
        if ( n % 10 == 3 ) {
            return n+4;
        }
        long retVal = n-4;
        
        //  Last digit 7.  k = largest position from right where we have a 7. 
        int k = 0;
        while ( n % 10 == 7 ) {
            k++;
            n /= 10;
        }
        
        //  Determine first digit from right where digit != 7.
        long digit = n % 10;

        //  Digit is 2, 3, or 5.  3-2 = 1, 5-3 = 2, 7-5 = 2, so digit = 2, coefficient = 1, otherwise 2.
        long coeff = (digit == 2 ? 1 : 2);
        
        //  Compute next value
        retVal += coeff * Math.pow(10, k);
        
        //  Subtract values for digit = 7.
        while ( k > 1 ) {
            retVal -= 5 * Math.pow(10, k-1);
            k--;
        }
        
        //  Even works for 777..777 --> 2222...223
        return retVal;
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


def digit_check(n):
    if len(str(n))<2:
        return True
    else:
        for digit in str(n):
            if not is_prime(int(digit)):
                return False
        return True


def sequence(max_n=None):
    ii = 0
    n = 0
    while True:
        ii += 1
        if is_prime(ii):
            if max_n is not None:
                if n>max_n:
                    break
            if digit_check(ii):
                n += 1
                yield ii


if __name__ == '__main__':
    generator = sequence(100)
    for index, item in zip(range(1, 16), generator):
        print(index, item)
    for index, item in zip(range(16, 100), generator):
        pass
    print(100, generator.__next__())

```

### python_code_2.txt
```python
1 2
2 3
3 5
4 7
5 23
6 37
7 53
8 73
9 223
10 227
11 233
12 257
13 277
14 337
15 353
100 33223

```

