# Abelian sandpile model/Identity

## Task Link
[Rosetta Code - Abelian sandpile model/Identity](https://rosettacode.org/wiki/Abelian_sandpile_model/Identity)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public final class AbelianSandpileModel {

	public static void main(String[] aArgs) {
		Sandpile avalanche = new Sandpile(List.of( 4, 3, 3, 3, 1, 2, 0, 2, 3 ));
		System.out.println("Avalanche reduction to stable state:");
		avalanche.display();
		System.out.println(" ==> ");
		avalanche.stabilise();
		avalanche.display();
		
		Sandpile s1 = new Sandpile(List.of( 1, 2, 0, 2, 1, 1, 0, 1, 3 ));
		Sandpile s2 = new Sandpile(List.of( 2, 1, 3, 1, 0, 1, 0, 1, 0 ));
		Sandpile sum1 = s1.add(s2);
		Sandpile sum2 = s2.add(s1);
		System.out.println(System.lineSeparator() + "Commutativity of addition" + System.lineSeparator());
		System.out.println("Sandpile1 + Sandpile2:");
		sum1.display();
		System.out.println("Sandpile2 + Sandpile1:");
		sum2.display();
		System.out.println("Sandpile1 + Sandpile2 = Sandpile2 + Sandpile1: " + sum1.equals(sum2));
		
		Sandpile s3 = new Sandpile(List.of( 3, 3, 3, 3, 3, 3, 3, 3, 3 ));
		Sandpile s3_id = new Sandpile(List.of( 2, 1, 2, 1, 0, 1, 2, 1, 2 ));
		Sandpile sum3 = s3.add(s3_id);
		Sandpile sum4 = s3_id.add(s3_id);
		System.out.println(System.lineSeparator() + "Identity Sandpile" + System.lineSeparator());
		System.out.println("Sandpile3 + Sandpile3_id:");
		sum3.display();
		System.out.println("Sandpile3_id + Sandpile3_id:");
		sum4.display();		
	}

}

final class Sandpile {
	
    public Sandpile(List<Integer> aList) {
    	if ( aList.size() != CELL_COUNT ) {
    		throw new IllegalArgumentException("Initialiser list must contain " + CELL_COUNT + " elements");
    	}    	
    	cells = new ArrayList<Integer>(aList);    	
    }
    
    public void stabilise() {
    	while ( ! isStable() ) {
            topple();
    	}
    }
    
    public boolean isStable() {
    	return cells.stream().noneMatch( i -> i >= CELL_LIMIT );
    }
     
    public void topple() {
    	for ( int i = 0; i < CELL_COUNT; i++ ) {
    		if ( cells.get(i) >= CELL_LIMIT ) {
	            cells.set(i, cells.get(i) - CELL_LIMIT);
	            final int row = rowIndex(i);
	            final int col = colIndex(i);
	            if ( row > 0 ) {
	            	increment(row - 1, col);
	            }
	            if ( row + 1 < ROW_COUNT ) {
	                increment(row + 1, col);
	            }
	            if ( col > 0 ) {
	                increment(row, col - 1);
	            }
	            if ( col + 1 < COL_COUNT ) {
	                increment(row, col + 1);
	            }
    		}
	    }
    }
    
    public Sandpile add(Sandpile aOther) {
    	List<Integer> list = new ArrayList<Integer>();
    	for ( int i = 0; i < CELL_COUNT; i++ ) {
            list.add(cells.get(i) + aOther.cells.get(i));
    	}
    	Sandpile result = new Sandpile(list);
        result.stabilise();
        return result;
    }
    
    public boolean equals(Sandpile aOther) {
    	return cells.equals(aOther.cells);
    } 
    
    public void display() {
    	for ( int i = 0; i < CELL_COUNT; i++ ) {
    		System.out.print(cells.get(i));
    		System.out.print( ( colIndex(i + 1) == 0 ) ? System.lineSeparator() : " ");
    	}
    }
  
