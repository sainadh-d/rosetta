# Evaluate binomial coefficients

## Task Link
[Rosetta Code - Evaluate binomial coefficients](https://rosettacode.org/wiki/Evaluate_binomial_coefficients)

## Java Code
### java_code_1.txt
```java
public class Binomial {

    // precise, but may overflow and then produce completely incorrect results
    private static long binomialInt(int n, int k) {
        if (k > n - k)
            k = n - k;

        long binom = 1;
        for (int i = 1; i <= k; i++)
            binom = binom * (n + 1 - i) / i;
        return binom;
    }

    // same as above, but with overflow check
    private static Object binomialIntReliable(int n, int k) {
        if (k > n - k)
            k = n - k;

        long binom = 1;
        for (int i = 1; i <= k; i++) {
            try {
                binom = Math.multiplyExact(binom, n + 1 - i) / i;
            } catch (ArithmeticException e) {
                return "overflow";
            }
        }
        return binom;
    }

    // using floating point arithmetic, larger numbers can be calculated,
    // but with reduced precision
    private static double binomialFloat(int n, int k) {
        if (k > n - k)
            k = n - k;

        double binom = 1.0;
        for (int i = 1; i <= k; i++)
            binom = binom * (n + 1 - i) / i;
        return binom;
    }

    // slow, hard to read, but precise
    private static BigInteger binomialBigInt(int n, int k) {
        if (k > n - k)
            k = n - k;

        BigInteger binom = BigInteger.ONE;
        for (int i = 1; i <= k; i++) {
            binom = binom.multiply(BigInteger.valueOf(n + 1 - i));
            binom = binom.divide(BigInteger.valueOf(i));
        }
        return binom;
    }

    private static void demo(int n, int k) {
        List<Object> data = Arrays.asList(
                n,
                k,
                binomialInt(n, k),
                binomialIntReliable(n, k),
                binomialFloat(n, k),
                binomialBigInt(n, k));

        System.out.println(data.stream().map(Object::toString).collect(Collectors.joining("\t")));
    }

    public static void main(String[] args) {
        demo(5, 3);
        demo(1000, 300);
    }
}

```

### java_code_2.txt
```java
public class Binomial
{
    private static long binom(int n, int k)
    {
        if (k==0)
            return 1;
        else if (k>n-k)
            return binom(n, n-k);
        else
            return binom(n-1, k-1)*n/k;
    }

    public static void main(String[] args)
    {
        System.out.println(binom(5, 3));
    }
}

```

## Python Code
### python_code_1.txt
```python
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

if __name__ == "__main__":
    print(binomialCoeff(5, 3))

```

### python_code_2.txt
```python
from operator import mul
from functools import reduce


def comb(n,r):
    ''' calculate nCr - the binomial coefficient
    >>> comb(3,2)
    3
    >>> comb(9,4)
    126
    >>> comb(9,6)
    84
    >>> comb(20,14)
    38760
    '''
 
    if r > n-r:
        # r = n-r   for smaller intermediate values during computation
        return ( reduce( mul, range((n - (n-r) + 1), n + 1), 1)
                 // reduce( mul, range(1, (n-r) + 1), 1) )
    else:
        return ( reduce( mul, range((n - r + 1), n + 1), 1)
                 // reduce( mul, range(1, r + 1), 1) )

```

### python_code_3.txt
```python
'''Evaluation of binomial coefficients'''

from functools import reduce


# binomialCoefficient :: Int -> Int -> Int
def binomialCoefficient(n):
    '''n choose k, expressed in terms of
       product and factorial functions.
    '''
    return lambda k: product(
        enumFromTo(1 + k)(n)
    ) // factorial(n - k)


# TEST ----------------------------------------------------
# main :: IO()
def main():
    '''Tests'''

    print(
        binomialCoefficient(5)(3)
    )

    # k=0 to k=5, where n=5
    print(
        list(map(
            binomialCoefficient(5),
            enumFromTo(0)(5)
        ))
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# factorial :: Int -> Int
def factorial(x):
    '''The factorial of x, where
       x is a positive integer.
    '''
    return product(enumFromTo(1)(x))


# product :: [Num] -> Num
def product(xs):
    '''The product of a list of
       numeric values.
    '''
    return reduce(lambda a, b: a * b, xs, 1)


# TESTS ---------------------------------------------------
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
from typing import (Callable, List, Any)
from functools import reduce
from operator import mul


def binomialCoefficient(n: int) -> Callable[[int], int]:
    return lambda k: product(enumFromTo(1 + k)(n)) // factorial(n - k)


def enumFromTo(m: int) -> Callable[[int], List[Any]]:
    return lambda n: list(range(m, 1 + n))


def factorial(x: int) -> int:
    return product(enumFromTo(1)(x))


def product(xs: List[Any]) -> int:
    return reduce(mul, xs, 1)


if __name__ == '__main__':
    print(binomialCoefficient(5)(3))
    # k=0 to k=5, where n=5
    print(list(map(binomialCoefficient(5), enumFromTo(0)(5))))

```

