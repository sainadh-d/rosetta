# Add a variable to a class instance at runtime

## Task Link
[Rosetta Code - Add a variable to a class instance at runtime](https://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime)

## Java Code
## Python Code
### python_code_1.txt
```python
class empty(object):
    pass
e = empty()

```

### python_code_2.txt
```python
   e.foo = 1

```

### python_code_3.txt
```python
   setattr(e, name, value)

```

### python_code_4.txt
```python
class empty(object):
    def __init__(this):
        this.foo = "whatever"

def patch_empty(obj):
    def fn(self=obj):
        print self.foo
    obj.print_output = fn

e = empty()
patch_empty(e)
e.print_output()
# >>> whatever

```

