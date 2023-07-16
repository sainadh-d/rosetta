# Longest increasing subsequence

## Task Link
[Rosetta Code - Longest increasing subsequence](https://rosettacode.org/wiki/Longest_increasing_subsequence)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class LIS {
    public static <E extends Comparable<? super E>> List<E> lis(List<E> n) {
        List<Node<E>> pileTops = new ArrayList<Node<E>>();
        // sort into piles
        for (E x : n) {
	    Node<E> node = new Node<E>();
	    node.value = x;
            int i = Collections.binarySearch(pileTops, node);
            if (i < 0) i = ~i;
	    if (i != 0)
		node.pointer = pileTops.get(i-1);
            if (i != pileTops.size())
                pileTops.set(i, node);
            else
                pileTops.add(node);
        }
	// extract LIS from nodes
	List<E> result = new ArrayList<E>();
	for (Node<E> node = pileTops.size() == 0 ? null : pileTops.get(pileTops.size()-1);
                node != null; node = node.pointer)
	    result.add(node.value);
	Collections.reverse(result);
	return result;
    }

    private static class Node<E extends Comparable<? super E>> implements Comparable<Node<E>> {
	public E value;
	public Node<E> pointer;
        public int compareTo(Node<E> y) { return value.compareTo(y.value); }
    }

    public static void main(String[] args) {
	List<Integer> d = Arrays.asList(3,2,6,4,5,1);
	System.out.printf("an L.I.S. of %s is %s\n", d, lis(d));
        d = Arrays.asList(0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15);
	System.out.printf("an L.I.S. of %s is %s\n", d, lis(d));
    }
}

```

## Python Code
### python_code_1.txt
```python
def longest_increasing_subsequence(X):
    """Returns the Longest Increasing Subsequence in the Given List/Array"""
    N = len(X)
    P = [0] * N
    M = [0] * (N+1)
    L = 0
    for i in range(N):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (X[M[mid]] < X[i]):
               lo = mid+1
           else:
               hi = mid-1
    
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
    
       if (newL > L):
           L = newL
    
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(X[k])
        k = P[k]
    return S[::-1]

if __name__ == '__main__':
    for d in [[3,2,6,4,5,1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))

```

### python_code_2.txt
```python
def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)

if __name__ == '__main__':
    for d in [[3,2,6,4,5,1], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, longest_increasing_subsequence(d)))

```

### python_code_3.txt
```python
from collections import namedtuple
from functools import total_ordering
from bisect import bisect_left

@total_ordering
class Node(namedtuple('Node_', 'val back')):
    def __iter__(self):
        while self is not None:
            yield self.val
            self = self.back
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        return self.val == other.val

def lis(d):
    """Return one of the L.I.S. of list d using patience sorting."""
    if not d:
        return []
    pileTops = []
    for di in d:
        j = bisect_left(pileTops, Node(di, None))
        pileTops[j:j+1] = [Node(di, pileTops[j-1] if j > 0 else None)]
    return list(pileTops[-1])[::-1]

if __name__ == '__main__':
    for d in [[3,2,6,4,5,1],
              [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]]:
        print('a L.I.S. of %s is %s' % (d, lis(d)))

```

