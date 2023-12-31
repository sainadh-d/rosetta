# Permutations by swapping

## Task Link
[Rosetta Code - Permutations by swapping](https://rosettacode.org/wiki/Permutations_by_swapping)

## Java Code
### java_code_1.txt
```java
package org.rosettacode.java;

import java.util.Arrays;
import java.util.stream.IntStream;

public class HeapsAlgorithm {

	public static void main(String[] args) {
		Object[] array = IntStream.range(0, 4)
				.boxed()
				.toArray();
		HeapsAlgorithm algorithm = new HeapsAlgorithm();
		algorithm.recursive(array);
		System.out.println();
		algorithm.loop(array);
	}

	void recursive(Object[] array) {
		recursive(array, array.length, true);
	}

	void recursive(Object[] array, int n, boolean plus) {
		if (n == 1) {
			output(array, plus);
		} else {
			for (int i = 0; i < n; i++) {
				recursive(array, n - 1, i == 0);
				swap(array, n % 2 == 0 ? i : 0, n - 1);
			}
		}
	}

	void output(Object[] array, boolean plus) {
		System.out.println(Arrays.toString(array) + (plus ? " +1" : " -1"));
	}

	void swap(Object[] array, int a, int b) {
		Object o = array[a];
		array[a] = array[b];
		array[b] = o;
	}

	void loop(Object[] array) {
		loop(array, array.length);
	}

	void loop(Object[] array, int n) {
		int[] c = new int[n];
		output(array, true);
		boolean plus = false;
		for (int i = 0; i < n; ) {
			if (c[i] < i) {
				if (i % 2 == 0) {
					swap(array, 0, i);
				} else {
					swap(array, c[i], i);
				}
				output(array, plus);
				plus = !plus;
				c[i]++;
				i = 0;
			} else {
				c[i] = 0;
				i++;
			}
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
from operator import itemgetter
 
DEBUG = False # like the built-in __debug__
 
def spermutations(n):
    """permutations by swapping. Yields: perm, sign"""
    sign = 1
    p = [[i, 0 if i == 0 else -1] # [num, direction]
         for i in range(n)]
 
    if DEBUG: print ' #', p
    yield tuple(pp[0] for pp in p), sign
 
    while any(pp[1] for pp in p): # moving
        i1, (n1, d1) = max(((i, pp) for i, pp in enumerate(p) if pp[1]),
                           key=itemgetter(1))
        sign *= -1
        if d1 == -1:
            # Swap down
            i2 = i1 - 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the First or last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == 0 or p[i2 - 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        elif d1 == 1:
            # Swap up
            i2 = i1 + 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the first or Last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == n - 1 or p[i2 + 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        if DEBUG: print ' #', p
        yield tuple(pp[0] for pp in p), sign
 
        for i3, pp in enumerate(p):
            n3, d3 = pp
            if n3 > n1:
                pp[1] = 1 if i3 < i2 else -1
                if DEBUG: print ' # Set Moving'
 
 
if __name__ == '__main__':
    from itertools import permutations
 
    for n in (3, 4):
        print '\nPermutations and sign of %i items' % n
        sp = set()
        for i in spermutations(n):
            sp.add(i[0])
            print('Perm: %r Sign: %2i' % i)
            #if DEBUG: raw_input('?')
        # Test
        p = set(permutations(range(n)))
        assert sp == p, 'Two methods of generating permutations do not agree'

```

### python_code_2.txt
```python
def s_permutations(seq):
    def s_perm(seq):
        if not seq:
            return [[]]
        else:
            new_items = []
            for i, item in enumerate(s_perm(seq[:-1])):
                if i % 2:
                    # step up
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item) + 1)]
                else:
                    # step down
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item), -1, -1)]
            return new_items

    return [(tuple(item), -1 if i % 2 else 1)
            for i, item in enumerate(s_perm(seq))]

```

### python_code_3.txt
```python
def s_permutations(seq):
    items = [[]]
    for j in seq:
        new_items = []
        for i, item in enumerate(items):
            if i % 2:
                # step up
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item) + 1)]
            else:
                # step down
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item), -1, -1)]
        items = new_items

    return [(tuple(item), -1 if i % 2 else 1)
            for i, item in enumerate(items)]

```

