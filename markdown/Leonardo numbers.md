# Leonardo numbers

## Task Link
[Rosetta Code - Leonardo numbers](https://rosettacode.org/wiki/Leonardo_numbers)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.List;

@SuppressWarnings("SameParameterValue")
public class LeonardoNumbers {
    private static List<Integer> leonardo(int n) {
        return leonardo(n, 1, 1, 1);
    }

    private static List<Integer> leonardo(int n, int l0, int l1, int add) {
        Integer[] leo = new Integer[n];
        leo[0] = l0;
        leo[1] = l1;
        for (int i = 2; i < n; i++) {
            leo[i] = leo[i - 1] + leo[i - 2] + add;
        }
        return Arrays.asList(leo);
    }

    public static void main(String[] args) {
        System.out.println("The first 25 Leonardo numbers with L[0] = 1, L[1] = 1 and add number = 1 are:");
        System.out.println(leonardo(25));
        System.out.println("\nThe first 25 Leonardo numbers with L[0] = 0, L[1] = 1 and add number = 0 are:");
        System.out.println(leonardo(25, 0, 1, 0));
    }
}

```

## Python Code
### python_code_1.txt
```python
def Leonardo(L_Zero, L_One, Add, Amount):
    terms = [L_Zero,L_One]
    while len(terms) < Amount:
        new = terms[-1] + terms[-2]
        new += Add
        terms.append(new)
    return terms

out = ""
print "First 25 Leonardo numbers:"
for term in Leonardo(1,1,1,25):
    out += str(term) + " "
print out

out = ""
print "Leonardo numbers with fibonacci parameters:"
for term in Leonardo(0,1,0,25):
    out += str(term) + " "
print out

```

### python_code_2.txt
```python
'''Leonardo numbers'''

from functools import (reduce)
from itertools import (islice)


# leo :: Int -> Int -> Int -> Generator [Int]
def leo(L0, L1, delta):
    '''A number series of the
       Leonardo and Fibonacci pattern,
       where L0 and L1 are the first two terms,
       and delta = 1 for (L0, L1) == (1, 1)
       yields the Leonardo series, while
       delta = 0 defines the Fibonacci series.'''
    (x, y) = (L0, L1)
    while True:
        yield x
        (x, y) = (y, x + y + delta)


# main :: IO()
def main():
    '''Tests.'''

    print('\n'.join([
        'First 25 Leonardo numbers:',
        folded(16)(take(25)(
            leo(1, 1, 1)
        )),
        '',
        'First 25 Fibonacci numbers:',
        folded(16)(take(25)(
            leo(0, 1, 0)
        ))
    ]))


# FORMATTING ----------------------------------------------

# folded :: Int -> [a] -> String
def folded(n):
    '''Long list folded to rows of n terms each.'''
    return lambda xs: '[' + ('\n '.join(
        str(ns)[1:-1] for ns in chunksOf(n)(xs)
    ) + ']')


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


# MAIN ---
if __name__ == '__main__':
    main()

```

