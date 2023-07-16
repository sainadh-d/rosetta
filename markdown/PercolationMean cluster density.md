# Percolation/Mean cluster density

## Task Link
[Rosetta Code - Percolation/Mean cluster density](https://rosettacode.org/wiki/Percolation/Mean_cluster_density)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public final class PercolationMeanCluster {

	public static void main(String[] aArgs) {
		final int size = 15;
		final double probability = 0.5;
		final int testCount = 5;
		
		Grid grid = new Grid(size, probability);
		System.out.println("This " + size + " by " + size + " grid contains " + grid.clusterCount() + " clusters:");
		grid.display();		
			
		System.out.println(System.lineSeparator() + " p = 0.5, iterations = " + testCount);
		List<Integer> gridSizes = List.of( 10, 100, 1_000, 10_000 );	
		for ( int gridSize : gridSizes ) {			
			double sumDensity = 0.0;
			for ( int test = 0; test < testCount; test++ ) {
				grid = new Grid(gridSize, probability);
				sumDensity += grid.clusterDensity();
			}
			double result = sumDensity / testCount;
			System.out.println(String.format("%s%5d%s%.6f", " n = ", gridSize, ", simulation K = ", result));
		}
	}
	
}
	
final class Grid {
	
	public Grid(int aSize, double aProbability) {
		createGrid(aSize, aProbability);
		countClusters();
	}
	
	public int clusterCount() {
		return clusterCount;
	}
	
	public double clusterDensity() {
		return (double) clusterCount / ( grid.length * grid.length );
	}
	
	public void display() {
	    for ( int row = 0; row < grid.length; row++ ) {
	        for ( int col = 0; col < grid.length; col++ ) {
	        	int value = grid[row][col];
	        	char ch = ( value < GRID_CHARACTERS.length() ) ? GRID_CHARACTERS.charAt(value) : '?';
	            System.out.print(" " + ch);
	        }
	        System.out.println();
	    }
	}
    
    private void countClusters() {
	    clusterCount = 0;
	    for ( int row = 0; row < grid.length; row++ ) {
	        for ( int col = 0; col < grid.length; col++ ) {
	            if ( grid[row][col] == CLUSTERED ) {
	                clusterCount += 1;
	                identifyCluster(row, col, clusterCount);
	            }
	        }
	    }
	}
	
	private void identifyCluster(int aRow, int aCol, int aCount) {
		grid[aRow][aCol] = aCount;
		if ( aRow < grid.length - 1 && grid[aRow + 1][aCol] == CLUSTERED ) {
			identifyCluster(aRow + 1, aCol, aCount);
		}
		if ( aCol < grid[0].length - 1 && grid[aRow][aCol + 1] == CLUSTERED ) {
		    identifyCluster(aRow, aCol + 1, aCount);
		}
		if ( aCol > 0 && grid[aRow][aCol - 1] == CLUSTERED ) {
		   	identifyCluster(aRow, aCol - 1, aCount);
		}
		if ( aRow > 0 && grid[aRow - 1][aCol] == CLUSTERED ) {
		    identifyCluster(aRow - 1, aCol, aCount);
		}
	}		
	
	private void createGrid(int aGridSize, double aProbability) {
        grid = new int[aGridSize][aGridSize];		
		for ( int row = 0; row < aGridSize; row++ ) {
			for ( int col = 0; col < aGridSize; col++ ) {
				if ( random.nextDouble(1.0) < aProbability ) {
					grid[row][col] = CLUSTERED;
				}
			}
		}		
	}
	
	private int[][] grid;
	private int clusterCount;

    private static ThreadLocalRandom random = ThreadLocalRandom.current();

	private static final int CLUSTERED = -1;
	private static final String GRID_CHARACTERS = ".ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import division
from random import random
import string
from math import fsum

n_range, p, t = (2**n2 for n2 in range(4, 14, 2)), 0.5, 5
N = M = 15

NOT_CLUSTERED = 1   # filled but not clustered cell
cell2char = ' #' + string.ascii_letters

def newgrid(n, p):
    return [[int(random() < p) for x in range(n)] for y in range(n)]

def pgrid(cell):
    for n in range(N):
        print( '%i)  ' % (n % 10) 
               + ' '.join(cell2char[cell[n][m]] for m in range(M)))


def cluster_density(n, p):
    cc = clustercount(newgrid(n, p))
    return cc / n / n

def clustercount(cell):
    walk_index = 1
    for n in range(N):
        for m in range(M):
            if cell[n][m] == NOT_CLUSTERED:
                walk_index += 1
                walk_maze(m, n, cell, walk_index)
    return walk_index - 1
        

def walk_maze(m, n, cell, indx):
    # fill cell 
    cell[n][m] = indx
    # down
    if n < N - 1 and cell[n+1][m] == NOT_CLUSTERED:
        walk_maze(m, n+1, cell, indx)
    # right
    if m < M - 1 and cell[n][m + 1] == NOT_CLUSTERED:
        walk_maze(m+1, n, cell, indx)
    # left
    if m and cell[n][m - 1] == NOT_CLUSTERED:
        walk_maze(m-1, n, cell, indx)
    # up
    if n and cell[n-1][m] == NOT_CLUSTERED:
        walk_maze(m, n-1, cell, indx)


if __name__ == '__main__':
    cell = newgrid(n=N, p=0.5)
    print('Found %i clusters in this %i by %i grid\n' 
          % (clustercount(cell), N, N))
    pgrid(cell)
    print('')
    
    for n in n_range:
        N = M = n
        sim = fsum(cluster_density(n, p) for i in range(t)) / t
        print('t=%3i p=%4.2f n=%5i sim=%7.5f'
              % (t, p, n, sim))

```

