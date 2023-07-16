# Sorting algorithms/Shell sort

## Task Link
[Rosetta Code - Sorting algorithms/Shell sort](https://rosettacode.org/wiki/Sorting_algorithms/Shell_sort)

## Java Code
### java_code_1.txt
```java
public static void shell(int[] a) {
	int increment = a.length / 2;
	while (increment > 0) {
		for (int i = increment; i < a.length; i++) {
			int j = i;
			int temp = a[i];
			while (j >= increment && a[j - increment] > temp) {
				a[j] = a[j - increment];
				j = j - increment;
			}
			a[j] = temp;
		}
		if (increment == 2) {
			increment = 1;
		} else {
			increment *= (5.0 / 11);
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq[inc:], inc):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11

```

