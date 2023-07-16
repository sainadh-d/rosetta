# 15 puzzle game

## Task Link
[Rosetta Code - 15 puzzle game](https://rosettacode.org/wiki/15_puzzle_game)

## Java Code
### java_code_1.txt
```java
package fifteenpuzzle;

import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import javax.swing.*;

class FifteenPuzzle extends JPanel {

    private final int side = 4;
    private final int numTiles = side * side - 1;

    private final Random rand = new Random();
    private final int[] tiles = new int[numTiles + 1];
    private final int tileSize;
    private int blankPos;
    private final int margin;
    private final int gridSize;
    private boolean gameOver;

    private FifteenPuzzle() {
        final int dim = 640;

        margin = 80;
        tileSize = (dim - 2 * margin) / side;
        gridSize = tileSize * side;

        setPreferredSize(new Dimension(dim, dim + margin));
        setBackground(Color.WHITE);
        setForeground(new Color(0x6495ED)); // cornflowerblue
        setFont(new Font("SansSerif", Font.BOLD, 60));

        gameOver = true;

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (gameOver) {
                    newGame();

                } else {

                    int ex = e.getX() - margin;
                    int ey = e.getY() - margin;

                    if (ex < 0 || ex > gridSize || ey < 0 || ey > gridSize) {
                        return;
                    }

                    int c1 = ex / tileSize;
                    int r1 = ey / tileSize;
                    int c2 = blankPos % side;
                    int r2 = blankPos / side;

                    int clickPos = r1 * side + c1;

                    int dir = 0;
                    if (c1 == c2 && Math.abs(r1 - r2) > 0) {
                        dir = (r1 - r2) > 0 ? 4 : -4;
                        
                    } else if (r1 == r2 && Math.abs(c1 - c2) > 0) {
                        dir = (c1 - c2) > 0 ? 1 : -1;
                    }

                    if (dir != 0) {
                        do {
                            int newBlankPos = blankPos + dir;
                            tiles[blankPos] = tiles[newBlankPos];
                            blankPos = newBlankPos;
                        } while (blankPos != clickPos);
                        tiles[blankPos] = 0;
                    }
                    
                    gameOver = isSolved();
                }
                repaint();
            }
        });

        newGame();
    }

    private void newGame() {
        do {
            reset();
            shuffle();
        } while (!isSolvable());
        gameOver = false;
    }

    private void reset() {
        for (int i = 0; i < tiles.length; i++) {
            tiles[i] = (i + 1) % tiles.length;
        }
        blankPos = tiles.length - 1;
    }

    private void shuffle() {
        // don't include the blank space in the shuffle, leave it
        // in the home position
        int n = numTiles;
        while (n > 1) {
            int r = rand.nextInt(n--);
            int tmp = tiles[r];
            tiles[r] = tiles[n];
            tiles[n] = tmp;
        }
    }

    /*  Only half the permutations of the puzzle are solvable.

        Whenever a tile is preceded by a tile with higher value it counts
        as an inversion. In our case, with the blank space in the home
        position, the number of inversions must be even for the puzzle
        to be solvable.

        See also:
        www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
     */
    private boolean isSolvable() {
        int countInversions = 0;
        for (int i = 0; i < numTiles; i++) {
            for (int j = 0; j < i; j++) {
                if (tiles[j] > tiles[i]) {
                    countInversions++;
                }
            }
        }
        return countInversions % 2 == 0;
    }

    private boolean isSolved() {
        if (tiles[tiles.length - 1] != 0) {
            return false;
        }
        for (int i = numTiles - 1; i >= 0; i--) {
            if (tiles[i] != i + 1) {
                return false;
            }
        }
        return true;
    }

    private void drawGrid(Graphics2D g) {
        for (int i = 0; i < tiles.length; i++) {
            int r = i / side;
            int c = i % side;
            int x = margin + c * tileSize;
            int y = margin + r * tileSize;

            if (tiles[i] == 0) {
                if (gameOver) {
                    g.setColor(Color.GREEN);
                    drawCenteredString(g, "\u2713", x, y);
                }
                continue;
            }

            g.setColor(getForeground());
            g.fillRoundRect(x, y, tileSize, tileSize, 25, 25);
            g.setColor(Color.blue.darker());
            g.drawRoundRect(x, y, tileSize, tileSize, 25, 25);
            g.setColor(Color.WHITE);

            drawCenteredString(g, String.valueOf(tiles[i]), x, y);
        }
    }

    private void drawStartMessage(Graphics2D g) {
        if (gameOver) {
            g.setFont(getFont().deriveFont(Font.BOLD, 18));
            g.setColor(getForeground());
            String s = "click to start a new game";
            int x = (getWidth() - g.getFontMetrics().stringWidth(s)) / 2;
            int y = getHeight() - margin;
            g.drawString(s, x, y);
        }
    }

    private void drawCenteredString(Graphics2D g, String s, int x, int y) {
        FontMetrics fm = g.getFontMetrics();
        int asc = fm.getAscent();
        int des = fm.getDescent();

        x = x + (tileSize - fm.stringWidth(s)) / 2;
        y = y + (asc + (tileSize - (asc + des)) / 2);

        g.drawString(s, x, y);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawGrid(g);
        drawStartMessage(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Fifteen Puzzle");
            f.setResizable(false);
            f.add(new FifteenPuzzle(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
int number_of_grid_cells = 16;  //   Set the number of cells of the board here 9, 16, 25 etc  
color piece_color = color(255, 175, 0);
color background_color = color(235, 231, 178);
color piece_shadow_dark = color(206, 141, 0);
color piece_shadow_light = color(255, 214, 126);
int z, t, p, piece_number, row_length, piece_side_length;

PuzzlePiece[] piece = new PuzzlePiece[number_of_grid_cells]; //  Number of puzzle pieces objects array

void setup() { 
  size(400, 400);  // Window size width and height must be egual
	background(200, 50, 0);
  row_length = int(sqrt(number_of_grid_cells));
  piece_side_length = width/row_length;
  textSize(piece_side_length/2.7);
  textAlign(CENTER);

  PVector[] xy_values = new PVector[number_of_grid_cells]; //  Setting the x and y values for each cell on grid
  for (int i = 0; i < number_of_grid_cells; i += row_length) { // Values are the top left pixel of the cell
    for (int j = 0; j < row_length; j++) {
      xy_values[z] = new PVector();
      xy_values[z].x = j*piece_side_length;
      xy_values[z].y = t*piece_side_length; 
      z++;
    }
    t++;
  } 

  int[] place = new int[number_of_grid_cells]; // This array is  to help placing the pieces randomly and store values in piece objects array
  for (int i = 0; i < number_of_grid_cells; i++) place[i] = 0;
  piece_number = 0;

  while (piece_number < number_of_grid_cells) {  // Placing pieces randomly in grid
    p = int(random(0, number_of_grid_cells));
    if (place[p] == 0) { // Once placed will be set to 1 to avoid designing again at this location
      piece[piece_number] = new PuzzlePiece(piece_number, xy_values[p].x, xy_values[p].y); // Creating the piece objects array 
      place[p] = 1;
      piece[piece_number].design(); // Design newly create piece object
      piece_number++;
    }
  }
}

void draw() {  
  for (int i = 0; i < number_of_grid_cells; i++) {   // Search all piece object indexes and verify which one is mouse pressed in this loop
    if (mousePressed == true && mouseX >= piece[i].xPosition() && mouseX <= piece[i].xPosition()+piece_side_length && mouseY >= piece[i].yPosition() && mouseY <= piece[i].yPosition()+piece_side_length && piece[i].pieceNumber() != 15) {  
      if (pieceMove(piece[number_of_grid_cells-1].xPosition(), piece[number_of_grid_cells-1].yPosition(), piece[i].xPosition(), piece[i].yPosition())) {
        float temp_x = piece[number_of_grid_cells-1].xPosition(); // Remember x and y value of final piece index (white piece) 
        float temp_y = piece[number_of_grid_cells-1].yPosition();
        piece[number_of_grid_cells-1].storePos(piece[i].xPosition(), piece[i].yPosition()); // Store clicked x and y value in final index of piece array
        piece[i].storePos(temp_x, temp_y); // Store temp x and y value (the last/previous final index values) in current clicked piece index  
        piece[number_of_grid_cells-1].design(); // draw the final index piece index (only final piece index is painted white)
        piece[i].design(); // Draw a numbered piece of current index
      }
    }
  }
}

boolean pieceMove(float final_index_piece_x, float final_index_piece_y, float current_index_x, float current_index_y) {
  // If both x values from clicked and white piece have same value meaning in same horizontal column 
  // AND   current clicked y value is equal to white piece y value - piece side lenght  OR  current clicked y value + piece side lenght is egual to white piece y 
  if (current_index_x == final_index_piece_x && (current_index_y == final_index_piece_y-piece_side_length || (current_index_y == final_index_piece_y+piece_side_length))) return true;
  // If both y values from clicked and white piece have same value meaning in same vertical column 
  // AND   current clicked x value is equal to white piece x value - piece side lenght  OR  current clicked x value + piece side lenght is egual to white piece x 
  else if (current_index_y == final_index_piece_y && (current_index_x == final_index_piece_x-piece_side_length || (current_index_x == final_index_piece_x+piece_side_length))) return true;
  else return false;
}

class PuzzlePiece {   
  int piece_number;
  float x_pos, y_pos;

  PuzzlePiece(int _piece_nr, float _xp, float _yp) {
    piece_number = _piece_nr;
    x_pos = _xp;
    y_pos = _yp;
  }  

  void storePos(float _xp, float _yp) {
    x_pos = _xp;
    y_pos = _yp;
  }

  int pieceNumber() {
    return piece_number;
  }

  float xPosition() {
    return x_pos;
  }

  float yPosition() {
    return y_pos;
  }

  void design() {
    noStroke();
    fill(piece_color);
    if (piece_number == number_of_grid_cells-1) fill(background_color);   
    rect(x_pos+1, y_pos+1, piece_side_length-1, piece_side_length-1);
    if (piece_number != number_of_grid_cells-1) {
      fill(0); // Black text shadow
      text(piece_number+1, x_pos+piece_side_length/2+1, y_pos+piece_side_length/2+textAscent()/2);
      fill(255);
      text(piece_number+1, x_pos+piece_side_length/2, y_pos+piece_side_length/2+textAscent()/2);
      stroke(piece_shadow_dark);
      line(x_pos+piece_side_length-1, y_pos+1, x_pos+piece_side_length-1, y_pos+piece_side_length-1); // Right side shadow
      line(x_pos+2, y_pos+piece_side_length, x_pos+piece_side_length-1, y_pos+piece_side_length); // Bottom side shadow
      stroke(piece_shadow_light);
      line(x_pos+2, y_pos-1, x_pos+2, y_pos+piece_side_length); // Left bright
      line(x_pos+2, y_pos+1, x_pos+piece_side_length-1, y_pos+1); // Upper bright
    }
  }
}

```

## Python Code
### python_code_2.txt
```python
# Set the number of cells of the board here 9, 16, 25 etc
num_grid_cells = 16
piece_color = color(255, 175, 0)
background_color = color(235, 231, 178)
piece_shadow_dark = color(206, 141, 0)
piece_shadow_light = color(255, 214, 126)

def setup():
    global piece, piece_number, row_length, piece_side_length
    size(400, 400)  # Window size width and height must be egual
    background(200, 50, 0)
    row_length = int(sqrt(num_grid_cells))
    piece_side_length = width / row_length
    textSize(piece_side_length / 2.7)
    textAlign(CENTER)
    # Setting the x and y values for each cell on grid
    xy_val = []
    t = 0
    for i in range(0, num_grid_cells, row_length):
        for j in range(row_length):
            xy_val.append((j * piece_side_length,
                           t * piece_side_length))
        t += 1
    piece = []  # Puzzle piece objects
    placed = [False] * num_grid_cells  # to help placing the pieces randomly
    piece_number = 0
    # Placing pieces randomly in grid
    while (piece_number < num_grid_cells):
        p = int(random(0, num_grid_cells))
        # Once placed will be set to True to avoid adding again at this location
        if not placed[p]:
            # Creating the piece objects list
            piece.append(PuzzlePiece(piece_number, xy_val[p][0], xy_val[p][1]))
            placed[p] = True
            piece[piece_number].design()  # Draw newly create piece object
            piece_number += 1

def draw():
    # Search all piece object indexes and verify which one is mouse pressed
    for i in range(num_grid_cells):
        if (mousePressed and
                piece[i].x <= mouseX <= piece[i].x + piece_side_length and
                piece[i].y <= mouseY <= piece[i].y + piece_side_length and
                piece[i].piece_number != 15):
            if (pieceMove(piece[num_grid_cells - 1].x, piece[num_grid_cells - 1].y, piece[i].x, piece[i].y)):
                # Remember x and y value of final piece index (white piece)
                temp_x = int(piece[num_grid_cells - 1].x)
                temp_y = int(piece[num_grid_cells - 1].y)
                # Store clicked x and y value in final index of piece list
                piece[num_grid_cells - 1].set_pos(piece[i].x, piece[i].y)
                # Store temp x and y value (the last/previous final index
                # values) in current clicked piece
                piece[i].set_pos(temp_x, temp_y)
                # draw the final index piece index (only final piece index is
                # painted white)
                piece[num_grid_cells - 1].design()
                piece[i].design()  # Draw a numbered piece of current index

def pieceMove(final_index_piece_x, final_index_piece_y, current_index_x, current_index_y):
    # If both x's from clicked and white piece have same value meaning in same horizontal column
    # AND current clicked y value is equal to white piece y value - piece side lenght OR
    # current clicked y value + piece side lenght is egual to white piece y
    if (current_index_x == final_index_piece_x and (current_index_y == final_index_piece_y - piece_side_length or
                                                    (current_index_y == final_index_piece_y + piece_side_length))):
        return True
    # If both y's from clicked and white piece have same value meaning in same vertical column AND current clicked x value
    # is equal to white piece x value - piece side lenght OR current clicked x value + piece side lenght is
    # egual to white piece x
    elif (current_index_y == final_index_piece_y and (current_index_x == final_index_piece_x - piece_side_length or
                                                      (current_index_x == final_index_piece_x + piece_side_length))):
        return True
    else:
        return False

class PuzzlePiece:

    def __init__(self, pn, xp, yp):
        self.piece_number = pn
        self.x = xp
        self.y = yp

    def set_pos(self, xp, yp):
        self.x = xp
        self.y = yp

    def design(self):
        noStroke()
        fill(piece_color)
        if (self.piece_number == num_grid_cells - 1):
            fill(background_color)
        rect(self.x + 1, self.y + 1,
             piece_side_length - 1, piece_side_length - 1)
        if (self.piece_number != num_grid_cells - 1):
            fill(0)  # Black text shadow
            text(self.piece_number + 1, self.x + piece_side_length / 2 + 2,
                 self.y + piece_side_length / 2 + textAscent() / 2)
            fill(255)
            text(self.piece_number + 1, self.x + piece_side_length / 2,
                 self.y + piece_side_length / 2 + textAscent() / 2)
            stroke(piece_shadow_dark)
            line(self.x + piece_side_length - 1, self.y + 1, self.x +
                 piece_side_length - 1, self.y + piece_side_length - 1)  # Right side shadow
            line(self.x + 2, self.y + piece_side_length, self.x +
                 piece_side_length - 1, self.y + piece_side_length)  # Bottom side shadow
            stroke(piece_shadow_light)
            # Left bright
            line(self.x + 2, self.y - 1, self.x + 2,
                 self.y + piece_side_length)
            # Upper bright
            line(self.x + 2, self.y + 1, self.x +
                 piece_side_length - 1, self.y + 1)

```

### python_code_3.txt
```python
''' Structural Game for 15 - Puzzle with different difficulty levels'''
from random import randint


class Puzzle:
    def __init__(self):
        self.items = {}
        self.position = None

    def main_frame(self):
        d = self.items
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[1], d[2], d[3], d[4]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[5], d[6], d[7], d[8]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[9], d[10], d[11], d[12]))
        print('+-----+-----+-----+-----+')
        print('|%s|%s|%s|%s|' % (d[13], d[14], d[15], d[16]))
        print('+-----+-----+-----+-----+')

    def format(self, ch):
        ch = ch.strip()
        if len(ch) == 1:
            return '  ' + ch + '  '
        elif len(ch) == 2:
            return '  ' + ch + ' '
        elif len(ch) == 0:
            return '     '

    def change(self, to):
        fro = self.position
        for a, b in self.items.items():
            if b == self.format(str(to)):
                to = a
                break
        self.items[fro], self.items[to] = self.items[to], self.items[fro]
        self.position = to

    def build_board(self, difficulty):
        for i in range(1, 17):
            self.items[i] = self.format(str(i))
        tmp = 0
        for a, b in self.items.items():
            if b == '  16 ':
                self.items[a] = '     '
                tmp = a
                break
        self.position = tmp
        if difficulty == 0:
            diff = 10
        elif difficulty == 1:
            diff = 50
        else:
            diff = 100
        for _ in range(diff):
            lst = self.valid_moves()
            lst1 = []
            for j in lst:
                lst1.append(int(j.strip()))
            self.change(lst1[randint(0, len(lst1)-1)])

    def valid_moves(self):
        pos = self.position
        if pos in [6, 7, 10, 11]:
            return self.items[pos - 4], self.items[pos - 1],\
                   self.items[pos + 1], self.items[pos + 4]
        elif pos in [5, 9]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos + 1]
        elif pos in [8, 12]:
            return self.items[pos - 4], self.items[pos + 4],\
                   self.items[pos - 1]
        elif pos in [2, 3]:
            return self.items[pos - 1], self.items[pos + 1], self.items[pos + 4]
        elif pos in [14, 15]:
            return self.items[pos - 1], self.items[pos + 1],\
                  self.items[pos - 4]
        elif pos == 1:
            return self.items[pos + 1], self.items[pos + 4]
        elif pos == 4:
            return self.items[pos - 1], self.items[pos + 4]
        elif pos == 13:
            return self.items[pos + 1], self.items[pos - 4]
        elif pos == 16:
            return self.items[pos - 1], self.items[pos - 4]

    def game_over(self):
        flag = False
        for a, b in self.items.items():
            if b == '     ':
                pass
            else:
                if a == int(b.strip()):
                    flag = True
                else:
                    flag = False
        return flag


g = Puzzle()
g.build_board(int(input('Enter the difficulty : 0 1 2\n2 '
                        '=> highest 0=> lowest\n')))
g.main_frame()
print('Enter 0 to exit')
while True:
    print('Hello user:\nTo change the position just enter the no. near it')
    lst = g.valid_moves()
    lst1 = []
    for i in lst:
        lst1.append(int(i.strip()))
        print(i.strip(), '\t', end='')
    print()
    x = int(input())
    if x == 0:
        break
    elif x not in lst1:
        print('Wrong move')
    else:
        g.change(x)
    g.main_frame()
    if g.game_over():
        print('You WON')
        break

```

### python_code_4.txt
```python
''' Python 3.6.5 code using Tkinter graphical user interface.''' 

from tkinter import *
from tkinter import messagebox
import random

# ************************************************

class Board:
    def __init__(self, playable=True):
        while True:
            # list of text for game squares:
            self.lot = [str(i) for i in range(1,16)] + ['']
            if not playable:
                break
            # list of text for game squares randomized:
            random.shuffle(self.lot)
            if self.is_solvable():
                break
            
        # game board is 2D array of game squares:
        self.bd = []
        i = 0
        for r in range(4):
            row = []
            for c in range(4):
                row.append(Square(r,c,self.lot[i]))
                i += 1
            self.bd.append(row)
            
    # How to check if an instance of a 15 puzzle
    # is solvable is explained here:
    # https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
    # I only coded for the case where N is even.
    def is_solvable(self):
        inv = self.get_inversions()
        odd = self.is_odd_row()
        if inv % 2 == 0 and odd:
            return True
        if inv % 2 == 1 and not odd:
            return True
        return False
        
    def get_inversions(self):
        cnt = 0
        for i, x in enumerate(self.lot[:-1]):
            if x != '':
                for y in self.lot[i+1:]:
                    if y != '' and int(x) > int(y):
                        cnt += 1
        return cnt

    # returns True if open square is in odd row from bottom:
    def is_odd_row(self):
        idx = self.lot.index('')
        return idx in [4,5,6,7,12,13,14,15]           

    # returns name, text, and button object at row & col:
    def get_item(self, r, c):
        return self.bd[r][c].get()

    def get_square(self, r, c):
        return self.bd[r][c]

    def game_won(self):
        goal = [str(i) for i in range(1,16)] + ['']
        i = 0
        for r in range(4):
            for c in range(4):
                nm, txt, btn = self.get_item(r,c)
                if txt != goal[i]:
                    return False
                i += 1
        return True
                
# ************************************************

class Square:       # ['btn00', '0', None]
    def __init__(self, row, col, txt):
        self.row = row
        self.col = col
        self.name = 'btn' + str(row) + str(col)
        self.txt = txt
        self.btn = None
        
    def get(self):
            return [self.name, self.txt, self.btn]

    def set_btn(self, btn):
        self.btn = btn

    def set_txt(self, txt):
        self.txt = txt

# ************************************************

class Game:
    def __init__(self, gw):
        self.window = gw

        # game data:
        self.bd = None
        self.playable = False

        # top frame:
        self.top_fr = Frame(gw,
                            width=600,
                            height=100,
                            bg='light green')
        self.top_fr.pack(fill=X)

        self.hdg = Label(self.top_fr,
                         text='  15 PUZZLE GAME  ',
                         font='arial 22 bold',
                         fg='Navy Blue',
                         bg='white')
        self.hdg.place(relx=0.5, rely=0.4,
                       anchor=CENTER)

        self.dir = Label(self.top_fr,
                 text="(Click 'New Game' to begin)",
                 font='arial 12 ',
                 fg='Navy Blue',
                 bg='light green')
        self.dir.place(relx=0.5, rely=0.8,
                       anchor=CENTER)

        self.play_btn = Button(self.top_fr,
                               text='New \nGame',
                               bd=5,
                               bg='PaleGreen4',
                               fg='White',
                               font='times 12 bold',
                               command=self.new_game)
        self.play_btn.place(relx=0.92, rely=0.5,
                       anchor=E)

        # bottom frame:
        self.btm_fr = Frame(gw,
                            width=600,
                            height=500,
                            bg='light steel blue')
        self.btm_fr.pack(fill=X)

        # board frame:
        self.bd_fr = Frame(self.btm_fr,
                           width=400+2,
                           height=400+2,
                           relief='solid',
                           bd=1,
                           bg='lemon chiffon')
        self.bd_fr.place(relx=0.5, rely=0.5,
                         anchor=CENTER)

        self.play_game()

# ************************************************

    def new_game(self):
        self.playable = True
        self.dir.config(text='(Click on a square to move it)')
        self.play_game()

    def play_game(self):
        # place squares on board:
        if self.playable:
            btn_state = 'normal'
        else:
            btn_state = 'disable'
        self.bd = Board(self.playable)               
        objh = 100  # widget height
        objw = 100  # widget width
        objx = 0    # x-position of widget in frame
        objy = 0    # y-position of widget in frame

        for r in range(4):
            for c in range(4):
                nm, txt, btn = self.bd.get_item(r,c)
                bg_color = 'RosyBrown1'
                if txt == '':
                    bg_color = 'White'           
                game_btn = Button(self.bd_fr,
                                  text=txt,
                                  relief='solid',
                                  bd=1,
                                  bg=bg_color,
                                  font='times 12 bold',
                                  state=btn_state,
                                  command=lambda x=nm: self.clicked(x))
                game_btn.place(x=objx, y=objy,
                               height=objh, width=objw)
                
                sq = self.bd.get_square(r,c)
                sq.set_btn(game_btn)
                
                objx = objx + objw
            objx = 0
            objy = objy + objh

    # processing when a square is clicked:
    def clicked(self, nm):
        r, c = int(nm[3]), int(nm[4])
        nm_fr, txt_fr, btn_fr = self.bd.get_item(r,c)
        
        # cannot 'move' open square to itself:
        if not txt_fr:
            messagebox.showerror(
                'Error Message',
                'Please select "square" to be moved')
            return

        # 'move' square to open square if 'adjacent' to it:            
        adjs = [(r-1,c), (r, c-1), (r, c+1), (r+1, c)]
        for x, y in adjs:
            if 0 <= x <= 3 and 0 <= y <= 3:
                nm_to, txt_to, btn_to = self.bd.get_item(x,y)
                if not txt_to:
                    sq = self.bd.get_square(x,y)
                    sq.set_txt(txt_fr)
                    sq = self.bd.get_square(r,c)
                    sq.set_txt(txt_to)
                    btn_to.config(text=txt_fr,
                                  bg='RosyBrown1')
                    btn_fr.config(text=txt_to,
                                  bg='White')
                    # check if game is won:              
                    if self.bd.game_won():
                        ans = messagebox.askquestion(
                            'You won!!!   Play again?')
                        if ans == 'no':
                            self.window.destroy()
                        else:
                            self.new_game()
                    return
                
        # cannot move 'non-adjacent' square to open square:
        messagebox.showerror(
            'Error Message',
            'Illigal move, Try again')
        return

# ************************************************

root = Tk()
root.title('15 Puzzle Game')
root.geometry('600x600+100+50')
root.resizable(False, False)
g = Game(root)
root.mainloop()

```

