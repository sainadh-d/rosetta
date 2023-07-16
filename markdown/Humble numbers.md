# Humble numbers

## Task Link
[Rosetta Code - Humble numbers](https://rosettacode.org/wiki/Humble_numbers)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HumbleNumbers {

    public static void main(String[] args) {
        System.out.println("First 50 humble numbers:");
        System.out.println(Arrays.toString(humble(50)));
        Map<Integer,Integer> lengthCountMap = new HashMap<>();
        BigInteger[] seq = humble(1_000_000);
        for ( int i = 0 ; i < seq.length ; i++ ) {
            BigInteger humbleNumber = seq[i];
            int len = humbleNumber.toString().length();
            lengthCountMap.merge(len, 1, (v1, v2) -> v1 + v2);
        }
        List<Integer> sorted = new ArrayList<>(lengthCountMap.keySet());
        Collections.sort(sorted);
        System.out.printf("Length  Count%n");
        for ( Integer len : sorted ) {
            System.out.printf("    %2s  %5s%n", len, lengthCountMap.get(len));
        }
    }
    
    private static BigInteger[] humble(int n) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger twoTest = two;
        BigInteger three = BigInteger.valueOf(3);
        BigInteger threeTest = three;
        BigInteger five = BigInteger.valueOf(5);
        BigInteger fiveTest = five;
        BigInteger seven = BigInteger.valueOf(7);
        BigInteger sevenTest = seven;
        BigInteger[] results = new BigInteger[n];
        results[0] = BigInteger.ONE;
        int twoIndex = 0, threeIndex = 0, fiveIndex = 0, sevenIndex = 0;
        for ( int index = 1 ; index < n ; index++ ) {
            results[index] = twoTest.min(threeTest).min(fiveTest).min(sevenTest);
            if ( results[index].compareTo(twoTest) == 0 ) {
                twoIndex++;
                twoTest = two.multiply(results[twoIndex]);
            }
            if (results[index].compareTo(threeTest) == 0 ) {
                threeIndex++;
                threeTest = three.multiply(results[threeIndex]);
            }
            if (results[index].compareTo(fiveTest) == 0 ) {
                fiveIndex++;
                fiveTest = five.multiply(results[fiveIndex]);
            }
            if (results[index].compareTo(sevenTest) == 0 ) {
                sevenIndex++;
                sevenTest = seven.multiply(results[sevenIndex]);
            }
        }
        return results;
    }

}

```

## Python Code
### python_code_1.txt
```python
'''Humble numbers'''

from itertools import groupby, islice
from functools import reduce


# humbles :: () -> [Int]
def humbles():
    '''A non-finite stream of Humble numbers.
       OEIS A002473
    '''
    hs = set([1])
    while True:
        nxt = min(hs)
        yield nxt
        hs.remove(nxt)
        hs.update(nxt * x for x in [2, 3, 5, 7])


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''First 50, and counts with N digits'''

    print('First 50 Humble numbers:\n')
    for row in chunksOf(10)(
            take(50)(humbles())
    ):
        print(' '.join(map(
            lambda x: str(x).rjust(3),
            row
        )))

    print('\nCounts of Humble numbers with n digits:\n')
    for tpl in take(10)(
            (k, len(list(g))) for k, g in
            groupby(len(str(x)) for x in humbles())
    ):
        print(tpl)


# GENERIC -------------------------------------------------

# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    '''A series of lists of length n, subdividing the
       contents of xs. Where the length of xs is not evenly
       divible, the final list will be shorter than n.
    '''
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        list(islice(xs, n))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

