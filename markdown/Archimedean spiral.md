# Archimedean spiral

## Task Link
[Rosetta Code - Archimedean spiral](https://rosettacode.org/wiki/Archimedean_spiral)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import static java.lang.Math.*;
import javax.swing.*;

public class ArchimedeanSpiral extends JPanel {

    public ArchimedeanSpiral() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);
    }

    void drawGrid(Graphics2D g) {
        g.setColor(new Color(0xEEEEEE));
        g.setStroke(new BasicStroke(2));

        double angle = toRadians(45);

        int w = getWidth();
        int center = w / 2;
        int margin = 10;
        int numRings = 8;

        int spacing = (w - 2 * margin) / (numRings * 2);

        for (int i = 0; i < numRings; i++) {
            int pos = margin + i * spacing;
            int size = w - (2 * margin + i * 2 * spacing);
            g.drawOval(pos, pos, size, size);

            double ia = i * angle;
            int x2 = center + (int) (cos(ia) * (w - 2 * margin) / 2);
            int y2 = center - (int) (sin(ia) * (w - 2 * margin) / 2);

            g.drawLine(center, center, x2, y2);
        }
    }

    void drawSpiral(Graphics2D g) {
        g.setStroke(new BasicStroke(2));
        g.setColor(Color.orange);

        double degrees = toRadians(0.1);
        double center = getWidth() / 2;
        double end = 360 * 2 * 10 * degrees;
        double a = 0;
        double b = 20;
        double c = 1;

        for (double theta = 0; theta < end; theta += degrees) {
            double r = a + b * pow(theta, 1 / c);
            double x = r * cos(theta);
            double y = r * sin(theta);
            plot(g, (int) (center + x), (int) (center - y));
        }
    }

    void plot(Graphics2D g, int x, int y) {
        g.drawOval(x, y, 1, 1);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawGrid(g);
        drawSpiral(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Archimedean Spiral");
            f.setResizable(false);
            f.add(new ArchimedeanSpiral(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
theta = 0
rotation = 0.1

def setup():
    size(300, 300)
    background(255)

def draw():
    global theta
    translate(width / 2.0, height / 2.0)
    x = theta * cos(theta / PI)
    y = theta * sin(theta / PI)
    point(x, y)
    theta = theta + rotation
    # check restart
    if x > width / 2.0:
        background(255)
        theta = 0

```

### python_code_2.txt
```python
from turtle import *
from math import *
color("blue")
down()
for i in range(200):
    t = i / 20 * pi
    x = (1 + 5 * t) * cos(t)
    y = (1 + 5 * t) * sin(t)
    goto(x, y)
up()
done()

```

