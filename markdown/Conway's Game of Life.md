# Conway's Game of Life

## Task Link
[Rosetta Code - Conway's Game of Life](https://rosettacode.org/wiki/Conway%27s_Game_of_Life)

## Java Code
### java_code_1.txt
```java
public class GameOfLife{
	public static void main(String[] args){
		String[] dish= {
				"_#_",
				"_#_",
				"_#_",};
		int gens= 3;
		for(int i= 0;i < gens;i++){
			System.out.println("Generation " + i + ":");
			print(dish);
			dish= life(dish);
		}
	}

	public static String[] life(String[] dish){
		String[] newGen= new String[dish.length];
		for(int row= 0;row < dish.length;row++){//each row
			newGen[row]= "";
			for(int i= 0;i < dish[row].length();i++){//each char in the row
				String above= "";//neighbors above
				String same= "";//neighbors in the same row
				String below= "";//neighbors below
				if(i == 0){//all the way on the left
					//no one above if on the top row
					//otherwise grab the neighbors from above
					above= (row == 0) ? null : dish[row - 1].substring(i,
									i + 2);
					same= dish[row].substring(i + 1, i + 2);
					//no one below if on the bottom row
					//otherwise grab the neighbors from below
					below= (row == dish.length - 1) ? null : dish[row + 1]
									.substring(i, i + 2);
				}else if(i == dish[row].length() - 1){//right
					//no one above if on the top row
					//otherwise grab the neighbors from above
					above= (row == 0) ? null : dish[row - 1].substring(i - 1,
									i + 1);
					same= dish[row].substring(i - 1, i);
					//no one below if on the bottom row
					//otherwise grab the neighbors from below
					below= (row == dish.length - 1) ? null : dish[row + 1]
									.substring(i - 1, i + 1);
				}else{//anywhere else
					//no one above if on the top row
					//otherwise grab the neighbors from above
					above= (row == 0) ? null : dish[row - 1].substring(i - 1,
									i + 2);
					same= dish[row].substring(i - 1, i)
									+ dish[row].substring(i + 1, i + 2);
					//no one below if on the bottom row
					//otherwise grab the neighbors from below
					below= (row == dish.length - 1) ? null : dish[row + 1]
									.substring(i - 1, i + 2);
				}
				int neighbors= getNeighbors(above, same, below);
				if(neighbors < 2 || neighbors > 3){
					newGen[row]+= "_";//<2 or >3 neighbors -> die
				}else if(neighbors == 3){
					newGen[row]+= "#";//3 neighbors -> spawn/live
				}else{
					newGen[row]+= dish[row].charAt(i);//2 neighbors -> stay
				}
			}
		}
		return newGen;
	}

	public static int getNeighbors(String above, String same, String below){
		int ans= 0;
		if(above != null){//no one above
			for(char x: above.toCharArray()){//each neighbor from above
				if(x == '#') ans++;//count it if someone is here
			}
		}
		for(char x: same.toCharArray()){//two on either side
			if(x == '#') ans++;//count it if someone is here
		}
		if(below != null){//no one below
			for(char x: below.toCharArray()){//each neighbor below
				if(x == '#') ans++;//count it if someone is here
			}
		}
		return ans;
	}

	public static void print(String[] dish){
		for(String s: dish){
			System.out.println(s);
		}
	}
}

```

### java_code_2.txt
```java
//package conway;

import java.util.*;
import java.io.*;

public class GameOfLife 
{
	//Set grid size
	int l=20,b=60;
	public static void main(String[] args)
	{
		
		GameOfLife now=new GameOfLife();
		now.setGame();
	}
	void setGame()
	{
		char[][] config=new char[l][b];
		startGame(config,l,b);
	}
	void startGame(char[][] mat,int l, int b)
	{
		Scanner s=new Scanner(System.in);
		String ch="";
		float per=0;
		while(!ch.equals("y"))
		{
			per=setConfig(mat);
			//setCustomConfig(mat,"GOLglidergun.txt");
			display2D(mat);
			System.out.println((per*100)+"% of grid filled.");
			System.out.println("Begin? y/n");
			ch=s.nextLine();
		}
		while(!ch.equals("x"))
		{
			mat=transform(mat,l,b);
			display2D(mat);
			
			System.out.println("Ctrl+Z to stop.");
			
			try
			{
				Thread.sleep(100);
			}
			catch(Exception e)
			{
				System.out.println("Something went horribly wrong.");
			}
			
			//ch=s.nextLine();
		}
		s.close();
		System.out.println("Game Over");
	}
	
	char[][] transform(char[][] mat,int l, int b)
	{
		
		char[][] newmat=new char[l][b];
		for(int i=0;i<l;i++)
			for(int j=0;j<b;j++)
				newmat[i][j]=flip(mat,i,j);
		return newmat;
	}
	char flip(char[][] mat,int i, int j)
	{
		int count=around(mat,i,j);
		if(mat[i][j]=='*')
		{
			if(count<2||count>3)
				return '_';
			return '*';
		}
		else
		{
			if(count==3)
				return '*';
			return '_';
		}
	}
	int around(char[][] mat, int i, int j)
	{
		int count=0;
		for(int x=i-1;x<=i+1;x++)
			for(int y=j-1;y<=j+1;y++)
			{
				if(x==i&&y==j)
					continue;
				count+=eval(mat,x,y);
			}
		return count;
	}
	int eval(char[][] mat, int i, int j)
	{
		if(i<0||j<0||i==l||j==b)
			return 0;
		if(mat[i][j]=='*')
			return 1;
		return 0;
	}
	
	float setCustomConfig(char[][] arr,String infile)
	{
		try
		{
			BufferedReader br=new BufferedReader(new FileReader(infile));
			String line;
			for(int i=0;i<arr.length;i++)
			{
				line=br.readLine();
				for(int j=0;j<arr[0].length;j++)
					arr[i][j]=line.charAt(j);
			}
			br.close();
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
		}
		return 0;
	}
	
	float setConfig(char[][] arr)
	{
		//Enter percentage of grid to be filled.
		float per=0.10f;//(float)Math.random();
		for(int i=0;i<arr.length;i++)
			setConfig1D(arr[i],per);
		return per;
	}
	void setConfig1D(char[] arr,float per)
	{
		for(int i=0;i<arr.length;i++)
		{
			if(Math.random()<per)
				arr[i]='*';
			else
				arr[i]='_';
		}
	}
	void display2D(char[][] arr)
	{
		for(int i=0;i<arr.length;i++)
			display1D(arr[i]);
		System.out.println();
	}
	void display1D(char[] arr)
	{
		for(int i=0;i<arr.length;i++)
			System.out.print(arr[i]);
		System.out.println();
	}
}

```

### java_code_3.txt
```java
import static java.util.List.of;

class GameOfLife {

   boolean[][] board = new boolean[3][3];

   GameOfLife() {}

   GameOfLife(String[] board) {
      set((i, j, s) -> board[i].charAt(j * 2) == '■');
   }

   void set(Setter setter) {
      for (int i = 0; i < board.length; i++) {
         for (int j = 0; j < board[i].length; j++) {
            board[i][j] = setter.set(i, j, board[i][j]);
         }
      }
   }

   void get(Getter getter) {
      set((i, j, s) -> {
         getter.get(i, j, s);
         return s;
      });
   }

   int countNeighbors(int i, int j) {
      var counter = new Getter() {
         int count;

         @Override
         public void get(int li, int lj, boolean state) {
            if (distance(i, j, li, lj) == 1 && board[li][lj])
               count++;
         }
      };
      get(counter);
      return counter.count;
   }

   int distance(int i, int j, int li, int lj) {
      return Math.max(
           Math.abs(i - li),
           Math.abs(j - lj));
   }

   GameOfLife makeNextGeneration() {
      var n = new GameOfLife();
      n.set((i, j, s) -> {
         var alive = board[i][j];
         int c = countNeighbors(i, j);
         if (alive) {
            return c == 2 || c == 3;
         } else {
            return c == 3;
         }
      });
      return n;
   }

   void print() {
      get((i, j, s) -> {
         if (j == 0)
            System.out.println();
         System.out.print(s ? "■ " : "□ ");
      });
   }

   interface Setter {
      boolean set(int i, int j, boolean state);
   }

   interface Getter {
      void get(int i, int j, boolean state);
   }

   public static void main(String[] args) {
      String[] board = {
           "□ ■ □ ",
           "□ ■ □ ",
           "□ ■ □ ",
      };
      var gol = new GameOfLife(board);
      for (var generation : of(0, 1, 2)) {
         gol.print();
         System.out.println("\n");
         gol = gol.makeNextGeneration();
      }
   }

}

```

### java_code_4.txt
```java
boolean play = true;
int cellSize = 10;
int cols, rows;
int lastCell = 0;
int sample = 10;
// Game of life board
int[][] grid;

void setup() {
  size(800, 500);
  noStroke();
  // Calculate cols, rows and init array
  cols = width/cellSize;
  rows = height/cellSize;
  grid = new int[cols][rows];
  init(-1); // randomized start

  println("Press 'space' to start/stop");
  println("'e' to clear all cells");
  println("'b' demonstrate 'blinker'");
  println("'g' demonstrate glider");
  println("'r' to randomize grid");
  println("'+'  and '-' to change speed");

}

void draw() {
  background(0);

  for ( int i = 0; i < cols; i++) {
    for ( int j = 0; j < rows; j++) {
      if ((grid[i][j] == 1)) fill(255);
      else fill(0); 
      rect(i*cellSize, j*cellSize, cellSize, cellSize);
    }
  }
  if (play && frameCount%sample==0 && !mousePressed) {
    generate();
  }
}

void generate() {
  int[][] nextGrid = new int[cols][rows];
  for (int x = 0; x < cols; x++) {
    for (int y = 0; y < rows; y++) {
      int ngbs = countNgbs(x, y);
      // the classic Conway rules
      if      ((grid[x][y] == 1) && (ngbs <  2)) nextGrid[x][y] = 0; // solitude
      else if ((grid[x][y] == 1) && (ngbs >  3)) nextGrid[x][y] = 0; // crowded 
      else if ((grid[x][y] == 0) && (ngbs == 3)) nextGrid[x][y] = 1; // cell born
      else                              nextGrid[x][y] = grid[x][y]; // keep
    }
  }
  grid = nextGrid;
}

int countNgbs(int x, int y) {
  int ngbCount = 0;
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      // 'united' borders
      ngbCount += grid[(x+i+cols)%cols][(y+j+rows)%rows];
    }
  }
  // cell taken out of count
  ngbCount -= grid[x][y];
  return ngbCount;
}

void init(int option) {
  int state;
  for (int x = 0; x < cols; x++) {
    for (int y = 0; y < rows; y++) {
      if (option == -1) {
        state = int(random(2));
      } else {
        state = option;
      }
      grid[x][y] = state;
    }
  }
}

void keyReleased() {
  if (key == 'r') {
    init(-1); // randomize grid
  }
  if (key == 'e') {
    init(0); // empty grid
  }
  if (key == 'g') {
    int glider[][] = {
      {0, 1, 0}, 
      {0, 0, 1}, 
      {1, 1, 1}};
    setNine(10, 10, glider);
  }
  if (key == 'b') {
    int blinker[][] = {
      {0, 1, 0}, 
      {0, 1, 0}, 
      {0, 1, 0}};
    setNine(10, 10, blinker);
  }
  if (key == ' ') {
    play = !play;
  }
  if (key == '+' || key == '=') {
    sample=max(sample-1, 1);
  }
  if (key == '-') {
    sample++;
  }
}

void setNine(int x, int y, int nine[][]) {
  for (int i = 0; i <= 2; i++) {
    for (int j = 0; j <= 2; j++) {
      grid[(x+i+cols)%cols][(y+j+rows)%rows] = nine[i][j];
    }
  }
}

void mousePressed() {
  paint();
}
void mouseDragged() {
  paint();
}

void paint() {
  int x = mouseX/cellSize;
  int y = mouseY/cellSize;
  int p = y*cols + x;
  if (p!=lastCell) {
    lastCell=p;
    int states[] = {1, 0};
    grid[x][y] = states[grid[x][y]]; // invert
  }
}

```

## Python Code
### python_code_1.txt
```python
cell_size = 10
sample = 10 
play = False   # simulation is running
last_cell = 0

def setup():
    global grid, next_grid, rows, cols
    size(800, 500)

    rows = height / cell_size
    cols = width / cell_size
    grid = empty_grid()
    next_grid = empty_grid()
    randomize_grid()

    println("Press 'space' to start/stop")
    println("'e' to clear all cells")
    println("'b' demonstrate 'blinker'")
    println("'g' demonstrate glider")
    println("'r' to randomize grid")
    println("'+' and '-' to change speed")

def draw():
    background(0)
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y = j * cell_size
            current_state = grid[i][j]
            fill(255)
            noStroke()
            if current_state:
                rect(x, y, cell_size, cell_size)
            if play:
                ngbs_alive = calc_ngbs_alive(i, j)
                result = rule(current_state, ngbs_alive)
                next_grid[i][j] = result
                
    if play and frameCount % sample == 0 and not mousePressed:
        step()

def rule(current, ngbs):
    """ classic Conway's Game of Life rule """
    if ngbs < 2 or ngbs > 3:
        return 0  # dies / dead
    elif ngbs == 3:
        return 1  # born / alive
    else:
        return current  # stays the same (ngbs == 2)

def calc_ngbs_alive(i, j):
    NEIGHBOURS = ((-1, 00), (01, 00),  # a tuple describing the neighbourhood of a cell
                  (-1, -1), (00, -1),
                  (01, -1), (-1, 01),
                  (00, 01), (01, 01))
    alive = 0
    for iv, jv in NEIGHBOURS:
        alive += grid[(i + iv) % cols][(j + jv) % rows]
    return alive

def empty_grid():
    grid = []
    for _ in range(cols):
        grid.append([0] * rows)
    return grid

def randomize_grid():
    from random import choice
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = choice((0, 1))

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def keyReleased():
    global grid, play, sample
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == "g":
         grid[10][10:13] = [0, 1, 0]       
         grid[11][10:13] = [0, 0, 1]       
         grid[12][10:13] = [1, 1, 1]       
    if key == "b":
         grid[10][10:13] = [0, 1, 0]       
         grid[11][10:13] = [0, 1, 0]       
         grid[12][10:13] = [0, 1, 0]               
    if key == " ":
        play = not play 
    if  str(key) in '+=':
        sample = max(sample - 1, 1);
    if key == '-':
        sample += 1

def mousePressed():
    paint()
    
def mouseDragged():
    paint()

def paint():
    global last_cell
    i, j = mouseX // cell_size, mouseY // cell_size
    p = j * cols + i
    if p != last_cell:
        last_cell = p
        grid[i][j] = (1, 0)[grid[i][j]]

```

### python_code_2.txt
```python
import random
from collections import defaultdict

printdead, printlive = '-#'
maxgenerations = 3
cellcount = 3,3
celltable = defaultdict(int, {
 (1, 2): 1,
 (1, 3): 1,
 (0, 3): 1,
 } ) # Only need to populate with the keys leading to life

##
## Start States
##
# blinker
u = universe = defaultdict(int)
u[(1,0)], u[(1,1)], u[(1,2)] = 1,1,1

## toad
#u = universe = defaultdict(int)
#u[(5,5)], u[(5,6)], u[(5,7)] = 1,1,1
#u[(6,6)], u[(6,7)], u[(6,8)] = 1,1,1

## glider
#u = universe = defaultdict(int)
#maxgenerations = 16
#u[(5,5)], u[(5,6)], u[(5,7)] = 1,1,1
#u[(6,5)] = 1
#u[(7,6)] = 1

## random start
#universe = defaultdict(int, 
#                       # array of random start values
#                       ( ((row, col), random.choice((0,1)))
#                         for col in range(cellcount[0])
#                         for row in range(cellcount[1])
#                       ) )  # returns 0 for out of bounds

for i in range(maxgenerations):
    print("\nGeneration %3i:" % ( i, ))
    for row in range(cellcount[1]):
        print("  ", ''.join(str(universe[(row,col)])
                            for col in range(cellcount[0])).replace(
                                '0', printdead).replace('1', printlive))
    nextgeneration = defaultdict(int)
    for row in range(cellcount[1]):
        for col in range(cellcount[0]):
            nextgeneration[(row,col)] = celltable[
                ( universe[(row,col)],
                  -universe[(row,col)] + sum(universe[(r,c)]
                                             for r in range(row-1,row+2)
                                             for c in range(col-1, col+2) )
                ) ]
    universe = nextgeneration

```

### python_code_3.txt
```python
from collections import Counter

def life(world, N):
    "Play Conway's game of life for N generations from initial world."
    for g in range(N+1):
        display(world, g)
        counts = Counter(n for c in world for n in offset(neighboring_cells, c))
        world = {c for c in counts 
                if counts[c] == 3 or (counts[c] == 2 and c in world)}

neighboring_cells = [(-1, -1), (-1, 0), (-1, 1), 
                     ( 0, -1),          ( 0, 1), 
                     ( 1, -1), ( 1, 0), ( 1, 1)]

def offset(cells, delta):
    "Slide/offset all the cells by delta, a (dx, dy) vector."
    (dx, dy) = delta
    return {(x+dx, y+dy) for (x, y) in cells}

def display(world, g):
    "Display the world as a grid of characters."
    print('          GENERATION {}:'.format(g))
    Xs, Ys = zip(*world)
    Xrange = range(min(Xs), max(Xs)+1)
    for y in range(min(Ys), max(Ys)+1):
        print(''.join('#' if (x, y) in world else '.'
                      for x in Xrange))

blinker = {(1, 0), (1, 1), (1, 2)}
block   = {(0, 0), (1, 1), (0, 1), (1, 0)}
toad    = {(1, 2), (0, 1), (0, 0), (0, 2), (1, 3), (1, 1)}
glider  = {(0, 1), (1, 0), (0, 0), (0, 2), (2, 1)}
world   = (block | offset(blinker, (5, 2)) | offset(glider, (15, 5)) | offset(toad, (25, 5))
           | {(18, 2), (19, 2), (20, 2), (21, 2)} | offset(block, (35, 7)))


life(world, 5)

```

### python_code_4.txt
```python
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
#import time

def conway_life(len=10, wid=10, gen=5):
     
    curr_gen = DataFrame(np.random.randint(0, 2, (len+2, wid+2)),
                         index = range(len+2), 
                         columns = range(wid+2))
    curr_gen[0] = 0
    curr_gen[wid+1] = 0
    curr_gen[0: 1] = 0
    curr_gen[len+1: len+2] = 0    
    
    for i in range(gen):
        
        fig, ax = plt.subplots()
        draw = curr_gen[1:len+1].drop([0, wid+1], axis=1)
        # 画图
        
        image = draw
        ax.imshow(image, cmap=plt.cm.cool, interpolation='nearest')
        ax.set_title("Conway's game of life.")
        
        # Move left and bottom spines outward by 10 points
        ax.spines['left'].set_position(('outward', 10))
        ax.spines['bottom'].set_position(('outward', 10))
        # Hide the right and top spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

        plt.show()
        # time.sleep(1)         
        
        
        # 初始化空表
        next_gen = DataFrame(np.random.randint(0, 1, (len+2, wid+2)),
                             index = range(len+2), 
                             columns = range(wid+2))
        
        
        # 生成下一代
        for x in range(1, wid+1):
            for y in range(1, len+1):
                env = (curr_gen[x-1][y-1] + curr_gen[x][y-1] + 
                       curr_gen[x+1][y-1]+ curr_gen[x-1][y] + 
                       curr_gen[x+1][y] + curr_gen[x-1][y+1] + 
                       curr_gen[x][y+1] + curr_gen[x+1][y+1])
            
                if (not curr_gen[x][y] and env == 3):
                    next_gen[x][y] = 1
                if (curr_gen[x][y] and env in (2, 3)):
                    next_gen[x][y] = 1
                
        curr_gen = next_gen 
         

conway_life()

```

