# Terminal control/Hiding the cursor

## Task Link
[Rosetta Code - Terminal control/Hiding the cursor](https://rosettacode.org/wiki/Terminal_control/Hiding_the_cursor)

## Java Code
## Python Code
### python_code_1.txt
```python
print("\x1b[?25l") # hidden
print("\x1b[?25h") # shown

```

### python_code_2.txt
```python
import curses
import time

stdscr = curses.initscr()
curses.curs_set(1)  # visible
time.sleep(2)
curses.curs_set(0)  # invisible
time.sleep(2)
curses.curs_set(1)  # visible
time.sleep(2)
curses.endwin()

```

