# Sorting algorithms/Insertion sort

## Task Link
[Rosetta Code - Sorting algorithms/Insertion sort](https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort)

## Java Code
### java_code_1.txt
```java
public static void insertSort(int[] A){
  for(int i = 1; i < A.length; i++){
    int value = A[i];
    int j = i - 1;
    while(j >= 0 && A[j] > value){
      A[j + 1] = A[j];
      j = j - 1;
    }
    A[j + 1] = value;
  }
}

```

### java_code_2.txt
```java
public static <E extends Comparable<? super E>> void insertionSort(List<E> a) {
  for (int i = 1; i < a.size(); i++) {
    int j = Math.abs(Collections.binarySearch(a.subList(0, i), a.get(i)) + 1);
    Collections.rotate(a.subList(j, i+1), j - i);
  }
}
public static <E extends Comparable<? super E>> void insertionSort(E[] a) {
  for (int i = 1; i < a.length; i++) {
    E x = a[i];
    int j = Math.abs(Arrays.binarySearch(a, 0, i, x) + 1);
    System.arraycopy(a, j, a, j+1, i-j);
    a[j] = x;
  }
}

```

## Python Code
### python_code_1.txt
```python
def insertion_sort(L):
    for i in xrange(1, len(L)):
        j = i-1 
        key = L[i]
        while j >= 0 and L[j] > key:
           L[j+1] = L[j]
           j -= 1
        L[j+1] = key

```

### python_code_2.txt
```python
def insertion_sort(L):
    for i, value in enumerate(L):
        for j in range(i - 1, -1, -1):
            if L[j] > value:
                L[j + 1] = L[j]
                L[j] = value

```

### python_code_3.txt
```python
def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted        
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]

```

### python_code_4.txt
```python
import bisect
def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)

```

