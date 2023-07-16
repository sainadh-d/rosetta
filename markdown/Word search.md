# Word search

## Task Link
[Rosetta Code - Word search](https://rosettacode.org/wiki/Word_search)

## Java Code
### java_code_1.txt
```java
import java.io.*;
import static java.lang.String.format;
import java.util.*;

public class WordSearch {
    static class Grid {
        int numAttempts;
        char[][] cells = new char[nRows][nCols];
        List<String> solutions = new ArrayList<>();
    }

    final static int[][] dirs = {{1, 0}, {0, 1}, {1, 1}, {1, -1}, {-1, 0},
    {0, -1}, {-1, -1}, {-1, 1}};

    final static int nRows = 10;
    final static int nCols = 10;
    final static int gridSize = nRows * nCols;
    final static int minWords = 25;

    final static Random rand = new Random();

    public static void main(String[] args) {
        printResult(createWordSearch(readWords("unixdict.txt")));
    }

    static List<String> readWords(String filename) {
        int maxLen = Math.max(nRows, nCols);

        List<String> words = new ArrayList<>();
        try (Scanner sc = new Scanner(new FileReader(filename))) {
            while (sc.hasNext()) {
                String s = sc.next().trim().toLowerCase();
                if (s.matches("^[a-z]{3," + maxLen + "}$"))
                    words.add(s);
            }
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
        return words;
    }

    static Grid createWordSearch(List<String> words) {
        Grid grid = null;
        int numAttempts = 0;

        outer:
        while (++numAttempts < 100) {
            Collections.shuffle(words);

            grid = new Grid();
            int messageLen = placeMessage(grid, "Rosetta Code");
            int target = gridSize - messageLen;

            int cellsFilled = 0;
            for (String word : words) {
                cellsFilled += tryPlaceWord(grid, word);
                if (cellsFilled == target) {
                    if (grid.solutions.size() >= minWords) {
                        grid.numAttempts = numAttempts;
                        break outer;
                    } else break; // grid is full but we didn't pack enough words, start over
                }
            }
        }

        return grid;
    }

    static int placeMessage(Grid grid, String msg) {
        msg = msg.toUpperCase().replaceAll("[^A-Z]", "");

        int messageLen = msg.length();
        if (messageLen > 0 && messageLen < gridSize) {
            int gapSize = gridSize / messageLen;

            for (int i = 0; i < messageLen; i++) {
                int pos = i * gapSize + rand.nextInt(gapSize);
                grid.cells[pos / nCols][pos % nCols] = msg.charAt(i);
            }
            return messageLen;
        }
        return 0;
    }

    static int tryPlaceWord(Grid grid, String word) {
        int randDir = rand.nextInt(dirs.length);
        int randPos = rand.nextInt(gridSize);

        for (int dir = 0; dir < dirs.length; dir++) {
            dir = (dir + randDir) % dirs.length;

            for (int pos = 0; pos < gridSize; pos++) {
                pos = (pos + randPos) % gridSize;

                int lettersPlaced = tryLocation(grid, word, dir, pos);
                if (lettersPlaced > 0)
                    return lettersPlaced;
            }
        }
        return 0;
    }

    static int tryLocation(Grid grid, String word, int dir, int pos) {

        int r = pos / nCols;
        int c = pos % nCols;
        int len = word.length();

        //  check bounds
        if ((dirs[dir][0] == 1 && (len + c) > nCols)
                || (dirs[dir][0] == -1 && (len - 1) > c)
                || (dirs[dir][1] == 1 && (len + r) > nRows)
                || (dirs[dir][1] == -1 && (len - 1) > r))
            return 0;

        int rr, cc, i, overlaps = 0;

        // check cells
        for (i = 0, rr = r, cc = c; i < len; i++) {
            if (grid.cells[rr][cc] != 0 && grid.cells[rr][cc] != word.charAt(i))
                return 0;
            cc += dirs[dir][0];
            rr += dirs[dir][1];
        }

        // place
        for (i = 0, rr = r, cc = c; i < len; i++) {
            if (grid.cells[rr][cc] == word.charAt(i))
                overlaps++;
            else
                grid.cells[rr][cc] = word.charAt(i);

            if (i < len - 1) {
                cc += dirs[dir][0];
                rr += dirs[dir][1];
            }
        }

        int lettersPlaced = len - overlaps;
        if (lettersPlaced > 0) {
            grid.solutions.add(format("%-10s (%d,%d)(%d,%d)", word, c, r, cc, rr));
        }

        return lettersPlaced;
    }

    static void printResult(Grid grid) {
        if (grid == null || grid.numAttempts == 0) {
            System.out.println("No grid to display");
            return;
        }
        int size = grid.solutions.size();

        System.out.println("Attempts: " + grid.numAttempts);
        System.out.println("Number of words: " + size);

        System.out.println("\n     0  1  2  3  4  5  6  7  8  9");
        for (int r = 0; r < nRows; r++) {
            System.out.printf("%n%d   ", r);
            for (int c = 0; c < nCols; c++)
                System.out.printf(" %c ", grid.cells[r][c]);
        }

        System.out.println("\n");

        for (int i = 0; i < size - 1; i += 2) {
            System.out.printf("%s   %s%n", grid.solutions.get(i),
                    grid.solutions.get(i + 1));
        }
        if (size % 2 == 1)
            System.out.println(grid.solutions.get(size - 1));
    }
}

```

## Python Code
### python_code_1.txt
```python
import re
from random import shuffle, randint

dirs = [[1, 0], [0, 1], [1, 1], [1, -1], [-1, 0], [0, -1], [-1, -1], [-1, 1]]
n_rows = 10
n_cols = 10
grid_size = n_rows * n_cols
min_words = 25


class Grid:
    def __init__(self):
        self.num_attempts = 0
        self.cells = [['' for _ in range(n_cols)] for _ in range(n_rows)]
        self.solutions = []


def read_words(filename):
    max_len = max(n_rows, n_cols)

    words = []
    with open(filename, "r") as file:
        for line in file:
            s = line.strip().lower()
            if re.match(r'^[a-z]{3,' + re.escape(str(max_len)) + r'}$', s) is not None:
                words.append(s)

    return words


def place_message(grid, msg):
    msg = re.sub(r'[^A-Z]', "", msg.upper())

    message_len = len(msg)
    if 0 < message_len < grid_size:
        gap_size = grid_size // message_len

        for i in range(0, message_len):
            pos = i * gap_size + randint(0, gap_size)
            grid.cells[pos // n_cols][pos % n_cols] = msg[i]

        return message_len

    return 0


def try_location(grid, word, direction, pos):
    r = pos // n_cols
    c = pos % n_cols
    length = len(word)

    # check bounds
    if (dirs[direction][0] == 1 and (length + c) > n_cols) or \
       (dirs[direction][0] == -1 and (length - 1) > c) or \
       (dirs[direction][1] == 1 and (length + r) > n_rows) or \
       (dirs[direction][1] == -1 and (length - 1) > r):
        return 0

    rr = r
    cc = c
    i = 0
    overlaps = 0

    # check cells
    while i < length:
        if grid.cells[rr][cc] != '' and grid.cells[rr][cc] != word[i]:
            return 0
        cc += dirs[direction][0]
        rr += dirs[direction][1]
        i += 1

    rr = r
    cc = c
    i = 0
    # place
    while i < length:
        if grid.cells[rr][cc] == word[i]:
            overlaps += 1
        else:
            grid.cells[rr][cc] = word[i]

        if i < length - 1:
            cc += dirs[direction][0]
            rr += dirs[direction][1]

        i += 1

    letters_placed = length - overlaps
    if letters_placed > 0:
        grid.solutions.append("{0:<10} ({1},{2})({3},{4})".format(word, c, r, cc, rr))

    return letters_placed


def try_place_word(grid, word):
    rand_dir = randint(0, len(dirs))
    rand_pos = randint(0, grid_size)

    for direction in range(0, len(dirs)):
        direction = (direction + rand_dir) % len(dirs)

        for pos in range(0, grid_size):
            pos = (pos + rand_pos) % grid_size

            letters_placed = try_location(grid, word, direction, pos)
            if letters_placed > 0:
                return letters_placed

    return 0


def create_word_search(words):
    grid = None
    num_attempts = 0

    while num_attempts < 100:
        num_attempts += 1
        shuffle(words)

        grid = Grid()
        message_len = place_message(grid, "Rosetta Code")
        target = grid_size - message_len

        cells_filled = 0
        for word in words:
            cells_filled += try_place_word(grid, word)
            if cells_filled == target:
                if len(grid.solutions) >= min_words:
                    grid.num_attempts = num_attempts
                    return grid
                else:
                    break # grid is full but we didn't pack enough words, start over

    return grid


def print_result(grid):
    if grid is None or grid.num_attempts == 0:
        print("No grid to display")
        return

    size = len(grid.solutions)

    print("Attempts: {0}".format(grid.num_attempts))
    print("Number of words: {0}".format(size))

    print("\n     0  1  2  3  4  5  6  7  8  9\n")
    for r in range(0, n_rows):
        print("{0}   ".format(r), end='')
        for c in range(0, n_cols):
            print(" %c " % grid.cells[r][c], end='')
        print()
    print()

    for i in range(0, size - 1, 2):
        print("{0}   {1}".format(grid.solutions[i], grid.solutions[i+1]))

    if size % 2 == 1:
        print(grid.solutions[size - 1])


if __name__ == "__main__":
    print_result(create_word_search(read_words("unixdict.txt")))

```

