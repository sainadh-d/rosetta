# Temperature conversion

## Task Link
[Rosetta Code - Temperature conversion](https://rosettacode.org/wiki/Temperature_conversion)

## Java Code
### java_code_1.txt
```java
public class TemperatureConversion {
    public static void main(String args[]) {
        if (args.length == 1) {
            try {
                double kelvin = Double.parseDouble(args[0]);
                if (kelvin >= 0) {
                    System.out.printf("K  %2.2f\n", kelvin);
                    System.out.printf("C  %2.2f\n", kelvinToCelsius(kelvin));
                    System.out.printf("F  %2.2f\n", kelvinToFahrenheit(kelvin));
                    System.out.printf("R  %2.2f\n", kelvinToRankine(kelvin));
                } else {
                    System.out.printf("%2.2f K is below absolute zero", kelvin);
                }
            } catch (NumberFormatException e) {
                System.out.println(e);
            }
        }
    }

    public static double kelvinToCelsius(double k) {
        return k - 273.15;
    }

    public static double kelvinToFahrenheit(double k) {
        return k * 1.8 - 459.67;
    }

    public static double kelvinToRankine(double k) {
        return k * 1.8;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> while True:
    k = float(input('K ? '))
    print("%g Kelvin = %g Celsius = %g Fahrenheit = %g Rankine degrees."
          % (k, k - 273.15, k * 1.8 - 459.67, k * 1.8))

    
K ? 21.0
21 Kelvin = -252.15 Celsius = -421.87 Fahrenheit = 37.8 Rankine degrees.
K ? 222.2
222.2 Kelvin = -50.95 Celsius = -59.71 Fahrenheit = 399.96 Rankine degrees.
K ?

```

### python_code_2.txt
```python
>>> toK = {'C': (lambda c: c + 273.15),
           'F': (lambda f: (f + 459.67) / 1.8),
           'R': (lambda r: r / 1.8),
           'K': (lambda k: k) }
>>> while True:
    magnitude, unit = input('<value> <K/R/F/C> ? ').split()
    k = toK[unit](float(magnitude))
    print("%g Kelvin = %g Celsius = %g Fahrenheit = %g Rankine degrees."
          % (k, k - 273.15, k * 1.8 - 459.67, k * 1.8))

    
<value> <K/R/F/C> ? 222.2 K
222.2 Kelvin = -50.95 Celsius = -59.71 Fahrenheit = 399.96 Rankine degrees.
<value> <K/R/F/C> ? -50.95 C
222.2 Kelvin = -50.95 Celsius = -59.71 Fahrenheit = 399.96 Rankine degrees.
<value> <K/R/F/C> ? -59.71 F
222.2 Kelvin = -50.95 Celsius = -59.71 Fahrenheit = 399.96 Rankine degrees.
<value> <K/R/F/C> ? 399.96 R
222.2 Kelvin = -50.95 Celsius = -59.71 Fahrenheit = 399.96 Rankine degrees.
<value> <K/R/F/C> ?

```

