# Fibonacci n-step number sequences

## Task Link
[Rosetta Code - Fibonacci n-step number sequences](https://rosettacode.org/wiki/Fibonacci_n-step_number_sequences)

## Java Code
### java_code_1.txt
```java
class Fibonacci
{
  public static int[] lucas(int n, int numRequested)
  {
    if (n < 2)
      throw new IllegalArgumentException("Fibonacci value must be at least 2");
    return fibonacci((n == 2) ? new int[] { 2, 1 } : lucas(n - 1, n), numRequested);
  }
  
  public static int[] fibonacci(int n, int numRequested)
  {
    if (n < 2)
      throw new IllegalArgumentException("Fibonacci value must be at least 2");
    return fibonacci((n == 2) ? new int[] { 1, 1 } : fibonacci(n - 1, n), numRequested);
  }
  
  public static int[] fibonacci(int[] startingValues, int numRequested)
  {
    int[] output = new int[numRequested];
    int n = startingValues.length;
    System.arraycopy(startingValues, 0, output, 0, n);
    for (int i = n; i < numRequested; i++)
      for (int j = 1; j <= n; j++)
        output[i] += output[i - j];
    return output;
  }
  
  public static void main(String[] args)
  {
    for (int n = 2; n <= 10; n++)
    {
      System.out.print("nacci(" + n + "):");
      for (int value : fibonacci(n, 15))
        System.out.print(" " + value);
      System.out.println();
    }
    for (int n = 2; n <= 10; n++)
    {
      System.out.print("lucas(" + n + "):");
      for (int value : lucas(n, 15))
        System.out.print(" " + value);
      System.out.println();
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> def fiblike(start):
	addnum = len(start)
	memo = start[:]
	def fibber(n):
		try:
			return memo[n]
		except IndexError:
			ans = sum(fibber(i) for i in range(n-addnum, n))
			memo.append(ans)
			return ans
	return fibber

>>> fibo = fiblike([1,1])
>>> [fibo(i) for i in range(10)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> lucas = fiblike([2,1])
>>> [lucas(i) for i in range(10)]
[2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
>>> for n, name in zip(range(2,11), 'fibo tribo tetra penta hexa hepta octo nona deca'.split()) :
	fibber = fiblike([1] + [2**i for i in range(n-1)])
	print('n=%2i, %5snacci -> %s ...' % (n, name, ' '.join(str(fibber(i)) for i in range(15))))

	
n= 2,  fibonacci -> 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 ...
n= 3, tribonacci -> 1 1 2 4 7 13 24 44 81 149 274 504 927 1705 3136 ...
n= 4, tetranacci -> 1 1 2 4 8 15 29 56 108 208 401 773 1490 2872 5536 ...
n= 5, pentanacci -> 1 1 2 4 8 16 31 61 120 236 464 912 1793 3525 6930 ...
n= 6,  hexanacci -> 1 1 2 4 8 16 32 63 125 248 492 976 1936 3840 7617 ...
n= 7, heptanacci -> 1 1 2 4 8 16 32 64 127 253 504 1004 2000 3984 7936 ...
n= 8,  octonacci -> 1 1 2 4 8 16 32 64 128 255 509 1016 2028 4048 8080 ...
n= 9,  nonanacci -> 1 1 2 4 8 16 32 64 128 256 511 1021 2040 4076 8144 ...
n=10,  decanacci -> 1 1 2 4 8 16 32 64 128 256 512 1023 2045 4088 8172 ...
>>>

```

### python_code_2.txt
```python
>>> class Fiblike():
	def __init__(self, start):
		self.addnum = len(start)
		self.memo = start[:]
	def __call__(self, n):
		try:
			return self.memo[n]
		except IndexError:
			ans = sum(self(i) for i in range(n-self.addnum, n))
			self.memo.append(ans)
			return ans

		
>>> fibo = Fiblike([1,1])
>>> [fibo(i) for i in range(10)]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> lucas = Fiblike([2,1])
>>> [lucas(i) for i in range(10)]
[2, 1, 3, 4, 7, 11, 18, 29, 47, 76]
>>> for n, name in zip(range(2,11), 'fibo tribo tetra penta hexa hepta octo nona deca'.split()) :
	fibber = Fiblike([1] + [2**i for i in range(n-1)])
	print('n=%2i, %5snacci -> %s ...' % (n, name, ' '.join(str(fibber(i)) for i in range(15))))

	
n= 2,  fibonacci -> 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 ...
n= 3, tribonacci -> 1 1 2 4 7 13 24 44 81 149 274 504 927 1705 3136 ...
n= 4, tetranacci -> 1 1 2 4 8 15 29 56 108 208 401 773 1490 2872 5536 ...
n= 5, pentanacci -> 1 1 2 4 8 16 31 61 120 236 464 912 1793 3525 6930 ...
n= 6,  hexanacci -> 1 1 2 4 8 16 32 63 125 248 492 976 1936 3840 7617 ...
n= 7, heptanacci -> 1 1 2 4 8 16 32 64 127 253 504 1004 2000 3984 7936 ...
n= 8,  octonacci -> 1 1 2 4 8 16 32 64 128 255 509 1016 2028 4048 8080 ...
n= 9,  nonanacci -> 1 1 2 4 8 16 32 64 128 256 511 1021 2040 4076 8144 ...
n=10,  decanacci -> 1 1 2 4 8 16 32 64 128 256 512 1023 2045 4088 8172 ...
>>>

```

### python_code_3.txt
```python
from itertools import islice, cycle

def fiblike(tail):
    for x in tail:
        yield x
    for i in cycle(xrange(len(tail))):
        tail[i] = x = sum(tail)
        yield x

fibo = fiblike([1, 1])
print list(islice(fibo, 10))
lucas = fiblike([2, 1])
print list(islice(lucas, 10))

suffixes = "fibo tribo tetra penta hexa hepta octo nona deca"
for n, name in zip(xrange(2, 11), suffixes.split()):
    fib = fiblike([1] + [2 ** i for i in xrange(n - 1)])
    items = list(islice(fib, 15))
    print "n=%2i, %5snacci -> %s ..." % (n, name, items)

```

### python_code_4.txt
```python
'''Fibonacci n-step number sequences'''

from itertools import chain, count, islice


# A000032 :: () -> [Int]
def A000032():
    '''Non finite sequence of Lucas numbers.
    '''
    return unfoldr(recurrence(2))([2, 1])


# nStepFibonacci :: Int -> [Int]
def nStepFibonacci(n):
    '''Non-finite series of N-step Fibonacci numbers,
       defined by a recurrence relation.
    '''
    return unfoldr(recurrence(n))(
        take(n)(
            chain(
                [1],
                (2 ** i for i in count(0))
            )
        )
    )


# recurrence :: Int -> [Int] -> Int
def recurrence(n):
    '''Recurrence relation in Fibonacci and related series.
    '''
    def go(xs):
        h, *t = xs
        return h, t + [sum(take(n)(xs))]
    return go


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 15 terms each n-step Fibonacci(n) series
       where n is drawn from [2..8]
    '''
    labels = "fibo tribo tetra penta hexa hepta octo nona deca"
    table = list(
        chain(
            [['lucas:'] + [
                str(x) for x in take(15)(A000032())]
             ],
            map(
                lambda k, n: list(
                    chain(
                        [k + 'nacci:'],
                        (
                            str(x) for x
                            in take(15)(nStepFibonacci(n))
                        )
                    )
                ),
                labels.split(),
                count(2)
            )
        )
    )
    print('Recurrence relation series:\n')
    print(
        spacedTable(table)
    )


# ----------------------- GENERIC ------------------------

# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Generic anamorphism.
       A lazy (generator) list unfolded from a seed value by
       repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None, or just (value, residue).
       For a strict output value, wrap in list().
    '''
    def go(x):
        valueResidue = f(x)
        while None is not valueResidue:
            yield valueResidue[0]
            valueResidue = f(valueResidue[1])
    return go


# ---------------------- FORMATTING ----------------------

# spacedTable :: [[String]] -> String
def spacedTable(rows):
    columnWidths = [
        max([len(x) for x in col])
        for col in zip(*rows)
    ]
    return '\n'.join([
        ' '.join(
            map(
                lambda x, w: x.rjust(w, ' '),
                row, columnWidths
            )
        )
        for row in rows
    ])


# MAIN ---
if __name__ == '__main__':
    main()

```

