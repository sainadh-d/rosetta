# Identity matrix

## Task Link
[Rosetta Code - Identity matrix](https://rosettacode.org/wiki/Identity_matrix)

## Java Code
### java_code_1.txt
```java
public class PrintIdentityMatrix {

    public static void main(String[] args) {
        int n = 5;
        int[][] array = new int[n][n];

        IntStream.range(0, n).forEach(i -> array[i][i] = 1);

        Arrays.stream(array)
                .map((int[] a) -> Arrays.toString(a))
                .forEach(System.out::println);
    }
}

```

## Python Code
### python_code_1.txt
```python
def identity(size):
    matrix = [[0]*size for i in range(size)]
    #matrix = [[0] * size] * size    #Has a flaw. See http://stackoverflow.com/questions/240178/unexpected-feature-in-a-python-list-of-lists

    for i in range(size):
        matrix[i][i] = 1
    
    for rows in matrix:
        for elements in rows:
            print elements,
        print ""

```

### python_code_2.txt
```python
'''Identity matrices by maps and equivalent list comprehensions'''

import operator


# idMatrix :: Int -> [[Int]]
def idMatrix(n):
    '''Identity matrix of order n,
       expressed as a nested map.
    '''
    eq = curry(operator.eq)
    xs = range(0, n)
    return list(map(
        lambda x: list(map(
            compose(int)(eq(x)),
            xs
        )),
        xs
    ))


# idMatrix3 :: Int -> [[Int]]
def idMatrix2(n):
    '''Identity matrix of order n,
       expressed as a nested comprehension.
    '''
    xs = range(0, n)
    return ([int(x == y) for x in xs] for y in xs)


# TEST ----------------------------------------------------
def main():
    '''
        Identity matrix of dimension five,
        by two different routes.
    '''
    for f in [idMatrix, idMatrix2]:
        print(
            '\n' + f.__name__ + ':',
            '\n\n' + '\n'.join(map(str, f(5))),
        )


# GENERIC -------------------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
>>> def identity(size):
...     return {(x, y):int(x == y) for x in range(size) for y in range(size)}
... 
>>> size = 4
>>> matrix = identity(size)
>>> print('\n'.join(' '.join(str(matrix[(x, y)]) for x in range(size)) for y in range(size)))
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
>>>

```

### python_code_4.txt
```python
np.mat(np.eye(size))

```

