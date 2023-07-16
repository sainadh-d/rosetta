# Sorting algorithms/Pancake sort

## Task Link
[Rosetta Code - Sorting algorithms/Pancake sort](https://rosettacode.org/wiki/Sorting_algorithms/Pancake_sort)

## Java Code
### java_code_1.txt
```java
public class PancakeSort
{
   int[] heap;

   public String toString() {
      String info = "";
      for (int x: heap)
         info += x + " ";
      return info;
   }
    
   public void flip(int n) {
      for (int i = 0; i < (n+1) / 2; ++i) {
         int tmp = heap[i];
         heap[i] = heap[n-i];
         heap[n-i] = tmp;
      }      
      System.out.println("flip(0.." + n + "): " + toString());
   }
   
   public int[] minmax(int n) {
      int xm, xM;
      xm = xM = heap[0];
      int posm = 0, posM = 0;
      
      for (int i = 1; i < n; ++i) {
         if (heap[i] < xm) {
            xm = heap[i];
            posm = i;
         }
         else if (heap[i] > xM) {
            xM = heap[i];
            posM = i;
         }
      }
      return new int[] {posm, posM};
   }
   
   public void sort(int n, int dir) {
      if (n == 0) return;
         
      int[] mM = minmax(n);
      int bestXPos = mM[dir];
      int altXPos = mM[1-dir];
      boolean flipped = false;
      
      if (bestXPos == n-1) {
         --n;
      }
      else if (bestXPos == 0) {
         flip(n-1);
         --n;
      }
      else if (altXPos == n-1) {
         dir = 1-dir;
         --n;
         flipped = true;
      }
      else {
         flip(bestXPos);
      }
      sort(n, dir);

      if (flipped) {
         flip(n);
      }
   }
   
   PancakeSort(int[] numbers) {
      heap = numbers;
      sort(numbers.length, 1);
   } 
 
   public static void main(String[] args) {
      int[] numbers = new int[args.length];
      for (int i = 0; i < args.length; ++i)
         numbers[i] = Integer.valueOf(args[i]);

      PancakeSort pancakes = new PancakeSort(numbers);
      System.out.println(pancakes);
   }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.IntStream;

public final class PancakeSort {

	public static void main(String[] aArgs) {
		List<Integer> numbers = Arrays.asList( 1, 5, 4, 2, 3, 2, 8, 6, 7 );
		System.out.println("Initial list: " + numbers);		
		pancakeSort(numbers);		
	}
	
	private static void pancakeSort(List<Integer> aList) {
		for ( int i = aList.size() - 1; i >= 0; i-- ) {	    
	    	int index = IntStream.rangeClosed(0, i).boxed().max(Comparator.comparing(aList::get)).get();
		    
		    if ( index != i ) {
		    	flip(aList, index);
		    	flip(aList, i);
		    }		
		}
	}
	
	private static void flip(List<Integer> aList, int aIndex) {
		if ( aIndex > 0 ) {
			Collections.reverse(aList.subList(0, aIndex + 1));		
			System.out.println("flip 0.." + aIndex + " --> " + aList);
		}
	}

}

```

## Python Code
### python_code_1.txt
```python
tutor = False

def pancakesort(data):
    if len(data) <= 1:
        return data
    if tutor: print()
    for size in range(len(data), 1, -1):
        maxindex = max(range(size), key=data.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                if tutor: print('With: %r doflip  %i'
                                % ( ' '.join(str(x) for x in data), maxindex+1 ))
                data[:maxindex+1] = reversed(data[:maxindex+1])
            # Flip it into its final position
            if tutor: print('With: %r  doflip %i'
                                % ( ' '.join(str(x) for x in data), size ))
            data[:size] = reversed(data[:size])
    if tutor: print()

```

### python_code_2.txt
```python
if __name__ == '__main__':
    import random

    tutor = True
    data = list('123456789')
    while data == sorted(data):
        random.shuffle(data)
    print('Original List: %r' % ' '.join(data))
    pancakesort(data)
    print('Pancake Sorted List: %r' % ' '.join(data))

```

