# Repunit primes

## Task Link
[Rosetta Code - Repunit primes](https://rosettacode.org/wiki/Repunit_primes)

## Java Code
## Python Code
### python_code_1.txt
```python
from sympy import isprime
for b in range(2, 17):
    print(b, [n for n in range(2, 1001) if isprime(n) and isprime(int('1'*n, base=b))])

```

