# Box the compass

## Task Link
[Rosetta Code - Box the compass](https://rosettacode.org/wiki/Box_the_compass)

## Java Code
### java_code_1.txt
```java
enum Compass {
    N, NbE, NNE, NEbN, NE, NEbE, ENE, EbN,
    E, EbS, ESE, SEbE, SE, SEbS, SSE, SbE,
    S, SbW, SSW, SWbS, SW, SWbW, WSW, WbS,
    W, WbN, WNW, NWbW, NW, NWbN, NNW, NbW;

    float midpoint() {
        float midpoint = (360 / 32f) * ordinal();
        return midpoint == 0 ? 360 : midpoint;
    }

    float[] bounds() {
        float bound = (360 / 32f) / 2f;
        float midpoint = midpoint();
        float boundA = midpoint - bound;
        float boundB = midpoint + bound;
        if (boundB > 360) boundB -= 360;
        return new float[] { boundA, boundB };
    }

    static Compass parse(float degrees) {
        float[] bounds;
        float[] boundsN = N.bounds();
        for (Compass value : Compass.values()) {
            bounds = value.bounds();
            if (degrees >= boundsN[0] || degrees < boundsN[1])
                return N;
            if (degrees >= bounds[0] && degrees < bounds[1])
                return value;
        }
        return null;
    }

    @Override
    public String toString() {
        String[] strings = new String[name().length()];
        int index = 0;
        for (char letter : name().toCharArray()) {
            switch (letter) {
                case 'N' -> strings[index] = "north";
                case 'E' -> strings[index] = "east";
                case 'S' -> strings[index] = "south";
                case 'W' -> strings[index] = "west";
                case 'b' -> strings[index] = "by";
            }
            index++;
        }
        String string
            = strings[0].substring(0, 1).toUpperCase() +
              strings[0].substring(1);
        switch (strings.length) {
            case 2 -> string += strings[1];
            case 3 -> {
                if (strings[1].equals("by")) {
                    string += " %s %s".formatted(strings[1], strings[2]);
                } else {
                    string += "-%s%s".formatted(strings[1], strings[2]);
                }
            }
            case 4 -> {
                string += String.join(" ", strings[1], strings[2], strings[3]);
            }
        }
        return string;
    }
}

```

## Python Code
### python_code_1.txt
```python
majors   = 'north east south west'.split()
majors   *= 2 # no need for modulo later
quarter1 = 'N,N by E,N-NE,NE by N,NE,NE by E,E-NE,E by N'.split(',')
quarter2 = [p.replace('NE','EN') for p in quarter1]

def degrees2compasspoint(d):
    d = (d % 360) + 360/64
    majorindex, minor = divmod(d, 90.)
    majorindex = int(majorindex)
    minorindex  = int( (minor*4) // 45 )
    p1, p2 = majors[majorindex: majorindex+2]
    if p1 in {'north', 'south'}:
        q = quarter1
    else:
        q = quarter2
    return q[minorindex].replace('N', p1).replace('E', p2).capitalize()

if __name__ == '__main__':
    for i in range(33):
        d = i * 11.25
        m = i % 3
        if   m == 1: d += 5.62
        elif m == 2: d -= 5.62
        n = i % 32 + 1
        print( '%2i %-18s %7.2f°' % (n, degrees2compasspoint(d), d) )

```

