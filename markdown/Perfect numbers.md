# Perfect numbers

## Task Link
[Rosetta Code - Perfect numbers](https://rosettacode.org/wiki/Perfect_numbers)

## Java Code
### java_code_1.txt
```java
public static boolean perf(int n){
	int sum= 0;
	for(int i= 1;i < n;i++){
		if(n % i == 0){
			sum+= i;
		}
	}
	return sum == n;
}

```

### java_code_2.txt
```java
import java.math.BigInteger;

public static boolean perf(BigInteger n){
	BigInteger sum= BigInteger.ZERO;
	for(BigInteger i= BigInteger.ONE;
	i.compareTo(n) < 0;i=i.add(BigInteger.ONE)){
		if(n.mod(i).equals(BigInteger.ZERO)){
			sum= sum.add(i);
		}
	}
	return sum.equals(n);
}

```

## Python Code
### python_code_1.txt
```python
def perf1(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

```

### python_code_2.txt
```python
from itertools import chain, cycle, accumulate

def factor2(n):
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r

def perf4(n):
    "Using most efficient prime factoring routine from: http://rosettacode.org/wiki/Factors_of_an_integer#Python"
    return 2 * n == sum(factor2(n))

```

### python_code_3.txt
```python
def perf2(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print (
    list(filter(perf2, range(1, 10001)))
)

```

### python_code_4.txt
```python
'''Perfect numbers'''

from math import sqrt


# perfect :: Int - > Bool
def perfect(n):
    '''Is n the sum of its proper divisors other than 1 ?'''

    root = sqrt(n)
    lows = [x for x in enumFromTo(2)(int(root)) if 0 == (n % x)]
    return 1 < n and (
        n == 1 + sum(lows + [n / x for x in lows if root != x])
    )


# main :: IO ()
def main():
    '''Test'''

    print([
        x for x in enumFromTo(1)(10000) if perfect(x)
    ])


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


if __name__ == '__main__':
    main()

```

