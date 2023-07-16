# Left factorials

## Task Link
[Rosetta Code - Left factorials](https://rosettacode.org/wiki/Left_factorials)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public class LeftFac{
	public static BigInteger factorial(BigInteger n){
		BigInteger ans = BigInteger.ONE;
		for(BigInteger x = BigInteger.ONE; x.compareTo(n) <= 0; x = x.add(BigInteger.ONE)){
			ans = ans.multiply(x);
		}
		return ans;
	}
	
	public static BigInteger leftFact(BigInteger n){
		BigInteger ans = BigInteger.ZERO;
		for(BigInteger k = BigInteger.ZERO; k.compareTo(n.subtract(BigInteger.ONE)) <= 0; k = k.add(BigInteger.ONE)){
			ans = ans.add(factorial(k));
		}
		return ans;
	}
	
	public static void main(String[] args){
		for(int i = 0; i <= 10; i++){
			System.out.println("!" + i + " = " + leftFact(BigInteger.valueOf(i)));
		}
		
		for(int i = 20; i <= 110; i += 10){
			System.out.println("!" + i + " = " + leftFact(BigInteger.valueOf(i)));
		}
		
		for(int i = 1000; i <= 10000; i += 1000){
			System.out.println("!" + i + " has " + leftFact(BigInteger.valueOf(i)).toString().length() + " digits");
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice

def lfact():
    yield 0
    fact, summ, n = 1, 0, 1 
    while 1:
        fact, summ, n = fact*n, summ + fact, n + 1
        yield summ

print('first 11:\n  %r' % [lf for i, lf in zip(range(11), lfact())])
print('20 through 110 (inclusive) by tens:')
for lf in islice(lfact(), 20, 111, 10):
    print(lf)
print('Digits in 1,000 through 10,000 (inclusive) by thousands:\n  %r' 
      % [len(str(lf)) for lf in islice(lfact(), 1000, 10001, 1000)] )

```

### python_code_2.txt
```python
'''Left factorials'''

from itertools import (accumulate, chain, count, islice)
from operator import (mul, add)


# leftFact :: [Integer]
def leftFact():
    '''Left factorial series defined in terms
       of the factorial series.
    '''
    return accumulate(
        chain([0], fact()), add
    )


# fact :: [Integer]
def fact():
    '''The factorial series.
    '''
    return accumulate(
        chain([1], count(1)), mul
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tests'''
    print(
        'Terms 0 thru 10 inclusive:\n  %r'
        % take(11)(leftFact())
    )

    print('\nTerms 20 thru 110 (inclusive) by tens:')
    for x in takeFromThenTo(20)(30)(110)(leftFact()):
        print(x)

    print(
        '\n\nDigit counts for terms 1k through 10k (inclusive) by k:\n  %r'
        % list(map(
            compose(len)(str),
            takeFromThenTo(1000)(2000)(10000)(
                leftFact()
            )
        ))
    )


# ----------------------- GENERIC ------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but defines a succession of
       intermediate values, building from the left.
    '''
    def go(a):
        def g(xs):
            return accumulate(chain([a], xs), f)
        return g
    return go


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# takeFromThenTo :: Int -> Int -> Int -> [a] -> [a]
def takeFromThenTo(a):
    '''Values drawn from a series betweens positions a and b
       at intervals of size z'''
    return lambda b: lambda z: lambda xs: islice(
        xs, a, 1 + z, b - a
    )


if __name__ == '__main__':
    main()

```

