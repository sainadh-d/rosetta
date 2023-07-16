# Averages/Arithmetic mean

## Task Link
[Rosetta Code - Averages/Arithmetic mean](https://rosettacode.org/wiki/Averages/Arithmetic_mean)

## Java Code
### java_code_1.txt
```java
public static double avg(double... arr) {
    double sum = 0.0;
    for (double x : arr) {
        sum += x;
    }
    return sum / arr.length;
}

```

## Python Code
### python_code_1.txt
```python
from math import fsum
def average(x):
    return fsum(x)/float(len(x)) if x else 0
print (average([0,0,3,1,4,1,5,9,0,0]))
print (average([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))

```

### python_code_2.txt
```python
2.3
2.3

```

### python_code_3.txt
```python
def average(x):
    return sum(x)/float(len(x)) if x else 0
print (average([0,0,3,1,4,1,5,9,0,0]))
print (average([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))

```

### python_code_4.txt
```python
2.3
1e-21

```

### python_code_5.txt
```python
def avg(data):
    if len(data)==0:
        return 0
    else:
        return sum(data)/float(len(data))
print avg([0,0,3,1,4,1,5,9,0,0])

```

### python_code_6.txt
```python
2.3

```

### python_code_7.txt
```python
>>> from statistics import mean
>>> mean([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20])
2.3
>>> mean([10**10000, -10**10000, 3, 1, 4, 1, 5, 9, 0, 0])
2.3
>>> mean([10**10000, -10**10000, 3, 1, 4, 1, 5, 9, Fraction(1, 10**10000), Fraction(-1, 10**10000)])
Fraction(23, 10)
>>> big = 10**10000
>>> mean([Decimal(big), Decimal(-big), 3, 1, 4, 1, 5, 9, 1/Decimal(big), -1/Decimal(big)])
Decimal('2.3')

```

### python_code_8.txt
```python
def (mean l)
  sum.l / len.l

```

