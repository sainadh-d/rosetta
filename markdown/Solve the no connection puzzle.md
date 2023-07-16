# Solve the no connection puzzle

## Task Link
[Rosetta Code - Solve the no connection puzzle](https://rosettacode.org/wiki/Solve_the_no_connection_puzzle)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.abs;
import java.util.*;
import static java.util.stream.Collectors.toList;
import static java.util.stream.IntStream.range;

public class NoConnection {

    // adopted from Go
    static int[][] links = {
        {2, 3, 4}, // A to C,D,E
        {3, 4, 5}, // B to D,E,F
        {2, 4},    // D to C, E
        {5},       // E to F
        {2, 3, 4}, // G to C,D,E
        {3, 4, 5}, // H to D,E,F
    };

    static int[] pegs = new int[8];

    public static void main(String[] args) {

        List<Integer> vals = range(1, 9).mapToObj(i -> i).collect(toList());
        do {
            Collections.shuffle(vals);
            for (int i = 0; i < pegs.length; i++)
                pegs[i] = vals.get(i);

        } while (!solved());

        printResult();
    }

    static boolean solved() {
        for (int i = 0; i < links.length; i++)
            for (int peg : links[i])
                if (abs(pegs[i] - peg) == 1)
                    return false;
        return true;
    }

    static void printResult() {
        System.out.printf("  %s %s%n", pegs[0], pegs[1]);
        System.out.printf("%s %s %s %s%n", pegs[2], pegs[3], pegs[4], pegs[5]);
        System.out.printf("  %s %s%n", pegs[6], pegs[7]);
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
from itertools import permutations
from enum import Enum

A, B, C, D, E, F, G, H = Enum('Peg', 'A, B, C, D, E, F, G, H')

connections = ((A, C), (A, D), (A, E),
               (B, D), (B, E), (B, F),
               (G, C), (G, D), (G, E),
               (H, D), (H, E), (H, F),
               (C, D), (D, E), (E, F))


def ok(conn, perm):
    """Connected numbers ok?"""
    this, that = (c.value - 1 for c in conn)
    return abs(perm[this] - perm[that]) != 1


def solve():
    return [perm for perm in permutations(range(1, 9))
            if all(ok(conn, perm) for conn in connections)]


if __name__ == '__main__':
    solutions = solve()
    print("A, B, C, D, E, F, G, H =", ', '.join(str(i) for i in solutions[0]))

```

### python_code_2.txt
```python
def pp(solution):
    """Prettyprint a solution"""
    boardformat = r"""
         A   B
        /|\ /|\
       / | X | \
      /  |/ \|  \
     C - D - E - F
      \  |\ /|  /
       \ | X | /
        \|/ \|/
         G   H"""
    for letter, number in zip("ABCDEFGH", solution):
        boardformat = boardformat.replace(letter, str(number))
    print(boardformat)


if __name__ == '__main__':
    for i, s in enumerate(solutions, 1):
        print("\nSolution", i, end='')
        pp(s)

```

