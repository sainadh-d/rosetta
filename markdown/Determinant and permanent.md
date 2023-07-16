# Determinant and permanent

## Task Link
[Rosetta Code - Determinant and permanent](https://rosettacode.org/wiki/Determinant_and_permanent)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class MatrixArithmetic {
	public static double[][] minor(double[][] a, int x, int y){
		int length = a.length-1;
		double[][] result = new double[length][length];
		for(int i=0;i<length;i++) for(int j=0;j<length;j++){
			if(i<x && j<y){
				result[i][j] = a[i][j];
			}else if(i>=x && j<y){
				result[i][j] = a[i+1][j];
			}else if(i<x && j>=y){
				result[i][j] = a[i][j+1];
			}else{ //i>x && j>y
				result[i][j] = a[i+1][j+1];
			}
		}
		return result;
	}
	public static double det(double[][] a){
		if(a.length == 1){
			return a[0][0];
		}else{
			int sign = 1;
			double sum = 0;
			for(int i=0;i<a.length;i++){
				sum += sign * a[0][i] * det(minor(a,0,i));
				sign *= -1;
			}
			return sum;
		}
	}
	public static double perm(double[][] a){
		if(a.length == 1){
			return a[0][0];
		}else{
			double sum = 0;
			for(int i=0;i<a.length;i++){
				sum += a[0][i] * perm(minor(a,0,i));
			}
			return sum;
		}
	}
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		double[][] a = new double[size][size];
		for(int i=0;i<size;i++) for(int j=0;j<size;j++){
			a[i][j] = sc.nextDouble();
		}
		sc.close();
		System.out.println("Determinant: "+det(a));
		System.out.println("Permanent: "+perm(a));
	}
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations
from operator import mul
from math import fsum
from spermutations import spermutations

def prod(lst):
    return reduce(mul, lst, 1)

def perm(a):
    n = len(a)
    r = range(n)
    s = permutations(r)
    return fsum(prod(a[i][sigma[i]] for i in r) for sigma in s)

def det(a):
    n = len(a)
    r = range(n)
    s = spermutations(n)
    return fsum(sign * prod(a[i][sigma[i]] for i in r)
                for sigma, sign in s)

if __name__ == '__main__':
    from pprint import pprint as pp

    for a in ( 
            [
             [1, 2], 
             [3, 4]], 

            [
             [1, 2, 3, 4],
             [4, 5, 6, 7],
             [7, 8, 9, 10],
             [10, 11, 12, 13]],        

            [
             [ 0,  1,  2,  3,  4],
             [ 5,  6,  7,  8,  9],
             [10, 11, 12, 13, 14],
             [15, 16, 17, 18, 19],
             [20, 21, 22, 23, 24]],
        ):
        print('')
        pp(a)
        print('Perm: %s Det: %s' % (perm(a), det(a)))

```

