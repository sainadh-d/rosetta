# Averages/Mean time of day

## Task Link
[Rosetta Code - Averages/Mean time of day](https://rosettacode.org/wiki/Averages/Mean_time_of_day)

## Java Code
### java_code_1.txt
```java
public class MeanTimeOfDay {
    
    static double meanAngle(double[] angles) {
        int len = angles.length;
        double sinSum = 0.0;
        for (int i = 0; i < len; i++) {
            sinSum += Math.sin(angles[i] * Math.PI / 180.0);
        }
 
        double cosSum = 0.0;
        for (int i = 0; i < len; i++) {
            cosSum += Math.cos(angles[i] * Math.PI / 180.0);
        }

        return Math.atan2(sinSum / len, cosSum / len) * 180.0 / Math.PI;
    }

    /* time string assumed to be in format "hh:mm:ss" */
    static int timeToSecs(String t) {
        int hours = Integer.parseInt(t.substring(0, 2));
        int mins  = Integer.parseInt(t.substring(3, 5));
        int secs  = Integer.parseInt(t.substring(6, 8));
        return 3600 * hours + 60 * mins + secs;
    }

    /* 1 second of time = 360/(24 * 3600) = 1/240th degree */
    static double timeToDegrees(String t) {
        return timeToSecs(t) / 240.0;
    }

    static String degreesToTime(double d) {
        if (d < 0.0) d += 360.0;
        int secs  = (int)(d * 240.0);
        int hours = secs / 3600;
        int mins  = secs % 3600;
        secs = mins % 60;
        mins /= 60;
        return String.format("%2d:%2d:%2d", hours, mins, secs);
    }

    public static void main(String[] args) {
        String[] tm = {"23:00:17", "23:40:20", "00:12:45", "00:17:19"};
        double[] angles = new double[4];
        for (int i = 0; i < 4; i++) angles[i] = timeToDegrees(tm[i]);        
        double mean = meanAngle(angles);
        System.out.println("Average time is : " + degreesToTime(mean));
    }
}

```

## Python Code
### python_code_1.txt
```python
from cmath import rect, phase
from math import radians, degrees


def mean_angle(deg):
    return degrees(phase(sum(rect(1, radians(d)) for d in deg)/len(deg)))

def mean_time(times):
    t = (time.split(':') for time in times)
    seconds = ((float(s) + int(m) * 60 + int(h) * 3600) 
               for h, m, s in t)
    day = 24 * 60 * 60
    to_angles = [s * 360. / day for s in seconds]
    mean_as_angle = mean_angle(to_angles)
    mean_seconds = mean_as_angle * day / 360.
    if mean_seconds < 0:
        mean_seconds += day
    h, m = divmod(mean_seconds, 3600)
    m, s = divmod(m, 60)
    return '%02i:%02i:%02i' % (h, m, s)


if __name__ == '__main__':
    print( mean_time(["23:00:17", "23:40:20", "00:12:45", "00:17:19"]) )

```

