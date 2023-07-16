# Kronecker product based fractals

## Task Link
[Rosetta Code - Kronecker product based fractals](https://rosettacode.org/wiki/Kronecker_product_based_fractals)

## Java Code
### java_code_1.txt
```java
package kronecker;

/**
 * Uses the Kronecker product powers of two rectangular matrices
 * to generate fractals and tests it with three examples.
 */
public class ProductFractals {
  /**
   * Find the Kronecker product of the arguments.
   * @param a The first matrix to multiply.
   * @param b The second matrix to multiply.
   * @return A new matrix: the Kronecker product of the arguments.
   */
  public static int[][] product(final int[][] a, final int[][] b) {
    // Create matrix c as the matrix to fill and return.
    // The length of a matrix is its number of rows.
    final int[][] c = new int[a.length*b.length][];
    // Fill in the (empty) rows of c.
    // The length of each row is the number of columns.
    for (int ix = 0; ix < c.length; ix++) {
      final int num_cols = a[0].length*b[0].length;
      c[ix] = new int[num_cols];
    }
    // Now fill in the values: the products of each pair.
    // Go through all the elements of a.
    for (int ia = 0; ia < a.length; ia++) {
      for (int ja = 0; ja < a[ia].length; ja++) {
        // For each element of a, multiply it by all the elements of b.
        for (int ib = 0; ib < b.length; ib++) {
          for (int jb = 0; jb < b[ib].length; jb++) {
             c[b.length*ia+ib][b[ib].length*ja+jb] = a[ia][ja] * b[ib][jb];
          }
        }
      }
    }

    // Return the completed product matrix c.
    return c;
  }

  /**
   * Print an image obtained from an integer matrix, using the specified
   * characters to indicate non-zero and zero elements.
   * @param m The matrix to print.
   * @param nz The character to print for a non-zero element.
   * @param z The character to print for a zero element.
   */
  public static void show_matrix(final int[][] m, final char nz, final char z) {
    for (int im = 0; im < m.length; im++) {
      for (int jm = 0; jm < m[im].length; jm++) {
        System.out.print(m[im][jm] == 0 ? z : nz);
      }
      System.out.println();
    }
  }

  /**
   * Compute the specified Kronecker product power
   * of the matrix and return  it.
   * @param m The matrix to raise to the power.
   * @param n The power to which to raise the matrix.
   * @return A new matrix containing the resulting power.
   */
  public static int[][] power(final int[][] m, final int n) {
    // Start with m itself as the first power.
    int[][] m_pow = m;
    // Start the iteration with 1, not 0,
    // since we already have the first power.
    for (int ix = 1; ix < n; ix++) {
      m_pow = product(m, m_pow);
    }
    return m_pow;
  }

  /**
   * Run a test by computing the specified Kronecker product power
   * of the matrix and printing matrix and power.
   * @param m The base matrix raise to the power.
   * @param n The power to which to raise the matrix.
   */
  private static void test(final int[][] m, final int n) {
    System.out.println("Test matrix");
    show_matrix(m, '*', ' ');
    final int[][] m_pow = power(m, n);
    System.out.println("Matrix power " + n);
    show_matrix(m_pow, '*', ' ');
  }

  /**
   * Create the matrix for the first test and run the test.
   */
  private static void test1() {
    // Create the matrix.
    final int[][] m = {{0, 1, 0},
                       {1, 1, 1},
                       {0, 1, 0}};
    // Run the test.
    test(m, 4);
  }

  /**
   * Create the matrix for the second test and run the test.
   */
  private static void test2() {
    // Create the matrix.
    final int[][] m = {{1, 1, 1},
                       {1, 0, 1},
                       {1, 1, 1}};
    // Run the test.
    test(m, 4);
  }

  /**
   * Create the matrix for the second test and run the test.
   */
  private static void test3() {
    // Create the matrix.
    final int[][] m = {{1, 0, 1},
                       {1, 0, 1},
                       {0, 1, 0}};
    // Run the test.
    test(m, 4);
  }

  /**
   * Run the program to run the three tests.
   * @param args Command line arguments (not used).
   */
  public static void main(final String[] args) {
    // Test the product fractals.
    test1();
    test2();
    test3();
  }

}

```

## Python Code
### python_code_1.txt
```python
import os
from PIL import Image


def imgsave(path, arr):
    w, h = len(arr), len(arr[0])
    img = Image.new('1', (w, h))
    for x in range(w):
        for y in range(h):
            img.putpixel((x, y), arr[x][y])
    img.save(path)


def get_shape(mat):
    return len(mat), len(mat[0])


def kron(matrix1, matrix2):
    """
    Calculate the kronecker product of two matrices
    """
    final_list = []

    count = len(matrix2)

    for elem1 in matrix1:
        for i in range(count):
            sub_list = []
            for num1 in elem1:
                for num2 in matrix2[i]:
                    sub_list.append(num1 * num2)
            final_list.append(sub_list)

    return final_list


def kronpow(mat):
    """
    Generate an arbitrary number of kronecker powers
    """
    matrix = mat
    while True:
        yield matrix
        matrix = kron(mat, matrix)


def fractal(name, mat, order=6):
    """
    Save fractal as jpg to 'fractals/name'
    """
    path = os.path.join('fractals', name)
    os.makedirs(path, exist_ok=True)

    fgen = kronpow(mat)
    print(name)
    for i in range(order):
        p = os.path.join(path, f'{i}.jpg')
        print('Calculating n =', i, end='\t', flush=True)

        mat = next(fgen)
        imgsave(p, mat)

        x, y = get_shape(mat)
        print('Saved as', x, 'x', y, 'image', p)


test1 = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

test2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

test3 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

fractal('test1', test1)
fractal('test2', test2)
fractal('test3', test3)

```

### python_code_2.txt
```python
import os
import numpy as np
from scipy.sparse import csc_matrix, kron
from scipy.misc import imsave


def imgsave(name, arr, *args):
    imsave(name, arr.toarray(), *args)


def get_shape(mat):
    return mat.shape


def kronpow(mat):
    """
    Generate an arbitrary number of kronecker powers
    """
    matrix = mat
    while True:
        yield matrix
        matrix = kron(mat, matrix)


def fractal(name, mat, order=6):
    """
    Save fractal as jpg to 'fractals/name'
    """
    path = os.path.join('fractals', name)
    os.makedirs(path, exist_ok=True)

    fgen = kronpow(mat)
    print(name)
    for i in range(order):
        p = os.path.join(path, f'{i}.jpg')
        print('Calculating n =', i, end='\t', flush=True)

        mat = next(fgen)
        imgsave(p, mat)

        x, y = get_shape(mat)
        print('Saved as', x, 'x', y, 'image', p)


test1 = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

test2 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

test3 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

test1 = np.array(test1, dtype='int8')
test1 = csc_matrix(test1)

test2 = np.array(test2, dtype='int8')
test2 = csc_matrix(test2)

test3 = np.array(test3, dtype='int8')
test3 = csc_matrix(test3)

fractal('test1', test1)
fractal('test2', test2)
fractal('test3', test3)

```

