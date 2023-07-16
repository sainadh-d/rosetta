# Sorting algorithms/Cocktail sort with shifting bounds

## Task Link
[Rosetta Code - Sorting algorithms/Cocktail sort with shifting bounds](https://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort_with_shifting_bounds)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class CocktailSort {
    public static void main(String[] args) {
        Integer[] array = new Integer[]{ 5, 1, -6, 12, 3, 13, 2, 4, 0, 15 };
        System.out.println("before: " + Arrays.toString(array));
        cocktailSort(array);
        System.out.println("after: " + Arrays.toString(array));
    }

    // Sorts an array of elements that implement the Comparable interface
    public static void cocktailSort(Object[] array) {
        int begin = 0;
        int end = array.length;
        if (end == 0)
            return;
        for (--end; begin < end; ) {
            int new_begin = end;
            int new_end = begin;
            for (int i = begin; i < end; ++i) {
                Comparable c1 = (Comparable)array[i];
                Comparable c2 = (Comparable)array[i + 1];
                if (c1.compareTo(c2) > 0) {
                    swap(array, i, i + 1);
                    new_end = i;
                }
            }
            end = new_end;
            for (int i = end; i > begin; --i) {
                Comparable c1 = (Comparable)array[i - 1];
                Comparable c2 = (Comparable)array[i];
                if (c1.compareTo(c2) > 0) {
                    swap(array, i, i - 1);
                    new_begin = i;
                }
            }
            begin = new_begin;
        }
    }

    private static void swap(Object[] array, int i, int j) {
        Object tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}

```

## Python Code
### python_code_1.txt
```python
"""

Python example of

http://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort_with_shifting_bounds

based on 

http://rosettacode.org/wiki/Sorting_algorithms/Cocktail_sort#Python

"""
            
def cocktailshiftingbounds(A):
    beginIdx = 0
    endIdx = len(A) - 1
    
    while beginIdx <= endIdx:
        newBeginIdx = endIdx
        newEndIdx = beginIdx
        for ii in range(beginIdx,endIdx):
            if A[ii] > A[ii + 1]:
                A[ii+1], A[ii] = A[ii], A[ii+1]
                newEndIdx = ii
                
        endIdx = newEndIdx
    
        for ii in range(endIdx,beginIdx-1,-1):
            if A[ii] > A[ii + 1]:
                A[ii+1], A[ii] = A[ii], A[ii+1]
                newBeginIdx = ii
        
        beginIdx = newBeginIdx + 1
            
test1 = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
cocktailshiftingbounds(test1)
print(test1)
 
test2=list('big fjords vex quick waltz nymph')
cocktailshiftingbounds(test2)
print(''.join(test2))

```

