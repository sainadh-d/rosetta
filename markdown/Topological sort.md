# Topological sort

## Task Link
[Rosetta Code - Topological sort](https://rosettacode.org/wiki/Topological_sort)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class TopologicalSort {

    public static void main(String[] args) {
        String s = "std, ieee, des_system_lib, dw01, dw02, dw03, dw04, dw05,"
                + "dw06, dw07, dware, gtech, ramlib, std_cell_lib, synopsys";

        Graph g = new Graph(s, new int[][]{
            {2, 0}, {2, 14}, {2, 13}, {2, 4}, {2, 3}, {2, 12}, {2, 1},
            {3, 1}, {3, 10}, {3, 11},
            {4, 1}, {4, 10},
            {5, 0}, {5, 14}, {5, 10}, {5, 4}, {5, 3}, {5, 1}, {5, 11},
            {6, 1}, {6, 3}, {6, 10}, {6, 11},
            {7, 1}, {7, 10},
            {8, 1}, {8, 10},
            {9, 1}, {9, 10},
            {10, 1},
            {11, 1},
            {12, 0}, {12, 1},
            {13, 1}
        });

        System.out.println("Topologically sorted order: ");
        System.out.println(g.topoSort());
    }
}

class Graph {
    String[] vertices;
    boolean[][] adjacency;
    int numVertices;

    public Graph(String s, int[][] edges) {
        vertices = s.split(",");
        numVertices = vertices.length;
        adjacency = new boolean[numVertices][numVertices];

        for (int[] edge : edges)
            adjacency[edge[0]][edge[1]] = true;
    }

    List<String> topoSort() {
        List<String> result = new ArrayList<>();
        List<Integer> todo = new LinkedList<>();

        for (int i = 0; i < numVertices; i++)
            todo.add(i);

        try {
            outer:
            while (!todo.isEmpty()) {
                for (Integer r : todo) {
                    if (!hasDependency(r, todo)) {
                        todo.remove(r);
                        result.add(vertices[r]);
                         // no need to worry about concurrent modification
                        continue outer;
                    }
                }
                throw new Exception("Graph has cycles");
            }
        } catch (Exception e) {
            System.out.println(e);
            return null;
        }
        return result;
    }

    boolean hasDependency(Integer r, List<Integer> todo) {
        for (Integer c : todo) {
            if (adjacency[r][c])
                return true;
        }
        return false;
    }
}

```

## Python Code
### python_code_1.txt
```python
try:
    from functools import reduce
except:
    pass

data = {
    'des_system_lib':   set('std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee'.split()),
    'dw01':             set('ieee dw01 dware gtech'.split()),
    'dw02':             set('ieee dw02 dware'.split()),
    'dw03':             set('std synopsys dware dw03 dw02 dw01 ieee gtech'.split()),
    'dw04':             set('dw04 ieee dw01 dware gtech'.split()),
    'dw05':             set('dw05 ieee dware'.split()),
    'dw06':             set('dw06 ieee dware'.split()),
    'dw07':             set('ieee dware'.split()),
    'dware':            set('ieee dware'.split()),
    'gtech':            set('ieee gtech'.split()),
    'ramlib':           set('std ieee'.split()),
    'std_cell_lib':     set('ieee std_cell_lib'.split()),
    'synopsys':         set(),
    }

def toposort2(data):
    for k, v in data.items():
        v.discard(k) # Ignore self dependencies
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item,dep in data.items() if not dep)
        if not ordered:
            break
        yield ' '.join(sorted(ordered))
        data = {item: (dep - ordered) for item,dep in data.items()
                if item not in ordered}
    assert not data, "A cyclic dependency exists amongst %r" % data

print ('\n'.join( toposort2(data) ))

```

### python_code_2.txt
```python
from graphlib import TopologicalSorter

#   LIBRARY     mapped_to   LIBRARY DEPENDENCIES
data = {
    'des_system_lib':   set('std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee'.split()),
    'dw01':             set('ieee dw01 dware gtech'.split()),
    'dw02':             set('ieee dw02 dware'.split()),
    'dw03':             set('std synopsys dware dw03 dw02 dw01 ieee gtech'.split()),
    'dw04':             set('dw04 ieee dw01 dware gtech'.split()),
    'dw05':             set('dw05 ieee dware'.split()),
    'dw06':             set('dw06 ieee dware'.split()),
    'dw07':             set('ieee dware'.split()),
    'dware':            set('ieee dware'.split()),
    'gtech':            set('ieee gtech'.split()),
    'ramlib':           set('std ieee'.split()),
    'std_cell_lib':     set('ieee std_cell_lib'.split()),
    'synopsys':         set(),
    }
# Ignore self dependencies
for k, v in data.items():
    v.discard(k)   

ts = TopologicalSorter(data)
print(tuple(ts.static_order()))

```

