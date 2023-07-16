# Abelian sandpile model

## Task Link
[Rosetta Code - Abelian sandpile model](https://rosettacode.org/wiki/Abelian_sandpile_model)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class AbelianSandpile {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Frame frame = new Frame();
                frame.setVisible(true);
            }
        });
    }

    private static class Frame extends JFrame {
        private Frame() {
            super("Abelian Sandpile Model");
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            Container contentPane = getContentPane();
            JPanel controlPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
            JButton start = new JButton("Restart Simulation");
            start.addActionListener(e -> restartSimulation());
            JButton stop = new JButton("Stop Simulation");
            stop.addActionListener(e -> stopSimulation());
            controlPanel.add(start);
            controlPanel.add(stop);
            contentPane.add(controlPanel, BorderLayout.NORTH);
            contentPane.add(canvas = new Canvas(), BorderLayout.CENTER);
            timer = new Timer(100, e -> canvas.runAndDraw());
            timer.start();
            pack();
        }

        private void restartSimulation() {
            timer.stop();
            canvas.initGrid();
            timer.start();
        }

        private void stopSimulation() {
            timer.stop();
        }

        private Timer timer;
        private Canvas canvas;
    }

    private static class Canvas extends JComponent {
        private Canvas() {
            setBorder(BorderFactory.createEtchedBorder());
            setPreferredSize(new Dimension(600, 600));
        }

        public void paintComponent(Graphics g) {
            int width = getWidth();
            int height = getHeight();
            g.setColor(Color.WHITE);
            g.fillRect(0, 0, width, height);
            int cellWidth = width/GRID_LENGTH;
            int cellHeight = height/GRID_LENGTH;
            for (int i = 0; i < GRID_LENGTH; ++i) {
                for (int j = 0; j < GRID_LENGTH; ++j) {
                    if (grid[i][j] > 0) {
                        g.setColor(COLORS[grid[i][j]]);
                        g.fillRect(i * cellWidth, j * cellHeight, cellWidth, cellHeight);
                    }
                }
            }
        }

        private void initGrid() {
            for (int i = 0; i < GRID_LENGTH; ++i) {
                for (int j = 0; j < GRID_LENGTH; ++j) {
                    grid[i][j] = 0;
                }
            }
        }

        private void runAndDraw() {
            for (int i = 0; i < 100; ++i)
                addSand(GRID_LENGTH/2, GRID_LENGTH/2);
            repaint();
        }

        private void addSand(int i, int j) {
            int grains = grid[i][j];
            if (grains < 3) {
                grid[i][j]++;
            }
            else {
                grid[i][j] = grains - 3;
                if (i > 0)
                    addSand(i - 1, j);
                if (i < GRID_LENGTH - 1)
                    addSand(i + 1, j);
                if (j > 0)
                    addSand(i, j - 1);
                if (j < GRID_LENGTH - 1)
                    addSand(i, j + 1);
            }
        }

        private int[][] grid = new int[GRID_LENGTH][GRID_LENGTH];
    }

    private static final Color[] COLORS = {
        Color.WHITE,
        new Color(0x00, 0xbf, 0xff),
        new Color(0xff, 0xd7, 0x00),
        new Color(0xb0, 0x30, 0x60)
    };
    private static final int GRID_LENGTH = 300;
}

```

## Python Code
### python_code_1.txt
```python
import numpy as np
import matplotlib.pyplot as plt


def iterate(grid):
    changed = False
    for ii, arr in enumerate(grid):
        for jj, val in enumerate(arr):
            if val > 3:
                grid[ii, jj] -= 4
                if ii > 0:
                    grid[ii - 1, jj] += 1
                if ii < len(grid)-1:
                    grid[ii + 1, jj] += 1
                if jj > 0:
                    grid[ii, jj - 1] += 1
                if jj < len(grid)-1:
                    grid[ii, jj + 1] += 1
                changed = True
    return grid, changed


def simulate(grid):
    while True:
        grid, changed = iterate(grid)
        if not changed:
            return grid


if __name__ == '__main__':
    start_grid = np.zeros((10, 10))
    start_grid[4:5, 4:5] = 64
    final_grid = simulate(start_grid.copy())
    plt.figure()
    plt.gray()
    plt.imshow(start_grid)
    plt.figure()
    plt.gray()
    plt.imshow(final_grid)

```

### python_code_2.txt
```python
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0.64. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

