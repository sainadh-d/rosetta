# Sorting algorithms/Selection sort

## Task Link
[Rosetta Code - Sorting algorithms/Selection sort](https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort)

## Java Code
### java_code_1.txt
```java
public static void sort(int[] nums){
	for(int currentPlace = 0;currentPlace<nums.length-1;currentPlace++){
		int smallest = Integer.MAX_VALUE;
		int smallestAt = currentPlace+1;
		for(int check = currentPlace; check<nums.length;check++){
			if(nums[check]<smallest){
				smallestAt = check;
				smallest = nums[check];
			}
		}
		int temp = nums[currentPlace];
		nums[currentPlace] = nums[smallestAt];
		nums[smallestAt] = temp;
	}
}

```

## Python Code
### python_code_1.txt
```python
def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

```

