# Solve a Numbrix puzzle

## Task Link
[Rosetta Code - Solve a Numbrix puzzle](https://rosettacode.org/wiki/Solve_a_Numbrix_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Numbrix {

    final static String[] board = {
        "00,00,00,00,00,00,00,00,00",
        "00,00,46,45,00,55,74,00,00",
        "00,38,00,00,43,00,00,78,00",
        "00,35,00,00,00,00,00,71,00",
        "00,00,33,00,00,00,59,00,00",
        "00,17,00,00,00,00,00,67,00",
        "00,18,00,00,11,00,00,64,00",
        "00,00,24,21,00,01,02,00,00",
        "00,00,00,00,00,00,00,00,00"};

    final static int[][] moves = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    static int[][] grid;
    static int[] clues;
    static int totalToFill;

    public static void main(String[] args) {
        int nRows = board.length + 2;
        int nCols = board[0].split(",").length + 2;
        int startRow = 0, startCol = 0;

        grid = new int[nRows][nCols];
        totalToFill = (nRows - 2) * (nCols - 2);
        List<Integer> lst = new ArrayList<>();

        for (int r = 0; r < nRows; r++) {
            Arrays.fill(grid[r], -1);

            if (r >= 1 && r < nRows - 1) {

                String[] row = board[r - 1].split(",");

                for (int c = 1; c < nCols - 1; c++) {
                    int val = Integer.parseInt(row[c - 1]);
                    if (val > 0)
                        lst.add(val);
                    if (val == 1) {
                        startRow = r;
                        startCol = c;
                    }
                    grid[r][c] = val;
                }
            }
        }

        clues = lst.stream().sorted().mapToInt(i -> i).toArray();

        if (solve(startRow, startCol, 1, 0))
            printResult();
    }

    static boolean solve(int r, int c, int count, int nextClue) {
        if (count > totalToFill)
            return true;

        if (grid[r][c] != 0 && grid[r][c] != count)
            return false;

        if (grid[r][c] == 0 && nextClue < clues.length)
            if (clues[nextClue] == count)
                return false;

        int back = grid[r][c];
        if (back == count)
            nextClue++;

        grid[r][c] = count;
        for (int[] move : moves)
            if (solve(r + move[1], c + move[0], count + 1, nextClue))
                return true;

        grid[r][c] = back;
        return false;
    }

    static void printResult() {
        for (int[] row : grid) {
            for (int i : row) {
                if (i == -1)
                    continue;
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
neighbours = [[-1, 0], [0, -1], [1, 0], [0, 1]]
exists = []
lastNumber = 0
wid = 0
hei = 0


def find_next(pa, x, y, z):
    for i in range(4):
        a = x + neighbours[i][0]
        b = y + neighbours[i][1]
        if wid > a > -1 and hei > b > -1:
            if pa[a][b] == z:
                return a, b

    return -1, -1


def find_solution(pa, x, y, z):
    if z > lastNumber:
        return 1
    if exists[z] == 1:
        s = find_next(pa, x, y, z)
        if s[0] < 0:
            return 0
        return find_solution(pa, s[0], s[1], z + 1)

    for i in range(4):
        a = x + neighbours[i][0]
        b = y + neighbours[i][1]
        if wid > a > -1 and hei > b > -1:
            if pa[a][b] == 0:
                pa[a][b] = z
                r = find_solution(pa, a, b, z + 1)
                if r == 1:
                    return 1
                pa[a][b] = 0

    return 0


def solve(pz, w, h):
    global lastNumber, wid, hei, exists

    lastNumber = w * h
    wid = w
    hei = h
    exists = [0 for j in range(lastNumber + 1)]

    pa = [[0 for j in range(h)] for i in range(w)]
    st = pz.split()
    idx = 0
    for j in range(h):
        for i in range(w):
            if st[idx] == ".":
                idx += 1
            else:
                pa[i][j] = int(st[idx])
                exists[pa[i][j]] = 1
                idx += 1

    x = 0
    y = 0
    t = w * h + 1
    for j in range(h):
        for i in range(w):
            if pa[i][j] != 0 and pa[i][j] < t:
                t = pa[i][j]
                x = i
                y = j

    return find_solution(pa, x, y, t + 1), pa


def show_result(r):
    if r[0] == 1:
        for j in range(hei):
            for i in range(wid):
                stdout.write(" {:0{}d}".format(r[1][i][j], 2))
            print()
    else:
        stdout.write("No Solution!\n")

    print()


r = solve(". . . . . . . . . . . 46 45 . 55 74 . . . 38 . . 43 . . 78 . . 35 . . . . . 71 . . . 33 . . . 59 . . . 17"
          " . . . . . 67 . . 18 . . 11 . . 64 . . . 24 21 . 1  2 . . . . . . . . . . .", 9, 9)
show_result(r)

r = solve(". . . . . . . . . . 11 12 15 18 21 62 61 . .  6 . . . . . 60 . . 33 . . . . . 57 . . 32 . . . . . 56 . . 37"
          " .  1 . . . 73 . . 38 . . . . . 72 . . 43 44 47 48 51 76 77 . . . . . . . . . .", 9, 9)
show_result(r)

r = solve("17 . . . 11 . . . 59 . 15 . . 6 . . 61 . . . 3 . . .  63 . . . . . . 66 . . . . 23 24 . 68 67 78 . 54 55"
          " . . . . 72 . . . . . . 35 . . . 49 . . . 29 . . 40 . . 47 . 31 . . . 39 . . . 45", 9, 9)
show_result(r)

```

