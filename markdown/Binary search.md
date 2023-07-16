# Binary search

## Task Link
[Rosetta Code - Binary search](https://rosettacode.org/wiki/Binary_search)

## Java Code
### java_code_1.txt
```java
public class BinarySearchIterative {

    public static int binarySearch(int[] nums, int check) {
        int hi = nums.length - 1;
        int lo = 0;
        while (hi >= lo) {
            int guess = (lo + hi) >>> 1;  // from OpenJDK
            if (nums[guess] > check) {
                hi = guess - 1;
            } else if (nums[guess] < check) {
                lo = guess + 1;
            } else {
                return guess;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] haystack = {1, 5, 6, 7, 8, 11};
        int needle = 5;
        int index = binarySearch(haystack, needle);
        if (index == -1) {
            System.out.println(needle + " is not in the array");
        } else {
            System.out.println(needle + " is at index " + index);
        }
    }
}

```

### java_code_2.txt
```java
public class BinarySearchRecursive {

    public static int binarySearch(int[] haystack, int needle, int lo, int hi) {
        if (hi < lo) {
            return -1;
        }
        int guess = (hi + lo) / 2;
        if (haystack[guess] > needle) {
            return binarySearch(haystack, needle, lo, guess - 1);
        } else if (haystack[guess] < needle) {
            return binarySearch(haystack, needle, guess + 1, hi);
        }
        return guess;
    }

    public static void main(String[] args) {
        int[] haystack = {1, 5, 6, 7, 8, 11};
        int needle = 5;

        int index = binarySearch(haystack, needle, 0, haystack.length);

        if (index == -1) {
            System.out.println(needle + " is not in the array");
        } else {
            System.out.println(needle + " is at index " + index);
        }
    }
}

```

### java_code_3.txt
```java
import java.util.Arrays;

int index = Arrays.binarySearch(array, thing);
int index = Arrays.binarySearch(array, startIndex, endIndex, thing);

// for objects, also optionally accepts an additional comparator argument:
int index = Arrays.binarySearch(array, thing, comparator);
int index = Arrays.binarySearch(array, startIndex, endIndex, thing, comparator);

```

### java_code_4.txt
```java
import java.util.Collections;

int index = Collections.binarySearch(list, thing);
int index = Collections.binarySearch(list, thing, comparator);

```

## Python Code
### python_code_1.txt
```python
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

```

### python_code_2.txt
```python
# findIndexBinary :: (a -> Ordering) -> [a] -> Maybe Int
def findIndexBinary(p):
    def isFound(bounds):
        (lo, hi) = bounds
        return lo > hi or 0 == hi

    def half(xs):
        def choice(lh):
            (lo, hi) = lh
            mid = (lo + hi) // 2
            cmpr = p(xs[mid])
            return (lo, mid - 1) if cmpr < 0 else (
                (1 + mid, hi) if cmpr > 0 else (
                    mid, 0
                )
            )
        return lambda bounds: choice(bounds)

    def go(xs):
        (lo, hi) = until(isFound)(
            half(xs)
        )((0, len(xs) - 1)) if xs else None
        return None if 0 != hi else lo

    return lambda xs: go(xs)


# COMPARISON CONSTRUCTORS ---------------------------------

# compare :: a -> a -> Ordering
def compare(a):
    '''Simple comparison of x and y -> LT|EQ|GT'''
    return lambda b: -1 if a < b else (1 if a > b else 0)


# byKV :: (a -> b) -> a -> a -> Ordering
def byKV(f):
    '''Property accessor function -> target value -> x -> LT|EQ|GT'''
    def go(v, x):
        fx = f(x)
        return -1 if v < fx else 1 if v > fx else 0
    return lambda v: lambda x: go(v, x)


# TESTS ---------------------------------------------------
def main():

    # BINARY SEARCH FOR WORD IN AZ-SORTED LIST

    mb1 = findIndexBinary(compare('iota'))(
        # Sorted AZ
        ['alpha', 'beta', 'delta', 'epsilon', 'eta', 'gamma', 'iota',
         'kappa', 'lambda', 'mu', 'theta', 'zeta']
    )

    print (
        'Not found' if None is mb1 else (
            'Word found at index ' + str(mb1)
        )
    )

    # BINARY SEARCH FOR WORD OF GIVEN LENGTH (IN WORD-LENGTH SORTED LIST)

    mb2 = findIndexBinary(byKV(len)(7))(
        # Sorted by rising length
        ['mu', 'eta', 'beta', 'iota', 'zeta', 'alpha', 'delta', 'gamma',
         'kappa', 'theta', 'lambda', 'epsilon']
    )

    print (
        'Not found' if None is mb2 else (
            'Word of given length found at index ' + str(mb2)
        )
    )


# GENERIC -------------------------------------------------

# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
def binary_search(l, value, low = 0, high = -1):
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low >= high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search(l, value, low, mid-1)
    elif l[mid] < value: return binary_search(l, value, mid+1, high)
    else: return mid

```

### python_code_4.txt
```python
# findIndexBinary_ :: (a -> Ordering) -> [a] -> Maybe Int
def findIndexBinary_(p):
    def go(xs):
        def bin(lo, hi):
            if hi < lo:
                return None
            else:
                mid = (lo + hi) // 2
                cmpr = p(xs[mid])
                return bin(lo, mid - 1) if -1 == cmpr else (
                    bin(mid + 1, hi) if 1 == cmpr else (
                        mid
                    )
                )
        n = len(xs)
        return bin(0, n - 1) if 0 < n else None
    return lambda xs: go(xs)


# COMPARISON CONSTRUCTORS ---------------------------------

# compare :: a -> a -> Ordering
def compare(a):
    '''Simple comparison of x and y -> LT|EQ|GT'''
    return lambda b: -1 if a < b else (1 if a > b else 0)


# byKV :: (a -> b) -> a -> a -> Ordering
def byKV(f):
    '''Property accessor function -> target value -> x -> LT|EQ|GT'''
    def go(v, x):
        fx = f(x)
        return -1 if v < fx else 1 if v > fx else 0
    return lambda v: lambda x: go(v, x)


# TESTS ---------------------------------------------------


if __name__ == '__main__':

    # BINARY SEARCH FOR WORD IN AZ-SORTED LIST

    mb1 = findIndexBinary_(compare('mu'))(
        # Sorted AZ
        ['alpha', 'beta', 'delta', 'epsilon', 'eta', 'gamma', 'iota',
         'kappa', 'lambda', 'mu', 'theta', 'zeta']
    )

    print (
        'Not found' if None is mb1 else (
            'Word found at index ' + str(mb1)
        )
    )

    # BINARY SEARCH FOR WORD OF GIVEN LENGTH (IN WORD-LENGTH SORTED LIST)

    mb2 = findIndexBinary_(byKV(len)(6))(
        # Sorted by rising length
        ['mu', 'eta', 'beta', 'iota', 'zeta', 'alpha', 'delta', 'gamma',
         'kappa', 'theta', 'lambda', 'epsilon']
    )

    print (
        'Not found' if None is mb2 else (
            'Word of given length found at index ' + str(mb2)
        )
    )

```

### python_code_5.txt
```python
index = bisect.bisect_left(list, item) # leftmost insertion point
index = bisect.bisect_right(list, item) # rightmost insertion point
index = bisect.bisect(list, item) # same as bisect_right

# same as above but actually insert the item into the list at the given place:
bisect.insort_left(list, item)
bisect.insort_right(list, item)
bisect.insort(list, item)

```

### python_code_6.txt
```python
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

```

### python_code_7.txt
```python
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low + 1 < high:
        mid = (low+high)//2
        if l[mid] > value:
            high = mid
        elif l[mid] < value:
            low = mid
        else:
            return mid
    return high if abs(l[high] - value) < abs(l[low] - value) else low

```

