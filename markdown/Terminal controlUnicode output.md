# Terminal control/Unicode output

## Task Link
[Rosetta Code - Terminal control/Unicode output](https://rosettacode.org/wiki/Terminal_control/Unicode_output)

## Java Code
## Python Code
### python_code_1.txt
```python
import sys

if "UTF-8" in sys.stdout.encoding:
    print("△")
else:
    raise Exception("Terminal can't handle UTF-8")

```

