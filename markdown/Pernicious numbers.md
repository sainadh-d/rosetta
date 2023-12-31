# Pernicious numbers

## Task Link
[Rosetta Code - Pernicious numbers](https://rosettacode.org/wiki/Pernicious_numbers)

## Java Code
### java_code_1.txt
```java
public class Pernicious{
    //very simple isPrime since x will be <= Long.SIZE
    public static boolean isPrime(int x){
        if(x < 2) return false;
        for(int i = 2; i < x; i++){
            if(x % i == 0) return false;
        }
        return true;
    }

    public static int popCount(long x){
        return Long.bitCount(x);
    }

    public static void main(String[] args){
        for(long i = 1, n = 0; n < 25; i++){
            if(isPrime(popCount(i))){
                System.out.print(i + " ");
                n++;
            }
        }
        
        System.out.println();
        
        for(long i = 888888877; i <= 888888888; i++){
            if(isPrime(popCount(i))) System.out.print(i + " ");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def popcount(n): return bin(n).count("1")

>>> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61}
>>> p, i = [], 0
>>> while len(p) < 25:
        if popcount(i) in primes: p.append(i)
        i += 1

        
>>> p
[3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31, 33, 34, 35, 36]
>>> p, i = [], 888888877
>>> while i <= 888888888:
        if popcount(i) in primes: p.append(i)
        i += 1

        
>>> p
[888888877, 888888878, 888888880, 888888883, 888888885, 888888886]
>>>

```

### python_code_2.txt
```python
'''Pernicious numbers'''

from itertools import count, islice


# isPernicious :: Int -> Bool
def isPernicious(n):
    '''True if the population count of n is
       a prime number.
    '''
    return isPrime(popCount(n))


# oeisA052294 :: [Int]
def oeisA052294():
    '''A non-finite stream of pernicious numbers.
       (Numbers with a prime population count)
    '''
    return (x for x in count(1) if isPernicious(x))


# popCount :: Int -> Int
def popCount(n):
    '''The count of non-zero digits in the binary
       representation of the positive integer n.
    '''
    def go(x):
        return divmod(x, 2) if 0 < x else None
    return sum(unfoldl(go)(n))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 25, and any in the range
       [888,888,877..888,888,888]
    '''

    print(
        take(25)(
            oeisA052294()
        )
    )
    print([
        x for x in enumFromTo(888888877)(888888888)
        if isPernicious(x)
    ])


# ----------------------- GENERIC ------------------------

# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    def go(n):
        return range(m, 1 + n)
    return go


# isPrime :: Int -> Bool
def isPrime(n):
    '''True if n is prime.'''
    if n in (2, 3):
        return True
    if 2 > n or 0 == n % 2:
        return False
    if 9 > n:
        return True
    if 0 == n % 3:
        return False

    return not any(map(
        lambda x: 0 == n % x or 0 == n % (2 + x),
        range(5, 1 + int(n ** 0.5), 6)
    ))


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''A lazy (generator) list unfolded from a seed value
       by repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None or just (residue, value).
       For a strict output list, wrap the result with list()
    '''
    def go(v):
        residueValue = f(v)
        while residueValue:
            yield residueValue[1]
            residueValue = f(residueValue[0])
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

