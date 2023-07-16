# Elementary cellular automaton

## Task Link
[Rosetta Code - Elementary cellular automaton](https://rosettacode.org/wiki/Elementary_cellular_automaton)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.ActionEvent;
import javax.swing.*;
import javax.swing.Timer;

public class WolframCA extends JPanel {
    final int[] ruleSet = {30, 45, 50, 57, 62, 70, 73, 75, 86, 89, 90, 99,
        101, 105, 109, 110, 124, 129, 133, 135, 137, 139, 141, 164,170, 232};
    byte[][] cells;
    int rule = 0;

    public WolframCA() {
        Dimension dim = new Dimension(900, 450);
        setPreferredSize(dim);
        setBackground(Color.white);
        setFont(new Font("SansSerif", Font.BOLD, 28));

        cells = new byte[dim.height][dim.width];
        cells[0][dim.width / 2] = 1;

        new Timer(5000, (ActionEvent e) -> {
            rule++;
            if (rule == ruleSet.length)
                rule = 0;
            repaint();
        }).start();
    }

    private byte rules(int lhs, int mid, int rhs) {
        int idx = (lhs << 2 | mid << 1 | rhs);
        return (byte) (ruleSet[rule] >> idx & 1);
    }

    void drawCa(Graphics2D g) {
        g.setColor(Color.black);
        for (int r = 0; r < cells.length - 1; r++) {
            for (int c = 1; c < cells[r].length - 1; c++) {
                byte lhs = cells[r][c - 1];
                byte mid = cells[r][c];
                byte rhs = cells[r][c + 1];
                cells[r + 1][c] = rules(lhs, mid, rhs); // next generation
                if (cells[r][c] == 1) {
                    g.fillRect(c, r, 1, 1);
                }
            }
        }
    }

    void drawLegend(Graphics2D g) {
        String s = String.valueOf(ruleSet[rule]);
        int sw = g.getFontMetrics().stringWidth(s);

        g.setColor(Color.white);
        g.fillRect(16, 5, 55, 30);

        g.setColor(Color.darkGray);
        g.drawString(s, 16 + (55 - sw) / 2, 30);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawCa(g);
        drawLegend(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Wolfram CA");
            f.setResizable(false);
            f.add(new WolframCA(), BorderLayout.CENTER);
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
def eca(cells, rule):
    lencells = len(cells)
    c = "0" + cells + "0"    # Zero pad the ends
    rulebits = '{0:08b}'.format(rule)
    neighbours2next = {'{0:03b}'.format(n):rulebits[::-1][n] for n in range(8)}
    yield c[1:-1]
    while True:
        c = ''.join(['0',
                     ''.join(neighbours2next[c[i-1:i+2]]
                             for i in range(1,lencells+1)),
                     '0'])
        yield c[1:-1]

if __name__ == '__main__':
    lines, start, rules = 50, '0000000001000000000', (90, 30, 122)
    zipped = [range(lines)] + [eca(start, rule) for rule in rules]
    print('\n   Rules: %r' % (rules,))
    for data in zip(*zipped):
        i = data[0]
        cells = data[1:]
        print('%2i: %s' % (i, '    '.join(cells).replace('0', '.').replace('1', '#')))

```

### python_code_2.txt
```python
def eca_wrap(cells, rule):
    lencells = len(cells)
    rulebits = '{0:08b}'.format(rule)
    neighbours2next = {tuple('{0:03b}'.format(n)):rulebits[::-1][n] for n in range(8)}
    c = cells
    while True:
        yield c
        c = ''.join(neighbours2next[(c[i-1], c[i], c[(i+1) % lencells])] for i in range(lencells))

if __name__ == '__main__':
    lines, start, rules = 50, '0000000001000000000', (90, 30, 122)
    zipped = [range(lines)] + [eca_wrap(start, rule) for rule in rules]
    print('\n   Rules: %r' % (rules,))
    for data in zip(*zipped):
        i = data[0]
        cells = data[1:]
        print('%2i: %s' % (i, '    '.join(cells).replace('0', '.').replace('1', '#')))

```

### python_code_3.txt
```python
def _notcell(c):
    return '0' if c == '1' else '1'

def eca_infinite(cells, rule):
    lencells = len(cells)
    rulebits = '{0:08b}'.format(rule)
    neighbours2next = {'{0:03b}'.format(n):rulebits[::-1][n] for n in range(8)}
    c = cells
    while True:
        yield c
        c = _notcell(c[0])*2 + c + _notcell(c[-1])*2    # Extend and pad the ends

        c = ''.join(neighbours2next[c[i-1:i+2]] for i in range(1,len(c) - 1))
        #yield c[1:-1]

if __name__ == '__main__':
    lines, start, rules = 20, '1', (90, 30, 122)
    zipped = [range(lines)] + [eca_infinite(start, rule) for rule in rules]
    print('\n   Rules: %r' % (rules,))
    for data in zip(*zipped):
        i = data[0]
        cells = ['%s%s%s' % (' '*(lines - i), c, ' '*(lines - i)) for c in data[1:]]
        print('%2i: %s' % (i, '    '.join(cells).replace('0', '.').replace('1', '#')))

```

