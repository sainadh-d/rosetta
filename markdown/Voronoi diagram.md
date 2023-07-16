# Voronoi diagram

## Task Link
[Rosetta Code - Voronoi diagram](https://rosettacode.org/wiki/Voronoi_diagram)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

public class Voronoi extends JFrame {
	static double p = 3;
	static BufferedImage I;
	static int px[], py[], color[], cells = 100, size = 1000;

	public Voronoi() {
		super("Voronoi Diagram");
		setBounds(0, 0, size, size);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		int n = 0;
		Random rand = new Random();
		I = new BufferedImage(size, size, BufferedImage.TYPE_INT_RGB);
		px = new int[cells];
		py = new int[cells];
		color = new int[cells];
		for (int i = 0; i < cells; i++) {
			px[i] = rand.nextInt(size);
			py[i] = rand.nextInt(size);
			color[i] = rand.nextInt(16777215);

		}
		for (int x = 0; x < size; x++) {
			for (int y = 0; y < size; y++) {
				n = 0;
				for (byte i = 0; i < cells; i++) {
					if (distance(px[i], x, py[i], y) < distance(px[n], x, py[n], y)) {
						n = i;

					}
				}
				I.setRGB(x, y, color[n]);

			}
		}

		Graphics2D g = I.createGraphics();
		g.setColor(Color.BLACK);
		for (int i = 0; i < cells; i++) {
			g.fill(new Ellipse2D .Double(px[i] - 2.5, py[i] - 2.5, 5, 5));
		}

		try {
			ImageIO.write(I, "png", new File("voronoi.png"));
		} catch (IOException e) {

		}

	}

	public void paint(Graphics g) {
		g.drawImage(I, 0, 0, this);
	}

	static double distance(int x1, int x2, int y1, int y2) {
		double d;
	    d = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)); // Euclidian
	//  d = Math.abs(x1 - x2) + Math.abs(y1 - y2); // Manhattan
	//  d = Math.pow(Math.pow(Math.abs(x1 - x2), p) + Math.pow(Math.abs(y1 - y2), p), (1 / p)); // Minkovski
	  	return d;
	}

	public static void main(String[] args) {
		new Voronoi().setVisible(true);
	}
}

```

### java_code_2.txt
```java
void setup() {
  size(500, 500);
  generateVoronoiDiagram(width, height, 25);
  saveFrame("VoronoiDiagram.png");
}

void generateVoronoiDiagram(int w, int h, int num_cells) {
  int nx[] = new int[num_cells];
  int ny[] = new int[num_cells];
  int nr[] = new int[num_cells];
  int ng[] = new int[num_cells];
  int nb[] = new int[num_cells];
  for (int n=0; n < num_cells; n++) {
    nx[n]=int(random(w));
    ny[n]=int(random(h));
    nr[n]=int(random(256));
    ng[n]=int(random(256));
    nb[n]=int(random(256));
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        float dmin = dist(0, 0, w - 1, h - 1);
        int j = -1;
        for (int i=0; i < num_cells; i++) {
          float d = dist(0, 0, nx[i] - x, ny[i] - y);
          if (d < dmin) {
            dmin = d;
            j = i;
          }
        }
        set(x, y, color(nr[j], ng[j], nb[j]));
      }
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    size(500, 500)
    generate_voronoi_diagram(width, height, 25)
    saveFrame("VoronoiDiagram.png")

def generate_voronoi_diagram(w, h, num_cells):
    nx, ny, nr, ng, nb = [], [], [], [], [] 
    for i in range(num_cells):
        nx.append(int(random(w)))
        ny.append(int(random(h)))
        nr.append(int(random(256)))
        ng.append(int(random(256)))
        nb.append(int(random(256)))
    for y in range(h):
        for x in range(w):
            dmin = dist(0, 0, w - 1, h - 1)
            j = -1
            for i in range(num_cells):
                d = dist(0, 0, nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            set(x, y, color(nr[j], ng[j], nb[j]))

```

### python_code_2.txt
```python
from PIL import Image
import random
import math

def generate_voronoi_diagram(width, height, num_cells):
	image = Image.new("RGB", (width, height))
	putpixel = image.putpixel
	imgx, imgy = image.size
	nx = []
	ny = []
	nr = []
	ng = []
	nb = []
	for i in range(num_cells):
		nx.append(random.randrange(imgx))
		ny.append(random.randrange(imgy))
		nr.append(random.randrange(256))
		ng.append(random.randrange(256))
		nb.append(random.randrange(256))
	for y in range(imgy):
		for x in range(imgx):
			dmin = math.hypot(imgx-1, imgy-1)
			j = -1
			for i in range(num_cells):
				d = math.hypot(nx[i]-x, ny[i]-y)
				if d < dmin:
					dmin = d
					j = i
			putpixel((x, y), (nr[j], ng[j], nb[j]))
	image.save("VoronoiDiagram.png", "PNG")
        image.show()
	
generate_voronoi_diagram(500, 500, 25)

```

### python_code_3.txt
```python
import numpy as np
from PIL import Image
from scipy.spatial import KDTree

def generate_voronoi_diagram(X, Y, num_cells):
    # Random colors and points
    colors = np.random.randint((256, 256, 256), size=(num_cells, 3), dtype=np.uint8)
    points = np.random.randint((Y, X), size=(num_cells, 2))

    # Construct a list of all possible (y,x) coordinates
    idx = np.indices((Y, X))
    coords = np.moveaxis(idx, 0, -1).reshape((-1, 2))

    # Find the closest point to each coordinate
    _d, labels = KDTree(points).query(coords)
    labels = labels.reshape((Y, X))

    # Export an RGB image
    rgb = colors[labels]
    img = Image.fromarray(rgb, mode='RGB')
    img.save('VoronoiDiagram.png', 'PNG')
    img.show()
    return rgb

```

