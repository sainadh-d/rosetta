# Combinations with repetitions

## Task Link
[Rosetta Code - Combinations with repetitions](https://rosettacode.org/wiki/Combinations_with_repetitions)

## Java Code
### java_code_1.txt
```java
import com.objectwave.utility.*;

public class MultiCombinationsTester {

    public MultiCombinationsTester() throws CombinatoricException {
        Object[] objects = {"iced", "jam", "plain"};
        //Object[] objects = {"abba", "baba", "ab"};
        //Object[] objects = {"aaa", "aa", "a"};
        //Object[] objects = {(Integer)1, (Integer)2, (Integer)3, (Integer)4};
        MultiCombinations mc = new MultiCombinations(objects, 2);
        while (mc.hasMoreElements()) {
            for (int i = 0; i < mc.nextElement().length; i++) {
                System.out.print(mc.nextElement()[i].toString() + " ");
            }
            System.out.println();
        }

        // Extra credit:
        System.out.println("----------");
        System.out.println("The ways to choose 3 items from 10 with replacement = " + MultiCombinations.c(10, 3));
    } // constructor

    public static void main(String[] args) throws CombinatoricException {
        new MultiCombinationsTester();
    }
} // class

```

### java_code_2.txt
```java
import com.objectwave.utility.*;
import java.util.*;

public class MultiCombinations {

    private HashSet<String> set = new HashSet<String>();
    private Combinations comb = null;
    private Object[] nextElem = null;

    public MultiCombinations(Object[] objects, int k) throws CombinatoricException {
        k = Math.max(0, k);
        Object[] myObjects = new Object[objects.length * k];
        for (int i = 0; i < objects.length; i++) {
            for (int j = 0; j < k; j++) {
                myObjects[i * k + j] = objects[i];
            }
        }
        comb = new Combinations(myObjects, k);
    } // constructor

    boolean hasMoreElements() {
        boolean ret = false;
        nextElem = null;
        int oldCount = set.size();
        while (comb.hasMoreElements()) {
            Object[] elem = (Object[]) comb.nextElement();
            String str = "";
            for (int i = 0; i < elem.length; i++) {
                str += ("%" + elem[i].toString() + "~");
            }
            set.add(str);
            if (set.size() > oldCount) {
                nextElem = elem;
                ret = true;
                break;
            }
        }
        return ret;
    } // hasMoreElements()

    Object[] nextElement() {
        return nextElem;
    }

    static java.math.BigInteger c(int n, int k) throws CombinatoricException {
        return Combinatoric.c(n + k - 1, k);
    }
} // class

```

## Python Code
### python_code_1.txt
```python
>>> from itertools import combinations_with_replacement
>>> n, k = 'iced jam plain'.split(), 2
>>> list(combinations_with_replacement(n,k))
[('iced', 'iced'), ('iced', 'jam'), ('iced', 'plain'), ('jam', 'jam'), ('jam', 'plain'), ('plain', 'plain')]
>>> # Extra credit
>>> len(list(combinations_with_replacement(range(10), 3)))
220
>>>

```

### python_code_2.txt
```python
'''Combinations with repetitions'''

from itertools import (accumulate, chain, islice, repeat)
from functools import (reduce)


# combsWithRep :: Int -> [a] -> [kTuple a]
def combsWithRep(k):
    '''A list of tuples, representing
       sets of cardinality k,
       with elements drawn from xs.
    '''
    def f(a, x):
        def go(ys, xs):
            return xs + [[x] + y for y in ys]
        return accumulate(a, go)

    def combsBySize(xs):
        return reduce(
            f, xs, chain(
                [[[]]],
                islice(repeat([]), k)
            )
        )
    return lambda xs: [
        tuple(x) for x in next(islice(
            combsBySize(xs), k, None
        ))
    ]


# TEST ----------------------------------------------------
def main():
    '''Test the generation of sets of cardinality
       k with elements drawn from xs.
    '''
    print(
        combsWithRep(2)(['iced', 'jam', 'plain'])
    )
    print(
        len(combsWithRep(3)(enumFromTo(0)(9)))
    )


# GENERIC -------------------------------------------------

# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# showLog :: a -> IO String
def showLog(*s):
    '''Arguments printed with
       intercalated arrows.'''
    print(
        ' -> '.join(map(str, s))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

