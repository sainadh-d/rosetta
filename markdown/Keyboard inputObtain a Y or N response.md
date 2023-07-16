# Keyboard input/Obtain a Y or N response

## Task Link
[Rosetta Code - Keyboard input/Obtain a Y or N response](https://rosettacode.org/wiki/Keyboard_input/Obtain_a_Y_or_N_response)

## Java Code
## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python

try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

print "Press Y or N to continue"
while True:
    char = getch()
    if char.lower() in ("y", "n"):
        print char
        break

```

### python_code_2.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from curses import wrapper
#
#
def main(stdscr):
  # const
  #y = ord("y")
  #n = ord("n")
  while True:
    # keyboard input interceptor|listener
    #window.nodelay(yes)
    # - If yes is 1, getch() will be non-blocking.
    # return char code
    #kb_Inpt = stdscr.getch()
    # return string
    kb_Inpt = stdscr.getkey()
    #if kb_Inpt == (y or n):
    if kb_Inpt.lower() == ('y' or 'n'):
      break
      return None
  #
  return None
#
#*** unit test ***#
if __name__ == "__main__":
  #
  wrapper(main)

```

