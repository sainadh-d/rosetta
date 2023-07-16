# Elementary cellular automaton/Random number generator

## Task Link
[Rosetta Code - Elementary cellular automaton/Random number generator](https://rosettacode.org/wiki/Elementary_cellular_automaton/Random_number_generator)

## Java Code
## Python Code
### python_code_1.txt
```python
from elementary_cellular_automaton import eca, eca_wrap

def rule30bytes(lencells=100):
    cells = '1' + '0' * (lencells - 1)
    gen = eca(cells, 30)
    while True:
        yield int(''.join(next(gen)[0] for i in range(8)), 2)

if __name__ == '__main__':
    print([b for i,b in zip(range(10), rule30bytes())])

```

### python_code_2.txt
```python
def rule30bytes(lencells=100):
    cells = '1' + '0' * (lencells - 1)
    gen = eca_wrap(cells, 30)
    while True:
        yield int(''.join(next(gen)[0] for i in range(8)), 2))

```

