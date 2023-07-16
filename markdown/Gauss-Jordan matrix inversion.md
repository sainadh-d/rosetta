# Gauss-Jordan matrix inversion

## Task Link
[Rosetta Code - Gauss-Jordan matrix inversion](https://rosettacode.org/wiki/Gauss-Jordan_matrix_inversion)

## Java Code
### java_code_1.txt
```java
// GaussJordan.java

import java.util.Random;

public class GaussJordan {
    public static void main(String[] args) {
        int rows = 5;
        Matrix m = new Matrix(rows, rows);
        Random r = new Random();
        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < rows; ++column)
                m.set(row, column, r.nextDouble());
        }
        System.out.println("Matrix:");
        m.print();
        System.out.println("Inverse:");
        Matrix inv = m.inverse();
        inv.print();
        System.out.println("Product of matrix and inverse:");
        Matrix.product(m, inv).print();
    }
}

```

### java_code_2.txt
```java
// Matrix.java

public class Matrix {
    private int rows;
    private int columns;
    private double[][] elements;

    public Matrix(int rows, int columns) {
        this.rows = rows;
        this.columns = columns;
        elements = new double[rows][columns];
    }

    public void set(int row, int column, double value) {
        elements[row][column] = value;
    }

    public double get(int row, int column) {
        return elements[row][column];
    }

    public void print() {
        for (int row = 0; row < rows; ++row) {
            for (int column = 0; column < columns; ++column) {
                if (column > 0)
                    System.out.print(' ');
                System.out.printf("%7.3f", elements[row][column]);
            }
            System.out.println();
        }
    }

    // Returns the inverse of this matrix
    public Matrix inverse() {
        assert(rows == columns);
        // Augment by identity matrix
        Matrix tmp = new Matrix(rows, columns * 2);
        for (int row = 0; row < rows; ++row) {
            System.arraycopy(elements[row], 0, tmp.elements[row], 0, columns);
            tmp.elements[row][row + columns] = 1;
        }
        tmp.toReducedRowEchelonForm();
        Matrix inv = new Matrix(rows, columns);
        for (int row = 0; row < rows; ++row)
            System.arraycopy(tmp.elements[row], columns, inv.elements[row], 0, columns);
        return inv;
    }

    // Converts this matrix into reduced row echelon form
    public void toReducedRowEchelonForm() {
        for (int row = 0, lead = 0; row < rows && lead < columns; ++row, ++lead) {
            int i = row;
            while (elements[i][lead] == 0) {
                if (++i == rows) {
                    i = row;
                    if (++lead == columns)
                        return;
                }
            }
            swapRows(i, row);
            if (elements[row][lead] != 0) {
                double f = elements[row][lead];
                for (int column = 0; column < columns; ++column)
                    elements[row][column] /= f;
            }
            for (int j = 0; j < rows; ++j) {
                if (j == row)
                    continue;
                double f = elements[j][lead];
                for (int column = 0; column < columns; ++column)
                    elements[j][column] -= f * elements[row][column];
            }
        }
    }

    // Returns the matrix product of a and b
    public static Matrix product(Matrix a, Matrix b) {
        assert(a.columns == b.rows);
        Matrix result = new Matrix(a.rows, b.columns);
        for (int i = 0; i < a.rows; ++i) {
            double[] resultRow = result.elements[i];
            double[] aRow = a.elements[i];
            for (int j = 0; j < a.columns; ++j) {
                double[] bRow = b.elements[j];
                for (int k = 0; k < b.columns; ++k)
                    resultRow[k] += aRow[j] * bRow[k];
            }
        }
        return result;
    }

    private void swapRows(int i, int j) {
        double[] tmp = elements[i];
        elements[i] = elements[j];
        elements[j] = tmp;
    }
}

```

## Python Code
### python_code_1.txt
```python
import numpy as np
from numpy.linalg import inv
a = np.array([[1., 2., 3.], [4., 1., 6.],[ 7., 8., 9.]])
ainv = inv(a)

print(a)
print(ainv)

```

