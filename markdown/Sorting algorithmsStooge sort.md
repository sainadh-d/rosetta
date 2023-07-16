# Sorting algorithms/Stooge sort

## Task Link
[Rosetta Code - Sorting algorithms/Stooge sort](https://rosettacode.org/wiki/Sorting_algorithms/Stooge_sort)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Stooge {
    public static void main(String[] args) {
        int[] nums = {1, 4, 5, 3, -6, 3, 7, 10, -2, -5};
        stoogeSort(nums);
        System.out.println(Arrays.toString(nums));
    }

    public static void stoogeSort(int[] L) {
        stoogeSort(L, 0, L.length - 1);
    }

    public static void stoogeSort(int[] L, int i, int j) {
        if (L[j] < L[i]) {
            int tmp = L[i];
            L[i] = L[j];
            L[j] = tmp;
        }
        if (j - i > 1) {
            int t = (j - i + 1) / 3;
            stoogeSort(L, i, j - t);
            stoogeSort(L, i + t, j);
            stoogeSort(L, i, j - t);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> data = [1, 4, 5, 3, -6, 3, 7, 10, -2, -5, 7, 5, 9, -3, 7]
>>> def stoogesort(L, i=0, j=None):
	if j is None:
		j = len(L) - 1
	if L[j] < L[i]:
		L[i], L[j] = L[j], L[i]
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(L, i  , j-t)
		stoogesort(L, i+t, j  )
		stoogesort(L, i  , j-t)
	return L

>>> stoogesort(data)
[-6, -5, -3, -2, 1, 3, 3, 4, 5, 5, 7, 7, 7, 9, 10]

```

### python_code_2.txt
```python
>>> def stoogesort(L, i, j):
	if L[j] < L[i]:
		L[i], L[j] = L[j], L[i]
	if j - i > 1:
		t = (j - i + 1) // 3
		stoogesort(L, i  , j-t)
		stoogesort(L, i+t, j  )
		stoogesort(L, i  , j-t)
	return L

>>> def stooge(L): return stoogesort(L, 0, len(L) - 1)

>>> data = [1, 4, 5, 3, -6, 3, 7, 10, -2, -5, 7, 5, 9, -3, 7]
>>> stooge(data)
[-6, -5, -3, -2, 1, 3, 3, 4, 5, 5, 7, 7, 7, 9, 10]

```

