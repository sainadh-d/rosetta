# Floyd's triangle

## Task Link
[Rosetta Code - Floyd's triangle](https://rosettacode.org/wiki/Floyd%27s_triangle)

## Java Code
### java_code_1.txt
```java
public class Floyd {
	public static void main(String[] args){
		printTriangle(5);
		printTriangle(14);
	}
	
	private static void printTriangle(int n){
		System.out.println(n + " rows:");
		for(int rowNum = 1, printMe = 1, numsPrinted = 0;
				rowNum <= n; printMe++){
			int cols = (int)Math.ceil(Math.log10(n*(n-1)/2 + numsPrinted + 2));
			System.out.printf("%"+cols+"d ", printMe);
			if(++numsPrinted == rowNum){
				System.out.println();
				rowNum++;
				numsPrinted = 0;
			}
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def floyd(rowcount=5):
	rows = [[1]]
	while len(rows) < rowcount:
		n = rows[-1][-1] + 1
		rows.append(list(range(n, n + len(rows[-1]) + 1)))
	return rows

>>> floyd()
[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
>>> def pfloyd(rows=[[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]):
	colspace = [len(str(n)) for n in rows[-1]]
	for row in rows:
		print( ' '.join('%*i' % space_n for space_n in zip(colspace, row)))

		
>>> pfloyd()
1
2 3
4 5 6
7 8 9 10
>>> pfloyd(floyd(5))
 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
>>> pfloyd(floyd(14))
 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44  45
46 47 48 49 50 51 52 53  54  55
56 57 58 59 60 61 62 63  64  65  66
67 68 69 70 71 72 73 74  75  76  77  78
79 80 81 82 83 84 85 86  87  88  89  90  91
92 93 94 95 96 97 98 99 100 101 102 103 104 105
>>>

```

### python_code_2.txt
```python
def floyd(rowcount=5):
    return [list(range(i * (i - 1) // 2 + 1, i * (i + 1) // 2 + 1))
            for i in range(1, rowcount + 1)]

```

### python_code_3.txt
```python
'''Floyd triangle in terms of concatMap'''

from itertools import chain


# floyd :: Int -> [[Int]]
def floyd(n):
    '''n rows of a Floyd triangle.'''
    def f(i):
        return [
            enumFromTo(i * pred(i) // 2 + 1)(
                i * succ(i) // 2
            )
        ]
    return concatMap(f)(enumFromTo(1)(n))


# main :: IO ()
def main():
    '''Test'''
    print(unlines(
        map(str, floyd(5))
    ))


# GENERIC FUNCTIONS ---------------------------------------


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''Concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# pred ::  Enum a => a -> a
def pred(x):
    '''The predecessor of a value. For numeric types, (- 1).'''
    return x - 1 if isinstance(x, int) else (
        chr(ord(x) - 1)
    )


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value. For numeric types, (1 +).'''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
'''Floyd triangle in terms of iterate(f)(x)'''

from itertools import islice


# floyd :: Int -> [[Int]]
def floyd(n):
    '''n rows of a Floyd triangle.'''
    return take(n)(iterate(nextFloyd)([1]))


# nextFloyd :: [Int] -> [Int]
def nextFloyd(xs):
    '''A Floyd triangle row derived from
       the preceding row.'''
    n = succ(len(xs))
    return [1] if n < 2 else (
        enumFromTo(succ(n * pred(n) // 2))(
            n * succ(n) // 2
        )
    )


# showFloyd :: [[Int]] -> String
def showFloyd(xs):
    '''A stringification of Floyd triangle rows.'''
    return unlines(str(x) for x in xs)


# main :: IO ()
def main():
    '''Test'''
    print(showFloyd(
        floyd(5)
    ))


# GENERIC ABSTRACTIONS ------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated applications of f to x.'''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)


# pred ::  Enum a => a -> a
def pred(x):
    '''The predecessor of a value. For numeric types, (- 1).'''
    return x - 1 if isinstance(x, int) else (
        chr(ord(x) - 1)
    )


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value. For numeric types, (1 +).'''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# MAIN ----------------------------------------------------
if __name__ == '__main__':
    main()

```

