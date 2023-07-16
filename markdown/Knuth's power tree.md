# Knuth's power tree

## Task Link
[Rosetta Code - Knuth's power tree](https://rosettacode.org/wiki/Knuth%27s_power_tree)

## Java Code
### java_code_1.txt
```java
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PowerTree {
    private static Map<Integer, Integer> p = new HashMap<>();
    private static List<List<Integer>> lvl = new ArrayList<>();

    static {
        p.put(1, 0);

        ArrayList<Integer> temp = new ArrayList<>();
        temp.add(1);
        lvl.add(temp);
    }

    private static List<Integer> path(int n) {
        if (n == 0) return new ArrayList<>();
        while (!p.containsKey(n)) {
            List<Integer> q = new ArrayList<>();
            for (Integer x : lvl.get(0)) {
                for (Integer y : path(x)) {
                    if (p.containsKey(x + y)) break;
                    p.put(x + y, x);
                    q.add(x + y);
                }
            }
            lvl.get(0).clear();
            lvl.get(0).addAll(q);
        }
        List<Integer> temp = path(p.get(n));
        temp.add(n);
        return temp;
    }

    private static BigDecimal treePow(double x, int n) {
        Map<Integer, BigDecimal> r = new HashMap<>();
        r.put(0, BigDecimal.ONE);
        r.put(1, BigDecimal.valueOf(x));

        int p = 0;
        for (Integer i : path(n)) {
            r.put(i, r.get(i - p).multiply(r.get(p)));
            p = i;
        }
        return r.get(n);
    }

    private static void showPow(double x, int n, boolean isIntegral) {
        System.out.printf("%d: %s\n", n, path(n));
        String f = isIntegral ? "%.0f" : "%f";
        System.out.printf(f, x);
        System.out.printf(" ^ %d = ", n);
        System.out.printf(f, treePow(x, n));
        System.out.println("\n");
    }

    public static void main(String[] args) {
        for (int n = 0; n <= 17; ++n) {
            showPow(2.0, n, true);
        }
        showPow(1.1, 81, false);
        showPow(3.0, 191, true);
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

# remember the tree generation state and expand on demand
def path(n, p = {1:0}, lvl=[[1]]):
	if not n: return []
	while n not in p:
		q = []
		for x,y in ((x, x+y) for x in lvl[0] for y in path(x) if not x+y in p):
			p[y] = x
			q.append(y)
		lvl[0] = q

	return path(p[n]) + [n]

def tree_pow(x, n):
    r, p = {0:1, 1:x}, 0
    for i in path(n):
        r[i] = r[i-p] * r[p]
        p = i
    return r[n]

def show_pow(x, n):
    fmt = "%d: %s\n" + ["%g^%d = %f", "%d^%d = %d"][x==int(x)] + "\n"
    print(fmt % (n, repr(path(n)), x, n, tree_pow(x, n)))

for x in range(18): show_pow(2, x)
show_pow(3, 191)
show_pow(1.1, 81)

```

