# Euler's sum of powers conjecture

## Task Link
[Rosetta Code - Euler's sum of powers conjecture](https://rosettacode.org/wiki/Euler%27s_sum_of_powers_conjecture)

## Java Code
### java_code_1.txt
```java
public class eulerSopConjecture
{

    static final int    MAX_NUMBER = 250;

    public static void main( String[] args )
    {
        boolean found = false;
        long[]  fifth = new long[ MAX_NUMBER ];

        for( int i = 1; i <= MAX_NUMBER; i ++ )
        {
            long i2 =  i * i;
            fifth[ i - 1 ] = i2 * i2 * i;
        } // for i

        for( int a = 0; a < MAX_NUMBER && ! found ; a ++ )
        {
            for( int b = a; b < MAX_NUMBER && ! found ; b ++ )
            {
                for( int c = b; c < MAX_NUMBER && ! found ; c ++ )
                {
                    for( int d = c; d < MAX_NUMBER && ! found ; d ++ )
                    {
                        long sum  = fifth[a] + fifth[b] + fifth[c] + fifth[d];
                        int  e = java.util.Arrays.binarySearch( fifth, sum );
                        found  = ( e >= 0 );
                        if( found )
                        {
                            // the value at e is a fifth power
                            System.out.print( (a+1) + "^5 + "
                                            + (b+1) + "^5 + "
                                            + (c+1) + "^5 + "
                                            + (d+1) + "^5 = "
                                            + (e+1) + "^5"
                                            );
                        } // if found;;
                    } // for d
                } // for c
            } // for b
        } // for a
    } // main

} // eulerSopConjecture

```

## Python Code
### python_code_1.txt
```python
def eulers_sum_of_powers():
    max_n = 250
    pow_5 = [n**5 for n in range(max_n)]
    pow5_to_n = {n**5: n for n in range(max_n)}
    for x0 in range(1, max_n):
        for x1 in range(1, x0):
            for x2 in range(1, x1):
                for x3 in range(1, x2):
                    pow_5_sum = sum(pow_5[i] for i in (x0, x1, x2, x3))
                    if pow_5_sum in pow5_to_n:
                        y = pow5_to_n[pow_5_sum]
                        return (x0, x1, x2, x3, y)

print("%i**5 + %i**5 + %i**5 + %i**5 == %i**5" % eulers_sum_of_powers())

```

### python_code_2.txt
```python
from itertools import combinations

def eulers_sum_of_powers():
    max_n = 250
    pow_5 = [n**5 for n in range(max_n)]
    pow5_to_n = {n**5: n for n in range(max_n)}
    for x0, x1, x2, x3 in combinations(range(1, max_n), 4):
        pow_5_sum = sum(pow_5[i] for i in (x0, x1, x2, x3))
        if pow_5_sum in pow5_to_n:
            y = pow5_to_n[pow_5_sum]
            return (x0, x1, x2, x3, y)

print("%i**5 + %i**5 + %i**5 + %i**5 == %i**5" % eulers_sum_of_powers())

```

### python_code_3.txt
```python
MAX = 250
p5, sum2 = {}, {}

for i in range(1, MAX):
	p5[i**5] = i
	for j in range(i, MAX):
		sum2[i**5 + j**5] = (i, j)

sk = sorted(sum2.keys())
for p in sorted(p5.keys()):
	for s in sk:
		if p <= s: break
		if p - s in sum2:
			print(p5[p], sum2[s] + sum2[p-s])
			exit()

```

### python_code_4.txt
```python
'''Euler's sum of powers conjecture'''

from itertools import (chain, takewhile)


# main :: IO ()
def main():
    '''Search for counter-example'''

    xs = enumFromTo(1)(249)

    powerMap = {x**5: x for x in xs}
    sumMap = {
        x**5 + y**5: (x, y)
        for x in xs[1:]
        for y in xs if x > y
    }

    # isExample :: (Int, Int) -> Bool
    def isExample(ps):
        p, s = ps
        return p - s in sumMap

    # display :: (Int, Int) -> String
    def display(ps):
        p, s = ps
        a, b = sumMap[p - s]
        c, d = sumMap[s]
        return '^5 + '.join([str(n) for n in [a, b, c, d]]) + (
            '^5 = ' + str(powerMap[p]) + '^5'
        )

    print(__doc__ + ' – counter-example:\n')
    print(
        maybe('No counter-example found.')(display)(
            find(isExample)(
                bind(powerMap.keys())(
                    lambda p: bind(
                        takewhile(
                            lambda x: p > x,
                            sumMap.keys()
                        )
                    )(lambda s: [(p, s)])
                )
            )
        )
    )


# ----------------------- GENERIC ------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: () -> Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# bind (>>=) :: [a] -> (a -> [b]) -> [b]
def bind(xs):
    '''List monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.
    '''
    def go(f):
        return chain.from_iterable(map(f, xs))
    return go


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


# find :: (a -> Bool) -> [a] -> Maybe a
def find(p):
    '''Just the first element in the list that matches p,
       or Nothing if no elements match.
    '''
    def go(xs):
        try:
            return Just(next(x for x in xs if p(x)))
        except StopIteration:
            return Nothing()
    return go


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if (
        None is m or m.get('Nothing')
    ) else f(m.get('Just'))


# MAIN ---
if __name__ == '__main__':
    main()

```

