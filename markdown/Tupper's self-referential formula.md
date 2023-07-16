# Tupper's self-referential formula

## Task Link
[Rosetta Code - Tupper's self-referential formula](https://rosettacode.org/wiki/Tupper%27s_self-referential_formula)

## Java Code
## Python Code
### python_code_1.txt
```python
#!/usr/bin/python

import codecs
import os

def tuppers_formula(x, y):
    """Return True if point (x, y) (x and y both start at 0) is to be drawn black, False otherwise
    """
    k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
    return ((k + y)//17//2**(17*int(x) + int(y)%17))%2 > 0.5


with codecs.open("tupper.txt", "w", "utf-8") as f:
    values = [[tuppers_formula(x, y) for x in range(106)] for y in range(17)]
    for row in values:
        for value in row[::-1]:   # x = 0 starts at the left so reverse the whole row
            if value:
                f.write("\u2588") # Write a block
            else:
                f.write(" ")
        f.write(os.linesep)

```

