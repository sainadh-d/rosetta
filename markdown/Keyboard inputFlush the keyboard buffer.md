# Keyboard input/Flush the keyboard buffer

## Task Link
[Rosetta Code - Keyboard input/Flush the keyboard buffer](https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer)

## Java Code
## Python Code
### python_code_1.txt
```python
def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

```

