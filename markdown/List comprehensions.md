# List comprehensions

## Task Link
[Rosetta Code - List comprehensions](https://rosettacode.org/wiki/List_comprehensions)

## Java Code
### java_code_1.txt
```java
// Boilerplate
import java.util.Arrays;
import java.util.List;
import static java.util.function.Function.identity;
import static java.util.stream.Collectors.toList;
import static java.util.stream.IntStream.range;
public interface PythagComp{
    static void main(String... args){
        System.out.println(run(20));
    }

    static List<List<Integer>> run(int n){
        return
            // Here comes the list comprehension bit
            // input stream - bit clunky
            range(1, n).mapToObj(
                x -> range(x, n).mapToObj(
                    y -> range(y, n).mapToObj(
                        z -> new Integer[]{x, y, z}
                    )
                )
            )
                .flatMap(identity())
                .flatMap(identity())
                // predicate
                .filter(a -> a[0]*a[0] + a[1]*a[1] == a[2]*a[2])
                // output expression
                .map(Arrays::asList)
                // the result is a list
                .collect(toList())
        ;
    }
}

```

## Python Code
### python_code_1.txt
```python
[(x,y,z) for x in xrange(1,n+1) for y in xrange(x,n+1) for z in xrange(y,n+1) if x**2 + y**2 == z**2]

```

### python_code_2.txt
```python
((x,y,z) for x in xrange(1,n+1) for y in xrange(x,n+1) for z in xrange(y,n+1) if x**2 + y**2 == z**2)

```

### python_code_3.txt
```python
[(x, y, z) for (x, y, z) in itertools.product(xrange(1,n+1),repeat=3) if x**2 + y**2 == z**2 and x <= y <= z]

```

### python_code_4.txt
```python
((x, y, z) for (x, y, z) in itertools.product(xrange(1,n+1),repeat=3) if x**2 + y**2 == z**2 and x <= y <= z)

```

### python_code_5.txt
```python
def triplets(n):
    for x in xrange(1, n + 1):
        for y in xrange(x, n + 1):
            for z in xrange(y, n + 1):
                yield x, y, z

```

### python_code_6.txt
```python
[(x, y, z) for (x, y, z) in triplets(n) if x**2 + y**2 == z**2]

```

### python_code_7.txt
```python
((x, y, z) for (x, y, z) in triplets(n) if x**2 + y**2 == z**2)

```

### python_code_8.txt
```python
from functools import (reduce)
from operator import (add)


# pts :: Int -> [(Int, Int, Int)]
def pts(n):
    m = 1 + n
    return [(x, y, z) for x in xrange(1, m)
            for y in xrange(x, m)
            for z in xrange(y, m) if x**2 + y**2 == z**2]


# pts2 :: Int -> [(Int, Int, Int)]
def pts2(n):
    m = 1 + n
    return bindList(
        xrange(1, m)
    )(lambda x: bindList(
        xrange(x, m)
    )(lambda y: bindList(
        xrange(y, m)
    )(lambda z: [(x, y, z)] if x**2 + y**2 == z**2 else [])))


# pts3 :: Int -> [(Int, Int, Int)]
def pts3(n):
    m = 1 + n
    return concatMap(
        lambda x: concatMap(
            lambda y: concatMap(
                lambda z: [(x, y, z)] if x**2 + y**2 == z**2 else []
            )(xrange(y, m))
        )(xrange(x, m))
    )(xrange(1, m))


# GENERIC ---------------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    return lambda xs: (
        reduce(add, map(f, xs), [])
    )


# (flip concatMap)
# bindList :: [a] -> (a -> [b])  -> [b]
def bindList(xs):
    return lambda f: (
        reduce(add, map(f, xs), [])
    )


def main():
    for f in [pts, pts2, pts3]:
        print (f(20))


main()

```

