# The sieve of Sundaram

## Task Link
[Rosetta Code - The sieve of Sundaram](https://rosettacode.org/wiki/The_sieve_of_Sundaram)

## Java Code
## Python Code
### python_code_1.txt
```python
from numpy import log

def sieve_of_Sundaram(nth, print_all=True):
    """
    The sieve of Sundaram is a simple deterministic algorithm for finding all the
    prime numbers up to a specified integer. This function is modified from the
    Wikipedia entry wiki/Sieve_of_Sundaram, to give primes to their nth rather
    than the Wikipedia function that gives primes less than n.
    """
    assert nth > 0, "nth must be a positive integer"
    k = int((2.4 * nth * log(nth)) // 2)  # nth prime is at about n * log(n)
    integers_list = [True] * k
    for i in range(1, k):
        j = i
        while i + j + 2 * i * j < k:
            integers_list[i + j + 2 * i * j] = False
            j += 1
    pcount = 0
    for i in range(1, k + 1):
        if integers_list[i]:
            pcount += 1
            if print_all:
                print(f"{2 * i + 1:4}", end=' ')
                if pcount % 10 == 0:
                    print()

            if pcount == nth:
                print(f"\nSundaram primes start with 3. The {nth}th Sundaram prime is {2 * i + 1}.\n")
                break



sieve_of_Sundaram(100, True)

sieve_of_Sundaram(1000000, False)

```

### python_code_2.txt
```python
'''Sieve of Sundaram'''

from math import floor, log, sqrt
from itertools import islice


# sundaram :: Int -> [Int]
def sundaram(n):
    '''Sundaram prime numbers up to n'''
    m = (n - 1) // 2
    exclusions = {
        2 * i * j + i + j
        for i in range(1, 1 + floor(sqrt(m / 2)))
        for j in range(
            i, 1 + floor((m - i) / (1 + (2 * i)))
        )
    }
    return [
        1 + (2 * x) for x in range(1, 1 + m)
        if not x in exclusions
    ]


# nPrimesBySundaram :: Int -> [Int]
def nPrimesBySundaram(n):
    '''First n primes, by sieve of Sundaram.
    '''
    return list(islice(
        sundaram(
            # Probable limit
            int((2.4 * n * log(n)) // 2)
        ),
        int(n)
    ))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 100 Sundaram primes, 
       and millionth Sundaram prime.
    '''
    print("First hundred Sundaram primes, starting at 3:\n")
    print(table(10)([
        str(s) for s in nPrimesBySundaram(100)
    ]))
    print("\n\nMillionth Sundaram prime, starting at 3:")
    print(
        f'\n\t{nPrimesBySundaram(1E6)[-1]}'
    )


# ----------------------- GENERIC ------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divisible, the final list will be shorter than n.
    '''
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


# table :: Int -> [String] -> String
def table(n):
    '''A list of strings formatted as
       right-justified rows of n columns.
    '''
    def go(xs):
        w = len(xs[-1])
        return '\n'.join(
            ' '.join(row) for row in chunksOf(n)([
                s.rjust(w, ' ') for s in xs
            ])
        )
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

