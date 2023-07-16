# Terminal control/Coloured text

## Task Link
[Rosetta Code - Terminal control/Coloured text](https://rosettacode.org/wiki/Terminal_control/Coloured_text)

## Java Code
## Python Code
### python_code_1.txt
```python
from colorama import init, Fore, Back, Style
init(autoreset=True)

print Fore.RED + "FATAL ERROR! Cannot write to /boot/vmlinuz-3.2.0-33-generic"
print Back.BLUE + Fore.YELLOW + "What a cute console!"
print "This is an %simportant%s word" % (Style.BRIGHT, Style.NORMAL)
print Fore.YELLOW  + "Rosetta Code!"
print Fore.CYAN    + "Rosetta Code!"
print Fore.GREEN   + "Rosetta Code!"
print Fore.MAGENTA + "Rosetta Code!"
print Back.YELLOW + Fore.BLUE + Style.BRIGHT + " " * 40 + " == Good Bye!"

```

### python_code_2.txt
```python
from ctypes import *

windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
#Default CMD colour = 7
def color(colour):
    windll.Kernel32.SetConsoleTextAttribute(h, colour)

for count in range (0, 16):
    color(count)
    print "This Colour Is #" + str(count)

print ""
color(7)
raw_input("holding cmd")

```

