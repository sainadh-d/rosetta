# Forest fire

## Task Link
[Rosetta Code - Forest fire](https://rosettacode.org/wiki/Forest_fire)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Fire {
	private static final char BURNING = 'w'; //w looks like fire, right?
	private static final char TREE = 'T';
	private static final char EMPTY = '.';
	private static final double F = 0.2;
	private static final double P = 0.4;
	private static final double TREE_PROB = 0.5;
	
	private static List<String> process(List<String> land){
		List<String> newLand = new LinkedList<String>();
		for(int i = 0; i < land.size(); i++){
			String rowAbove, thisRow = land.get(i), rowBelow;
			if(i == 0){//first row
				rowAbove = null;
				rowBelow = land.get(i + 1);
			}else if(i == land.size() - 1){//last row
				rowBelow = null;
				rowAbove = land.get(i - 1);
			}else{//middle
				rowBelow = land.get(i + 1);
				rowAbove = land.get(i - 1);
			}
			newLand.add(processRows(rowAbove, thisRow, rowBelow));
		}
		return newLand;
	}

	private static String processRows(String rowAbove, String thisRow,
			String rowBelow){
		String newRow = "";
		for(int i = 0; i < thisRow.length();i++){
			switch(thisRow.charAt(i)){
			case BURNING:
				newRow+= EMPTY;
				break;
			case EMPTY:
				newRow+= Math.random() < P ? TREE : EMPTY;
				break;
			case TREE:
				String neighbors = "";
				if(i == 0){//first char
					neighbors+= rowAbove == null ? "" : rowAbove.substring(i, i + 2);
					neighbors+= thisRow.charAt(i + 1);
					neighbors+= rowBelow == null ? "" : rowBelow.substring(i, i + 2);
					if(neighbors.contains(Character.toString(BURNING))){
						newRow+= BURNING;
						break;
					}
				}else if(i == thisRow.length() - 1){//last char
					neighbors+= rowAbove == null ? "" : rowAbove.substring(i - 1, i + 1);
					neighbors+= thisRow.charAt(i - 1);
					neighbors+= rowBelow == null ? "" : rowBelow.substring(i - 1, i + 1);
					if(neighbors.contains(Character.toString(BURNING))){
						newRow+= BURNING;
						break;
					}
				}else{//middle
					neighbors+= rowAbove == null ? "" : rowAbove.substring(i - 1, i + 2);
					neighbors+= thisRow.charAt(i + 1);
					neighbors+= thisRow.charAt(i - 1);
					neighbors+= rowBelow == null ? "" : rowBelow.substring(i - 1, i + 2);
					if(neighbors.contains(Character.toString(BURNING))){
						newRow+= BURNING;
						break;
					}
				}
				newRow+= Math.random() < F ? BURNING : TREE;
			}
		}
		return newRow;
	}
	
	public static List<String> populate(int width, int height){
		List<String> land = new LinkedList<String>();
		for(;height > 0; height--){//height is just a copy anyway
			StringBuilder line = new StringBuilder(width);
			for(int i = width; i > 0; i--){
				line.append((Math.random() < TREE_PROB) ? TREE : EMPTY);
			}
			land.add(line.toString());
		}
		return land;
	}
	
	//process the land n times
	public static void processN(List<String> land, int n){
		for(int i = 0;i < n; i++){
			land = process(land);
		}
	}
	
	//process the land n times and print each step along the way
	public static void processNPrint(List<String> land, int n){
		for(int i = 0;i < n; i++){
			land = process(land);
			print(land);
		}
	}
	
	//print the land
	public static void print(List<String> land){
		for(String row: land){
			System.out.println(row);
		}
		System.out.println();
	}
	
	public static void main(String[] args){
		List<String> land = Arrays.asList(".TTT.T.T.TTTT.T",
				"T.T.T.TT..T.T..",
				"TT.TTTT...T.TT.",
				"TTT..TTTTT.T..T",
				".T.TTT....TT.TT",
				"...T..TTT.TT.T.",
				".TT.TT...TT..TT",
				".TT.T.T..T.T.T.",
				"..TTT.TT.T..T..",
				".T....T.....TTT",
				"T..TTT..T..T...",
				"TTT....TTTTTT.T",
				"......TwTTT...T",
				"..T....TTTTTTTT",
				".T.T.T....TT...");
		print(land);
		processNPrint(land, 10);
		
		System.out.println("Random land test:");
		
		land = populate(10, 10);
		print(land);
		processNPrint(land, 10);
	}
}

```

## Python Code
### python_code_1.txt
```python
'''
Forest-Fire Cellular automation
 See: http://en.wikipedia.org/wiki/Forest-fire_model
'''

L = 15
# d = 2 # Fixed
initial_trees = 0.55
p = 0.01
f = 0.001

try:
    raw_input
except:
    raw_input = input
    
import random


tree, burning, space = 'TB.'
hood = ((-1,-1), (-1,0), (-1,1),
        (0,-1),          (0, 1),
        (1,-1),  (1,0),  (1,1))

def initialise():
    grid = {(x,y): (tree if random.random()<= initial_trees else space)
            for x in range(L)
            for y in range(L) }
    return grid

def gprint(grid):
    txt = '\n'.join(''.join(grid[(x,y)] for x in range(L))
                    for y in range(L))
    print(txt)

def quickprint(grid):
    t = b = 0
    ll = L * L
    for x in range(L):
        for y in range(L):
            if grid[(x,y)] in (tree, burning):
                t += 1
                if grid[(x,y)] == burning:
                    b += 1
    print(('Of %6i cells, %6i are trees of which %6i are currently burning.'
          + ' (%6.3f%%, %6.3f%%)')
          % (ll, t, b, 100. * t / ll, 100. * b / ll))
                

def gnew(grid):
    newgrid = {}
    for x in range(L):
        for y in range(L):
            if grid[(x,y)] == burning:
                newgrid[(x,y)] = space
            elif grid[(x,y)] == space:
                newgrid[(x,y)] = tree if random.random()<= p else space
            elif grid[(x,y)] == tree:
                newgrid[(x,y)] = (burning
                                   if any(grid.get((x+dx,y+dy),space) == burning
                                            for dx,dy in hood)
                                        or random.random()<= f 
                                   else tree)
    return newgrid

if __name__ == '__main__':
    grid = initialise()
    iter = 0
    while True:
        quickprint(grid)
        inp = raw_input('Print/Quit/<int>/<return> %6i: ' % iter).lower().strip()
        if inp:
            if inp[0] == 'p':
                gprint(grid)
            elif inp.isdigit():
                for i in range(int(inp)):
                    iter +=1
                    grid = gnew(grid)
                    quickprint(grid)
            elif inp[0] == 'q':
                break
        grid = gnew(grid)
        iter +=1

```

