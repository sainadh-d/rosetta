# Averages/Mode

## Task Link
[Rosetta Code - Averages/Mode](https://rosettacode.org/wiki/Averages/Mode)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Mode {
    public static <T> List<T> mode(List<? extends T> coll) {
        Map<T, Integer> seen = new HashMap<T, Integer>();
        int max = 0;
        List<T> maxElems = new ArrayList<T>();
        for (T value : coll) {
            if (seen.containsKey(value))
                seen.put(value, seen.get(value) + 1);
            else
                seen.put(value, 1);
            if (seen.get(value) > max) {
                max = seen.get(value);
                maxElems.clear();
                maxElems.add(value);
            } else if (seen.get(value) == max) {
                maxElems.add(value);
            }
        }
        return maxElems;
    }

    public static void main(String[] args) {
        System.out.println(mode(Arrays.asList(1, 3, 6, 6, 6, 6, 7, 7, 12, 12, 17))); // prints [6]
        System.out.println(mode(Arrays.asList(1, 1, 2, 4, 4))); // prints [1, 4]
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from collections import defaultdict
>>> def modes(values):
	count = defaultdict(int)
	for v in values:
		count[v] +=1
	best = max(count.values())
	return [k for k,v in count.items() if v == best]

>>> modes([1,3,6,6,6,6,7,7,12,12,17])
[6]
>>> modes((1,1,2,4,4))
[1, 4]

```

### python_code_2.txt
```python
>>> from collections import Counter
>>> def modes(values):
	count = Counter(values)
	best = max(count.values())
	return [k for k,v in count.items() if v == best]

>>> modes([1,3,6,6,6,6,7,7,12,12,17])
[6]
>>> modes((1,1,2,4,4))
[1, 4]

```

### python_code_3.txt
```python
def onemode(values):
    return max(set(values), key=values.count)

```

