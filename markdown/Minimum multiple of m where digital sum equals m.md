# Minimum multiple of m where digital sum equals m

## Task Link
[Rosetta Code - Minimum multiple of m where digital sum equals m](https://rosettacode.org/wiki/Minimum_multiple_of_m_where_digital_sum_equals_m)

## Java Code
### java_code_1.txt
```java
public final class MinimumMultipleDigitSum {

	public static void main(String[] aArgs) {
		for ( int n = 1; n <= 70; n++ ) {
			int k = 0;
			while ( digitSum(k += n) != n );
			System.out.print(String.format("%8d%s", k / n, ( n % 10 ) == 0 ? "\n" : " "));
		}
	}
	
	private static int digitSum(int aN) {
		int sum = 0;
		while ( aN > 0 ) {
			sum += aN % 10;
			aN /= 10;
		}
		return sum;
	}

}

```

## Python Code
### python_code_1.txt
```python
'''A131382'''

from itertools import count, islice


# a131382 :: [Int]
def a131382():
    '''An infinite series of the terms of A131382'''
    return (
        elemIndex(x)(
            productDigitSums(x)
        ) for x in count(1)
    )


# productDigitSums :: Int -> [Int]
def productDigitSums(n):
    '''The sum of the decimal digits of n'''
    return (digitSum(n * x) for x in count(0))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 40 terms of A131382'''

    print(
        table(10)([
            str(x) for x in islice(
                a131382(),
                40
            )
        ])
    )


# ----------------------- GENERIC ------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divisible, the final list will be shorter than n.
    '''
    def go(xs):
        return (
            xs[i:n + i] for i in range(0, len(xs), n)
        ) if 0 < n else None
    return go


# digitSum :: Int -> Int
def digitSum(n):
    '''The sum of the digital digits of n.
    '''
    return sum(int(x) for x in list(str(n)))


# elemIndex :: a -> [a] -> (None | Int)
def elemIndex(x):
    '''Just the first index of x in xs,
       or None if no elements match.
    '''
    def go(xs):
        try:
            return next(
                i for i, v in enumerate(xs) if x == v
            )
        except StopIteration:
            return None
    return go


# table :: Int -> [String] -> String
def table(n):
    '''A list of strings formatted as
       right-justified rows of n columns.
    '''
    def go(xs):
        w = len(xs[-1])
        return '\n'.join(
            ' '.join(row) for row in chunksOf(n)([
                s.rjust(w, ' ') for s in xs
            ])
        )
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

