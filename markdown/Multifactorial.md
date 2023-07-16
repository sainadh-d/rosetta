# Multifactorial

## Task Link
[Rosetta Code - Multifactorial](https://rosettacode.org/wiki/Multifactorial)

## Java Code
### java_code_1.txt
```java
public class MultiFact {
	private static long multiFact(long n, int deg){
		long ans = 1;
		for(long i = n; i > 0; i -= deg){
			ans *= i;
		}
		return ans;
	}
	
	public static void main(String[] args){
		for(int deg = 1; deg <= 5; deg++){
			System.out.print("degree " + deg + ":");
			for(long n = 1; n <= 10; n++){
				System.out.print(" " + multiFact(n, deg));
			}
			System.out.println();
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> from functools import reduce
>>> from operator import mul
>>> def mfac(n, m): return reduce(mul, range(n, 0, -m))

>>> for m in range(1, 11): print("%2i: %r" % (m, [mfac(n, m) for n in range(1, 11)]))

 1: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
 2: [1, 2, 3, 8, 15, 48, 105, 384, 945, 3840]
 3: [1, 2, 3, 4, 10, 18, 28, 80, 162, 280]
 4: [1, 2, 3, 4, 5, 12, 21, 32, 45, 120]
 5: [1, 2, 3, 4, 5, 6, 14, 24, 36, 50]
 6: [1, 2, 3, 4, 5, 6, 7, 16, 27, 40]
 7: [1, 2, 3, 4, 5, 6, 7, 8, 18, 30]
 8: [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
 9: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>

```

### python_code_2.txt
```python
>>> def mfac2(n, m): return n if n <= (m + 1) else n * mfac2(n - m, m)

>>> for m in range(1, 6): print("%2i: %r" % (m, [mfac2(n, m) for n in range(1, 11)]))

 1: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
 2: [1, 2, 3, 8, 15, 48, 105, 384, 945, 3840]
 3: [1, 2, 3, 4, 10, 18, 28, 80, 162, 280]
 4: [1, 2, 3, 4, 5, 12, 21, 32, 45, 120]
 5: [1, 2, 3, 4, 5, 6, 14, 24, 36, 50]
>>>

```

