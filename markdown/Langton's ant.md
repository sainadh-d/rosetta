# Langton's ant

## Task Link
[Rosetta Code - Langton's ant](https://rosettacode.org/wiki/Langton%27s_ant)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Langton extends JFrame{
	private JPanel planePanel;
	private static final int ZOOM = 4;
	
	public Langton(final boolean[][] plane){
		planePanel = new JPanel(){
			@Override
			public void paint(Graphics g) {
				for(int y = 0; y < plane.length;y++){
					for(int x = 0; x < plane[0].length;x++){
						g.setColor(plane[y][x] ? Color.BLACK : Color.WHITE);
						g.fillRect(x * ZOOM, y * ZOOM, ZOOM, ZOOM);
					}
				}
				//mark the starting point
				g.setColor(Color.GREEN);
				g.fillRect(plane[0].length / 2 * ZOOM,
				           plane.length / 2 * ZOOM, ZOOM/2, ZOOM/2);
			}
		};
		planePanel.setSize(plane[0].length - 1, plane.length - 1);
		add(planePanel);
		setSize(ZOOM * plane[0].length, ZOOM * plane.length + 30);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public static void main(String[] args){
		new Langton(runAnt(100, 100));
	}

	private static boolean[][] runAnt(int height, int width){
		boolean[][] plane = new boolean[height][width];
		int antX = width/2, antY = height/2;//start in the middle-ish
		int xChange = 0, yChange = -1; //start moving up
		while(antX < width && antY < height && antX >= 0 && antY >= 0){
			if(plane[antY][antX]){
				//turn left
				if(xChange == 0){ //if moving up or down
					xChange = yChange;
					yChange = 0;
				}else{ //if moving left or right
					yChange = -xChange;
					xChange = 0;
				}
			}else{
				//turn right
				if(xChange == 0){ //if moving up or down
					xChange = -yChange;
					yChange = 0;
				}else{ //if moving left or right
					yChange = xChange;
					xChange = 0;
				}
			}
			plane[antY][antX] = !plane[antY][antX];
			antX += xChange;
			antY += yChange;
		}
		return plane;
	}
}

```

## Python Code
### python_code_1.txt
```python
"""
we use the following conventions:
directions 0: up, 1: left, 2: down: 3: right

pixel white: True, black: False

turn right: True, left: False
"""

# number of iteration steps per frame
# set this to 1 to see a slow animation of each
# step or to 10 or 100 for a faster animation

STEP = 100
count = 0

def setup():
    global x, y, direction

    # 100x100 is large enough to show the
    # corridor after about 10000 cycles
    size(100, 100, P2D)

    background(255)
    x = width / 2
    y = height / 2
    direction = 0

def draw():
    global count
    for i in range(STEP):
        count += 1
        pix = get(x, y) != -1 # white =-1
        setBool(x, y, pix)

        turn(pix)
        move()

        if (x < 0 or y < 0 or x >= width or y >= height):
            println("finished")
            noLoop()
            break

    if count % 1000 == 0:
        println("iteration {}".format(count))

def move():
    global x, y
    if direction == 0:
        y -= 1
    elif direction == 1:
        x -= 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x += 1

def turn(rightleft):
    global direction
    direction += 1 if rightleft else -1
    if direction == -1:
        direction = 3
    if direction == 4:
        direction = 0

def setBool(x, y, white):
    set(x, y, -1 if white else 0)

```

### python_code_2.txt
```python
"""Langton's ant implementation."""
from enum import Enum, IntEnum


class Dir(IntEnum):
    """Possible directions."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Color(Enum):
    """Possible colors."""

    WHITE = " "
    BLACK = "#"


def invert_color(grid, x, y):
    """Invert the color of grid at x, y coordinate."""
    if grid[y][x] == Color.BLACK:
        grid[y][x] = Color.WHITE
    else:
        grid[y][x] = Color.BLACK


def next_direction(grid, x, y, direction):
    """Compute next direction according to current position and direction."""
    if grid[y][x] == Color.BLACK:
        turn_right = False
    else:
        turn_right = True
    direction_index = direction.value
    if turn_right:
        direction_index = (direction_index + 1) % 4
    else:
        direction_index = (direction_index - 1) % 4
    directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
    direction = directions[direction_index]
    return direction


def next_position(x, y, direction):
    """Compute next position according to direction."""
    if direction == Dir.UP:
        y -= 1
    elif direction == Dir.RIGHT:
        x -= 1
    elif direction == Dir.DOWN:
        y += 1
    elif direction == Dir.LEFT:
        x += 1
    return x, y


def print_grid(grid):
    """Display grid."""
    print(80 * "#")
    print("\n".join("".join(v.value for v in row) for row in grid))


def ant(width, height, max_nb_steps):
    """Langton's ant."""
    grid = [[Color.WHITE] * width for _ in range(height)]
    x = width // 2
    y = height // 2
    direction = Dir.UP

    i = 0
    while i < max_nb_steps and 0 <= x < width and 0 <= y < height:
        invert_color(grid, x, y)
        direction = next_direction(grid, x, y, direction)
        x, y = next_position(x, y, direction)
        print_grid(grid)
        i += 1


if __name__ == "__main__":
    ant(width=75, height=52, max_nb_steps=12000)

```

