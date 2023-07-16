# Knight's tour

## Task Link
[Rosetta Code - Knight's tour](https://rosettacode.org/wiki/Knight%27s_tour)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class KnightsTour {
    private final static int base = 12;
    private final static int[][] moves = {{1,-2},{2,-1},{2,1},{1,2},{-1,2},
        {-2,1},{-2,-1},{-1,-2}};
    private static int[][] grid;
    private static int total;

    public static void main(String[] args) {
        grid = new int[base][base];
        total = (base - 4) * (base - 4);

        for (int r = 0; r < base; r++)
            for (int c = 0; c < base; c++)
                if (r < 2 || r > base - 3 || c < 2 || c > base - 3)
                    grid[r][c] = -1;

        int row = 2 + (int) (Math.random() * (base - 4));
        int col = 2 + (int) (Math.random() * (base - 4));

        grid[row][col] = 1;

        if (solve(row, col, 2))
            printResult();
        else System.out.println("no result");

    }

    private static boolean solve(int r, int c, int count) {
        if (count > total)
            return true;

        List<int[]> nbrs = neighbors(r, c);

        if (nbrs.isEmpty() && count != total)
            return false;

        Collections.sort(nbrs, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[2] - b[2];
            }
        });

        for (int[] nb : nbrs) {
            r = nb[0];
            c = nb[1];
            grid[r][c] = count;
            if (!orphanDetected(count, r, c) && solve(r, c, count + 1))
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
                int num = countNeighbors(r + y, c + x);
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

    private static boolean orphanDetected(int cnt, int r, int c) {
        if (cnt < total - 1) {
            List<int[]> nbrs = neighbors(r, c);
            for (int[] nb : nbrs)
                if (countNeighbors(nb[0], nb[1]) == 0)
                    return true;
        }
        return false;
    }

    private static void printResult() {
        for (int[] row : grid) {
            for (int i : row) {
                if (i == -1) continue;
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
import copy

boardsize=6
_kmoves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)) 


def chess2index(chess, boardsize=boardsize):
    'Convert Algebraic chess notation to internal index format'
    chess = chess.strip().lower()
    x = ord(chess[0]) - ord('a')
    y = boardsize - int(chess[1:])
    return (x, y)
    
def boardstring(board, boardsize=boardsize):
    r = range(boardsize)
    lines = ''
    for y in r:
        lines += '\n' + ','.join('%2i' % board[(x,y)] if board[(x,y)] else '  '
                                 for x in r)
    return lines
    
def knightmoves(board, P, boardsize=boardsize):
    Px, Py = P
    kmoves = set((Px+x, Py+y) for x,y in _kmoves)
    kmoves = set( (x,y)
                  for x,y in kmoves
                  if 0 <= x < boardsize
                     and 0 <= y < boardsize
                     and not board[(x,y)] )
    return kmoves

def accessibility(board, P, boardsize=boardsize):
    access = []
    brd = copy.deepcopy(board)
    for pos in knightmoves(board, P, boardsize=boardsize):
        brd[pos] = -1
        access.append( (len(knightmoves(brd, pos, boardsize=boardsize)), pos) )
        brd[pos] = 0
    return access
    
def knights_tour(start, boardsize=boardsize, _debug=False):
    board = {(x,y):0 for x in range(boardsize) for y in range(boardsize)}
    move = 1
    P = chess2index(start, boardsize)
    board[P] = move
    move += 1
    if _debug:
        print(boardstring(board, boardsize=boardsize))
    while move <= len(board):
        P = min(accessibility(board, P, boardsize))[1]
        board[P] = move
        move += 1
        if _debug:
            print(boardstring(board, boardsize=boardsize))
            input('\n%2i next: ' % move)
    return board

if __name__ == '__main__':
    while 1:
        boardsize = int(input('\nboardsize: '))
        if boardsize < 5:
            continue
        start = input('Start position: ')
        board = knights_tour(start, boardsize)
        print(boardstring(board, boardsize=boardsize))

```

