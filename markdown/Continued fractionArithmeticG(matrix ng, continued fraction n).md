# Continued fraction/Arithmetic/G(matrix ng, continued fraction n)

## Task Link
[Rosetta Code - Continued fraction/Arithmetic/G(matrix ng, continued fraction n)](https://rosettacode.org/wiki/Continued_fraction/Arithmetic/G(matrix_ng,_continued_fraction_n))

## Java Code
## Python Code
### python_code_1.txt
```python
class NG:
  def __init__(self, a1, a, b1, b):
    self.a1, self.a, self.b1, self.b = a1, a, b1, b

  def ingress(self, n):
    self.a, self.a1 = self.a1, self.a + self.a1 * n
    self.b, self.b1 = self.b1, self.b + self.b1 * n

  @property
  def needterm(self):
    return (self.b == 0 or self.b1 == 0) or not self.a//self.b == self.a1//self.b1

  @property
  def egress(self):
    n = self.a // self.b
    self.a,  self.b  = self.b,  self.a  - self.b  * n
    self.a1, self.b1 = self.b1, self.a1 - self.b1 * n
    return n

  @property
  def egress_done(self):
    if self.needterm: self.a, self.b = self.a1, self.b1
    return self.egress

  @property
  def done(self):
    return self.b == 0 and self.b1 == 0

```

### python_code_2.txt
```python
data = [["[1;5,2] + 1/2",      [2,1,0,2], [13,11]],
        ["[3;7] + 1/2",        [2,1,0,2], [22, 7]],
        ["[3;7] divided by 4", [1,0,0,4], [22, 7]]]

for string, ng, r in data:
  print( "%-20s->" % string, end='' )
  op = NG(*ng)
  for n in r2cf(*r):
    if not op.needterm: print( " %r" % op.egress, end='' )
    op.ingress(n)
  while True:
    print( " %r" % op.egress_done, end='' )
    if op.done: break
  print()

```

