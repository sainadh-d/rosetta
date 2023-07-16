# Sorting Algorithms/Circle Sort

## Task Link
[Rosetta Code - Sorting Algorithms/Circle Sort](https://rosettacode.org/wiki/Sorting_Algorithms/Circle_Sort)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class CircleSort {

    public static void main(String[] args) {
        circleSort(new int[]{2, 14, 4, 6, 8, 1, 3, 5, 7, 11, 0, 13, 12, -1});
    }

    public static void circleSort(int[] arr) {
        if (arr.length > 0)
            do {
                System.out.println(Arrays.toString(arr));
            } while (circleSortR(arr, 0, arr.length - 1, 0) != 0);
    }

    private static int circleSortR(int[] arr, int lo, int hi, int numSwaps) {
        if (lo == hi)
            return numSwaps;

        int high = hi;
        int low = lo;
        int mid = (hi - lo) / 2;

        while (lo < hi) {
            if (arr[lo] > arr[hi]) {
                swap(arr, lo, hi);
                numSwaps++;
            }
            lo++;
            hi--;
        }

        if (lo == hi && arr[lo] > arr[hi + 1]) {
            swap(arr, lo, hi + 1);
            numSwaps++;
        }

        numSwaps = circleSortR(arr, low, low + mid, numSwaps);
        numSwaps = circleSortR(arr, low + mid + 1, high, numSwaps);

        return numSwaps;
    }

    private static void swap(int[] arr, int idx1, int idx2) {
        int tmp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = tmp;
    }
}

```

## Python Code
### python_code_1.txt
```python
#python3
#tests: expect no output.
#doctest with  python3 -m doctest thisfile.py
#additional tests:  python3 thisfile.py

def circle_sort_backend(A:list, L:int, R:int)->'sort A in place, returning the number of swaps':
    '''
        >>> L = [3, 2, 8, 28, 2,]
        >>> circle_sort(L)
        3
        >>> print(L)
        [2, 2, 3, 8, 28]
        >>> L = [3, 2, 8, 28,]
        >>> circle_sort(L)
        1
        >>> print(L)
        [2, 3, 8, 28]
    '''
    n = R-L
    if n < 2:
        return 0
    swaps = 0
    m = n//2
    for i in range(m):
        if A[R-(i+1)] < A[L+i]:
            (A[R-(i+1)], A[L+i],) = (A[L+i], A[R-(i+1)],)
            swaps += 1
    if (n & 1) and (A[L+m] < A[L+m-1]):
        (A[L+m-1], A[L+m],) = (A[L+m], A[L+m-1],)
        swaps += 1
    return swaps + circle_sort_backend(A, L, L+m) + circle_sort_backend(A, L+m, R)

def circle_sort(L:list)->'sort A in place, returning the number of swaps':
    swaps = 0
    s = 1
    while s:
        s = circle_sort_backend(L, 0, len(L))
        swaps += s
    return swaps

# more tests!
if __name__ == '__main__':
    from random import shuffle
    for i in range(309):
        L = list(range(i))
        M = L[:]
        shuffle(L)
        N = L[:]
        circle_sort(L)
        if L != M:
            print(len(L))
            print(N)
            print(L)

```

