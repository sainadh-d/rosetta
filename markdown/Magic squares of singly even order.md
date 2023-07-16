# Magic squares of singly even order

## Task Link
[Rosetta Code - Magic squares of singly even order](https://rosettacode.org/wiki/Magic_squares_of_singly_even_order)

## Java Code
### java_code_1.txt
```java
public class MagicSquareSinglyEven {

    public static void main(String[] args) {
        int n = 6;
        for (int[] row : magicSquareSinglyEven(n)) {
            for (int x : row)
                System.out.printf("%2s ", x);
            System.out.println();
        }
        System.out.printf("\nMagic constant: %d ", (n * n + 1) * n / 2);
    }

    public static int[][] magicSquareOdd(final int n) {
        if (n < 3 || n % 2 == 0)
            throw new IllegalArgumentException("base must be odd and > 2");

        int value = 0;
        int gridSize = n * n;
        int c = n / 2, r = 0;

        int[][] result = new int[n][n];

        while (++value <= gridSize) {
            result[r][c] = value;
            if (r == 0) {
                if (c == n - 1) {
                    r++;
                } else {
                    r = n - 1;
                    c++;
                }
            } else if (c == n - 1) {
                r--;
                c = 0;
            } else if (result[r - 1][c + 1] == 0) {
                r--;
                c++;
            } else {
                r++;
            }
        }
        return result;
    }

    static int[][] magicSquareSinglyEven(final int n) {
        if (n < 6 || (n - 2) % 4 != 0)
            throw new IllegalArgumentException("base must be a positive "
                    + "multiple of 4 plus 2");

        int size = n * n;
        int halfN = n / 2;
        int subSquareSize = size / 4;

        int[][] subSquare = magicSquareOdd(halfN);
        int[] quadrantFactors = {0, 2, 3, 1};
        int[][] result = new int[n][n];

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int quadrant = (r / halfN) * 2 + (c / halfN);
                result[r][c] = subSquare[r % halfN][c % halfN];
                result[r][c] += quadrantFactors[quadrant] * subSquareSize;
            }
        }

        int nColsLeft = halfN / 2;
        int nColsRight = nColsLeft - 1;

        for (int r = 0; r < halfN; r++)
            for (int c = 0; c < n; c++) {
                if (c < nColsLeft || c >= n - nColsRight
                        || (c == nColsLeft && r == nColsLeft)) {

                    if (c == 0 && r == nColsLeft)
                        continue;

                    int tmp = result[r][c];
                    result[r][c] = result[r + halfN][c];
                    result[r + halfN][c] = tmp;
                }
            }

        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
import math
from sys import stdout

LOG_10 = 2.302585092994


# build odd magic square
def build_oms(s):
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1

    return q, s


# build singly even magic square
def build_sems(s):
    if s % 2 == 1:
        s += 1
    while s % 4 == 0:
        s += 2

    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = build_oms(z)

    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d

    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t

    return q, s


def format_sqr(s, l):
    for i in range(0, l - len(s)):
        s = "0" + s
    return s + " "


def display(q):
    s = q[1]
    print(" - {0} x {1}\n".format(s, s))
    k = 1 + math.floor(math.log(s * s) / LOG_10)
    for j in range(0, s):
        for i in range(0, s):
            stdout.write(format_sqr("{0}".format(q[0][i][j]), k))
        print()
    print("Magic sum: {0}\n".format(s * ((s * s) + 1) // 2))


stdout.write("Singly Even Magic Square")
display(build_sems(6))

```

