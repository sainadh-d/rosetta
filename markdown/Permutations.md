# Permutations

## Task Link
[Rosetta Code - Permutations](https://rosettacode.org/wiki/Permutations)

## Java Code
### java_code_2.txt
```java
public class PermutationGenerator {
    private int[] array;
    private int firstNum;
    private boolean firstReady = false;

    public PermutationGenerator(int n, int firstNum_) {
        if (n < 1) {
            throw new IllegalArgumentException("The n must be min. 1");
        }
        firstNum = firstNum_;
        array = new int[n];
        reset();
    }

    public void reset() {
        for (int i = 0; i < array.length; i++) {
            array[i] = i + firstNum;
        }
        firstReady = false;
    }

    public boolean hasMore() {
        boolean end = firstReady;
        for (int i = 1; i < array.length; i++) {
            end = end && array[i] < array[i-1];
        }
        return !end;
    }

    public int[] getNext() {

        if (!firstReady) {
            firstReady = true;
            return array;
        }

        int temp;
        int j = array.length - 2;
        int k = array.length - 1;

        // Find largest index j with a[j] < a[j+1]

        for (;array[j] > array[j+1]; j--);

        // Find index k such that a[k] is smallest integer
        // greater than a[j] to the right of a[j]

        for (;array[j] > array[k]; k--);

        // Interchange a[j] and a[k]

        temp = array[k];
        array[k] = array[j];
        array[j] = temp;

        // Put tail end of permutation after jth position in increasing order

        int r = array.length - 1;
        int s = j + 1;

        while (r > s) {
            temp = array[s];
            array[s++] = array[r];
            array[r--] = temp;
        }

        return array;
    } // getNext()

    // For testing of the PermutationGenerator class
    public static void main(String[] args) {
        PermutationGenerator pg = new PermutationGenerator(3, 1);

        while (pg.hasMore()) {
            int[] temp =  pg.getNext();
            for (int i = 0; i < temp.length; i++) {
                System.out.print(temp[i] + " ");
            }
            System.out.println();
        }
    }

} // class

```

### java_code_3.txt
```java
public class Permutations {
	public static void main(String[] args) {
		System.out.println(Utils.Permutations(Utils.mRange(1, 3)));
	}
}

```

## Python Code
### python_code_1.txt
```python
import itertools
for values in itertools.permutations([1,2,3]):
    print (values)

```

### python_code_2.txt
```python
def perm1(n):
    a = list(range(n))
    def sub(i):
        if i == n - 1:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                yield from sub(i + 1)
                a[i], a[k] = a[k], a[i]
    yield from sub(0)

def perm2(n):
    a = list(range(n))
    def sub(i):
        if i == n - 1:
            yield tuple(a)
        else:
            for k in range(i, n):
                a[i], a[k] = a[k], a[i]
                yield from sub(i + 1)
            x = a[i]
            for k in range(i + 1, n):
                a[k - 1] = a[k]
            a[n - 1] = x
    yield from sub(0)

```

### python_code_3.txt
```python
for u in perm1(3): print(u)
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 1, 0)
(2, 0, 1)

for u in perm2(3): print(u)
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)

```

### python_code_4.txt
```python
def nextperm(a):
    n = len(a)
    i = n - 1
    while i > 0 and a[i - 1] > a[i]:
        i -= 1
    j = i
    k = n - 1
    while j < k:
        a[j], a[k] = a[k], a[j]
        j += 1
        k -= 1
    if i == 0:
        return False
    else:
        j = i
        while a[j] < a[i - 1]:
            j += 1
        a[i - 1], a[j] = a[j], a[i - 1]
        return True

def perm3(n):
    if type(n) is int:
        if n < 1:
            return []
        a = list(range(n))
    else:
        a = sorted(n)
    u = [tuple(a)]
    while nextperm(a):
        u.append(tuple(a))
    return u

for p in perm3(3): print(p)
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0)
(2, 0, 1)
(2, 1, 0)

```

### python_code_5.txt
```python
def permutations(xs):
    ac = [[]]
    for x in xs:
        ac_new = []
        for ts in ac:
            for n in range(0,ts.__len__()+1):
                new_ts = ts[:]  #(shallow) copy of ts
                new_ts.insert(n,x)
                ac_new.append(new_ts)
        ac=ac_new
    return ac

print(permutations([1,2,3,4]))

```

### python_code_6.txt
```python
'''Permutations of a list, string or tuple'''

from functools import (reduce)
from itertools import (chain)


# permutations :: [a] -> [[a]]
def permutations(xs):
    '''Type-preserving permutations of xs.
    '''
    ps = reduce(
        lambda a, x: concatMap(
            lambda xs: (
                xs[n:] + [x] + xs[0:n] for n in range(0, 1 + len(xs)))
        )(a),
        xs, [[]]
    )
    t = type(xs)
    return ps if list == t else (
        [''.join(x) for x in ps] if str == t else [
            t(x) for x in ps
        ]
    )


# TEST ----------------------------------------------------

# main :: IO ()
def main():
    '''Permutations of lists, strings and tuples.'''

    print(
        fTable(__doc__ + ':\n')(repr)(showList)(
            permutations
        )([
            [1, 2, 3],
            'abc',
            (1, 2, 3),
        ])
    )


# GENERIC -------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).'''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# FORMATTING ----------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(showList(x) for x in xs) + ']' if (
        isinstance(xs, list)
    ) else repr(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

