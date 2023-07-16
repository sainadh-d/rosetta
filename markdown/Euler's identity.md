# Euler's identity

## Task Link
[Rosetta Code - Euler's identity](https://rosettacode.org/wiki/Euler%27s_identity)

## Java Code
### java_code_1.txt
```java
public class EulerIdentity {

    public static void main(String[] args) {
        System.out.println("e ^ (i*Pi) + 1 = " + (new Complex(0, Math.PI).exp()).add(new Complex(1, 0)));
    }

    public static class Complex {

        private double x, y;
        
        public Complex(double re, double im) {
            x = re;
            y = im;
        }
        
        public Complex exp() {
            double exp = Math.exp(x);
            return new Complex(exp * Math.cos(y), exp * Math.sin(y));
        }
        
        public Complex add(Complex a) {
            return new Complex(x + a.x, y + a.y);
        }
        
        @Override
        public String toString() {
            return x + " + " + y + "i";
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import math
>>> math.e ** (math.pi * 1j) + 1
1.2246467991473532e-16j

```

