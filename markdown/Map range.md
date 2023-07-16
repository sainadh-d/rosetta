# Map range

## Task Link
[Rosetta Code - Map range](https://rosettacode.org/wiki/Map_range)

## Java Code
### java_code_1.txt
```java
public class Range {
	public static void main(String[] args){
		for(float s = 0;s <= 10; s++){
			System.out.println(s + " in [0, 10] maps to "+ 
					mapRange(0, 10, -1, 0, s)+" in [-1, 0].");
		}
	}
	
	public static double mapRange(double a1, double a2, double b1, double b2, double s){
		return b1 + ((s - a1)*(b2 - b1))/(a2 - a1);
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def maprange( a, b, s):
	(a1, a2), (b1, b2) = a, b
	return  b1 + ((s - a1) * (b2 - b1) / (a2 - a1))

>>> for s in range(11):
	print("%2g maps to %g" % (s, maprange( (0, 10), (-1, 0), s)))

	
 0 maps to -1
 1 maps to -0.9
 2 maps to -0.8
 3 maps to -0.7
 4 maps to -0.6
 5 maps to -0.5
 6 maps to -0.4
 7 maps to -0.3
 8 maps to -0.2
 9 maps to -0.1
10 maps to 0

```

### python_code_2.txt
```python
>>> from fractions import Fraction
>>> for s in range(11):
	print("%2g maps to %s" % (s, maprange( (0, 10), (-1, 0), Fraction(s))))

	
 0 maps to -1
 1 maps to -9/10
 2 maps to -4/5
 3 maps to -7/10
 4 maps to -3/5
 5 maps to -1/2
 6 maps to -2/5
 7 maps to -3/10
 8 maps to -1/5
 9 maps to -1/10
10 maps to 0
>>>

```

