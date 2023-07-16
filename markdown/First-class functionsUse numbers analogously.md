# First-class functions/Use numbers analogously

## Task Link
[Rosetta Code - First-class functions/Use numbers analogously](https://rosettacode.org/wiki/First-class_functions/Use_numbers_analogously)

## Java Code
## Python Code
### python_code_1.txt
```python
IDLE 2.6.1      
>>> # Number literals
>>> x,xi, y,yi = 2.0,0.5, 4.0,0.25
>>> # Numbers from calculation
>>> z  = x + y
>>> zi = 1.0 / (x + y)
>>> # The multiplier function is similar to 'compose' but with numbers
>>> multiplier = lambda n1, n2: (lambda m: n1 * n2 * m)
>>> # Numbers as members of collections
>>> numlist = [x, y, z]
>>> numlisti = [xi, yi, zi]
>>> # Apply numbers from list
>>> [multiplier(inversen, n)(.5) for n, inversen in zip(numlist, numlisti)]
[0.5, 0.5, 0.5]
>>>

```

### python_code_2.txt
```python
>>> # Some built in functions and their inverses
>>> from math import sin, cos, acos, asin
>>> # Add a user defined function and its inverse
>>> cube = lambda x: x * x * x
>>> croot = lambda x: x ** (1/3.0)
>>> # First class functions allow run-time creation of functions from functions
>>> # return function compose(f,g)(x) == f(g(x))
>>> compose = lambda f1, f2: ( lambda x: f1(f2(x)) )
>>> # first class functions should be able to be members of collection types
>>> funclist = [sin, cos, cube]
>>> funclisti = [asin, acos, croot]
>>> # Apply functions from lists as easily as integers
>>> [compose(inversef, f)(.5) for f, inversef in zip(funclist, funclisti)]
[0.5, 0.4999999999999999, 0.5]
>>>

```

