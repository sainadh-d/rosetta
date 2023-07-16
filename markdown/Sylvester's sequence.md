# Sylvester's sequence

## Task Link
[Rosetta Code - Sylvester's sequence](https://rosettacode.org/wiki/Sylvester%27s_sequence)

## Java Code
## Python Code
### python_code_1.txt
```python
'''Sylvester's sequence'''

from functools import reduce
from itertools import count, islice


# sylvester :: [Int]
def sylvester():
    '''Non-finite stream of the terms
       of Sylvester's sequence.
       (OEIS A000058)
    '''
    def go(n):
        return 1 + reduce(
            lambda a, x: a * go(x),
            range(0, n),
            1
        ) if 0 != n else 2

    return map(go, count(0))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First terms, and sum of reciprocals.'''

    print("First 10 terms of OEIS A000058:")
    xs = list(islice(sylvester(), 10))
    print('\n'.join([
        str(x) for x in xs
    ]))

    print("\nSum of the reciprocals of the first 10 terms:")
    print(
        reduce(lambda a, x: a + 1 / x, xs, 0)
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
'''Sylvester's sequence'''

from functools import reduce
from itertools import islice

# sylvester :: [Int]
def sylvester():
    '''A non finite sequence of the terms of OEIS A000058
    '''
    return iterate(
        lambda x: x * (x - 1) + 1
    )(2)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First terms, and sum of reciprocals.'''

    print("First 10 terms of OEIS A000058:")
    xs = list(islice(sylvester(), 10))
    print('\n'.join([
        str(x) for x in xs
    ]))

    print("\nSum of the reciprocals of the first 10 terms:")
    print(
        reduce(lambda a, x: a + 1 / x, xs, 0)
    )

# ----------------------- GENERIC ------------------------

# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

