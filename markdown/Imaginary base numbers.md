# Imaginary base numbers

## Task Link
[Rosetta Code - Imaginary base numbers](https://rosettacode.org/wiki/Imaginary_base_numbers)

## Java Code
### java_code_1.txt
```java
public class ImaginaryBaseNumber {
    private static class Complex {
        private Double real, imag;

        public Complex(double r, double i) {
            this.real = r;
            this.imag = i;
        }

        public Complex(int r, int i) {
            this.real = (double) r;
            this.imag = (double) i;
        }

        public Complex add(Complex rhs) {
            return new Complex(
                real + rhs.real,
                imag + rhs.imag
            );
        }

        public Complex times(Complex rhs) {
            return new Complex(
                real * rhs.real - imag * rhs.imag,
                real * rhs.imag + imag * rhs.real
            );
        }

        public Complex times(double rhs) {
            return new Complex(
                real * rhs,
                imag * rhs
            );
        }

        public Complex inv() {
            double denom = real * real + imag * imag;
            return new Complex(
                real / denom,
                -imag / denom
            );
        }

        public Complex unaryMinus() {
            return new Complex(-real, -imag);
        }

        public Complex divide(Complex rhs) {
            return this.times(rhs.inv());
        }

        // only works properly if 'real' and 'imag' are both integral
        public QuaterImaginary toQuaterImaginary() {
            if (real == 0.0 && imag == 0.0) return new QuaterImaginary("0");
            int re = real.intValue();
            int im = imag.intValue();
            int fi = -1;
            StringBuilder sb = new StringBuilder();
            while (re != 0) {
                int rem = re % -4;
                re /= -4;
                if (rem < 0) {
                    rem += 4;
                    re++;
                }
                sb.append(rem);
                sb.append(0);
            }
            if (im != 0) {
                Double f = new Complex(0.0, imag).divide(new Complex(0.0, 2.0)).real;
                im = ((Double) Math.ceil(f)).intValue();
                f = -4.0 * (f - im);
                int index = 1;
                while (im != 0) {
                    int rem = im % -4;
                    im /= -4;
                    if (rem < 0) {
                        rem += 4;
                        im++;
                    }
                    if (index < sb.length()) {
                        sb.setCharAt(index, (char) (rem + 48));
                    } else {
                        sb.append(0);
                        sb.append(rem);
                    }
                    index += 2;
                }
                fi = f.intValue();
            }
            sb.reverse();
            if (fi != -1) sb.append(".").append(fi);
            while (sb.charAt(0) == '0') sb.deleteCharAt(0);
            if (sb.charAt(0) == '.') sb.insert(0, '0');
            return new QuaterImaginary(sb.toString());
        }

        @Override
        public String toString() {
            double real2 = real == -0.0 ? 0.0 : real;  // get rid of negative zero
            double imag2 = imag == -0.0 ? 0.0 : imag;  // ditto
            String result = imag2 >= 0.0 ? String.format("%.0f + %.0fi", real2, imag2) : String.format("%.0f - %.0fi", real2, -imag2);
            result = result.replace(".0 ", " ").replace(".0i", "i").replace(" + 0i", "");
            if (result.startsWith("0 + ")) result = result.substring(4);
            if (result.startsWith("0 - ")) result = result.substring(4);
            return result;
        }
    }

    private static class QuaterImaginary {
        private static final Complex TWOI = new Complex(0.0, 2.0);
        private static final Complex INVTWOI = TWOI.inv();

        private String b2i;

        public QuaterImaginary(String b2i) {
            if (b2i.equals("") || !b2i.chars().allMatch(c -> "0123.".indexOf(c) > -1) || b2i.chars().filter(c -> c == '.').count() > 1) {
                throw new RuntimeException("Invalid Base 2i number");
            }
            this.b2i = b2i;
        }

        public Complex toComplex() {
            int pointPos = b2i.indexOf(".");
            int posLen = pointPos != -1 ? pointPos : b2i.length();
            Complex sum = new Complex(0, 0);
            Complex prod = new Complex(1, 0);

            for (int j = 0; j < posLen; ++j) {
                double k = b2i.charAt(posLen - 1 - j) - '0';
                if (k > 0.0) sum = sum.add(prod.times(k));
                prod = prod.times(TWOI);
            }
            if (pointPos != -1) {
                prod = INVTWOI;
                for (int j = posLen + 1; j < b2i.length(); ++j) {
                    double k = b2i.charAt(j) - '0';
                    if (k > 0.0) sum = sum.add(prod.times(k));
                    prod = prod.times(INVTWOI);
                }
            }

            return sum;
        }

        @Override
        public String toString() {
            return b2i;
        }
    }

    public static void main(String[] args) {
        String fmt = "%4s -> %8s -> %4s";
        for (int i = 1; i <= 16; ++i) {
            Complex c1 = new Complex(i, 0);
            QuaterImaginary qi = c1.toQuaterImaginary();
            Complex c2 = qi.toComplex();
            System.out.printf(fmt + "     ", c1, qi, c2);
            c1 = c2.unaryMinus();
            qi = c1.toQuaterImaginary();
            c2 = qi.toComplex();
            System.out.printf(fmt, c1, qi, c2);
            System.out.println();
        }
        System.out.println();
        for (int i = 1; i <= 16; ++i) {
            Complex c1 = new Complex(0, i);
            QuaterImaginary qi = c1.toQuaterImaginary();
            Complex c2 = qi.toComplex();
            System.out.printf(fmt + "     ", c1, qi, c2);
            c1 = c2.unaryMinus();
            qi = c1.toQuaterImaginary();
            c2 = qi.toComplex();
            System.out.printf(fmt, c1, qi, c2);
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import math
import re

def inv(c):
    denom = c.real * c.real + c.imag * c.imag
    return complex(c.real / denom, -c.imag / denom)

class QuaterImaginary:
    twoI = complex(0, 2)
    invTwoI = inv(twoI)

    def __init__(self, str):
        if not re.match("^[0123.]+$", str) or str.count('.') > 1:
            raise Exception('Invalid base 2i number')
        self.b2i = str

    def toComplex(self):
        pointPos = self.b2i.find('.')
        posLen = len(self.b2i) if (pointPos < 0) else pointPos
        sum = complex(0, 0)
        prod = complex(1, 0)
        for j in xrange(0, posLen):
            k = int(self.b2i[posLen - 1 - j])
            if k > 0:
                sum += prod * k
            prod *= QuaterImaginary.twoI
        if pointPos != -1:
            prod = QuaterImaginary.invTwoI
            for j in xrange(posLen + 1, len(self.b2i)):
                k = int(self.b2i[j])
                if k > 0:
                    sum += prod * k
                prod *= QuaterImaginary.invTwoI
        return sum

    def __str__(self):
        return str(self.b2i)

def toQuaterImaginary(c):
    if c.real == 0.0 and c.imag == 0.0:
        return QuaterImaginary("0")

    re = int(c.real)
    im = int(c.imag)
    fi = -1
    ss = ""
    while re != 0:
        re, rem = divmod(re, -4)
        if rem < 0:
            rem += 4
            re += 1
        ss += str(rem) + '0'
    if im != 0:
        f = c.imag / 2
        im = int(math.ceil(f))
        f = -4 * (f - im)
        index = 1
        while im != 0:
            im, rem = divmod(im, -4)
            if rem < 0:
                rem += 4
                im += 1
            if index < len(ss):
                ss[index] = str(rem)
            else:
                ss += '0' + str(rem)
            index = index + 2
        fi = int(f)
    ss = ss[::-1]
    if fi != -1:
        ss += '.' + str(fi)
    ss = ss.lstrip('0')
    if ss[0] == '.':
        ss = '0' + ss
    return QuaterImaginary(ss)

for i in xrange(1,17):
    c1 = complex(i, 0)
    qi = toQuaterImaginary(c1)
    c2 = qi.toComplex()
    print "{0:8} -> {1:>8} -> {2:8}     ".format(c1, qi, c2),

    c1 = -c1
    qi = toQuaterImaginary(c1)
    c2 = qi.toComplex()
    print "{0:8} -> {1:>8} -> {2:8}".format(c1, qi, c2)
print

for i in xrange(1,17):
    c1 = complex(0, i)
    qi = toQuaterImaginary(c1)
    c2 = qi.toComplex()
    print "{0:8} -> {1:>8} -> {2:8}     ".format(c1, qi, c2),

    c1 = -c1
    qi = toQuaterImaginary(c1)
    c2 = qi.toComplex()
    print "{0:8} -> {1:>8} -> {2:8}".format(c1, qi, c2)

print "done"

```

