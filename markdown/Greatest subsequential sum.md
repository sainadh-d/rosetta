# Greatest subsequential sum

## Task Link
[Rosetta Code - Greatest subsequential sum](https://rosettacode.org/wiki/Greatest_subsequential_sum)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;
import java.util.ArrayList;

public class Sub{
    private static int[] indices;

    public static void main(String[] args){
        ArrayList<Long> array= new ArrayList<Long>(); //the main set
        Scanner in = new Scanner(System.in);
        while(in.hasNextLong()) array.add(in.nextLong());
        long highSum= Long.MIN_VALUE;//start the sum at the lowest possible value
        ArrayList<Long> highSet= new ArrayList<Long>();
        //loop through all possible subarray sizes including 0
        for(int subSize= 0;subSize<= array.size();subSize++){
            indices= new int[subSize];
            for(int i= 0;i< subSize;i++) indices[i]= i;
            do{
                long sum= 0;//this subarray sum variable
                ArrayList<Long> temp= new ArrayList<Long>();//this subarray
                //sum it and save it
                for(long index:indices) {sum+= array.get(index); temp.add(array.get(index));}
                if(sum > highSum){//if we found a higher sum
                    highSet= temp;    //keep track of it
                    highSum= sum;
                }
            }while(nextIndices(array));//while we haven't tested all subarrays
        }
        System.out.println("Sum: " + highSum + "\nSet: " + 
        		highSet);
    }
    /**
     * Computes the next set of choices from the previous. The
     * algorithm tries to increment the index of the final choice
     * first. Should that fail (index goes out of bounds), it
     * tries to increment the next-to-the-last index, and resets
     * the last index to one more than the next-to-the-last.
     * Should this fail the algorithm keeps starting at an earlier
     * choice until it runs off the start of the choice list without
     * Finding a legal set of indices for all the choices.
     *
     * @return true unless all choice sets have been exhausted.
     * @author James Heliotis
     */

    private static boolean nextIndices(ArrayList<Long> a) {
        for(int i= indices.length-1;i >= 0;--i){
            indices[i]++;
            for(int j=i+1;j < indices.length;++j){
                indices[j]= indices[j - 1] + 1;//reset the last failed try
            }
            if(indices[indices.length - 1] < a.size()){//if this try went out of bounds
                return true;
            }
        }
        return false;
    }
}

```

### java_code_2.txt
```java
private static int BiggestSubsum(int[] t) {
    int sum = 0;
    int maxsum = 0;

    for (int i : t) {
        sum += i;
        if (sum < 0)
            sum = 0;
        maxsum = sum > maxsum ? sum : maxsum;
    }        
    return maxsum;
}

```

## Python Code
### python_code_1.txt
```python
def maxsubseq(seq):
  return max((seq[begin:end] for begin in xrange(len(seq)+1)
                             for end in xrange(begin, len(seq)+1)),
             key=sum)

```

### python_code_2.txt
```python
def maxsum(sequence):
    """Return maximum sum."""
    maxsofar, maxendinghere = 0, 0
    for x in sequence:
        # invariant: ``maxendinghere`` and ``maxsofar`` are accurate for ``x[0..i-1]``          
        maxendinghere = max(maxendinghere + x, 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar

```

### python_code_3.txt
```python
def maxsumseq(sequence):
    start, end, sum_start = -1, -1, -1
    maxsum_, sum_ = 0, 0
    for i, x in enumerate(sequence):
        sum_ += x
        if maxsum_ < sum_: # found maximal subsequence so far
            maxsum_ = sum_
            start, end = sum_start, i
        elif sum_ < 0: # start new sequence
            sum_ = 0
            sum_start = i
    assert maxsum_ == maxsum(sequence) 
    assert maxsum_ == sum(sequence[start + 1:end + 1])
    return sequence[start + 1:end + 1]

```

### python_code_4.txt
```python
def maxsumit(iterable):
    maxseq = seq = []
    start, end, sum_start = -1, -1, -1
    maxsum_, sum_ = 0, 0
    for i, x in enumerate(iterable):
        seq.append(x); sum_ += x
        if maxsum_ < sum_: 
            maxseq = seq; maxsum_ = sum_
            start, end = sum_start, i
        elif sum_ < 0:
            seq = []; sum_ = 0
            sum_start = i
    assert maxsum_ == sum(maxseq[:end - start])
    return maxseq[:end - start]

```

### python_code_5.txt
```python
f = maxsumit
assert f([]) == []
assert f([-1]) == []
assert f([0])  == []
assert f([1])       == [1]
assert f([1, 0])    == [1]
assert f([0, 1])    == [0, 1]   
assert f([0, 1, 0]) == [0, 1]   
assert f([2])         == [2]
assert f([2, -1])     == [2]
assert f([-1, 2])     == [2]
assert f([-1, 2, -1]) == [2]
assert f([2, -1, 3])         == [2, -1, 3]
assert f([2, -1, 3, -1])     == [2, -1, 3] 
assert f([-1, 2, -1, 3])     == [2, -1, 3]
assert f([-1, 2, -1, 3, -1]) == [2, -1, 3]
assert f([-1, 1, 2, -5, -6]) == [1,2]

```

### python_code_6.txt
```python
'''Greatest subsequential sum'''

from functools import (reduce)


# maxSubseq :: [Int] -> [Int] -> (Int, [Int])
def maxSubseq(xs):
    '''Subsequence of xs with the maximum sum'''
    def go(ab, x):
        (m1, m2) = ab[0]
        hi = max((0, []), (m1 + x, m2 + [x]))
        return (hi, max(ab[1], hi))
    return reduce(go, xs, ((0, []), (0, [])))[1]


# TEST -----------------------------------------------------------
print(
    maxSubseq(
        [-1, -2, 3, 5, 6, -2, -1, 4, -4, 2, -1]
    )
)

```

