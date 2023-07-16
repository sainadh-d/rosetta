# Sum multiples of 3 and 5

## Task Link
[Rosetta Code - Sum multiples of 3 and 5](https://rosettacode.org/wiki/Sum_multiples_of_3_and_5)

## Java Code
### java_code_1.txt
```java
class SumMultiples {
	public static long getSum(long n) {
		long sum = 0;
		for (int i = 3; i < n; i++) {
			if (i % 3 == 0 || i % 5 == 0) sum += i;
		}
		return sum;
	}
	public static void main(String[] args) {
		System.out.println(getSum(1000));
	}
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

public class SumMultiples {

    public static void main(String[] args) {
        BigInteger m1 = BigInteger.valueOf(3);
        BigInteger m2 = BigInteger.valueOf(5);
        for ( int i = 1 ; i <= 25 ; i++ ) {
            BigInteger limit = BigInteger.valueOf(10).pow(i);
            System.out.printf("Limit = 10^%d, answer = %s%n", i, sumMultiples(limit.subtract(BigInteger.ONE), m1, m2));
        }
    }

    //  Use Inclusion - Exclusion
    private static BigInteger sumMultiples(BigInteger max, BigInteger n1, BigInteger n2) {
        return sumMultiple(max, n1).add(sumMultiple(max, n2)).subtract(sumMultiple(max, n1.multiply(n2)));
    }
    
    private static BigInteger sumMultiple(BigInteger max, BigInteger m) {
        BigInteger maxDivM = max.divide(m);
        return m.multiply(maxDivM.multiply(maxDivM.add(BigInteger.ONE))).divide(BigInteger.valueOf(2));
    }
    
    //  Used for testing
    @SuppressWarnings("unused")
    private static long sumMultiples(long max, long n1, long n2) {
        return sumMultiple(max, n1) + sumMultiple(max, n2) - sumMultiple(max, n1 * n2);
    }
    
    private static long sumMultiple(long max, long n) {
        long sum = 0;
        for ( int i = 1 ; i <= max ; i++ ) {
            if ( i % n == 0 ) {
                sum += i;
            }
        }
        return sum;
    }

}

```

## Python Code
### python_code_1.txt
```python
def sum35a(n):
    'Direct count'
    # note: ranges go to n-1
    return sum(x for x in range(n) if x%3==0 or x%5==0)

def sum35b(n): 
    "Count all the 3's; all the 5's; minus double-counted 3*5's"
    # note: ranges go to n-1
    return sum(range(3, n, 3)) + sum(range(5, n, 5)) - sum(range(15, n, 15))
    
def sum35c(n):
    'Sum the arithmetic progressions: sum3 + sum5 - sum15'
    consts = (3, 5, 15)
    # Note: stop at n-1
    divs = [(n-1) // c for c in consts]
    sums = [d*c*(1+d)/2 for d,c in zip(divs, consts)]
    return sums[0] + sums[1] - sums[2]

#test
for n in range(1001):
    sa, sb, sc = sum35a(n), sum35b(n), sum35c(n)
    assert sa == sb == sc  # python tests aren't like those of c.

print('For n = %7i -> %i\n' % (n, sc))

# Pretty patterns
for p in range(7):
    print('For n = %7i -> %i' % (10**p, sum35c(10**p)))

# Scalability 
p = 20
print('\nFor n = %20i -> %i' % (10**p, sum35c(10**p)))

```

### python_code_2.txt
```python
'''Summed multiples of 3 and 5 up to n'''


# sum35 :: Int -> Int
def sum35(n):
    '''Sum of all positive multiples
       of 3 or 5 below n.
    '''
    f = sumMults(n)
    return f(3) + f(5) - f(15)


# sumMults :: Int -> Int -> Int
def sumMults(n):
    '''Area under a straight line between
       the first multiple and the last.
    '''
    def go(n, m):
        n1 = (n - 1) // m
        return (m * n1 * (n1 + 1)) // 2
    return lambda x: go(n, x)


# TEST ----------------------------------------------------
def main():
    '''Tests for [10^1 .. 10^5], and [10^8 .. 10^25]
    '''
    print(
        fTable(__doc__ + ':\n')(lambda x: '10E' + str(x))(
            str
        )(compose(sum35)(lambda x: 10**x))(
            enumFromTo(1)(5) + enumFromTo(18)(25)
        )
    )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# fTable :: String -> (a -> String) ->
#                     (b -> String) ->
#        (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

