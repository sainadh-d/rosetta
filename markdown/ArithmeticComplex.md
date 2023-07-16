# Arithmetic/Complex

## Task Link
[Rosetta Code - Arithmetic/Complex](https://rosettacode.org/wiki/Arithmetic/Complex)

## Java Code
### java_code_1.txt
```java
public class Complex {
    public final double real;
    public final double imag;

    public Complex() {
        this(0, 0);
    }

    public Complex(double r, double i) {
        real = r;
        imag = i;
    }

    public Complex add(Complex b) {
        return new Complex(this.real + b.real, this.imag + b.imag);
    }

    public Complex mult(Complex b) {
        // FOIL of (a+bi)(c+di) with i*i = -1
        return new Complex(this.real * b.real - this.imag * b.imag,
                this.real * b.imag + this.imag * b.real);
    }

    public Complex inv() {
        // 1/(a+bi) * (a-bi)/(a-bi) = 1/(a+bi) but it's more workable
        double denom = real * real + imag * imag;
        return new Complex(real / denom, -imag / denom);
    }

    public Complex neg() {
        return new Complex(-real, -imag);
    }

    public Complex conj() {
        return new Complex(real, -imag);
    }

    @Override
    public String toString() {
        return real + " + " + imag + " * i";
    }

    public static void main(String[] args) {
        Complex a = new Complex(Math.PI, -5); //just some numbers
        Complex b = new Complex(-1, 2.5);
        System.out.println(a.neg());
        System.out.println(a.add(b));
        System.out.println(a.inv());
        System.out.println(a.mult(b));
        System.out.println(a.conj());
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> z1 = 1.5 + 3j
>>> z2 = 1.5 + 1.5j
>>> z1 + z2
(3+4.5j)
>>> z1 - z2
1.5j
>>> z1 * z2
(-2.25+6.75j)
>>> z1 / z2
(1.5+0.5j)
>>> - z1
(-1.5-3j)
>>> z1.conjugate()
(1.5-3j)
>>> abs(z1)
3.3541019662496847
>>> z1 ** z2
(-1.1024829553277784-0.38306415117199333j)
>>> z1.real
1.5
>>> z1.imag
3.0
>>>

```

