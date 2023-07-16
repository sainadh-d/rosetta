# Random numbers

## Task Link
[Rosetta Code - Random numbers](https://rosettacode.org/wiki/Random_numbers)

## Java Code
### java_code_1.txt
```java
double[] list = new double[1000];
double mean = 1.0, std = 0.5;
Random rng = new Random();
for(int i = 0;i<list.length;i++) {
  list[i] = mean + std * rng.nextGaussian();
}

```

## Python Code
### python_code_1.txt
```python
>>> import random
>>> values = [random.gauss(1, .5) for i in range(1000)]
>>>

```

### python_code_2.txt
```python
>>> def quick_check(numbers):
    count = len(numbers)
    mean = sum(numbers) / count
    sdeviation = (sum((i - mean)**2 for i in numbers) / count)**0.5
    return mean, sdeviation

>>> quick_check(values)
(1.0140373306786599, 0.49943411329234066)
>>>

```

### python_code_3.txt
```python
>>> values = [ random.normalvariate(1, 0.5) for i in range(1000)]
>>> quick_check(values)
(0.990099111944864, 0.5029847005836282)
>>>

```