	private void increment(int aRow, int aCol) {
		final int index = cellIndex(aRow, aCol);
		cells.set(index, cells.get(index) + 1);
	}
    
    private static int cellIndex(int aRow, int aCol) {
        return aRow * COL_COUNT + aCol;
    }
    
    private static int rowIndex(int aCellIndex) {
        return aCellIndex / COL_COUNT;
    }
    
    private static int colIndex(int aCellIndex) {
        return aCellIndex % COL_COUNT;
    }
	
    private List<Integer> cells;

	private static final int ROW_COUNT = 3;
	private static final int COL_COUNT = 3;
	private static final int CELL_COUNT = ROW_COUNT * COL_COUNT;
	private static final int CELL_LIMIT = 4;
	
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product
from collections import defaultdict


class Sandpile():
    def __init__(self, gridtext):
        array = [int(x) for x in gridtext.strip().split()]
        self.grid = defaultdict(int,
                                {(i //3, i % 3): x 
                                 for i, x in enumerate(array)})

    _border = set((r, c) 
                  for r, c in product(range(-1, 4), repeat=2) 
                  if not 0 <= r <= 2 or not 0 <= c <= 2
                  )
    _cell_coords = list(product(range(3), repeat=2))
    
    def topple(self):
        g = self.grid
        for r, c in self._cell_coords:
            if g[(r, c)] >= 4:
                g[(r - 1, c)] += 1
                g[(r + 1, c)] += 1
                g[(r, c - 1)] += 1
                g[(r, c + 1)] += 1
                g[(r, c)] -= 4
                return True
        return False
    
    def stabilise(self):
        while self.topple():
            pass
        # Remove extraneous grid border
        g = self.grid
        for row_col in self._border.intersection(g.keys()):
            del g[row_col]
        return self
    
    __pos__ = stabilise     # +s == s.stabilise()
    
    def __eq__(self, other):
        g = self.grid
        return all(g[row_col] == other.grid[row_col]
                   for row_col in self._cell_coords)

    def __add__(self, other):
        g = self.grid
        ans = Sandpile("")
        for row_col in self._cell_coords:
            ans.grid[row_col] = g[row_col] + other.grid[row_col]
        return ans.stabilise()
       
    def __str__(self):
        g, txt = self.grid, []
        for row in range(3):
            txt.append(' '.join(str(g[(row, col)]) 
                                for col in range(3)))
        return '\n'.join(txt)
    
    def __repr__(self):
        return f'{self.__class__.__name__}(""""\n{self.__str__()}""")'
        

unstable = Sandpile("""
4 3 3
3 1 2
0 2 3""")
s1 = Sandpile("""
    1 2 0
    2 1 1
    0 1 3
""")
s2 = Sandpile("""
    2 1 3
    1 0 1
    0 1 0 
""")
s3 = Sandpile("3 3 3  3 3 3  3 3 3")
s3_id = Sandpile("2 1 2  1 0 1  2 1 2")

```

### python_code_2.txt
```python
'''Abelian Sandpile – Identity'''

from operator import add, eq


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Tests of cascades and additions'''
    s0 = [[4, 3, 3], [3, 1, 2], [0, 2, 3]]
    s1 = [[1, 2, 0], [2, 1, 1], [0, 1, 3]]
    s2 = [[2, 1, 3], [1, 0, 1], [0, 1, 0]]
    s3 = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    s3_id = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]

    series = list(cascadeSeries(s0))
    for expr in [
            'Cascade:',
            showSandPiles(
                [(' ', series[0])] + [
                    (':', xs) for xs in series[1:]
                ]
            ),
            '',
            f's1 + s2 == s2 + s1 -> {addSand(s1)(s2) == addSand(s2)(s1)}',
            showSandPiles([
                (' ', s1),
                ('+', s2),
                ('=', addSand(s1)(s2))
            ]),
            '',
            showSandPiles([
                (' ', s2),
                ('+', s1),
                ('=', addSand(s2)(s1))
            ]),
            '',
            f's3 + s3_id == s3 -> {addSand(s3)(s3_id) == s3}',
            showSandPiles([
                (' ', s3),
                ('+', s3_id),
                ('=', addSand(s3)(s3_id))
            ]),
            '',
            f's3_id + s3_id == s3_id -> {addSand(s3_id)(s3_id) == s3_id}',
            showSandPiles([
                (' ', s3_id),
                ('+', s3_id),
                ('=', addSand(s3_id)(s3_id))
            ]),

    ]:
        print(expr)


# ----------------------- SANDPILES ------------------------

# addSand :: [[Int]] -> [[Int]] -> [[Int]]
def addSand(xs):
    '''The stabilised sum of two sandpiles.
    '''
    def go(ys):
        return cascadeSeries(
            chunksOf(len(xs))(
                map(
                    add,
                    concat(xs),
                    concat(ys)
                )
            )
        )[-1]
    return go


# cascadeSeries :: [[Int]] -> [[[Int]]]
def cascadeSeries(rows):
    '''The sequence of states from a given
       sand pile to a stable condition.
    '''
    xs = list(rows)
    w = len(xs)
    return [
        list(chunksOf(w)(x)) for x
        in convergence(eq)(
            iterate(nextState(w))(
                concat(xs)
            )
        )
    ]


# convergence :: (a -> a -> Bool) -> [a] -> [a]
def convergence(p):
    '''All items of xs to the point where the binary
       p returns True over two successive values.
    '''
    def go(xs):
        def conv(prev, ys):
            y = next(ys)
            return [prev] + (
                [] if p(prev, y) else conv(y, ys)
            )
        return conv(next(xs), xs)
    return go


# nextState Int -> Int -> [Int] -> [Int]
def nextState(w):
    '''The next state of a (potentially unstable)
       flattened sand-pile matrix of row length w.
    '''
    def go(xs):
        def tumble(i):
            neighbours = indexNeighbours(w)(i)
            return [
                1 + k if j in neighbours else (
                    k - (1 + w) if j == i else k
                ) for (j, k) in enumerate(xs)
            ]
        return maybe(xs)(tumble)(
            findIndex(lambda x: w < x)(xs)
        )
    return go


# indexNeighbours :: Int -> Int -> [Int]
def indexNeighbours(w):
    '''Indices vertically and horizontally adjoining the
       given index in a flattened matrix of dimension w.
    '''
    def go(i):
        lastCol = w - 1
        iSqr = (w * w)
        col = i % w
        return [
            j for j in [i - w, i + w]
            if -1 < j < iSqr
        ] + ([i - 1] if 0 != col else []) + (
            [1 + i] if lastCol != col else []
        )
    return go


# ------------------------ DISPLAY -------------------------

# showSandPiles :: [(String, [[Int]])] -> String
def showSandPiles(pairs):
    '''Indented multi-line representation
       of a sequence of matrices, delimited
       by preceding operators or indents.
    '''
    return '\n'.join([
        ' '.join([' '.join(map(str, seq)) for seq in tpl])
        for tpl in zip(*[
            zip(
                *[list(str(pfx).center(len(rows)))]
                + list(zip(*rows))
            )
            for (pfx, rows) in pairs
        ])
    ])


# ------------------------ GENERIC -------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    def go(xs):
        ys = list(xs)
        return (
            ys[i:n + i] for i in range(0, len(ys), n)
        ) if 0 < n else None
    return go


# concat :: [[a]] -> [a]
def concat(xs):
    '''The concatenation of all
       elements in a list.
    '''
    return [x for lst in xs for x in lst]


# findIndex :: (a -> Bool) -> [a] -> Maybe Int
def findIndex(p):
    '''Just the first index at which an
       element in xs matches p,
       or Nothing if no elements match.
    '''
    def go(xs):
        return next(
            (i for (i, x) in enumerate(xs) if p(x)),
            None
        )
    return go


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if x is None,
       or the application of f to x.
    '''
    def go(f):
        def g(x):
            return v if None is x else f(x)
        return g
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

