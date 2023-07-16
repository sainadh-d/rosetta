# Department numbers

## Task Link
[Rosetta Code - Department numbers](https://rosettacode.org/wiki/Department_numbers)

## Java Code
### java_code_1.txt
```java
public class DepartmentNumbers {
    public static void main(String[] args) {
        System.out.println("Police  Sanitation  Fire");
        System.out.println("------  ----------  ----");
        int count = 0;
        for (int i = 2; i <= 6; i += 2) {
            for (int j = 1; j <= 7; ++j) {
                if (j == i) continue;
                for (int k = 1; k <= 7; ++k) {
                    if (k == i || k == j) continue;
                    if (i + j + k != 12) continue;
                    System.out.printf("  %d         %d         %d\n", i, j, k);
                    count++;
                }
            }
        }
        System.out.printf("\n%d valid combinations", count);
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations
 
def solve():
    c, p, f, s = "\\,Police,Fire,Sanitation".split(',')
    print(f"{c:>3}  {p:^6} {f:^4} {s:^10}")
    c = 1
    for p, f, s in permutations(range(1, 8), r=3):
        if p + s + f == 12 and p % 2 == 0:
            print(f"{c:>3}: {p:^6} {f:^4} {s:^10}")
            c += 1
 
if __name__ == '__main__':
    solve()

```

### python_code_2.txt
```python
'''Department numbers'''

from itertools import (chain)
from operator import (ne)


# options :: Int -> Int -> Int -> [(Int, Int, Int)]
def options(lo, hi, total):
    '''Eligible integer triples.'''
    ds = enumFromTo(lo)(hi)
    return bind(filter(even, ds))(
        lambda x: bind(filter(curry(ne)(x), ds))(
            lambda y: bind([total - (x + y)])(
                lambda z: [(x, y, z)] if (
                    z != y and lo <= z <= hi
                ) else []
            )
        )
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''

    xs = options(1, 7, 12)
    print(('Police', 'Sanitation', 'Fire'))
    for tpl in xs:
        print(tpl)
    print('\nNo. of options: ' + str(len(xs)))


# GENERIC ABSTRACTIONS ------------------------------------

# bind (>>=) :: [a] -> (a -> [b]) -> [b]
def bind(xs):
    '''List monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.'''
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# even :: Int -> Bool
def even(x):
    '''True if x is an integer
       multiple of two.'''
    return 0 == x % 2


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''Department numbers'''

from operator import ne


# options :: Int -> Int -> Int -> [(Int, Int, Int)]
def options(lo, hi, total):
    '''Eligible triples.'''
    ds = enumFromTo(lo)(hi)
    return [
        (x, y, z)
        for x in filter(even, ds)
        for y in filter(curry(ne)(x), ds)
        for z in [total - (x + y)]
        if y != z and lo <= z <= hi
    ]


# Or with less tightly-constrained generation,
# and more winnowing work downstream:

# options2 :: Int -> Int -> Int -> [(Int, Int, Int)]
def options2(lo, hi, total):
    '''Eligible triples.'''
    ds = enumFromTo(lo)(hi)
    return [
        (x, y, z)
        for x in ds
        for y in ds
        for z in [total - (x + y)]
        if even(x) and y not in [x, z] and lo <= z <= hi
    ]


# GENERIC -------------------------------------------------


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# even :: Int -> Bool
def even(x):
    '''True if x is an integer
       multiple of two.'''
    return 0 == x % 2


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test'''

    xs = options(1, 7, 12)
    print(('Police', 'Sanitation', 'Fire'))
    print(unlines(map(str, xs)))
    print('\nNo. of options: ' + str(len(xs)))


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
# We start with the Police Department.
# Range is the start, stop, and step. This returns only even numbers.
for p in range(2, 7, 2):
    #Next, the Sanitation Department. A simple range.
    for s in range(1, 7):
        # And now the Fire Department. After determining the Police and Fire
        # numbers we just have to subtract those from 12 to get the FD number.
        f = 12 - p -s
        if s >= f: 
            break
        elif f > 7:
            continue
        print("Police: ", p, " Sanitation:", s, " Fire: ", f)
        print("Police: ", p, " Sanitation:", f, " Fire: ", s)

```

### python_code_5.txt
```python
import constraint

depts = ( 'police', 'sanitation', 'fire' )

p = constraint.Problem()

for var in depts:
    p.addVariable(var, range(1,8))

p.addConstraint(constraint.AllDifferentConstraint())
p.addConstraint(lambda *vars: sum(vars)==12, depts)
p.addConstraint(lambda p: p%2==0, ('police',))

for s in p.getSolutions():
    print(s)

```

