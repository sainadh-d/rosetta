# Flipping bits game

## Task Link
[Rosetta Code - Flipping bits game](https://rosettacode.org/wiki/Flipping_bits_game)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class FlippingBitsGame extends JPanel {
    final int maxLevel = 7;
    final int minLevel = 3;

    private Random rand = new Random();
    private int[][] grid, target;
    private Rectangle box;
    private int n = maxLevel;
    private boolean solved = true;

    FlippingBitsGame() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);
        setFont(new Font("SansSerif", Font.PLAIN, 18));

        box = new Rectangle(120, 90, 400, 400);

        startNewGame();

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (solved) {
                    startNewGame();
                } else {
                    int x = e.getX();
                    int y = e.getY();

                    if (box.contains(x, y))
                        return;

                    if (x > box.x && x < box.x + box.width) {
                        flipCol((x - box.x) / (box.width / n));

                    } else if (y > box.y && y < box.y + box.height)
                        flipRow((y - box.y) / (box.height / n));

                    if (solved(grid, target))
                        solved = true;

                    printGrid(solved ? "Solved!" : "The board", grid);
                }
                repaint();
            }
        });
    }

    void startNewGame() {
        if (solved) {

            n = (n == maxLevel) ? minLevel : n + 1;

            grid = new int[n][n];
            target = new int[n][n];

            do {
                shuffle();

                for (int i = 0; i < n; i++)
                    target[i] = Arrays.copyOf(grid[i], n);

                shuffle();

            } while (solved(grid, target));

            solved = false;
            printGrid("The target", target);
            printGrid("The board", grid);
        }
    }

    void printGrid(String msg, int[][] g) {
        System.out.println(msg);
        for (int[] row : g)
            System.out.println(Arrays.toString(row));
        System.out.println();
    }

    boolean solved(int[][] a, int[][] b) {
        for (int i = 0; i < n; i++)
            if (!Arrays.equals(a[i], b[i]))
                return false;
        return true;
    }

    void shuffle() {
        for (int i = 0; i < n * n; i++) {
            if (rand.nextBoolean())
                flipRow(rand.nextInt(n));
            else
                flipCol(rand.nextInt(n));
        }
    }

    void flipRow(int r) {
        for (int c = 0; c < n; c++) {
            grid[r][c] ^= 1;
        }
    }

    void flipCol(int c) {
        for (int[] row : grid) {
            row[c] ^= 1;
        }
    }

    void drawGrid(Graphics2D g) {
        g.setColor(getForeground());

        if (solved)
            g.drawString("Solved! Click here to play again.", 180, 600);
        else
            g.drawString("Click next to a row or a column to flip.", 170, 600);

        int size = box.width / n;

        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) {
                g.setColor(grid[r][c] == 1 ? Color.blue : Color.orange);
                g.fillRect(box.x + c * size, box.y + r * size, size, size);
                g.setColor(getBackground());
                g.drawRect(box.x + c * size, box.y + r * size, size, size);
                g.setColor(target[r][c] == 1 ? Color.blue : Color.orange);
                g.fillRect(7 + box.x + c * size, 7 + box.y + r * size, 10, 10);
            }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawGrid(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Flipping Bits Game");
            f.setResizable(false);
            f.add(new FlippingBitsGame(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
"""
Given a %i by %i sqare array of zeroes or ones in an initial
configuration, and a target configuration of zeroes and ones
The task is to transform one to the other in as few moves as 
possible by inverting whole numbered rows or whole lettered 
columns at once.
In an inversion any 1 becomes 0 and any 0 becomes 1 for that
whole row or column.

"""

from random import randrange
from copy import deepcopy
from string import ascii_lowercase


try:    # 2to3 fix
    input = raw_input
except:
    pass

N = 3   # N x N Square arrray

board  = [[0]* N for i in range(N)]

def setbits(board, count=1):
    for i in range(count):
        board[randrange(N)][randrange(N)] ^= 1

def shuffle(board, count=1):
    for i in range(count):
        if randrange(0, 2):
            fliprow(randrange(N))
        else:
            flipcol(randrange(N))


def pr(board, comment=''):
    print(str(comment))
    print('     ' + ' '.join(ascii_lowercase[i] for i in range(N)))
    print('  ' + '\n  '.join(' '.join(['%2s' % j] + [str(i) for i in line])
                             for j, line in enumerate(board, 1)))

def init(board):
    setbits(board, count=randrange(N)+1)
    target = deepcopy(board)
    while board == target:
        shuffle(board, count=2 * N)
    prompt = '  X, T, or 1-%i / %s-%s to flip: ' % (N, ascii_lowercase[0], 
                                                    ascii_lowercase[N-1])
    return target, prompt

def fliprow(i):
    board[i-1][:] = [x ^ 1 for x in board[i-1] ]
    
def flipcol(i):
    for row in board:
        row[i] ^= 1

if __name__ == '__main__':
    print(__doc__ % (N, N))
    target, prompt = init(board)
    pr(target, 'Target configuration is:')
    print('')
    turns = 0
    while board != target:
        turns += 1
        pr(board, '%i:' % turns)
        ans = input(prompt).strip()
        if (len(ans) == 1 
            and ans in ascii_lowercase and ascii_lowercase.index(ans) < N):
            flipcol(ascii_lowercase.index(ans))
        elif ans and all(ch in '0123456789' for ch in ans) and 1 <= int(ans) <= N:
            fliprow(int(ans))
        elif ans == 'T':
            pr(target, 'Target configuration is:')
            turns -= 1
        elif ans == 'X':
            break
        else:
            print("  I don't understand %r... Try again. "
                  "(X to exit or T to show target)\n" % ans[:9])
            turns -= 1
    else:
        print('\nWell done!\nBye.')

```

