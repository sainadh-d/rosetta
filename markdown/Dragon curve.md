# Dragon curve

## Task Link
[Rosetta Code - Dragon curve](https://rosettacode.org/wiki/Dragon_curve)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.util.*;
import javax.swing.JFrame;

public class DragonCurve extends JFrame {

    private List<Integer> turns;
    private double startingAngle, side;

    public DragonCurve(int iter) {
        super("Dragon Curve");
        setBounds(100, 100, 800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        turns = getSequence(iter);
        startingAngle = -iter * (Math.PI / 4);
        side = 400 / Math.pow(2, iter / 2.);
    }

    public List<Integer> getSequence(int iterations) {
        List<Integer> turnSequence = new ArrayList<Integer>();
        for (int i = 0; i < iterations; i++) {
            List<Integer> copy = new ArrayList<Integer>(turnSequence);
            Collections.reverse(copy);
            turnSequence.add(1);
            for (Integer turn : copy) {
                turnSequence.add(-turn);
            }
        }
        return turnSequence;
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.BLACK);
        double angle = startingAngle;
        int x1 = 230, y1 = 350;
        int x2 = x1 + (int) (Math.cos(angle) * side);
        int y2 = y1 + (int) (Math.sin(angle) * side);
        g.drawLine(x1, y1, x2, y2);
        x1 = x2;
        y1 = y2;
        for (Integer turn : turns) {
            angle += turn * (Math.PI / 2);
            x2 = x1 + (int) (Math.cos(angle) * side);
            y2 = y1 + (int) (Math.sin(angle) * side);
            g.drawLine(x1, y1, x2, y2);
            x1 = x2;
            y1 = y2;
        }
    }

    public static void main(String[] args) {
        new DragonCurve(14).setVisible(true);
    }
}

```

### java_code_2.txt
```java
float l = 3;
int ints = 13;

void setup() {
  size(700, 600);
  background(0, 0, 255);
  translate(150, 100);
  stroke(255);
  turn_left(l, ints);
  turn_right(l, ints);
}

void turn_right(float l, int ints) {
  if (ints == 0) {
    line(0, 0, 0, -l);
    translate(0, -l);
  } else {
    turn_left(l, ints-1);
    rotate(radians(90));
    turn_right(l, ints-1);
  }
}

void turn_left(float l, int ints) {
  if (ints == 0) {
    line(0, 0, 0, -l);
    translate(0, -l);
  } else {
    turn_left(l, ints-1);
    rotate(radians(-90));
    turn_right(l, ints-1);
  }
}

```

## Python Code
### python_code_1.txt
```python
l = 3
ints = 13

def setup():
  size(700, 600)
  background(0, 0, 255)
  translate(150, 100)
  stroke(255)
  turn_left(l, ints)
  turn_right(l, ints)

def turn_right(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(90))
        turn_right(l, ints - 1)
  
def turn_left(l, ints):
    if ints == 0:
        line(0, 0, 0, -l)
        translate(0, -l)
    else:
        turn_left(l, ints - 1)
        rotate(radians(-90))
        turn_right(l, ints - 1)

```

### python_code_2.txt
```python
from turtle import *

def dragon(step, length):
    dcr(step, length)

def dcr(step, length):
    step -= 1
    length /= 1.41421
    if step > 0:
        right(45)
        dcr(step, length)
        left(90)
        dcl(step, length)
        right(45)
    else:
        right(45)
        forward(length)
        left(90)
        forward(length)
        right(45)

def dcl(step, length):
    step -= 1
    length /= 1.41421

    if step > 0:
        left(45)
        dcr(step, length)
        right(90)
        dcl(step, length)
        left(45)
    else:
        left(45)
        forward(length)
        right(90)
        forward(length)
        left(45)

```

### python_code_3.txt
```python
from turtle import right, left, forward, speed, exitonclick, hideturtle

def dragon(level=4, size=200, zig=right, zag=left):
    if level <= 0:
        forward(size)
        return

    size /= 1.41421
    zig(45)
    dragon(level-1, size, right, left)
    zag(90)
    dragon(level-1, size, left, right)
    zig(45)

speed(0)
hideturtle()
dragon(6)
exitonclick() # click to exit

```

### python_code_4.txt
```python
from turtle import right, left, forward, speed, exitonclick, hideturtle

def dragon(level=4, size=200, direction=45):
    if level:
        right(direction)
        dragon(level-1, size/1.41421356237, 45)
        left(direction * 2)
        dragon(level-1, size/1.41421356237, -45)
        right(direction)
    else:
        forward(size)

speed(0)
hideturtle()
dragon(6)
exitonclick() # click to exit

```

