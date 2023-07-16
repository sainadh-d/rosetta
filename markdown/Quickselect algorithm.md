# Quickselect algorithm

## Task Link
[Rosetta Code - Quickselect algorithm](https://rosettacode.org/wiki/Quickselect_algorithm)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class QuickSelect {

	private static <E extends Comparable<? super E>> int partition(E[] arr, int left, int right, int pivot) {
		E pivotVal = arr[pivot];
		swap(arr, pivot, right);
		int storeIndex = left;
		for (int i = left; i < right; i++) {
			if (arr[i].compareTo(pivotVal) < 0) {
				swap(arr, i, storeIndex);
				storeIndex++;
			}
		}
		swap(arr, right, storeIndex);
		return storeIndex;
	}
	
	private static <E extends Comparable<? super E>> E select(E[] arr, int n) {
		int left = 0;
		int right = arr.length - 1;
		Random rand = new Random();
		while (right >= left) {
			int pivotIndex = partition(arr, left, right, rand.nextInt(right - left + 1) + left);
			if (pivotIndex == n) {
				return arr[pivotIndex];
			} else if (pivotIndex < n) {
				left = pivotIndex + 1;
			} else {
				right = pivotIndex - 1;
			}
		}
		return null;
	}
	
	private static void swap(Object[] arr, int i1, int i2) {
		if (i1 != i2) {
			Object temp = arr[i1];
			arr[i1] = arr[i2];
			arr[i2] = temp;
		}
	}
	
	public static void main(String[] args) {
		for (int i = 0; i < 10; i++) {
			Integer[] input = {9, 8, 7, 6, 5, 0, 1, 2, 3, 4};
			System.out.print(select(input, i));
			if (i < 9) System.out.print(", ");
		}
		System.out.println();
	}

}

```

## Python Code
### python_code_1.txt
```python
import random

def partition(vector, left, right, pivotIndex):
    pivotValue = vector[pivotIndex]
    vector[pivotIndex], vector[right] = vector[right], vector[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if vector[i] < pivotValue:
            vector[storeIndex], vector[i] = vector[i], vector[storeIndex]
            storeIndex += 1
    vector[right], vector[storeIndex] = vector[storeIndex], vector[right]  # Move pivot to its final place
    return storeIndex

def _select(vector, left, right, k):
    "Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1] inclusive."
    while True:
        pivotIndex = random.randint(left, right)     # select pivotIndex between left and right
        pivotNewIndex = partition(vector, left, right, pivotIndex)
        pivotDist = pivotNewIndex - left
        if pivotDist == k:
            return vector[pivotNewIndex]
        elif k < pivotDist:
            right = pivotNewIndex - 1
        else:
            k -= pivotDist + 1
            left = pivotNewIndex + 1

def select(vector, k, left=None, right=None):
    """\
    Returns the k-th smallest, (k >= 0), element of vector within vector[left:right+1].
    left, right default to (0, len(vector) - 1) if omitted
    """
    if left is None:
        left = 0
    lv1 = len(vector) - 1
    if right is None:
        right = lv1
    assert vector and k >= 0, "Either null vector or k < 0 "
    assert 0 <= left <= lv1, "left is out of range"
    assert left <= right <= lv1, "right is out of range"
    return _select(vector, left, right, k)

if __name__ == '__main__':
    v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print([select(v, i) for i in range(10)])

```

### python_code_2.txt
```python
'''Quick select'''

from functools import reduce


# quickselect :: Ord a => Int -> [a] -> a
def quickSelect(k):
    '''The kth smallest element
       in the unordered list xs.'''
    def go(k, xs):
        x = xs[0]

        def ltx(y):
            return y < x
        ys, zs = partition(ltx)(xs[1:])
        n = len(ys)
        return go(k, ys) if k < n else (
            go(k - n - 1, zs) if k > n else x
        )
    return lambda xs: go(k, xs) if xs else None


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''

    v = [9, 8, 7, 6, 5, 0, 1, 2, 3, 4]
    print(list(map(
        flip(quickSelect)(v),
        range(0, len(v))
    )))


# GENERIC -------------------------------------------------


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried) function f with its
       arguments reversed.'''
    return lambda a: lambda b: f(b)(a)


# partition :: (a -> Bool) -> [a] -> ([a], [a])
def partition(p):
    '''The pair of lists of those elements in xs
       which respectively do, and don't
       satisfy the predicate p.'''
    def go(a, x):
        ts, fs = a
        return (ts + [x], fs) if p(x) else (ts, fs + [x])
    return lambda xs: reduce(go, xs, ([], []))


# MAIN ---
if __name__ == '__main__':
    main()

```

