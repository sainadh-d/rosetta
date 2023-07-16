# Sorting algorithms/Quicksort

## Task Link
[Rosetta Code - Sorting algorithms/Quicksort](https://rosettacode.org/wiki/Sorting_algorithms/Quicksort)

## Java Code
### java_code_1.txt
```java
public static <E extends Comparable<? super E>> List<E> quickSort(List<E> arr) {
    if (arr.isEmpty())
        return arr;
    else {
        E pivot = arr.get(0);

        List<E> less = new LinkedList<E>();
        List<E> pivotList = new LinkedList<E>();
        List<E> more = new LinkedList<E>();

        // Partition
        for (E i: arr) {
            if (i.compareTo(pivot) < 0)
                less.add(i);
            else if (i.compareTo(pivot) > 0)
                more.add(i);
            else
                pivotList.add(i);
        }

        // Recursively sort sublists
        less = quickSort(less);
        more = quickSort(more);

        // Concatenate results
        less.addAll(pivotList);
        less.addAll(more);
        return less;
    }
}

```

### java_code_2.txt
```java
public static <E extends Comparable<E>> List<E> sort(List<E> col) {
    if (col == null || col.isEmpty())
        return Collections.emptyList();
    else {
        E pivot = col.get(0);
        Map<Integer, List<E>> grouped = col.stream()
                .collect(Collectors.groupingBy(pivot::compareTo));
        return Stream.of(sort(grouped.get(1)), grouped.get(0), sort(grouped.get(-1)))
                .flatMap(Collection::stream).collect(Collectors.toList());
    }
}

```

## Python Code
### python_code_1.txt
```python
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quickSort(a)

```

### python_code_2.txt
```python
def qsort(L):
    return (qsort([y for y in L[1:] if y <  L[0]]) + 
            [L[0]] + 
            qsort([y for y in L[1:] if y >= L[0]])) if len(L) > 1 else L

```

### python_code_3.txt
```python
def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list[1:]   if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)

```

### python_code_4.txt
```python
from random import *

def qSort(a):
    if len(a) <= 1:
        return a
    else:
        q = choice(a)
        return qSort([elem for elem in a if elem < q]) + [q] * a.count(q) + qSort([elem for elem in a if elem > q])

```

### python_code_5.txt
```python
def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        less = []
        more = []
        pivot = choice(a)
        for i in a:
            if i < pivot:
                less.append(i)
            if i > pivot:
                more.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + [pivot] * a.count(pivot) + more

```

### python_code_6.txt
```python
def qsort(array):
    if len(array) < 2:
        return array
    head, *tail = array
    less = qsort([i for i in tail if i < head])
    more = qsort([i for i in tail if i >= head])
    return less + [head] + more

```

### python_code_7.txt
```python
def quicksort(array):
    _quicksort(array, 0, len(array) - 1)

def _quicksort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

```

### python_code_8.txt
```python
def (qsort (pivot ... ns))
  (+ (qsort+keep (fn(_) (_ < pivot)) ns)
     list.pivot
     (qsort+keep (fn(_) (_ > pivot)) ns))

def (qsort x) :case x=nil
  nil

```

