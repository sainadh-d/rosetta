# Compound data type

## Task Link
[Rosetta Code - Compound data type](https://rosettacode.org/wiki/Compound_data_type)

## Java Code
### java_code_1.txt
```java
record Point(int x, int y) { }

```

### java_code_2.txt
```java
Point point = new Point(1, 2);
int x = point.x;
int y = point.y;

```

### java_code_3.txt
```java
public class Point
{
  public int x, y;
  public Point() { this(0); }
  public Point(int x0) { this(x0,0); }
  public Point(int x0, int y0) { x = x0; y = y0; }

  public static void main(String args[])
  {
    Point point = new Point(1,2);
    System.out.println("x = " + point.x );
    System.out.println("y = " + point.y );
  }
}

```

## Python Code
### python_code_1.txt
```python
X, Y = 0, 1
p = (3, 4)
p = [3, 4]

print p[X]

```

### python_code_2.txt
```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point()
print p.x

```

### python_code_3.txt
```python
class MyObject(object): pass
point = MyObject()
point.x, point.y = 0, 1
# objects directly instantiated from "object()"  cannot be "monkey patched"
# however this can generally be done to it's subclasses

```

### python_code_4.txt
```python
pseudo_object = {'x': 1, 'y': 2}

```

### python_code_5.txt
```python
>>> from collections import namedtuple
>>> help(namedtuple)
Help on function namedtuple in module collections:

namedtuple(typename, field_names, verbose=False)
    Returns a new subclass of tuple with named fields.
    
    >>> Point = namedtuple('Point', 'x y')
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessable by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

>>>

```

