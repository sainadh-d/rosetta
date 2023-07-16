# Faces from a mesh

## Task Link
[Rosetta Code - Faces from a mesh](https://rosettacode.org/wiki/Faces_from_a_mesh)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public final class FacesFromMesh {

	public static void main(String[] aArgs) {
		final List<Integer> perimeterFormatQ = Arrays.asList( 8, 1, 3 );
		final List<Integer> perimeterFormatR = Arrays.asList( 1, 3, 8 );
		final List<Integer> perimeterFormatU = Arrays.asList( 18, 8, 14, 10, 12, 17, 19 );
		final List<Integer> perimeterFormatV = Arrays.asList( 8, 14, 10, 12, 17, 19, 18 );
		
		final List<Edge> edgeFormatE = Arrays.asList( new Edge(1, 11), new Edge(7, 11), new Edge(1, 7) );	
		final List<Edge> edgeFormatF =
			Arrays.asList( new Edge(11, 23), new Edge(1, 17), new Edge(17, 23), new Edge(1, 11) );
		final List<Edge> edgeFormatG = Arrays.asList( new Edge(8, 14), new Edge(17, 19),
			new Edge(10, 12), new Edge(10, 14), new Edge(12, 17), new Edge(8, 18), new Edge(18, 19) );
		final List<Edge> edgeFormatH = 
			Arrays.asList( new Edge(1, 3), new Edge(9, 11), new Edge(3, 11), new Edge(1, 11) );		
		
		System.out.println("PerimeterFormat equality checks:");
		boolean sameFace = isSameFace(perimeterFormatQ, perimeterFormatR);
		System.out.println(perimeterFormatQ + " == " + perimeterFormatR + ": " + sameFace);
		sameFace = isSameFace(perimeterFormatU, perimeterFormatV);
		System.out.println(perimeterFormatU + " == " + perimeterFormatV + ": " + sameFace);

		System.out.println(System.lineSeparator() + "EdgeFormat to PerimeterFormat conversions:");
		List<List<Edge>> edgeFormatFaces = List.of( edgeFormatE, edgeFormatF, edgeFormatG, edgeFormatH ); 
		for ( List<Edge> edgeFormatFace : edgeFormatFaces ) {
			List<Integer> perimeterFormatFace = toPerimeterFormatFace(edgeFormatFace);
		    if ( perimeterFormatFace.isEmpty() ) {
		    	System.out.println(edgeFormatFace + " has invalid edge format");
		    } else {
		        System.out.println(edgeFormatFace + " => " + perimeterFormatFace);
		    }
		}
	}
	
	private static boolean isSameFace(List<Integer> aOne, List<Integer> aTwo) {
		if ( aOne.size() != aTwo.size() || aOne.isEmpty() ||
			! new HashSet<Integer>(aOne).equals( new HashSet<Integer>(aTwo) )) {
			return false;
		}

		List<Integer> copyTwo = new ArrayList<Integer>(aTwo);
		for ( int i = 0; i < 2; i++ ) {
			int start = copyTwo.indexOf(aOne.get(0));
			List<Integer> test = new ArrayList<Integer>(copyTwo.subList(start, copyTwo.size()));
			test.addAll(copyTwo.subList(0, start));
			if ( aOne.equals(test) ) {
			    return true;
			}
			Collections.reverse(copyTwo);
		}	
		return false;
	}
	
	private static List<Integer> toPerimeterFormatFace(List<Edge> aEdgeFormatFace) {
		if ( aEdgeFormatFace.isEmpty() ) {
			return Collections.emptyList();
		}		
		
		List<Edge> edges = new ArrayList<Edge>(aEdgeFormatFace);
		List<Integer> result = new ArrayList<Integer>();
		Edge firstEdge = edges.remove(0);
		int nextVertex = firstEdge.first;
		result.add(nextVertex);
		
		while ( ! edges.isEmpty() ) {
			int index = -1;
			for ( Edge edge : edges ) {
				if ( edge.first == nextVertex || edge.second == nextVertex ) {
			        index = edges.indexOf(edge);
			        nextVertex = ( nextVertex == edge.first ) ? edge.second : edge.first;
			        break;
				}
			}			
			if ( index == -1 ) {
				return Collections.emptyList();
			}
			result.add(nextVertex);
			edges.remove(index);
		}
		
		if ( nextVertex != firstEdge.second ) {
		    return Collections.emptyList();
		}		
		return result;
	}
	
	private static class Edge {
		
		public Edge(int aFirst, int aSecond) {
			first = aFirst;
			second = aSecond;
		}
		
		@Override
		public String toString() {
			return "(" + first + ", " + second + ")";
		}
		
		private int first, second;
		
	}

}

```

## Python Code
### python_code_1.txt
```python
def perim_equal(p1, p2):
    # Cheap tests first
    if len(p1) != len(p2) or set(p1) != set(p2):
        return False
    if any(p2 == (p1[n:] + p1[:n]) for n in range(len(p1))):
        return True
    p2 = p2[::-1] # not inplace
    return any(p2 == (p1[n:] + p1[:n]) for n in range(len(p1)))

def edge_to_periphery(e):
    edges = sorted(e)
    p = list(edges.pop(0)) if edges else []
    last = p[-1] if p else None
    while edges:
        for n, (i, j) in enumerate(edges):
            if i == last:
                p.append(j)
                last = j
                edges.pop(n)
                break
            elif j == last:
                p.append(i)
                last = i
                edges.pop(n)
                break
        else:
            #raise ValueError(f'Invalid edge format: {e}')
            return ">>>Error! Invalid edge format<<<"
    return p[:-1]

if __name__ == '__main__':
    print('Perimeter format equality checks:')
    for eq_check in [
            { 'Q': (8, 1, 3),
              'R': (1, 3, 8)},
            { 'U': (18, 8, 14, 10, 12, 17, 19),
              'V': (8, 14, 10, 12, 17, 19, 18)} ]:
        (n1, p1), (n2, p2) = eq_check.items()
        eq = '==' if perim_equal(p1, p2) else '!='
        print(' ', n1, eq, n2)

    print('\nEdge to perimeter format translations:')
    edge_d = {
     'E': {(1, 11), (7, 11), (1, 7)},
     'F': {(11, 23), (1, 17), (17, 23), (1, 11)},
     'G': {(8, 14), (17, 19), (10, 12), (10, 14), (12, 17), (8, 18), (18, 19)},
     'H': {(1, 3), (9, 11), (3, 11), (1, 11)}
            }
    for name, edges in edge_d.items():
        print(f"  {name}: {edges}\n     -> {edge_to_periphery(edges)}")

```

