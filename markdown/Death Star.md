# Death Star

## Task Link
[Rosetta Code - Death Star](https://rosettacode.org/wiki/Death_Star)

## Java Code
### java_code_1.txt
```java
import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.geometry.Point3D;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.shape.MeshView;
import javafx.scene.shape.TriangleMesh;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;
public class DeathStar extends Application {

	private static final int DIVISION = 200;// the bigger the higher resolution
	float radius = 300;// radius of the sphere

	@Override
	public void start(Stage primaryStage) throws Exception {
		Point3D otherSphere = new Point3D(-radius, 0, -radius * 1.5);
		final TriangleMesh triangleMesh = createMesh(DIVISION, radius, otherSphere);
		MeshView a = new MeshView(triangleMesh);

		a.setTranslateY(radius);
		a.setTranslateX(radius);
		a.setRotationAxis(Rotate.Y_AXIS);
		Scene scene = new Scene(new Group(a));
//		uncomment if you want to move the other sphere
		
//		scene.setOnKeyPressed(new EventHandler<KeyEvent>() {
//			Point3D sphere = otherSphere;
//
//			@Override
//			public void handle(KeyEvent e) {
//				KeyCode code = e.getCode();
//				switch (code) {
//				case UP:
//					sphere = sphere.add(0, -10, 0);
//					break;
//				case DOWN:
//					sphere = sphere.add(0, 10, 0);
//					break;
//				case LEFT:
//					sphere = sphere.add(-10, 0, 0);
//					break;
//				case RIGHT:
//					sphere = sphere.add(10, 0, 0);
//					break;
//				case W:
//					sphere = sphere.add(0, 0, 10);
//					break;
//				case S:
//					sphere = sphere.add(0, 0, -10);
//					break;
//				default:
//					return;
//				}
//				a.setMesh(createMesh(DIVISION, radius, sphere));
//
//			}
//		});

		primaryStage.setScene(scene);
		primaryStage.show();
	}

	static TriangleMesh createMesh(final int division, final float radius, final Point3D centerOtherSphere) {
		Rotate rotate = new Rotate(180, centerOtherSphere);
		final int div2 = division / 2;

		final int nPoints = division * (div2 - 1) + 2;
		final int nTPoints = (division + 1) * (div2 - 1) + division * 2;
		final int nFaces = division * (div2 - 2) * 2 + division * 2;

		final float rDiv = 1.f / division;

		float points[] = new float[nPoints * 3];
		float tPoints[] = new float[nTPoints * 2];
		int faces[] = new int[nFaces * 6];

		int pPos = 0, tPos = 0;

		for (int y = 0; y < div2 - 1; ++y) {
			float va = rDiv * (y + 1 - div2 / 2) * 2 * (float) Math.PI;
			float sin_va = (float) Math.sin(va);
			float cos_va = (float) Math.cos(va);

			float ty = 0.5f + sin_va * 0.5f;
			for (int i = 0; i < division; ++i) {
				double a = rDiv * i * 2 * (float) Math.PI;
				float hSin = (float) Math.sin(a);
				float hCos = (float) Math.cos(a);
				points[pPos + 0] = hSin * cos_va * radius;
				points[pPos + 2] = hCos * cos_va * radius;
				points[pPos + 1] = sin_va * radius;

				final Point3D point3D = new Point3D(points[pPos + 0], points[pPos + 1], points[pPos + 2]);
				double distance = centerOtherSphere.distance(point3D);
				if (distance <= radius) {
					Point3D subtract = centerOtherSphere.subtract(point3D);
					Point3D transform = rotate.transform(subtract);
					points[pPos + 0] = (float) transform.getX();
					points[pPos + 1] = (float) transform.getY();
					points[pPos + 2] = (float) transform.getZ();
					
				}
				tPoints[tPos + 0] = 1 - rDiv * i;
				tPoints[tPos + 1] = ty;
				pPos += 3;
				tPos += 2;
			}
			tPoints[tPos + 0] = 0;
			tPoints[tPos + 1] = ty;
			tPos += 2;
		}

		points[pPos + 0] = 0;
		points[pPos + 1] = -radius;
		points[pPos + 2] = 0;
		points[pPos + 3] = 0;
		points[pPos + 4] = radius;
		points[pPos + 5] = 0;
		pPos += 6;

		int pS = (div2 - 1) * division;

		float textureDelta = 1.f / 256;
		for (int i = 0; i < division; ++i) {
			tPoints[tPos + 0] = rDiv * (0.5f + i);
			tPoints[tPos + 1] = textureDelta;
			tPos += 2;
		}

		for (int i = 0; i < division; ++i) {
			tPoints[tPos + 0] = rDiv * (0.5f + i);
			tPoints[tPos + 1] = 1 - textureDelta;
			tPos += 2;
		}

		int fIndex = 0;
		for (int y = 0; y < div2 - 2; ++y) {
			for (int x = 0; x < division; ++x) {
				int p0 = y * division + x;
				int p1 = p0 + 1;
				int p2 = p0 + division;
				int p3 = p1 + division;

				int t0 = p0 + y;
				int t1 = t0 + 1;
				int t2 = t0 + division + 1;
				int t3 = t1 + division + 1;

				// add p0, p1, p2
				faces[fIndex + 0] = p0;
				faces[fIndex + 1] = t0;
				faces[fIndex + 2] = p1 % division == 0 ? p1 - division : p1;
				faces[fIndex + 3] = t1;
				faces[fIndex + 4] = p2;
				faces[fIndex + 5] = t2;
				fIndex += 6;

				// add p3, p2, p1
				faces[fIndex + 0] = p3 % division == 0 ? p3 - division : p3;
				faces[fIndex + 1] = t3;
				faces[fIndex + 2] = p2;
				faces[fIndex + 3] = t2;
				faces[fIndex + 4] = p1 % division == 0 ? p1 - division : p1;
				faces[fIndex + 5] = t1;
				fIndex += 6;
			}
		}

		int p0 = pS;
		int tB = (div2 - 1) * (division + 1);
		for (int x = 0; x < division; ++x) {
			int p2 = x, p1 = x + 1, t0 = tB + x;
			faces[fIndex + 0] = p0;
			faces[fIndex + 1] = t0;
			faces[fIndex + 2] = p1 == division ? 0 : p1;
			faces[fIndex + 3] = p1;
			faces[fIndex + 4] = p2;
			faces[fIndex + 5] = p2;
			fIndex += 6;
		}

		p0 = p0 + 1;
		tB = tB + division;
		int pB = (div2 - 2) * division;

		for (int x = 0; x < division; ++x) {
			int p1 = pB + x, p2 = pB + x + 1, t0 = tB + x;
			int t1 = (div2 - 2) * (division + 1) + x, t2 = t1 + 1;
			faces[fIndex + 0] = p0;
			faces[fIndex + 1] = t0;
			faces[fIndex + 2] = p1;
			faces[fIndex + 3] = t1;
			faces[fIndex + 4] = p2 % division == 0 ? p2 - division : p2;
			faces[fIndex + 5] = t2;
			fIndex += 6;
		}

		TriangleMesh m = new TriangleMesh();
		m.getPoints().setAll(points);
		m.getTexCoords().setAll(tPoints);
		m.getFaces().setAll(faces);

		return m;
	}

	public static void main(String[] args) {

		launch(args);
	}

}

```

### java_code_2.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.List;

import javax.imageio.ImageIO;

public final class DeathStar {

	public static void main(String[] aArgs) throws IOException {
		Vector direction = new Vector(20.0, -40.0, -10.0);
		direction.normalise();
		Sphere positive = new Sphere(0, 0, 0, 120);
		Sphere negative = new Sphere(-90, -90, -30, 100);

		BufferedImage image = deathStar(positive, negative, direction, 1.5, 0.5);
		
		ImageIO.write(image, "png", new File("DeathStarJava.png"));
	}
	
	private static BufferedImage deathStar(
			Sphere aPositive, Sphere aNegative, Vector aDirection, double aShadow, double aBrightness) {
		final int width = aPositive.radius * 4;
		final int height = aPositive.radius * 3;
		BufferedImage result = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
		Graphics graphics = result.getGraphics();
        graphics.setColor(Color.CYAN);
        graphics.fillRect(0, 0, width, height);
        
		Vector ray = new Vector(0.0, 0.0, 0.0);
		final int deltaX = aPositive.x - width / 2;
		final int deltaY = aPositive.y - height / 2;

		double xMax = aPositive.x + aPositive.radius;
		double yMax = aPositive.y + aPositive.radius;
		for ( int y = aPositive.y - aPositive.radius; y < yMax; y++ ) {
		    for ( int x = aPositive.x - aPositive.radius; x < xMax; x++ ) {
		    	List<Object> contacts = aPositive.contact(x, y);
		    	final double zb1 = (double) contacts.get(0);
		    	final int zb2 = (int) contacts.get(1);
		    	final boolean positiveHit = (boolean) contacts.get(2);
		    	if ( ! positiveHit ) {
		    		continue;
		    	}
	       		contacts = aNegative.contact(x, y);
	       		final double zs1 = (double) contacts.get(0);
	       		final int zs2 = (int) contacts.get(1);
	       		boolean negativeHit = (boolean) contacts.get(2);
	       		if ( negativeHit ) {
	       			if ( zs1 > zb1 ) {
	       				negativeHit = false;
	       			} else if ( zs2 > zb2 ) {
	       				continue;
	       			}
	       		}
	       		
		       	if ( negativeHit ) {
		       		ray.x = aNegative.x - x;
		       		ray.y = aNegative.y - y;
		       		ray.z = aNegative.z - zs2;
		       	} else {
		       		ray.x = x - aPositive.x;
		       		ray.y = y - aPositive.y;
		       		ray.z = zb1 - aPositive.z;
		       	}
		       	ray.normalise();
		       	double rayComponent = ray.scalarProduct(aDirection);
		       	if ( rayComponent < 0 ) { 
		       		rayComponent = 0;
		       	}
		       	int color = (int) ( 255 * ( Math.pow(rayComponent, aShadow) + aBrightness) / ( 1 + aBrightness ) );
		       	if ( color < 0 ) {
		       		color = 0;
		       	} else if ( color > 255 ) {
		       		color = 255;
		       	}
		       	result.setRGB(x - deltaX, y - deltaY, color);
		    }
		}
		return result;
	}	
	
	private static class Vector {
		
		public Vector(double aX, double aY, double aZ) {
			x = aX; y = aY; z = aZ;
		}
		
		public double scalarProduct(Vector aOther) {
			return x * aOther.x + y * aOther.y + z * aOther.z;
		}
		
		public Vector normalise() {
			final double magnitude = Math.sqrt(this.scalarProduct(this));
			return new Vector(x /= magnitude, y /= magnitude, z /= magnitude);
		}
		
		private double x, y, z;
		
	}
	
	private static class Sphere {
		
		public Sphere(int aX, int aY, int aZ, int aRadius) {
			x = aX; y = aY; z = aZ; radius = aRadius;
		}
		
		public List<Object> contact(int aX, int aY) {
			final int xx = aX - x;
			final int yy = aY - y;
			final int zSquared = radius * radius - ( xx * xx + yy * yy );
			if ( zSquared >= 0 ) {
				final double zz = Math.sqrt(zSquared);
				return List.of(z - zz, z, true);
			}
			return List.of( 0.0, 0, false );
		}	
		
		private int x, y, z, radius;
		
	}

}

```

## Python Code
### python_code_1.txt
```python
import sys, math, collections

Sphere = collections.namedtuple("Sphere", "cx cy cz r")
V3 = collections.namedtuple("V3", "x y z")

def normalize((x, y, z)):
    len = math.sqrt(x**2 + y**2 + z**2)
    return V3(x / len, y / len, z / len)

def dot(v1, v2):
    d = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
    return -d if d < 0 else 0.0

def hit_sphere(sph, x0, y0):
    x = x0 - sph.cx
    y = y0 - sph.cy
    zsq = sph.r ** 2 - (x ** 2 + y ** 2)
    if zsq < 0:
        return (False, 0, 0)
    szsq = math.sqrt(zsq)
    return (True, sph.cz - szsq, sph.cz + szsq)

def draw_sphere(k, ambient, light):
    shades = ".:!*oe&#%@"
    pos = Sphere(20.0, 20.0, 0.0, 20.0)
    neg = Sphere(1.0, 1.0, -6.0, 20.0)

    for i in xrange(int(math.floor(pos.cy - pos.r)),
                    int(math.ceil(pos.cy + pos.r) + 1)):
        y = i + 0.5
        for j in xrange(int(math.floor(pos.cx - 2 * pos.r)),
                        int(math.ceil(pos.cx + 2 * pos.r) + 1)):
            x = (j - pos.cx) / 2.0 + 0.5 + pos.cx

            (h, zb1, zb2) = hit_sphere(pos, x, y)
            if not h:
                hit_result = 0
            else:
                (h, zs1, zs2) = hit_sphere(neg, x, y)
                if not h:
                    hit_result = 1
                elif zs1 > zb1:
                    hit_result = 1
                elif zs2 > zb2:
                    hit_result = 0
                elif zs2 > zb1:
                    hit_result = 2
                else:
                    hit_result = 1

            if hit_result == 0:
                sys.stdout.write(' ')
                continue
            elif hit_result == 1:
                vec = V3(x - pos.cx, y - pos.cy, zb1 - pos.cz)
            elif hit_result == 2:
                vec = V3(neg.cx-x, neg.cy-y, neg.cz-zs2)
            vec = normalize(vec)

            b = dot(light, vec) ** k + ambient
            intensity = int((1 - b) * len(shades))
            intensity = min(len(shades), max(0, intensity))
            sys.stdout.write(shades[intensity])
        print

light = normalize(V3(-50, 30, 50))
draw_sphere(2, 0.5, light)

```

