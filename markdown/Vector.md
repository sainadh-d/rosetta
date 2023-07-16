# Vector

## Task Link
[Rosetta Code - Vector](https://rosettacode.org/wiki/Vector)

## Java Code
### java_code_1.txt
```java
import java.util.Locale;

public class Test {

    public static void main(String[] args) {
        System.out.println(new Vec2(5, 7).add(new Vec2(2, 3)));
        System.out.println(new Vec2(5, 7).sub(new Vec2(2, 3)));
        System.out.println(new Vec2(5, 7).mult(11));
        System.out.println(new Vec2(5, 7).div(2));
    }
}

class Vec2 {
    final double x, y;

    Vec2(double x, double y) {
        this.x = x;
        this.y = y;
    }

    Vec2 add(Vec2 v) {
        return new Vec2(x + v.x, y + v.y);
    }

    Vec2 sub(Vec2 v) {
        return new Vec2(x - v.x, y - v.y);
    }

    Vec2 div(double val) {
        return new Vec2(x / val, y / val);
    }

    Vec2 mult(double val) {
        return new Vec2(x * val, y * val);
    }

    @Override
    public String toString() {
        return String.format(Locale.US, "[%s, %s]", x, y);
    }
}

```

### java_code_2.txt
```java
PVector v1 = new PVector(5, 7);
PVector v2 = new PVector(2, 3);

println(v1.x, v1.y, v1.mag(), v1.heading(),'\n');

// static methods
println(PVector.add(v1, v2));
println(PVector.sub(v1, v2));
println(PVector.mult(v1, 11));
println(PVector.div(v1, 2), '\n');

// object methods
println(v1.sub(v1));
println(v1.add(v2));
println(v1.mult(10));
println(v1.div(10));

```

## Python Code
### python_code_1.txt
```python
v1 = PVector(5, 7)
v2 = PVector(2, 3)

println('{} {} {} {}\n'.format( v1.x, v1.y, v1.mag(), v1.heading()))

# math overloaded operators (static methods in the comments)
println(v1 + v2) # PVector.add(v1, v2)
println(v1 - v2) # PVector.sub(v1, v2)
println(v1 * 11) # PVector.mult(v1, 11)
println(v1 / 2)  # PVector.div(v1, 2)
println('')

# object methods (related augmented assigment in the comments)
println(v1.sub(v1))  # v1 -= v1; println(v1)
println(v1.add(v2))  # v1 += v2; println(v2)
println(v1.mult(10)) # v1 *= 10; println(v1)
println(v1.div(10))  # v1 /= 10; println(v1)

```

### python_code_2.txt
```python
class Vector:
    def __init__(self,m,value):
        self.m = m
        self.value = value
        self.angle = math.degrees(math.atan(self.m))
        self.x = self.value * math.sin(math.radians(self.angle))
        self.y = self.value * math.cos(math.radians(self.angle))

    def __add__(self,vector):
        """
        >>> Vector(1,10) + Vector(1,2)
        Vector:
            - Angular coefficient: 1.0
            - Angle: 45.0 degrees
            - Value: 12.0
            - X component: 8.49
            - Y component: 8.49
        """
        final_x = self.x + vector.x
        final_y = self.y + vector.y
        final_value = pytagoras(final_x,final_y)
        final_m = final_y / final_x
        return Vector(final_m,final_value)

    def __neg__(self):
        return Vector(self.m,-self.value)

    def __sub__(self,vector):
        return self + (- vector)
        
    def __mul__(self,scalar):
        """
        >>> Vector(4,5) * 2
        Vector:
            - Angular coefficient: 4
            - Angle: 75.96 degrees
            - Value: 10
            - X component: 9.7
            - Y component: 2.43

        """
        return Vector(self.m,self.value*scalar)

    def __div__(self,scalar):
        return self * (1 / scalar)
    
    def __repr__(self):
        """
        Returns a nicely formatted list of the properties of the Vector.

        >>> Vector(1,10)
        Vector:
            - Angular coefficient: 1
            - Angle: 45.0 degrees
            - Value: 10
            - X component: 7.07
            - Y component: 7.07
        
        """
        return """Vector:
    - Angular coefficient: {}
    - Angle: {} degrees
    - Value: {}
    - X component: {}
    - Y component: {}""".format(self.m.__round__(2),
               self.angle.__round__(2),
               self.value.__round__(2),
               self.x.__round__(2),
               self.y.__round__(2))

```

### python_code_3.txt
```python
from __future__ import annotations
import math
from functools import lru_cache
from typing import NamedTuple

CACHE_SIZE = None


def hypotenuse(leg: float,
               other_leg: float) -> float:
    """Returns hypotenuse for given legs"""
    return math.sqrt(leg ** 2 + other_leg ** 2)


class Vector(NamedTuple):
    slope: float
    length: float

    @property
    @lru_cache(CACHE_SIZE)
    def angle(self) -> float:
        return math.atan(self.slope)

    @property
    @lru_cache(CACHE_SIZE)
    def x(self) -> float:
        return self.length * math.sin(self.angle)

    @property
    @lru_cache(CACHE_SIZE)
    def y(self) -> float:
        return self.length * math.cos(self.angle)
 
    def __add__(self, other: Vector) -> Vector:
        """Returns self + other"""
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_length = hypotenuse(new_x, new_y)
        new_slope = new_y / new_x
        return Vector(new_slope, new_length)
 
    def __neg__(self) -> Vector:
        """Returns -self"""
        return Vector(self.slope, -self.length)
 
    def __sub__(self, other: Vector) -> Vector:
        """Returns self - other"""
        return self + (-other)
 
    def __mul__(self, scalar: float) -> Vector:
        """Returns self * scalar"""
        return Vector(self.slope, self.length * scalar)
 
    def __truediv__(self, scalar: float) -> Vector:
        """Returns self / scalar"""
        return self * (1 / scalar)


if __name__ == '__main__':
    v1 = Vector(1, 1)

    print("Pretty print:")
    print(v1, end='\n' * 2)

    print("Addition:")
    v2 = v1 + v1
    print(v1 + v1, end='\n' * 2)

    print("Subtraction:")
    print(v2 - v1, end='\n' * 2)

    print("Multiplication:")
    print(v1 * 2, end='\n' * 2)

    print("Division:")
    print(v2 / 2)

```

