# Range extraction

## Task Link
[Rosetta Code - Range extraction](https://rosettacode.org/wiki/Range_extraction)

## Java Code
### java_code_1.txt
```java
public class RangeExtraction {

    public static void main(String[] args) {
        int[] arr = {0, 1, 2, 4, 6, 7, 8, 11, 12, 14,
            15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, 27, 28, 29, 30, 31, 32, 33, 35, 36,
            37, 38, 39};

        int len = arr.length;
        int idx = 0, idx2 = 0;
        while (idx < len) {
            while (++idx2 < len && arr[idx2] - arr[idx2 - 1] == 1);
            if (idx2 - idx > 2) {
                System.out.printf("%s-%s,", arr[idx], arr[idx2 - 1]);
                idx = idx2;
            } else {
                for (; idx < idx2; idx++)
                    System.out.printf("%s,", arr[idx]);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
def range_extract(lst):
    'Yield 2-tuple ranges or 1-tuple single elements from list of increasing ints'
    lenlst = len(lst)
    i = 0
    while i< lenlst:
        low = lst[i]
        while i <lenlst-1 and lst[i]+1 == lst[i+1]: i +=1
        hi = lst[i]
        if   hi - low >= 2:
            yield (low, hi)
        elif hi - low == 1:
            yield (low,)
            yield (hi,)
        else:
            yield (low,)
        i += 1

def printr(ranges):
    print( ','.join( (('%i-%i' % r) if len(r) == 2 else '%i' % r)
                     for r in ranges ) )

if __name__ == '__main__':
    for lst in [[-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7,
                 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]]:
        #print(list(range_extract(lst)))
        printr(range_extract(lst))

```

### python_code_2.txt
```python
def range_extract(iterable):
    '''Assumes iterable is sorted sequentially. Returns iterator of range tuples.'''
    it = iter(iterable)

    try:
        i = next(it)
    except StopIteration:
        return

    while True:
        low = i

        try:
            j = next(it)
        except StopIteration:
            yield (low, )
            return
        while i + 1 == j:
            i_next = j
            try:
                j = next(it)
            except StopIteration:
                yield (low, j)
                return
            i = i_next

        hi = i

        if   hi - low >= 2:
            yield (low, hi)
        elif hi - low == 1:
            yield (low,)
            yield (hi,)
        else:
            yield (low,)

        i = j

def printr(ranges):
    print( ','.join( (('%i-%i' % r) if len(r) == 2 else '%i' % r)
                     for r in ranges ) )

if __name__ == '__main__':
    for lst in [[-8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7,
                 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                [0, 1, 2, 4, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39]]:
        #print(list(range_extract(lst)))
        printr(range_extract(lst))

```

### python_code_3.txt
```python
class PushableIter():
    "Can push items back on iterable"
    def __init__(self, it):
        self.it = iter(it)
        self.pushed = []

    def push(self, item):
        self.pushed.append(item)

    def pop(self):
        return self.pushed.pop(0) if self.pushed else self.it.__next__()

    def __iter__(self):
        return self

    def __next__(self):
        return self.pop()

def range_extractp(sorted_iterable):
    'Yield 2-tuple ranges or 1-tuple single elements from iter of increasing ints'
    rest = PushableIter(sorted_iterable)
    for this in rest:
        low = hi = last = this
        for nxt in rest:        # Find upper range on incremented values
            if nxt == last + 1:
                last = hi = nxt
            else:       # Out of (sub)-range
                rest.push(nxt)
                break
        if   hi - low >= 2:
            yield (low, hi)
        elif hi - low == 1:
            yield (low,)
            yield (hi,)
        else:
            yield (low,)

```

### python_code_4.txt
```python
'''Range extraction'''

from functools import reduce


# rangeFormat :: [Int] -> String
def rangeFormat(xs):
    '''Range-formatted display string for
       a list of integers.
    '''
    return ','.join([
        rangeString(x) for x
        in splitBy(lambda a, b: 1 < b - a)(xs)
    ])


# rangeString :: [Int] -> String
def rangeString(xs):
    '''Start and end of xs delimited by hyphens
       if there are more than two integers.
       Otherwise, comma-delimited xs.
    '''
    ys = [str(x) for x in xs]
    return '-'.join([ys[0], ys[-1]]) if 2 < len(ys) else (
        ','.join(ys)
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''

    xs = [
        0, 1, 2, 4, 6, 7, 8, 11, 12, 14,
        15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
        25, 27, 28, 29, 30, 31, 32, 33, 35, 36,
        37, 38, 39
    ]
    print(
        __doc__ + ':\n[' + '\n'.join(map(
            lambda x: ' ' + repr(x)[1:-1],
            chunksOf(11)(xs)
        )) + " ]\n\n        -> '" + rangeFormat(xs) + "'\n"
    )


# GENERIC -------------------------------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n,
       subdividing the contents of xs.
       Where the length of xs is not evenly divible,
       the final list will be shorter than n.'''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# splitBy :: (a -> a -> Bool) -> [a] -> [[a]]
def splitBy(p):
    '''A list split wherever two consecutive
       items match the binary predicate p.
    '''
    # step :: ([[a]], [a], a) -> a -> ([[a]], [a], a)
    def step(acp, x):
        acc, active, prev = acp
        return (acc + [active], [x], x) if p(prev, x) else (
            (acc, active + [x], x)
        )

    # go :: [a] -> [[a]]
    def go(xs):
        if 2 > len(xs):
            return xs
        else:
            h = xs[0]
            ys = reduce(step, xs[1:], ([], [h], h))
            # The accumulated sublists, and the current group.
            return ys[0] + [ys[1]]

    return lambda xs: go(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

