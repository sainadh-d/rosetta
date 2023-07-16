# Address of a variable

## Task Link
[Rosetta Code - Address of a variable](https://rosettacode.org/wiki/Address_of_a_variable)

## Java Code
## Python Code
### python_code_1.txt
```python
var num = 12
var pointer = ptr(num) # get pointer

print pointer # print address

@unsafe # bad idea!
pointer.addr = 0xFFFE # set the address

```

### python_code_2.txt
```python
foo = object()  # Create (instantiate) an empty object
address = id(foo)

```

