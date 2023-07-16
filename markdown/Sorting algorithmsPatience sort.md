# Sorting algorithms/Patience sort

## Task Link
[Rosetta Code - Sorting algorithms/Patience sort](https://rosettacode.org/wiki/Sorting_algorithms/Patience_sort)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class PatienceSort {
    public static <E extends Comparable<? super E>> void sort (E[] n) {
        List<Pile<E>> piles = new ArrayList<Pile<E>>();
        // sort into piles
        for (E x : n) {
            Pile<E> newPile = new Pile<E>();
            newPile.push(x);
            int i = Collections.binarySearch(piles, newPile);
            if (i < 0) i = ~i;
            if (i != piles.size())
                piles.get(i).push(x);
            else
                piles.add(newPile);
        }
 
        // priority queue allows us to retrieve least pile efficiently
        PriorityQueue<Pile<E>> heap = new PriorityQueue<Pile<E>>(piles);
        for (int c = 0; c < n.length; c++) {
            Pile<E> smallPile = heap.poll();
            n[c] = smallPile.pop();
            if (!smallPile.isEmpty())
                heap.offer(smallPile);
        }
        assert(heap.isEmpty());
    }
 
    private static class Pile<E extends Comparable<? super E>> extends Stack<E> implements Comparable<Pile<E>> {
        public int compareTo(Pile<E> y) { return peek().compareTo(y.peek()); }
    }

    public static void main(String[] args) {
	Integer[] a = {4, 65, 2, -31, 0, 99, 83, 782, 1};
	sort(a);
	System.out.println(Arrays.toString(a));
    }
}

```

## Python Code
### python_code_1.txt
```python
from functools import total_ordering
from bisect import bisect_left
from heapq import merge

@total_ordering
class Pile(list):
    def __lt__(self, other): return self[-1] < other[-1]
    def __eq__(self, other): return self[-1] == other[-1]

def patience_sort(n):
    piles = []
    # sort into piles
    for x in n:
        new_pile = Pile([x])
        i = bisect_left(piles, new_pile)
        if i != len(piles):
            piles[i].append(x)
        else:
            piles.append(new_pile)

    # use a heap-based merge to merge piles efficiently
    n[:] = merge(*[reversed(pile) for pile in piles])

if __name__ == "__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    patience_sort(a)
    print a

```

