# Combinations

## Task Link
[Rosetta Code - Combinations](https://rosettacode.org/wiki/Combinations)

## Java Code
### java_code_1.txt
```java
import java.util.Collections;
import java.util.LinkedList;

public class Comb{

        public static void main(String[] args){
                System.out.println(comb(3,5));
        }

        public static String bitprint(int u){
                String s= "";
                for(int n= 0;u > 0;++n, u>>= 1)
                        if((u & 1) > 0) s+= n + " ";
                return s;
        }

        public static int bitcount(int u){
                int n;
                for(n= 0;u > 0;++n, u&= (u - 1));//Turn the last set bit to a 0
                return n;
        }

        public static LinkedList<String> comb(int c, int n){
                LinkedList<String> s= new LinkedList<String>();
                for(int u= 0;u < 1 << n;u++)
                        if(bitcount(u) == c) s.push(bitprint(u));
                Collections.sort(s);
                return s;
        }
}

```

## Python Code
### python_code_1.txt
```python
>>> from itertools import combinations
>>> list(combinations(range(5),3))
[(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4), (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

```

### python_code_2.txt
```python
def comb(m, lst):
    if m == 0: return [[]]
    return [[x] + suffix for i, x in enumerate(lst)
            for suffix in comb(m - 1, lst[i + 1:])]

```

### python_code_3.txt
```python
>>> comb(3, range(5))
[[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3], [0, 2, 4], [0, 3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

```

### python_code_4.txt
```python
def comb(m, s):
    if m == 0: return [[]]
    if s == []: return []
    return [s[:1] + a for a in comb(m-1, s[1:])] + comb(m, s[1:])

print comb(3, range(5))

```

### python_code_5.txt
```python
def comb(m, s):
    if m == 1: return [[x] for x in s]
    if m == len(s): return [s]
    return [s[:1] + a for a in comb(m-1, s[1:])] + comb(m, s[1:])

```

