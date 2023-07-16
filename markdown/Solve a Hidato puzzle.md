# Solve a Hidato puzzle

## Task Link
[Rosetta Code - Solve a Hidato puzzle](https://rosettacode.org/wiki/Solve_a_Hidato_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Hidato {

    private static int[][] board;
    private static int[] given, start;

    public static void main(String[] args) {
        String[] input = {"_ 33 35 _ _ . . .",
            "_ _ 24 22 _ . . .",
            "_ _ _ 21 _ _ . .",
            "_ 26 _ 13 40 11 . .",
            "27 _ _ _ 9 _ 1 .",
            ". . _ _ 18 _ _ .",
            ". . . . _ 7 _ _",
            ". . . . . . 5 _"};

        setup(input);
        printBoard();
        System.out.println("\nFound:");
        solve(start[0], start[1], 1, 0);
        printBoard();
    }

    private static void setup(String[] input) {
        /* This task is not about input validation, so
           we're going to trust the input to be valid */

        String[][] puzzle = new String[input.length][];
        for (int i = 0; i < input.length; i++)
            puzzle[i] = input[i].split(" ");

        int nCols = puzzle[0].length;
        int nRows = puzzle.length;

        List<Integer> list = new ArrayList<>(nRows * nCols);

        board = new int[nRows + 2][nCols + 2];
        for (int[] row : board)
            for (int c = 0; c < nCols + 2; c++)
                row[c] = -1;

        for (int r = 0; r < nRows; r++) {
            String[] row = puzzle[r];
            for (int c = 0; c < nCols; c++) {
                String cell = row[c];
                switch (cell) {
                    case "_":
                        board[r + 1][c + 1] = 0;
                        break;
                    case ".":
                        break;
                    default:
                        int val = Integer.parseInt(cell);
                        board[r + 1][c + 1] = val;
                        list.add(val);
                        if (val == 1)
                            start = new int[]{r + 1, c + 1};
                }
            }
        }
        Collections.sort(list);
        given = new int[list.size()];
        for (int i = 0; i < given.length; i++)
            given[i] = list.get(i);
    }

    private static boolean solve(int r, int c, int n, int next) {
        if (n > given[given.length - 1])
            return true;

        if (board[r][c] != 0 && board[r][c] != n)
            return false;

        if (board[r][c] == 0 && given[next] == n)
            return false;

        int back = board[r][c];
        if (back == n)
            next++;

        board[r][c] = n;
        for (int i = -1; i < 2; i++)
            for (int j = -1; j < 2; j++)
                if (solve(r + i, c + j, n + 1, next))
                    return true;

        board[r][c] = back;
        return false;
    }

    private static void printBoard() {
        for (int[] row : board) {
            for (int c : row) {
                if (c == -1)
                    System.out.print(" . ");
                else
                    System.out.printf(c > 0 ? "%2d " : "__ ", c);
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
board = []
given = []
start = None

def setup(s):
    global board, given, start
    lines = s.splitlines()
    ncols = len(lines[0].split())
    nrows = len(lines)
    board = [[-1] * (ncols + 2) for _ in xrange(nrows + 2)]

    for r, row in enumerate(lines):
        for c, cell in enumerate(row.split()):
            if cell == "__" :
                board[r + 1][c + 1] = 0
                continue
            elif cell == ".":
                continue # -1
            else:
                val = int(cell)
                board[r + 1][c + 1] = val
                given.append(val)
                if val == 1:
                    start = (r + 1, c + 1)
    given.sort()

def solve(r, c, n, next=0):
    if n > given[-1]:
        return True
    if board[r][c] and board[r][c] != n:
        return False
    if board[r][c] == 0 and given[next] == n:
        return False

    back = 0
    if board[r][c] == n:
        next += 1
        back = n

    board[r][c] = n
    for i in xrange(-1, 2):
        for j in xrange(-1, 2):
            if solve(r + i, c + j, n + 1, next):
                return True
    board[r][c] = back
    return False

def print_board():
    d = {-1: "  ", 0: "__"}
    bmax = max(max(r) for r in board)
    form = "%" + str(len(str(bmax)) + 1) + "s"
    for r in board[1:-1]:
        print "".join(form % d.get(c, str(c)) for c in r[1:-1])

hi = """\
__ 33 35 __ __  .  .  .
__ __ 24 22 __  .  .  .
__ __ __ 21 __ __  .  .
__ 26 __ 13 40 11  .  .
27 __ __ __  9 __  1  .
 .  . __ __ 18 __ __  .
 .  .  .  . __  7 __ __
 .  .  .  .  .  .  5 __"""

setup(hi)
print_board()
solve(start[0], start[1], 1)
print
print_board()

```

