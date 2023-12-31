# Define a primitive data type

## Task Link
[Rosetta Code - Define a primitive data type](https://rosettacode.org/wiki/Define_a_primitive_data_type)

## Java Code
### java_code_1.txt
```java
class BoundedIntOutOfBoundsException extends Exception
{
  public BoundedIntOutOfBoundsException(int v, int l, int u) {
    super("value " + v + " is out of bounds [" + l + "," + u + "]");
  }
}

class BoundedInt {
  private int value;
  private int lower;
  private int upper;

  public BoundedInt(int l, int u) {
    lower = Math.min(l, u);
    upper = Math.max(l, u);
  }

  private boolean checkBounds(int v) {
    return (v >= this.lower) && (v <= this.upper);
  }

  public void assign(BoundedInt i) throws BoundedIntOutOfBoundsException {{
    assign(i.value()); //could still throw Exception if the other BoundedInt has different bounds
  }

  public void assign(int v) throws BoundedIntOutOfBoundsException {
    if ( checkBounds(v) ) {
      this.value = v;
    } else {
      throw new BoundedIntOutOfBoundsException(v, this.lower, this.upper);
    }
  }

  public int add(BoundedInt i) throws BoundedIntOutOfBoundsException {
    return add(i.value());
  }

  public int add(int i) throws BoundedIntOutOfBoundsException {
    if ( checkBounds(this.value + i) ) {
      this.value += i;
    }  else {
      throw new BoundedIntOutOfBoundsException(this.value + i, this.lower, this.upper);
    }
    return this.value;
  }

  public int value() {
    return this.value;
  }
}


public class Bounded {
  public static void main(String[] args) throws BoundedIntOutOfBoundsException {
    BoundedInt a = new BoundedInt(1, 10);
    BoundedInt b = new BoundedInt(1, 10);

    a.assign(6);
    try {
      b.assign(12);
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
    b.assign(9);
    try {
      a.add(b.value());
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> class num(int):
    def __init__(self, b):
        if 1 <= b <= 10:
            return int.__init__(self+0)
        else:
            raise ValueError,"Value %s should be >=0 and <= 10" % b

        
>>> x = num(3)
>>> x = num(11)

Traceback (most recent call last):
  File "<pyshell#394>", line 1, in <module>
    x = num(11)
  File "<pyshell#392>", line 6, in __init__
    raise ValueError,"Value %s should be >=0 and <= 10" % b
ValueError: Value 11 should be >=0 and <= 10
>>> x
3
>>> type(x)
<class '__main__.num'>
>>>

```

