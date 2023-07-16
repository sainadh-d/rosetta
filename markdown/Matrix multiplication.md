# Matrix multiplication

## Task Link
[Rosetta Code - Matrix multiplication](https://rosettacode.org/wiki/Matrix_multiplication)

## Java Code
### java_code_1.txt
```java
public static double[][] mult(double a[][], double b[][]){//a[m][n], b[n][p]
   if(a.length == 0) return new double[0][0];
   if(a[0].length != b.length) return null; //invalid dims

   int n = a[0].length;
   int m = a.length;
   int p = b[0].length;

   double ans[][] = new double[m][p];

   for(int i = 0;i < m;i++){
      for(int j = 0;j < p;j++){
         for(int k = 0;k < n;k++){
            ans[i][j] += a[i][k] * b[k][j];
         }
      }
   }
   return ans;
}

```

## Python Code
### python_code_1.txt
```python
a=((1,  1,  1,   1), # matrix A #
     (2,  4,  8,  16),
     (3,  9, 27,  81),
     (4, 16, 64, 256))

b=((  4  , -3  ,  4/3.,  -1/4. ), # matrix B #
     (-13/3., 19/4., -7/3.,  11/24.),
     (  3/2., -2.  ,  7/6.,  -1/4. ),
     ( -1/6.,  1/4., -1/6.,   1/24.))



def MatrixMul( mtx_a, mtx_b):
    tpos_b = zip( *mtx_b)
    rtn = [[ sum( ea*eb for ea,eb in zip(a,b)) for b in tpos_b] for a in mtx_a]
    return rtn


v = MatrixMul( a, b )

print 'v = ('
for r in v:
    print '[', 
    for val in r:
        print '%8.2f '%val, 
    print ']'
print ')'


u = MatrixMul(b,a)

print 'u = '
for r in u:
    print '[', 
    for val in r:
        print '%8.2f '%val, 
    print ']'
print ')'

```

### python_code_2.txt
```python
from operator import mul

def matrixMul(m1, m2):
  return map(
    lambda row:
      map(
        lambda *column:
          sum(map(mul, row, column)),
        *m2),
    m1)

```

### python_code_3.txt
```python
def mm(A, B):
    return [[sum(x * B[i][col] for i,x in enumerate(row)) for col in range(len(B[0]))] for row in A]

```

### python_code_4.txt
```python
import numpy as np
np.dot(a,b)
#or if a is an array
a.dot(b)

```

