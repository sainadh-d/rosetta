# Named parameters

## Task Link
[Rosetta Code - Named parameters](https://rosettacode.org/wiki/Named_parameters)

## Java Code
### java_code_2.txt
```java
processNutritionFacts(new NutritionFacts.Builder(240, 8).calories(100).sodium(35).carbohydrate(27).build());

```

## Python Code
### python_code_1.txt
```python
def subtract(x, y):
    return x - y

subtract(5, 3)         # used as positional parameters; evaluates to 2
subtract(y = 3, x = 5) # used as named parameters;      evaluates to 2

```

### python_code_2.txt
```python
>>> from __future__ import print_function
>>>
>>> def show_args(defparam1, defparam2 = 'default value', *posparam, **keyparam):
  "Straight-forward function to show its arguments"
  print ("  Default Parameters:")
  print ("    defparam1 value is:", defparam1)
  print ("    defparam2 value is:", defparam2)

  print ("  Positional Arguments:")
  if posparam:
    n = 0
    for p in posparam:
      print ("    positional argument:", n, "is:", p)
      n += 1
  else:
    print ("    <None>")

  print ("  Keyword Arguments (by sorted key name):")
  if keyparam:
    for k,v in sorted(keyparam.items()):
      print ("    keyword argument:", k, "is:", v)
  else:
    print ("    <None>")


>>> show_args('POSITIONAL', 'ARGUMENTS')
  Default Parameters:
    defparam1 value is: POSITIONAL
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args(defparam2='ARGUMENT', defparam1='KEYWORD')
  Default Parameters:
    defparam1 value is: KEYWORD
    defparam2 value is: ARGUMENT
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args( *('SEQUENCE', 'ARGUMENTS') )
  Default Parameters:
    defparam1 value is: SEQUENCE
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args( **{'defparam2':'ARGUMENTS', 'defparam1':'MAPPING'} )
  Default Parameters:
    defparam1 value is: MAPPING
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args('ONLY DEFINE defparam1 ARGUMENT')
  Default Parameters:
    defparam1 value is: ONLY DEFINE defparam1 ARGUMENT
    defparam2 value is: default value
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args('POSITIONAL', 'ARGUMENTS',
              'EXTRA', 'POSITIONAL', 'ARGUMENTS')
  Default Parameters:
    defparam1 value is: POSITIONAL
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    positional argument: 0 is: EXTRA
    positional argument: 1 is: POSITIONAL
    positional argument: 2 is: ARGUMENTS
  Keyword Arguments (by sorted key name):
    <None>
>>> show_args('POSITIONAL', 'ARGUMENTS',
              kwa1='EXTRA', kwa2='KEYWORD', kwa3='ARGUMENTS')
  Default Parameters:
    defparam1 value is: POSITIONAL
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    <None>
  Keyword Arguments (by sorted key name):
    keyword argument: kwa1 is: EXTRA
    keyword argument: kwa2 is: KEYWORD
    keyword argument: kwa3 is: ARGUMENTS
>>> show_args('POSITIONAL',
              'ARGUMENTS', 'EXTRA', 'POSITIONAL', 'ARGUMENTS',
              kwa1='EXTRA', kwa2='KEYWORD', kwa3='ARGUMENTS')
  Default Parameters:
    defparam1 value is: POSITIONAL
    defparam2 value is: ARGUMENTS
  Positional Arguments:
    positional argument: 0 is: EXTRA
    positional argument: 1 is: POSITIONAL
    positional argument: 2 is: ARGUMENTS
  Keyword Arguments (by sorted key name):
    keyword argument: kwa1 is: EXTRA
    keyword argument: kwa2 is: KEYWORD
    keyword argument: kwa3 is: ARGUMENTS
>>> # But note:
>>> show_args('POSITIONAL', 'ARGUMENTS',
              kwa1='EXTRA', kwa2='KEYWORD', kwa3='ARGUMENTS',
              'EXTRA', 'POSITIONAL', 'ARGUMENTS')
SyntaxError: non-keyword arg after keyword arg
>>>

```