```

### python_code_3.txt
```python
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 1. 2. 1. 0. 0. 0. 0.]
 [0. 0. 2. 2. 2. 2. 2. 0. 0. 0.]
 [0. 1. 2. 2. 2. 2. 2. 1. 0. 0.]
 [0. 2. 2. 2. 0. 2. 2. 2. 0. 0.]
 [0. 1. 2. 2. 2. 2. 2. 1. 0. 0.]
 [0. 0. 2. 2. 2. 2. 2. 0. 0. 0.]
 [0. 0. 0. 1. 2. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

```

### python_code_4.txt
```python
from os import system, name
from time import sleep

def clear():
	if name == 'nt':
		_ = system('cls')
	else: _ = system('clear')

def exit():
	import sys
	clear()
	sys.exit()

def make_area(x, y):
	area = [[0]*x for _ in range(y)]
	return area

def make_sandpile(area, loc, height):
	loc=list(n-1 for n in loc)
	x, y = loc

	try: area[y][x]+=height
	except IndexError: pass
	
def run(area, by_frame=False):
	def run_frame():
		for y_index, group in enumerate(area):
			y = y_index+1

			for x_index, height in enumerate(group):
				x = x_index+1

				if height < 4: continue

				else:
					make_sandpile(area, (x+1, y), 1)
					make_sandpile(area, (x, y+1), 1)

					if x_index-1 >= 0:
						make_sandpile(area, (x-1, y), 1)
					if y_index-1 >= 0:
						make_sandpile(area, (x, y-1), 1)

					make_sandpile(area, (x, y), -4)

	while any([any([pile>=4 for pile in group]) for group in area]):
		if by_frame:
			clear()
		run_frame()
		if by_frame:
			show_area(area); sleep(.05)

def show_area(area):
	display = [' '.join([str(item) if item else ' ' for item in group]) 
			   for group in area]
	[print(i) for i in display]

clear()
if __name__ == '__main__':
	area = make_area(10, 10)
	print('\nBefore:')
	show_area(area)
	make_sandpile(area, (5, 5), 64)
	run(area)
	print('\nAfter:')
	show_area(area)

```

### python_code_5.txt
```python
Before:
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

After:
0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 1 0 0 0 0
0 0 2 2 2 2 2 0 0 0
0 1 2 2 2 2 2 1 0 0
0 2 2 2 0 2 2 2 0 0
0 1 2 2 2 2 2 1 0 0
0 0 2 2 2 2 2 0 0 0
0 0 0 1 2 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

```

### python_code_6.txt
```python
''' Python 3.6.5 code using Tkinter graphical user
    interface (Canvas widget) to display final results.'''
from tkinter import *

# given a grid, display it on a tkinter Canvas:
class Sandpile:
    def __init__(self, wn, grid):
        self.window = wn
        self.grid = grid
        self.canvas = Canvas(wn, bg='lemon chiffon')
        self.canvas.pack(fill=BOTH, expand=1)       

        colors = {0:'dodger blue',
                  1:'red',
                  2:'green',
                  3:'lemon chiffon'}
        
        x = 10
        y = 10
        d = 5
        
        for row in self.grid:
            for value in row:
                clr = colors[value]
                self.canvas.create_rectangle(
                    x, y, x+d, y+d,
                    outline=clr,
                    fill = clr)
                x += 5
            x = 10
            y += 5
            
class Grid:
    def __init__(self, size, center):
        self.size = size        # rows/cols in (best if odd)
        self.center = center    # start value at center of grid
        self.grid = [[0]*self.size for i in range(self.size)]
        self.grid[self.size // 2][self.size // 2] = self.center

    # print the grid:
    def show(self, msg):
        print('  ' + msg + ':')
        for row in self.grid:
            print(' '.join(str(x) for x in row))       
        print()
        return

    # dissipate piles of sand as required:
    def abelian(self):
        while True:
            found = False
            for r in range(self.size):
                for c in range(self.size):
                    if self.grid[r][c] > 3:
                        self.distribute(self.grid[r][c], r, c)
                        found = True
            if not found:
                return

    # distribute sand from a single pile to its neighbors:
    def distribute(self, nbr, row, col):
        qty, remain = divmod(nbr, 4)
        self.grid[row][col] = remain
        for r, c in [(row+1, col),
                     (row-1, col),
                     (row, col+1),
                     (row, col-1)]:
            self.grid[r][c] += qty
        return

    # display the grid using tkinter:
    def display(self):
        root = Tk()
        root.title('Sandpile')
        root.geometry('700x700+100+50')
        sp = Sandpile(root, self.grid)
        root.mainloop()

# execute program for size, center value pair:
# just print results for a small grid
g = Grid(9,17)
g.show('BEFORE')
g.abelian()          # scatter the sand
g.show('AFTER')

# just show results in tkinter for a large grid
# I wish there was a way to attach a screen shot
# of the tkinter result here
g = Grid(131,25000)
g.abelian()          # scatter the sand
g.display()          # display result using tkinter
  
##  OUTPUT:
##
##      BEFORE:
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 17 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##
##      AFTER:
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 1 0 0 0 0
##    0 0 0 2 1 2 0 0 0
##    0 0 1 1 1 1 1 0 0
##    0 0 0 2 1 2 0 0 0
##    0 0 0 0 1 0 0 0 0
##    0 0 0 0 0 0 0 0 0
##    0 0 0 0 0 0 0 0 0

```

