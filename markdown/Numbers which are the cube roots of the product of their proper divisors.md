# Numbers which are the cube roots of the product of their proper divisors

## Task Link
[Rosetta Code - Numbers which are the cube roots of the product of their proper divisors](https://rosettacode.org/wiki/Numbers_which_are_the_cube_roots_of_the_product_of_their_proper_divisors)

## Java Code
## Python Code
### python_code_1.txt
```python
''' Rosetta code rosettacode.org/wiki/Numbers_which_are_the_cube_roots_of_the_product_of_their_proper_divisors '''

from functools import reduce
from sympy import divisors


FOUND = 0
for num in range(1, 1_000_000):
    divprod = reduce(lambda x, y: x * y, divisors(num)[:-1])if num > 1 else 1
    if num * num * num == divprod:
        FOUND += 1
        if FOUND <= 50:
            print(f'{num:5}', end='\n' if FOUND % 10 == 0 else '')
        if FOUND == 500:
            print(f'\nFive hundreth: {num:,}')
        if FOUND == 5000:
            print(f'\nFive thousandth: {num:,}')
        if FOUND == 50000:
            print(f'\nFifty thousandth: {num:,}')
            break

```

### python_code_2.txt
```python
from sympy import divisors

numfound = 0
for num in range(1, 1_000_000):
    if num == 1 or len(divisors(num)) == 8:
        numfound += 1
        if numfound <= 50:
            print(f'{num:5}', end='\n' if numfound % 10 == 0 else '')
        if numfound == 500:
            print(f'\nFive hundreth: {num:,}')
        if numfound == 5000:
            print(f'\nFive thousandth: {num:,}')
        if numfound == 50000:
            print(f'\nFifty thousandth: {num:,}')
            break

```

