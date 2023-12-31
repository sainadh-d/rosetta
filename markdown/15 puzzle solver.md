# 15 puzzle solver

## Task Link
[Rosetta Code - 15 puzzle solver](https://rosettacode.org/wiki/15_puzzle_solver)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;

public final class Puzzle15Solver {
    
    public static void main(String[] aArgs) {
        List<Integer> start = List.of( 15, 14, 1, 6, 9, 11, 4, 12, 0, 10, 7, 3, 13, 8, 5, 2 );
        final int zeroIndex = 8;
        Puzzle initial = new Puzzle(start, new ArrayList<String>(), zeroIndex, 0);
        openSet.add(initial);
        System.out.println("Solving the 15 puzzle:");
        initial.display();        
        
        while ( solution == null ) {
            search();
        }

        System.out.println(solution.moves.stream().collect(Collectors.joining("")));
        System.out.println("Number of steps: " + solution.moves.size());
        System.out.println("Number of puzzle states checked: " + closedSet.size());
    }
    
    private static void search() {
		Puzzle current = openSet.poll();
	    closedSet.add(current);
	    final int zeroIndex = current.zeroIndex;
	    final int row = zeroIndex / 4;
        final int column = zeroIndex % 4;
	    
		if ( column > 0 ) {
			Puzzle nextPuzzle = current.clone();
			nextPuzzle.makeMove(Move.LEFT);
	    }
	    if ( column < 3 ) {
	    	Puzzle nextPuzzle = current.clone();
	    	nextPuzzle.makeMove(Move.RIGHT);
	    }
	    if ( row > 0 ) {
	    	Puzzle nextPuzzle = current.clone();
	    	nextPuzzle.makeMove(Move.UP);
	    }
	    if ( row < 3 ) {
	    	Puzzle nextPuzzle = current.clone();
	    	nextPuzzle.makeMove(Move.DOWN);
	    }
	}

    private enum Move {		
		LEFT("L", -1), RIGHT("R", +1), UP("U", -4), DOWN("D", +4);		
		
		private Move(String aSymbol, int aStep) {
			symbol = aSymbol;
			step = aStep;
		}
		
		private String symbol;
		private Integer step;		
	}
    
    private static class Puzzle {    

        public Puzzle(List<Integer> aTiles, List<String> aMoves, int aZeroIndex, int aSearchDepth) {
        	tiles = aTiles;
            moves = aMoves;        
            zeroIndex = aZeroIndex;
            searchDepth = aSearchDepth;             
        }
        
        public void makeMove(Move aMove) {    		
    		Integer temp = tiles.get(zeroIndex + aMove.step);
    		tiles.set(zeroIndex + aMove.step, 0);
    		tiles.set(zeroIndex, temp);
    		
    		zeroIndex += aMove.step;
    		moves.add(aMove.symbol);
    		
    		if ( ! closedSet.contains(this) ) {
                openSet.add(this);
                if ( tiles.equals(Puzzle.GOAL) ) {
                    solution = this;
                }
            }
    	}

        public long heuristic() {
        	int distance = 0;
        	for ( int i = 0; i < tiles.size(); i++ ) {
        		final int tile = tiles.get(i);
            	if ( tile > 0 ) { 
            		distance += Math.abs( ( i / 4 ) - ( tile - 1 ) / 4 ) + Math.abs( ( i % 4 ) - ( tile - 1 ) % 4 );
            	}
            }
            return distance + searchDepth;
        }  
        
        public Puzzle clone() {
            return new Puzzle(new ArrayList<Integer>(tiles), new ArrayList<String>(moves), zeroIndex, searchDepth + 1);
        }

        public void display() {
        	 for ( int i = 0; i < tiles.size(); i++ ) {
                 System.out.print(String.format("%s%2d%s",
                 	( i % 4 == 0 ) ? "[" : "", tiles.get(i), ( i % 4 == 3 ) ? "]\n" : " "));
             }
             System.out.println();
        }   

        @Override
        public boolean equals(Object aObject) {
        	return switch(aObject) {
        		case Puzzle puzzle -> tiles.equals(puzzle.tiles);
        		case Object object -> false;
        	};
        }
        
        @Override
        public int hashCode() {
            int hash = 3;
            hash = 23 * hash + tiles.hashCode();
            hash = 23 * hash + zeroIndex;
            return hash;
        }
        
        private List<Integer> tiles;
        private List<String> moves;
        private int zeroIndex;
        private int searchDepth;        
        
        private static final List<Integer> GOAL = List.of( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0 );
        
    }

    private static Queue<Puzzle> openSet =
    	new PriorityQueue<Puzzle>( (one, two) -> Long.compare(one.heuristic(), two.heuristic()) ); 
    private static Set<Puzzle> closedSet = new HashSet<Puzzle>();
    private static Puzzle solution;
   
}

```

## Python Code
### python_code_1.txt
```python
import random


class IDAStar:
    def __init__(self, h, neighbours):
        """ Iterative-deepening A* search.

        h(n) is the heuristic that gives the cost between node n and the goal node. It must be admissable, meaning that h(n) MUST NEVER OVERSTIMATE the true cost. Underestimating is fine.

        neighbours(n) is an iterable giving a pair (cost, node, descr) for each node neighbouring n
        IN ASCENDING ORDER OF COST. descr is not used in the computation but can be used to
        efficiently store information about the path edges (e.g. up/left/right/down for grids).
        """

        self.h = h
        self.neighbours = neighbours
        self.FOUND = object()


    def solve(self, root, is_goal, max_cost=None):
        """ Returns the shortest path between the root and a given goal, as well as the total cost.
        If the cost exceeds a given max_cost, the function returns None. If you do not give a
        maximum cost the solver will never return for unsolvable instances."""

        self.is_goal = is_goal
        self.path = [root]
        self.is_in_path = {root}
        self.path_descrs = []
        self.nodes_evaluated = 0

        bound = self.h(root)

        while True:
            t = self._search(0, bound)
            if t is self.FOUND: return self.path, self.path_descrs, bound, self.nodes_evaluated
            if t is None: return None
            bound = t

    def _search(self, g, bound):
        self.nodes_evaluated += 1

        node = self.path[-1]
        f = g + self.h(node)
        if f > bound: return f
        if self.is_goal(node): return self.FOUND

        m = None # Lower bound on cost.
        for cost, n, descr in self.neighbours(node):
            if n in self.is_in_path: continue

            self.path.append(n)
            self.is_in_path.add(n)
            self.path_descrs.append(descr)
            t = self._search(g + cost, bound)

            if t == self.FOUND: return self.FOUND
            if m is None or (t is not None and t < m): m = t

            self.path.pop()
            self.path_descrs.pop()
            self.is_in_path.remove(n)

        return m


def slide_solved_state(n):
    return tuple(i % (n*n) for i in range(1, n*n+1))

def slide_randomize(p, neighbours):
    for _ in range(len(p) ** 2):
        _, p, _ = random.choice(list(neighbours(p)))
    return p

def slide_neighbours(n):
    movelist = []
    for gap in range(n*n):
        x, y = gap % n, gap // n
        moves = []
        if x > 0: moves.append(-1)    # Move the gap left.
        if x < n-1: moves.append(+1)  # Move the gap right.
        if y > 0: moves.append(-n)    # Move the gap up.
        if y < n-1: moves.append(+n)  # Move the gap down.
        movelist.append(moves)

    def neighbours(p):
        gap = p.index(0)
        l = list(p)

        for m in movelist[gap]:
            l[gap] = l[gap + m]
            l[gap + m] = 0
            yield (1, tuple(l), (l[gap], m))
            l[gap + m] = l[gap]
            l[gap] = 0

    return neighbours

def slide_print(p):
    n = int(round(len(p) ** 0.5))
    l = len(str(n*n))
    for i in range(0, len(p), n):
        print(" ".join("{:>{}}".format(x, l) for x in p[i:i+n]))

def encode_cfg(cfg, n):
    r = 0
    b = n.bit_length()
    for i in range(len(cfg)):
        r |= cfg[i] << (b*i)
    return r


def gen_wd_table(n):
    goal = [[0] * i + [n] + [0] * (n - 1 - i) for i in range(n)]
    goal[-1][-1] = n - 1
    goal = tuple(sum(goal, []))

    table = {}
    to_visit = [(goal, 0, n-1)]
    while to_visit:
        cfg, cost, e = to_visit.pop(0)
        enccfg = encode_cfg(cfg, n)
        if enccfg in table: continue
        table[enccfg] = cost

        for d in [-1, 1]:
            if 0 <= e + d < n:
                for c in range(n):
                    if cfg[n*(e+d) + c] > 0:
                        ncfg = list(cfg)
                        ncfg[n*(e+d) + c] -= 1
                        ncfg[n*e + c] += 1
                        to_visit.append((tuple(ncfg), cost + 1, e+d))

    return table

def slide_wd(n, goal):
    wd = gen_wd_table(n)
    goals = {i : goal.index(i) for i in goal}
    b = n.bit_length()

    def h(p):
        ht = 0 # Walking distance between rows.
        vt = 0 # Walking distance between columns.
        d = 0
        for i, c in enumerate(p):
            if c == 0: continue
            g = goals[c]
            xi, yi = i % n, i // n
            xg, yg = g % n, g // n
            ht += 1 << (b*(n*yi+yg))
            vt += 1 << (b*(n*xi+xg))

            if yg == yi:
                for k in range(i + 1, i - i%n + n): # Until end of row.
                    if p[k] and goals[p[k]] // n == yi and goals[p[k]] < g:
                        d += 2

            if xg == xi:
                for k in range(i + n, n * n, n): # Until end of column.
                    if p[k] and goals[p[k]] % n == xi and goals[p[k]] < g:
                        d += 2

        d += wd[ht] + wd[vt]

        return d
    return h




if __name__ == "__main__":
    solved_state = slide_solved_state(4)
    neighbours = slide_neighbours(4)
    is_goal = lambda p: p == solved_state

    tests = [
        (15, 14, 1, 6, 9, 11, 4, 12, 0, 10, 7, 3, 13, 8, 5, 2),
    ]

    slide_solver = IDAStar(slide_wd(4, solved_state), neighbours)

    for p in tests:
        path, moves, cost, num_eval = slide_solver.solve(p, is_goal, 80)
        slide_print(p)
        print(", ".join({-1: "Left", 1: "Right", -4: "Up", 4: "Down"}[move[1]] for move in moves))
        print(cost, num_eval)

```

### python_code_2.txt
```python
"""

Python example for this Rosetta Code task:

http://rosettacode.org/wiki/15_puzzle_solver

Using A* Algorithm from Wikkipedia:

https://en.wikipedia.org/wiki/A*_search_algorithm

Need to use heuristic that guarantees a shortest path
solution.

"""

import heapq
import copy

# Hopefully this is larger than any fscore or gscore

integer_infinity = 1000000000

class Position(object):
    """Position class represents one position of a 15 puzzle"""

    def __init__(self, tiles):
        """
        Takes a tuple of tuples representing the tiles on a 4x4 puzzle board
        numbering 1-15 with 0 representing an empty square. For example:
        
        (( 1,  2,  3,  4),
         ( 5,  6,  7,  8),
         ( 9, 10, 11, 12),
         (13, 14, 15,  0))
         
        Converts list of lists representation into tuple of tuples.
        """
        if type(tiles) == type(list()):
            t = tiles
            self.tiles = ((t[0][0], t[0][1], t[0][2], t[0][3]),
                          (t[1][0], t[1][1], t[1][2], t[1][3]),        
                          (t[2][0], t[2][1], t[2][2], t[2][3]),        
                          (t[3][0], t[3][1], t[3][2], t[3][3]))
        else:
            self.tiles = tiles
            
        # fields for A* algorithm
        
        self.fscore = integer_infinity
        self.gscore = integer_infinity
        
        self.cameFrom = None
                                    
    def copy_tiles(self):
        """ returns list of lists version """
        t = self.tiles
        
        return [[t[0][0], t[0][1], t[0][2], t[0][3]],
                [t[1][0], t[1][1], t[1][2], t[1][3]],        
                [t[2][0], t[2][1], t[2][2], t[2][3]],        
                [t[3][0], t[3][1], t[3][2], t[3][3]]]        

        
    def neighbors(self):
        """
        returns a list of neighbors
        returns a list position objects with their
        directiontomoveto set to the direction that the
        empty square moved.
        
        tiles is 4x4 tuple of tuples with
        0,0 as top left.
    
        tiles[y][x]

        """
        
        # find 0 - blank square
        
        x0 = None
        y0 = None
        
        for i in range(4):
            for j in range(4):
                if self.tiles[i][j] == 0:
                    y0 = i
                    x0 = j

        if x0 == None or y0 == None:
            return []
            
        neighbor_list = []
            
        # move 0 to the right
        if x0 < 3:
            new_tiles = self.copy_tiles()
            temp = new_tiles[y0][x0+1]
            new_tiles[y0][x0+1] = 0
            new_tiles[y0][x0] = temp
            new_pos = new_position(new_tiles)
            neighbor_list.append(new_pos)
        # move 0 to the left
        if x0 > 0:
            new_tiles = self.copy_tiles()
            temp = new_tiles[y0][x0-1]
            new_tiles[y0][x0-1] = 0
            new_tiles[y0][x0] = temp
            new_pos = new_position(new_tiles)
            neighbor_list.append(new_pos)
        # move 0 up
        if y0 > 0:
            new_tiles = self.copy_tiles()
            temp = new_tiles[y0-1][x0]
            new_tiles[y0-1][x0] = 0
            new_tiles[y0][x0] = temp
            new_pos = new_position(new_tiles)
            neighbor_list.append(new_pos)
        # move 0 down
        if y0 < 3:
            new_tiles = self.copy_tiles()
            temp = new_tiles[y0+1][x0]
            new_tiles[y0+1][x0] = 0
            new_tiles[y0][x0] = temp
            new_pos = new_position(new_tiles)
            neighbor_list.append(new_pos)
            
        return neighbor_list
        
    def __repr__(self):
        # printable version of self
        
        return str(self.tiles[0])+'\n'+str(self.tiles[1])+'\n'+str(self.tiles[2])+'\n'+str(self.tiles[3])+'\n'

# takes tuple of tuples tiles as key, Position object for that tiles as value

all_positions = dict()

def new_position(tiles):
    """ returns a new position or looks up existing one """
    global all_positions
    if type(tiles) == type(list()):
        t = tiles
        tuptiles =   ((t[0][0], t[0][1], t[0][2], t[0][3]),
                      (t[1][0], t[1][1], t[1][2], t[1][3]),        
                      (t[2][0], t[2][1], t[2][2], t[2][3]),        
                      (t[3][0], t[3][1], t[3][2], t[3][3]))
    else:
        tuptiles = tiles
        
    if tuptiles in all_positions:
        return 	all_positions[tuptiles]
    else:
        new_pos = Position(tiles)
        all_positions[tuptiles] = new_pos
        return new_pos
                
def reconstruct_path(current):
    """ 
    Uses the cameFrom members to follow the chain of moves backwards
    and then reverses the list to get the path in the correct order.
    """
    total_path = [current]

    while current.cameFrom != None:
        current = current.cameFrom
        total_path.append(current)
        
    total_path.reverse()
    
    return total_path
        
class PriorityQueue(object):
    """
    Priority queue using heapq.
    elements of queue are (fscore,tiles) for each position.
    If element is removed from queue and fscore doesn't match
    then that element is discarded.
    """

    def __init__(self, object_list):
        """ 
        Save a list in a heapq.
        Assume that each object only appears once
        in the list.
        """
        self.queue_length = 0
        self.qheap = []
        for e in object_list:
            self.qheap.append((e.fscore,e.tiles))
            self.queue_length += 1
        heapq.heapify(self.qheap)
        
    def push(self, new_object):
        """ save object in heapq """
        heapq.heappush(self.qheap,(new_object.fscore,new_object.tiles))
        self.queue_length += 1
        
    def pop(self):
        """ remove object from heap and return """
        if self.queue_length < 1:
            return None
        fscore, tiles = heapq.heappop(self.qheap)
        self.queue_length -= 1
        global all_positions
        pos = all_positions[tiles]
        if pos.fscore == fscore:
            return pos
        else:
            return self.pop()
                
    def __repr__(self):
        # printable version of self
        strrep = ""
        for e in self.qheap:
          fscore, tiles = e
          strrep += str(fscore)+":"+str(tiles)+"\n"
        
        return strrep
        
conflict_table = None

def build_conflict_table():
    global conflict_table
    conflict_table = dict()
    
    # assumes goal tuple has up to 
    # for the given pattern it the start position
    # how much to add for linear conflicts
    # 2 per conflict - max of 6
    
    # goal tuple is ('g0', 'g1', 'g2', 'g3')
    
    conflict_table[('g0', 'g1', 'g2', 'g3')] = 0
    conflict_table[('g0', 'g1', 'g2', 'x')] = 0
    conflict_table[('g0', 'g1', 'g3', 'g2')] = 2
    conflict_table[('g0', 'g1', 'g3', 'x')] = 0
    conflict_table[('g0', 'g1', 'x', 'g2')] = 0
    conflict_table[('g0', 'g1', 'x', 'g3')] = 0
    conflict_table[('g0', 'g1', 'x', 'x')] = 0
    conflict_table[('g0', 'g2', 'g1', 'g3')] = 2
    conflict_table[('g0', 'g2', 'g1', 'x')] = 2
    conflict_table[('g0', 'g2', 'g3', 'g1')] = 4
    conflict_table[('g0', 'g2', 'g3', 'x')] = 0
    conflict_table[('g0', 'g2', 'x', 'g1')] = 2
    conflict_table[('g0', 'g2', 'x', 'g3')] = 0
    conflict_table[('g0', 'g2', 'x', 'x')] = 0
    conflict_table[('g0', 'g3', 'g1', 'g2')] = 4 
    conflict_table[('g0', 'g3', 'g1', 'x')] = 2
    conflict_table[('g0', 'g3', 'g2', 'g1')] = 4
    conflict_table[('g0', 'g3', 'g2', 'x')] = 2
    conflict_table[('g0', 'g3', 'x', 'g1')] = 2
    conflict_table[('g0', 'g3', 'x', 'g2')] = 2
    conflict_table[('g0', 'g3', 'x', 'x')] = 0
    conflict_table[('g0', 'x', 'g1', 'g2')] = 0
    conflict_table[('g0', 'x', 'g1', 'g3')] = 0
    conflict_table[('g0', 'x', 'g1', 'x')] = 0
    conflict_table[('g0', 'x', 'g2', 'g1')] = 2
    conflict_table[('g0', 'x', 'g2', 'g3')] = 0
    conflict_table[('g0', 'x', 'g2', 'x')] = 0
    conflict_table[('g0', 'x', 'g3', 'g1')] = 2
    conflict_table[('g0', 'x', 'g3', 'g2')] = 2
    conflict_table[('g0', 'x', 'g3', 'x')] = 0
    conflict_table[('g0', 'x', 'x', 'g1')] = 0
    conflict_table[('g0', 'x', 'x', 'g2')] = 0
    conflict_table[('g0', 'x', 'x', 'g3')] = 0
    conflict_table[('g1', 'g0', 'g2', 'g3')] = 2
    conflict_table[('g1', 'g0', 'g2', 'x')] = 2
    conflict_table[('g1', 'g0', 'g3', 'g2')] = 4 
    conflict_table[('g1', 'g0', 'g3', 'x')] = 2
    conflict_table[('g1', 'g0', 'x', 'g2')] = 2
    conflict_table[('g1', 'g0', 'x', 'g3')] = 2
    conflict_table[('g1', 'g0', 'x', 'x')] = 2
    conflict_table[('g1', 'g2', 'g0', 'g3')] = 4 
    conflict_table[('g1', 'g2', 'g0', 'x')] = 4
    conflict_table[('g1', 'g2', 'g3', 'g0')] = 6 
    conflict_table[('g1', 'g2', 'g3', 'x')] = 0
    conflict_table[('g1', 'g2', 'x', 'g0')] = 4
    conflict_table[('g1', 'g2', 'x', 'g3')] = 0
    conflict_table[('g1', 'g2', 'x', 'x')] = 0
    conflict_table[('g1', 'g3', 'g0', 'g2')] = 4 
    conflict_table[('g1', 'g3', 'g0', 'x')] = 4
    conflict_table[('g1', 'g3', 'g2', 'g0')] = 6 
    conflict_table[('g1', 'g3', 'g2', 'x')] = 0
    conflict_table[('g1', 'g3', 'x', 'g0')] = 4
    conflict_table[('g1', 'g3', 'x', 'g2')] = 2
    conflict_table[('g1', 'g3', 'x', 'x')] = 0
    conflict_table[('g1', 'x', 'g0', 'g2')] = 2
    conflict_table[('g1', 'x', 'g0', 'g3')] = 2
    conflict_table[('g1', 'x', 'g0', 'x')] = 2
    conflict_table[('g1', 'x', 'g2', 'g0')] = 4
    conflict_table[('g1', 'x', 'g2', 'g3')] = 0
    conflict_table[('g1', 'x', 'g2', 'x')] = 0
    conflict_table[('g1', 'x', 'g3', 'g0')] = 4
    conflict_table[('g1', 'x', 'g3', 'g2')] = 2
    conflict_table[('g1', 'x', 'g3', 'x')] = 0
    conflict_table[('g1', 'x', 'x', 'g0')] = 2
    conflict_table[('g1', 'x', 'x', 'g2')] = 0
    conflict_table[('g1', 'x', 'x', 'g3')] = 0
    conflict_table[('g2', 'g0', 'g1', 'g3')] = 4
    conflict_table[('g2', 'g0', 'g1', 'x')] = 4
    conflict_table[('g2', 'g0', 'g3', 'g1')] = 4
    conflict_table[('g2', 'g0', 'g3', 'x')] = 2
    conflict_table[('g2', 'g0', 'x', 'g1')] = 4
    conflict_table[('g2', 'g0', 'x', 'g3')] = 2
    conflict_table[('g2', 'g0', 'x', 'x')] = 2
    conflict_table[('g2', 'g1', 'g0', 'g3')] = 4
    conflict_table[('g2', 'g1', 'g0', 'x')] = 4
    conflict_table[('g2', 'g1', 'g3', 'g0')] = 6
    conflict_table[('g2', 'g1', 'g3', 'x')] = 2
    conflict_table[('g2', 'g1', 'x', 'g0')] = 4
    conflict_table[('g2', 'g1', 'x', 'g3')] = 2
    conflict_table[('g2', 'g1', 'x', 'x')] = 2
    conflict_table[('g2', 'g3', 'g0', 'g1')] = 4
    conflict_table[('g2', 'g3', 'g0', 'x')] = 4
    conflict_table[('g2', 'g3', 'g1', 'g0')] = 6
    conflict_table[('g2', 'g3', 'g1', 'x')] = 4
    conflict_table[('g2', 'g3', 'x', 'g0')] = 4
    conflict_table[('g2', 'g3', 'x', 'g1')] = 4
    conflict_table[('g2', 'g3', 'x', 'x')] = 0
    conflict_table[('g2', 'x', 'g0', 'g1')] = 4
    conflict_table[('g2', 'x', 'g0', 'g3')] = 2
    conflict_table[('g2', 'x', 'g0', 'x')] = 2
    conflict_table[('g2', 'x', 'g1', 'g0')] = 4
    conflict_table[('g2', 'x', 'g1', 'g3')] = 2
    conflict_table[('g2', 'x', 'g1', 'x')] = 2
    conflict_table[('g2', 'x', 'g3', 'g0')] = 4
    conflict_table[('g2', 'x', 'g3', 'g1')] = 4
    conflict_table[('g2', 'x', 'g3', 'x')] = 0
    conflict_table[('g2', 'x', 'x', 'g0')] = 2
    conflict_table[('g2', 'x', 'x', 'g1')] = 2
    conflict_table[('g2', 'x', 'x', 'g3')] = 0
    conflict_table[('g3', 'g0', 'g1', 'g2')] = 6
    conflict_table[('g3', 'g0', 'g1', 'x')] = 4
    conflict_table[('g3', 'g0', 'g2', 'g1')] = 6
    conflict_table[('g3', 'g0', 'g2', 'x')] = 4
    conflict_table[('g3', 'g0', 'x', 'g1')] = 4
    conflict_table[('g3', 'g0', 'x', 'g2')] = 4
    conflict_table[('g3', 'g0', 'x', 'x')] = 2
    conflict_table[('g3', 'g1', 'g0', 'g2')] = 6
    conflict_table[('g3', 'g1', 'g0', 'x')] = 4
    conflict_table[('g3', 'g1', 'g2', 'g0')] = 6
    conflict_table[('g3', 'g1', 'g2', 'x')] = 4
    conflict_table[('g3', 'g1', 'x', 'g0')] = 4
    conflict_table[('g3', 'g1', 'x', 'g2')] = 4
    conflict_table[('g3', 'g1', 'x', 'x')] = 2
    conflict_table[('g3', 'g2', 'g0', 'g1')] = 6
    conflict_table[('g3', 'g2', 'g0', 'x')] = 4
    conflict_table[('g3', 'g2', 'g1', 'g0')] = 6
    conflict_table[('g3', 'g2', 'g1', 'x')] = 4
    conflict_table[('g3', 'g2', 'x', 'g0')] = 4
    conflict_table[('g3', 'g2', 'x', 'g1')] = 4
    conflict_table[('g3', 'g2', 'x', 'x')] = 2
    conflict_table[('g3', 'x', 'g0', 'g1')] = 4
    conflict_table[('g3', 'x', 'g0', 'g2')] = 4
    conflict_table[('g3', 'x', 'g0', 'x')] = 2
    conflict_table[('g3', 'x', 'g1', 'g0')] = 4
    conflict_table[('g3', 'x', 'g1', 'g2')] = 4
    conflict_table[('g3', 'x', 'g1', 'x')] = 2
    conflict_table[('g3', 'x', 'g2', 'g0')] = 4
    conflict_table[('g3', 'x', 'g2', 'g1')] = 4
    conflict_table[('g3', 'x', 'g2', 'x')] = 2
    conflict_table[('g3', 'x', 'x', 'g0')] = 2
    conflict_table[('g3', 'x', 'x', 'g1')] = 2
    conflict_table[('g3', 'x', 'x', 'g2')] = 2
    conflict_table[('x', 'g0', 'g1', 'g2')] = 0
    conflict_table[('x', 'g0', 'g1', 'g3')] = 0
    conflict_table[('x', 'g0', 'g1', 'x')] = 0
    conflict_table[('x', 'g0', 'g2', 'g1')] = 2
    conflict_table[('x', 'g0', 'g2', 'g3')] = 0
    conflict_table[('x', 'g0', 'g2', 'x')] = 0
    conflict_table[('x', 'g0', 'g3', 'g1')] = 2
    conflict_table[('x', 'g0', 'g3', 'g2')] = 2
    conflict_table[('x', 'g0', 'g3', 'x')] = 0
    conflict_table[('x', 'g0', 'x', 'g1')] = 0
    conflict_table[('x', 'g0', 'x', 'g2')] = 0
    conflict_table[('x', 'g0', 'x', 'g3')] = 0
    conflict_table[('x', 'g1', 'g0', 'g2')] = 2
    conflict_table[('x', 'g1', 'g0', 'g3')] = 2
    conflict_table[('x', 'g1', 'g0', 'x')] = 2
    conflict_table[('x', 'g1', 'g2', 'g0')] = 4
    conflict_table[('x', 'g1', 'g2', 'g3')] = 0
    conflict_table[('x', 'g1', 'g2', 'x')] = 0
    conflict_table[('x', 'g1', 'g3', 'g0')] = 4
    conflict_table[('x', 'g1', 'g3', 'g2')] = 2
    conflict_table[('x', 'g1', 'g3', 'x')] = 0
    conflict_table[('x', 'g1', 'x', 'g0')] = 2
    conflict_table[('x', 'g1', 'x', 'g2')] = 0
    conflict_table[('x', 'g1', 'x', 'g3')] = 0
    conflict_table[('x', 'g2', 'g0', 'g1')] = 4
    conflict_table[('x', 'g2', 'g0', 'g3')] = 2
    conflict_table[('x', 'g2', 'g0', 'x')] = 2
    conflict_table[('x', 'g2', 'g1', 'g0')] = 4
    conflict_table[('x', 'g2', 'g1', 'g3')] = 2
    conflict_table[('x', 'g2', 'g1', 'x')] = 2
    conflict_table[('x', 'g2', 'g3', 'g0')] = 4
    conflict_table[('x', 'g2', 'g3', 'g1')] = 4
    conflict_table[('x', 'g2', 'g3', 'x')] = 0
    conflict_table[('x', 'g2', 'x', 'g0')] = 2
    conflict_table[('x', 'g2', 'x', 'g1')] = 2
    conflict_table[('x', 'g2', 'x', 'g3')] = 0
    conflict_table[('x', 'g3', 'g0', 'g1')] = 4
    conflict_table[('x', 'g3', 'g0', 'g2')] = 4
    conflict_table[('x', 'g3', 'g0', 'x')] = 2
    conflict_table[('x', 'g3', 'g1', 'g0')] = 4
    conflict_table[('x', 'g3', 'g1', 'g2')] = 4
    conflict_table[('x', 'g3', 'g1', 'x')] = 2
    conflict_table[('x', 'g3', 'g2', 'g0')] = 4
    conflict_table[('x', 'g3', 'g2', 'g1')] = 4
    conflict_table[('x', 'g3', 'g2', 'x')] = 2
    conflict_table[('x', 'g3', 'x', 'g0')] = 2
    conflict_table[('x', 'g3', 'x', 'g1')] = 2
    conflict_table[('x', 'g3', 'x', 'g2')] = 2
    conflict_table[('x', 'x', 'g0', 'g1')] = 0
    conflict_table[('x', 'x', 'g0', 'g2')] = 0
    conflict_table[('x', 'x', 'g0', 'g3')] = 0
    conflict_table[('x', 'x', 'g1', 'g0')] = 2
    conflict_table[('x', 'x', 'g1', 'g2')] = 0
    conflict_table[('x', 'x', 'g1', 'g3')] = 0
    conflict_table[('x', 'x', 'g2', 'g0')] = 2
    conflict_table[('x', 'x', 'g2', 'g1')] = 2
    conflict_table[('x', 'x', 'g2', 'g3')] = 0
    conflict_table[('x', 'x', 'g3', 'g0')] = 2
    conflict_table[('x', 'x', 'g3', 'g1')] = 2
    conflict_table[('x', 'x', 'g3', 'g2')] = 2
        
def linear_conflicts(start_list,goal_list):
    """
    calculates number of moves to add to the estimate of
    the moves to get from start to goal based on the number
    of conflicts on a given row or column. start_list
    represents the current location and goal_list represnts
    the final goal.
    """
    
    # Find which of the tiles in start_list have their goals on this line
    # build a pattern to use in a lookup table of this form:
    # g0, g1, g3, g3 fill in x where there is no goal for this line
    
    # all 'x' until we file a tile whose goal is in this line
    
    goal_pattern = ['x', 'x', 'x', 'x']
    
    for g in range(4):
        for s in range(4):
            start_tile_num = start_list[s]
            if start_tile_num == goal_list[g] and start_tile_num != 0:
                goal_pattern[s] = 'g' + str(g) # i.e. g0
                                
    global conflict_table
    
    tup_goal_pattern = tuple(goal_pattern)
    
    if tup_goal_pattern in conflict_table:
        return conflict_table[tuple(goal_pattern)]
    else:
        return 0
    
class lcmap(dict):
    """ 
    Lets you return 0 if you look for an object that
    is not in the dictionary. 
    """
    def __missing__(self, key):
        return 0

def listconflicts(goal_list):
    """ 
    list all possible start lists that will have at least
    one linear conflict.
    
    Possible goal tile configurations
    
    g g g g
    g g g x
    g g x g
    g x g g
    x g g g
    g g x x
    g x g x
    g x x g
    x g g x
    x g x g
    x x g g
        
    """
    
    all_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    non_goal_tiles = []
    
    for t in all_tiles:
        if t not in goal_list:
            non_goal_tiles.append(t) 
            
    combinations = lcmap()

    # g g g g
    
    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in tile_list3:
                tile_list4 = tile_list3[:]
                tile_list4.remove(k)
                for l in tile_list4:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd    
    
    # g g g x
    
    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in non_goal_tiles:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd  

    # g g x g
    
    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in non_goal_tiles:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd
    # g x g g
    
    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            for k in tile_list2:
                tile_list3 = tile_list2[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd

    # x g g g
    
    for i in non_goal_tiles:
        for j in goal_list:
            tile_list2 = goal_list[:]
            tile_list2.remove(j)
            for k in tile_list2:
                tile_list3 = tile_list2[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd

    # g g x x

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in tile_list2:
            tile_list3 = tile_list2[:]
            tile_list3.remove(j)
            for k in non_goal_tiles:
                tile_list4 = non_goal_tiles[:]
                tile_list4.remove(k)
                for l in tile_list4:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd 
                        
    # g x g x

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            tile_list3 = non_goal_tiles[:]
            tile_list3.remove(j)
            for k in tile_list2:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd    
                        
    # g x x g

    for i in goal_list:
        tile_list2 = goal_list[:]
        tile_list2.remove(i)
        for j in non_goal_tiles:
            tile_list3 = non_goal_tiles[:]
            tile_list3.remove(j)
            for k in tile_list2:
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd     
    
    # x g g x

    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in goal_list:
            tile_list3 = goal_list[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in tile_list2:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd      
    
    # x g x g
    
    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in goal_list:
            tile_list3 = goal_list[:]
            tile_list3.remove(j)
            for k in tile_list3:
                for l in tile_list2:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd      
      
    # x x g g
    
    for i in non_goal_tiles:
        tile_list2 = non_goal_tiles[:]
        tile_list2.remove(i)
        for j in tile_list2:
            for k in goal_list:
                tile_list3 = goal_list[:]
                tile_list3.remove(k)
                for l in tile_list3:
                    start_list = (i, j, k, l)
                    conflictadd = linear_conflicts(start_list,goal_list)
                    if conflictadd > 0:
                        combinations[start_list]=conflictadd      
      
    return combinations


class HeuristicObj(object):
    """ Object used to preprocess goal position for heuristic function """

    def __init__(self, goal):
        """
        Preprocess goal position to setup internal data structures
        that can be used to speed up heuristic.
        """
        
        build_conflict_table()
        
        self.goal_map = []
        for i in range(16):
            self.goal_map.append(i)    
        
        self.goal_lists = goal.tiles
        
        # preprocess for manhattan distance
        
        for row in range(4):
            for col in range(4):
                self.goal_map[goal.tiles[row][col]] = (row, col)
                
        # make access faster by changing to a tuple
        
        self.goal_map = tuple(self.goal_map)
                
        # preprocess for linear conflicts
        
        self.row_conflicts = []
        for row in range(4):
            t = goal.tiles[row]
            conf_dict = listconflicts([t[0],t[1],t[2],t[3]])
            self.row_conflicts.append(conf_dict)
            
        self.col_conflicts = []
        for col in range(4):
            col_list =[]
            for row in range(4):
                col_list.append(goal.tiles[row][col])
            conf_dict = listconflicts(col_list)
            self.col_conflicts.append(conf_dict)

    def heuristic(self, start):
        """ 
        
        Estimates the number of moves from start to goal.
        The goal was preprocessed in __init__.
        
        """
        
        distance = 0
        
        # local variables for instance variables
        
        t = start.tiles
        g = self.goal_map
        rc = self.row_conflicts
        cc = self.col_conflicts
        
        # calculate manhattan distance
        
        for row in range(4):
            for col in range(4):
                start_tilenum = t[row][col]
                if start_tilenum != 0:
                    (grow, gcol) = g[start_tilenum]
                    distance += abs(row - grow) + abs(col - gcol)
                                        
        # add linear conflicts 
        
        for row in range(4):
            curr_row = t[row]
            distance += rc[row][curr_row]
       
        for col in range(4):
            col_tuple = (t[0][col], t[1][col], t[2][col], t[3][col])
            distance += cc[col][col_tuple]
          
        return distance
        
# global variable for heuristic object

hob = None
        
def a_star(start_tiles, goal_tiles):
    """ Based on https://en.wikipedia.org/wiki/A*_search_algorithm """
    
    start = new_position(start_tiles)
    goal = new_position(goal_tiles)
    
    # Process goal position for use in heuristic
    
    global hob
    hob = HeuristicObj(goal)
    
    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    # For the first node, the fscore is completely heuristic.
    
    start.fscore = hob.heuristic(start)
    openSet = PriorityQueue([start])
 
    # The cost of going from start to start is zero.
    
    start.gscore = 0
    
    num_popped = 0
    
    while openSet.queue_length > 0:
        current = openSet.pop()
        if current == None: # tried to pop but only found old fscore values
            break
        num_popped += 1
        if num_popped % 100000 == 0:
            print(str(num_popped)+" positions examined")
        
        if current == goal:
            return reconstruct_path(current)
            
        for neighbor in current.neighbors():

            # The distance from start to a neighbor
            # All nodes are 1 move from their neighbors
            
            tentative_gScore = current.gscore + 1
            
            # update gscore and fscore if this is shorter path
            # to the neighbor node

            if tentative_gScore < neighbor.gscore: 
                neighbor.cameFrom = current
                neighbor.gscore = tentative_gScore
                neighbor.fscore = neighbor.gscore + hob.heuristic(neighbor)
                openSet.push(neighbor) # add to open set every time
                

def find_zero(tiles):
    """ file the 0 tile """
    for row in range(4):
        for col in range(4):
            if tiles[row][col] == 0:
                return (row, col)

def path_as_0_moves(path):
    """
    Takes the path which is a list of Position
    objects and outputs it as a string of rlud 
    directions to match output desired by 
    Rosetta Code task.
    """
    strpath = ""
    if len(path) < 1:
        return ""
    prev_pos = path[0]
    p_row, p_col = find_zero(prev_pos.tiles)
    for i in range(1,len(path)):
        curr_pos = path[i]
        c_row, c_col = find_zero(curr_pos.tiles)
        if c_row > p_row:
            strpath += 'd'
        elif c_row < p_row:
            strpath += 'u'
        elif c_col > p_col:
            strpath += 'r'
        elif c_col < p_col:
            strpath += 'l'
        # reset for next loop
        prev_pos = curr_pos
        p_row = c_row
        p_col = c_col
    return strpath

```

### python_code_3.txt
```python
"""

Runs one test of the solver passing a 
start and goal position.

"""

from astar import *
import time

# Rosetta Code start position


start_tiles =    [[ 15, 14,  1,  6],
                  [ 9, 11,  4, 12],
                  [ 0, 10,  7,  3],
                  [13,  8,  5,  2]]

goal_tiles =        [[ 1,  2,  3,  4],
                     [ 5,  6,  7,  8],
                     [ 9, 10, 11, 12],
                     [13, 14, 15,  0]]
                 

before = time.perf_counter()

result = a_star(start_tiles,goal_tiles)

after = time.perf_counter()

print(" ")
print("Path length = "+str(len(result) - 1))
print(" ")
print("Path using rlud:")
print(" ")
print(path_as_0_moves(result))
print(" ")
print("Run time in seconds: "+str(after - before))

```

