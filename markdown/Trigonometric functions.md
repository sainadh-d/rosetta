# Trigonometric functions

## Task Link
[Rosetta Code - Trigonometric functions](https://rosettacode.org/wiki/Trigonometric_functions)

## Java Code
### java_code_1.txt
```java
public class Trig {
        public static void main(String[] args) {
                //Pi / 4 is 45 degrees. All answers should be the same.
                double radians = Math.PI / 4;
                double degrees = 45.0;
                //sine
                System.out.println(Math.sin(radians) + " " + Math.sin(Math.toRadians(degrees)));
                //cosine
                System.out.println(Math.cos(radians) + " " + Math.cos(Math.toRadians(degrees)));
                //tangent
                System.out.println(Math.tan(radians) + " " + Math.tan(Math.toRadians(degrees)));
                //arcsine
                double arcsin = Math.asin(Math.sin(radians));
                System.out.println(arcsin + " " + Math.toDegrees(arcsin));
                //arccosine
                double arccos = Math.acos(Math.cos(radians));
                System.out.println(arccos + " " + Math.toDegrees(arccos));
                //arctangent
                double arctan = Math.atan(Math.tan(radians));
                System.out.println(arctan + " " + Math.toDegrees(arctan));
        }
}

```

## Python Code
### python_code_1.txt
```python
Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from math import degrees, radians, sin, cos, tan, asin, acos, atan, pi
>>> rad, deg = pi/4, 45.0
>>> print("Sine:", sin(rad), sin(radians(deg)))
Sine: 0.7071067811865475 0.7071067811865475
>>> print("Cosine:", cos(rad), cos(radians(deg)))
Cosine: 0.7071067811865476 0.7071067811865476
>>> print("Tangent:", tan(rad), tan(radians(deg)))
Tangent: 0.9999999999999999 0.9999999999999999
>>> arcsine = asin(sin(rad))
>>> print("Arcsine:", arcsine, degrees(arcsine))
Arcsine: 0.7853981633974482 44.99999999999999
>>> arccosine = acos(cos(rad))
>>> print("Arccosine:", arccosine, degrees(arccosine))
Arccosine: 0.7853981633974483 45.0
>>> arctangent = atan(tan(rad))
>>> print("Arctangent:", arctangent, degrees(arctangent))
Arctangent: 0.7853981633974483 45.0
>>>

```

