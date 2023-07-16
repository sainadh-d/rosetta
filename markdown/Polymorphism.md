# Polymorphism

## Task Link
[Rosetta Code - Polymorphism](https://rosettacode.org/wiki/Polymorphism)

## Java Code
### java_code_1.txt
```java
class Point {
   protected int x, y;
   public Point() { this(0); }
   public Point(int x) { this(x, 0); }
   public Point(int x, int y) { this.x = x; this.y = y; }
   public Point(Point p) { this(p.x, p.y); }
   public int getX() { return this.x; }
   public int getY() { return this.y; }
   public void setX(int x) { this.x = x; }
   public void setY(int y) { this.y = y; }
   public void print() { System.out.println("Point x: " + this.x + " y: " + this.y); }
}

class Circle extends Point {
   private int r;
   public Circle(Point p) { this(p, 0); }
   public Circle(Point p, int r) { super(p); this.r = r; }
   public Circle() { this(0); }
   public Circle(int x) { this(x, 0); }
   public Circle(int x, int y) { this(x, y, 0); }
   public Circle(int x, int y, int r) { super(x, y); this.r = r; }
   public Circle(Circle c) { this(c.x, c.y, c.r); }
   public int getR() { return this.r; }
   public void setR(int r) { this.r = r; }
   public void print() { System.out.println("Circle x: " + this.x + " y: " + this.y + " r: " + this.r); }
}

public class test {
  public static void main(String args[]) {
    Point p = new Point();
    Point c = new Circle();
    p.print();
    c.print();     
  }
}

```

## Python Code
### python_code_1.txt
```python
class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __repr__(self):
        return '<Point 0x%x x: %f y: %f>' % (id(self), self.x, self.y)

class Circle(object):
    def __init__(self, center=None, radius=1.0):
        self.center = center or Point()
        self.radius = radius
    def __repr__(self):
        return '<Circle 0x%x x: %f y: %f radius: %f>' % (
            id(self), self.center.x, self.center.y, self.radius)

```

### python_code_2.txt
```python
class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __repr__(self):
        return '<Point 0x%x x: %f y: %f>' % (id(self), self.x, self.y)

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, radius=1.0):
        Point.__init__(self, x, y)
        self.radius = radius
    def __repr__(self):
        return '<Circle 0x%x x: %f y: %f radius: %f>' % (
            id(self), self.x, self.y, self.radius)

```

### python_code_3.txt
```python
>>> from collections import namedtuple
>>> class Point(namedtuple('Point', 'x y')):
	def __new__( _cls, x=0, y=0 ):
		return super().__new__(_cls, x, y)

	
>>> class Circle(namedtuple('Circle', 'x y r')):
	def __new__( _cls, x=0, y=0, r=0 ):
		return super().__new__(_cls, x, y, r)

	
>>> Point(), Point(x=1), Point(y=2), Point(3, 4)
(Point(x=0, y=0), Point(x=1, y=0), Point(x=0, y=2), Point(x=3, y=4))
>>> Circle(), Circle(r=2), Circle(1, 2, 3)
(Circle(x=0, y=0, r=0), Circle(x=0, y=0, r=2), Circle(x=1, y=2, r=3))
>>> p = Point(1.25, 3.87)
>>> p
Point(x=1.25, y=3.87)
>>> p.x = 10.81
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    p.x = 10.81
AttributeError: can't set attribute
>>>

```

### python_code_4.txt
```python
>>> Point = namedtuple('Point', 'x y')
>>> Circle = namedtuple('Circle', 'x y r')
>>> Point(3, 4)
Point(x=3, y=4)
>>> Circle(x=1, y=2, r=3)
Circle(x=1, y=2, r=3)
>>>

```

