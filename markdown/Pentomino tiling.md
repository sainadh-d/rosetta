# Pentomino tiling

## Task Link
[Rosetta Code - Pentomino tiling](https://rosettacode.org/wiki/Pentomino_tiling)

## Java Code
### java_code_1.txt
```java
package pentominotiling;

import java.util.*;

public class PentominoTiling {

    static final char[] symbols = "FILNPTUVWXYZ-".toCharArray();
    static final Random rand = new Random();

    static final int nRows = 8;
    static final int nCols = 8;
    static final int blank = 12;

    static int[][] grid = new int[nRows][nCols];
    static boolean[] placed = new boolean[symbols.length - 1];

    public static void main(String[] args) {
        shuffleShapes();

        for (int r = 0; r < nRows; r++)
            Arrays.fill(grid[r], -1);

        for (int i = 0; i < 4; i++) {
            int randRow, randCol;
            do {
                randRow = rand.nextInt(nRows);
                randCol = rand.nextInt(nCols);
            } while (grid[randRow][randCol] == blank);
            grid[randRow][randCol] = blank;
        }

        if (solve(0, 0)) {
            printResult();
        } else {
            System.out.println("no solution");
        }
    }

    static void shuffleShapes() {
        int n = shapes.length;
        while (n > 1) {
            int r = rand.nextInt(n--);

            int[][] tmp = shapes[r];
            shapes[r] = shapes[n];
            shapes[n] = tmp;

            char tmpSymbol = symbols[r];
            symbols[r] = symbols[n];
            symbols[n] = tmpSymbol;
        }
    }

    static void printResult() {
        for (int[] r : grid) {
            for (int i : r)
                System.out.printf("%c ", symbols[i]);
            System.out.println();
        }
    }

    static boolean tryPlaceOrientation(int[] o, int r, int c, int shapeIndex) {

        for (int i = 0; i < o.length; i += 2) {
            int x = c + o[i + 1];
            int y = r + o[i];
            if (x < 0 || x >= nCols || y < 0 || y >= nRows || grid[y][x] != -1)
                return false;
        }

        grid[r][c] = shapeIndex;
        for (int i = 0; i < o.length; i += 2)
            grid[r + o[i]][c + o[i + 1]] = shapeIndex;

        return true;
    }

    static void removeOrientation(int[] o, int r, int c) {
        grid[r][c] = -1;
        for (int i = 0; i < o.length; i += 2)
            grid[r + o[i]][c + o[i + 1]] = -1;
    }

    static boolean solve(int pos, int numPlaced) {
        if (numPlaced == shapes.length)
            return true;

        int row = pos / nCols;
        int col = pos % nCols;

        if (grid[row][col] != -1)
            return solve(pos + 1, numPlaced);

        for (int i = 0; i < shapes.length; i++) {
            if (!placed[i]) {
                for (int[] orientation : shapes[i]) {

                    if (!tryPlaceOrientation(orientation, row, col, i))
                        continue;

                    placed[i] = true;

                    if (solve(pos + 1, numPlaced + 1))
                        return true;

                    removeOrientation(orientation, row, col);
                    placed[i] = false;
                }
            }
        }
        return false;
    }

    static final int[][] F = {{1, -1, 1, 0, 1, 1, 2, 1}, {0, 1, 1, -1, 1, 0, 2, 0},
    {1, 0, 1, 1, 1, 2, 2, 1}, {1, 0, 1, 1, 2, -1, 2, 0}, {1, -2, 1, -1, 1, 0, 2, -1},
    {0, 1, 1, 1, 1, 2, 2, 1}, {1, -1, 1, 0, 1, 1, 2, -1}, {1, -1, 1, 0, 2, 0, 2, 1}};

    static final int[][] I = {{0, 1, 0, 2, 0, 3, 0, 4}, {1, 0, 2, 0, 3, 0, 4, 0}};

    static final int[][] L = {{1, 0, 1, 1, 1, 2, 1, 3}, {1, 0, 2, 0, 3, -1, 3, 0},
    {0, 1, 0, 2, 0, 3, 1, 3}, {0, 1, 1, 0, 2, 0, 3, 0}, {0, 1, 1, 1, 2, 1, 3, 1},
    {0, 1, 0, 2, 0, 3, 1, 0}, {1, 0, 2, 0, 3, 0, 3, 1}, {1, -3, 1, -2, 1, -1, 1, 0}};

    static final int[][] N = {{0, 1, 1, -2, 1, -1, 1, 0}, {1, 0, 1, 1, 2, 1, 3, 1},
    {0, 1, 0, 2, 1, -1, 1, 0}, {1, 0, 2, 0, 2, 1, 3, 1}, {0, 1, 1, 1, 1, 2, 1, 3},
    {1, 0, 2, -1, 2, 0, 3, -1}, {0, 1, 0, 2, 1, 2, 1, 3}, {1, -1, 1, 0, 2, -1, 3, -1}};

    static final int[][] P = {{0, 1, 1, 0, 1, 1, 2, 1}, {0, 1, 0, 2, 1, 0, 1, 1},
    {1, 0, 1, 1, 2, 0, 2, 1}, {0, 1, 1, -1, 1, 0, 1, 1}, {0, 1, 1, 0, 1, 1, 1, 2},
    {1, -1, 1, 0, 2, -1, 2, 0}, {0, 1, 0, 2, 1, 1, 1, 2}, {0, 1, 1, 0, 1, 1, 2, 0}};

    static final int[][] T = {{0, 1, 0, 2, 1, 1, 2, 1}, {1, -2, 1, -1, 1, 0, 2, 0},
    {1, 0, 2, -1, 2, 0, 2, 1}, {1, 0, 1, 1, 1, 2, 2, 0}};

    static final int[][] U = {{0, 1, 0, 2, 1, 0, 1, 2}, {0, 1, 1, 1, 2, 0, 2, 1},
    {0, 2, 1, 0, 1, 1, 1, 2}, {0, 1, 1, 0, 2, 0, 2, 1}};

    static final int[][] V = {{1, 0, 2, 0, 2, 1, 2, 2}, {0, 1, 0, 2, 1, 0, 2, 0},
    {1, 0, 2, -2, 2, -1, 2, 0}, {0, 1, 0, 2, 1, 2, 2, 2}};

    static final int[][] W = {{1, 0, 1, 1, 2, 1, 2, 2}, {1, -1, 1, 0, 2, -2, 2, -1},
    {0, 1, 1, 1, 1, 2, 2, 2}, {0, 1, 1, -1, 1, 0, 2, -1}};

    static final int[][] X = {{1, -1, 1, 0, 1, 1, 2, 0}};

    static final int[][] Y = {{1, -2, 1, -1, 1, 0, 1, 1}, {1, -1, 1, 0, 2, 0, 3, 0},
    {0, 1, 0, 2, 0, 3, 1, 1}, {1, 0, 2, 0, 2, 1, 3, 0}, {0, 1, 0, 2, 0, 3, 1, 2},
    {1, 0, 1, 1, 2, 0, 3, 0}, {1, -1, 1, 0, 1, 1, 1, 2}, {1, 0, 2, -1, 2, 0, 3, 0}};

    static final int[][] Z = {{0, 1, 1, 0, 2, -1, 2, 0}, {1, 0, 1, 1, 1, 2, 2, 2},
    {0, 1, 1, 1, 2, 1, 2, 2}, {1, -2, 1, -1, 1, 0, 2, -2}};

    static final int[][][] shapes = {F, I, L, N, P, T, U, V, W, X, Y, Z};
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product

minos = (((197123, 7, 6), (1797, 6, 7), (1287, 6, 7), (196867, 7, 6)),
        ((263937, 6, 6), (197126, 6, 6), (393731, 6, 6), (67332, 6, 6)),
        ((16843011, 7, 5), (2063, 5, 7), (3841, 5, 7), (271, 5, 7), (3848, 5, 7), (50463234, 7, 5), (50397441, 7, 5), (33686019, 7, 5)),
        ((131843, 7, 6), (1798, 6, 7), (775, 6, 7), (1795, 6, 7), (1543, 6, 7), (197377, 7, 6), (197378, 7, 6), (66307, 7, 6)),
        ((132865, 6, 6), (131846, 6, 6), (198146, 6, 6), (132611, 6, 6), (393986, 6, 6), (263938, 6, 6), (67330, 6, 6), (132868, 6, 6)),
        ((1039, 5, 7), (33751554, 7, 5), (16843521, 7, 5), (16974081, 7, 5), (33686274, 7, 5), (3842, 5, 7), (3844, 5, 7), (527, 5, 7)),
        ((1804, 5, 7), (33751297, 7, 5), (33686273, 7, 5), (16974338, 7, 5), (16843522, 7, 5), (782, 5, 7), (3079, 5, 7), (3587, 5, 7)),
        ((263683, 6, 6), (198148, 6, 6), (66310, 6, 6), (393985, 6, 6)),
        ((67329, 6, 6), (131591, 6, 6), (459266, 6, 6), (263940, 6, 6)),
        ((459780, 6, 6), (459009, 6, 6), (263175, 6, 6), (65799, 6, 6)),
        ((4311810305, 8, 4), (31, 4, 8)),
        ((132866, 6, 6),))

boxchar_double_width = ' ╶╺╵└┕╹┖┗╴─╼┘┴┶┚┸┺╸╾━┙┵┷┛┹┻╷┌┍│├┝╿┞┡┐┬┮┤┼┾┦╀╄┑┭┯┥┽┿┩╃╇╻┎┏╽┟┢┃┠┣┒┰┲┧╁╆┨╂╊┓┱┳┪╅╈┫╉╋'
boxchar_single_width = [c + ' ─━'[i%3] for i, c in enumerate(boxchar_double_width)]

# choose drawing alphabet based on terminal font
patterns = boxchar_single_width

tiles = []
for row in reversed(minos):
    tiles.append([])
    for n, x, y in row:
        for shift in (b*8 + a for a, b in product(range(x), range(y))):
            tiles[-1].append(n << shift)

def img(seq):
    b = [[0]*10 for _ in range(10)]

    for i, s in enumerate(seq):
        for j, k in product(range(8), range(8)):
            if s & (1<<(j*8 + k)):
                b[j + 1][k + 1] = i + 1

    idices = [[0]*9 for _ in range(9)]
    for i, j in product(range(9), range(9)):
        n = (b[i+1][j+1], b[i][j+1], b[i][j], b[i+1][j], b[i+1][j+1])
        idices[i][j] = sum((a != b)*(1 + (not a or not b))*3**i for i, (a,b) in enumerate(zip(n, n[1:])))

    return '\n'.join(''.join(patterns[i] for i in row) for row in idices)

def tile(board=0, seq=tuple(), tiles=tiles):
    if not tiles:
        yield img(seq)
        return

    for c in tiles[0]:
        b = board | c

        tnext = [] # not using list comprehension ...
        for t in tiles[1:]:
            tnext.append(tuple(n for n in t if not n&b))
            if not tnext[-1]: break # because early break is faster
        else:
            yield from tile(b, seq + (c,), tnext)

for x in tile():
    print(x)

```

