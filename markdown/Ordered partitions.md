# Ordered partitions

## Task Link
[Rosetta Code - Ordered partitions](https://rosettacode.org/wiki/Ordered_partitions)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public final class OrderedPartitions {

	public static void main(String[] aArgs) {
		List<Integer> sizes = ( aArgs == null || aArgs.length == 0 ) ? 
			List.of( 2, 0, 2 ) : Arrays.stream(aArgs).map( s -> Integer.valueOf(s) ).toList();
		
		System.out.println("Partitions for " + sizes + ":");
		final int total = sizes.stream().reduce(0, Integer::sum);
		List<Integer> permutation = IntStream.rangeClosed(1, total).boxed().collect(Collectors.toList());
	      
		while ( hasNextPermutation(permutation) ) {
	        List<List<Integer>> partition = new ArrayList<List<Integer>>();
	        int sum = 0;
	        boolean isValid = true; 
	        for ( int size : sizes ) {
            	List<Integer> subList = permutation.subList(sum, sum + size);
                if ( ! isIncreasing(subList) ) {
                    isValid = false;
                    break;
                }
                partition.add(subList);
	            sum += size;
	        }
	        
	        if ( isValid ) {
	        	System.out.println(" ".repeat(4) + partition); 
	        }	        
	    } 
	}
	
	private static boolean hasNextPermutation(List<Integer> aPerm) {
	    final int lastIndex = aPerm.size() - 1;
	    int i = lastIndex;
	    while ( i > 0 && aPerm.get(i - 1) >= aPerm.get(i) ) {
	        i--;
	    }
	    
	    if ( i <= 0 ) {
	        return false;
	    }
	    
	    int j = lastIndex;
	    while ( aPerm.get(j) <= aPerm.get(i - 1) ) {
	        j--;
	    }	    
	    swap(aPerm, i - 1, j);
	    
	    j = lastIndex;
	    while ( i < j ) {
	    	swap(aPerm, i++, j--);
	    }
	    
	    return true;
	}
	
	private static boolean isIncreasing(List<Integer> aList) {
	    return aList.stream().sorted().toList().equals(aList);
	} 
	
	private static void swap(List<Integer> aList, int aOne, int aTwo) {
		final int temp = aList.get(aOne);
	    aList.set(aOne, aList.get(aTwo));
	    aList.set(aTwo, temp);
	}

}

```

## Python Code
### python_code_1.txt
```python
from itertools import combinations

def partitions(*args):
    def p(s, *args):
        if not args: return [[]]
        res = []
        for c in combinations(s, args[0]):
            s0 = [x for x in s if x not in c]
            for r in p(s0, *args[1:]):
                res.append([c] + r)
        return res
    s = range(sum(args))
    return p(s, *args)

print partitions(2, 0, 2)

```

### python_code_2.txt
```python
from itertools import combinations as comb

def partitions(*args):
    def minus(s1, s2): return [x for x in s1 if x not in s2]
    def p(s, *args):
        if not args: return [[]]
        return [[c] + r for c in comb(s, args[0]) for r in p(minus(s, c), *args[1:])]
    return p(range(1, sum(args) + 1), *args)

print partitions(2, 0, 2)

```

### python_code_3.txt
```python
'''Ordered Partitions'''


# partitions :: [Int] -> [[[Int]]]
def partitions(xs):
    '''Ordered partitions of xs.'''
    n = sum(xs)

    def go(s, n, ys):
        return [
            [l] + r
            for (l, rest) in choose(s)(n)(ys[0])
            for r in go(rest, n - ys[0], ys[1:])
        ] if ys else [[]]
    return go(enumFromTo(1)(n), n, xs)


# choose :: [Int] -> Int -> Int -> [([Int], [Int])]
def choose(xs):
    '''(m items chosen from n items, the rest)'''
    def go(xs, n, m):
        f = cons(xs[0])
        choice = choose(xs[1:])(n - 1)
        return [([], xs)] if 0 == m else (
            [(xs, [])] if n == m else (
                [first(f)(x) for x in choice(m - 1)] +
                [second(f)(x) for x in choice(m)]
            )
        )
    return lambda n: lambda m: go(xs, n, m)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Tests of the partitions function'''

    f = partitions
    print(
        fTable(main.__doc__ + ':')(
            lambda x: '\n' + f.__name__ + '(' + repr(x) + ')'
        )(
            lambda ps: '\n\n' + '\n'.join(
                '    ' + repr(p) for p in ps
            )
        )(f)([
            [2, 0, 2],
            [1, 1, 1]
        ])
    )


# DISPLAY -------------------------------------------------

# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# GENERIC -------------------------------------------------

# cons :: a -> [a] -> [a]
def cons(x):
    '''Construction of a list from x as head,
       and xs as tail.
    '''
    return lambda xs: [x] + xs


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# first :: (a -> b) -> ((a, c) -> (b, c))
def first(f):
    '''A simple function lifted to a function over a tuple,
       with f applied only the first of two values.
    '''
    return lambda xy: (f(xy[0]), xy[1])


# second :: (a -> b) -> ((c, a) -> (c, b))
def second(f):
    '''A simple function lifted to a function over a tuple,
       with f applied only the second of two values.
    '''
    return lambda xy: (xy[0], f(xy[1]))


# MAIN ---
if __name__ == '__main__':
    main()

```

