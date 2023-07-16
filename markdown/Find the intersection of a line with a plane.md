# Find the intersection of a line with a plane

## Task Link
[Rosetta Code - Find the intersection of a line with a plane](https://rosettacode.org/wiki/Find_the_intersection_of_a_line_with_a_plane)

## Java Code
### java_code_1.txt
```java
public class LinePlaneIntersection {
    private static class Vector3D {
        private double x, y, z;

        Vector3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        Vector3D plus(Vector3D v) {
            return new Vector3D(x + v.x, y + v.y, z + v.z);
        }

        Vector3D minus(Vector3D v) {
            return new Vector3D(x - v.x, y - v.y, z - v.z);
        }

        Vector3D times(double s) {
            return new Vector3D(s * x, s * y, s * z);
        }

        double dot(Vector3D v) {
            return x * v.x + y * v.y + z * v.z;
        }

        @Override
        public String toString() {
            return String.format("(%f, %f, %f)", x, y, z);
        }
    }

    private static Vector3D intersectPoint(Vector3D rayVector, Vector3D rayPoint, Vector3D planeNormal, Vector3D planePoint) {
        Vector3D diff = rayPoint.minus(planePoint);
        double prod1 = diff.dot(planeNormal);
        double prod2 = rayVector.dot(planeNormal);
        double prod3 = prod1 / prod2;
        return rayPoint.minus(rayVector.times(prod3));
    }

    public static void main(String[] args) {
        Vector3D rv = new Vector3D(0.0, -1.0, -1.0);
        Vector3D rp = new Vector3D(0.0, 0.0, 10.0);
        Vector3D pn = new Vector3D(0.0, 0.0, 1.0);
        Vector3D pp = new Vector3D(0.0, 0.0, 5.0);
        Vector3D ip = intersectPoint(rv, rp, pn, pp);
        System.out.println("The ray intersects the plane at " + ip);
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/bin/python
from __future__ import print_function
import numpy as np

def LinePlaneCollision(planeNormal, planePoint, rayDirection, rayPoint, epsilon=1e-6):

	ndotu = planeNormal.dot(rayDirection)
	if abs(ndotu) < epsilon:
		raise RuntimeError("no intersection or line is within plane")

	w = rayPoint - planePoint
	si = -planeNormal.dot(w) / ndotu
	Psi = w + si * rayDirection + planePoint
	return Psi


if __name__=="__main__":
	#Define plane
	planeNormal = np.array([0, 0, 1])
	planePoint = np.array([0, 0, 5]) #Any point on the plane

	#Define ray
	rayDirection = np.array([0, -1, -1])
	rayPoint = np.array([0, 0, 10]) #Any point along the ray

	Psi = LinePlaneCollision(planeNormal, planePoint, rayDirection, rayPoint)
	print ("intersection at", Psi)

```

