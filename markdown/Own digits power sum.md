# Own digits power sum

## Task Link
[Rosetta Code - Own digits power sum](https://rosettacode.org/wiki/Own_digits_power_sum)

## Java Code
## Python Code
### python_code_1.txt
```python
""" Rosetta code task: Own_digits_power_sum """

def isowndigitspowersum(integer):
    """ true if sum of (digits of number raised to number of digits) == number """
    digits = [int(c) for c in str(integer)]
    exponent = len(digits)
    return sum(x ** exponent for x in digits) == integer

print("Own digits power sums for N = 3 to 9 inclusive:")
for i in range(100, 1000000000):
    if isowndigitspowersum(i):
        print(i)

```

### python_code_2.txt
```python
""" Rosetta code task: Own_digits_power_sum (recursive method)"""

MAX_BASE = 10
POWER_DIGIT = [[1 for _ in range(MAX_BASE)] for _ in range(MAX_BASE)]
USED_DIGITS = [0 for _ in range(MAX_BASE)]
NUMBERS = []

def calc_num(depth, used):
    """ calculate the number at a given recurse depth """
    result = 0
    if depth < 3:
        return 0
    for i in range(1, MAX_BASE):
        if used[i] > 0:
            result += used[i] * POWER_DIGIT[depth][i]
    if result != 0:
        num, rnum = result, 1
        while rnum != 0:
            rnum = num // MAX_BASE
            used[num - rnum * MAX_BASE] -= 1
            num = rnum
            depth -= 1
        if depth == 0:
            i = 1
            while i < MAX_BASE and used[i] == 0:
                i += 1
            if i >= MAX_BASE:
                NUMBERS.append(result)
    return 0

def next_digit(dgt, depth):
    """ get next digit at the given depth """
    if depth < MAX_BASE - 1:
        for i in range(dgt, MAX_BASE):
            USED_DIGITS[dgt] += 1
            next_digit(i, depth + 1)
            USED_DIGITS[dgt] -= 1

    if dgt == 0:
        dgt = 1
    for i in range(dgt, MAX_BASE):
        USED_DIGITS[i] += 1
        calc_num(depth, USED_DIGITS.copy())
        USED_DIGITS[i] -= 1

for j in range(1, MAX_BASE):
    for k in range(MAX_BASE):
        POWER_DIGIT[j][k] = POWER_DIGIT[j - 1][k] * k

next_digit(0, 0)
print(NUMBERS)
NUMBERS = list(set(NUMBERS))
NUMBERS.sort()
print('Own digits power sums for N = 3 to 9 inclusive:')
for n in NUMBERS:
    print(n)

```

### python_code_3.txt
```python
'''Own digit power sums'''

from itertools import accumulate, chain, islice, repeat
from functools import reduce


# ownDigitsPowerSums :: Int -> [Int]
def ownDigitsPowerSums(n):
    '''All own digit power sums of digit length N'''
    def go(xs):
        m = reduce(lambda a, x: a + (x ** n), xs, 0)
        return [m] if digitsMatch(m)(xs) else []

    return concatMap(go)(
        combinationsWithRepetitions(n)(range(0, 1 + 9))
    )


# digitsMatch :: Int -> [Int] -> Bool
def digitsMatch(n):
    '''True if the digits in ds contain exactly
       the digits of n, in any order.
    '''
    def go(ds):
        return sorted(ds) == sorted(digits(n))
    return go


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Own digit power sums for digit lengths 3..9'''
    print(
        '\n'.join([
            'N ∈ [3 .. 8]',
            *map(str, concatMap(ownDigitsPowerSums)(
                range(3, 1 + 8)
            )),
            '\nN=9',
            *map(str, ownDigitsPowerSums(9))
        ])
    )


# ----------------------- GENERIC ------------------------

# combinationsWithRepetitions :: Int -> [a] -> [kTuple a]
def combinationsWithRepetitions(k):
    '''Combinations with repetitions.
       A list of tuples, representing
       sets of cardinality k,
       with elements drawn from xs.
    '''
    def f(a, x):
        def go(ys, xs):
            return xs + [[x] + y for y in ys]
        return accumulate(a, go)

    def combsBySize(xs):
        return [
            tuple(x) for x in next(islice(
                reduce(
                    f, xs, chain(
                        [[[]]],
                        islice(repeat([]), k)
                    )
                ), k, None
            ))
        ]
    return combsBySize


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been
       mapped.
       The list monad can be derived by using a function f
       which wraps its output in a list, (using an empty
       list to represent computational failure).
    '''
    def go(xs):
        return list(chain.from_iterable(map(f, xs)))
    return go


# digits :: Int -> [Int]
def digits(n):
    '''The individual digits of n as integers'''
    return [int(c) for c in str(n)]


# MAIN ---
if __name__ == '__main__':
    main()

```

