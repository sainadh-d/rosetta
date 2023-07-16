# Zero to the zero power

## Task Link
[Rosetta Code - Zero to the zero power](https://rosettacode.org/wiki/Zero_to_the_zero_power)

## Java Code
### java_code_1.txt
```java
System.out.println(Math.pow(0, 0));

```

## Python Code
### python_code_1.txt
```python
from decimal import Decimal
from fractions import Fraction
from itertools import product

zeroes = [0, 0.0, 0j, Decimal(0), Fraction(0, 1), -0.0, -0.0j, Decimal(-0.0)]
for i, j in product(zeroes, repeat=2):
    try:
        ans = i**j
    except:
        ans = '<Exception raised>'
    print(f'{i!r:>15} ** {j!r:<15} = {ans!r}')

```

### python_code_2.txt
```python
from decimal import Decimal
from fractions import Fraction
for n in (Decimal(0), Fraction(0, 1), complex(0), float(0), int(0)):
	try:
		n1 = n**n
	except:
		n1 = '<Raised exception>'
	try:
		n2 = pow(n, n)
	except:
		n2 = '<Raised exception>'
	print('%8s: ** -> %r; pow -> %r' % (n.__class__.__name__, n1, n2))

```

