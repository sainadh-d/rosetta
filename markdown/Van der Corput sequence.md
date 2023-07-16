# Van der Corput sequence

## Task Link
[Rosetta Code - Van der Corput sequence](https://rosettacode.org/wiki/Van_der_Corput_sequence)

## Java Code
### java_code_1.txt
```java
public class VanDerCorput{
	public static double vdc(int n){
		double vdc = 0;
		int denom = 1;
		while(n != 0){
			vdc += n % 2.0 / (denom *= 2);
			n /= 2;
		}
		return vdc;
	}
	
	public static void main(String[] args){
		for(int i = 0; i <= 10; i++){
			System.out.println(vdc(i));
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def base10change(n, base):
	digits = []
	while n:
		n,remainder = divmod(n, base)
		digits.insert(0, remainder)
	return digits

>>> base10change(11, 2)
[1, 0, 1, 1]

```

### python_code_2.txt
```python
def vdc(n, base=2):
    vdc, denom = 0,1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc

```

### python_code_3.txt
```python
>>> [vdc(i) for i in range(10)]
[0, 0.5, 0.25, 0.75, 0.125, 0.625, 0.375, 0.875, 0.0625, 0.5625]
>>> [vdc(i, 3) for i in range(10)]
[0, 0.3333333333333333, 0.6666666666666666, 0.1111111111111111, 0.4444444444444444, 0.7777777777777777, 0.2222222222222222, 0.5555555555555556, 0.8888888888888888, 0.037037037037037035]
>>>

```

### python_code_4.txt
```python
>>> from fractions import Fraction
>>> Fraction.__repr__ = lambda x: '%i/%i' % (x.numerator, x.denominator)
>>> [vdc(i, base=Fraction(2)) for i in range(10)]
[0, 1/2, 1/4, 3/4, 1/8, 5/8, 3/8, 7/8, 1/16, 9/16]

```

### python_code_5.txt
```python
>>> for b in range(3,6):
	print('\nBase', b)
	print([vdc(i, base=Fraction(b)) for i in range(10)])

Base 3
[0, 1/3, 2/3, 1/9, 4/9, 7/9, 2/9, 5/9, 8/9, 1/27]

Base 4
[0, 1/4, 1/2, 3/4, 1/16, 5/16, 9/16, 13/16, 1/8, 3/8]

Base 5
[0, 1/5, 2/5, 3/5, 4/5, 1/25, 6/25, 11/25, 16/25, 21/25]

```

