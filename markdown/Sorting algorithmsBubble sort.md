# Sorting algorithms/Bubble sort

## Task Link
[Rosetta Code - Sorting algorithms/Bubble sort](https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort)

## Java Code
### java_code_1.txt
```java
public static <E extends Comparable<? super E>> void bubbleSort(E[] comparable) {
    boolean changed = false;
    do {
        changed = false;
        for (int a = 0; a < comparable.length - 1; a++) {
            if (comparable[a].compareTo(comparable[a + 1]) > 0) {
                E tmp = comparable[a];
                comparable[a] = comparable[a + 1];
                comparable[a + 1] = tmp;
                changed = true;
            }
        }
    } while (changed);
}

```

### java_code_2.txt
```java
if (comparable[a].compareTo(comparable[b]) < 0){
   //same swap code as before
}

```

## Python Code
### python_code_1.txt
```python
def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
       seq MUST BE A MUTABLE SEQUENCE.

       As with list.sort() and random.shuffle this does NOT return 
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq

if __name__ == "__main__":
   """Sample usage and simple test suite"""

   from random import shuffle

   testset = [_ for _ in range(100)]
   testcase = testset.copy() # make a copy
   shuffle(testcase)
   assert testcase != testset  # we've shuffled it
   bubble_sort(testcase)
   assert testcase == testset  # we've unshuffled it back into a copy

```

