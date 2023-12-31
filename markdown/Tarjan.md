# Tarjan

## Task Link
[Rosetta Code - Tarjan](https://rosettacode.org/wiki/Tarjan)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

public final class TarjanSCC {
	
	public static void main(String[] aArgs) {
		Graph graph = new Graph(8);
		
		graph.addDirectedEdge(0, 1);
		graph.addDirectedEdge(1, 2); graph.addDirectedEdge(1, 7);
		graph.addDirectedEdge(2, 3); graph.addDirectedEdge(2, 6);
		graph.addDirectedEdge(3, 4);
		graph.addDirectedEdge(4, 2); graph.addDirectedEdge(4, 5);
		graph.addDirectedEdge(6, 3); graph.addDirectedEdge(6, 5);
		graph.addDirectedEdge(7, 0); graph.addDirectedEdge(7, 6);
		
		System.out.println("The strongly connected components are: ");
		for ( Set<Integer> component : graph.getSCC() ) {
			System.out.println(component);
		}		
	}
	
}

final class Graph {

	public Graph(int aSize) {		
		adjacencyLists = new ArrayList<Set<Integer>>(aSize);
		for ( int i = 0; i < aSize; i++ ) {
			vertices.add(i);
			adjacencyLists.add( new HashSet<Integer>() );
		}		
	}
	
	public void addDirectedEdge(int aFrom, int aTo) {
		adjacencyLists.get(aFrom).add(aTo);
	}
	
	public List<Set<Integer>> getSCC() {
		for ( int vertex : vertices ) {
			if ( ! numbers.keySet().contains(vertex) ) {
				stronglyConnect(vertex);
			}
		}
		
		return stronglyConnectedComponents;
	}
	
	private void stronglyConnect(int aVertex) {
		numbers.put(aVertex, index);
		lowlinks.put(aVertex, index);
		index += 1;
		stack.push(aVertex);
		
		for ( int adjacent : adjacencyLists.get(aVertex) ) {
			if ( ! numbers.keySet().contains(adjacent) ) {
				stronglyConnect(adjacent);				
				lowlinks.put(aVertex, Math.min(lowlinks.get(aVertex), lowlinks.get(adjacent)));
			} else if ( stack.contains(adjacent) ) {			
				lowlinks.put(aVertex, Math.min(lowlinks.get(aVertex), numbers.get(adjacent)));
			}
		}
		
		if ( lowlinks.get(aVertex) == numbers.get(aVertex) ) {
			Set<Integer> stonglyConnectedComponent = new HashSet<Integer>();
			int top;
			do {
				top = stack.pop();
				stonglyConnectedComponent.add(top);
			} while ( top != aVertex );
						
			stronglyConnectedComponents.add(stonglyConnectedComponent);
		}
	}		
	
	private List<Set<Integer>> adjacencyLists;
	private List<Integer> vertices = new ArrayList<Integer>();	
	private int index = 0;
	private Stack<Integer> stack = new Stack<Integer>();
	private Map<Integer, Integer> numbers = new HashMap<Integer, Integer>();
	private Map<Integer, Integer> lowlinks = new HashMap<Integer, Integer>();
	private List<Set<Integer>> stronglyConnectedComponents = new ArrayList<Set<Integer>>();

}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict

def from_edges(edges):
    '''translate list of edges to list of nodes'''

    class Node:
        def __init__(self):
            # root is one of:
            #   None: not yet visited
            #   -1: already processed
            #   non-negative integer: what Wikipedia pseudo code calls 'lowlink'
            self.root = None
            self.succ = []

    nodes = defaultdict(Node)
    for v,w in edges:
        nodes[v].succ.append(nodes[w])

    for i,v in nodes.items(): # name the nodes for final output
        v.id = i

    return nodes.values()

def trajan(V):
    def strongconnect(v, S):
        v.root = pos = len(S)
        S.append(v)

        for w in v.succ:
            if w.root is None:  # not yet visited
                yield from strongconnect(w, S)

            if w.root >= 0:  # still on stack
                v.root = min(v.root, w.root)

        if v.root == pos:  # v is the root, return everything above
            res, S[pos:] = S[pos:], []
            for w in res:
                w.root = -1
            yield [r.id for r in res]

    for v in V:
        if v.root is None:
            yield from strongconnect(v, [])


tables = [  # table 1
            [(1,2), (3,1), (3,6), (6,7), (7,6), (2,3), (4,2),
             (4,3), (4,5), (5,6), (5,4), (8,5), (8,7), (8,6)],

            # table 2
            [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'Other')]]

for table in (tables):
    for g in trajan(from_edges(table)):
        print(g)
    print()

```

### python_code_2.txt
```python
from collections import defaultdict


class Graph:
    "Directed Graph Tarjan's strongly connected components algorithm"

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        g = defaultdict(list)  # map node vertex to direct connections
        for n1, n2 in connections:
            if n1 != n2:
                g[n1].append(n2)
            else:
                g[n1]
        for _, n2 in connections:
            g[n2]   # For leaf nodes having no edges from themselves
        self.graph = dict(g)
        self.tarjan_algo()

    def _visitor(self, this, low, disc, stack):
        '''
        Recursive function that finds SCC's
        using DFS traversal of vertices.

        Arguments:
            this        --> Vertex to be visited in this call.
            disc{}      --> Discovery order of visited vertices.
            low{}       --> Connected vertex of earliest discovery order
            stack       --> Ancestor node stack during DFS.
        '''

        disc[this] = low[this] = self._order
        self._order += 1
        stack.append(this)

        for neighbr in self.graph[this]:
            if neighbr not in disc:
                # neighbour not visited so do DFS recurrence.
                self._visitor(neighbr, low, disc, stack)
                low[this] = min(low[this], low[neighbr])  # Prior connection?

            elif neighbr in stack:
                # Update low value of this only if neighbr in stack
                low[this] = min(low[this], disc[neighbr])

        if low[this] == disc[this]:
            # Head node found of SCC
            top, new = None, []
            while top != this:
                top = stack.pop()
                new.append(top)
            self.scc.append(new)

    def tarjan_algo(self):
        '''
        Recursive function that finds strongly connected components
        using the Tarjan Algorithm and function _visitor() to visit nodes.
        '''

        self._order = 0         # Visitation order counter
        disc, low = {}, {}
        stack = []

        self.scc = []           # SCC result accumulator
        for vertex in sorted(self.graph):
            if vertex not in disc:
                self._visitor(vertex, low, disc, stack)
        self._disc, self._low = disc, low


if __name__ == '__main__':
    for n, m in [('Tx1', '10 02 21 03 34'.split()),
                 ('Tx2', '01 12 23'.split()),
                 ('Tx3', '01 12 20 13 14 16 35 45'.split()),
                 ('Tx4', '01 03 12 14 20 26 32 45 46 56 57 58 59 64 79 89 98 AA'.split()),
                 ('Tx5', '01 12 23 24 30 42'.split()),
                 ]:
        print(f"\n\nGraph({repr(n)}, {m}):\n")
        g = Graph(n, m)
        print("               : ", '  '.join(str(v) for v in sorted(g._disc)))
        print("    DISC of", g.name + ':', [v for _, v in sorted(g._disc.items())])
        print("     LOW of", g.name + ':', [v for _, v in sorted(g._low.items())])
        scc = repr(g.scc if g.scc else '').replace("'", '').replace(',', '')[1:-1]
        print("\n   SCC's of", g.name + ':', scc)

```

