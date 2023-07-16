# Cumulative standard deviation

## Task Link
[Rosetta Code - Cumulative standard deviation](https://rosettacode.org/wiki/Cumulative_standard_deviation)

## Java Code
### java_code_1.txt
```java
public class StdDev {
    int n = 0;
    double sum = 0;
    double sum2 = 0;

    public double sd(double x) {
	n++;
	sum += x;
	sum2 += x*x;

	return Math.sqrt(sum2/n - sum*sum/n/n);
    }

    public static void main(String[] args) {
        double[] testData = {2,4,4,4,5,5,7,9};
        StdDev sd = new StdDev();

        for (double x : testData) {
            System.out.println(sd.sd(x));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from math import sqrt
>>> def sd(x):
    sd.sum  += x
    sd.sum2 += x*x
    sd.n    += 1.0
    sum, sum2, n = sd.sum, sd.sum2, sd.n
    return sqrt(sum2/n - sum*sum/n/n)

>>> sd.sum = sd.sum2 = sd.n = 0
>>> for value in (2,4,4,4,5,5,7,9):
    print (value, sd(value))

    
(2, 0.0)
(4, 1.0)
(4, 0.94280904158206258)
(4, 0.8660254037844386)
(5, 0.97979589711327075)
(5, 1.0)
(7, 1.3997084244475311)
(9, 2.0)
>>>

```

### python_code_2.txt
```python
>>> class SD(object): # Plain () for python 3.x
	def __init__(self):
		self.sum, self.sum2, self.n = (0,0,0)
	def sd(self, x):
		self.sum  += x
		self.sum2 += x*x
		self.n    += 1.0
		sum, sum2, n = self.sum, self.sum2, self.n
		return sqrt(sum2/n - sum*sum/n/n)

>>> sd_inst = SD()
>>> for value in (2,4,4,4,5,5,7,9):
	print (value, sd_inst.sd(value))

```

### python_code_3.txt
```python
>>> from math import sqrt
>>> def sdcreator():
	sum = sum2 = n = 0
	def sd(x):
		nonlocal sum, sum2, n

		sum  += x
		sum2 += x*x
		n    += 1.0
		return sqrt(sum2/n - sum*sum/n/n)
	return sd

>>> sd = sdcreator()
>>> for value in (2,4,4,4,5,5,7,9):
	print (value, sd(value))

	
2 0.0
4 1.0
4 0.942809041582
4 0.866025403784
5 0.979795897113
5 1.0
7 1.39970842445
9 2.0

```

### python_code_4.txt
```python
>>> from math import sqrt
>>> def sdcreator():
	sum = sum2 = n = 0
	while True:
		x = yield sqrt(sum2/n - sum*sum/n/n) if n else None

		sum  += x
		sum2 += x*x
		n    += 1.0

>>> sd = sdcreator()
>>> sd.send(None)
>>> for value in (2,4,4,4,5,5,7,9):
	print (value, sd.send(value))

	
2 0.0
4 1.0
4 0.942809041582
4 0.866025403784
5 0.979795897113
5 1.0
7 1.39970842445
9 2.0

```

### python_code_5.txt
```python
>>> myMean = lambda MyList : reduce(lambda x, y: x + y, MyList) / float(len(MyList))
>>> myStd = lambda MyList : (reduce(lambda x,y : x + y , map(lambda x: (x-myMean(MyList))**2 , MyList)) / float(len(MyList)))**.5

>>> print myStd([2,4,4,4,5,5,7,9])
2.0

```

