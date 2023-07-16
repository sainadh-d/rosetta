# Color wheel

## Task Link
[Rosetta Code - Color wheel](https://rosettacode.org/wiki/Color_wheel)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import javax.swing.*;

public class ColorWheel {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                ColorWheelFrame frame = new ColorWheelFrame();
                frame.setVisible(true);
            }
        });
    }

    private static class ColorWheelFrame extends JFrame {
        private ColorWheelFrame() {
            super("Color Wheel");
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            getContentPane().add(new ColorWheelPanel());
            pack();
        }
    }

    private static class ColorWheelPanel extends JComponent {
        private ColorWheelPanel() {
            setPreferredSize(new Dimension(400, 400));
        }
        public void paint(Graphics g) {
            Graphics2D g2 = (Graphics2D)g;
            int w = getWidth();
            int h = getHeight();
            int margin = 10;
            int radius = (Math.min(w, h) - 2 * margin)/2;
            int cx = w/2;
            int cy = h/2;
            float[] dist = {0.F, 1.0F};
            g2.setColor(Color.BLACK);
            g2.fillRect(0, 0, w, h);
            for (int angle = 0; angle < 360; ++angle) {
                Color color = hsvToRgb(angle, 1.0, 1.0);
                Color[] colors = {Color.WHITE, color};
                RadialGradientPaint paint = new RadialGradientPaint(cx, cy,
                        radius, dist, colors);
                g2.setPaint(paint);
                g2.fillArc(cx - radius, cy - radius, radius*2, radius*2,
                        angle, 1);
            }
        }
    }

    private static Color hsvToRgb(int h, double s, double v) {
        double hp = h/60.0;
        double c = s * v;
        double x = c * (1 - Math.abs(hp % 2.0 - 1));
        double m = v - c;
        double r = 0, g = 0, b = 0;
        if (hp <= 1) {
            r = c;
            g = x;
        } else if (hp <= 2) {
            r = x;
            g = c;
        } else if (hp <= 3) {
            g = c;
            b = x;
        } else if (hp <= 4) {
            g = x;
            b = c;
        } else if (hp <= 5) {
            r = x;
            b = c;
        } else {
            r = c;
            b = x;
        }
        r += m;
        g += m;
        b += m;
        return new Color((int)(r * 255), (int)(g * 255), (int)(b * 255));
    }
}

```

### java_code_2.txt
```java
size(300, 300);
background(0);
float radius = min(width, height) / 2.0;
float cx = width / 2;
float cy = width / 2;
for (int x = 0; x < width; x++) {
  for (int y = 0; y < width; y++) {
    float rx = x - cx;
    float ry = y - cy;
    float s = sqrt(sq(rx) + sq(ry)) / radius;
    if (s <= 1.0) {
      float h = ((atan2(ry, rx) / PI) + 1.0) / 2.0;
      colorMode(HSB);
      color c = color(int(h * 255), int(s * 255), 255);
      set(x, y, c);
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
size(300, 300)
background(0)
radius = min(width, height) / 2.0
cx, cy = width / 2, width / 2
for x in range(width):
        for y in range(height):
            rx = x - cx
            ry = y - cy
            s = sqrt(rx ** 2 + ry ** 2) / radius
            if s <= 1.0:
                h = ((atan2(ry, rx) / PI) + 1.0) / 2.0
                colorMode(HSB)
                c = color(int(h * 255), int(s * 255), 255)
                set(x, y, c) # note set() used as Processing set() not as Python set()

```

### python_code_2.txt
```python
from PIL import Image
import colorsys
import math

if __name__ == "__main__":

    im = Image.new("RGB", (300,300))
    radius = min(im.size)/2.0
    cx, cy = im.size[0]/2, im.size[1]/2
    pix = im.load()
 
    for x in range(im.width):
        for y in range(im.height):
            rx = x - cx
            ry = y - cy
            s = (rx ** 2.0 + ry ** 2.0) ** 0.5 / radius
            if s <= 1.0:
                h = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
                rgb = colorsys.hsv_to_rgb(h, s, 1.0)
                pix[x,y] = tuple([int(round(c*255.0)) for c in rgb])

    im.show()

```

