# Equilibrium index

## Task Link
[Rosetta Code - Equilibrium index](https://rosettacode.org/wiki/Equilibrium_index)

## Java Code
### java_code_1.txt
```java
public class Equlibrium {
	public static void main(String[] args) {
		int[] sequence = {-7, 1, 5, 2, -4, 3, 0};
		equlibrium_indices(sequence);
	}

	public static void equlibrium_indices(int[] sequence){
		//find total sum
		int totalSum = 0;
		for (int n : sequence) {
			totalSum += n;
		}
		//compare running sum to remaining sum to find equlibrium indices
		int runningSum = 0;
		for (int i = 0; i < sequence.length; i++) {
			int n = sequence[i];
			if (totalSum - runningSum - n == runningSum) {
				System.out.println(i);
			}
			runningSum += n;
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
def eqindex2Pass(data):
    "Two pass"
    suml, sumr, ddelayed = 0, sum(data), 0
    for i, d in enumerate(data):
        suml += ddelayed
        sumr -= d
        ddelayed = d
        if suml == sumr:
            yield i

```

### python_code_2.txt
```python
def eqindexMultiPass(data):
    "Multi pass"
    for i in range(len(data)):
        suml, sumr = sum(data[:i]), sum(data[i+1:])
        if suml == sumr:
            yield i

```

### python_code_3.txt
```python
def eqindexMultiPass(s):
    return [i for i in xrange(len(s)) if sum(s[:i]) == sum(s[i+1:])]

print eqindexMultiPass([-7, 1, 5, 2, -4, 3, 0])

```

### python_code_4.txt
```python
from collections import defaultdict

def eqindex1Pass(data):
    "One pass"
    l, h = 0, defaultdict(list)
    for i, c in enumerate(data):
        l += c
        h[l * 2 - c].append(i)
    return h[l]

```

### python_code_5.txt
```python
f = (eqindex2Pass, eqindexMultiPass, eqindex1Pass)
d = ([-7, 1, 5, 2, -4, 3, 0],
     [2, 4, 6],
     [2, 9, 2],
     [1, -1, 1, -1, 1, -1, 1])

for data in d:
    print("d = %r" % data)
    for func in f:
        print("  %16s(d) -> %r" % (func.__name__, list(func(data))))

```

### python_code_6.txt
```python
"""Equilibrium index"""

from itertools import (accumulate)


# equilibriumIndices :: [Num] -> [Int]
def equilibriumIndices(xs):
    '''List indices at which the sum of values to the left
       equals the sum of values to the right.
    '''
    def go(xs):
        '''Left scan from accumulate,
           right scan derived from left
        '''
        ls = list(accumulate(xs))
        n = ls[-1]
        return [
            i for (i, (x, y)) in enumerate(zip(
                ls,
                [n] + [n - x for x in ls[0:-1]]
            )) if x == y
        ]
    return go(xs) if xs else []


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tabulated test results'''
    print(
        tabulated('Equilibrium indices:\n')(
            equilibriumIndices
        )([
            [-7, 1, 5, 2, -4, 3, 0],
            [2, 4, 6],
            [2, 9, 2],
            [1, -1, 1, -1, 1, -1, 1],
            [1],
            []
        ])
    )


# ----------------------- GENERIC ------------------------

# tabulated :: String -> (a -> b) -> [a] -> String
def tabulated(s):
    '''heading -> function -> input List
       -> tabulated output string
    '''
    def go(f):
        def width(x):
            return len(str(x))
        def cols(xs):
            w = width(max(xs, key=width))
            return s + '\n' + '\n'.join([
                str(x).rjust(w, ' ') + ' -> ' + str(f(x))
                for x in xs
            ])
        return cols
    return go


if __name__ == '__main__':
    main()

```

