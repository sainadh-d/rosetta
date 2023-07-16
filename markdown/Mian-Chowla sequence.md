# Mian-Chowla sequence

## Task Link
[Rosetta Code - Mian-Chowla sequence](https://rosettacode.org/wiki/Mian-Chowla_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class MianChowlaSequence {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        System.out.println("First 30 terms of the Mian–Chowla sequence.");
        mianChowla(1, 30);
        System.out.println("Terms 91 through 100 of the Mian–Chowla sequence.");
        mianChowla(91, 100);
        long end = System.currentTimeMillis();
        System.out.printf("Elapsed = %d ms%n", (end-start));
    }

    private static void mianChowla(int minIndex, int maxIndex) {
        int [] sums = new int[1];
        int [] chowla = new int[maxIndex+1];
        sums[0] = 2;
        chowla[0] = 0;
        chowla[1] = 1;
        if ( minIndex == 1 ) {
            System.out.printf("%d ", 1);
        }
        int chowlaLength = 1;
        for ( int n = 2 ; n <= maxIndex ; n++ ) {

            //  Sequence is strictly increasing.
            int test = chowla[n - 1];
            //  Bookkeeping.  Generate only new sums.
            int[] sumsNew = Arrays.copyOf(sums, sums.length + n);
            int sumNewLength = sums.length;
            int savedsSumNewLength = sumNewLength;
            
            //  Generate test candidates for the next value of the sequence.
            boolean found = false;
            while ( ! found ) {
                test++;
                found = true;
                sumNewLength = savedsSumNewLength;
                //  Generate test sums
                for ( int j = 0 ; j <= chowlaLength ; j++ ) {
                    int testSum = (j == 0 ? test : chowla[j]) + test;
                    boolean duplicate = false;
                    
                    //  Check if test Sum in array
                    for ( int k = 0 ; k < sumNewLength ; k++ ) {
                        if ( sumsNew[k] == testSum ) {
                            duplicate = true;
                            break;
                        }
                    }
                    if ( ! duplicate ) {
                        //  Add to array 
                        sumsNew[sumNewLength] = testSum;
                        sumNewLength++;
                    }
                    else {
                        //  Duplicate found.  Therefore, test candidate of the next value of the sequence is not OK.
                        found = false;
                        break;
                    }
                }
            }
            
            //  Bingo!  Now update bookkeeping.
            chowla[n] = test;
            chowlaLength++;            
            sums = sumsNew;
            if ( n >= minIndex ) {
                System.out.printf("%d %s", chowla[n], (n==maxIndex ? "\n" : ""));
            }
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
from itertools import count, islice, chain
import time

def mian_chowla():
    mc = [1]
    yield mc[-1]
    psums = set([2])
    newsums = set([])
    for trial in count(2):
        for n in chain(mc, [trial]):
            sum = n + trial
            if sum in psums:
                newsums.clear()
                break
            newsums.add(sum)
        else:
            psums |= newsums
            newsums.clear()
            mc.append(trial)
            yield trial

def pretty(p, t, s, f):
    print(p, t, " ".join(str(n) for n in (islice(mian_chowla(), s, f))))

if __name__ == '__main__':
    st = time.time()
    ts = "of the Mian-Chowla sequence are:\n"
    pretty("The first 30 terms", ts, 0, 30)
    pretty("\nTerms 91 to 100", ts, 90, 100)
    print("\nComputation time was", (time.time()-st) * 1000, "ms")

```

### python_code_2.txt
```python
'''Mian-Chowla series'''

from itertools import (islice)
from time import time


# mianChowlas :: Gen [Int]
def mianChowlas():
    '''Mian-Chowla series - Generator constructor
    '''
    mcs = [1]
    sumSet = set([2])
    x = 1
    while True:
        yield x
        (sumSet, mcs, x) = nextMC(sumSet, mcs, x)


# nextMC :: (Set Int, [Int], Int) -> (Set Int, [Int], Int)
def nextMC(setSums, mcs, n):
    '''(Set of sums, series so far, current term) ->
        (updated sum set, updated series, next term)
    '''
    def valid(x):
        for m in mcs:
            if x + m in setSums:
                return False
        return True

    x = until(valid)(succ)(n)
    setSums.update(
        [x + y for y in mcs] + [2 * x]
    )
    return (setSums, mcs + [x], x)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests'''

    start = time()
    genMianChowlas = mianChowlas()
    print(
        'First 30 terms of the Mian-Chowla series:\n',
        take(30)(genMianChowlas)
    )
    drop(60)(genMianChowlas)
    print(
        '\n\nTerms 91 to 100 of the Mian-Chowla series:\n',
        take(10)(genMianChowlas),
        '\n'
    )
    print(
        '(Computation time c. ' + str(round(
            1000 * (time() - start)
        )) + ' ms)'
    )


# GENERIC -------------------------------------------------

# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The suffix of xs after the
       first n elements, or [] if n > length xs'''
    def go(xs):
        if isinstance(xs, list):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)


# succ :: Int -> Int
def succ(x):
    '''The successor of a numeric value (1 +)'''
    return 1 + x


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


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of applying f until p holds.
       The initial seed value is x.'''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

