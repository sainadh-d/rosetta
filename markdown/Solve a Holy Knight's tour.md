# Solve a Holy Knight's tour

## Task Link
[Rosetta Code - Solve a Holy Knight's tour](https://rosettacode.org/wiki/Solve_a_Holy_Knight%27s_tour)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class HolyKnightsTour {

    final static String[] board = {
        " xxx    ",
        " x xx   ",
        " xxxxxxx",
        "xxx  x x",
        "x x  xxx",
        "1xxxxxx ",
        "  xx x  ",
        "   xxx  "};

    private final static int base = 12;
    private final static int[][] moves = {{1, -2}, {2, -1}, {2, 1}, {1, 2},
    {-1, 2}, {-2, 1}, {-2, -1}, {-1, -2}};
    private static int[][] grid;
    private static int total = 2;

    public static void main(String[] args) {
        int row = 0, col = 0;

        grid = new int[base][base];

        for (int r = 0; r < base; r++) {
            Arrays.fill(grid[r], -1);
            for (int c = 2; c < base - 2; c++) {
                if (r >= 2 && r < base - 2) {
                    if (board[r - 2].charAt(c - 2) == 'x') {
                        grid[r][c] = 0;
                        total++;
                    }
                    if (board[r - 2].charAt(c - 2) == '1') {
                        row = r;
                        col = c;
                    }
                }
            }
        }

        grid[row][col] = 1;

        if (solve(row, col, 2))
            printResult();
    }

    private static boolean solve(int r, int c, int count) {
        if (count == total)
            return true;

        List<int[]> nbrs = neighbors(r, c);

        if (nbrs.isEmpty() && count != total)
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

    private static List<int[]> neighbors(int r, int c) {
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

    private static int countNeighbors(int r, int c) {
        int num = 0;
        for (int[] m : moves)
            if (grid[r + m[1]][c + m[0]] == 0)
                num++;
        return num;
    }

    private static void printResult() {
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
moves = [
    [-1, -2], [1, -2], [-1, 2], [1, 2],
    [-2, -1], [-2, 1], [2, -1], [2, 1]
]


def solve(pz, sz, sx, sy, idx, cnt):
    if idx > cnt:
        return 1

    for i in range(len(moves)):
        x = sx + moves[i][0]
        y = sy + moves[i][1]
        if sz > x > -1 and sz > y > -1 and pz[x][y] == 0:
            pz[x][y] = idx
            if 1 == solve(pz, sz, x, y, idx + 1, cnt):
                return 1
            pz[x][y] = 0

    return 0


def find_solution(pz, sz):
    p = [[-1 for j in range(sz)] for i in range(sz)]
    idx = x = y = cnt = 0
    for j in range(sz):
        for i in range(sz):
            if pz[idx] == "x":
                p[i][j] = 0
                cnt += 1
            elif pz[idx] == "s":
                p[i][j] = 1
                cnt += 1
                x = i
                y = j
            idx += 1

    if 1 == solve(p, sz, x, y, 2, cnt):
        for j in range(sz):
            for i in range(sz):
                if p[i][j] != -1:
                    stdout.write(" {:0{}d}".format(p[i][j], 2))
                else:
                    stdout.write("   ")
            print()
    else:
        print("Cannot solve this puzzle!")


# entry point
find_solution(".xxx.....x.xx....xxxxxxxxxx..x.xx.x..xxxsxxxxxx...xx.x.....xxx..", 8)
print()
find_solution(".....s.x..........x.x.........xxxxx.........xxx.......x..x.x..x..xxxxx...xxxxx..xx.....xx..xxxxx...xxxxx..x..x.x..x.......xxx.........xxxxx.........x.x..........x.x.....", 13)

```

