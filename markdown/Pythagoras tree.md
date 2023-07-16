# Pythagoras tree

## Task Link
[Rosetta Code - Pythagoras tree](https://rosettacode.org/wiki/Pythagoras_tree)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.geom.Path2D;
import javax.swing.*;

public class PythagorasTree extends JPanel {
    final int depthLimit = 7;
    float hue = 0.15f;

    public PythagorasTree() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);
    }

    private void drawTree(Graphics2D g, float x1, float y1, float x2, float y2,
            int depth) {

        if (depth == depthLimit)
            return;

        float dx = x2 - x1;
        float dy = y1 - y2;

        float x3 = x2 - dy;
        float y3 = y2 - dx;
        float x4 = x1 - dy;
        float y4 = y1 - dx;
        float x5 = x4 + 0.5F * (dx - dy);
        float y5 = y4 - 0.5F * (dx + dy);

        Path2D square = new Path2D.Float();
        square.moveTo(x1, y1);
        square.lineTo(x2, y2);
        square.lineTo(x3, y3);
        square.lineTo(x4, y4);
        square.closePath();

        g.setColor(Color.getHSBColor(hue + depth * 0.02f, 1, 1));
        g.fill(square);
        g.setColor(Color.lightGray);
        g.draw(square);

        Path2D triangle = new Path2D.Float();
        triangle.moveTo(x3, y3);
        triangle.lineTo(x4, y4);
        triangle.lineTo(x5, y5);
        triangle.closePath();

        g.setColor(Color.getHSBColor(hue + depth * 0.035f, 1, 1));
        g.fill(triangle);
        g.setColor(Color.lightGray);
        g.draw(triangle);

        drawTree(g, x4, y4, x5, y5, depth + 1);
        drawTree(g, x5, y5, x3, y3, depth + 1);
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawTree((Graphics2D) g, 275, 500, 375, 500, 0);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Pythagoras Tree");
            f.setResizable(false);
            f.add(new PythagorasTree(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
void tree(float x1, float y1, float x2, float y2, int depth) {

  if (depth <= 0) {
    return;
  }

  float dx = (x2 - x1);
  float dy = (y1 - y2);

  float x3 = (x2 - dy);
  float y3 = (y2 - dx);
  float x4 = (x1 - dy);
  float y4 = (y1 - dx);
  float x5 = (x4 + 0.5*(dx - dy));
  float y5 = (y4 - 0.5*(dx + dy));

  // square
  beginShape();
  fill(0.0, 255.0/depth, 0.0);
  vertex(x1, y1);
  vertex(x2, y2);
  vertex(x3, y3);
  vertex(x4, y4);
  vertex(x1, y1);
  endShape();

  // triangle
  beginShape();
  fill(0.0, 255.0/depth, 0.0);
  vertex(x3, y3);
  vertex(x4, y4);
  vertex(x5, y5);
  vertex(x3, y3);
  endShape();

  tree(x4, y4, x5, y5, depth-1);
  tree(x5, y5, x3, y3, depth-1);
}  

void setup() {
  size(1920, 1080);
  background(255);
  stroke(0, 255, 0);
  tree(width/2.3, height, width/1.8, height, 10);
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    size(800, 400)
    background(255)
    stroke(0, 255, 0)
    tree(width / 2.3, height, width / 1.8, height, 10)


def tree(x1, y1, x2, y2, depth):
    if depth <= 0: return
    dx = (x2 - x1)
    dy = (y1 - y2)

    x3 = (x2 - dy)
    y3 = (y2 - dx)
    x4 = (x1 - dy)
    y4 = (y1 - dx)
    x5 = (x4 + 0.5 * (dx - dy))
    y5 = (y4 - 0.5 * (dx + dy))

    # square
    beginShape()
    fill(0.0, 255.0 / depth, 0.0)
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x1, y1)
    endShape()

    # triangle
    beginShape()
    fill(0.0, 255.0 / depth, 0.0)
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x5, y5)
    vertex(x3, y3)
    endShape()

    tree(x4, y4, x5, y5, depth - 1)
    tree(x5, y5, x3, y3, depth - 1)

```

### python_code_2.txt
```python
from turtle import goto, pu, pd, color, done

def level(ax, ay, bx, by, depth=0):
    if depth > 0:
        dx,dy = bx-ax, ay-by
        x3,y3 = bx-dy, by-dx
        x4,y4 = ax-dy, ay-dx
        x5,y5 = x4 + (dx - dy)/2, y4 - (dx + dy)/2
        goto(ax, ay), pd()
        for x, y in ((bx, by), (x3, y3), (x4, y4), (ax, ay)):
            goto(x, y)
        pu()
        level(x4,y4, x5,y5, depth - 1)
        level(x5,y5, x3,y3, depth - 1)

if __name__ == '__main__':
    color('red', 'yellow')
    pu()
    level(-100, 500, 100, 500, depth=8)
    done()

```

