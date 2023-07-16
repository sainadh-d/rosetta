# RPG attributes generator

## Task Link
[Rosetta Code - RPG attributes generator](https://rosettacode.org/wiki/RPG_attributes_generator)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.Random;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Rpg {

    private static final Random random = new Random();
 
    public static int genAttribute() {
        return random.ints(1, 6 + 1) // Throw dices between 1 and 6
            .limit(4) // Do 5 throws
            .sorted() // Sort them
            .limit(3) // Take the top 3
            .sum();   // Sum them
    }
 
    public static void main(String[] args) {
        while (true) {
            List<Integer> stats =
                Stream.generate(Rpg::genAttribute) // Generate some stats
                    .limit(6) // Take 6
                    .collect(toList()); // Save them in an array
            int sum = stats.stream().mapToInt(Integer::intValue).sum();
            long count = stats.stream().filter(v -> v >= 15).count();
            if (count >= 2 && sum >= 75) {
                System.out.printf("The 6 random numbers generated are: %s\n", stats);
                System.out.printf("Their sum is %s and %s of them are >= 15\n", sum, count);
                return;
            }      
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import random
random.seed()
attributes_total = 0
count = 0

while attributes_total < 75 or count < 2:
    attributes = []

    for attribute in range(0, 6):
        rolls = []
        
        for roll in range(0, 4):
            result = random.randint(1, 6)
            rolls.append(result)
        
        sorted_rolls = sorted(rolls)
        largest_3 = sorted_rolls[1:]
        rolls_total = sum(largest_3)
        
        if rolls_total >= 15:
            count += 1
        
        attributes.append(rolls_total)

    attributes_total = sum(attributes)
    
print(attributes_total, attributes)

```

### python_code_2.txt
```python
import random
random.seed()
total = 0
count = 0

while total < 75 or count < 2:
    attributes = [(sum(sorted([random.randint(1, 6) for roll in range(0, 4)])[1:])) for attribute in range(0, 6)]    
   
    for attribute in attributes:
        if attribute >= 15:
            count += 1
   
    total = sum(attributes)
    
print(total, attributes)

```

### python_code_3.txt
```python
import random

def compute():
    values = []
    while (sum(values) < 75                            # Total must be >= 75
           or sum(1 for v in values if v >= 15) < 2):  # Two must be >= 15
        values = [sum(sorted(random.randint(1, 6) for _ in range(4))[1:]) for _ in range(6)]
    return sum(values), values

for i in range(3):
    print(*compute())

```

### python_code_4.txt
```python
'''RPG Attributes Generator'''

from itertools import islice
from random import randint
from operator import eq


# heroes :: Gen IO [(Int, Int, Int, Int, Int, Int)]
def heroes(p):
    '''Non-finite list of heroes matching
       the requirements of predicate p.
    '''
    while True:
        yield tuple(
            until(p)(character)([])
        )


# character :: () -> IO [Int]
def character(_):
    '''A random character with six
       integral attributes.
    '''
    return [
        sum(sorted(map(
            randomRInt(1)(6),
            enumFromTo(1)(4)
        ))[1:])
        for _ in enumFromTo(1)(6)
    ]


# ------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Test :: Sample of 10'''

    # seventyFivePlusWithTwo15s :: [Int] -> Bool
    def seventyFivePlusIncTwo15s(xs):
        '''Sums to 75 or more,
           and includes at least two 15s.
        '''
        return 75 <= sum(xs) and (
            1 < len(list(filter(curry(eq)(15), xs)))
        )

    print('A sample of 10:\n')
    print(unlines(
        str(sum(x)) + ' -> ' + str(x) for x
        in take(10)(heroes(
            seventyFivePlusIncTwo15s
        ))
    ))


# ------------------------- GENERIC -------------------------

# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.
    '''
    return lambda x: lambda y: f(x, y)


# enumFromTo :: Int -> Int -> [Int]
def enumFromTo(m):
    '''Enumeration of integer values [m..n]'''
    return lambda n: range(m, 1 + n)


# randomRInt :: Int -> Int -> IO () -> Int
def randomRInt(m):
    '''The return value of randomRInt is itself
       a function. The returned function, whenever
       called, yields a a new pseudo-random integer
       in the range [m..n].
    '''
    return lambda n: lambda _: randint(m, n)


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, (list, tuple))
        else list(islice(xs, n))
    )


# unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f, x):
        v = x
        while not p(v):
            v = f(v)
        return v
    return lambda f: lambda x: go(f, x)


if __name__ == '__main__':
    main()

```

### python_code_5.txt
```python
import random; print((lambda attr: f"Attributes: {attr}\nTotal: {sum(attr)}")((lambda func, roll_func: func(func, roll_func, roll_func()))((lambda func, roll_func, rolls: rolls if sum(rolls) >= 75 and rolls.count(15) >= 2 else func(func, roll_func, roll_func())), lambda: [sum(sorted(random.randint(1, 6) for _ in range(4))[1:]) for _ in range(6)])))

```

