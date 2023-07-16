# Old Russian measure of length

## Task Link
[Rosetta Code - Old Russian measure of length](https://rosettacode.org/wiki/Old_Russian_measure_of_length)

## Java Code
### java_code_1.txt
```java
public class OldRussianMeasures {

    final static String[] keys = {"tochka", "liniya", "centimeter", "diuym",
        "vershok", "piad", "fut", "arshin", "meter", "sazhen", "kilometer",
        "versta", "milia"};

    final static double[] values = {0.000254, 0.00254, 0.01,0.0254,
        0.04445, 0.1778, 0.3048, 0.7112, 1.0, 2.1336, 1000.0,
        1066.8, 7467.6};

    public static void main(String[] a) {
        if (a.length == 2 && a[0].matches("[+-]?\\d*(\\.\\d+)?")) {
            double inputVal = lookup(a[1]);
            if (!Double.isNaN(inputVal)) {
                double magnitude = Double.parseDouble(a[0]);
                double meters = magnitude * inputVal;
                System.out.printf("%s %s to: %n%n", a[0], a[1]);
                for (String k: keys)
                    System.out.printf("%10s: %g%n", k, meters / lookup(k));
                return;
            }
        }
        System.out.println("Please provide a number and unit");

    }

    public static double lookup(String key) {
        for (int i = 0; i < keys.length; i++)
            if (keys[i].equals(key))
                return values[i];
        return Double.NaN;
    }
}

```

## Python Code
### python_code_1.txt
```python
from sys import argv
 
unit2mult = {"arshin": 0.7112, "centimeter": 0.01,     "diuym":   0.0254,
             "fut":    0.3048, "kilometer":  1000.0,   "liniya":  0.00254,
             "meter":  1.0,    "milia":      7467.6,   "piad":    0.1778,
             "sazhen": 2.1336, "tochka":     0.000254, "vershok": 0.04445,
             "versta": 1066.8}
 
if __name__ == '__main__':
    assert len(argv) == 3, 'ERROR. Need two arguments - number then units'
    try:
        value = float(argv[1])
    except:
        print('ERROR. First argument must be a (float) number')
        raise
    unit = argv[2]
    assert unit in unit2mult, ( 'ERROR. Only know the following units: ' 
                                + ' '.join(unit2mult.keys()) )

    print("%g %s to:" % (value, unit))
    for unt, mlt in sorted(unit2mult.items()):
        print('  %10s: %g' % (unt, value * unit2mult[unit] / mlt))

```

