# Sierpinski arrowhead curve

## Task Link
[Rosetta Code - Sierpinski arrowhead curve](https://rosettacode.org/wiki/Sierpinski_arrowhead_curve)

## Java Code
### java_code_1.txt
```java
import java.awt.Point;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public final class SierpinskiArrowhead {

	public static void main(String[] aArgs) throws IOException {
		List<Point> points = initialStraightLine();
    	for ( int i = 1; i < 8; i++ ) {
    		points = nextIteration(points);
    	}    	
    	
    	String text = sierpinskiArrowheadText(points, IMAGE_SIZE);    
    	Files.write(Paths.get("sierpinkskiArrowhead.svg"), text.getBytes());
	}
	
	private static List<Point> initialStraightLine() {
		final int margin = 50;
	    final int boxSize = IMAGE_SIZE - 2 * margin;
	    final int x = margin;
	    final int y = Math.round(( IMAGE_SIZE + SQRT3_2 * boxSize ) / 2.0F);
	    
	    List<Point> points = Arrays.asList( new Point(x, y), new Point(x + boxSize, y) );
	    return points;
	}
	
	private static List<Point> nextIteration(List<Point> aPoints) {
		List<Point> result = new ArrayList<Point>();
		
	    for ( int i = 0; i < aPoints.size() - 1; i++ ) {
	        final int x0 = aPoints.get(i).x;
	        final int y0 = aPoints.get(i).y;
	        final int x1 = aPoints.get(i + 1).x;
	        final int y1 = aPoints.get(i + 1).y;
	        final int dx = x1 - x0;
	        result.add( new Point(x0, y0) );
	        
	        if ( y0 == y1 ) {
	            final float d = Math.abs(dx) * SQRT3_2 / 2;
	            result.add( new Point(x0 + dx / 4, Math.round(y0 - d)) );
	            result.add( new Point(x1 - dx / 4, Math.round(y0 - d)) );
	        } else if ( y1 < y0 ) {
	        	result.add( new Point(x1, y0));
	        	result.add( new Point(x1 + dx / 2, ( y0 + y1 ) / 2) );
	        } else {
	        	result.add( new Point(x0 - dx / 2, ( y0 + y1 ) / 2) );
	        	result.add( new Point(x0, y1) );
	        }
	    }
	    
	    result.add(aPoints.get(aPoints.size() - 1)); 
	    return result;
	}
	
	private static String sierpinskiArrowheadText(List<Point> aPoints, int aSize) {
    	StringBuilder text = new StringBuilder();    	
    	text.append("<svg xmlns='http://www.w3.org/2000/svg'");
        text.append(" width='" + aSize + "' height='" + aSize + "'>\n");
        text.append("<rect width='100%' height='100%' fill='white'/>\n");
        text.append("<path stroke-width='1' stroke='black' fill='white' d='");
        for ( int i = 0; i < aPoints.size(); i++ ) {
        	text.append(( i == 0 ? "M" : "L" ) + aPoints.get(i).x + ", " + aPoints.get(i).y + " ");
        }
        text.append("'/>\n</svg>\n");
            	
        return text.toString();
    }
	
	private static final float SQRT3_2 = (float) Math.sqrt(3.0F) / 2.0F;
	private static final int IMAGE_SIZE = 700;

}

```

### java_code_2.txt
```java
final PVector t = new PVector(20, 30, 60);

void setup() {
  size(450, 400);
  noLoop();
  background(0, 0, 200);
  stroke(-1);
  sc(7, 400, -60, t);
}

PVector sc(int o, float l, final int a, final PVector s) {
  if (o > 0) {
    sc(--o, l *= .5, -a, s).z += a;
    sc(o, l, a, s).z += a;
    sc(o, l, -a, s);
  } else line(s.x, s.y, 
    s.x += cos(radians(s.z)) * l, 
    s.y += sin(radians(s.z)) * l);
  return s;
}

```

## Python Code
### python_code_1.txt
```python
t = { 'x': 20, 'y': 30, 'a': 60 }

def setup():
    size(450, 400)
    background(0, 0, 200)
    stroke(-1)
    sc(7, 400, -60)

def sc(o, l, a, s = t, X = 'x', Y = 'y', A = 'a', HALF = .5):
    if o:
        o -= 1
        l *= HALF
        sc(o, l, -a)[A] += a
        sc(o, l, a)[A] += a
        sc(o, l, -a)
    else:
        x, y = s[X], s[Y]
        s[X] += cos(radians(s[A])) * l
        s[Y] += sin(radians(s[A])) * l
        line(x, y, s[X], s[Y])

    return s

```

### python_code_2.txt
```python
import matplotlib.pyplot as plt
import math


def nextPoint(x, y, angle):
    a = math.pi * angle / 180
    x2 = (int)(round(x + (1 * math.cos(a))))
    y2 = (int)(round(y + (1 * math.sin(a))))
    return x2, y2


def expand(axiom, rules, level):
    for l in range(0, level):
        a2 = ""
        for c in axiom:
            if c in rules:
                a2 += rules[c]
            else:
                a2 += c
        axiom = a2
    return axiom


def draw_lsystem(axiom, rules, angle, iterations):
    xp = [1]
    yp = [1]
    direction = 0
    for c in expand(axiom, rules, iterations):
        if c == "F":
            xn, yn = nextPoint(xp[-1], yp[-1], direction)
            xp.append(xn)
            yp.append(yn)
        elif c == "-":
            direction = direction - angle
            if direction < 0:
                direction = 360 + direction
        elif c == "+":
            direction = (direction + angle) % 360

    plt.plot(xp, yp)
    plt.show()


if __name__ == '__main__':
    # Sierpinski Arrowhead Curve L-System Definition
    s_axiom = "XF"
    s_rules = {"X": "YF+XF+Y",
               "Y": "XF-YF-X"}
    s_angle = 60

    draw_lsystem(s_axiom, s_rules, s_angle, 7)

```

