# Mandelbrot set

## Task Link
[Rosetta Code - Mandelbrot set](https://rosettacode.org/wiki/Mandelbrot_set)

## Java Code
### java_code_1.txt
```java
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;

public class Mandelbrot extends JFrame {

    private final int MAX_ITER = 570;
    private final double ZOOM = 150;
    private BufferedImage I;
    private double zx, zy, cX, cY, tmp;

    public Mandelbrot() {
        super("Mandelbrot Set");
        setBounds(100, 100, 800, 600);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        I = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_RGB);
        for (int y = 0; y < getHeight(); y++) {
            for (int x = 0; x < getWidth(); x++) {
                zx = zy = 0;
                cX = (x - 400) / ZOOM;
                cY = (y - 300) / ZOOM;
                int iter = MAX_ITER;
                while (zx * zx + zy * zy < 4 && iter > 0) {
                    tmp = zx * zx - zy * zy + cX;
                    zy = 2.0 * zx * zy + cY;
                    zx = tmp;
                    iter--;
                }
                I.setRGB(x, y, iter | (iter << 8));
            }
        }
    }

    @Override
    public void paint(Graphics g) {
        g.drawImage(I, 0, 0, this);
    }

    public static void main(String[] args) {
        new Mandelbrot().setVisible(true);
    }
}

```

### java_code_2.txt
```java
import static java.awt.Color.HSBtoRGB;
import static java.awt.Color.black;
import static java.awt.event.KeyEvent.VK_BACK_SLASH;
import static java.awt.event.KeyEvent.VK_ESCAPE;
import static java.awt.image.BufferedImage.TYPE_INT_RGB;
import static java.lang.Integer.signum;
import static java.lang.Math.abs;
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.System.currentTimeMillis;
import static java.util.Locale.ROOT;

import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Insets;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.util.function.Consumer;
import java.util.function.Predicate;

import javax.swing.JFrame;

/* 
 *      click: point to center
 * ctrl-click: point to origin
 *       drag: point to mouse release point
 *  ctrl-drag: point to origin + zoom
 * back-slash: back to previous point      
 *        esc: back to previous zoom point - zoom     
 */

public class Mandelbrot extends JFrame {
	private static final long serialVersionUID = 1L;
	
	private Insets insets;
	private int width, height;
	private double widthHeightRatio;
	private int minX, minY;
	private double Zoom;
		
	private int mpX, mpY, mdX, mdY;
	private boolean isCtrlDown, ctrl;
	private Stack stack = new Stack();
	
	private BufferedImage image;
	private boolean newImage = true;
	
	public static void main(String[] args) {
		new Mandelbrot(800, 600); // (800, 600), (1024, 768), (1600, 900), (1920, 1080)
		//new Mandelbrot(800, 600, 4.5876514379235943e-09, -0.6092161175392330, -0.4525577210859453);
		//new Mandelbrot(800, 600, 5.9512354925205320e-10, -0.6092146769531246, -0.4525564820098262);
		//new Mandelbrot(800, 600, 6.7178527589983420e-08, -0.7819036465400592, -0.1298363433443265);
		//new Mandelbrot(800, 600, 4.9716091454775210e-09, -0.7818800036717134, -0.1298044093748981);
		//new Mandelbrot(800, 600, 7.9333341281639390e-06, -0.7238770725243187, -0.2321214232559487); 
		/*
		new Mandelbrot(800, 600, new double[][] {
			{5.0000000000000000e-03, -2.6100000000000000, -1.4350000000000000}, // done!
			{3.5894206549118390e-04, -0.7397795969773300, -0.4996473551637279}, // done!
			{3.3905106941862460e-05, -0.6270410477828043, -0.4587021918164572}, // done!
			{6.0636337351945460e-06, -0.6101531446039512, -0.4522561221394852}, // done!
			{1.5502741161769430e-06, -0.6077214060084073, -0.4503995886987711}, // done!
		});
		//*/
	}
	
	public Mandelbrot(int width, int height) {
		this(width, height, .005, -2.61, -1.435);
	}
	
	public Mandelbrot(int width, int height, double Zoom, double r, double i) {
		this(width, height, new double[] {Zoom, r, i});
	}
	
	public Mandelbrot(int width, int height, double[] ... points) {
		super("Mandelbrot Set");
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		Dimension screen = getToolkit().getScreenSize();
		setBounds(
			rint((screen.getWidth() - width) / 2),
			rint((screen.getHeight() - height) / 2),
			width,
			height
		);
		addMouseListener(mouseAdapter);
		addMouseMotionListener(mouseAdapter);
		addKeyListener(keyAdapter);
		Point point = stack.push(points);
		this.Zoom = point.Zoom;
		this.minX = point.minX;
		this.minY = point.minY;
		setVisible(true);
		insets = getInsets();
		this.width = width -= insets.left + insets.right;
		this.height = height -= insets.top + insets.bottom;
		widthHeightRatio = (double) width / height;
	}
	
	private int rint(double d) {
		return (int) Math.rint(d); // half even
	}

	private void repaint(boolean newImage) {
		this.newImage = newImage;
		repaint();
	}

	private MouseAdapter mouseAdapter = new MouseAdapter() {
		public void mouseClicked(MouseEvent e) {
			stack.push(false);
			if (!ctrl) {
				minX -= width / 2 ;
				minY -= height / 2;
			}
			minX += e.getX() - insets.left;
			minY += e.getY() - insets.top;
			ctrl = false;
			repaint(true);
	 	}
		public void mousePressed(MouseEvent e) {
			mpX = e.getX();
			mpY = e.getY();
			ctrl = isCtrlDown;
		}
		public void mouseDragged(MouseEvent e) {
			if (!ctrl) return;
			setMdCoord(e);
			repaint();
		}
		private void setMdCoord(MouseEvent e) {
			int dx = e.getX() - mpX;
			int dy = e.getY() - mpY;
			mdX = mpX + max(abs(dx), rint(abs(dy) * widthHeightRatio) * signum(dx));
			mdY = mpY + max(abs(dy), rint(abs(dx) / widthHeightRatio) * signum(dy));
			acceptIf(insets.left, ge(mdX), setMdXY); 
			acceptIf(insets.top,  ge(mdY), setMdYX);
			acceptIf(insets.left+width-1, le(mdX), setMdXY); 
			acceptIf(insets.top+height-1, le(mdY), setMdYX);
		}
		private void acceptIf(int value, Predicate<Integer> p, Consumer<Integer> c) { if (p.test(value)) c.accept(value); }
		private Predicate<Integer> ge(int md) { return v-> v >= md; }
		private Predicate<Integer> le(int md) { return v-> v <= md; }
		private Consumer<Integer> setMdXY = v-> mdY = mpY + rint(abs((mdX=v)-mpX) / widthHeightRatio) * signum(mdY-mpY);
		private Consumer<Integer> setMdYX = v-> mdX = mpX + rint(abs((mdY=v)-mpY) * widthHeightRatio) * signum(mdX-mpX);
		public void mouseReleased(MouseEvent e) {
			if (e.getX() == mpX && e.getY() == mpY) return; 
			stack.push(ctrl);
			if (!ctrl) {
				minX += mpX - (mdX = e.getX());
				minY += mpY - (mdY = e.getY());
			}
			else {
				setMdCoord(e);
				if (mdX < mpX) { int t=mpX; mpX=mdX; mdX=t; } 
				if (mdY < mpY) { int t=mpY; mpY=mdY; mdY=t; } 
				minX += mpX - insets.left;
				minY += mpY - insets.top;
				double rZoom = (double) width / abs(mdX - mpX);
				minX *= rZoom;
				minY *= rZoom;
				Zoom /= rZoom;
			}
			ctrl = false;
			repaint(true);		
		}
	};
	
	private KeyAdapter keyAdapter = new KeyAdapter() {
		public void keyPressed(KeyEvent e) {
			isCtrlDown = e.isControlDown();
		}
		public void keyReleased(KeyEvent e) {
			isCtrlDown = e.isControlDown();
		}
		public void keyTyped(KeyEvent e) {
			char c = e.getKeyChar();
			boolean isEsc = c == VK_ESCAPE;
			if (!isEsc && c != VK_BACK_SLASH) return;
			repaint(stack.pop(isEsc));
		}
	};
	
	private class Point {
		public boolean type;
		public double Zoom;
		public int minX;
		public int minY;
		Point(boolean type, double Zoom, int minX, int minY) {
			this.type = type;
			this.Zoom = Zoom;
			this.minX = minX;
			this.minY = minY;
		}
	}
	private class Stack extends java.util.Stack<Point> {
		private static final long serialVersionUID = 1L;
		public Point push(boolean type) {
			return push(type, Zoom, minX, minY);
		}
		public Point push(boolean type, double ... point) {
			double Zoom = point[0];
			return push(type, Zoom, rint(point[1]/Zoom), rint(point[2]/Zoom));
		}
		public Point push(boolean type, double Zoom, int minX, int minY) {
			return push(new Point(type, Zoom, minX, minY));
		}
		public Point push(double[] ... points) {
			Point lastPoint = push(false, points[0]);
			for (int i=0, e=points.length-1; i<e; i+=1) {
				double[] point = points[i];
				lastPoint = push(point[0] != points[i+1][0], point);
				done(printPoint(lastPoint));
			}
			return lastPoint;
		}
		public boolean pop(boolean type) {
			for (;;) {
				if (empty()) return false;
				Point d = super.pop();
				Zoom = d.Zoom;
				minX = d.minX;
				minY = d.minY;
				if (!type || d.type) return true;
			}
		}
	}
	
	@Override
	public void paint(Graphics g) {
		if (newImage) newImage();
		g.drawImage(image, insets.left, insets.top, this);
		//g.drawLine(insets.left+width/2, insets.top+0,        insets.left+width/2, insets.top+height);
		//g.drawLine(insets.left+0,       insets.top+height/2, insets.left+width,   insets.top+height/2);
		if (!ctrl) return;
		g.drawRect(min(mpX, mdX), min(mpY, mdY), abs(mpX - mdX), abs(mpY - mdY));
	}

	private void newImage() {
		long milli = printPoint();
		image = new BufferedImage(width, height, TYPE_INT_RGB);
		int maxX = minX + width;
		int maxY = minY + height;
		for (int x = minX; x < maxX; x+=1) {
			double r = x * Zoom;
			for (int y = minY; y < maxY; y+=1) {
				double i = y * Zoom;
				//System.out.printf("%+f%+fi\n", r, i);
				//             0f    1/6f  1/3f 1/2f 2/3f    5/6f
				//straight -> red  yellow green cian blue magenta <- reverse 
				image.setRGB(x-minX, y-minY, color(r, i, 360, false, 2/3f));
			}
		}
		newImage = false;
		done(milli);
	}

	private long printPoint() {
		return printPoint(Zoom, minX, minY);
	}
	private long printPoint(Point point) {
		return printPoint(point.Zoom, point.minX, point.minY);
	}
	private long printPoint(double Zoom, int minX, int minY) {
		return printPoint(Zoom, minX*Zoom, minY*Zoom);
	}
	private long printPoint(Object ... point) {
		System.out.printf(ROOT,	"{%.16e, %.16g, %.16g},", point);
		return currentTimeMillis();
	}
	
	private void done(long milli) {
		milli = currentTimeMillis() - milli;
		System.out.println(" // " + milli + "ms done!");
	}

	private int color(double r0, double i0, int max, boolean straight, float shift) {
		int n = -1;
		double r=0, i=0, r2=0, i2=0;
		do {
			i = r*(i+i) + i0;
			r = r2-i2 + r0;
			r2 = r*r;
			i2 = i*i;
		}
		while (++n < max && r2 + i2 < 4); 
		return n == max
			? black.getRGB()
			: HSBtoRGB(shift + (float) (straight ? n : max-n) / max * 11/12f + (straight ? 0f : 1/12f), 1, 1)
		;		
	}
}

```

### java_code_3.txt
```java
double x, y, zr, zi, zr2, zi2, cr, ci, n;
double zmx1, zmx2, zmy1, zmy2, f, di, dj;
double fn1, fn2, fn3, re, gr, bl, xt, yt, i, j;
 
void setup() {
  size(500, 500);
  di = 0;
  dj = 0;
  f = 10;
  fn1 = random(20); 
  fn2 = random(20); 
  fn3 = random(20);
  zmx1 = int(width / 4);
  zmx2 = 2;
  zmy1 = int(height / 4);
  zmy2 = 2;
}
 
void draw() {
  if (i <= width) i++;
  x =  (i +  di)/ zmx1 - zmx2;
  for ( j = 0; j <= height; j++) {
    y = zmy2 - (j + dj) / zmy1;
    zr = 0;
    zi = 0;
    zr2 = 0; 
    zi2 = 0; 
    cr = x;   
    ci = y;  
    n = 1;
    while (n < 200 && (zr2 + zi2) < 4) {
      zi2 = zi * zi;
      zr2 = zr * zr;
      zi = 2 * zi * zr + ci;
      zr = zr2 - zi2 + cr;
      n++;
    }  
    re = (n * fn1) % 255;
    gr = (n * fn2) % 255;
    bl = (n * fn3) % 255;
    stroke((float)re, (float)gr, (float)bl); 
    point((float)i, (float)j);
  }
}
 
void mousePressed() {
  background(200); 
  xt = mouseX;
  yt = mouseY;
  di = di + xt - float(width / 2);
  dj = dj + yt - float(height / 2);
  zmx1 = zmx1 * f;
  zmx2 = zmx2 * (1 / f);
  zmy1 = zmy1 * f;
  zmy2 = zmy2 * (1 / f);
  di = di * f;
  dj = dj * f;
  i = 0;
  j = 0;
}

```

## Python Code
### python_code_1.txt
```python
i = di = dj = 0
fn1, fn2, fn3 = random(20), random(20), random(20)
f = 10
    
def setup():
    global zmx1, zmx2, zmy1, zmy2
    size(500, 500)
    zmx1 = int(width / 4)
    zmx2 = 2
    zmy1 = int(height / 4)
    zmy2 = 2


def draw():
    global i

    if i <= width:
        i += 1
    x = float(i + di) / zmx1 - zmx2
    for j in range(height + 1):
        y = zmy2 - float(j + dj) / zmy1
        zr = zi = zr2 = zi2 = 0
        cr, ci = x, y
        n = 1
        while n < 200 and (zr2 + zi2) < 4:
            zi2 = zi * zi
            zr2 = zr * zr
            zi = 2 * zi * zr + ci
            zr = zr2 - zi2 + cr
            n += 1

        re = (n * fn1) % 255
        gr = (n * fn2) % 255
        bl = (n * fn3) % 255
        stroke(re, gr, bl)
        point(i, j)


def mousePressed():
    global zmx1, zmx2, zmy1, zmy2, di, dj
    global i, j
    background(200)
    xt, yt = mouseX, mouseY
    di = di + xt - width / 2.
    dj = dj + yt - height / 2.
    zmx1 = zmx1 * f
    zmx2 = zmx2 * (1. / f)
    zmy1 = zmy1 * f
    zmy2 = zmy2 * (1. / f)
    di, dj = di * f, dj * f
    i = j = 0

```

### python_code_10.txt
```python
from functools import reduce

def mandelbrot(x, y, c): return ' *'[abs(reduce(lambda z, _: z*z + c, range(99), 0)) < 2]

print('\n'.join(''.join(mandelbrot(x, y, x/50 + y/50j) for x in range(-100, 25)) for y in range(-50, 50)))

```

### python_code_2.txt
```python
# Python 3.0+ and 2.5+
try:
    from functools import reduce
except:
    pass


def mandelbrot(a):
    return reduce(lambda z, _: z * z + a, range(50), 0)

def step(start, step, iterations):
    return (start + (i * step) for i in range(iterations))

rows = (("*" if abs(mandelbrot(complex(x, y))) < 2 else " "
        for x in step(-2.0, .0315, 80))
        for y in step(1, -.05, 41))

print("\n".join("".join(row) for row in rows))

```

### python_code_3.txt
```python
import math

def mandelbrot(z , c , n=40):
    if abs(z) > 1000:
        return float("nan")
    elif n > 0:
        return mandelbrot(z ** 2 + c, c, n - 1) 
    else:
        return z ** 2 + c

print("\n".join(["".join(["#" if not math.isnan(mandelbrot(0, x + 1j * y).real) else " "
                 for x in [a * 0.02 for a in range(-80, 30)]]) 
                 for y in [a * 0.05 for a in range(-20, 20)]])
     )

```

### python_code_4.txt
```python
from pylab import *
from numpy import NaN

def m(a):
	z = 0
	for n in range(1, 100):
		z = z**2 + a
		if abs(z) > 2:
			return n
	return NaN

X = arange(-2, .5, .002)
Y = arange(-1,  1, .002)
Z = zeros((len(Y), len(X)))

for iy, y in enumerate(Y):
	print (iy, "of", len(Y))
	for ix, x in enumerate(X):
		Z[iy,ix] = m(x + 1j * y)

imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")
savefig("mandelbrot_python.svg")
show()

```

### python_code_5.txt
```python
import matplotlib.pyplot as plt
import numpy as np

npts = 300
max_iter = 100

X = np.linspace(-2, 1, 2 * npts)
Y = np.linspace(-1, 1, npts)

#broadcast X to a square array
C = X[:, None] + 1J * Y
#initial value is always zero
Z = np.zeros_like(C)

exit_times = max_iter * np.ones(C.shape, np.int32)
mask = exit_times > 0

for k in range(max_iter):
    Z[mask] = Z[mask] * Z[mask] + C[mask]
    mask, old_mask = abs(Z) < 2, mask
    #use XOR to detect the area which has changed 
    exit_times[mask ^ old_mask] = k

plt.imshow(exit_times.T,
           cmap=plt.cm.prism,
           extent=(X.min(), X.max(), Y.min(), Y.max()))
plt.show()

```

### python_code_6.txt
```python
import numpy as np
import matplotlib.pyplot as plt

d, h = 800, 500  # pixel density (= image width) and image height
n, r = 200, 500  # number of iterations and escape radius (r > 2)

direction, height = 45, 1.5  # direction and height of the incoming light
v = np.exp(direction / 180 * np.pi * 1j)  # unit 2D vector in this direction

x = np.linspace(0, 2, num=d+1)
y = np.linspace(0, 2 * h / d, num=h+1)

A, B = np.meshgrid(x - 1, y - h / d)
C = (2.0 + 1.0j) * (A + B * 1j) - 0.5

Z, dZ, ddZ = np.zeros_like(C), np.zeros_like(C), np.zeros_like(C)
D, T = np.zeros(C.shape), np.zeros(C.shape)

for k in range(n):
    M = Z.real ** 2 + Z.imag ** 2 < r ** 2
    Z[M], dZ[M], ddZ[M] = Z[M] ** 2 + C[M], 2 * Z[M] * dZ[M] + 1, 2 * (dZ[M] ** 2 + Z[M] * ddZ[M])

N = abs(Z) > 2  # exterior distance estimation
D[N] = np.log(abs(Z[N])) * abs(Z[N]) / abs(dZ[N])

plt.imshow(D ** 0.1, cmap=plt.cm.twilight_shifted, origin="lower")
plt.savefig("Mandelbrot_distance_est.png", dpi=200)

N = abs(Z) > 2  # normal map effect 1 (potential function)
U = Z[N] / dZ[N]  # normal vectors to the equipotential lines
U, S = U / abs(U), 1 + np.sin(100 * np.angle(U)) / 10  # unit normal vectors and stripes
T[N] = np.maximum((U.real * v.real + U.imag * v.imag + S * height) / (1 + height), 0)

plt.imshow(T ** 1.0, cmap=plt.cm.bone, origin="lower")
plt.savefig("Mandelbrot_normal_map_1.png", dpi=200)

N = abs(Z) > 2  # normal map effect 2 (distance estimation)
U = Z[N] * dZ[N] * ((1 + np.log(abs(Z[N]))) * np.conj(dZ[N] ** 2) - np.log(abs(Z[N])) * np.conj(Z[N] * ddZ[N]))
U = U / abs(U)  # unit normal vectors to the equidistant lines
T[N] = np.maximum((U.real * v.real + U.imag * v.imag + height) / (1 + height), 0)

plt.imshow(T ** 1.0, cmap=plt.cm.afmhot, origin="lower")
plt.savefig("Mandelbrot_normal_map_2.png", dpi=200)

```

### python_code_7.txt
```python
import numpy as np
import matplotlib.pyplot as plt

d, h = 200, 1200  # pixel density (= image width) and image height
n, r = 8000, 10000  # number of iterations and escape radius (r > 2)

a = -.743643887037158704752191506114774  # real coordinate of the zoom center
b = 0.131825904205311970493132056385139  # imaginary coordinate of the center

x = np.linspace(0, 2, num=d+1)
y = np.linspace(0, 2 * h / d, num=h+1)

A, B = np.meshgrid(x * np.pi, y * np.pi)
C = 8.0 * np.exp((A + B * 1j) * 1j) + (a + b * 1j)

Z, dZ = np.zeros_like(C), np.zeros_like(C)
D = np.zeros(C.shape)

for k in range(n):
    M = Z.real ** 2 + Z.imag ** 2 < r ** 2
    Z[M], dZ[M] = Z[M] ** 2 + C[M], 2 * Z[M] * dZ[M] + 1

N = abs(Z) > 2  # exterior distance estimation
D[N] = np.log(abs(Z[N])) * abs(Z[N]) / abs(dZ[N])

plt.imshow(D.T ** 0.05, cmap=plt.cm.nipy_spectral, origin="lower")
plt.savefig("Mercator_Mandelbrot_map.png", dpi=200)

X, Y = C.real, C.imag  # zoom images (adjust circle size 100 and zoom level 20 as needed)
R, c, z = 100 * (2 / d) * np.pi * np.exp(- B), min(d, h) + 1, max(0, h - d) // 20

fig, ax = plt.subplots(2, 2, figsize=(12, 12))
ax[0, 0].scatter(X[1*z:1*z+c,0:d], Y[1*z:1*z+c,0:d], s=R[0:c,0:d]**2.0, c=D[1*z:1*z+c,0:d]**0.5, cmap=plt.cm.nipy_spectral)
ax[0, 1].scatter(X[2*z:2*z+c,0:d], Y[2*z:2*z+c,0:d], s=R[0:c,0:d]**2.0, c=D[2*z:2*z+c,0:d]**0.4, cmap=plt.cm.nipy_spectral)
ax[1, 0].scatter(X[3*z:3*z+c,0:d], Y[3*z:3*z+c,0:d], s=R[0:c,0:d]**2.0, c=D[3*z:3*z+c,0:d]**0.3, cmap=plt.cm.nipy_spectral)
ax[1, 1].scatter(X[4*z:4*z+c,0:d], Y[4*z:4*z+c,0:d], s=R[0:c,0:d]**2.0, c=D[4*z:4*z+c,0:d]**0.2, cmap=plt.cm.nipy_spectral)
plt.savefig("Mercator_Mandelbrot_zoom.png", dpi=100)

```

### python_code_8.txt
```python
import numpy as np
import matplotlib.pyplot as plt

import decimal as dc  # decimal floating point arithmetic with arbitrary precision
dc.getcontext().prec = 80  # set precision to 80 digits (about 256 bits)

d, h = 50, 1000  # pixel density (= image width) and image height
n, r = 80000, 100000  # number of iterations and escape radius (r > 2)

a = dc.Decimal("-1.256827152259138864846434197797294538253477389787308085590211144291")
b = dc.Decimal(".37933802890364143684096784819544060002129071484943239316486643285025")

S = np.zeros(n+1, dtype=np.complex128)
u, v = dc.Decimal(0), dc.Decimal(0)

for k in range(n+1):
    S[k] = float(u) + float(v) * 1j
    if u ** 2 + v ** 2 < r ** 2:
        u, v = u ** 2 - v ** 2 + a, 2 * u * v + b
    else:
        print("The reference sequence diverges within %s iterations." % k)
        break

x = np.linspace(0, 2, num=d+1)
y = np.linspace(0, 2 * h / d, num=h+1)

A, B = np.meshgrid(x * np.pi, y * np.pi)
C = 8.0 * np.exp((A + B * 1j) * 1j)

E, Z, dZ = np.zeros_like(C), np.zeros_like(C), np.zeros_like(C)
D, I, J = np.zeros(C.shape), np.zeros(C.shape, dtype=np.int64), np.zeros(C.shape, dtype=np.int64)

for k in range(n):
    Z2 = Z.real ** 2 + Z.imag ** 2
    M, R = Z2 < r ** 2, Z2 < E.real ** 2 + E.imag ** 2
    E[R], I[R] = Z[R], J[R]  # rebase when z is closer to zero
    E[M], I[M] = (2 * S[I[M]] + E[M]) * E[M] + C[M], I[M] + 1
    Z[M], dZ[M] = S[I[M]] + E[M], 2 * Z[M] * dZ[M] + 1

N = abs(Z) > 2  # exterior distance estimation
D[N] = np.log(abs(Z[N])) * abs(Z[N]) / abs(dZ[N])

plt.imshow(D.T ** 0.015, cmap=plt.cm.nipy_spectral, origin="lower")
plt.savefig("Mercator_Mandelbrot_deep_map.png", dpi=200)

```

### python_code_9.txt
```python
print(
'\n'.join(
    ''.join(
        ' *'[(z:=0, c:=x/50+y/50j, [z:=z*z+c for _ in range(99)], abs(z))[-1]<2]
        for x in range(-100,25)
    )
    for y in range(-50,50)
))

```

