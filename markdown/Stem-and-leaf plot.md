# Stem-and-leaf plot

## Task Link
[Rosetta Code - Stem-and-leaf plot](https://rosettacode.org/wiki/Stem-and-leaf_plot)

## Java Code
### java_code_1.txt
```java
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class StemAndLeaf {
	private static int[] data = { 12, 127, 28, 42, 39, 113, 42, 18, 44, 118,
			44, 37, 113, 124, 37, 48, 127, 36, 29, 31, 125, 139, 131, 115, 105,
			132, 104, 123, 35, 113, 122, 42, 117, 119, 58, 109, 23, 105, 63,
			27, 44, 105, 99, 41, 128, 121, 116, 125, 32, 61, 37, 127, 29, 113,
			121, 58, 114, 126, 53, 114, 96, 25, 109, 7, 31, 141, 46, 13, 27,
			43, 117, 116, 27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118,
			117, 38, 27, 106, 33, 117, 116, 111, 40, 119, 47, 105, 57, 122,
			109, 124, 115, 43, 120, 43, 27, 27, 18, 28, 48, 125, 107, 114, 34,
			133, 45, 120, 30, 127, 31, 116, 146 };
	
	public static Map<Integer, List<Integer>> createPlot(int... data){
		Map<Integer, List<Integer>> plot = new TreeMap<Integer, List<Integer>>();
		int highestStem = -1; //for filling in stems with no leaves
		for(int datum:data){
			int leaf = datum % 10;
			int stem = datum / 10; //integer division
			if(stem > highestStem){
				highestStem = stem;
			}
			if(plot.containsKey(stem)){
				plot.get(stem).add(leaf);
			}else{
				LinkedList<Integer> list = new LinkedList<Integer>();
				list.add(leaf);
				plot.put(stem, list);
			}
		}
		if(plot.keySet().size() < highestStem + 1 /*highest stem value and 0*/ ){
			for(int i = 0; i <= highestStem; i++){
				if(!plot.containsKey(i)){
					LinkedList<Integer> list = new LinkedList<Integer>();
					plot.put(i, list);
				}
			}
		}
		return plot;
	}
	
	public static void printPlot(Map<Integer, List<Integer>> plot){
		for(Map.Entry<Integer, List<Integer>> line : plot.entrySet()){
			Collections.sort(line.getValue());
			System.out.println(line.getKey() + " | " + line.getValue());
		}
	}
	
	public static void main(String[] args){
		Map<Integer, List<Integer>> plot = createPlot(data);
		printPlot(plot);
	}
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public interface StemAndLeaf {
  public static final int[] data = {12, 127, 28, 42, 39, 113, 42, 18, 44, 118,
    44, 37, 113, 124, 37, 48, 127, 36, 29, 31, 125, 139, 131, 115, 105,
    132, 104, 123, 35, 113, 122, 42, 117, 119, 58, 109, 23, 105, 63,
    27, 44, 105, 99, 41, 128, 121, 116, 125, 32, 61, 37, 127, 29, 113,
    121, 58, 114, 126, 53, 114, 96, 25, 109, 7, 31, 141, 46, 13, 27,
    43, 117, 116, 27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118,
    117, 38, 27, 106, 33, 117, 116, 111, 40, 119, 47, 105, 57, 122,
    109, 124, 115, 43, 120, 43, 27, 27, 18, 28, 48, 125, 107, 114, 34,
    133, 45, 120, 30, 127, 31, 116, 146};

  public static Map<Integer, List<Integer>> createPlot(int... data) {
    Map<Integer, List<Integer>> plot = Arrays.stream(data)
      .parallel()
      .boxed()
      .collect(
        Collectors.groupingBy(
          datum -> datum / 10, // stem, integer division
          Collectors.mapping(
            datum -> datum % 10, // leaf
            Collectors.toList()
          )
        )
      )
    ;
    int highestStem = Arrays.stream(data)
      .parallel()
      .map(datum -> datum / 10)
      .max()
      .orElse(-1) //for filling in stems with no leaves
    ;
    Optional.of(plot)
      .map(Map::keySet)
      .map(Collection::size)
      .filter(size -> size < highestStem + 1 /*highest stem value and 0*/)
      .ifPresent(p ->
        IntStream.rangeClosed(
          0,
          highestStem
        )
          .parallel()
          .forEach(i ->
            plot.computeIfAbsent(i, $ -> new LinkedList<>())
          )
      )
    ;
    return plot;
  }

  public static void printPlot(Map<Integer, List<Integer>> plot) {
    plot.entrySet()
      .stream()
      .parallel()
      .peek(line -> Optional.of(line)
        .map(Map.Entry::getValue)
        .ifPresent(Collections::sort)
      )
      .map(line ->
        String.join(" ",
          String.valueOf(line.getKey()),
          "|",
          String.valueOf(line.getValue())
        )
      )
      .forEachOrdered(System.out::println)
    ;
  }

  public static void main(String... arguments) {
    Optional.of(data)
      .map(StemAndLeaf::createPlot)
      .ifPresent(StemAndLeaf::printPlot)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
from collections import namedtuple
from pprint import pprint as pp
from math import floor

Stem = namedtuple('Stem', 'data, leafdigits')

data0 = Stem((12, 127, 28, 42, 39, 113, 42, 18, 44, 118, 44, 37, 113, 124, 37,
              48, 127, 36, 29, 31, 125, 139, 131, 115, 105, 132, 104, 123, 35,
              113, 122, 42, 117, 119, 58, 109, 23, 105, 63, 27, 44, 105, 99,
              41, 128, 121, 116, 125, 32, 61, 37, 127, 29, 113, 121, 58, 114,
              126, 53, 114, 96, 25, 109, 7, 31, 141, 46, 13, 27, 43, 117, 116,
              27, 7, 68, 40, 31, 115, 124, 42, 128, 52, 71, 118, 117, 38, 27,
              106, 33, 117, 116, 111, 40, 119, 47, 105, 57, 122, 109, 124, 115,
              43, 120, 43, 27, 27, 18, 28, 48, 125, 107, 114, 34, 133, 45, 120,
              30, 127, 31, 116, 146),
             1.0)

def stemplot(stem):
    d = []
    interval = int(10**int(stem.leafdigits))
    for data in sorted(stem.data):
        data = int(floor(data))
        stm, lf = divmod(data,interval)
        d.append( (int(stm), int(lf)) )
    stems, leafs = list(zip(*d))
    stemwidth = max(len(str(x)) for x in stems)
    leafwidth = max(len(str(x)) for x in leafs)
    laststem, out = min(stems) - 1, []
    for s,l in d:
        while laststem < s:
            laststem += 1
            out.append('\n%*i |' % ( stemwidth, laststem))
        out.append(' %0*i' % (leafwidth, l))
    out.append('\n\nKey:\n Stem multiplier: %i\n X | Y  =>  %i*X+Y\n'
               % (interval, interval))
    return ''.join(out)

if __name__ == '__main__':
    print( stemplot(data0) )

```

### python_code_2.txt
```python
from collections import OrderedDict, Counter

x= [12, 127, 28, 42, 39, 113, 42, 18, 44, 118, 44, 37, 113, 124, 37, 48,
    127, 36, 29, 31, 125, 139, 131, 115, 105, 132, 104, 123, 35, 113,
    122, 42, 117, 119, 58, 109, 23, 105, 63, 27, 44, 105, 99, 41, 128,
    121, 116, 125, 32, 61, 37, 127, 29, 113, 121, 58, 114, 126, 53, 114,
    96, 25, 109, 7, 31, 141, 46, 13, 27, 43, 117, 116, 27, 7, 68, 40, 31,
    115, 124, 42, 128, 52, 71, 118, 117, 38, 27, 106, 33, 117, 116, 111,
    40, 119, 47, 105, 57, 122, 109, 124, 115, 43, 120, 43, 27, 27, 18,
    28, 48, 125, 107, 114, 34, 133, 45, 120, 30, 127, 31, 116, 146]

def stemleaf(x):
    d = OrderedDict((((str(v)[:-1],' ')[v<10], Counter()) for v in sorted(x)))
    for s in ((str(v),' '+str(v))[v<10] for v in x) : d[s[:-1]][s[-1]]+=1
    m=max(len(s) for s in d)
    for k in d:
        print('%s%s | %s'%(' '*(m-len(k)),k,' '.join(sorted(d[k].elements()))))

stemleaf(x)

```

### python_code_3.txt
```python
from itertools import (groupby)
from functools import (reduce)


# stemLeaf :: (String -> Int) -> (String -> String) -> String -> String
def stemLeaf(f, g, s):
    return '\n'.join(map(
        lambda x: str(x[0]).rjust(2) + ' | ' +
        reduce(lambda a, tpl: a + tpl[1] + ' ', x[1], ''),
        (groupby(sorted(
            map(lambda x: (f(x), g(x)), s.split())
        ),
            lambda x: x[0]
        ))
    ))


# main :: IO()
def main():
    def stem(s):
        return (lambda x=s[:-1]: int(x) if 0 < len(x) else 0)()

    def leaf(s):
        return s[-1]

    s = ('12 127 28 42 39 113 42 18 44 118 44 37 113 124 37 48 127 36 29 31'
         ' 125 139 131 115 105 132 104 123 35 113 122 42 117 119 58 109 23'
         ' 105 63 27 44 105 99 41 128 121 116 125 32 61 37 127 29 113 121 58'
         ' 114 126 53 114 96 25 109 7 31 141 46 13 27 43 117 116 27 7 68 40'
         ' 31 115 124 42 128 52 71 118 117 38 27 106 33 117 116 111 40 119 47'
         ' 105 57 122 109 124 115 43 120 43 27 27 18 28 48 125 107 114 34 133'
         ' 45 120 30 127 31 116 146')

    print (stemLeaf(stem, leaf, s))


main()

```

