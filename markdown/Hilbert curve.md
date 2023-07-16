# Hilbert curve

## Task Link
[Rosetta Code - Hilbert curve](https://rosettacode.org/wiki/Hilbert_curve)

## Java Code
### java_code_1.txt
```java
// Translation from https://en.wikipedia.org/wiki/Hilbert_curve

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class HilbertCurve {
    public static class Point {
        public int x;
        public int y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
        
        //rotate/flip a quadrant appropriately
        public void rot(int n, boolean rx, boolean ry) {
            if (!ry) {
                if (rx) {
                    x = (n - 1) - x;
                    y = (n - 1) - y;
                }
        
                //Swap x and y
                int t  = x;
                x = y;
                y = t;
            }
            
            return;
        }
        
        public int calcD(int n) {
            boolean rx, ry;
            int d = 0;
            for (int s = n >>> 1; s > 0; s >>>= 1) {
                rx = ((x & s) != 0);
                ry = ((y & s) != 0);
                d += s * s * ((rx ? 3 : 0) ^ (ry ? 1 : 0));
                rot(s, rx, ry);
            }
            
            return d;
        }
        
    }

    public static Point fromD(int n, int d) {
        Point p = new Point(0, 0);
        boolean rx, ry;
        int t = d;
        for (int s = 1; s < n; s <<= 1) {
            rx = ((t & 2) != 0);
            ry = (((t ^ (rx ? 1 : 0)) & 1) != 0);
            p.rot(s, rx, ry);
            p.x += (rx ? s : 0);
            p.y += (ry ? s : 0);
            t >>>= 2;
        }
        return p;
    }
    
    public static List<Point> getPointsForCurve(int n) {
        List<Point> points = new ArrayList<Point>();
        for (int d = 0; d < (n * n); d++) {
            Point p = fromD(n, d);
            points.add(p);
        }
        
        return points;
    }
    
    public static List<String> drawCurve(List<Point> points, int n) {
        char[][] canvas = new char[n][n * 3 - 2];
        for (char[] line : canvas) {
            Arrays.fill(line, ' ');
        }
        for (int i = 1; i < points.size(); i++) {
             Point lastPoint = points.get(i - 1);
            Point curPoint = points.get(i);
            int deltaX = curPoint.x - lastPoint.x;
            int deltaY = curPoint.y - lastPoint.y;
            if (deltaX == 0) {
                if (deltaY == 0) {
                    // A mistake has been made
                    throw new IllegalStateException("Duplicate point, deltaX=" + deltaX + ", deltaY=" + deltaY);
                }
                // Vertical line
                int row = Math.max(curPoint.y, lastPoint.y);
                int col = curPoint.x * 3;
                canvas[row][col] = '|';
            }
            else {
                if (deltaY != 0) {
                    // A mistake has been made
                    throw new IllegalStateException("Diagonal line, deltaX=" + deltaX + ", deltaY=" + deltaY);
                }
                // Horizontal line
                int row = curPoint.y;
                int col = Math.min(curPoint.x, lastPoint.x) * 3 + 1;
                canvas[row][col] = '_';
                canvas[row][col + 1] = '_';
            }
            
        }
        List<String> lines = new ArrayList<String>();
        for (char[] row : canvas) {
            String line = new String(row);
            lines.add(line);
        }
        
        return lines;
    }
    
    public static void main(String... args) {
        for (int order = 1; order <= 5; order++) {
            int n = (1 << order);
            List<Point> points = getPointsForCurve(n);
            System.out.println("Hilbert curve, order=" + order);
            List<String> lines = drawCurve(points, n);
            for (String line : lines) {
                System.out.println(line);
            }
            System.out.println();
        }
        return;
    }
}

```

### java_code_2.txt
```java
int  iterations = 7;
float strokeLen = 600;
int angleDeg = 90;
String axiom = "L";
StringDict rules = new StringDict();
String sentence = axiom;
int xo, yo;

void setup() {
  size(700, 700);
  xo= 50; 
  yo = height - 50;
  strokeWeight(1);
  noFill();
  
  rules.set("L", "+RF-LFL-FR+");
  rules.set("R", "-LF+RFR+FL-");
  
  generate(iterations);
}

void draw() {
  background(0);
  translate(xo, yo);
  plot(radians(angleDeg));
}

void generate(int n) {
  for (int i=0; i < n; i++) {
    strokeLen *= 0.5;
    String nextSentence = "";
    for (int j=0; j < sentence.length(); j++) {
      char c = sentence.charAt(j);
      String ruleResult = rules.get(str(c), str(c));
      nextSentence += ruleResult;
    }
    sentence = nextSentence;
  }
}

void plot(float angle) {
  for (int i=0; i < sentence.length(); i++) {
    char c = sentence.charAt(i);
    if (c == 'F') {
      stroke(255); 
      line(0, 0, 0, -strokeLen);
      translate(0, -strokeLen);
    } else if (c == '+') {
      rotate(angle);
    } else if (c == '-') {
      rotate(-angle);
    }
  }
}

void keyPressed() {
  if (key == '-') {
    angleDeg -= 1;
    println("Angle: " + angleDeg);
  }
  if (key == '=' || key == '+') {
    angleDeg += 1;
    println("Angle: " + angleDeg);
  }
  if (key == 'a') {
    strokeLen *= 2;
  }
  if (key == 'z') {
    strokeLen /= 2;
  }
  if (keyCode == LEFT) {
    xo -= 25;
  }
  if (keyCode == RIGHT) {
    xo += 25;
  }
  if (keyCode == UP) {
    yo -= 25;
  }
  if (keyCode == DOWN) {
    yo += 25;
  }
}

```

## Python Code
### python_code_1.txt
```python
iterations = 7
stroke_len = 600
angle_deg = 90
axiom = 'L'
sentence = axiom
rules = {
    'L': '+RF-LFL-FR+',
    'R': '-LF+RFR+FL-',
}

def setup():
    size(700, 700)
    global xo, yo
    xo, yo = 50, height - 50
    strokeWeight(1)
    noFill()
    generate(iterations)

def draw():
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        next_sentence = ''
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence

def plot(angle):
    for c in sentence:
        if c == 'F':
            stroke(255)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == '+':
            rotate(angle)
        elif c == '-':
            rotate(-angle)

def keyPressed():
    global angle_deg, xo, yo, stroke_len
    if key == '-':
        angle_deg -= 5
        print(angle_deg)
    if str(key) in "=+":
        angle_deg += 5
        print(angle_deg)
    if key == 'a':
        stroke_len *= 2
    if key == 'z':
        stroke_len /= 2
    if keyCode == LEFT:
        xo -= 50
    if keyCode == RIGHT:
        xo += 50
    if keyCode == UP:
        yo -= 50
    if keyCode == DOWN:
        yo += 50

```

### python_code_2.txt
```python
'''Hilbert curve'''

from itertools import (chain, islice)


# hilbertCurve :: Int -> SVG String
def hilbertCurve(n):
    '''An SVG string representing a
       Hilbert curve of degree n.
    '''
    w = 1024
    return svgFromPoints(w)(
        hilbertPoints(w)(
            hilbertTree(n)
        )
    )


# hilbertTree :: Int -> Tree Char
def hilbertTree(n):
    '''Nth application of a rule to a seedling tree.'''

    # rule :: Dict Char [Char]
    rule = {
        'a': ['d', 'a', 'a', 'b'],
        'b': ['c', 'b', 'b', 'a'],
        'c': ['b', 'c', 'c', 'd'],
        'd': ['a', 'd', 'd', 'c']
    }

    # go :: Tree Char -> Tree Char
    def go(tree):
        c = tree['root']
        xs = tree['nest']
        return Node(c)(
            map(go, xs) if xs else map(
                flip(Node)([]),
                rule[c]
            )
        )
    seed = Node('a')([])
    return list(islice(
        iterate(go)(seed), n
    ))[-1] if 0 < n else seed


# hilbertPoints :: Int -> Tree Char -> [(Int, Int)]
def hilbertPoints(w):
    '''Serialization of a tree to a list of points
       bounded by a square of side w.
    '''

    # vectors :: Dict Char [(Int, Int)]
    vectors = {
        'a': [(-1, 1), (-1, -1), (1, -1), (1, 1)],
        'b': [(1, -1), (-1, -1), (-1, 1), (1, 1)],
        'c': [(1, -1), (1, 1), (-1, 1), (-1, -1)],
        'd': [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    }

    # points :: Int -> ((Int, Int), Tree Char) -> [(Int, Int)]
    def points(d):
        '''Size -> Centre of a Hilbert subtree -> All subtree points
        '''
        def go(xy, tree):
            r = d // 2

            def deltas(v):
                return (
                    xy[0] + (r * v[0]),
                    xy[1] + (r * v[1])
                )
            centres = map(deltas, vectors[tree['root']])
            return chain.from_iterable(
                map(points(r), centres, tree['nest'])
            ) if tree['nest'] else centres
        return go

    d = w // 2
    return lambda tree: list(points(d)((d, d), tree))


# svgFromPoints :: Int -> [(Int, Int)] -> SVG String
def svgFromPoints(w):
    '''Width of square canvas -> Point list -> SVG string'''

    def go(xys):
        def points(xy):
            return str(xy[0]) + ' ' + str(xy[1])
        xs = ' '.join(map(points, xys))
        return '\n'.join(
            ['<svg xmlns="http://www.w3.org/2000/svg"',
             f'width="512" height="512" viewBox="5 5 {w} {w}">',
             f'<path d="M{xs}" ',
             'stroke-width="2" stroke="red" fill="transparent"/>',
             '</svg>'
             ]
        )
    return go


# ------------------------- TEST --------------------------
def main():
    '''Testing generation of the SVG for a Hilbert curve'''
    print(
        hilbertCurve(6)
    )


# ------------------- GENERIC FUNCTIONS -------------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    '''Contructor for a Tree node which connects a
       value of some kind to a list of zero or
       more child trees.'''
    return lambda xs: {'type': 'Node', 'root': v, 'nest': xs}


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.
    '''
    return lambda a: lambda b: f(b)(a)


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


#  TEST ---------------------------------------------------
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import matplotlib.pyplot as plt
import numpy as np
import turtle as tt

# dictionary containing the first order hilbert curves
base_shape = {'u': [np.array([0, 1]), np.array([1, 0]), np.array([0, -1])],
              'd': [np.array([0, -1]), np.array([-1, 0]), np.array([0, 1])],
              'r': [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0])],
              'l': [np.array([-1, 0]), np.array([0, -1]), np.array([1, 0])]}


def hilbert_curve(order, orientation):
    """
    Recursively creates the structure for a hilbert curve of given order
    """
    if order > 1:
        if orientation == 'u':
            return hilbert_curve(order - 1, 'r') + [np.array([0, 1])] + \
                   hilbert_curve(order - 1, 'u') + [np.array([1, 0])] + \
                   hilbert_curve(order - 1, 'u') + [np.array([0, -1])] + \
                   hilbert_curve(order - 1, 'l')
        elif orientation == 'd':
            return hilbert_curve(order - 1, 'l') + [np.array([0, -1])] + \
                   hilbert_curve(order - 1, 'd') + [np.array([-1, 0])] + \
                   hilbert_curve(order - 1, 'd') + [np.array([0, 1])] + \
                   hilbert_curve(order - 1, 'r')
        elif orientation == 'r':
            return hilbert_curve(order - 1, 'u') + [np.array([1, 0])] + \
                   hilbert_curve(order - 1, 'r') + [np.array([0, 1])] + \
                   hilbert_curve(order - 1, 'r') + [np.array([-1, 0])] + \
                   hilbert_curve(order - 1, 'd')
        else:
            return hilbert_curve(order - 1, 'd') + [np.array([-1, 0])] + \
                   hilbert_curve(order - 1, 'l') + [np.array([0, -1])] + \
                   hilbert_curve(order - 1, 'l') + [np.array([1, 0])] + \
                   hilbert_curve(order - 1, 'u')
    else:
        return base_shape[orientation]


# test the functions
if __name__ == '__main__':
    order = 8
    curve = hilbert_curve(order, 'u')
    curve = np.array(curve) * 4
    cumulative_curve = np.array([np.sum(curve[:i], 0) for i in range(len(curve)+1)])
    # plot curve using plt
    plt.plot(cumulative_curve[:, 0], cumulative_curve[:, 1])
    # draw curve using turtle graphics
    tt.setup(1920, 1000)
    tt.pu()
    tt.goto(-950, -490)
    tt.pd()
    tt.speed(0)
    for item in curve:
        tt.goto(tt.pos()[0] + item[0], tt.pos()[1] + item[1])
    tt.done()

```

