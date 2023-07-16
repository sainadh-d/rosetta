# Barnsley fern

## Task Link
[Rosetta Code - Barnsley fern](https://rosettacode.org/wiki/Barnsley_fern)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.swing.*;

public class BarnsleyFern extends JPanel {

    BufferedImage img;

    public BarnsleyFern() {
        final int dim = 640;
        setPreferredSize(new Dimension(dim, dim));
        setBackground(Color.white);
        img = new BufferedImage(dim, dim, BufferedImage.TYPE_INT_ARGB);
        createFern(dim, dim);
    }

    void createFern(int w, int h) {
        double x = 0;
        double y = 0;

        for (int i = 0; i < 200_000; i++) {
            double tmpx, tmpy;
            double r = Math.random();

            if (r <= 0.01) {
                tmpx = 0;
                tmpy = 0.16 * y;
            } else if (r <= 0.08) {
                tmpx = 0.2 * x - 0.26 * y;
                tmpy = 0.23 * x + 0.22 * y + 1.6;
            } else if (r <= 0.15) {
                tmpx = -0.15 * x + 0.28 * y;
                tmpy = 0.26 * x + 0.24 * y + 0.44;
            } else {
                tmpx = 0.85 * x + 0.04 * y;
                tmpy = -0.04 * x + 0.85 * y + 1.6;
            }
            x = tmpx;
            y = tmpy;

            img.setRGB((int) Math.round(w / 2 + x * w / 11),
                    (int) Math.round(h - y * h / 11), 0xFF32CD32);
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Barnsley Fern");
            f.setResizable(false);
            f.add(new BarnsleyFern(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
void setup() {
  size(640, 640);
  background(0, 0, 0);
}

float x = 0;
float y = 0;

void draw() {
  for (int i = 0; i < 100000; i++) {

    float xt = 0;
    float yt = 0;

    float r = random(100);

    if (r <= 1) {
      xt = 0;
      yt = 0.16*y;
    } else if (r <= 8) {
      xt = 0.20*x - 0.26*y;
      yt = 0.23*x + 0.22*y + 1.60;
    } else if (r <= 15) {
      xt = -0.15*x + 0.28*y;
      yt =  0.26*x + 0.24*y + 0.44;
    } else {
      xt =  0.85*x + 0.04*y;
      yt = -0.04*x + 0.85*y + 1.60;
    }

    x = xt;
    y = yt;

    int m = round(width/2 + 60*x);
    int n = height-round(60*y);

    set(m, n, #00ff00);
  }
  noLoop();
}

```

## Python Code
### python_code_1.txt
```python
size(640, 640)
background(0)

x = 0
y = 0

for _ in range(100000):
    xt = 0
    yt = 0
    r = random(100)

    if r <= 1:
        xt = 0
        yt = 0.16 * y
    elif r <= 8:
        xt = 0.20 * x - 0.26 * y
        yt = 0.23 * x + 0.22 * y + 1.60
    elif r <= 15:
        xt = -0.15 * x + 0.28 * y
        yt = +0.26 * x + 0.24 * y + 0.44
    else:
        xt = +0.85 * x + 0.04 * y
        yt = -0.04 * x + 0.85 * y + 1.60
size(640, 640)
background(0)

x = 0
y = 0

for _ in range(100000):
    xt = 0
    yt = 0
    r = random(100)
    
    if r <= 1:
        xt = 0
        yt = 0.16*y
    elif r <= 8:
        xt = 0.20*x - 0.26*y
        yt = 0.23*x + 0.22*y + 1.60
    elif r <= 15:
        xt = -0.15*x + 0.28*y
        yt =    0.26*x + 0.24*y + 0.44
    else:
        xt =    0.85*x + 0.04*y
        yt = -0.04*x + 0.85*y + 1.60
    
    x = xt
    y = yt

    m = round(width/2 + 60*x)
    n = height-round(60*y)

    set(m, n, "#00ff00")
    x = xt
    y = yt

    m = round(width / 2 + 60 * x)
    n = height - round(60 * y)

    set(m, n, "#00ff00")

```

### python_code_2.txt
```python
import random
from PIL import Image


class BarnsleyFern(object):
    def __init__(self, img_width, img_height, paint_color=(0, 150, 0),
                 bg_color=(255, 255, 255)):
        self.img_width, self.img_height = img_width, img_height
        self.paint_color = paint_color
        self.x, self.y = 0, 0
        self.age = 0

        self.fern = Image.new('RGB', (img_width, img_height), bg_color)
        self.pix = self.fern.load()
        self.pix[self.scale(0, 0)] = paint_color

    def scale(self, x, y):
        h = (x + 2.182)*(self.img_width - 1)/4.8378
        k = (9.9983 - y)*(self.img_height - 1)/9.9983
        return h, k

    def transform(self, x, y):
        rand = random.uniform(0, 100)
        if rand < 1:
            return 0, 0.16*y
        elif 1 <= rand < 86:
            return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
        elif 86 <= rand < 93:
            return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
        else:
            return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

    def iterate(self, iterations):
        for _ in range(iterations):
            self.x, self.y = self.transform(self.x, self.y)
            self.pix[self.scale(self.x, self.y)] = self.paint_color
        self.age += iterations

fern = BarnsleyFern(500, 500)
fern.iterate(1000000)
fern.fern.show()

```

