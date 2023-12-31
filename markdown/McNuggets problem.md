# McNuggets problem

## Task Link
[Rosetta Code - McNuggets problem](https://rosettacode.org/wiki/McNuggets_problem)

## Java Code
### java_code_1.txt
```java
public class McNuggets {

    public static void main(String... args) {
        int[] SIZES = new int[] { 6, 9, 20 };
        int MAX_TOTAL = 100;
        // Works like Sieve of Eratosthenes
        int numSizes = SIZES.length;
        int[] counts = new int[numSizes];
        int maxFound = MAX_TOTAL + 1;
        boolean[] found = new boolean[maxFound];
        int numFound = 0;
        int total = 0;
        boolean advancedState = false;
        do {
            if (!found[total]) {
                found[total] = true;
                numFound++;
            }
            
            // Advance state
            advancedState = false;
            for (int i = 0; i < numSizes; i++) {
                int curSize = SIZES[i];
                if ((total + curSize) > MAX_TOTAL) {
                    // Reset to zero and go to the next box size
                    total -= counts[i] * curSize;
                    counts[i] = 0;
                }
                else {
                    // Adding a box of this size still keeps the total at or below the maximum
                    counts[i]++;
                    total += curSize;
                    advancedState = true;
                    break;
                }
            }
            
        } while ((numFound < maxFound) && advancedState);
        
        if (numFound < maxFound) {
            // Did not find all counts within the search space
            for (int i = MAX_TOTAL; i >= 0; i--) {
                if (!found[i]) {
                    System.out.println("Largest non-McNugget number in the search space is " + i);
                    break;
                }
            }
        }
        else {
            System.out.println("All numbers in the search space are McNugget numbers");
        }
        
        return;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from itertools import product
>>> nuggets = set(range(101))
>>> for s, n, t in product(range(100//6+1), range(100//9+1), range(100//20+1)):
	nuggets.discard(6*s + 9*n + 20*t)

	
>>> max(nuggets)
43
>>>

```

### python_code_2.txt
```python
>>> from itertools import product
>>> max(x for x in range(100+1) if x not in
...   (6*s + 9*n + 20*t for s, n, t in
...     product(range(100//6+1), range(100//9+1), range(100//20+1))))
43
>>>

```

### python_code_3.txt
```python
#Wherein I observe that Set Comprehension is not intrinsically dysfunctional. Nigel Galloway: October 28th., 2018
n = {n for x in range(0,101,20) for y in range(x,101,9) for n in range(y,101,6)}
g = {n for n in range(101)}
print(max(g.difference(n)))

```

### python_code_4.txt
```python
'''mcNuggets list monad'''

from itertools import (chain, dropwhile)


# mcNuggetsByListMonad :: Int -> Set Int
def mcNuggetsByListMonad(limit):
    '''McNugget numbers up to limit.'''

    box = size(limit)
    return set(
        bind(
            box(6)
        )(lambda x: bind(
            box(9)
        )(lambda y: bind(
            box(20)
        )(lambda z: (
            lambda v=sum([x, y, z]): (
                [] if v > limit else [v]
            )
        )())))
    )


# Which, for comparison, is equivalent to:

# mcNuggetsByComprehension :: Int -> Set Int
def mcNuggetsByComprehension(limit):
    '''McNuggets numbers up to limit'''
    box = size(limit)
    return {
        v for v in (
            sum([x, y, z])
            for x in box(6)
            for y in box(9)
            for z in box(20)
        ) if v <= limit
    }


# size :: Int -> Int -> [Int]
def size(limit):
    '''Multiples of n up to limit.'''
    return lambda n: enumFromThenTo(0)(n)(limit)


# -------------------------- TEST --------------------------
def main():
    '''List monad and set comprehension - parallel routes'''

    def test(limit):
        def go(nuggets):
            ys = list(dropwhile(
                lambda x: x in nuggets,
                enumFromThenTo(limit)(limit - 1)(1)
            ))
            return str(ys[0]) if ys else (
                'No unreachable targets in this range.'
            )
        return lambda nuggets: go(nuggets)

    def fName(f):
        return f.__name__

    limit = 100
    print(
        fTable(main.__doc__ + ':\n')(fName)(test(limit))(
            lambda f: f(limit)
        )([mcNuggetsByListMonad, mcNuggetsByComprehension])
    )


# ------------------------ GENERIC -------------------------

# bind (>>=) :: [a] -> (a -> [b]) -> [b]
def bind(xs):
    '''List monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.
    '''
    return lambda f: chain.from_iterable(
        map(f, xs)
    )


# enumFromThenTo :: Int -> Int -> Int -> [Int]
def enumFromThenTo(m):
    '''Integer values enumerated from m to n
       with a step defined by nxt-m.
    '''
    def go(nxt, n):
        d = nxt - m
        return range(m, n - 1 if d < 0 else 1 + n, d)
    return lambda nxt: lambda n: go(nxt, n)


# ------------------------ DISPLAY -------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + fxShow(f(x))
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox


# MAIN ---
if __name__ == '__main__':
    main()

```

