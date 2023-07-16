# Angle difference between two bearings

## Task Link
[Rosetta Code - Angle difference between two bearings](https://rosettacode.org/wiki/Angle_difference_between_two_bearings)

## Java Code
### java_code_1.txt
```java
public class AngleDifference {

    public static double getDifference(double b1, double b2) {
        double r = (b2 - b1) % 360.0;
        if (r < -180.0)
            r += 360.0;
        if (r >= 180.0)
            r -= 360.0;
        return r;
    }

    public static void main(String[] args) {
        System.out.println("Input in -180 to +180 range");
        System.out.println(getDifference(20.0, 45.0));
        System.out.println(getDifference(-45.0, 45.0));
        System.out.println(getDifference(-85.0, 90.0));
        System.out.println(getDifference(-95.0, 90.0));
        System.out.println(getDifference(-45.0, 125.0));
        System.out.println(getDifference(-45.0, 145.0));
        System.out.println(getDifference(-45.0, 125.0));
        System.out.println(getDifference(-45.0, 145.0));
        System.out.println(getDifference(29.4803, -88.6381));
        System.out.println(getDifference(-78.3251, -159.036));

        System.out.println("Input in wider range");
        System.out.println(getDifference(-70099.74233810938, 29840.67437876723));
        System.out.println(getDifference(-165313.6666297357, 33693.9894517456));
        System.out.println(getDifference(1174.8380510598456, -154146.66490124757));
        System.out.println(getDifference(60175.77306795546, 42213.07192354373));
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
 
def getDifference(b1, b2):
	r = (b2 - b1) % 360.0
	# Python modulus has same sign as divisor, which is positive here,
	# so no need to consider negative case
	if r >= 180.0:
		r -= 360.0
	return r
 
if __name__ == "__main__":
	print ("Input in -180 to +180 range")
	print (getDifference(20.0, 45.0))
	print (getDifference(-45.0, 45.0))
	print (getDifference(-85.0, 90.0))
	print (getDifference(-95.0, 90.0))
	print (getDifference(-45.0, 125.0))
	print (getDifference(-45.0, 145.0))
	print (getDifference(-45.0, 125.0))
	print (getDifference(-45.0, 145.0))
	print (getDifference(29.4803, -88.6381))
	print (getDifference(-78.3251, -159.036))
 
	print ("Input in wider range")
	print (getDifference(-70099.74233810938, 29840.67437876723))
	print (getDifference(-165313.6666297357, 33693.9894517456))
	print (getDifference(1174.8380510598456, -154146.66490124757))
	print (getDifference(60175.77306795546, 42213.07192354373))

```

### python_code_2.txt
```python
'''Difference between two bearings'''

from math import (acos, cos, pi, sin)


# bearingDelta :: Radians -> Radians -> Radians
def bearingDelta(ar):
    '''Difference between two bearings,
       expressed in radians.'''
    def go(br):
        [(ax, ay), (bx, by)] = [
            (sin(x), cos(x)) for x in [ar, br]
        ]
        # cross-product > 0 ?
        sign = +1 if 0 < ((ay * bx) - (by * ax)) else -1
        # sign * dot-product
        return sign * acos((ax * bx) + (ay * by))
    return lambda br: go(br)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test and display'''

    # showMap :: Degrees -> Degrees -> String
    def showMap(da, db):
        return unwords(
            str(x).rjust(n) for n, x in
            [
                (22, str(da) + ' +'),
                (24, str(db) + '  -> '),
                (7, round(
                    degrees(
                        bearingDelta
                        (radians(da))
                        (radians(db))
                    ), 2)
                 )
            ]
        )

    print(__doc__ + ':')
    print(
        unlines(showMap(a, b) for a, b in [
            (20, 45),
            (-45, 45),
            (-85, 90),
            (-95, 90),
            (-45, 125),
            (-45, 145),
            (-70099.74233810938, 29840.67437876723),
            (-165313.6666297357, 33693.9894517456),
            (1174.8380510598456, -154146.66490124757),
            (60175.77306795546, 42213.07192354373)
        ]))


# GENERIC ----------------------------------------------


# radians :: Float x => Degrees x -> Radians x
def radians(x):
    '''Radians derived from degrees.'''
    return pi * x / 180


# degrees :: Float x => Radians x -> Degrees x
def degrees(x):
    '''Degrees derived from radians.'''
    return 180 * x / pi


# unlines :: [String] -> String
def unlines(xs):
    '''A single newline-delimited string derived
       from a list of strings.'''
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from
       a list of words.'''
    return ' '.join(xs)


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
"""
Difference between two bearings
"""

def  delta_bearing(b1 , b2):
	return ((b2-b1+540)%360)-180

dataSet = [[20, 45], [-45, 45], [-85, 90], [-95, 90], [-45, 125], [-45, 145], \
	[29.4803, -88.6381], [-78.3251, -159.036], \
	[-70099.74233810938, 29840.67437876723], \
	[-165313.6666297357, 33693.9894517456], \
	[1174.8380510598456, -154146.66490124757], \
	[60175.77306795546, 42213.07192354373]]

print('.{:-^19}.{:-^19}.{:-^9}.' .format(" b1 ", " b2 ", " Δ b " ))
for Δ in dataSet: 
	print('|{: > 19}|{: > 19}|{: > 9.4f}|' .format(Δ[0], Δ[1],delta_bearing(Δ[0],Δ[1])))

```

