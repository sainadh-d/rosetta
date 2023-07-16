# Check output device is a terminal

## Task Link
[Rosetta Code - Check output device is a terminal](https://rosettacode.org/wiki/Check_output_device_is_a_terminal)

## Java Code
## Python Code
### python_code_1.txt
```python
from sys import stdout
if stdout.isatty():
    print 'The output device is a teletype. Or something like a teletype.'
else:
    print 'The output device isn\'t like a teletype.'

```

