# Chaos game

## Task Link
[Rosetta Code - Chaos game](https://rosettacode.org/wiki/Chaos_game)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;
import javax.swing.Timer;

public class ChaosGame extends JPanel {
    static class ColoredPoint extends Point {
        int colorIndex;

        ColoredPoint(int x, int y, int idx) {
            super(x, y);
            colorIndex = idx;
        }
    }

    Stack<ColoredPoint> stack = new Stack<>();
    Point[] points = new Point[3];
    Color[] colors = {Color.red, Color.green, Color.blue};
    Random r = new Random();

    public ChaosGame() {
        Dimension dim = new Dimension(640, 640);
        setPreferredSize(dim);
        setBackground(Color.white);

        int margin = 60;
        int size = dim.width - 2 * margin;

        points[0] = new Point(dim.width / 2, margin);
        points[1] = new Point(margin, size);
        points[2] = new Point(margin + size, size);

        stack.push(new ColoredPoint(-1, -1, 0));

        new Timer(10, (ActionEvent e) -> {
            if (stack.size() < 50_000) {
                for (int i = 0; i < 1000; i++)
                    addPoint();
                repaint();
            }
        }).start();
    }

    private void addPoint() {
        try {
            int colorIndex = r.nextInt(3);
            Point p1 = stack.peek();
            Point p2 = points[colorIndex];
            stack.add(halfwayPoint(p1, p2, colorIndex));
        } catch (EmptyStackException e) {
            e.printStackTrace();
        }
    }

    void drawPoints(Graphics2D g) {
        for (ColoredPoint p : stack) {
            g.setColor(colors[p.colorIndex]);
            g.fillOval(p.x, p.y, 1, 1);
        }
    }

    ColoredPoint halfwayPoint(Point a, Point b, int idx) {
        return new ColoredPoint((a.x + b.x) / 2, (a.y + b.y) / 2, idx);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawPoints(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Chaos Game");
            f.setResizable(false);
            f.add(new ChaosGame(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
size(300, 260);

background(#ffffff); // white

int x = floor(random(width));
int y = floor(random(height));

int colour = #ffffff;

for (int i=0; i<30000; i++) {
  int v = floor(random(3));
  switch (v) {
  case 0:
    x = x / 2;
    y = y / 2;
    colour = #00ff00; // green
    break;
  case 1:
    x = width/2 + (width/2 - x)/2;
    y = height - (height - y)/2;
    colour = #ff0000; // red
    break;
  case 2:
    x = width - (width - x)/2;
    y = y / 2;
    colour = #0000ff; // blue
  }
  set(x, height-y, colour);
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division

size(300, 260)

background(255)  # white

x = floor(random(width))
y = floor(random(height))

for _ in range(30000):
    v = floor(random(3))
    if v == 0:
        x = x / 2
        y = y / 2
        colour = color(0, 255, 0)  # green
    elif v == 1:
        x = width / 2 + (width / 2 - x) / 2
        y = height - (height - y) / 2
        colour = color(255, 0, 0)  # red
    elif v == 2:
        x = width - (width - x) / 2
        y = y / 2
        colour = color(0, 0, 255)  # blue

    set(x, height - y, colour)

```

### python_code_2.txt
```python
import argparse
import random
import shapely.geometry as geometry
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main(args):
    # Styles
    plt.style.use("ggplot")

    # Creating figure
    fig = plt.figure()
    line, = plt.plot([], [], ".")

    # Limit axes
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Titles
    title = "Chaos Game"
    plt.title(title)
    fig.canvas.set_window_title(title)

    # Getting data
    data = get_data(args.frames)

    # Creating animation
    line_ani = animation.FuncAnimation(
        fig=fig,
        func=update_line,
        frames=args.frames,
        fargs=(data, line),
        interval=args.interval,
        repeat=False
    )

    # To save the animation install ffmpeg and uncomment
    # line_ani.save("chaos_game.gif")

    plt.show()


def get_data(n):
    """
    Get data to plot
    """
    leg = 1
    triangle = get_triangle(leg)
    cur_point = gen_point_within_poly(triangle)
    data = []
    for _ in range(n):
        data.append((cur_point.x, cur_point.y))
        cur_point = next_point(triangle, cur_point)
    return data


def get_triangle(n):
    """
    Create right triangle
    """
    ax = ay = 0.0
    a = ax, ay

    bx = 0.5  *  n
    by = 0.75 * (n ** 2)
    b = bx, by

    cx = n
    cy = 0.0
    c = cx, cy

    triangle = geometry.Polygon([a, b, c])
    return triangle


def gen_point_within_poly(poly):
    """
    Generate random point inside given polygon
    """
    minx, miny, maxx, maxy = poly.bounds
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = geometry.Point(x, y)
        if point.within(poly):
            return point


def next_point(poly, point):
    """
    Generate next point according to chaos game rules
    """
    vertices = poly.boundary.coords[:-1]  # Last point is the same as the first one
    random_vertex = geometry.Point(random.choice(vertices))
    line = geometry.linestring.LineString([point, random_vertex])
    return line.centroid


def update_line(num, data, line):
    """
    Update line with new points
    """
    new_data = zip(*data[:num]) or [(), ()]
    line.set_data(new_data)
    return line,


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Chaos Game by Suenweek (c) 2017")
    arg_parser.add_argument("-f", dest="frames", type=int, default=1000)
    arg_parser.add_argument("-i", dest="interval", type=int, default=10)

    main(arg_parser.parse_args())

```

