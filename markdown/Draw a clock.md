# Draw a clock

## Task Link
[Rosetta Code - Draw a clock](https://rosettacode.org/wiki/Draw_a_clock)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import static java.lang.Math.*;
import java.time.LocalTime;
import javax.swing.*;

class Clock extends JPanel {

    final float degrees06 = (float) (PI / 30);
    final float degrees30 = degrees06 * 5;
    final float degrees90 = degrees30 * 3;

    final int size = 590;
    final int spacing = 40;
    final int diameter = size - 2 * spacing;
    final int cx = diameter / 2 + spacing;
    final int cy = diameter / 2 + spacing;

    public Clock() {
        setPreferredSize(new Dimension(size, size));
        setBackground(Color.white);

        new Timer(1000, (ActionEvent e) -> {
            repaint();
        }).start();
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawFace(g);

        final LocalTime time  = LocalTime.now();
        int hour = time.getHour();
        int minute = time.getMinute();
        int second = time.getSecond();

        float angle = degrees90 - (degrees06 * second);
        drawHand(g, angle, diameter / 2 - 30, Color.red);

        float minsecs = (minute + second / 60.0F);
        angle = degrees90 - (degrees06 * minsecs);
        drawHand(g, angle, diameter / 3 + 10, Color.black);

        float hourmins = (hour + minsecs / 60.0F);
        angle = degrees90 - (degrees30 * hourmins);
        drawHand(g, angle, diameter / 4 + 10, Color.black);
    }

    private void drawFace(Graphics2D g) {
        g.setStroke(new BasicStroke(2));
        g.setColor(Color.white);
        g.fillOval(spacing, spacing, diameter, diameter);
        g.setColor(Color.black);
        g.drawOval(spacing, spacing, diameter, diameter);
    }

    private void drawHand(Graphics2D g, float angle, int radius, Color color) {
        int x = cx + (int) (radius * cos(angle));
        int y = cy - (int) (radius * sin(angle));
        g.setColor(color);
        g.drawLine(cx, cy, x, y);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Clock");
            f.setResizable(false);
            f.add(new Clock(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
void draw() {
  drawClock();
}
void drawClock() {
  background(192);
  translate(width/2, height/2);
  float s = second() * TWO_PI / 60.0;
  float m = minute() * TWO_PI / 60.0;
  float h = hour() * TWO_PI / 12.0;
  rotate(s);
  strokeWeight(1);
  line(0, 0, 0, -width*0.5);
  rotate(-s+m);
  strokeWeight(2);
  line(0, 0, 0, -width*0.4);
  rotate(-m+h);
  strokeWeight(4);
  line(0, 0, 0, -width*0.2);
}

```

### java_code_3.txt
```java
int lastSec = second();
void draw() {
  if (lastSec!=second()) {
    drawClock();
    lastSec=second();
  }
}

```

## Python Code
### python_code_1.txt
```python
last_sec = second()

def draw():
    global last_sec
    if last_sec != second():
        draw_clock()
        last_sec = second()

def draw_clock():
    background(192)
    translate(width / 2, height / 2)
    s = second() * TWO_PI / 60.0
    m = minute() * TWO_PI / 60.0
    h = hour() * TWO_PI / 12.0
    rotate(s)
    strokeWeight(1)
    line(0, 0, 0, -width * 0.5)
    rotate(-s + m)
    strokeWeight(2)
    line(0, 0, 0, -width * 0.4)
    rotate(-m + h)
    strokeWeight(4)
    line(0, 0, 0, -width * 0.2)

```

### python_code_2.txt
```python
import time

def chunks(l, n=5):
    return [l[i:i+n] for i in range(0, len(l), n)]

def binary(n, digits=8):
    n=int(n)
    return '{0:0{1}b}'.format(n, digits)

def secs(n):
    n=int(n)
    h='x' * n
    return "|".join(chunks(h))

def bin_bit(h):
    h=h.replace("1","x")
    h=h.replace("0"," ")
    return "|".join(list(h))


x=str(time.ctime()).split()
y=x[3].split(":")

s=y[-1]
y=map(binary,y[:-1])

print bin_bit(y[0])
print
print bin_bit(y[1])
print
print secs(s)

```

