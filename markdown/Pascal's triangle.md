# Pascal's triangle

## Task Link
[Rosetta Code - Pascal's triangle](https://rosettacode.org/wiki/Pascal%27s_triangle)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
...//class definition, etc.
public static void genPyrN(int rows){
	if(rows < 0) return;
	//save the last row here
	ArrayList<Integer> last = new ArrayList<Integer>();
	last.add(1);
	System.out.println(last);
	for(int i= 1;i <= rows;++i){
		//work on the next row
		ArrayList<Integer> thisRow= new ArrayList<Integer>();
		thisRow.add(last.get(0)); //beginning
		for(int j= 1;j < i;++j){//loop the number of elements in this row
			//sum from the last row
			thisRow.add(last.get(j - 1) + last.get(j));
		}
		thisRow.add(last.get(0)); //end
		last= thisRow;//save this row
		System.out.println(thisRow);
	}
}

```

### java_code_2.txt
```java
public class Pas{
	public static void main(String[] args){
		//usage
		pas(20);
	}

	public static void pas(int rows){
		for(int i = 0; i < rows; i++){
			for(int j = 0; j <= i; j++){
				System.out.print(ncr(i, j) + " ");
			}
			System.out.println();
		}
	}

	public static long ncr(int n, int r){
		return fact(n) / (fact(r) * fact(n - r));
	}

	public static long fact(int n){
		long ans = 1;
		for(int i = 2; i <= n; i++){
			ans *= i;
		}
		return ans;
	}
}

```

### java_code_3.txt
```java
public class Pascal {
	private static void printPascalLine (int n) {
		if (n < 1)
			return;
		int m = 1;
		System.out.print("1 ");
		for (int j=1; j<n; j++) {
			m = m * (n-j)/j;
			System.out.print(m);
			System.out.print(" ");
		}
		System.out.println();
	}
	
	public static void printPascal (int nRows) {
		for(int i=1; i<=nRows; i++)
			printPascalLine(i);
	}
}

```

## Python Code
### python_code_1.txt
```python
def pascal(n):
   """Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success."""
   row = [1]
   k = [0]
   for x in range(max(n,0)):
      print row
      row=[l+r for l,r in zip(row+k,k+row)]
   return n>=1

```

### python_code_2.txt
```python
def scan(op, seq, it):
  a = []
  result = it
  a.append(it)
  for x in seq:
    result = op(result, x)
    a.append(result)
  return a

def pascal(n):
    def nextrow(row, x):
        return [l+r for l,r in zip(row+[0,],[0,]+row)]

    return scan(nextrow, range(n-1), [1,])

for row in pascal(4):
    print(row)

```

### python_code_3.txt
```python
'''Pascal's triangle'''

from itertools import (accumulate, chain, islice)
from operator import (add)


# nextPascal :: [Int] -> [Int]
def nextPascal(xs):
    '''A row of Pascal's triangle
       derived from a preceding row.'''
    return list(
        map(add, [0] + xs, xs + [0])
    )


# pascalTriangle :: Generator [[Int]]
def pascalTriangle():
    '''A non-finite stream of
       Pascal's triangle rows.'''
    return iterate(nextPascal)([1])


# finitePascalRows :: Int -> [[Int]]
def finitePascalRows(n):
    '''The first n rows of Pascal's triangle.'''
    return accumulate(
        chain(
            [[1]], range(1, n)
        ),
        lambda a, _: nextPascal(a)
    )


# ------------------------ TESTS -------------------------
# main :: IO ()
def main():
    '''Test of two different approaches:
        - taking from a non-finite stream of rows,
        - or constructing a finite list of rows.'''
    print('\n'.join(map(
        showPascal,
        [
            islice(
                pascalTriangle(),       # Non finite,
                7
            ),
            finitePascalRows(7)         # finite.
        ]
    )))


# showPascal :: [[Int]] -> String
def showPascal(xs):
    '''Stringification of a list of
       Pascal triangle rows.'''
    ys = list(xs)

    def align(w):
        return lambda ns: center(w)(
            ' '
        )('   '.join(map(str, ns)))

    w = len('   '.join((map(str, ys[-1]))))
    return '\n'.join(map(align(w), ys))


# ----------------------- GENERIC ------------------------

# center :: Int -> Char -> String -> String
def center(n):
    '''String s padded with c to approximate centre,
       fitting in but not truncated to width n.'''
    def go(c, s):
        qr = divmod(n - len(s), 2)
        q = qr[0]
        return (q * c) + s + ((q + qr[1]) * c)

    return lambda c: lambda s: go(c, s)


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


# MAIN ---
if __name__ == '__main__':
    main()

```

