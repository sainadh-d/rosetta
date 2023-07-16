# Respond to an unknown method call

## Task Link
[Rosetta Code - Respond to an unknown method call](https://rosettacode.org/wiki/Respond_to_an_unknown_method_call)

## Java Code
## Python Code
### python_code_1.txt
```python
class Example(object):
    def foo(self):
        print("this is foo")
    def bar(self):
        print("this is bar")
    def __getattr__(self, name):
        def method(*args):
            print("tried to handle unknown method " + name)
            if args:
                print("it had arguments: " + str(args))
        return method

example = Example()

example.foo()        # prints “this is foo”
example.bar()        # prints “this is bar”
example.grill()      # prints “tried to handle unknown method grill”
example.ding("dong") # prints “tried to handle unknown method ding”
                     # prints “it had arguments: ('dong',)”

```

