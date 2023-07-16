# Search a list

## Task Link
[Rosetta Code - Search a list](https://rosettacode.org/wiki/Search_a_list)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.Arrays;

List<String> haystack = Arrays.asList("Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo");

for (String needle : new String[]{"Washington","Bush"}) {
    int index = haystack.indexOf(needle);
    if (index < 0)
        System.out.println(needle + " is not in haystack");
    else
        System.out.println(index + " " + needle);
}

```

### java_code_2.txt
```java
import java.util.Arrays;
 
String[] haystack = { "Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo"};

for (String needle : new String[]{"Washington","Bush"}) {
    int index = Arrays.binarySearch(haystack, needle);
    if (index < 0)
        System.out.println(needle + " is not in haystack");
    else
        System.out.println(index + " " + needle);
}

```

## Python Code
### python_code_1.txt
```python
haystack=["Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo"]

for needle in ("Washington","Bush"):
  try:
    print haystack.index(needle), needle
  except ValueError, value_error:
    print needle,"is not in haystack"

```

### python_code_2.txt
```python
>>> haystack=["Zig","Zag","Wally","Ronald","Bush","Krusty","Charlie","Bush","Bozo"]
>>> haystack.index('Bush')
4
>>> haystack.index('Washington')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    haystack.index('Washington')
ValueError: list.index(x): x not in list
>>>

```

### python_code_3.txt
```python
>>> def hi_index(needle, haystack):
	return len(haystack)-1 - haystack[::-1].index(needle)

>>> # Lets do some checks
>>> for n in haystack:
	hi = hi_index(n, haystack)
	assert haystack[hi] == n, "Hi index is of needle"
	assert n not in haystack[hi+1:], "No higher index exists"
	if haystack.count(n) == 1:
		assert hi == haystack.index(n), "index == hi_index if needle occurs only once"

>>>

```

### python_code_4.txt
```python
def (pos x (seq | (head ... tail)) n)
  default n :to 0
  if seq
    if (head = x)
      n
      (pos x tail n+1)

```

