# Koch curve

## Task Link
[Rosetta Code - Koch curve](https://rosettacode.org/wiki/Koch_curve)

## Java Code
### java_code_1.txt
```java
import java.awt.Point;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public final class KochCurve {
	
    public static void main(String[] aArgs) throws IOException {    	
    	List<Point> points = initialEquilateralTriangle();
    	for ( int i = 1; i < 5; i++ ) {
    		points = nextIteration(points);
    	}    	
    	
    	String text = kochCurveText(points, IMAGE_SIZE);    
    	Files.write(Paths.get("C:/Users/psnow/Desktop/koch.svg"), text.getBytes());
    }
    
    private static List<Point> initialEquilateralTriangle() {
    	final int margin = 50;
    	final int boxSize = IMAGE_SIZE - margin;
    	final int sideLength = Math.round(boxSize * SIN_60_DEGREES);
    	final int x = ( boxSize + margin - sideLength ) / 2;
    	final int y = Math.round(( boxSize + margin ) / 2 - sideLength * SIN_60_DEGREES / 3);
    	
    	List<Point> points = Arrays.asList(
                new Point(x, y),
                new Point(x + sideLength / 2, Math.round(y + sideLength * SIN_60_DEGREES)),
                new Point(x + sideLength, y),
                new Point(x, y)
            );
    	
    	return points;    	
    }
    
    private static List<Point> nextIteration(List<Point> aPoints) {
        List<Point> result = new ArrayList<Point>();
        
        for ( int i = 0; i < aPoints.size() - 1; i++ ) {
        	final int x0 = aPoints.get(i).x;
            final int y0 = aPoints.get(i).y;
            final int x1 = aPoints.get(i + 1).x;
            final int y1 = aPoints.get(i + 1).y;
            final int dy = y1 - y0;
            final int dx = x1 - x0;
            
            result.add(aPoints.get(i));
            result.add( new Point(x0 + dx / 3, y0 + dy / 3) );
            result.add( new Point(Math.round(x0 + dx / 2 - dy * SIN_60_DEGREES / 3),
            					  Math.round(y0 + dy / 2 + dx * SIN_60_DEGREES / 3)) );
            result.add( new Point(x0 + 2 * dx / 3, y0 + 2 * dy / 3) ) ;
        }
        
        result.add(aPoints.get(aPoints.size() - 1));        
        return result;
    }
    
    private static String kochCurveText(List<Point> aPoints, int aSize) {
    	StringBuilder text = new StringBuilder();
        text.append("<svg xmlns='http://www.w3.org/2000/svg'");
        text.append(" width='" + aSize + "' height='" + aSize + "'>\n");
        text.append("<rect style='width:100%;height:100%;fill:cyan'/>\n");
        text.append("<polygon points='");
        for ( int i = 0; i < aPoints.size(); i++ ) {
            text.append(aPoints.get(i).x + ", " + aPoints.get(i).y + " ");
        }
        text.append("' style='fill:pink;stroke:black;stroke-width:2'/>\n</svg>\n");
        
        return text.toString();
    }
    
    private static final int IMAGE_SIZE = 700;  
    private static final float SIN_60_DEGREES = (float) Math.sin(Math.PI / 3.0);
  
}

```

### java_code_2.txt
```java
int l = 300;

void setup() {
  size(400, 400);
  background(0, 0, 255);
  stroke(255);
  // draw from center of screen
  translate(width/2.0, height/2.0);
  // center curve from lower-left corner of base equilateral triangle
  translate(-l/2.0, l*sqrt(3)/6.0);
  for (int i = 1; i <= 3; i++) {
    kcurve(0, l);
    rotate(radians(120));
    translate(-l, 0);
  }
}

void kcurve(float x1, float x2) {
  float s = (x2-x1)/3;
  if (s < 5) {
    pushMatrix();
    translate(x1, 0);
    line(0, 0, s, 0);
    line(2*s, 0, 3*s, 0);
    translate(s, 0);
    rotate(radians(60));
    line(0, 0, s, 0);
    translate(s, 0);
    rotate(radians(-120));
    line(0, 0, s, 0);
    popMatrix();
    return;
  }
  pushMatrix();
  translate(x1, 0);
  kcurve(0, s);
  kcurve(2*s, 3*s);
  translate(s, 0);
  rotate(radians(60));
  kcurve(0, s);
  translate(s, 0);
  rotate(radians(-120));
  kcurve(0, s);
  popMatrix();
}

```

## Python Code
### python_code_1.txt
```python
l = 300

def setup():
    size(400, 400)
    background(0, 0, 255)
    stroke(255)
    # draw from center of screen
    translate(width / 2.0, height / 2.0)
    # center curve from lower - left corner of base equilateral triangle
    translate(-l / 2.0, l * sqrt(3) / 6.0)
    for i in range(4):
        kcurve(0, l)
        rotate(radians(120))
        translate(-l, 0)


def kcurve(x1, x2):
    s = (x2 - x1) / 3.0
    if s < 5:
        pushMatrix()
        translate(x1, 0)
        line(0, 0, s, 0)
        line(2 * s, 0, 3 * s, 0)
        translate(s, 0)
        rotate(radians(60))
        line(0, 0, s, 0)
        translate(s, 0)
        rotate(radians(-120))
        line(0, 0, s, 0)
        popMatrix()
        return

    pushMatrix()
    translate(x1, 0)
    kcurve(0, s)
    kcurve(2 * s, 3 * s)
    translate(s, 0)
    rotate(radians(60))
    kcurve(0, s)
    translate(s, 0)
    rotate(radians(-120))
    kcurve(0, s)
    popMatrix()

```

### python_code_2.txt
```python
'''Koch curve'''

from math import cos, pi, sin
from operator import add, sub
from itertools import chain


# kochSnowflake :: Int -> (Float, Float) -> (Float, Float) -> [(Float, Float)]
def kochSnowflake(n, a, b):
    '''List of points on a Koch snowflake of order n, derived
       from an equilateral triangle with base a b.
    '''
    points = [a, equilateralApex(a, b), b]
    return chain.from_iterable(map(
        kochCurve(n),
        points,
        points[1:] + [points[0]]
    ))


# kochCurve :: Int -> (Float, Float) -> (Float, Float)
#                  -> [(Float, Float)]
def kochCurve(n):
    '''List of points on a Koch curve of order n,
       starting at point ab, and ending at point xy.
    '''
    def koch(n):
        def goTuple(abxy):
            ab, xy = abxy
            if 0 == n:
                return [xy]
            else:
                mp, mq = midThirdOfLine(ab, xy)
                points = [
                    ab,
                    mp,
                    equilateralApex(mp, mq),
                    mq,
                    xy
                ]
                return list(
                    chain.from_iterable(map(
                        koch(n - 1),
                        zip(points, points[1:])
                    ))
                )
        return goTuple

    def go(ab, xy):
        return [ab] + koch(n)((ab, xy))
    return go


# equilateralApex :: (Float, Float) -> (Float, Float) -> (Float, Float)
def equilateralApex(p, q):
    '''Apex of triangle with base p q.
    '''
    return rotatedPoint(pi / 3)(p, q)


# rotatedPoint :: Float -> (Float, Float) ->
#                (Float, Float) -> (Float, Float)
def rotatedPoint(theta):
    '''The point ab rotated theta radians
        around the origin xy.
    '''
    def go(xy, ab):
        ox, oy = xy
        a, b = ab
        dx, dy = rotatedVector(theta, (a - ox, oy - b))
        return ox + dx, oy - dy
    return go


# rotatedVector :: Float -> (Float, Float) -> (Float, Float)
def rotatedVector(theta, xy):
    '''The vector xy rotated by theta radians.
    '''
    x, y = xy
    return (
        x * cos(theta) - y * sin(theta),
        x * sin(theta) + y * cos(theta)
    )


# midThirdOfLine :: (Float, Float) -> (Float, Float)
#                -> ((Float, Float), (Float, Float))
def midThirdOfLine(ab, xy):
    '''Second of three equal segments of
       the line between ab and xy.
    '''
    vector = [x / 3 for x in map(sub, xy, ab)]

    def f(p):
        return tuple(map(add, vector, p))
    p = f(ab)
    return (p, f(p))


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''SVG for Koch snowflake of order 4.
    '''
    print(
        svgFromPoints(1024)(
            kochSnowflake(
                4, (200, 600), (800, 600)
            )
        )
    )


# -------------------------- SVG ---------------------------

# svgFromPoints :: Int -> [(Float, Float)] -> SVG String
def svgFromPoints(w):
    '''Width of square canvas -> Point list -> SVG string.
    '''
    def go(xys):
        xs = ' '.join(map(
            lambda xy: str(round(xy[0], 2)) + ' ' + str(round(xy[1], 2)),
            xys
        ))
        return '\n'.join([
            '<svg xmlns="http://www.w3.org/2000/svg"',
            f'width="512" height="512" viewBox="5 5 {w} {w}">',
            f'<path d="M{xs}" ',
            'stroke-width="2" stroke="red" fill="transparent"/>',
            '</svg>'
        ])
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb as hsv

def curve(axiom, rules, angle, depth):
    for _ in range(depth):
        axiom = ''.join(rules[c] if c in rules else c for c in axiom)

    a, x, y = 0, [0], [0]
    for c in axiom:
        match c:
            case '+':
                a += 1
            case '-':
                a -= 1
            case 'F' | 'G':
                x.append(x[-1] + np.cos(a*angle*np.pi/180))
                y.append(y[-1] + np.sin(a*angle*np.pi/180))

    l = len(x)
    # this is very slow, but pretty colors
    for i in range(l - 1):
        plt.plot(x[i:i+2], y[i:i+2], color=hsv([i/l, 1, .7]))
    plt.gca().set_aspect(1)
    plt.show()

curve('F++F++F', {'F': 'F+F--F+F'}, 60, 5)
#curve('F--XF--F--XF', {'X': 'XF+G+XF--F--XF+G+X'}, 45, 5)
#curve('F+XF+F+XF', {'X': 'XF-F+F-XF+F+XF-F+F-X'}, 90, 5)
#curve('F', {'F': 'G-F-G', 'G': 'F+G+F'}, 60, 7)
#curve('A', {'A': '+BF-AFA-FB+', 'B': '-AF+BFB+FA-'}, 90, 6)
#curve('FX+FX+', {'X': 'X+YF', 'Y': 'FX-Y'}, 90, 12)

```

