# Price fraction

## Task Link
[Rosetta Code - Price fraction](https://rosettacode.org/wiki/Price_fraction)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class Main {
	private static float priceFraction(float f) {
		if (0.00f <= f && f < 0.06f) return 0.10f;
		else if (f < 0.11f) return 0.18f;
		else if (f < 0.16f) return 0.26f;
		else if (f < 0.21f) return 0.32f;
		else if (f < 0.26f) return 0.38f;
		else if (f < 0.31f) return 0.44f;
		else if (f < 0.36f) return 0.50f;
		else if (f < 0.41f) return 0.54f;
		else if (f < 0.46f) return 0.58f;
		else if (f < 0.51f) return 0.62f;
		else if (f < 0.56f) return 0.66f;
		else if (f < 0.61f) return 0.70f;
		else if (f < 0.66f) return 0.74f;
		else if (f < 0.71f) return 0.78f;
		else if (f < 0.76f) return 0.82f;
		else if (f < 0.81f) return 0.86f;
		else if (f < 0.86f) return 0.90f;
		else if (f < 0.91f) return 0.94f;
		else if (f < 0.96f) return 0.98f;
		else if (f < 1.01f) return 1.00f;
		else throw new IllegalArgumentException();
	}

	public static void main(String[] args) {
		Random rnd = new Random();
		for (int i = 0; i < 5; i++) {
			float f = rnd.nextFloat();
			System.out.format("%8.6f -> %4.2f%n", f, priceFraction(f));
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> import bisect
>>> _cin  = [.06, .11, .16, .21, .26, .31, .36, .41, .46, .51, .56, .61, .66, .71, .76, .81, .86, .91, .96, 1.01]
>>> _cout = [.10, .18, .26, .32, .38, .44, .50, .54, .58, .62, .66, .70, .74, .78, .82, .86, .90, .94, .98, 1.00]
>>> def pricerounder(pricein):
	return _cout[ bisect.bisect_right(_cin, pricein) ]

```

### python_code_2.txt
```python
>>> import bisect
>>> _cin  = [ 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101]
>>> _cout = [10, 18, 26, 32, 38, 44, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 100]
>>> def centsrounder(centsin):
	return _cout[ bisect.bisect_right(_cin, centsin) ]

```

### python_code_3.txt
```python
def bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo

```

