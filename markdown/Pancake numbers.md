# Pancake numbers

## Task Link
[Rosetta Code - Pancake numbers](https://rosettacode.org/wiki/Pancake_numbers)

## Java Code
### java_code_1.txt
```java
public class Pancake {
    private static int pancake(int n) {
        int gap = 2;
        int sum = 2;
        int adj = -1;
        while (sum < n) {
            adj++;
            gap = 2 * gap - 1;
            sum += gap;
        }
        return n + adj;
    }

    public static void main(String[] args) {
        for (int i = 0; i < 4; i++) {
            for (int j = 1; j < 6; j++) {
                int n = 5 * i + j;
                System.out.printf("p(%2d) = %2d  ", n, pancake(n));
            }
            System.out.println();
        }
    }
}

```

### java_code_2.txt
```java
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.toList;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.stream.IntStream;


public class Pancake {

    private static List<Integer> flipStack(List<Integer> stack, int spatula) {
        List<Integer> copy = new ArrayList<>(stack);
        Collections.reverse(copy.subList(0, spatula));
        return copy;
    }

    private static Map.Entry<List<Integer>, Integer> pancake(int n) {
        List<Integer> initialStack = IntStream.rangeClosed(1, n).boxed().collect(toList());
        Map<List<Integer>, Integer> stackFlips = new HashMap<>();
        stackFlips.put(initialStack, 1);
        Queue<List<Integer>> queue = new ArrayDeque<>();
        queue.add(initialStack);
        while (!queue.isEmpty()) {
            List<Integer> stack = queue.remove();
            int flips = stackFlips.get(stack) + 1;
            for (int i = 2; i <= n; ++i) {
                List<Integer> flipped = flipStack(stack, i);
                if (stackFlips.putIfAbsent(flipped, flips) == null) {
                    queue.add(flipped);
                }
            }
        }
        return stackFlips.entrySet().stream().max(comparing(e -> e.getValue())).get();
    }
     
    public static void main(String[] args) {
        for (int i = 1; i <= 10; ++i) {
            Map.Entry<List<Integer>, Integer> result = pancake(i);
            System.out.printf("pancake(%s) = %s. Example: %s\n", i, result.getValue(), result.getKey());
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
"""Pancake numbers. Requires Python>=3.7."""
import time

from collections import deque
from operator import itemgetter
from typing import Tuple

Pancakes = Tuple[int, ...]


def flip(pancakes: Pancakes, position: int) -> Pancakes:
    """Flip the stack of pancakes at the given position."""
    return tuple([*reversed(pancakes[:position]), *pancakes[position:]])


def pancake(n: int) -> Tuple[Pancakes, int]:
    """Return the nth pancake number."""
    init_stack = tuple(range(1, n + 1))
    stack_flips = {init_stack: 0}
    queue = deque([init_stack])

    while queue:
        stack = queue.popleft()
        flips = stack_flips[stack] + 1

        for i in range(2, n + 1):
            flipped = flip(stack, i)
            if flipped not in stack_flips:
                stack_flips[flipped] = flips
                queue.append(flipped)

    return max(stack_flips.items(), key=itemgetter(1))


if __name__ == "__main__":
    start = time.time()

    for n in range(1, 10):
        pancakes, p = pancake(n)
        print(f"pancake({n}) = {p:>2}. Example: {list(pancakes)}")

    print(f"\nTook {time.time() - start:.3} seconds.")

```

