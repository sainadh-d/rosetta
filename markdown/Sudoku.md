# Sudoku

## Task Link
[Rosetta Code - Sudoku](https://rosettacode.org/wiki/Sudoku)

## Java Code
### java_code_1.txt
```java
public class Sudoku
{
    private int mBoard[][];
    private int mBoardSize;
    private int mBoxSize;
    private boolean mRowSubset[][];
    private boolean mColSubset[][];
    private boolean mBoxSubset[][];
 
    public Sudoku(int board[][]) {
        mBoard = board;
        mBoardSize = mBoard.length;
        mBoxSize = (int)Math.sqrt(mBoardSize);
        initSubsets();
    }
 
    public void initSubsets() {
        mRowSubset = new boolean[mBoardSize][mBoardSize];
        mColSubset = new boolean[mBoardSize][mBoardSize];
        mBoxSubset = new boolean[mBoardSize][mBoardSize];
        for(int i = 0; i < mBoard.length; i++) {
            for(int j = 0; j < mBoard.length; j++) {
                int value = mBoard[i][j];
                if(value != 0) {
                    setSubsetValue(i, j, value, true);
                }
            }
        }
    }
 
    private void setSubsetValue(int i, int j, int value, boolean present) {
        mRowSubset[i][value - 1] = present;
        mColSubset[j][value - 1] = present;
        mBoxSubset[computeBoxNo(i, j)][value - 1] = present;
    }
 
    public boolean solve() {
        return solve(0, 0);
    }
 
    public boolean solve(int i, int j) {
        if(i == mBoardSize) {
            i = 0;
            if(++j == mBoardSize) {
                return true;
            }
        }
        if(mBoard[i][j] != 0) {
            return solve(i + 1, j);
        }
        for(int value = 1; value <= mBoardSize; value++) {
            if(isValid(i, j, value)) {
                mBoard[i][j] = value;
                setSubsetValue(i, j, value, true);
                if(solve(i + 1, j)) {
                    return true;
                }
                setSubsetValue(i, j, value, false);
            }
        }
 
        mBoard[i][j] = 0;
        return false;
    }
 
    private boolean isValid(int i, int j, int val) {
        val--;
        boolean isPresent = mRowSubset[i][val] || mColSubset[j][val] || mBoxSubset[computeBoxNo(i, j)][val];
        return !isPresent;
    }
 
    private int computeBoxNo(int i, int j) {
        int boxRow = i / mBoxSize;
        int boxCol = j / mBoxSize;
        return boxRow * mBoxSize + boxCol;
    }
 
    public void print() {
        for(int i = 0; i < mBoardSize; i++) {
            if(i % mBoxSize == 0) {
                System.out.println(" -----------------------");
            }
            for(int j = 0; j < mBoardSize; j++) {
                if(j % mBoxSize == 0) {
                    System.out.print("| ");
                }
                System.out.print(mBoard[i][j] != 0 ? ((Object) (Integer.valueOf(mBoard[i][j]))) : "-");
                System.out.print(' ');
            }
 
            System.out.println("|");
        }
 
        System.out.println(" -----------------------");
    }

    public static void main(String[] args) {
        int[][] board = { 
            {8, 5, 0, 0, 0, 2, 4, 0, 0},
            {7, 2, 0, 0, 0, 0, 0, 0, 9},
            {0, 0, 4, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 1, 0, 7, 0, 0, 2},
            {3, 0, 5, 0, 0, 0, 9, 0, 0},
            {0, 4, 0, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 8, 0, 0, 7, 0},
            {0, 1, 7, 0, 0, 0, 0, 0, 0},
            {0, 0, 0, 0, 3, 6, 0, 4, 0}
        };
        Sudoku s = new Sudoku(board);
        System.out.print("Starting grid:\n");
        s.print();        
        if (s.solve()) {
            System.out.print("\nSolution:\n");
            s.print();
        } else {
            System.out.println("\nUnsolvable!");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def initiate():
    box.append([0, 1, 2, 9, 10, 11, 18, 19, 20])
    box.append([3, 4, 5, 12, 13, 14, 21, 22, 23])
    box.append([6, 7, 8, 15, 16, 17, 24, 25, 26])
    box.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
    box.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
    box.append([33, 34, 35, 42, 43, 44, 51, 52, 53])
    box.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
    box.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
    box.append([60, 61, 62, 69, 70, 71, 78, 79, 80])
    for i in range(0, 81, 9):
        row.append(range(i, i+9))
    for i in range(9):
        column.append(range(i, 80+i, 9))

def valid(n, pos):
    current_row = pos/9
    current_col = pos%9
    current_box = (current_row/3)*3 + (current_col/3)
    for i in row[current_row]:
        if (grid[i] == n):
            return False
    for i in column[current_col]:
        if (grid[i] == n):
            return False
    for i in box[current_box]:
        if (grid[i] == n):
            return False
    return True

def solve():
    i = 0
    proceed = 1
    while(i < 81):
        if given[i]:
            if proceed:
                    i += 1
            else:
                i -= 1
        else:
            n = grid[i]
            prev = grid[i]
            while(n < 9):
              if (n < 9):
                  n += 1
              if valid(n, i):
                  grid[i] = n
                  proceed = 1
                  break
            if (grid[i] == prev):
               grid[i] = 0
               proceed = 0
            if proceed:
               i += 1
            else:
               i -=1

def inputs():
    nextt = 'T'
    number = 0
    pos = 0
    while(not(nextt == 'N' or nextt == 'n')):
        print "Enter the position:",
        pos = int(raw_input())
        given[pos - 1] = True
        print "Enter the numerical:",
        number = int(raw_input())
        grid[pos - 1] = number
        print "Do you want to enter another given?(Y, for yes: N, for no)"
        nextt = raw_input()


grid = [0]*81
given = [False]*81
box = []
row = []
column = []
initiate()
inputs()
solve()
for i in range(9):
    print grid[i*9:i*9+9]
raw_input()

```

