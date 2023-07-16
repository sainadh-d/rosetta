# Sum of elements below main diagonal of matrix

## Task Link
[Rosetta Code - Sum of elements below main diagonal of matrix](https://rosettacode.org/wiki/Sum_of_elements_below_main_diagonal_of_matrix)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args) {
    int[][] matrix = {{1, 3, 7, 8, 10},
                      {2, 4, 16, 14, 4},
                      {3, 1, 9, 18, 11},
                      {12, 14, 17, 18, 20},
                      {7, 1, 3, 9, 5}};
    int sum = 0;
    for (int row = 1; row < matrix.length; row++) {
        for (int col = 0; col < row; col++) {
            sum += matrix[row][col];
        }
    }
    System.out.println(sum);
}

```

## Python Code
### python_code_1.txt
```python
from numpy import array, tril, sum

A = [[1,3,7,8,10],
    [2,4,16,14,4],
    [3,1,9,18,11],
    [12,14,17,18,20],
    [7,1,3,9,5]]

print(sum(tril(A, -1)))   # 69

```

### python_code_2.txt
```python
'''Lower triangle of a matrix'''

from itertools import chain, islice
from functools import reduce


# lowerTriangle :: [[a]] -> None | [[a]]
def lowerTriangle(matrix):
    '''Either None, if the matrix is not square, or
       the rows of the matrix, each containing only
       those values that form part of the lower triangle.
    '''
    def go(n_rows, xs):
        n, rows = n_rows
        return 1 + n, rows + [list(islice(xs, n))]

    return reduce(
        go,
        matrix,
        (0, [])
    )[1] if isSquare(matrix) else None


# isSquare :: [[a]] -> Bool
def isSquare(matrix):
    '''True if all rows of the matrix share
       the length of the matrix itself.
    '''
    n = len(matrix)
    return all([n == len(x) for x in matrix])


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Sum of integers in the lower triangle of a matrix.
    '''
    rows = lowerTriangle([
        [1, 3, 7, 8, 10],
        [2, 4, 16, 14, 4],
        [3, 1, 9, 18, 11],
        [12, 14, 17, 18, 20],
        [7, 1, 3, 9, 5]
    ])

    print(
        "Not a square matrix." if None is rows else (
            sum(chain(*rows))
        )
    )

# MAIN ---
if __name__ == '__main__':
    main()

```

