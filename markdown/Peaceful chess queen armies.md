# Peaceful chess queen armies

## Task Link
[Rosetta Code - Peaceful chess queen armies](https://rosettacode.org/wiki/Peaceful_chess_queen_armies)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Peaceful {
    enum Piece {
        Empty,
        Black,
        White,
    }

    public static class Position {
        public int x, y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj instanceof Position) {
                Position pos = (Position) obj;
                return pos.x == x && pos.y == y;
            }
            return false;
        }
    }

    private static boolean place(int m, int n, List<Position> pBlackQueens, List<Position> pWhiteQueens) {
        if (m == 0) {
            return true;
        }
        boolean placingBlack = true;
        for (int i = 0; i < n; ++i) {
            inner:
            for (int j = 0; j < n; ++j) {
                Position pos = new Position(i, j);
                for (Position queen : pBlackQueens) {
                    if (pos.equals(queen) || !placingBlack && isAttacking(queen, pos)) {
                        continue inner;
                    }
                }
                for (Position queen : pWhiteQueens) {
                    if (pos.equals(queen) || placingBlack && isAttacking(queen, pos)) {
                        continue inner;
                    }
                }
                if (placingBlack) {
                    pBlackQueens.add(pos);
                    placingBlack = false;
                } else {
                    pWhiteQueens.add(pos);
                    if (place(m - 1, n, pBlackQueens, pWhiteQueens)) {
                        return true;
                    }
                    pBlackQueens.remove(pBlackQueens.size() - 1);
                    pWhiteQueens.remove(pWhiteQueens.size() - 1);
                    placingBlack = true;
                }
            }
        }
        if (!placingBlack) {
            pBlackQueens.remove(pBlackQueens.size() - 1);
        }
        return false;
    }

    private static boolean isAttacking(Position queen, Position pos) {
        return queen.x == pos.x
            || queen.y == pos.y
            || Math.abs(queen.x - pos.x) == Math.abs(queen.y - pos.y);
    }

    private static void printBoard(int n, List<Position> blackQueens, List<Position> whiteQueens) {
        Piece[] board = new Piece[n * n];
        Arrays.fill(board, Piece.Empty);

        for (Position queen : blackQueens) {
            board[queen.x + n * queen.y] = Piece.Black;
        }
        for (Position queen : whiteQueens) {
            board[queen.x + n * queen.y] = Piece.White;
        }
        for (int i = 0; i < board.length; ++i) {
            if ((i != 0) && i % n == 0) {
                System.out.println();
            }

            Piece b = board[i];
            if (b == Piece.Black) {
                System.out.print("B ");
            } else if (b == Piece.White) {
                System.out.print("W ");
            } else {
                int j = i / n;
                int k = i - j * n;
                if (j % 2 == k % 2) {
                    System.out.print("• ");
                } else {
                    System.out.print("◦ ");
                }
            }
        }
        System.out.println('\n');
    }

    public static void main(String[] args) {
        List<Position> nms = List.of(
            new Position(2, 1),
            new Position(3, 1),
            new Position(3, 2),
            new Position(4, 1),
            new Position(4, 2),
            new Position(4, 3),
            new Position(5, 1),
            new Position(5, 2),
            new Position(5, 3),
            new Position(5, 4),
            new Position(5, 5),
            new Position(6, 1),
            new Position(6, 2),
            new Position(6, 3),
            new Position(6, 4),
            new Position(6, 5),
            new Position(6, 6),
            new Position(7, 1),
            new Position(7, 2),
            new Position(7, 3),
            new Position(7, 4),
            new Position(7, 5),
            new Position(7, 6),
            new Position(7, 7)
        );
        for (Position nm : nms) {
            int m = nm.y;
            int n = nm.x;
            System.out.printf("%d black and %d white queens on a %d x %d board:\n", m, m, n, n);
            List<Position> blackQueens = new ArrayList<>();
            List<Position> whiteQueens = new ArrayList<>();
            if (place(m, n, blackQueens, whiteQueens)) {
                printBoard(n, blackQueens, whiteQueens);
            } else {
                System.out.println("No solution exists.\n");
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations, product, count
from functools import lru_cache, reduce


_bbullet, _wbullet = '\u2022\u25E6'
_or = set.__or__

def place(m, n):
    "Place m black and white queens, peacefully, on an n-by-n board"
    board = set(product(range(n), repeat=2))  # (x, y) tuples
    placements = {frozenset(c) for c in combinations(board, m)}
    for blacks in placements:
        black_attacks = reduce(_or, 
                               (queen_attacks_from(pos, n) for pos in blacks), 
                               set())
        for whites in {frozenset(c)     # Never on blsck attacking squares
                       for c in combinations(board - black_attacks, m)}:
            if not black_attacks & whites:
                return blacks, whites
    return set(), set()

@lru_cache(maxsize=None)
def queen_attacks_from(pos, n):
    x0, y0 = pos
    a = set([pos])    # Its position
    a.update((x, y0) for x in range(n))    # Its row
    a.update((x0, y) for y in range(n))    # Its column
    # Diagonals
    for x1 in range(n):
        # l-to-r diag
        y1 = y0 -x0 +x1
        if 0 <= y1 < n: 
            a.add((x1, y1))
        # r-to-l diag
        y1 = y0 +x0 -x1
        if 0 <= y1 < n: 
            a.add((x1, y1))
    return a

def pboard(black_white, n):
    "Print board"
    if black_white is None: 
        blk, wht = set(), set()
    else:
        blk, wht = black_white
    print(f"## {len(blk)} black and {len(wht)} white queens "
          f"on a {n}-by-{n} board:", end='')
    for x, y in product(range(n), repeat=2):
        if y == 0:
            print()
        xy = (x, y)
        ch = ('?' if xy in blk and xy in wht 
              else 'B' if xy in blk
              else 'W' if xy in wht
              else _bbullet if (x + y)%2 else _wbullet)
        print('%s' % ch, end='')
    print()

if __name__ == '__main__':
    n=2
    for n in range(2, 7):
        print()
        for m in count(1):
            ans = place(m, n)
            if ans[0]:
                pboard(ans, n)
            else:
                print (f"# Can't place {m} queens on a {n}-by-{n} board")
                break
    #
    print('\n')
    m, n = 5, 7
    ans = place(m, n)
    pboard(ans, n)

```

### python_code_2.txt
```python
from peaceful_queen_armies_simpler import place
from itertools import product, count

_bqueenh, _wqueenh = '&#x265b;', '<font color="green">&#x2655;</font>'

def hboard(black_white, n):
    "HTML board generator"
    if black_white is None: 
        blk, wht = set(), set()
    else:
        blk, wht = black_white
    out = (f"<br><b>## {len(blk)} black and {len(wht)} white queens "
           f"on a {n}-by-{n} board</b><br>\n")
    out += '<table style="font-weight:bold">\n  '
    tbl = ''
    for x, y in product(range(n), repeat=2):
        if y == 0:
            tbl += '  </tr>\n  <tr valign="middle" align="center">\n'
        xy = (x, y)
        ch = ('<span style="color:red">?</span>' if xy in blk and xy in wht 
              else _bqueenh if xy in blk
              else _wqueenh if xy in wht
              else "")
        bg = "" if (x + y)%2 else ' bgcolor="silver"'
        tbl += f'    <td style="width:14pt; height:14pt;"{bg}>{ch}</td>\n'
    out += tbl[7:]
    out += '  </tr>\n</table>\n<br>\n'
    return out

if __name__ == '__main__':
    n=2
    html = ''
    for n in range(2, 7):
        print()
        for m in count(1):
            ans = place(m, n)
            if ans[0]:
                html += hboard(ans, n)
            else:
                html += (f"<b># Can't place {m} queen armies on a "
                         f"{n}-by-{n} board</b><br><br>\n\n" )
                break
    #
    html += '<br>\n'
    m, n = 6, 7
    ans = place(m, n)
    html += hboard(ans, n)
    with open('peaceful_queen_armies.htm', 'w') as f:
        f.write(html)

```

