# Roots of unity

## Task Link
[Rosetta Code - Roots of unity](https://rosettacode.org/wiki/Roots_of_unity)

## Java Code
### java_code_1.txt
```java
import java.util.Locale;

public class Test {

    public static void main(String[] a) {
        for (int n = 2; n < 6; n++)
            unity(n);
    }

    public static void unity(int n) {
        System.out.printf("%n%d: ", n);

        //all the way around the circle at even intervals
        for (double angle = 0; angle < 2 * Math.PI; angle += (2 * Math.PI) / n) {

            double real = Math.cos(angle); //real axis is the x axis

            if (Math.abs(real) < 1.0E-3)
                real = 0.0; //get rid of annoying sci notation

            double imag = Math.sin(angle); //imaginary axis is the y axis

            if (Math.abs(imag) < 1.0E-3)
                imag = 0.0;

            System.out.printf(Locale.US, "(%9f,%9f) ", real, imag);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import cmath


class Complex(complex):
    def __repr__(self):
        rp = '%7.5f' % self.real if not self.pureImag() else ''
        ip = '%7.5fj' % self.imag if not self.pureReal() else ''
        conj = '' if (
            self.pureImag() or self.pureReal() or self.imag < 0.0
        ) else '+'
        return '0.0' if (
            self.pureImag() and self.pureReal()
        ) else rp + conj + ip

    def pureImag(self):
        return abs(self.real) < 0.000005

    def pureReal(self):
        return abs(self.imag) < 0.000005


def croots(n):
    if n <= 0:
        return None
    return (Complex(cmath.rect(1, 2 * k * cmath.pi / n)) for k in range(n))
    # in pre-Python 2.6:
    #   return (Complex(cmath.exp(2j*k*cmath.pi/n)) for k in range(n))


for nr in range(2, 11):
    print(nr, list(croots(nr)))

```

