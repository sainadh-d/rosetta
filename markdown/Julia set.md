# Julia set

## Task Link
[Rosetta Code - Julia set](https://rosettacode.org/wiki/Julia_set)

## Java Code
### java_code_1.txt
```java
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class JuliaSet extends JPanel {
    private static final int MAX_ITERATIONS = 300;
    private static final double ZOOM = 1;
    private static final double CX = -0.7;
    private static final double CY = 0.27015;
    private static final double MOVE_X = 0;
    private static final double MOVE_Y = 0;

    public JuliaSet() {
        setPreferredSize(new Dimension(800, 600));
        setBackground(Color.white);
    }

    void drawJuliaSet(Graphics2D g) {
        int w = getWidth();
        int h = getHeight();
        BufferedImage image = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);

        for (int x = 0; x < w; x++) {
            for (int y = 0; y < h; y++) {
                double zx = 1.5 * (x - w / 2) / (0.5 * ZOOM * w) + MOVE_X;
                double zy = (y - h / 2) / (0.5 * ZOOM * h) + MOVE_Y;
                float i = MAX_ITERATIONS;
                while (zx * zx + zy * zy < 4 && i > 0) {
                    double tmp = zx * zx - zy * zy + CX;
                    zy = 2.0 * zx * zy + CY;
                    zx = tmp;
                    i--;
                }
                int c = Color.HSBtoRGB((MAX_ITERATIONS / i) % 1, 1, i > 0 ? 1 : 0);
                image.setRGB(x, y, c);
            }
        }
        g.drawImage(image, 0, 0, null);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        drawJuliaSet(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Julia Set");
            f.setResizable(false);
            f.add(new JuliaSet(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.stream.IntStream;

public class JuliaSet extends JPanel {
    private static final int MAX_ITERATIONS = 300;
    private static final double ZOOM = 1;
    private static final double CX = -0.7;
    private static final double CY = 0.27015;
    private static final double MOVE_X = 0;
    private static final double MOVE_Y = 0;

    public JuliaSet() {
        setPreferredSize(new Dimension(800, 600));
        setBackground(Color.white);
    }

    void drawJuliaSet(Graphics2D g) {
        int w = getWidth();
        int h = getHeight();
        BufferedImage image = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);

        IntStream.range(0, w).parallel().forEach(x -> {
            IntStream.range(0, h).parallel().forEach(y -> {
                double zx = 1.5 * (x - w / 2) / (0.5 * ZOOM * w) + MOVE_X;
                double zy = (y - h / 2) / (0.5 * ZOOM * h) + MOVE_Y;
                float i = MAX_ITERATIONS;
                while (zx * zx + zy * zy < 4 && i > 0) {
                    double tmp = zx * zx - zy * zy + CX;
                    zy = 2.0 * zx * zy + CY;
                    zx = tmp;
                    i--;
                }
                int c = Color.HSBtoRGB((MAX_ITERATIONS / i) % 1, 1, i > 0 ? 1 : 0);
                image.setRGB(x, y, c);
            });
        });
        g.drawImage(image, 0, 0, null);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        drawJuliaSet(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Julia Set");
            f.setResizable(false);
            f.add(new JuliaSet(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_3.txt
```java
float cX = -0.7;
float cY = 0.27015;
float zx, zy;
float maxIter = 300;

void setup() {
  size(640, 480);
}

void draw() {
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      zx = 1.5 * (x - width / 2) / (0.5 * width);
      zy = (y - height / 2) / (0.5 * height);
      float i = maxIter;
      while (zx * zx + zy * zy < 4 && i > 0) {
        float tmp = zx * zx - zy * zy + cX;
        zy = 2.0 * zx * zy + cY;
        zx = tmp;
        i -= 1;
      }
     colorMode(HSB); 
     color c = color(i / maxIter * 255, 255,  i > 1 ? 255 : 0);
     set(x, y, c);
    }
  }
  noLoop();
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division

cX = -0.7
cY = 0.27015
maxIter = 300

def setup():
    size(640, 480)

def draw():
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * width)
            zy = (y - height / 2) / (0.5 * height)
            i = maxIter
            while zx * zx + zy * zy < 4 and i > 0:
                tmp = zx * zx - zy * zy + cX
                zy = 2.0 * zx * zy + cY
                zx = tmp
                i -= 1
            colorMode(HSB)
            c = color(i / maxIter * 255, 255, 255 if i > 1 else 0)
            set(x, y, c)

```

### python_code_2.txt
```python
from PIL import Image

if __name__ == "__main__":
	w, h, zoom = 800,600,1
	bitmap = Image.new("RGB", (w, h), "white")
	pix = bitmap.load()
 
	cX, cY = -0.7, 0.27015
	moveX, moveY = 0.0, 0.0
	maxIter = 255
 
	for x in range(w):
		for y in range(h):
			zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX
			zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY
			i = maxIter
			while zx*zx + zy*zy < 4 and i > 1:
				tmp = zx*zx - zy*zy + cX
				zy,zx = 2.0*zx*zy + cY, tmp
				i -= 1
			# convert byte to RGB (3 bytes), kinda magic to get nice colors
			pix[x][y] = (i << 21) + (i << 10) + i*8
 
	bitmap.show()

```

### python_code_3.txt
```python
"""
Solution from:
https://codereview.stackexchange.com/questions/210271/generating-julia-set
"""
from functools import partial
from numbers import Complex
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


def douady_hubbard_polynomial(z: Complex,
                              c: Complex) -> Complex:
    """
    Monic and centered quadratic complex polynomial
    https://en.wikipedia.org/wiki/Complex_quadratic_polynomial#Map
    """
    return z ** 2 + c


def julia_set(mapping: Callable[[Complex], Complex],
              *,
              min_coordinate: Complex,
              max_coordinate: Complex,
              width: int,
              height: int,
              iterations_count: int = 256,
              threshold: float = 2.) -> np.ndarray:
    """
    As described in https://en.wikipedia.org/wiki/Julia_set
    :param mapping: function defining Julia set
    :param min_coordinate: bottom-left complex plane coordinate
    :param max_coordinate: upper-right complex plane coordinate
    :param height: pixels in vertical axis
    :param width: pixels in horizontal axis
    :param iterations_count: number of iterations
    :param threshold: if the magnitude of z becomes greater
    than the threshold we assume that it will diverge to infinity
    :return: 2D pixels array of intensities
    """
    im, re = np.ogrid[min_coordinate.imag: max_coordinate.imag: height * 1j,
                      min_coordinate.real: max_coordinate.real: width * 1j]
    z = (re + 1j * im).flatten()

    live, = np.indices(z.shape)  # indexes of pixels that have not escaped
    iterations = np.empty_like(z, dtype=int)

    for i in range(iterations_count):
        z_live = z[live] = mapping(z[live])
        escaped = abs(z_live) > threshold
        iterations[live[escaped]] = i
        live = live[~escaped]
        if live.size == 0:
            break
    else:
        iterations[live] = iterations_count

    return iterations.reshape((height, width))


if __name__ == '__main__':
    mapping = partial(douady_hubbard_polynomial,
                      c=-0.7 + 0.27015j)  # type: Callable[[Complex], Complex]

    image = julia_set(mapping,
                      min_coordinate=-1.5 - 1j,
                      max_coordinate=1.5 + 1j,
                      width=800,
                      height=600)
    plt.axis('off')
    plt.imshow(image,
               cmap='nipy_spectral_r',
               origin='lower')
    plt.show()

```

