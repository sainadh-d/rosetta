# Babbage problem

## Task Link
[Rosetta Code - Babbage problem](https://rosettacode.org/wiki/Babbage_problem)

## Java Code
### java_code_1.txt
```java
public class Test {

    public static void main(String[] args) {

        // let n be zero
        int n = 0;

        // repeat the following action
        do {

            // increase n by 1
            n++;

        // while the modulo of n times n is not equal to 269696
        } while (n * n % 1000_000 != 269696);

        // show the result
        System.out.println(n);
    }
}

```

### java_code_2.txt
```java
// Lines that begin with two slashes, thus, are comments: they
// will be ignored by the machine.

// First we must declare a variable, n, suitable to store an integer:

int n;

// Each statement we address to the machine must end with a semicolon.

// To begin with, the value of n will be zero:

n = 0;

// Now we must repeatedly increase it by one, checking each time to see
// whether its square ends in 269,696.

// We shall do this by seeing whether the remainder, when n squared
// is divided by one million, is equal to 269,696.

do {
    n = n + 1;
} while (n * n % 1000000 != 269696);

// To read this formula, it is necessary to know the following
// elements of the notation:
//     * means 'multiplied by'
//     % means 'modulo', or remainder after division
//     != means 'is not equal to'

// Now that we have our result, we need to display it.

// println is short for 'print line'

println(n);

```

## Python Code
### python_code_1.txt
```python
# Lines that start by # are a comments:
# they will be ignored by the machine

n=0 # n is a variable and its value is 0

# we will increase its value by one until
# its square ends in 269,696

while n**2 % 1000000 != 269696:

    # n**2 -> n squared
    # %    -> 'modulo' or remainder after division
    # !=   -> not equal to
    
    n += 1 # += -> increase by a certain number

print(n) # prints n

```

### python_code_2.txt
```python
print(next(x for x in range(30000) if pow(x, 2, 1000000) == 269696))

```

### python_code_3.txt
```python
from itertools import accumulate, count

print(*next(filter(lambda t: t[1] % 1000000 == 269696, enumerate(accumulate(count(1, 2)), 1))))

```

### python_code_4.txt
```python
'''Babbage problem'''

from math import (floor, sqrt)
from itertools import (islice)


# squaresWithSuffix :: Int -> Gen [Int]
def squaresWithSuffix(n):
    '''Non finite stream of squares with a given suffix.'''
    stem = 10 ** len(str(n))
    i = 0
    while True:
        i = until(lambda x: isPerfectSquare(n + (stem * x)))(
            succ
        )(i)
        yield n + (stem * i)
        i = succ(i)


# isPerfectSquare :: Int -> Bool
def isPerfectSquare(n):
    '''True if n is a perfect square.'''
    r = sqrt(n)
    return r == floor(r)


# TEST ----------------------------------------------------

# main :: IO ()
def main():
    '''Smallest positive integers whose squares end in the digits 269,696'''
    print(
        fTable(main.__doc__ + ':\n')(
            lambda n: str(int(sqrt(n))) + '^2'
        )(repr)(identity)(
            take(10)(squaresWithSuffix(269696))
        )
    )


# GENERIC -------------------------------------------------

# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


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


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


# FORMATTING ----------------------------------------------
# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

