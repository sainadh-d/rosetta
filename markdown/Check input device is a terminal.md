# Check input device is a terminal

## Task Link
[Rosetta Code - Check input device is a terminal](https://rosettacode.org/wiki/Check_input_device_is_a_terminal)

## Java Code
## Python Code
### python_code_1.txt
```python
from sys import stdin
if stdin.isatty():
    print("Input comes from tty.")
else:
    print("Input doesn't come from tty.")

```

