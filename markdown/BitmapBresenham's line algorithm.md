# Bitmap/Bresenham's line algorithm

## Task Link
[Rosetta Code - Bitmap/Bresenham's line algorithm](https://rosettacode.org/wiki/Bitmap/Bresenham%27s_line_algorithm)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;

public class Bresenham {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(Bresenham::run);
    }

    private static void run() {
        JFrame f = new JFrame();
        f.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        f.setTitle("Bresenham");

        f.getContentPane().add(new BresenhamPanel());
        f.pack();

        f.setLocationRelativeTo(null);
        f.setVisible(true);
    }
}

class BresenhamPanel extends JPanel {

    private final int pixelSize = 10;

    BresenhamPanel() {
        setPreferredSize(new Dimension(600, 500));
        setBackground(Color.WHITE);
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        int w = (getWidth() - 1) / pixelSize;
        int h = (getHeight() - 1) / pixelSize;
        int maxX = (w - 1) / 2;
        int maxY = (h - 1) / 2;
        int x1 = -maxX, x2 = maxX * -2 / 3, x3 = maxX * 2 / 3, x4 = maxX;
        int y1 = -maxY, y2 = maxY * -2 / 3, y3 = maxY * 2 / 3, y4 = maxY;

        drawLine(g, 0, 0, x3, y1); // NNE
        drawLine(g, 0, 0, x4, y2); // ENE
        drawLine(g, 0, 0, x4, y3); // ESE
        drawLine(g, 0, 0, x3, y4); // SSE
        drawLine(g, 0, 0, x2, y4); // SSW
        drawLine(g, 0, 0, x1, y3); // WSW
        drawLine(g, 0, 0, x1, y2); // WNW
        drawLine(g, 0, 0, x2, y1); // NNW
    }

    private void plot(Graphics g, int x, int y) {
        int w = (getWidth() - 1) / pixelSize;
        int h = (getHeight() - 1) / pixelSize;
        int maxX = (w - 1) / 2;
        int maxY = (h - 1) / 2;

        int borderX = getWidth() - ((2 * maxX + 1) * pixelSize + 1);
        int borderY = getHeight() - ((2 * maxY + 1) * pixelSize + 1);
        int left = (x + maxX) * pixelSize + borderX / 2;
        int top = (y + maxY) * pixelSize + borderY / 2;

        g.setColor(Color.black);
        g.drawOval(left, top, pixelSize, pixelSize);
    }

    private void drawLine(Graphics g, int x1, int y1, int x2, int y2) {
        // delta of exact value and rounded value of the dependent variable
        int d = 0;

        int dx = Math.abs(x2 - x1);
        int dy = Math.abs(y2 - y1);

        int dx2 = 2 * dx; // slope scaling factors to
        int dy2 = 2 * dy; // avoid floating point

        int ix = x1 < x2 ? 1 : -1; // increment direction
        int iy = y1 < y2 ? 1 : -1;

        int x = x1;
        int y = y1;

        if (dx >= dy) {
            while (true) {
                plot(g, x, y);
                if (x == x2)
                    break;
                x += ix;
                d += dy2;
                if (d > dx) {
                    y += iy;
                    d -= dx2;
                }
            }
        } else {
            while (true) {
                plot(g, x, y);
                if (y == y2)
                    break;
                y += iy;
                d += dx2;
                if (d > dy) {
                    x += ix;
                    d -= dy2;
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def line(self, x0, y0, x1, y1):
    "Bresenham's line algorithm"
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    if dx > dy:
        err = dx / 2.0
        while x != x1:
            self.set(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            self.set(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy        
    self.set(x, y)
Bitmap.line = line

bitmap = Bitmap(17,17)
for points in ((1,8,8,16),(8,16,16,8),(16,8,8,1),(8,1,1,8)):
    bitmap.line(*points)
bitmap.chardisplay()

'''
The origin, 0,0; is the lower left, with x increasing to the right,
and Y increasing upwards.

The chardisplay above produces the following output :
+-----------------+
|        @        |
|       @ @       |
|      @   @      |
|     @     @     |
|    @       @    |
|    @        @   |
|   @          @  |
|  @            @ |
| @              @|
|  @            @ |
|   @          @  |
|    @       @@   |
|     @     @     |
|      @   @      |
|       @ @       |
|        @        |
|                 |
+-----------------+
'''

```

### python_code_2.txt
```python
from fractions import Fraction

def line(self, x0, y0, x1, y1):
    rev = reversed
    if abs(y1 - y0) <= abs(x1 - x0):
        x0, y0, x1, y1 = y0, x0, y1, x1
        rev = lambda x: x
    if x1 < x0:
        x0, y0, x1, y1 = x1, y1, x0, y0
    leny = abs(y1 - y0)
    for i in range(leny + 1):
        self.set(*rev((round(Fraction(i, leny) * (x1 - x0)) + x0, (1 if y1 > y0 else -1) * i + y0)))

Bitmap.line = line

# see test code above

```

