# Heronian triangles

## Task Link
[Rosetta Code - Heronian triangles](https://rosettacode.org/wiki/Heronian_triangles)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;

public class Heron {
    public static void main(String[] args) {
        ArrayList<int[]> list = new ArrayList<>();

        for (int c = 1; c <= 200; c++) {
            for (int b = 1; b <= c; b++) {
                for (int a = 1; a <= b; a++) {

                    if (gcd(gcd(a, b), c) == 1 && isHeron(heronArea(a, b, c))){
                        int area = (int) heronArea(a, b, c);
                        list.add(new int[]{a, b, c, a + b + c, area});
                    }
                }
            }
        }
        sort(list);

        System.out.printf("Number of primitive Heronian triangles with sides up "
                + "to 200: %d\n\nFirst ten when ordered by increasing area, then"
                + " perimeter:\nSides       Perimeter   Area", list.size());

        for (int i = 0; i < 10; i++) {
            System.out.printf("\n%d x %d x %d   %d      %d",
                    list.get(i)[0], list.get(i)[1], list.get(i)[2],
                    list.get(i)[3], list.get(i)[4]);
        }

        System.out.printf("\n\nArea = 210\nSides        Perimeter   Area");
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i)[4] == 210)
                System.out.printf("\n%d x %d x %d   %d      %d",
                        list.get(i)[0], list.get(i)[1], list.get(i)[2],
                        list.get(i)[3], list.get(i)[4]);
        }
    }

    public static double heronArea(int a, int b, int c) {
        double s = (a + b + c) / 2f;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }

    public static boolean isHeron(double h) {
        return h % 1 == 0 && h > 0;
    }

    public static int gcd(int a, int b) {
        int leftover = 1, dividend = a > b ? a : b, divisor = a > b ? b : a;
        while (leftover != 0) {
            leftover = dividend % divisor;
            if (leftover > 0) {
                dividend = divisor;
                divisor = leftover;
            }
        }
        return divisor;
    }

    public static void sort(ArrayList<int[]> list) {
        boolean swapped = true;
        int[] temp;
        while (swapped) {
            swapped = false;
            for (int i = 1; i < list.size(); i++) {
                if (list.get(i)[4] < list.get(i - 1)[4] ||
                        list.get(i)[4] == list.get(i - 1)[4] &&
                        list.get(i)[3] < list.get(i - 1)[3]) {
                    temp = list.get(i);
                    list.set(i, list.get(i - 1));
                    list.set(i - 1, temp);
                    swapped = true;
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division, print_function
from math import gcd, sqrt


def hero(a, b, c):
    s = (a + b + c) / 2
    a2 = s * (s - a) * (s - b) * (s - c)
    return sqrt(a2) if a2 > 0 else 0


def is_heronian(a, b, c):
    a = hero(a, b, c)
    return a > 0 and a.is_integer()


def gcd3(x, y, z):
    return gcd(gcd(x, y), z)


if __name__ == '__main__':
    MAXSIDE = 200

    N = 1 + MAXSIDE
    h = [(x, y, z)
         for x in range(1, N)
         for y in range(x, N)
         for z in range(y, N) if (x + y > z) and
         1 == gcd3(x, y, z) and
         is_heronian(x, y, z)]

    # By increasing area, perimeter, then sides
    h.sort(key=lambda x: (hero(*x), sum(x), x[::-1]))

    print(
        'Primitive Heronian triangles with sides up to %i:' % MAXSIDE, len(h)
    )
    print('\nFirst ten when ordered by increasing area, then perimeter,',
          'then maximum sides:')
    print('\n'.join('  %14r perim: %3i area: %i'
                    % (sides, sum(sides), hero(*sides)) for sides in h[:10]))
    print('\nAll with area 210 subject to the previous ordering:')
    print('\n'.join('  %14r perim: %3i area: %i'
                    % (sides, sum(sides), hero(*sides)) for sides in h
                    if hero(*sides) == 210))

```

