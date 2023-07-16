# Cut a rectangle

## Task Link
[Rosetta Code - Cut a rectangle](https://rosettacode.org/wiki/Cut_a_rectangle)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class CutRectangle {

    private static int[][] dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};

    public static void main(String[] args) {
        cutRectangle(2, 2);
        cutRectangle(4, 3);
    }

    static void cutRectangle(int w, int h) {
        if (w % 2 == 1 && h % 2 == 1)
            return;

        int[][] grid = new int[h][w];
        Stack<Integer> stack = new Stack<>();

        int half = (w * h) / 2;
        long bits = (long) Math.pow(2, half) - 1;

        for (; bits > 0; bits -= 2) {

            for (int i = 0; i < half; i++) {
                int r = i / w;
                int c = i % w;
                grid[r][c] = (bits & (1 << i)) != 0 ? 1 : 0;
                grid[h - r - 1][w - c - 1] = 1 - grid[r][c];
            }

            stack.push(0);
            grid[0][0] = 2;
            int count = 1;
            while (!stack.empty()) {

                int pos = stack.pop();
                int r = pos / w;
                int c = pos % w;

                for (int[] dir : dirs) {

                    int nextR = r + dir[0];
                    int nextC = c + dir[1];

                    if (nextR >= 0 && nextR < h && nextC >= 0 && nextC < w) {

                        if (grid[nextR][nextC] == 1) {
                            stack.push(nextR * w + nextC);
                            grid[nextR][nextC] = 2;
                            count++;
                        }
                    }
                }
            }
            if (count == half) {
                printResult(grid);
            }
        }
    }

    static void printResult(int[][] arr) {
        for (int[] a : arr)
            System.out.println(Arrays.toString(a));
        System.out.println();
    }
}

```

## Python Code
### python_code_1.txt
```python
def cut_it(h, w):
    dirs = ((1, 0), (-1, 0), (0, -1), (0, 1))
    if h % 2: h, w = w, h
    if h % 2: return 0
    if w == 1: return 1
    count = 0

    next = [w + 1, -w - 1, -1, 1]
    blen = (h + 1) * (w + 1) - 1
    grid = [False] * (blen + 1)

    def walk(y, x, count):
        if not y or y == h or not x or x == w:
            return count + 1

        t = y * (w + 1) + x
        grid[t] = grid[blen - t] = True

        if not grid[t + next[0]]:
            count = walk(y + dirs[0][0], x + dirs[0][1], count)
        if not grid[t + next[1]]:
            count = walk(y + dirs[1][0], x + dirs[1][1], count)
        if not grid[t + next[2]]:
            count = walk(y + dirs[2][0], x + dirs[2][1], count)
        if not grid[t + next[3]]:
            count = walk(y + dirs[3][0], x + dirs[3][1], count)

        grid[t] = grid[blen - t] = False
        return count

    t = h // 2 * (w + 1) + w // 2
    if w % 2:
        grid[t] = grid[t + 1] = True
        count = walk(h // 2, w // 2 - 1, count)
        res = count
        count = 0
        count = walk(h // 2 - 1, w // 2, count)
        return res + count * 2
    else:
        grid[t] = True
        count = walk(h // 2, w // 2 - 1, count)
        if h == w:
            return count * 2
        count = walk(h // 2 - 1, w // 2, count)
        return count

def main():
    for w in xrange(1, 10):
        for h in xrange(1, w + 1):
            if not((w * h) % 2):
                print "%d x %d: %d" % (w, h, cut_it(w, h))

main()

```

### python_code_2.txt
```python
try:
    import psyco
except ImportError:
    pass
else:
    psyco.full()

w, h = 0, 0
count = 0
vis = []

def cwalk(y, x, d):
    global vis, count, w, h
    if not y or y == h or not x or x == w:
        count += 1
        return

    vis[y][x] = vis[h - y][w - x] = 1

    if x and not vis[y][x - 1]:
        cwalk(y, x - 1, d | 1)
    if (d & 1) and x < w and not vis[y][x+1]:
        cwalk(y, x + 1, d|1)
    if y and not vis[y - 1][x]:
        cwalk(y - 1, x, d | 2)
    if (d & 2) and y < h and not vis[y + 1][x]:
        cwalk(y + 1, x, d | 2)

    vis[y][x] = vis[h - y][w - x] = 0

def count_only(x, y):
    global vis, count, w, h
    count = 0
    w = x
    h = y

    if (h * w) & 1:
        return count
    if h & 1:
        w, h = h, w

    vis = [[0] * (w + 1) for _ in xrange(h + 1)]
    vis[h // 2][w // 2] = 1

    if w & 1:
        vis[h // 2][w // 2 + 1] = 1

    res = 0
    if w > 1:
        cwalk(h // 2, w // 2 - 1, 1)
        res = 2 * count - 1
        count = 0
        if w != h:
            cwalk(h // 2 + 1, w // 2, 3 if (w & 1) else 2)

        res += 2 * count - (not (w & 1))
    else:
        res = 1

    if w == h:
        res = 2 * res + 2
    return res

def main():
    for y in xrange(1, 10):
        for x in xrange(1, y + 1):
            if not (x & 1) or not (y & 1):
                print "%d x %d: %d" % (y, x, count_only(x, y))

main()

```

