# Terminal control/Cursor positioning

## Task Link
[Rosetta Code - Terminal control/Cursor positioning](https://rosettacode.org/wiki/Terminal_control/Cursor_positioning)

## Java Code
## Python Code
### python_code_1.txt
```python
print("\033[6;3HHello")

```

### python_code_2.txt
```python
from ctypes import *

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass
    
COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    
    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)

print_at(6, 3, "Hello")

```

