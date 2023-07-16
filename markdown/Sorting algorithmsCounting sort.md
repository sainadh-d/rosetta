# Sorting algorithms/Counting sort

## Task Link
[Rosetta Code - Sorting algorithms/Counting sort](https://rosettacode.org/wiki/Sorting_algorithms/Counting_sort)

## Java Code
### java_code_1.txt
```java
public static void countingSort(int[] array, int min, int max){
	int[] count= new int[max - min + 1];
	for(int number : array){
		count[number - min]++;
	}
	int z= 0;
	for(int i= min;i <= max;i++){
		while(count[i - min] > 0){
			array[z]= i;
			z++;
			count[i - min]--;
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> from collections import defaultdict
>>> def countingSort(array, mn, mx):
	count = defaultdict(int)
	for i in array:
		count[i] += 1
	result = []
	for j in range(mn,mx+1):
		result += [j]* count[j]
	return result

>>> data = [9, 7, 10, 2, 9, 7, 4, 3, 10, 2, 7, 10, 2, 1, 3, 8, 7, 3, 9, 5, 8, 5, 1, 6, 3, 7, 5, 4, 6, 9, 9, 6, 6, 10, 2, 4, 5, 2, 8, 2, 2, 5, 2, 9, 3, 3, 5, 7, 8, 4]
>>> mini,maxi = 1,10
>>> countingSort(data, mini, maxi) == sorted(data)
True

```

### python_code_2.txt
```python
def countingSort(a, min, max):
    cnt = [0] * (max - min + 1)
    for x in a:
        cnt[x - min] += 1
 
    return [x for x, n in enumerate(cnt, start=min)
              for i in xrange(n)]

```

