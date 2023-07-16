# Metaprogramming

## Task Link
[Rosetta Code - Metaprogramming](https://rosettacode.org/wiki/Metaprogramming)

## Java Code
## Python Code
### python_code_1.txt
```python
from macropy.core.macros import *
from macropy.core.quotes import macros, q, ast, u

macros = Macros()

@macros.expr
def expand(tree, **kw):
    addition = 10
    return q[lambda x: x * ast[tree] + u[addition]]

```

### python_code_2.txt
```python
func = expand[1 + 2]
print func(5)

```

