# Function definition

## Task Link
[Rosetta Code - Function definition](https://rosettacode.org/wiki/Function_definition)

## Java Code
### java_code_2.txt
```java
public class Math
{
     public static    int multiply(   int a,    int b) { return a*b; }
     public static double multiply(double a, double b) { return a*b; }
}

```

### java_code_3.txt
```java
float multiply(float x, float y)
{
    return x * y;
}

```

## Python Code
### python_code_1.txt
```python
def multiply(x, y):
    return x * y

```

### python_code_2.txt
```python
def multiply(a, b):
    return a * b

```

### python_code_3.txt
```python
multiply = lambda a, b: a * b

```

### python_code_4.txt
```python
class Multiply:
    def __init__(self):
        pass
    def __call__(self, a, b):
        return a * b

multiply = Multiply()
print multiply(2, 4)    # prints 8

```

### python_code_5.txt
```python
def (multiply a b)
  a*b

```

### python_code_6.txt
```python
(multiply 3 4)
=> 12

```

### python_code_7.txt
```python
(multiply 3 :a 4)  # arg order doesn't matter here, but try subtract instead
=> 12

```

### python_code_8.txt
```python
def (multiply a b|by)
  (* a b)

```

### python_code_9.txt
```python
multiply 3 :by 4
=> 12

```

