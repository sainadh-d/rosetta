# Sorting algorithms/Strand sort

## Task Link
[Rosetta Code - Sorting algorithms/Strand sort](https://rosettacode.org/wiki/Sorting_algorithms/Strand_sort)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.LinkedList;

public class Strand{
	// note: the input list is destroyed
	public static <E extends Comparable<? super E>> 
	LinkedList<E> strandSort(LinkedList<E> list){
		if(list.size() <= 1) return list;

		LinkedList<E> result = new LinkedList<E>();
		while(list.size() > 0){
			LinkedList<E> sorted = new LinkedList<E>();
			sorted.add(list.removeFirst()); //same as remove() or remove(0)
			for(Iterator<E> it = list.iterator(); it.hasNext(); ){
				E elem = it.next();
				if(sorted.peekLast().compareTo(elem) <= 0){
					sorted.addLast(elem); //same as add(elem) or add(0, elem)
					it.remove();
				}
			}
			result = merge(sorted, result);
		}
		return result;
	}

	private static <E extends Comparable<? super E>>
	LinkedList<E> merge(LinkedList<E> left, LinkedList<E> right){
		LinkedList<E> result = new LinkedList<E>();
		while(!left.isEmpty() && !right.isEmpty()){
			//change the direction of this comparison to change the direction of the sort
			if(left.peek().compareTo(right.peek()) <= 0)
				result.add(left.remove());
			else
				result.add(right.remove());
		}
		result.addAll(left);
		result.addAll(right);
		return result;
	}
	
	public static void main(String[] args){
		System.out.println(strandSort(new LinkedList<Integer>(Arrays.asList(3,1,2,4,5))));
		System.out.println(strandSort(new LinkedList<Integer>(Arrays.asList(3,3,1,2,4,5))));
		System.out.println(strandSort(new LinkedList<Integer>(Arrays.asList(3,3,1,2,4,3,5,6))));
	}
}

```

## Python Code
### python_code_1.txt
```python
def merge_list(a, b):
	out = []
	while len(a) and len(b):
		if a[0] < b[0]:
			out.append(a.pop(0))
		else:
			out.append(b.pop(0))
	out += a
	out += b
	return out

def strand(a):
	i, s = 0, [a.pop(0)]
	while i < len(a):
		if a[i] > s[-1]:
			s.append(a.pop(i))
		else:
			i += 1
	return s

def strand_sort(a):
	out = strand(a)
	while len(a):
		out = merge_list(out, strand(a))
	return out

print strand_sort([1, 6, 3, 2, 1, 7, 5, 3])

```

