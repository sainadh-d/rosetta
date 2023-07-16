# Plasma effect

## Task Link
[Rosetta Code - Plasma effect](https://rosettacode.org/wiki/Plasma_effect)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import static java.awt.image.BufferedImage.*;
import static java.lang.Math.*;
import javax.swing.*;

public class PlasmaEffect extends JPanel {
    float[][] plasma;
    float hueShift = 0;
    BufferedImage img;

    public PlasmaEffect() {
        Dimension dim = new Dimension(640, 640);
        setPreferredSize(dim);
        setBackground(Color.white);

        img = new BufferedImage(dim.width, dim.height, TYPE_INT_RGB);
        plasma = createPlasma(dim.height, dim.width);

        // animate about 24 fps and shift hue value with every frame
        new Timer(42, (ActionEvent e) -> {
            hueShift = (hueShift + 0.02f) % 1;
            repaint();
        }).start();
    }

    float[][] createPlasma(int w, int h) {
        float[][] buffer = new float[h][w];

        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++) {

                double value = sin(x / 16.0);
                value += sin(y / 8.0);
                value += sin((x + y) / 16.0);
                value += sin(sqrt(x * x + y * y) / 8.0);
                value += 4; // shift range from -4 .. 4 to 0 .. 8
                value /= 8; // bring range down to 0 .. 1

                // requires VM option -ea
                assert (value >= 0.0 && value <= 1.0) : "Hue value out of bounds";

                buffer[y][x] = (float) value;
            }
        return buffer;
    }

    void drawPlasma(Graphics2D g) {
        int h = plasma.length;
        int w = plasma[0].length;
        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++) {
                float hue = hueShift + plasma[y][x] % 1;
                img.setRGB(x, y, Color.HSBtoRGB(hue, 1, 1));
            }
        g.drawImage(img, 0, 0, null);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawPlasma(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Plasma Effect");
            f.setResizable(false);
            f.add(new PlasmaEffect(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
/**
 Plasmas with Palette Looping
 https://lodev.org/cgtutor/plasma.html#Plasmas_with_Palette_Looping_
 */

int pal[] = new int[128];
int[] buffer;
float r = 42, g = 84, b = 126;
boolean rd, gd, bd;

void setup() {
  size(600, 600);
  frameRate(25);
  buffer = new int[width*height];
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      buffer[x+y*width] = int(((128+(128*sin(x/32.0)))
        +(128+(128*cos(y/32.0))) 
        +(128+(128*sin(sqrt((x*x+y*y))/32.0))))/4);
    }
  }
}

void draw() {
  if (r > 128) rd = true;
  if (!rd) r++;
  else r--;
  if (r < 0) rd = false;
  if (g > 128) gd = true;
  if (!gd) g++;
  else g--;
  if (r < 0) gd = false; 
  if (b > 128) bd = true;
  if (!bd) b++;
  else b--;
  if (b < 0){ bd = false;}
  float s_1, s_2;
  for (int i = 0; i < 128; i++) {
    s_1 = sin(i*PI/25);
    s_2 = sin(i*PI/50+PI/4);
    pal[i] = color(r+s_1*128, g+s_2*128, b+s_1*128);
  }
  loadPixels();
  for (int i = 0; i < buffer.length; i++) {                    
    pixels[i] =  pal[(buffer[i]+frameCount)&127];
  }
  updatePixels();
}

```

## Python Code
### python_code_1.txt
```python
"""
Plasmas with Palette Looping
https://lodev.org/cgtutor/plasma.html#Plasmas_with_Palette_Looping_
"""

pal = [0] * 128
r = 42
g = 84
b = 126
rd = gd = bd = False

def setup():
    global buffer
    size(600, 600)
    frameRate(25)
    buffer = [None] * width * height
    for x in range(width):
        for y in range(width):
            value = int(((128 + (128 * sin(x / 32.0)))
                         + (128 + (128 * cos(y / 32.0)))
                         + (128 + (128 * sin(sqrt((x * x + y * y)) / 32.0)))) / 4)
            buffer[x + y * width] = value

def draw():
    global r, g, b, rd, gd, bd
    if r > 128: rd = True
    if not rd: r += 1
    else: r-=1
    if r < 0: rd = False
    if g > 128: gd = True
    if not gd: g += 1
    else: g- = 1
    if r < 0: gd = False 
    if b > 128: bd = True
    if not bd: b += 1
    else: b- = 1
    if b < 0: bd = False
 
    for i in range(128):
          s_1 = sin(i * PI / 25)
          s_2 = sin(i * PI / 50 + PI / 4)
          pal[i] = color(r + s_1 * 128, g + s_2 * 128, b + s_1 * 128)

    loadPixels()
    for i, b in enumerate(buffer):
          pixels[i] = pal[(b + frameCount) % 127]
    updatePixels()

```

### python_code_2.txt
```python
import math
import colorsys
from PIL import Image

def plasma (w, h):
	out = Image.new("RGB", (w, h))
	pix = out.load()
	for x in range (w):
		for y in range(h):
			hue = 4.0 + math.sin(x / 19.0) + math.sin(y / 9.0) \
				+ math.sin((x + y) / 25.0) + math.sin(math.sqrt(x**2.0 + y**2.0) / 8.0)
			hsv = colorsys.hsv_to_rgb(hue/8.0, 1, 1)
			pix[x, y] = tuple([int(round(c * 255.0)) for c in hsv])
	return out

if __name__=="__main__":
	im = plasma(400, 400)
	im.show()

```

