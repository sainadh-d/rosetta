# Hailstone sequence

## Task Link
[Rosetta Code - Hailstone sequence](https://rosettacode.org/wiki/Hailstone_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Hailstone {

  public static List<Long> getHailstoneSequence(long n) {
    if (n <= 0)
      throw new IllegalArgumentException("Invalid starting sequence number");
    List<Long> list = new ArrayList<Long>();
    list.add(Long.valueOf(n));
    while (n != 1) {
      if ((n & 1) == 0)
        n = n / 2;
      else
        n = 3 * n + 1;
      list.add(Long.valueOf(n));
    }
    return list;
  }
  
  public static void main(String[] args) {
    List<Long> sequence27 = getHailstoneSequence(27);
    System.out.println("Sequence for 27 has " + sequence27.size() + " elements: " + sequence27);
    
    long MAX = 100000;
    // Simple way
    {
      long highestNumber = 1;
      int highestCount = 1;
      for (long i = 2; i < MAX; i++) {
        int count = getHailstoneSequence(i).size();
        if (count > highestCount) {
          highestCount = count;
          highestNumber = i;
        }
      }
      System.out.println("Method 1, number " + highestNumber + " has the longest sequence, with a length of " + highestCount);
    }
    
    // More memory efficient way
    {
      long highestNumber = 1;
      int highestCount = 1;
      for (long i = 2; i < MAX; i++) {
        int count = 1;
        long n = i;
        while (n != 1) {
          if ((n & 1) == 0)
            n = n / 2;
          else
            n = 3 * n + 1;
          count++;
        }
        if (count > highestCount) {
          highestCount = count;
          highestNumber = i;
        }
      }
      System.out.println("Method 2, number " + highestNumber + " has the longest sequence, with a length of " + highestCount);
    }
    
    // Efficient for analyzing all sequences
    {
      long highestNumber = 1;
      long highestCount = 1;
      Map<Long, Integer> sequenceMap = new HashMap<Long, Integer>();
      sequenceMap.put(Long.valueOf(1), Integer.valueOf(1));
      
      List<Long> currentList = new ArrayList<Long>();
      for (long i = 2; i < MAX; i++) {
        currentList.clear();
        Long n = Long.valueOf(i);
        Integer count = null;
        while ((count = sequenceMap.get(n)) == null) {
          currentList.add(n);
          long nValue = n.longValue();
          if ((nValue & 1) == 0)
            n = Long.valueOf(nValue / 2);
          else
            n = Long.valueOf(3 * nValue + 1);
        }
        int curCount = count.intValue();
        for (int j = currentList.size() - 1; j >= 0; j--)
          sequenceMap.put(currentList.get(j), Integer.valueOf(++curCount));
        if (curCount > highestCount) {
          highestCount = curCount;
          highestNumber = i;
        }
      }
      System.out.println("Method 3, number " + highestNumber + " has the longest sequence, with a length of " + highestCount);
    }
    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
def hailstone(n):
    seq = [n]
    while n > 1:
        n = 3 * n + 1 if n & 1 else n // 2
        seq.append(n)
    return seq


if __name__ == '__main__':
    h = hailstone(27)
    assert (len(h) == 112
            and h[:4] == [27, 82, 41, 124]
            and h[-4:] == [8, 4, 2, 1])
    max_length, n = max((len(hailstone(i)), i) for i in range(1, 100_000))
    print(f"Maximum length {max_length} was found for hailstone({n}) "
          f"for numbers <100,000")

```

### python_code_2.txt
```python
from itertools import islice


def hailstone(n):
    yield n
    while n > 1:
        n = 3 * n + 1 if n & 1 else n // 2
        yield n


if __name__ == '__main__':
    h = hailstone(27)
    assert list(islice(h, 4)) == [27, 82, 41, 124]
    for _ in range(112 - 4 * 2):
        next(h)
    assert list(islice(h, 4)) == [8, 4, 2, 1]
    max_length, n = max((sum(1 for _ in hailstone(i)), i)
                        for i in range(1, 100_000))
    print(f"Maximum length {max_length} was found for hailstone({n}) "
          f"for numbers <100,000")

```

### python_code_3.txt
```python
'''Hailstone sequences'''

from itertools import (islice, takewhile)


# hailstone :: Int -> [Int]
def hailstone(x):
    '''Hailstone sequence starting with x.'''
    def p(n):
        return 1 != n
    return list(takewhile(p, iterate(collatz)(x))) + [1]


# collatz :: Int -> Int
def collatz(n):
    '''Next integer in the hailstone sequence.'''
    return 3 * n + 1 if 1 & n else n // 2


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Tests.'''

    n = 27
    xs = hailstone(n)
    print(unlines([
        f'The hailstone sequence for {n} has {len(xs)} elements,',
        f'starting with {take(4)(xs)},',
        f'and ending with {drop(len(xs) - 4)(xs)}.\n'
    ]))

    (a, b) = (1, 99999)
    (i, x) = max(
        enumerate(
            map(compose(len)(hailstone), enumFromTo(a)(b))
        ),
        key=snd
    )
    print(unlines([
        f'The number in the range {a}..{b} '
        f'which produces the longest sequence is {1 + i},',
        f'generating a hailstone sequence of {x} integers.'
    ]))


# ----------------------- GENERIC ------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.
    '''
    def go(xs):
        if isinstance(xs, (list, tuple, str)):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return go


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: range(m, 1 + n)


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


# snd :: (a, b) -> b
def snd(tpl):
    '''Second component of a tuple.'''
    return tpl[1]


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


# unlines :: [String] -> String
def unlines(xs):
    '''A single newline-delimited string derived
       from a list of strings.'''
    return '\n'.join(xs)


if __name__ == '__main__':
    main()

```

