# One of n lines in a file

## Task Link
[Rosetta Code - One of n lines in a file](https://rosettacode.org/wiki/One_of_n_lines_in_a_file)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Random;

public class OneOfNLines {

	static Random rand;
	
	public static int oneOfN(int n) {
		int choice = 0;
		
		for(int i = 1; i < n; i++) {
			if(rand.nextInt(i+1) == 0)
				choice = i;
		}
		
		return choice;
	}
	
	public static void main(String[] args) {
		int n = 10;
		int trials = 1000000;
		int[] bins = new int[n];
		rand = new Random();
		
		for(int i = 0; i < trials; i++)
			bins[oneOfN(n)]++;
		
		
		System.out.println(Arrays.toString(bins));
	}
}

```

## Python Code
### python_code_1.txt
```python
from random import randrange
try:
    range = xrange
except: pass

def one_of_n(lines): # lines is any iterable
    choice = None
    for i, line in enumerate(lines):
        if randrange(i+1) == 0:
            choice = line
    return choice
            
def one_of_n_test(n=10, trials=1000000):
    bins = [0] * n
    if n:
        for i in range(trials):
            bins[one_of_n(range(n))] += 1
    return bins

print(one_of_n_test())

```

