# Maze generation

## Task Link
[Rosetta Code - Maze generation](https://rosettacode.org/wiki/Maze_generation)

## Java Code
### java_code_1.txt
```java
package org.rosettacode;

import java.util.Collections;
import java.util.Arrays;

/*
 * recursive backtracking algorithm
 * shamelessly borrowed from the ruby at
 * http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking
 */
public class MazeGenerator {
	private final int x;
	private final int y;
	private final int[][] maze;

	public MazeGenerator(int x, int y) {
		this.x = x;
		this.y = y;
		maze = new int[this.x][this.y];
		generateMaze(0, 0);
	}

	public void display() {
		for (int i = 0; i < y; i++) {
			// draw the north edge
			for (int j = 0; j < x; j++) {
				System.out.print((maze[j][i] & 1) == 0 ? "+---" : "+   ");
			}
			System.out.println("+");
			// draw the west edge
			for (int j = 0; j < x; j++) {
				System.out.print((maze[j][i] & 8) == 0 ? "|   " : "    ");
			}
			System.out.println("|");
		}
		// draw the bottom line
		for (int j = 0; j < x; j++) {
			System.out.print("+---");
		}
		System.out.println("+");
	}

	private void generateMaze(int cx, int cy) {
		DIR[] dirs = DIR.values();
		Collections.shuffle(Arrays.asList(dirs));
		for (DIR dir : dirs) {
			int nx = cx + dir.dx;
			int ny = cy + dir.dy;
			if (between(nx, x) && between(ny, y)
					&& (maze[nx][ny] == 0)) {
				maze[cx][cy] |= dir.bit;
				maze[nx][ny] |= dir.opposite.bit;
				generateMaze(nx, ny);
			}
		}
	}

	private static boolean between(int v, int upper) {
		return (v >= 0) && (v < upper);
	}

	private enum DIR {
		N(1, 0, -1), S(2, 0, 1), E(4, 1, 0), W(8, -1, 0);
		private final int bit;
		private final int dx;
		private final int dy;
		private DIR opposite;

		// use the static initializer to resolve forward references
		static {
			N.opposite = S;
			S.opposite = N;
			E.opposite = W;
			W.opposite = E;
		}

		private DIR(int bit, int dx, int dy) {
			this.bit = bit;
			this.dx = dx;
			this.dy = dy;
		}
	};

	public static void main(String[] args) {
		int x = args.length >= 1 ? (Integer.parseInt(args[0])) : 8;
		int y = args.length == 2 ? (Integer.parseInt(args[1])) : 8;
		MazeGenerator maze = new MazeGenerator(x, y);
		maze.display();
	}

}

```

### java_code_2.txt
```java
int g_size = 10;
color background_color = color (80, 80, 220);
color runner = color (255, 50, 50);
color visited_color = color(220, 240, 240);
color done_color = color (100, 160, 250);
int c_size;

Cell[][] cell;
ArrayList<Cell> done = new ArrayList<Cell>();
ArrayList<Cell> visit = new ArrayList<Cell>();
Cell run_cell;

void setup() {
  size(600, 600);
  frameRate(20);
  smooth(4);
  strokeCap(ROUND);
  c_size = max(width/g_size, height/g_size);
  cell = new Cell[g_size][g_size];
  for (int i = 0; i < g_size; i++) {
    for (int j = 0; j < g_size; j++) {
      cell[i][j] = new Cell(i, j);
    }
  }
  for (int i = 0; i < g_size; i++) {
    for (int j = 0; j < g_size; j++) {
      cell[i][j].add_neighbor();
    }
  }
  run_cell = cell[0][0];
  visit.add(run_cell);
}

void draw() {
  background(background_color);
  for (int i = 0; i < g_size; i++) {
    for (int j = 0; j < g_size; j++) {
      cell[i][j].draw_cell();
      cell[i][j].draw_wall();
    }
  }
  if (visit.size() < g_size*g_size) {
    if (run_cell.check_sides()) {
      Cell chosen = run_cell.pick_neighbor();
      done.add(run_cell);
      run_cell.stacked = true;
      if (chosen.i - run_cell.i == 1) {
        run_cell.wall[1] = false;
        chosen.wall[3] = false;
      } else if (chosen.i - run_cell.i == -1) {
        run_cell.wall[3] = false;
        chosen.wall[1] = false;
      } else if (chosen.j - run_cell.j == 1) {
        run_cell.wall[2] = false;
        chosen.wall[0] = false;
      } else {
        run_cell.wall[0] = false;
        chosen.wall[2] = false;
      }
      run_cell.current = false;
      run_cell = chosen;
      run_cell.current = true;
      run_cell.visited = true;
    } else if (done.size()>0) {
      run_cell.current = false;
      run_cell = done.remove(done.size()-1);
      run_cell.stacked = false;
      run_cell.current = true;
    }
  }
}

class Cell {
  ArrayList<Cell> neighbor;
  boolean visited, stacked, current;
  boolean[] wall;
  int i, j;
  
  Cell(int _i, int _j) {
    i = _i;
    j = _j;
    wall = new boolean[]{true,true,true,true}; 
  }
  
  Cell pick_neighbor() {
    ArrayList<Cell> unvisited = new ArrayList<Cell>();
     for(int i = 0;  i < neighbor.size(); i++){
      Cell nb = neighbor.get(i);
     if(nb.visited == false) unvisited.add(nb);
    }        
    return unvisited.get(floor(random(unvisited.size())));
  }
  
  void add_neighbor() {
    neighbor = new ArrayList<Cell>();
    if(i>0){neighbor.add(cell[i-1][j]);}
    if(i<g_size-1){neighbor.add(cell[i+1][j]);}
    if(j>0){neighbor.add(cell[i][j-1]);}
    if(j<g_size-1){neighbor.add(cell[i][j+1]);}
  }
  
    boolean check_sides() {
      for(int i = 0;  i < neighbor.size(); i++){
      Cell nb = neighbor.get(i);
     if(!nb.visited) return true;
    } 
    return false;
  }
  
  void draw_cell() {
    noStroke();
    noFill();
    if(current) fill(runner);
    else if(stacked) fill(done_color);
    else if(visited) fill(visited_color);
    rect(j*c_size,i*c_size,c_size,c_size);
  }
  
  void draw_wall() {
    stroke(0);
    strokeWeight(5);
    if(wall[0]) line(j*c_size, i*c_size, j*c_size, (i+1)* c_size);
    if(wall[1]) line(j*c_size, (i+1)*c_size, (j+1)*c_size, (i+1)*c_size);
    if(wall[2]) line((j+1)*c_size, (i+1)*c_size, (j+1)*c_size, i*c_size);
    if(wall[3]) line((j+1)*c_size, i*c_size, j*c_size, i*c_size);
  }
}

```

## Python Code
### python_code_1.txt
```python
g_size = 10
background_color = color(80, 80, 220)
runner = color(255, 50, 50)
visited_color = color(220, 240, 240)
done_color = color(100, 160, 250)

def setup():
    global cell, done, visit, run_cell, c_size
    size(600, 600)
    frameRate(20)
    smooth(4)
    strokeCap(ROUND)
    c_size = max(width / g_size, height / g_size)
    cell = [[None] * g_size for _ in range(g_size)]
    
    for i in range(g_size):
        for j in range(g_size):
            cell[i][j] = Cell(i, j)

    for i in range(g_size):
        for j in range(g_size):
            cell[i][j].add_neighbor()

    run_cell = cell[0][0]
    visit, done = [], []
    visit.append(run_cell)


def draw():
    global run_cell
    
    background(background_color)
    
    for i in range(g_size):
        for j in range(g_size):
            cell[i][j].draw_cell()
            cell[i][j].draw_wall()

    if len(visit) < g_size * g_size:
        if run_cell.check_sides():
            chosen = run_cell.pick_neighbor()
            done.append(run_cell)
            run_cell.stacked = True
            if chosen.i - run_cell.i == 1:
                run_cell.wall[1] = False
                chosen.wall[3] = False
            elif chosen.i - run_cell.i == -1:
                run_cell.wall[3] = False
                chosen.wall[1] = False
            elif chosen.j - run_cell.j == 1:
                run_cell.wall[2] = False
                chosen.wall[0] = False
            else:
                run_cell.wall[0] = False
                chosen.wall[2] = False
            run_cell.current = False
            run_cell = chosen
            run_cell.current = True
            run_cell.visited = True
        elif done:
            run_cell.current = False
            run_cell = done.pop()
            run_cell.stacked = False
            run_cell.current = True


class Cell:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.wall = [True, True, True, True]
        self.visited = False
        self.stacked = False
        self.current = False

    def pick_neighbor(self):
        from random import choice
        unvisited = [nb for nb in self.neighbor
                          if nb.visited == False]
        return choice(unvisited)

    def add_neighbor(self):
        i, j = self.i, self.j
        neighbor = []
        if i > 0:
            neighbor.append(cell[i - 1][j])
        if i < g_size - 1:
            neighbor.append(cell[i + 1][j])
        if j > 0:
            neighbor.append(cell[i][j - 1])
        if j < g_size - 1:
            neighbor.append(cell[i][j + 1])
        self.neighbor = neighbor

    def check_sides(self):
        for nb in self.neighbor:
            if not nb.visited:
                return True
        return False

    def draw_cell(self):
        s = c_size
        noStroke()
        noFill()
        if self.current:
            fill(runner)
        elif self.stacked:
            fill(done_color)
        elif self.visited:
            fill(visited_color)
        rect(self.j * s, self.i * s, s, s)

    def draw_wall(self):
        i, j = self.i, self.j
        wall = self.wall
        stroke(0)
        strokeWeight(5)
        if wall[0]: line(j * c_size, i * c_size, j * c_size, (i + 1) * c_size)
        if wall[1]: line(j * c_size, (i + 1) * c_size, (j + 1) * c_size, (i + 1) * c_size)
        if wall[2]: line((j + 1) * c_size, (i + 1) * c_size, (j + 1) * c_size, i * c_size)
        if wall[3]: line((j + 1) * c_size, i * c_size, j * c_size, i * c_size)

```

### python_code_2.txt
```python
from random import shuffle, randrange

def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

if __name__ == '__main__':
    print(make_maze())

```

