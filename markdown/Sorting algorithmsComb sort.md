# Sorting algorithms/Comb sort

## Task Link
[Rosetta Code - Sorting algorithms/Comb sort](https://rosettacode.org/wiki/Sorting_algorithms/Comb_sort)

## Java Code
### java_code_1.txt
```java
public static <E extends Comparable<? super E>> void sort(E[] input) {
    int gap = input.length;
    boolean swapped = true;
    while (gap > 1 || swapped) {
        if (gap > 1) {
            gap = (int) (gap / 1.3);
        }
        swapped = false;
        for (int i = 0; i + gap < input.length; i++) {
            if (input[i].compareTo(input[i + gap]) > 0) {
                E t = input[i];
                input[i] = input[i + gap];
                input[i + gap] = t;
                swapped = true;
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def combsort(input):
    gap = len(input)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(input) - gap):
            j = i+gap
            if input[i] > input[j]:
                input[i], input[j] = input[j], input[i]
                swaps = True

                
>>> y = [88, 18, 31, 44, 4, 0, 8, 81, 14, 78, 20, 76, 84, 33, 73, 75, 82, 5, 62, 70]
>>> combsort(y)
>>> assert y == sorted(y)
>>> y
[0, 4, 5, 8, 14, 18, 20, 31, 33, 44, 62, 70, 73, 75, 76, 78, 81, 82, 84, 88]
>>>

```

