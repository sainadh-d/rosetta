# Sorting algorithms/Bogosort

## Task Link
[Rosetta Code - Sorting algorithms/Bogosort](https://rosettacode.org/wiki/Sorting_algorithms/Bogosort)

## Java Code
### java_code_1.txt
```java
public class BogoSort 
{
	public static void main(String[] args)
	{
		//Enter array to be sorted here
		int[] arr={4,5,6,0,7,8,9,1,2,3};
		
		BogoSort now=new BogoSort();
		System.out.print("Unsorted: ");
		now.display1D(arr);
		
		now.bogo(arr);
		
		System.out.print("Sorted: ");
		now.display1D(arr);
	}
	void bogo(int[] arr)
	{
		//Keep a track of the number of shuffles
		int shuffle=1;
		for(;!isSorted(arr);shuffle++)
			shuffle(arr);
		//Boast
		System.out.println("This took "+shuffle+" shuffles.");
	}
	void shuffle(int[] arr)
	{
		//Standard Fisher-Yates shuffle algorithm
		int i=arr.length-1;
		while(i>0)
			swap(arr,i--,(int)(Math.random()*i));
	}
	void swap(int[] arr,int i,int j)
	{
		int temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
	}
	boolean isSorted(int[] arr)
	{

		for(int i=1;i<arr.length;i++)
			if(arr[i]<arr[i-1])
				return false;
		return true;
	}
	void display1D(int[] arr)
	{
		for(int i=0;i<arr.length;i++)
			System.out.print(arr[i]+" ");
		System.out.println();
	}

}

```

### java_code_2.txt
```java
import java.util.Collections;
import java.util.List;
import java.util.Iterator;

public class Bogosort {
    private static <T extends Comparable<? super T>> boolean isSorted(List<T> list) {
        if (list.isEmpty())
            return true;
        Iterator<T> it = list.iterator();
        T last = it.next();
        while (it.hasNext()) {
            T current = it.next();
            if (last.compareTo(current) > 0)
                return false;
            last = current;
        }
        return true;
    }

    public static <T extends Comparable<? super T>> void bogoSort(List<T> list) {
        while (!isSorted(list))
            Collections.shuffle(list);
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

def bogosort(l):
    while not in_order(l):
        random.shuffle(l)
    return l

def in_order(l):
    if not l:
        return True
    last = l[0]
    for x in l[1:]:
        if x < last:
            return False
        last = x
    return True

```

### python_code_2.txt
```python
def in_order(l):
    return all( l[i] <= l[i+1] for i in xrange(0,len(l)-1))

```

### python_code_3.txt
```python
import random
def bogosort(lst):
   random.shuffle(lst)  # must shuffle it first or it's a bug if lst was pre-sorted! :)
   while lst != sorted(lst):
       random.shuffle(lst)
   return lst

```

### python_code_4.txt
```python
import operator
import random
from itertools import dropwhile, imap, islice, izip, repeat, starmap

def shuffled(x):
    x = x[:]
    random.shuffle(x)
    return x

bogosort = lambda l: next(dropwhile(
    lambda l: not all(starmap(operator.le, izip(l, islice(l, 1, None)))),
    imap(shuffled, repeat(l))))

```

