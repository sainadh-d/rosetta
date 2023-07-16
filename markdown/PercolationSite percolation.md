# Percolation/Site percolation

## Task Link
[Rosetta Code - Percolation/Site percolation](https://rosettacode.org/wiki/Percolation/Site_percolation)

## Java Code
### java_code_1.txt
```java
import java.util.concurrent.ThreadLocalRandom;

public final class PercolationSite {

	public static void main(String[] aArgs) {		
		final int rowCount = 15;
		final int colCount = 15;
		final int testCount = 1_000;
		
		Grid grid = new Grid(rowCount, colCount, 0.5);
		grid.percolate();
		grid.display();
		
		System.out.println("Proportion of " + testCount + " tests that percolate through the grid:");
	    for ( double probable = 0.0; probable <= 1.0; probable += 0.1 ) {
	    	int percolationCount = 0;
	        for ( int test = 0; test < testCount; test++) {
	            Grid testGrid = new Grid(rowCount, colCount, probable);
	            if ( testGrid.percolate() ) {
	            	percolationCount += 1;
	            }
	        }
	        double percolationProportion = (double) percolationCount / testCount;
	        System.out.println(String.format("%s%.1f%s%.4f", " p = ", probable, ": ", percolationProportion));
	    }
	}

}

final class Grid {
	
	public Grid(int aRowCount, int aColCount, double aProbability) {
		createGrid(aRowCount, aColCount, aProbability);
	}
	
	public boolean percolate() {
		for ( int x = 0; x < table[0].length; x++ ) {
			if ( pathExists(x, 0) ) {
				return true;
			}
		}
		return false;
	}
	
	public void display() {
	    for ( int col = 0; col < table.length; col++ ) {
	        for ( int row = 0; row < table[0].length; row++ ) {
	            System.out.print(" " + table[col][row]);
	        }
	        System.out.println();
	    }
	    System.out.println();
	}
	
	private boolean pathExists(int aX, int aY) {		
	    if ( aY < 0 || aX < 0 || aX >= table[0].length || table[aY][aX].compareTo(FILLED) != 0 ) {
	    	return false;
	    }
	    table[aY][aX] = PATH;
	    if ( aY == table.length - 1 ) { 
	    	return true;
	    }
	    return pathExists(aX, aY + 1) || pathExists(aX + 1, aY) || pathExists(aX - 1, aY) || pathExists(aX, aY - 1);
	}
	
	private void createGrid(int aRowCount, int aColCount, double aProbability) {
		table = new String[aRowCount][aColCount];		
		for ( int col = 0; col < aRowCount; col++ ) {
			for ( int row = 0; row < aColCount; row++ ) {
				table[col][row] = ( RANDOM.nextFloat(1.0F) < aProbability ) ? FILLED: EMPTY;
			}
		}	
	}
	
	private String[][] table;
	
	private static final String EMPTY = " ";
	private static final String FILLED = ".";
	private static final String PATH = "#";
	private static final ThreadLocalRandom RANDOM = ThreadLocalRandom.current();
	
}

```

## Python Code
### python_code_1.txt
```python
from random import random
import string
from pprint import pprint as pp

M, N, t = 15, 15, 100

cell2char = ' #' + string.ascii_letters
NOT_VISITED = 1     # filled cell not walked

class PercolatedException(Exception): pass

def newgrid(p):
    return [[int(random() < p) for m in range(M)] for n in range(N)] # cell

def pgrid(cell, percolated=None):
    for n in range(N):
        print( '%i)  ' % (n % 10) 
               + ' '.join(cell2char[cell[n][m]] for m in range(M)))
    if percolated: 
        where = percolated.args[0][0]
        print('!)  ' + '  ' * where + cell2char[cell[n][where]])
    
def check_from_top(cell):
    n, walk_index = 0, 1
    try:
        for m in range(M):
            if cell[n][m] == NOT_VISITED:
                walk_index += 1
                walk_maze(m, n, cell, walk_index)
    except PercolatedException as ex:
        return ex
    return None
        

def walk_maze(m, n, cell, indx):
    # fill cell 
    cell[n][m] = indx
    # down
    if n < N - 1 and cell[n+1][m] == NOT_VISITED:
        walk_maze(m, n+1, cell, indx)
    # THE bottom
    elif n == N - 1:
        raise PercolatedException((m, indx))
    # left
    if m and cell[n][m - 1] == NOT_VISITED:
        walk_maze(m-1, n, cell, indx)
    # right
    if m < M - 1 and cell[n][m + 1] == NOT_VISITED:
        walk_maze(m+1, n, cell, indx)
    # up
    if n and cell[n-1][m] == NOT_VISITED:
        walk_maze(m, n-1, cell, indx)

if __name__ == '__main__':
    sample_printed = False
    pcount = {}
    for p10 in range(11):
        p = p10 / 10.0
        pcount[p] = 0
        for tries in range(t):
            cell = newgrid(p)
            percolated = check_from_top(cell)
            if percolated:
                pcount[p] += 1
                if not sample_printed:
                    print('\nSample percolating %i x %i, p = %5.2f grid\n' % (M, N, p))
                    pgrid(cell, percolated)
                    sample_printed = True
    print('\n p: Fraction of %i tries that percolate through\n' % t )
    
    pp({p:c/float(t) for p, c in pcount.items()})

```

