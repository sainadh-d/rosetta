# Cholesky decomposition

## Task Link
[Rosetta Code - Cholesky decomposition](https://rosettacode.org/wiki/Cholesky_decomposition)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Cholesky {
	public static double[][] chol(double[][] a){
		int m = a.length;
		double[][] l = new double[m][m]; //automatically initialzed to 0's
		for(int i = 0; i< m;i++){
			for(int k = 0; k < (i+1); k++){
				double sum = 0;
				for(int j = 0; j < k; j++){
					sum += l[i][j] * l[k][j];
				}
				l[i][k] = (i == k) ? Math.sqrt(a[i][i] - sum) :
					(1.0 / l[k][k] * (a[i][k] - sum));
			}
		}
		return l;
	}
	
	public static void main(String[] args){
		double[][] test1 = {{25, 15, -5},
							{15, 18, 0},
							{-5, 0, 11}};
		System.out.println(Arrays.deepToString(chol(test1)));
		double[][] test2 = {{18, 22, 54, 42},
							{22, 70, 86, 62},
							{54, 86, 174, 134},
							{42, 62, 134, 106}};
		System.out.println(Arrays.deepToString(chol(test2)));
	}
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

from pprint import pprint
from math import sqrt


def cholesky(A):
    L = [[0.0] * len(A) for _ in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else \
                      (1.0 / L[j][j] * (A[i][j] - s))
    return L

if __name__ == "__main__":
    m1 = [[25, 15, -5],
          [15, 18,  0],
          [-5,  0, 11]]
    pprint(cholesky(m1))
    print()
    
    m2 = [[18, 22,  54,  42],
          [22, 70,  86,  62],
          [54, 86, 174, 134],
          [42, 62, 134, 106]]
    pprint(cholesky(m2), width=120)

```

### python_code_2.txt
```python
def cholesky(A):
    L = [[0.0] * len(A) for _ in range(len(A))]
    for i, (Ai, Li) in enumerate(zip(A, L)):
        for j, Lj in enumerate(L[:i+1]):
            s = sum(Li[k] * Lj[k] for k in range(j))
            Li[j] = sqrt(Ai[i] - s) if (i == j) else \
                      (1.0 / Lj[j] * (Ai[j] - s))
    return L

```

