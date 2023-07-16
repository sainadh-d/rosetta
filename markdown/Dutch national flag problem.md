# Dutch national flag problem

## Task Link
[Rosetta Code - Dutch national flag problem](https://rosettacode.org/wiki/Dutch_national_flag_problem)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Random;

public class DutchNationalFlag {
    enum DutchColors {
        RED, WHITE, BLUE
    }

    public static void main(String[] args){
        DutchColors[] balls = new DutchColors[12];
        DutchColors[] values = DutchColors.values();
        Random rand = new Random();

        for (int i = 0; i < balls.length; i++)
            balls[i]=values[rand.nextInt(values.length)];
        System.out.println("Before: " + Arrays.toString(balls));

        Arrays.sort(balls);
        System.out.println("After:  " + Arrays.toString(balls));

        boolean sorted = true;
        for (int i = 1; i < balls.length; i++ ){
            if (balls[i-1].compareTo(balls[i]) > 0){
                sorted=false;
                break;
            }
        }
        System.out.println("Correctly sorted: " + sorted);
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

colours_in_order = 'Red White Blue'.split()

def dutch_flag_sort(items, order=colours_in_order):
    'return sort of items using the given order'
    reverse_index = dict((x,i) for i,x in enumerate(order))
    return sorted(items, key=lambda x: reverse_index[x])

def dutch_flag_check(items, order=colours_in_order):
    'Return True if each item of items is in the given order'
    reverse_index = dict((x,i) for i,x in enumerate(order))
    order_of_items = [reverse_index[item] for item in items]
    return all(x <= y for x, y in zip(order_of_items, order_of_items[1:]))

def random_balls(mx=5):
    'Select from 1 to mx balls of each colour, randomly'
    balls = sum([[colour] * random.randint(1, mx)
                 for colour in colours_in_order], [])
    random.shuffle(balls)
    return balls

def main():
    # Ensure we start unsorted
    while True:
        balls = random_balls()
        if not dutch_flag_check(balls):
            break
    print("Original Ball order:", balls)
    sorted_balls = dutch_flag_sort(balls)
    print("Sorted Ball Order:", sorted_balls)
    assert dutch_flag_check(sorted_balls), 'Whoops. Not sorted!'

if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
from itertools import chain
def dutch_flag_sort2(items, order=colours_in_order):
    'return summed filter of items using the given order'
    return list(chain.from_iterable(filter(lambda c: c==colour, items)
                                    for colour in order))

```

### python_code_3.txt
```python
def dutch_flag_sort2(items, order=colours_in_order):
    'return summed filter of items using the given order'
    return [c for colour in order for c in items if c==colour]

```

### python_code_4.txt
```python
def dutch_flag_sort3(items, order=colours_in_order):
    'counts each colour to construct flag'
    return sum([[colour] * items.count(colour) for colour in order], [])

```

### python_code_5.txt
```python
import random

colours_in_order = 'Red White Blue'.split()

def dutch_flag_sort(items):
    '''\
    In-place sort of list items using the given order.
    Python idiom is to return None when argument is modified in-place

    O(n)? Algorithm from Go language implementation of
    http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Sort/Flag/'''

    lo, mid, hi = 0, 0, len(items)-1
    while mid <= hi:
        colour = items[mid]
        if colour == 'Red':
            items[lo], items[mid] = items[mid], items[lo]
            lo += 1
            mid += 1
        elif colour == 'White':
            mid += 1
        else:
            items[mid], items[hi] = items[hi], items[mid]
            hi -= 1

def dutch_flag_check(items, order=colours_in_order):
    'Return True if each item of items is in the given order'
    order_of_items = [order.index(item) for item in items]
    return all(x <= y for x, y in zip(order_of_items, order_of_items[1:]))

def random_balls(mx=5):
    'Select from 1 to mx balls of each colour, randomly'
    balls = sum(([[colour] * random.randint(1, mx)
                 for colour in colours_in_order]), [])
    random.shuffle(balls)
    return balls

def main():
    # Ensure we start unsorted
    while 1:
        balls = random_balls()
        if not dutch_flag_check(balls):
            break
    print("Original Ball order:", balls)
    dutch_flag_sort(balls)
    print("Sorted Ball Order:", balls)
    assert dutch_flag_check(balls), 'Whoops. Not sorted!'

if __name__ == '__main__':
    main()

```

