# Sokoban

## Task Link
[Rosetta Code - Sokoban](https://rosettacode.org/wiki/Sokoban)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Sokoban {
    String destBoard, currBoard;
    int playerX, playerY, nCols;

    Sokoban(String[] board) {
        nCols = board[0].length();
        StringBuilder destBuf = new StringBuilder();
        StringBuilder currBuf = new StringBuilder();

        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < nCols; c++) {

                char ch = board[r].charAt(c);

                destBuf.append(ch != '$' && ch != '@' ? ch : ' ');
                currBuf.append(ch != '.' ? ch : ' ');

                if (ch == '@') {
                    this.playerX = c;
                    this.playerY = r;
                }
            }
        }
        destBoard = destBuf.toString();
        currBoard = currBuf.toString();
    }

    String move(int x, int y, int dx, int dy, String trialBoard) {

        int newPlayerPos = (y + dy) * nCols + x + dx;

        if (trialBoard.charAt(newPlayerPos) != ' ')
            return null;

        char[] trial = trialBoard.toCharArray();
        trial[y * nCols + x] = ' ';
        trial[newPlayerPos] = '@';

        return new String(trial);
    }

    String push(int x, int y, int dx, int dy, String trialBoard) {

        int newBoxPos = (y + 2 * dy) * nCols + x + 2 * dx;

        if (trialBoard.charAt(newBoxPos) != ' ')
            return null;

        char[] trial = trialBoard.toCharArray();
        trial[y * nCols + x] = ' ';
        trial[(y + dy) * nCols + x + dx] = '@';
        trial[newBoxPos] = '$';

        return new String(trial);
    }

    boolean isSolved(String trialBoard) {
        for (int i = 0; i < trialBoard.length(); i++)
            if ((destBoard.charAt(i) == '.')
                    != (trialBoard.charAt(i) == '$'))
                return false;
        return true;
    }

    String solve() {
        class Board {
            String cur, sol;
            int x, y;

            Board(String s1, String s2, int px, int py) {
                cur = s1;
                sol = s2;
                x = px;
                y = py;
            }
        }
        char[][] dirLabels = {{'u', 'U'}, {'r', 'R'}, {'d', 'D'}, {'l', 'L'}};
        int[][] dirs = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};

        Set<String> history = new HashSet<>();
        LinkedList<Board> open = new LinkedList<>();

        history.add(currBoard);
        open.add(new Board(currBoard, "", playerX, playerY));

        while (!open.isEmpty()) {
            Board item = open.poll();
            String cur = item.cur;
            String sol = item.sol;
            int x = item.x;
            int y = item.y;

            for (int i = 0; i < dirs.length; i++) {
                String trial = cur;
                int dx = dirs[i][0];
                int dy = dirs[i][1];

                // are we standing next to a box ?
                if (trial.charAt((y + dy) * nCols + x + dx) == '$') {

                    // can we push it ?
                    if ((trial = push(x, y, dx, dy, trial)) != null) {

                        // or did we already try this one ?
                        if (!history.contains(trial)) {

                            String newSol = sol + dirLabels[i][1];

                            if (isSolved(trial))
                                return newSol;

                            open.add(new Board(trial, newSol, x + dx, y + dy));
                            history.add(trial);
                        }
                    }

                // otherwise try changing position
                } else if ((trial = move(x, y, dx, dy, trial)) != null) {

                    if (!history.contains(trial)) {
                        String newSol = sol + dirLabels[i][0];
                        open.add(new Board(trial, newSol, x + dx, y + dy));
                        history.add(trial);
                    }
                }
            }
        }
        return "No solution";
    }

    public static void main(String[] a) {
        String level = "#######,#     #,#     #,#. #  #,#. $$ #,"
                + "#.$$  #,#.#  @#,#######";
        System.out.println(new Sokoban(level.split(",")).solve());
    }
}

```

## Python Code
### python_code_1.txt
```python
from array import array
from collections import deque
import psyco

data = []
nrows = 0
px = py = 0
sdata = ""
ddata = ""

def init(board):
    global data, nrows, sdata, ddata, px, py
    data = filter(None, board.splitlines())
    nrows = max(len(r) for r in data)

    maps = {' ':' ', '.': '.', '@':' ', '#':'#', '$':' '}
    mapd = {' ':' ', '.': ' ', '@':'@', '#':' ', '$':'*'}

    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            sdata += maps[ch]
            ddata += mapd[ch]
            if ch == '@':
                px = c
                py = r

def push(x, y, dx, dy, data):
    if sdata[(y+2*dy) * nrows + x+2*dx] == '#' or \
       data[(y+2*dy) * nrows + x+2*dx] != ' ':
        return None

    data2 = array("c", data)
    data2[y * nrows + x] = ' '
    data2[(y+dy) * nrows + x+dx] = '@'
    data2[(y+2*dy) * nrows + x+2*dx] = '*'
    return data2.tostring()

def is_solved(data):
    for i in xrange(len(data)):
        if (sdata[i] == '.') != (data[i] == '*'):
            return False
    return True

def solve():
    open = deque([(ddata, "", px, py)])
    visited = set([ddata])
    dirs = ((0, -1, 'u', 'U'), ( 1, 0, 'r', 'R'),
            (0,  1, 'd', 'D'), (-1, 0, 'l', 'L'))

    lnrows = nrows
    while open:
        cur, csol, x, y = open.popleft()

        for di in dirs:
            temp = cur
            dx, dy = di[0], di[1]

            if temp[(y+dy) * lnrows + x+dx] == '*':
                temp = push(x, y, dx, dy, temp)
                if temp and temp not in visited:
                    if is_solved(temp):
                        return csol + di[3]
                    open.append((temp, csol + di[3], x+dx, y+dy))
                    visited.add(temp)
            else:
                if sdata[(y+dy) * lnrows + x+dx] == '#' or \
                   temp[(y+dy) * lnrows + x+dx] != ' ':
                    continue

                data2 = array("c", temp)
                data2[y * lnrows + x] = ' '
                data2[(y+dy) * lnrows + x+dx] = '@'
                temp = data2.tostring()

                if temp not in visited:
                    if is_solved(temp):
                        return csol + di[2]
                    open.append((temp, csol + di[2], x+dx, y+dy))
                    visited.add(temp)

    return "No solution"


level = """\
#######
#     #
#     #
#. #  #
#. $$ #
#.$$  #
#.#  @#
#######"""

psyco.full()
init(level)
print level, "\n\n", solve()

```

