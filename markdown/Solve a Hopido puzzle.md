# Solve a Hopido puzzle

## Task Link
[Rosetta Code - Solve a Hopido puzzle](https://rosettacode.org/wiki/Solve_a_Hopido_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Hopido {

    final static String[] board = {
        ".00.00.",
        "0000000",
        "0000000",
        ".00000.",
        "..000..",
        "...0..."};

    final static int[][] moves = {{-3, 0}, {0, 3}, {3, 0}, {0, -3},
    {2, 2}, {2, -2}, {-2, 2}, {-2, -2}};
    static int[][] grid;
    static int totalToFill;

    public static void main(String[] args) {
        int nRows = board.length + 6;
        int nCols = board[0].length() + 6;

        grid = new int[nRows][nCols];

        for (int r = 0; r < nRows; r++) {
            Arrays.fill(grid[r], -1);
            for (int c = 3; c < nCols - 3; c++)
                if (r >= 3 && r < nRows - 3) {
                    if (board[r - 3].charAt(c - 3) == '0') {
                        grid[r][c] = 0;
                        totalToFill++;
                    }
                }
        }

        int pos = -1, r, c;
        do {
            do {
                pos++;
                r = pos / nCols;
                c = pos % nCols;
            } while (grid[r][c] == -1);

            grid[r][c] = 1;
            if (solve(r, c, 2))
                break;
            grid[r][c] = 0;

        } while (pos < nRows * nCols);

        printResult();
    }

    static boolean solve(int r, int c, int count) {
        if (count > totalToFill)
            return true;

        List<int[]> nbrs = neighbors(r, c);

        if (nbrs.isEmpty() && count != totalToFill)
            return false;

        Collections.sort(nbrs, (a, b) -> a[2] - b[2]);

        for (int[] nb : nbrs) {
            r = nb[0];
            c = nb[1];
            grid[r][c] = count;
            if (solve(r, c, count + 1))
                return true;
            grid[r][c] = 0;
        }

        return false;
    }

    static List<int[]> neighbors(int r, int c) {
        List<int[]> nbrs = new ArrayList<>();

        for (int[] m : moves) {
            int x = m[0];
            int y = m[1];
            if (grid[r + y][c + x] == 0) {
                int num = countNeighbors(r + y, c + x) - 1;
                nbrs.add(new int[]{r + y, c + x, num});
            }
        }
        return nbrs;
    }

    static int countNeighbors(int r, int c) {
        int num = 0;
        for (int[] m : moves)
            if (grid[r + m[1]][c + m[0]] == 0)
                num++;
        return num;
    }

    static void printResult() {
        for (int[] row : grid) {
            for (int i : row) {
                if (i == -1)
                    System.out.printf("%2s ", ' ');
                else
                    System.out.printf("%2d ", i);
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from sys import stdout

neighbours = [[2, 2], [-2, 2], [2, -2], [-2, -2], [3, 0], [0, 3], [-3, 0], [0, -3]]
cnt = 0
pWid = 0
pHei = 0


def is_valid(a, b):
    return -1 < a < pWid and -1 < b < pHei


def iterate(pa, x, y, v):
    if v > cnt:
        return 1

    for i in range(len(neighbours)):
        a = x + neighbours[i][0]
        b = y + neighbours[i][1]
        if is_valid(a, b) and pa[a][b] == 0:
            pa[a][b] = v
            r = iterate(pa, a, b, v + 1)
            if r == 1:
                return r
            pa[a][b] = 0
    return 0


def solve(pz, w, h):
    global cnt, pWid, pHei

    pa = [[-1 for j in range(h)] for i in range(w)]
    f = 0
    pWid = w
    pHei = h
    for j in range(h):
        for i in range(w):
            if pz[f] == "1":
                pa[i][j] = 0
                cnt += 1
            f += 1

    for y in range(h):
        for x in range(w):
            if pa[x][y] == 0:
                pa[x][y] = 1
                if 1 == iterate(pa, x, y, 2):
                    return 1, pa
                pa[x][y] = 0

    return 0, pa

r = solve("011011011111111111111011111000111000001000", 7, 6)
if r[0] == 1:
    for j in range(6):
        for i in range(7):
            if r[1][i][j] == -1:
                stdout.write("   ")
            else:
                stdout.write(" {:0{}d}".format(r[1][i][j], 2))
        print()
else:
    stdout.write("No solution!")

```

