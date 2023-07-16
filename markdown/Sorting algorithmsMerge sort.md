# Sorting algorithms/Merge sort

## Task Link
[Rosetta Code - Sorting algorithms/Merge sort](https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class Merge{
    public static <E extends Comparable<? super E>> List<E> mergeSort(List<E> m){
        if(m.size() <= 1) return m;

        int middle = m.size() / 2;
        List<E> left = m.subList(0, middle);
        List<E> right = m.subList(middle, m.size());

        right = mergeSort(right);
        left = mergeSort(left);
        List<E> result = merge(left, right);

        return result;
    }

    public static <E extends Comparable<? super E>> List<E> merge(List<E> left, List<E> right){
        List<E> result = new ArrayList<E>();
        Iterator<E> it1 = left.iterator();
        Iterator<E> it2 = right.iterator();

	E x = it1.next();
	E y = it2.next();
        while (true){
            //change the direction of this comparison to change the direction of the sort
            if(x.compareTo(y) <= 0){
		result.add(x);
		if(it1.hasNext()){
		    x = it1.next();
		}else{
		    result.add(y);
		    while(it2.hasNext()){
			result.add(it2.next());
		    }
		    break;
		}
	    }else{
		result.add(y);
		if(it2.hasNext()){
		    y = it2.next();
		}else{
		    result.add(x);
		    while (it1.hasNext()){
			result.add(it1.next());
		    }
		    break;
		}
	    }
        }
        return result;
    }
}

```

## Python Code
### python_code_2.txt
```python
from heapq import merge

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

```

### python_code_3.txt
```python
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

```

### python_code_4.txt
```python
def merge(x, y):
    if x==[]: return y
    if y==[]: return x
    return [x[0]] + merge(x[1:], y) if x[0]<y[0] else [y[0]] + merge(x, y[1:])

def sort(a, n):
    m = n//2
    return a if n<=1 else merge(sort(a[:m], m), sort(a[m:], n-m))

a = list(map(int, input().split()))
print(sort(a, len(a)))

```

