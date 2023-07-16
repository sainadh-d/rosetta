# Sierpinski pentagon

## Task Link
[Rosetta Code - Sierpinski pentagon](https://rosettacode.org/wiki/Sierpinski_pentagon)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.geom.Path2D;
import static java.lang.Math.*;
import java.util.Random;
import javax.swing.*;

public class SierpinskiPentagon extends JPanel {
    // exterior angle
    final double degrees072 = toRadians(72);

    /* After scaling we'll have 2 sides plus a gap occupying the length
       of a side before scaling. The gap is the base of an isosceles triangle
       with a base angle of 72 degrees. */
    final double scaleFactor = 1 / (2 + cos(degrees072) * 2);

    final int margin = 20;
    int limit = 0;
    Random r = new Random();

    public SierpinskiPentagon() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);

        new Timer(3000, (ActionEvent e) -> {
            limit++;
            if (limit >= 5)
                limit = 0;
            repaint();
        }).start();
    }

    void drawPentagon(Graphics2D g, double x, double y, double side, int depth) {
        double angle = 3 * degrees072; // starting angle

        if (depth == 0) {

            Path2D p = new Path2D.Double();
            p.moveTo(x, y);

            // draw from the top
            for (int i = 0; i < 5; i++) {
                x = x + cos(angle) * side;
                y = y - sin(angle) * side;
                p.lineTo(x, y);
                angle += degrees072;
            }

            g.setColor(RandomHue.next());
            g.fill(p);

        } else {

            side *= scaleFactor;

            /* Starting at the top of the highest pentagon, calculate
               the top vertices of the other pentagons by taking the
               length of the scaled side plus the length of the gap. */
            double distance = side + side * cos(degrees072) * 2;

            /* The top positions form a virtual pentagon of their own,
               so simply move from one to the other by changing direction. */
            for (int i = 0; i < 5; i++) {
                x = x + cos(angle) * distance;
                y = y - sin(angle) * distance;
                drawPentagon(g, x, y, side, depth - 1);
                angle += degrees072;
            }
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        int w = getWidth();
        double radius = w / 2 - 2 * margin;
        double side = radius * sin(PI / 5) * 2;

        drawPentagon(g, w / 2, 3 * margin, side, limit);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Sierpinski Pentagon");
            f.setResizable(true);
            f.add(new SierpinskiPentagon(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

class RandomHue {
    /* Try to avoid random color values clumping together */
    final static double goldenRatioConjugate = (sqrt(5) - 1) / 2;
    private static double hue = Math.random();

    static Color next() {
        hue = (hue + goldenRatioConjugate) % 1;
        return Color.getHSBColor((float) hue, 1, 1);
    }
}

```

### java_code_2.txt
```java
float s_angle, scale, margin = 25, total = 4;
float p_size = 700;
float radius = p_size/2-2*margin;
float side = radius * sin(PI/5)*2;

void setup() {
  float temp = width/2;
  size(590, 590);
  background(0, 0, 200);
  stroke(255);
  s_angle = 72*PI/180;
  scale = 1/(2+cos(s_angle)*2);
  for (int i = 0; i < total; i++) {
    background(0, 0, 200);
    drawPentagon(width/2, (height-p_size)/2 + 3*margin, side, total);
  }
}

void drawPentagon(float x, float y, float side, float depth) {
  float angle = 3*s_angle; 
  if (depth == 0) {  
    for (int i = 0; i < 5; i++) {
      float px = x;
      float py = y;
      x = x+cos(angle)*side;
      y = y-sin(angle)*side;
      line(x, y, px, py);
      angle += s_angle;
    }
  } else {
    side *= scale;
    float distance = side+side*cos(s_angle)*2;
    for (int j = 0; j < 5; j++) {
      x = x+cos(angle)*distance;
      y = y-sin(angle)*distance;
      drawPentagon(x, y, side, depth-1);
      angle += s_angle;
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
from turtle import *
import math
speed(0)      # 0 is the fastest speed. Otherwise, 1 (slow) to 10 (fast)
hideturtle()  # hide the default turtle

part_ratio = 2 * math.cos(math.radians(72))
side_ratio = 1 / (part_ratio + 2)

hide_turtles = True   # show/hide turtles as they draw
path_color = "black"  # path color
fill_color = "black"  # fill color

# turtle, size
def pentagon(t, s):
  t.color(path_color, fill_color)
  t.pendown()
  t.right(36)
  t.begin_fill()
  for i in range(5):
    t.forward(s)
    t.right(72)
  t.end_fill()

# iteration, turtle, size
def sierpinski(i, t, s):
  t.setheading(0)
  new_size = s * side_ratio
  
  if i > 1:
    i -= 1
    
    # create four more turtles
    for j in range(4):
      t.right(36)
      short = s * side_ratio / part_ratio
      dist = [short, s, s, short][j]
      
      # spawn a turtle
      spawn = Turtle()
      if hide_turtles:spawn.hideturtle()
      spawn.penup()
      spawn.setposition(t.position())
      spawn.setheading(t.heading())
      spawn.forward(dist)
      
      # recurse for spawned turtles
      sierpinski(i, spawn, new_size)
    
    # recurse for parent turtle
    sierpinski(i, t, new_size)
    
  else:
    # draw a pentagon
    pentagon(t, s)
    # delete turtle
    del t

def main():
  t = Turtle()
  t.hideturtle()
  t.penup()
  screen = t.getscreen()
  y = screen.window_height()
  t.goto(0, y/2-20)
  
  i = 5       # depth. i >= 1
  size = 300  # side length
  
  # so the spawned turtles move only the distance to an inner pentagon
  size *= part_ratio
  
  # begin recursion
  sierpinski(i, t, size)

main()

```

