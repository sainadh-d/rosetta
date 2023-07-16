# Horizontal sundial calculations

## Task Link
[Rosetta Code - Horizontal sundial calculations](https://rosettacode.org/wiki/Horizontal_sundial_calculations)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class Sundial {
    public static void main(String[] args) {
        double lat, slat, lng, ref;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter latitude: ");
        lat = sc.nextDouble();
        System.out.print("Enter longitude: ");
        lng = sc.nextDouble();
        System.out.print("Enter legal meridian: ");
        ref = sc.nextDouble();
        System.out.println();

        slat = Math.sin(Math.toRadians(lat));
        System.out.printf("sine of latitude: %.3f\n", slat);
        System.out.printf("diff longitude: %.3f\n\n", lng - ref);

        System.out.printf("Hour, sun hour angle, dial hour line angle from 6am to 6pm\n");

        for (int h = -6; h <= 6; h++) {
            double hla, hra, hraRad;
            hra = 15.0 * h;
            hra = hra - lng + ref;
            hraRad = Math.toRadians(hra);
            hla = Math.toDegrees(Math.atan2(Math.sin(hraRad)*Math.sin(Math.toRadians(lat)), Math.cos(hraRad)));
            System.out.printf("HR= %3d;  \t  HRA=%7.3f;  \t  HLA= %7.3f\n",
                    h, hra, hla);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
import math
try: raw_input
except: raw_input = input

lat = float(raw_input("Enter latitude       => "))
lng = float(raw_input("Enter longitude      => "))
ref = float(raw_input("Enter legal meridian => "))
print()

slat = math.sin(math.radians(lat))
print("    sine of latitude:   %.3f" % slat)
print("    diff longitude:     %.3f" % (lng-ref))
print()
print("Hour, sun hour angle, dial hour line angle from 6am to 6pm")

for h in range(-6, 7):
  hra = 15 * h
  hra -= lng - ref
  hla = math.degrees(math.atan(slat * math.tan(math.radians(hra))))
  print("HR=%3d; HRA=%7.3f; HLA=%7.3f" % (h, hra, hla))

```

