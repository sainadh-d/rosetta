# Sorting algorithms/Gnome sort

## Task Link
[Rosetta Code - Sorting algorithms/Gnome sort](https://rosettacode.org/wiki/Sorting_algorithms/Gnome_sort)

## Java Code
### java_code_1.txt
```java
public static void gnomeSort(int[] a)
{
  int i=1;
  int j=2;
 
  while(i < a.length) {
    if ( a[i-1] <= a[i] ) {
      i = j; j++;
    } else {
      int tmp = a[i-1];
      a[i-1] = a[i];
      a[i--] = tmp;
      i = (i==0) ? j++ : i;
    }
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> def gnomesort(a):
	i,j,size = 1,2,len(a)
	while i < size:
		if a[i-1] <= a[i]:
			i,j = j, j+1
		else:
			a[i-1],a[i] = a[i],a[i-1]
			i -= 1
			if i == 0:
				i,j = j, j+1
	return a

>>> gnomesort([3,4,2,5,1,6])
[1, 2, 3, 4, 5, 6]
>>>

```

