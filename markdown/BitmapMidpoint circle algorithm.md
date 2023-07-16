# Bitmap/Midpoint circle algorithm

## Task Link
[Rosetta Code - Bitmap/Midpoint circle algorithm](https://rosettacode.org/wiki/Bitmap/Midpoint_circle_algorithm)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;

public class MidPointCircle {
	private BasicBitmapStorage image;

	public MidPointCircle(final int imageWidth, final int imageHeight) {
		this.image = new BasicBitmapStorage(imageWidth, imageHeight);
	}

	private void drawCircle(final int centerX, final int centerY, final int radius) {
		int d = (5 - radius * 4)/4;
		int x = 0;
		int y = radius;
		Color circleColor = Color.white;

		do {
			image.setPixel(centerX + x, centerY + y, circleColor);
			image.setPixel(centerX + x, centerY - y, circleColor);
			image.setPixel(centerX - x, centerY + y, circleColor);
			image.setPixel(centerX - x, centerY - y, circleColor);
			image.setPixel(centerX + y, centerY + x, circleColor);
			image.setPixel(centerX + y, centerY - x, circleColor);
			image.setPixel(centerX - y, centerY + x, circleColor);
			image.setPixel(centerX - y, centerY - x, circleColor);
			if (d < 0) {
				d += 2 * x + 1;
			} else {
				d += 2 * (x - y) + 1;
				y--;
			}
			x++;
		} while (x <= y);

	}
}

```

## Python Code
### python_code_1.txt
```python
def circle(self, x0, y0, radius, colour=black):
    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius
    x = 0
    y = radius
    self.set(x0, y0 + radius, colour)
    self.set(x0, y0 - radius, colour)
    self.set(x0 + radius, y0, colour)
    self.set(x0 - radius, y0, colour)

    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        self.set(x0 + x, y0 + y, colour)
        self.set(x0 - x, y0 + y, colour)
        self.set(x0 + x, y0 - y, colour)
        self.set(x0 - x, y0 - y, colour)
        self.set(x0 + y, y0 + x, colour)
        self.set(x0 - y, y0 + x, colour)
        self.set(x0 + y, y0 - x, colour)
        self.set(x0 - y, y0 - x, colour)
Bitmap.circle = circle

bitmap = Bitmap(25,25)
bitmap.circle(x0=12, y0=12, radius=12)
bitmap.chardisplay()

'''
The origin, 0,0; is the lower left, with x increasing to the right,
and Y increasing upwards.

The program above produces the following display :

+-------------------------+
|         @@@@@@@         |
|       @@       @@       |
|     @@           @@     |
|    @               @    |
|   @                 @   |
|  @                   @  |
|  @                   @  |
| @                     @ |
| @                     @ |
|@                       @|
|@                       @|
|@                       @|
|@                       @|
|@                       @|
|@                       @|
|@                       @|
| @                     @ |
| @                     @ |
|  @                   @  |
|  @                   @  |
|   @                 @   |
|    @               @    |
|     @@           @@     |
|       @@       @@       |
|         @@@@@@@         |
+-------------------------+
'''

```

