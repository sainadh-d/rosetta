# Sorting algorithms/Cocktail sort

## Task Link
[Rosetta Code - Sorting algorithms/Cocktail sort](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort)

## Java Code
### java_code_1.txt
```java
public static void cocktailSort( int[] A ){
	boolean swapped;
	do {
		swapped = false;
		for (int i =0; i<=  A.length  - 2;i++) {
			if (A[ i ] > A[ i + 1 ]) {
				//test whether the two elements are in the wrong order
				int temp = A[i];
				A[i] = A[i+1];
				A[i+1]=temp;
				swapped = true;
			}
		}
		if (!swapped) {
			//we can exit the outer loop here if no swaps occurred.
			break;
		}
		swapped = false;
		for (int i= A.length - 2;i>=0;i--) {
			if (A[ i ] > A[ i + 1 ]) {
				int temp = A[i];
				A[i] = A[i+1];
				A[i+1]=temp;
				swapped = true;
			}
		}
		//if no elements have been swapped, then the list is sorted
	} while (swapped);
}

```

## Python Code
### python_code_1.txt
```python
def cocktailSort(A):
    up = range(len(A)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i] > A[i+1]:  
                    A[i], A[i+1] =  A[i+1], A[i]
                    swapped = True
            if not swapped:
                return

```

### python_code_2.txt
```python
test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
cocktailSort(test1)
print test1
#>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

test2=list('big fjords vex quick waltz nymph')
cocktailSort(test2)
print ''.join(test2)
#>>>      abcdefghiijklmnopqrstuvwxyz

```

### python_code_3.txt
```python
def cocktail(a):
    for i in range(len(a)//2):
        swap = False
        for j in range(1+i, len(a)-i):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break
        swap = False
        for j in range(len(a)-i-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                swap = True
        if not swap:
            break

```

