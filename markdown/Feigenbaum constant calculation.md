# Feigenbaum constant calculation

## Task Link
[Rosetta Code - Feigenbaum constant calculation](https://rosettacode.org/wiki/Feigenbaum_constant_calculation)

## Java Code
### java_code_1.txt
```java
public class Feigenbaum {
    public static void main(String[] args) {
        int max_it = 13;
        int max_it_j = 10;
        double a1 = 1.0;
        double a2 = 0.0;
        double d1 = 3.2;
        double a;

        System.out.println(" i       d");
        for (int i = 2; i <= max_it; i++) {
            a = a1 + (a1 - a2) / d1;
            for (int j = 0; j < max_it_j; j++) {
                double x = 0.0;
                double y = 0.0;
                for (int k = 0; k < 1 << i; k++) {
                    y = 1.0 - 2.0 * y * x;
                    x = a - x * x;
                }
                a -= x / y;
            }
            double d = (a1 - a2) / (a - a1);
            System.out.printf("%2d    %.8f\n", i, d);
            d1 = d;
            a2 = a1;
            a1 = a;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
max_it = 13
max_it_j = 10
a1 = 1.0
a2 = 0.0
d1 = 3.2
a = 0.0

print " i       d"
for i in range(2, max_it + 1):
    a = a1 + (a1 - a2) / d1
    for j in range(1, max_it_j + 1):
        x = 0.0
        y = 0.0
        for k in range(1, (1 << i) + 1):
            y = 1.0 - 2.0 * y * x
            x = a - x * x
        a = a - x / y
    d = (a1 - a2) / (a - a1)
    print("{0:2d}    {1:.8f}".format(i, d))
    d1 = d
    a2 = a1
    a1 = a

```

