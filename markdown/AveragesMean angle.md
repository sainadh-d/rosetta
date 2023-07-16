# Averages/Mean angle

## Task Link
[Rosetta Code - Averages/Mean angle](https://rosettacode.org/wiki/Averages/Mean_angle)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class AverageMeanAngle {

    public static void main(String[] args) {
        printAverageAngle(350.0, 10.0);
        printAverageAngle(90.0, 180.0, 270.0, 360.0);
        printAverageAngle(10.0, 20.0, 30.0);
        printAverageAngle(370.0);
        printAverageAngle(180.0);
    }

    private static void printAverageAngle(double... sample) {
        double meanAngle = getMeanAngle(sample);
        System.out.printf("The mean angle of %s is %s%n", Arrays.toString(sample), meanAngle);
    }

    public static double getMeanAngle(double... anglesDeg) {
        double x = 0.0;
        double y = 0.0;

        for (double angleD : anglesDeg) {
            double angleR = Math.toRadians(angleD);
            x += Math.cos(angleR);
            y += Math.sin(angleR);
        }
        double avgR = Math.atan2(y / anglesDeg.length, x / anglesDeg.length);
        return Math.toDegrees(avgR);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from cmath import rect, phase
>>> from math import radians, degrees
>>> def mean_angle(deg):
...     return degrees(phase(sum(rect(1, radians(d)) for d in deg)/len(deg)))
... 
>>> for angles in [[350, 10], [90, 180, 270, 360], [10, 20, 30]]:
...     print('The mean angle of', angles, 'is:', round(mean_angle(angles), 12), 'degrees')
...     
The mean angle of [350, 10] is: -0.0 degrees
The mean angle of [90, 180, 270, 360] is: -90.0 degrees
The mean angle of [10, 20, 30] is: 20.0 degrees
>>>

```

