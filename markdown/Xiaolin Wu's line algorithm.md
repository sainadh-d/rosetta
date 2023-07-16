# Xiaolin Wu's line algorithm

## Task Link
[Rosetta Code - Xiaolin Wu's line algorithm](https://rosettacode.org/wiki/Xiaolin_Wu%27s_line_algorithm)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import static java.lang.Math.*;
import javax.swing.*;

public class XiaolinWu extends JPanel {

    public XiaolinWu() {
        Dimension dim = new Dimension(640, 640);
        setPreferredSize(dim);
        setBackground(Color.white);
    }

    void plot(Graphics2D g, double x, double y, double c) {
        g.setColor(new Color(0f, 0f, 0f, (float)c));
        g.fillOval((int) x, (int) y, 2, 2);
    }

    int ipart(double x) {
        return (int) x;
    }

    double fpart(double x) {
        return x - floor(x);
    }

    double rfpart(double x) {
        return 1.0 - fpart(x);
    }

    void drawLine(Graphics2D g, double x0, double y0, double x1, double y1) {

        boolean steep = abs(y1 - y0) > abs(x1 - x0);
        if (steep)
            drawLine(g, y0, x0, y1, x1);

        if (x0 > x1)
            drawLine(g, x1, y1, x0, y0);

        double dx = x1 - x0;
        double dy = y1 - y0;
        double gradient = dy / dx;

        // handle first endpoint
        double xend = round(x0);
        double yend = y0 + gradient * (xend - x0);
        double xgap = rfpart(x0 + 0.5);
        double xpxl1 = xend; // this will be used in the main loop
        double ypxl1 = ipart(yend);

        if (steep) {
            plot(g, ypxl1, xpxl1, rfpart(yend) * xgap);
            plot(g, ypxl1 + 1, xpxl1, fpart(yend) * xgap);
        } else {
            plot(g, xpxl1, ypxl1, rfpart(yend) * xgap);
            plot(g, xpxl1, ypxl1 + 1, fpart(yend) * xgap);
        }

        // first y-intersection for the main loop
        double intery = yend + gradient;

        // handle second endpoint
        xend = round(x1);
        yend = y1 + gradient * (xend - x1);
        xgap = fpart(x1 + 0.5);
        double xpxl2 = xend; // this will be used in the main loop
        double ypxl2 = ipart(yend);

        if (steep) {
            plot(g, ypxl2, xpxl2, rfpart(yend) * xgap);
            plot(g, ypxl2 + 1, xpxl2, fpart(yend) * xgap);
        } else {
            plot(g, xpxl2, ypxl2, rfpart(yend) * xgap);
            plot(g, xpxl2, ypxl2 + 1, fpart(yend) * xgap);
        }

        // main loop
        for (double x = xpxl1 + 1; x <= xpxl2 - 1; x++) {
            if (steep) {
                plot(g, ipart(intery), x, rfpart(intery));
                plot(g, ipart(intery) + 1, x, fpart(intery));
            } else {
                plot(g, x, ipart(intery), rfpart(intery));
                plot(g, x, ipart(intery) + 1, fpart(intery));
            }
            intery = intery + gradient;
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;

        drawLine(g, 550, 170, 50, 435);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Xiaolin Wu's line algorithm");
            f.setResizable(false);
            f.add(new XiaolinWu(), BorderLayout.CENTER);
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
"""Script demonstrating drawing of anti-aliased lines using Xiaolin Wu's line
algorithm

usage: python xiaolinwu.py [output-file]

"""
from __future__ import division
import sys

from PIL import Image


def _fpart(x):
    return x - int(x)

def _rfpart(x):
    return 1 - _fpart(x)

def putpixel(img, xy, color, alpha=1):
    """
    Paints color over the background at the point xy in img.
    Use alpha for blending. alpha=1 means a completely opaque foreground.
    """
    compose_color = lambda bg, fg: int(round(alpha * fg + (1-alpha) * bg))
    c = compose_color(img.getpixel(xy), color)
    img.putpixel(xy, c)

def draw_line(img, p1, p2, color):
    """Draws an anti-aliased line in img from p1 to p2 with the given color."""
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2-x1, y2-y1
    steep = abs(dx) < abs(dy)
    p = lambda px, py: ((px,py), (py,px))[steep]

    if steep:
        x1, y1, x2, y2, dx, dy = y1, x1, y2, x2, dy, dx
    if x2 < x1:
        x1, x2, y1, y2 = x2, x1, y2, y1

    grad = dy/dx
    intery = y1 + _rfpart(x1) * grad
    def draw_endpoint(pt):
        x, y = pt
        xend = round(x)
        yend = y + grad * (xend - x)
        xgap = _rfpart(x + 0.5)
        px, py = int(xend), int(yend)
        putpixel(img, p(px, py), color, _rfpart(yend) * xgap)
        putpixel(img, p(px, py+1), color, _fpart(yend) * xgap)
        return px

    xstart = draw_endpoint(p(*p1)) + 1
    xend = draw_endpoint(p(*p2))

    for x in range(xstart, xend):
        y = int(intery)
        putpixel(img, p(x, y), color, _rfpart(intery))
        putpixel(img, p(x, y+1), color, _fpart(intery))
        intery += grad


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: python xiaolinwu.py [output-file]'
        sys.exit(-1)

    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    img = Image.new("RGB", (500,500), blue)
    for a in range(10, 431, 60):
        draw_line(img, (10, 10), (490, a), yellow)
        draw_line(img, (10, 10), (a, 490), yellow)
    draw_line(img, (10, 10), (490, 490), yellow)
    filename = sys.argv[1]
    img.save(filename)
    print 'image saved to', filename

```

