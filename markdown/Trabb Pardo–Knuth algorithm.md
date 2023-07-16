# Trabb Pardo–Knuth algorithm

## Task Link
[Rosetta Code - Trabb Pardo–Knuth algorithm](https://rosettacode.org/wiki/Trabb_Pardo%E2%80%93Knuth_algorithm)

## Java Code
### java_code_1.txt
```java
/**
 * Alexander Alvonellos 
 */
import java.util.*;
import java.io.*; 

public class TPKA {
	public static void main(String... args) {
		double[] input = new double[11];
		double userInput = 0.0;
		Scanner in = new Scanner(System.in);
		for(int i = 0; i < 11; i++) {
			System.out.print("Please enter a number: ");
			String s = in.nextLine();
			try {
				userInput = Double.parseDouble(s);
			} catch (NumberFormatException e) { 
				System.out.println("You entered invalid input, exiting");
				System.exit(1);
			}
			input[i] = userInput;
		}
		for(int j = 10; j >= 0; j--) {
			double x = input[j]; double y = f(x);
			if( y < 400.0) {
				System.out.printf("f( %.2f ) = %.2f\n", x, y);
			} else {
				System.out.printf("f( %.2f ) = %s\n", x, "TOO LARGE");
			}
		}
	}

	private static double f(double x) {
		return Math.pow(Math.abs(x), 0.5) + (5*(Math.pow(x, 3)));
	}
}

```

## Python Code
### python_code_1.txt
```python
Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(x): return abs(x) ** 0.5 + 5 * x**3

>>> print(', '.join('%s:%s' % (x, v if v<=400 else "TOO LARGE!")
	           for x,v in ((y, f(float(y))) for y in input('\nnumbers: ').strip().split()[:11][::-1])))

11 numbers: 1 2 3 4 5 6 7 8 9 10 11
11:TOO LARGE!, 10:TOO LARGE!, 9:TOO LARGE!, 8:TOO LARGE!, 7:TOO LARGE!, 6:TOO LARGE!, 5:TOO LARGE!, 4:322.0, 3:136.73205080756887, 2:41.41421356237309, 1:6.0
>>>

```

### python_code_2.txt
```python
import math

def f(x):
    return math.sqrt(abs(x)) + 5 * x**3

def ask_numbers(n=11):
    print(f'Enter {n} numbers:')
    return (float(input('>')) for _ in range(n))

if __name__ == '__main__':
    for x in ask_numbers().reverse():
        if (result := f(x)) > 400:
            print(f'f({x}): overflow')
        else:
            print(f'f({x}) = {result}')

```

