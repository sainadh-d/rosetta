# Memory layout of a data structure

## Task Link
[Rosetta Code - Memory layout of a data structure](https://rosettacode.org/wiki/Memory_layout_of_a_data_structure)

## Java Code
## Python Code
### python_code_1.txt
```python
from ctypes import Structure, c_int

rs232_9pin  = "_0 CD RD TD DTR SG DSR RTS CTS RI".split()
rs232_25pin = ( "_0  PG  TD  RD  RTS CTS DSR SG  CD  pos neg"
                "_11 SCD SCS STD TC  SRD RC"
                "_18 SRS DTR SQD RI DRS XTC" ).split()

class RS232_9pin(Structure):
    _fields_ = [(__, c_int, 1) for __ in rs232_9pin]

	
class RS232_25pin(Structure):
    _fields_ = [(__, c_int, 1) for __ in rs232_25pin]

```

