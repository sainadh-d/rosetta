# Perfect shuffle

## Task Link
[Rosetta Code - Perfect shuffle](https://rosettacode.org/wiki/Perfect_shuffle)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.stream.IntStream;

public class PerfectShuffle {

    public static void main(String[] args) {
        int[] sizes = {8, 24, 52, 100, 1020, 1024, 10_000};
        for (int size : sizes)
            System.out.printf("%5d : %5d%n", size, perfectShuffle(size));
    }

    static int perfectShuffle(int size) {
        if (size % 2 != 0)
            throw new IllegalArgumentException("size must be even");

        int half = size / 2;
        int[] a = IntStream.range(0, size).toArray();
        int[] original = a.clone();
        int[] aa = new int[size];

        for (int count = 1; true; count++) {
            System.arraycopy(a, 0, aa, 0, size);

            for (int i = 0; i < half; i++) {
                a[2 * i] = aa[i];
                a[2 * i + 1] = aa[i + half];
            }

            if (Arrays.equals(a, original))
                return count;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import doctest
import random


def flatten(lst):
    """
    >>> flatten([[3,2],[1,2]])
    [3, 2, 1, 2]
    """
    return [i for sublst in lst for i in sublst]

def magic_shuffle(deck):
    """
    >>> magic_shuffle([1,2,3,4])
    [1, 3, 2, 4]
    """
    half = len(deck) // 2 
    return flatten(zip(deck[:half], deck[half:]))

def after_how_many_is_equal(shuffle_type,start,end):
    """
    >>> after_how_many_is_equal(magic_shuffle,[1,2,3,4],[1,2,3,4])
    2
    """

    start = shuffle_type(start)
    counter = 1
    while start != end:
        start = shuffle_type(start)
        counter += 1
    return counter

def main():
    doctest.testmod()

    print("Length of the deck of cards | Perfect shuffles needed to obtain the same deck back")
    for length in (8, 24, 52, 100, 1020, 1024, 10000):
        deck = list(range(length))
        shuffles_needed = after_how_many_is_equal(magic_shuffle,deck,deck)
        print("{} | {}".format(length,shuffles_needed))


if __name__ == "__main__":
    main()

```

### python_code_2.txt
```python
"""
Brute force solution for the Perfect Shuffle problem.
See http://oeis.org/A002326 for possible improvements
"""
from functools import partial
from itertools import chain
from operator import eq
from typing import (Callable,
                    Iterable,
                    Iterator,
                    List,
                    TypeVar)

T = TypeVar('T')


def main():
    print("Deck length | Shuffles ")
    for length in (8, 24, 52, 100, 1020, 1024, 10000):
        deck = list(range(length))
        shuffles_needed = spin_number(deck, shuffle)
        print(f"{length:<11} | {shuffles_needed}")


def shuffle(deck: List[T]) -> List[T]:
    """[1, 2, 3, 4] -> [1, 3, 2, 4]"""
    half = len(deck) // 2
    return list(chain.from_iterable(zip(deck[:half], deck[half:])))


def spin_number(source: T,
                function: Callable[[T], T]) -> int:
    """
    Applies given function to the source
    until the result becomes equal to it,
    returns the number of calls 
    """
    is_equal_source = partial(eq, source)
    spins = repeat_call(function, source)
    return next_index(is_equal_source,
                      spins,
                      start=1)


def repeat_call(function: Callable[[T], T],
                value: T) -> Iterator[T]:
    """(f, x) -> f(x), f(f(x)), f(f(f(x))), ..."""
    while True:
        value = function(value)
        yield value


def next_index(predicate: Callable[[T], bool],
               iterable: Iterable[T],
               start: int = 0) -> int:
    """
    Returns index of the first element of the iterable
    satisfying given condition
    """
    for index, item in enumerate(iterable, start=start):
        if predicate(item):
            return index


if __name__ == "__main__":
    main()

```

### python_code_3.txt
```python
def mul_ord2(n):
	# directly calculate how many shuffles are needed to restore
	# initial order: 2^o mod(n-1) == 1
	if n == 2: return 1

	n,t,o = n-1,2,1
	while t != 1:
		t,o = (t*2)%n,o+1
	return o

def shuffles(n):
	a,c = list(range(n)), 0
	b = a

	while True:
		# Reverse shuffle; a[i] can be taken as the current
		# position of the card with value i.  This is faster.
		a = a[0:n:2] + a[1:n:2]
		c += 1
		if b == a: break
	return c

for n in range(2, 10000, 2):
	#print(n, mul_ord2(n))
	print(n, shuffles(n))

```

