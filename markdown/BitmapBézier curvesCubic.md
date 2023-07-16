# Bitmap/Bézier curves/Cubic

## Task Link
[Rosetta Code - Bitmap/Bézier curves/Cubic](https://rosettacode.org/wiki/Bitmap/B%C3%A9zier_curves/Cubic)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Point;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.imageio.ImageIO;

public final class BezierCubic {

	public static void main(String[] args) throws IOException {
		final int width = 200;
	    final int height = 200;
	    BasicBitmapStorage bitmap = new BasicBitmapStorage(width, height);	    
        bitmap.fill(Color.YELLOW);
        
        Point point1 = new Point(0, 150);
        Point point2 = new Point(30, 50);
        Point point3 = new Point(120, 130);
        Point point4 = new Point(160, 30);
        bitmap.cubicBezier(point1, point2, point3, point4, Color.BLACK, 20);
        
        File bezierFile = new File("CubicBezierJava.jpg");
        ImageIO.write((RenderedImage) bitmap.getImage(), "jpg", bezierFile);
	}
	
}
	
final class BasicBitmapStorage {

	public BasicBitmapStorage(int width, int height) {
        image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
    } 
	
	public void fill(Color color) {
		Graphics graphics = image.getGraphics();
	    graphics.setColor(color);
	    graphics.fillRect(0, 0, image.getWidth(), image.getHeight());
	}    

    public Color getPixel(int x, int y) {
        return new Color(image.getRGB(x, y));
    }
    
    public void setPixel(int x, int y, Color color) {
        image.setRGB(x, y, color.getRGB());
    }
    
    public Image getImage() {
    	return image;
    }
    
    public void cubicBezier(
    		Point point1, Point point2, Point point3, Point point4, Color color, int intermediatePointCount) {
    	
     	List<Point> points = new ArrayList<Point>();
        
        for ( int i = 0; i <= intermediatePointCount; i++ ) {
            final double t = (double) i / intermediatePointCount;
            final double u = 1.0 - t;
            final double a = u * u * u;
            final double b = 3.0 * t * u * u;
            final double c = 3.0 * t * t * u;
            final double d = t * t * t;
            
            final int x = (int) ( a * point1.x + b * point2.x + c * point3.x + d * point4.x );
            final int y = (int) ( a * point1.y + b * point2.y + c * point3.y + d * point4.y );             
            points.add( new Point(x, y) );           
            setPixel(x, y, color);
        }
        
        for ( int i = 0; i < intermediatePointCount; i++ ) {
            drawLine(points.get(i).x, points.get(i).y, points.get(i + 1).x, points.get(i + 1).y, color);
        }
    }
    
    public void drawLine(int x0, int y0, int x1, int y1, Color color) {
    	final int dx = Math.abs(x1 - x0);
    	final int dy = Math.abs(y1 - y0); 
    	final int xIncrement = x0 < x1 ? 1 : -1;
    	final int yIncrement = y0 < y1 ? 1 : -1; 
    	
    	int error = ( dx > dy ? dx : -dy ) / 2;
    	
    	while ( x0 != x1 || y0 != y1 ) {
    	    setPixel(x0, y0, color);
    	    int error2 = error;
    	    
    	    if ( error2 > -dx ) {
    	    	error -= dy;
    	    	x0 += xIncrement;
    	    }
    	    
    	    if ( error2 < dy ) {
    	    	error += dx;
    	    	y0 += yIncrement;
    	    }
    	}
    	setPixel(x0, y0, color);
    }
    
    private BufferedImage image;
    
}

```

## Python Code
### python_code_1.txt
```python
def cubicbezier(self, x0, y0, x1, y1, x2, y2, x3, y3, n=20):
    pts = []
    for i in range(n+1):
        t = i / n
        a = (1. - t)**3
        b = 3. * t * (1. - t)**2
        c = 3.0 * t**2 * (1.0 - t)
        d = t**3
        
        x = int(a * x0 + b * x1 + c * x2 + d * x3)
        y = int(a * y0 + b * y1 + c * y2 + d * y3)
        pts.append( (x, y) )
    for i in range(n):
        self.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1])
Bitmap.cubicbezier = cubicbezier

bitmap = Bitmap(17,17)
bitmap.cubicbezier(16,1, 1,4, 3,16, 15,11)
bitmap.chardisplay()


'''
The origin, 0,0; is the lower left, with x increasing to the right,
and Y increasing upwards.

The chardisplay above produces the following output :
+-----------------+
|                 |
|                 |
|                 |
|                 |
|         @@@@    |
|      @@@    @@@ |
|     @           |
|     @           |
|     @           |
|     @           |
|      @          |
|      @          |
|       @         |
|        @        |
|         @@@@    |
|             @@@@|
|                 |
+-----------------+
'''

```

