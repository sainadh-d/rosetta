# Kosaraju

## Task Link
[Rosetta Code - Kosaraju](https://rosettacode.org/wiki/Kosaraju)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.BiConsumer;
import java.util.function.IntConsumer;
import java.util.stream.Collectors;

public class Kosaraju {
    static class Recursive<I> {
        I func;
    }

    private static List<Integer> kosaraju(List<List<Integer>> g) {
        // 1. For each vertex u of the graph, mark u as unvisited. Let l be empty.
        int size = g.size();
        boolean[] vis = new boolean[size];
        int[] l = new int[size];
        AtomicInteger x = new AtomicInteger(size);

        List<List<Integer>> t = new ArrayList<>();
        for (int i = 0; i < size; ++i) {
            t.add(new ArrayList<>());
        }

        Recursive<IntConsumer> visit = new Recursive<>();
        visit.func = (int u) -> {
            if (!vis[u]) {
                vis[u] = true;
                for (Integer v : g.get(u)) {
                    visit.func.accept(v);
                    t.get(v).add(u);
                }
                int xval = x.decrementAndGet();
                l[xval] = u;
            }
        };

        // 2. For each vertex u of the graph do visit(u)
        for (int i = 0; i < size; ++i) {
            visit.func.accept(i);
        }
        int[] c = new int[size];

        Recursive<BiConsumer<Integer, Integer>> assign = new Recursive<>();
        assign.func = (Integer u, Integer root) -> {
            if (vis[u]) {  // repurpose vis to mean 'unassigned'
                vis[u] = false;
                c[u] = root;
                for (Integer v : t.get(u)) {
                    assign.func.accept(v, root);
                }
            }
        };

        // 3: For each element u of l in order, do assign(u, u)
        for (int u : l) {
            assign.func.accept(u, u);
        }

        return Arrays.stream(c).boxed().collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<List<Integer>> g = new ArrayList<>();
        for (int i = 0; i < 8; ++i) {
            g.add(new ArrayList<>());
        }
        g.get(0).add(1);
        g.get(1).add(2);
        g.get(2).add(0);
        g.get(3).add(1);
        g.get(3).add(2);
        g.get(3).add(4);
        g.get(4).add(3);
        g.get(4).add(5);
        g.get(5).add(2);
        g.get(5).add(6);
        g.get(6).add(5);
        g.get(7).add(4);
        g.get(7).add(6);
        g.get(7).add(7);

        List<Integer> output = kosaraju(g);
        System.out.println(output);
    }
}

```

## Python Code
### python_code_1.txt
```python
def kosaraju(g):
    class nonlocal: pass

    # 1. For each vertex u of the graph, mark u as unvisited. Let l be empty.
    size = len(g)

    vis = [False]*size # vertexes that have been visited
    l = [0]*size
    nonlocal.x = size
    t = [[]]*size   # transpose graph

    def visit(u):
        if not vis[u]:
            vis[u] = True
            for v in g[u]:
                visit(v)
                t[v] = t[v] + [u]
            nonlocal.x = nonlocal.x - 1
            l[nonlocal.x] = u

    # 2. For each vertex u of the graph do visit(u)
    for u in range(len(g)):
        visit(u)
    c = [0]*size

    def assign(u, root):
        if vis[u]:
            vis[u] = False
            c[u] = root
            for v in t[u]:
                assign(v, root)

    # 3: For each element u of l in order, do assign(u, u)
    for u in l:
        assign(u, u)

    return c

g = [[1], [2], [0], [1,2,4], [3,5], [2,6], [5], [4,6,7]]
print kosaraju(g)

```

