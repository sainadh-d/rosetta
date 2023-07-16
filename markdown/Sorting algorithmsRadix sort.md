# Sorting algorithms/Radix sort

## Task Link
[Rosetta Code - Sorting algorithms/Radix sort](https://rosettacode.org/wiki/Sorting_algorithms/Radix_sort)

## Java Code
### java_code_1.txt
```java
public static int[] sort(int[] old) {
    // Loop for every bit in the integers
    for (int shift = Integer.SIZE - 1; shift > -1; shift--) {
        // The array to put the partially sorted array into
        int[] tmp = new int[old.length];
        // The number of 0s
        int j = 0;

        // Move the 0s to the new array, and the 1s to the old one
        for (int i = 0; i < old.length; i++) {
            // If there is a 1 in the bit we are testing, the number will be negative
            boolean move = old[i] << shift >= 0;

            // If this is the last bit, negative numbers are actually lower
            if (shift == 0 ? !move : move) {
                tmp[j] = old[i];
                j++;
            } else {
                // It's a 1, so stick it in the old array for now
                old[i - j] = old[i];
            }
        }

        // Copy over the 1s from the old array
        for (int i = j; i < tmp.length; i++) {
            tmp[i] = old[i - j];
        }

        // And now the tmp array gets switched for another round of sorting
        old = tmp;
    }

    return old;
}

```

### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class RSortingRadixsort00 {

  public RSortingRadixsort00() {

    return;
  }

  public static int[] lsdRadixSort(int[] tlist) {

    List<Integer> intermediates;
    int[] limits = getLimits(tlist);
    tlist = rescale(tlist, limits[1]);

    for (int px = 1; px <= limits[2]; ++px) {
      @SuppressWarnings("unchecked")
      Queue<Integer> bukits[] = new Queue[10];
      for (int ix = 0; ix < tlist.length; ++ix) {
        int cval = tlist[ix];
        int digit = (int) (cval / Math.pow(10, px - 1) % 10);
        if (bukits[digit] == null) {
          bukits[digit] = new LinkedList<>();
        }
        bukits[digit].add(cval);
      }

      intermediates = new ArrayList<>();
      for (int bi = 0; bi < 10; ++bi) {
        if (bukits[bi] != null) {
          while (bukits[bi].size() > 0) {
            int nextd;
            nextd = bukits[bi].poll();
            intermediates.add(nextd);
          }
        }
      }

      for (int iw = 0; iw < intermediates.size(); ++iw) {
        tlist[iw] = intermediates.get(iw);
      }
    }

    tlist = rescale(tlist, -limits[1]);

    return tlist;
  }

  private static int[] rescale(int[] arry, int delta) {

    for (int ix = 0; ix < arry.length; ++ix) {
      arry[ix] -= delta;
    }

    return arry;
  }

  private static int[] getLimits(int[] tlist) {

    int[] lims = new int[3];

    for (int i_ = 0; i_ < tlist.length; ++i_) {
      lims[0] = Math.max(lims[0], tlist[i_]);
      lims[1] = Math.min(lims[1], tlist[i_]);
    }
    lims[2] = (int) Math.ceil(Math.log10(lims[0] - lims[1]));

    return lims;
  }

  private static void runSample(String[] args) {

    int[][] lists = {
      new int[] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, },
      new int[] { -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, -0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, },
      new int[] { 2, 24, 45, 0, 66, 75, 170, -802, -90, 1066, 666, },
      new int[] { 170, 45, 75, 90, 2, 24, 802, 66, },
      new int[] { -170, -45, -75, -90, -2, -24, -802, -66, },
    };

    long etime;
    lsdRadixSort(Arrays.copyOf(lists[0], lists[0].length)); // do one pass to set up environment to remove it from timings

    for (int[] tlist : lists) {
      System.out.println(array2list(tlist));
      etime = System.nanoTime();
      tlist = lsdRadixSort(tlist);
      etime = System.nanoTime() - etime;
      System.out.println(array2list(tlist));
      System.out.printf("Elapsed time: %fs%n", ((double) etime / 1_000_000_000.0));
      System.out.println();
    }

    return;
  }

  private static List<Integer> array2list(int[] arry) {

    List<Integer> target = new ArrayList<>(arry.length);

    for (Integer iv : arry) {
      target.add(iv);
    }

    return target;
  }

  public static void main(String[] args) {

    runSample(args);

    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
#python2.6 <
from math import log
 
def getDigit(num, base, digit_num):
    # pulls the selected digit
    return (num // base ** digit_num) % base  
 
def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [ [] for i in range(size) ]  
 
def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        buckets[getDigit(num, base, digit_num)].append(num)  
    return buckets
 
# concatenate the lists back in order for the next step
def merge(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list
 
def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)

def split_by_sign(a_list):
    # splits values by sign - negative values go to the first bucket,
    # non-negative ones into the second
    buckets = [[], []]
    for num in a_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets
 
def radixSort(a_list, base):
    # there are as many passes as there are digits in the longest number
    passes = int(round(log(maxAbs(a_list), base)) + 1) 
    new_list = list(a_list)
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))
    return merge(split_by_sign(new_list))

```

### python_code_2.txt
```python
#python3.7 <
def flatten(some_list):
    """
    Flatten a list of lists.
    Usage: flatten([[list a], [list b], ...])
    Output: [elements of list a, elements of list b]
    """
    new_list = []
    for sub_list in some_list:
        new_list += sub_list
    return new_list

def radix(some_list, idex=None, size=None):
    """
    Recursive radix sort
    Usage: radix([unsorted list])
    Output: [sorted list]
    """
    # Initialize variables not set in the initial call
    if size == None:
        largest_num = max(some_list)
        largest_num_str = str(largest_num)
        largest_num_len = len(largest_num_str)
        size = largest_num_len

    if idex == None:
        idex = size

    # Translate the index we're looking at into an array index.
    # e.g., looking at the 10's place for 100:
    # size: 3
    # idex: 2
    #    i: (3-2) == 1
    # str(123)[i] -> 2
    i = size - idex 

    # The recursive base case.
    # Hint: out of range indexing errors
    if i >= size:
        return some_list

    # Initialize the bins we will place numbers into
    bins = [[] for _ in range(10)]

    # Iterate over the list of numbers we are given
    for e in some_list:
        # The destination bin; e.g.,:
        #   size: 5
        #      e: 29
        #  num_s: '00029'
        #      i: 3
        # dest_c: '2'
        # dest_i: 2
        num_s  = str(e).zfill(size)
        dest_c = num_s[i]
        dest_i = int(dest_c) 
        bins[dest_i] += [e]

    result = []
    for b in bins:
        #If the bin is empty it skips the recursive call
        if b == []:
            continue
        # Make the recursive call
        # Sort each of the sub-lists in our bins
        result.append(radix(b, idex-1, size))

    # Flatten our list
    # This is also called in our recursive call,
    # so we don't need flatten to be recursive.
    flattened_result = flatten(result)

    return flattened_result

```

### python_code_3.txt
```python
#python3.7 <
def flatten(l):
    return [y for x in l for y in x]

def radix(l, p=None, s=None):
    if s == None:
        s = len(str(max(l)))
    if p == None:
        p = s

    i = s - p

    if i >= s:
        return l

    bins = [[] for _ in range(10)]

    for e in l:
        bins[int(str(e).zfill(s)[i])] += [e]

    return flatten([radix(b, p-1, s) for b in bins])

```

