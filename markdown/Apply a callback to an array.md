# Apply a callback to an array

## Task Link
[Rosetta Code - Apply a callback to an array](https://rosettacode.org/wiki/Apply_a_callback_to_an_array)

## Java Code
### java_code_1.txt
```java
public class ArrayCallback7 {

    interface IntConsumer {
        void run(int x);
    }

    interface IntToInt {
        int run(int x);
    }

    static void forEach(int[] arr, IntConsumer consumer) {
        for (int i : arr) {
            consumer.run(i);
        }
    }

    static void update(int[] arr, IntToInt mapper) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = mapper.run(arr[i]);
        }
    }

    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        forEach(numbers, new IntConsumer() {
            public void run(int x) {
                System.out.println(x);
            }
        });

        update(numbers, new IntToInt() {
            @Override
            public int run(int x) {
                return x * x;
            }
        });

        forEach(numbers, new IntConsumer() {
            public void run(int x) {
                System.out.println(x);
            }
        });
    }
}

```

### java_code_2.txt
```java
import java.util.Arrays;

public class ArrayCallback {

    public static void main(String[] args) {
        int[] myIntArray = {1, 2, 3, 4, 5};

        int sum = Arrays.stream(myIntArray)
                .map(x -> {
                    int cube = x * x * x;
                    System.out.println(cube);
                    return cube;
                })
                .reduce(0, (left, right) -> left + right); // <-- could substitute .sum() for .reduce(...) here.
        System.out.println("sum: " + sum);
    }
}

```

## Python Code
### python_code_1.txt
```python
def square(n):
    return n * n
  
numbers = [1, 3, 5, 7]

squares1 = [square(n) for n in numbers]     # list comprehension

squares2a = map(square, numbers)            # functional form

squares2b = map(lambda x: x*x, numbers)     # functional form with `lambda`

squares3 = [n * n for n in numbers]         # no need for a function,
                                            # anonymous or otherwise

isquares1 = (n * n for n in numbers)        # iterator, lazy

import itertools
isquares2 = itertools.imap(square, numbers) # iterator, lazy

```

### python_code_2.txt
```python
print " ".join(str(n * n) for n in range(10))

```

### python_code_3.txt
```python
print " ".join(map(str, map(square, range(10))))

```

