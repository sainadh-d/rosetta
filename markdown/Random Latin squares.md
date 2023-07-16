# Random Latin squares

## Task Link
[Rosetta Code - Random Latin squares](https://rosettacode.org/wiki/Random_Latin_squares)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;

public class RandomLatinSquares {
    private static void printSquare(List<List<Integer>> latin) {
        for (List<Integer> row : latin) {
            Iterator<Integer> it = row.iterator();

            System.out.print("[");
            if (it.hasNext()) {
                Integer col = it.next();
                System.out.print(col);
            }
            while (it.hasNext()) {
                Integer col = it.next();
                System.out.print(", ");
                System.out.print(col);
            }
            System.out.println("]");
        }
        System.out.println();
    }

    private static void latinSquare(int n) {
        if (n <= 0) {
            System.out.println("[]");
            return;
        }

        List<List<Integer>> latin = new ArrayList<>(n);
        for (int i = 0; i < n; ++i) {
            List<Integer> inner = new ArrayList<>(n);
            for (int j = 0; j < n; ++j) {
                inner.add(j);
            }
            latin.add(inner);
        }
        // first row
        Collections.shuffle(latin.get(0));

        // middle row(s)
        for (int i = 1; i < n - 1; ++i) {
            boolean shuffled = false;
            shuffling:
            while (!shuffled) {
                Collections.shuffle(latin.get(i));
                for (int k = 0; k < i; ++k) {
                    for (int j = 0; j < n; ++j) {
                        if (Objects.equals(latin.get(k).get(j), latin.get(i).get(j))) {
                            continue shuffling;
                        }
                    }
                }
                shuffled = true;
            }
        }

        // last row
        for (int j = 0; j < n; ++j) {
            List<Boolean> used = new ArrayList<>(n);
            for (int i = 0; i < n; ++i) {
                used.add(false);
            }
            for (int i = 0; i < n - 1; ++i) {
                used.set(latin.get(i).get(j), true);
            }
            for (int k = 0; k < n; ++k) {
                if (!used.get(k)) {
                    latin.get(n - 1).set(j, k);
                    break;
                }
            }
        }

        printSquare(latin);
    }

    public static void main(String[] args) {
        latinSquare(5);
        latinSquare(5);
        latinSquare(10);
    }
}

```

## Python Code
### python_code_1.txt
```python
from random import choice, shuffle
from copy import deepcopy

def rls(n):
    if n <= 0:
        return []
    else:
        symbols = list(range(n))
        square = _rls(symbols)
        return _shuffle_transpose_shuffle(square)


def _shuffle_transpose_shuffle(matrix):
    square = deepcopy(matrix)
    shuffle(square)
    trans = list(zip(*square))
    shuffle(trans)
    return trans


def _rls(symbols):
    n = len(symbols)
    if n == 1:
        return [symbols]
    else:
        sym = choice(symbols)
        symbols.remove(sym)
        square = _rls(symbols)
        square.append(square[0].copy())
        for i in range(n):
            square[i].insert(i, sym)
        return square

def _to_text(square):
    if square:
        width = max(len(str(sym)) for row in square for sym in row)
        txt = '\n'.join(' '.join(f"{sym:>{width}}" for sym in row)
                        for row in square)
    else:
        txt = ''
    return txt

def _check(square):
    transpose = list(zip(*square))
    assert _check_rows(square) and _check_rows(transpose), \
        "Not a Latin square"

def _check_rows(square):
    if not square:
        return True
    set_row0 = set(square[0])
    return all(len(row) == len(set(row)) and set(row) == set_row0
               for row in square)


if __name__ == '__main__':
    for i in [3, 3,  5, 5, 12]:
        square = rls(i)
        print(_to_text(square))
        _check(square)
        print()

```

