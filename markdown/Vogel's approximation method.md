# Vogel's approximation method

## Task Link
[Rosetta Code - Vogel's approximation method](https://rosettacode.org/wiki/Vogel%27s_approximation_method)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import static java.util.Arrays.stream;
import java.util.concurrent.*;

public class VogelsApproximationMethod {

    final static int[] demand = {30, 20, 70, 30, 60};
    final static int[] supply = {50, 60, 50, 50};
    final static int[][] costs = {{16, 16, 13, 22, 17}, {14, 14, 13, 19, 15},
    {19, 19, 20, 23, 50}, {50, 12, 50, 15, 11}};

    final static int nRows = supply.length;
    final static int nCols = demand.length;

    static boolean[] rowDone = new boolean[nRows];
    static boolean[] colDone = new boolean[nCols];
    static int[][] result = new int[nRows][nCols];

    static ExecutorService es = Executors.newFixedThreadPool(2);

    public static void main(String[] args) throws Exception {
        int supplyLeft = stream(supply).sum();
        int totalCost = 0;

        while (supplyLeft > 0) {
            int[] cell = nextCell();
            int r = cell[0];
            int c = cell[1];

            int quantity = Math.min(demand[c], supply[r]);
            demand[c] -= quantity;
            if (demand[c] == 0)
                colDone[c] = true;

            supply[r] -= quantity;
            if (supply[r] == 0)
                rowDone[r] = true;

            result[r][c] = quantity;
            supplyLeft -= quantity;

            totalCost += quantity * costs[r][c];
        }

        stream(result).forEach(a -> System.out.println(Arrays.toString(a)));
        System.out.println("Total cost: " + totalCost);

        es.shutdown();
    }

    static int[] nextCell() throws Exception {
        Future<int[]> f1 = es.submit(() -> maxPenalty(nRows, nCols, true));
        Future<int[]> f2 = es.submit(() -> maxPenalty(nCols, nRows, false));

        int[] res1 = f1.get();
        int[] res2 = f2.get();

        if (res1[3] == res2[3])
            return res1[2] < res2[2] ? res1 : res2;

        return (res1[3] > res2[3]) ? res2 : res1;
    }

    static int[] diff(int j, int len, boolean isRow) {
        int min1 = Integer.MAX_VALUE, min2 = Integer.MAX_VALUE;
        int minP = -1;
        for (int i = 0; i < len; i++) {
            if (isRow ? colDone[i] : rowDone[i])
                continue;
            int c = isRow ? costs[j][i] : costs[i][j];
            if (c < min1) {
                min2 = min1;
                min1 = c;
                minP = i;
            } else if (c < min2)
                min2 = c;
        }
        return new int[]{min2 - min1, min1, minP};
    }

    static int[] maxPenalty(int len1, int len2, boolean isRow) {
        int md = Integer.MIN_VALUE;
        int pc = -1, pm = -1, mc = -1;
        for (int i = 0; i < len1; i++) {
            if (isRow ? rowDone[i] : colDone[i])
                continue;
            int[] res = diff(i, len2, isRow);
            if (res[0] > md) {
                md = res[0];  // max diff
                pm = i;       // pos of max diff
                mc = res[1];  // min cost
                pc = res[2];  // pos of min cost
            }
        }
        return isRow ? new int[]{pm, pc, mc, md} : new int[]{pc, pm, mc, md};
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict

costs  = {'W': {'A': 16, 'B': 16, 'C': 13, 'D': 22, 'E': 17},
          'X': {'A': 14, 'B': 14, 'C': 13, 'D': 19, 'E': 15},
          'Y': {'A': 19, 'B': 19, 'C': 20, 'D': 23, 'E': 50},
          'Z': {'A': 50, 'B': 12, 'C': 50, 'D': 15, 'E': 11}}
demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
cols = sorted(demand.iterkeys())
supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}
res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
    g[x] = sorted(costs[x].iterkeys(), key=lambda g: costs[x][g])
for x in demand:
    g[x] = sorted(costs.iterkeys(), key=lambda g: costs[g][x])

while g:
    d = {}
    for x in demand:
        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]
    s = {}
    for x in supply:
        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
    f = max(d, key=lambda n: d[n])
    t = max(s, key=lambda n: s[n])
    t, f = (f, g[f][0]) if d[f] > s[t] else (g[t][0], t)
    v = min(supply[f], demand[t])
    res[f][t] += v
    demand[t] -= v
    if demand[t] == 0:
        for k, n in supply.iteritems():
            if n != 0:
                g[k].remove(t)
        del g[t]
        del demand[t]
    supply[f] -= v
    if supply[f] == 0:
        for k, n in demand.iteritems():
            if n != 0:
                g[k].remove(f)
        del g[f]
        del supply[f]

for n in cols:
    print "\t", n,
print
cost = 0
for g in sorted(costs):
    print g, "\t",
    for n in cols:
        y = res[g][n]
        if y != 0:
            print y,
        cost += y * costs[g][n]
        print "\t",
    print
print "\n\nTotal Cost = ", cost

```

