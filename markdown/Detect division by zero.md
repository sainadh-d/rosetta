# Detect division by zero

## Task Link
[Rosetta Code - Detect division by zero](https://rosettacode.org/wiki/Detect_division_by_zero)

## Java Code
### java_code_1.txt
```java
public static boolean infinity(double numer, double denom){
	return Double.isInfinite(numer/denom);
}

```

### java_code_2.txt
```java
public static boolean except(double numer, double denom){
	try{
		int dummy = (int)numer / (int)denom;//ArithmeticException is only thrown from integer math
		return false;
	}catch(ArithmeticException e){return true;}
}

```

## Python Code
### python_code_1.txt
```python
def div_check(x, y):
  try:
    x / y
  except ZeroDivisionError:
    return True
  else:
    return False

```

