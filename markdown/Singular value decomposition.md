# Singular value decomposition

## Task Link
[Rosetta Code - Singular value decomposition](https://rosettacode.org/wiki/Singular_value_decomposition)

## Java Code
### java_code_1.txt
```java
import Jama.Matrix;
public class SingularValueDecomposition {
    public static void main(String[] args) {
        double[][] matrixArray = {{3, 0}, {4, 5}};
        var matrix = new Matrix(matrixArray);
        var svd = matrix.svd();
        svd.getU().print(0, 10); // The number of digits after the decimal is 10.
        svd.getS().print(0, 10);
        svd.getV().print(0, 10);
    }
}

```

## Python Code
### python_code_1.txt
```python
from numpy import *
A = matrix([[3, 0], [4, 5]])
U, Sigma, VT = linalg.svd(A)
print(U)
print(Sigma)
print(VT)

```

