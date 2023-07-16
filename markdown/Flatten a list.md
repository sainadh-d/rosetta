# Flatten a list

## Task Link
[Rosetta Code - Flatten a list](https://rosettacode.org/wiki/Flatten_a_list)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;
import java.util.List;


public final class FlattenUtil {

	public static List<Object> flatten(List<?> list) {
		List<Object> retVal = new LinkedList<Object>();
		flatten(list, retVal);
		return retVal;
	}

	public static void flatten(List<?> fromTreeList, List<Object> toFlatList) {
		for (Object item : fromTreeList) {
			if (item instanceof List<?>) {
				flatten((List<?>) item, toFlatList);
			} else {
				toFlatList.add(item);
			}
		}
	}
}

```

### java_code_2.txt
```java
import static java.util.Arrays.asList;
import java.util.List;

public final class FlattenTestMain {

	public static void main(String[] args) {
		List<Object> treeList = a(a(1), 2, a(a(3, 4), 5), a(a(a())), a(a(a(6))), 7, 8, a());
		List<Object> flatList = FlattenUtil.flatten(treeList);
		System.out.println(treeList);
		System.out.println("flatten: " + flatList);
	}
	
	private static List<Object> a(Object... a) {
		return asList(a);
	}
}

```

### java_code_3.txt
```java
import java.util.List;
import java.util.stream.Stream;
import java.util.stream.Collectors;

public final class FlattenUtil {

	public static Stream<Object> flattenToStream(List<?> list) {
		return list.stream().flatMap(item ->
			item instanceof List<?> ?
			flattenToStream((List<?>)item) :
			Stream.of(item));
	}

	public static List<Object> flatten(List<?> list) {
		return flattenToStream(list).collect(Collectors.toList());
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x)
		     for x in lst), [] )

>>> lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
>>> flatten(lst)
[1, 2, 3, 4, 5, 6, 7, 8]

```

### python_code_2.txt
```python
>>> def flatten(itr):
>>>    for x in itr:
>>>        try:
>>>            yield from flatten(x)
>>>        except:
>>>            yield x

>>> lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]

>>> list(flatten(lst))
[1, 2, 3, 4, 5, 6, 7, 8]

>>> tuple(flatten(lst))
(1, 2, 3, 4, 5, 6, 7, 8)

>>>for i in flatten(lst):
>>>    print(i)
1
2
3
4
5
6
7
8

```

### python_code_3.txt
```python
>>> def flat(lst):
    i=0
    while i<len(lst):
        while True:
            try:
                lst[i:i+1] = lst[i]
            except (TypeError, IndexError):
                break
        i += 1
        
>>> lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
>>> flat(lst)
>>> lst
[1, 2, 3, 4, 5, 6, 7, 8]

```

### python_code_4.txt
```python
>>> def flatten(lst):
     for x in lst:
         if isinstance(x, list):
             for x in flatten(x):
                 yield x
         else:
             yield x
 
 
>>> lst = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
>>> print list(flatten(lst)) 
[1, 2, 3, 4, 5, 6, 7, 8]

```

### python_code_5.txt
```python
'''Flatten a nested list'''

from itertools import (chain)


# ----------------------- FLATTEN ------------------------

# flatten :: NestedList a -> [a]
def flatten(x):
    '''A list of atomic values resulting from fully
       flattening an arbitrarily nested list.
    '''
    return concatMap(flatten)(x) if (
        isinstance(x, list)
    ) else [x]


# ------------------------- TEST -------------------------
def main():
    '''Test: flatten an arbitrarily nested list.
    '''
    print(
        fTable(__doc__ + ':')(showList)(showList)(
            flatten
        )([
            [[[]]],
            [[1, 2, 3]],
            [[1], [[2]], [[[3, 4]]]],
            [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
        ])
    )


# ----------------------- GENERIC ------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# fTable :: String -> (a -> String) ->
#                     (b -> String) ->
#        (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
                 fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + (' -> ') + fxShow(f(x))
            for x in xs
        ])
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(str(x) for x in xs) + ']'


if __name__ == '__main__':
    main()

```

### python_code_6.txt
```python
'''Flatten a list'''

from functools import (reduce)
from itertools import (chain)


def flatten(xs):
    '''A flat list of atomic values derived
       from a nested list.
    '''
    return reduce(
        lambda a, x: a + list(until(every(notList))(
            concatMap(pureList)
        )([x])),
        xs, []
    )


# TEST ----------------------------------------------------
def main():
    '''From nested list to flattened list'''

    print(main.__doc__ + ':\n\n')
    xs = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
    print(
        repr(xs) + ' -> ' + repr(flatten(xs))
    )


# GENERIC -------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list over which a function has been mapped.
       The list monad can be derived by using a function f which
       wraps its output in a list,
       (using an empty list to represent computational failure).
    '''
    return lambda xs: list(
        chain.from_iterable(map(f, xs))
    )


# every :: (a -> Bool) -> [a] -> Bool
def every(p):
    '''True if p(x) holds for every x in xs'''
    def go(p, xs):
        return all(map(p, xs))
    return lambda xs: go(p, xs)


# notList :: a -> Bool
def notList(x):
    '''True if the value x is not a list.'''
    return not isinstance(x, list)


# pureList :: a -> [b]
def pureList(x):
    '''x if x is a list, othewise [x]'''
    return x if isinstance(x, list) else [x]


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.'''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

### python_code_7.txt
```python
def (flatten seq acc)
  if no.seq
       acc
     ~list?.seq
       (cons seq acc)
     :else
       (flatten car.seq (flatten cdr.seq acc))

```

