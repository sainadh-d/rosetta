# Largest int from concatenated ints

## Task Link
[Rosetta Code - Largest int from concatenated ints](https://rosettacode.org/wiki/Largest_int_from_concatenated_ints)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class IntConcat {
 
    private static Comparator<Integer> sorter = new Comparator<Integer>(){
        @Override
        public int compare(Integer o1, Integer o2){
            String o1s = o1.toString();
            String o2s = o2.toString();
            
            if(o1s.length() == o2s.length()){
                return o2s.compareTo(o1s);
            }

            int mlen = Math.max(o1s.length(), o2s.length());
            while(o1s.length() < mlen * 2) o1s += o1s;
            while(o2s.length() < mlen * 2) o2s += o2s;
            
            return o2s.compareTo(o1s);
        }
    };
    
    public static String join(List<?> things){
        String output = "";
        for(Object obj:things){
            output += obj;
        }
        return output;
    }
    
    public static void main(String[] args){
        List<Integer> ints1 = new ArrayList<Integer>(Arrays.asList(1, 34, 3, 98, 9, 76, 45, 4));
        
        Collections.sort(ints1, sorter);
        System.out.println(join(ints1));
        
        List<Integer> ints2 = new ArrayList<Integer>(Arrays.asList(54, 546, 548, 60));
        
        Collections.sort(ints2, sorter);
        System.out.println(join(ints2));
    }
}

```

### java_code_2.txt
```java
import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public interface IntConcat {
  public static Comparator<Integer> SORTER = (o1, o2) -> {
    String o1s = o1.toString();
    String o2s = o2.toString();
    
    if (o1s.length() == o2s.length()) {
      return o2s.compareTo(o1s);
    }
    
    int mlen = Math.max(o1s.length(), o2s.length());
    while (o1s.length() < mlen * 2) {
      o1s += o1s;
    }
    while (o2s.length() < mlen * 2) {
      o2s += o2s;
    }
    
    return o2s.compareTo(o1s);
  };

  public static void main(String[] args) {
    Stream<Integer> ints1 = Stream.of(
      1, 34, 3, 98, 9, 76, 45, 4
    );

    System.out.println(ints1
      .parallel()
      .sorted(SORTER)
      .map(String::valueOf)
      .collect(Collectors.joining())
    );

    Stream<Integer> ints2 = Stream.of(
      54, 546, 548, 60
    );

    System.out.println(ints2
      .parallel()
      .sorted(SORTER)
      .map(String::valueOf)
      .collect(Collectors.joining())
    );
  }
}

```

## Python Code
### python_code_1.txt
```python
try:
    cmp     # Python 2 OK or NameError in Python 3
    def maxnum(x):
        return ''.join(sorted((str(n) for n in x),
                              cmp=lambda x,y:cmp(y+x, x+y)))
except NameError:
    # Python 3
    from functools import cmp_to_key
    def cmp(x, y):
        return -1 if x<y else ( 0 if x==y else 1)
    def maxnum(x):
        return ''.join(sorted((str(n) for n in x),
                              key=cmp_to_key(lambda x,y:cmp(y+x, x+y))))

for numbers in [(1, 34, 3, 98, 9, 76, 45, 4), (54, 546, 548, 60)]:
    print('Numbers: %r\n  Largest integer: %15s' % (numbers, maxnum(numbers)))

```

### python_code_2.txt
```python
def maxnum(x):
    maxlen = len(str(max(x)))
    return ''.join(sorted((str(v) for v in x), reverse=True,
                          key=lambda i: i*(maxlen * 2 // len(i))))

for numbers in [(212, 21221), (1, 34, 3, 98, 9, 76, 45, 4), (54, 546, 548, 60)]:
    print('Numbers: %r\n  Largest integer: %15s' % (numbers, maxnum(numbers)))

```

### python_code_3.txt
```python
from fractions import Fraction
from math import log10

def maxnum(x):
    return ''.join(str(n) for n in sorted(x, reverse=True,
                          key=lambda i: Fraction(i, 10**(int(log10(i))+1)-1)))

for numbers in [(1, 34, 3, 98, 9, 76, 45, 4), (54, 546, 548, 60)]:
    print('Numbers: %r\n  Largest integer: %15s' % (numbers, maxnum(numbers)))

```

### python_code_4.txt
```python
from itertools import permutations
def maxnum(x):
    return max(int(''.join(n) for n in permutations(str(i) for i in x)))

for numbers in [(1, 34, 3, 98, 9, 76, 45, 4), (54, 546, 548, 60)]:
    print('Numbers: %r\n  Largest integer: %15s' % (numbers, maxnum(numbers)))

```

