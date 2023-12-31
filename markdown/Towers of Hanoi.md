# Towers of Hanoi

## Task Link
[Rosetta Code - Towers of Hanoi](https://rosettacode.org/wiki/Towers_of_Hanoi)

## Java Code
### java_code_1.txt
```java
public void move(int n, int from, int to, int via) {
  if (n == 1) {
    System.out.println("Move disk from pole " + from + " to pole " + to);
  } else {
    move(n - 1, from, via, to);
    move(1, from, to, via);
    move(n - 1, via, to, from);
  }
}

```

### java_code_2.txt
```java
move(3, 1, 2, 3);

```

### java_code_3.txt
```java
Move disk from pole 1 to pole 2
Move disk from pole 1 to pole 3
Move disk from pole 2 to pole 3
Move disk from pole 1 to pole 2
Move disk from pole 3 to pole 1
Move disk from pole 3 to pole 2
Move disk from pole 1 to pole 2

```

## Python Code
### python_code_1.txt
```python
# (C) 2013 Ezhil Language Project
# Tower of Hanoi – recursive solution

நிரல்பாகம் ஹோனாய்(வட்டுகள், முதல்அச்சு, இறுதிஅச்சு,வட்டு)

  @(வட்டுகள் == 1 ) ஆனால்
     பதிப்பி  “வட்டு ” + str(வட்டு) + “ஐ \t  (” + str(முதல்அச்சு) + “  —> ” +  str(இறுதிஅச்சு)+ “) அச்சிற்கு நகர்த்துக.”
  இல்லை

  @( ["இ", "அ",  "ஆ"]  இல் அச்சு ) ஒவ்வொன்றாக
          @( (முதல்அச்சு != அச்சு)  && (இறுதிஅச்சு  != அச்சு) ) ஆனால்
              நடு = அச்சு
          முடி
  முடி

    # solve problem for n-1 again between src and temp pegs                      
    ஹோனாய்(வட்டுகள்-1,   முதல்அச்சு,நடு,வட்டுகள்-1)

    # move largest disk from src to destination
    ஹோனாய்(1, முதல்அச்சு, இறுதிஅச்சு,வட்டுகள்)

    # solve problem for n-1 again between different pegs
    ஹோனாய்(வட்டுகள்-1, நடு, இறுதிஅச்சு,வட்டுகள்-1)
  முடி
முடி

ஹோனாய்(4,”அ”,”ஆ”,0)

```

### python_code_2.txt
```python
proc hanoi(disks: int; fromTower, toTower, viaTower: string) =
  if disks != 0:
    hanoi(disks - 1, fromTower, viaTower, toTower)
    echo("Move disk ", disks, " from ", fromTower, " to ", toTower)
    hanoi(disks - 1, viaTower, toTower, fromTower)
    
hanoi(4, "1", "2", "3")

```

### python_code_3.txt
```python
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print(f"Move disk {ndisks} from peg {startPeg} to peg {endPeg}")
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
 
hanoi(4)

```

### python_code_4.txt
```python
'''Towers of Hanoi'''


# hanoi :: Int -> String -> String -> String -> [(String, String)]
def hanoi(n):
    '''A list of (from, to) label pairs,
       where a, b and c are labels for each of the
       three Hanoi tower positions.'''
    def go(n, a, b, c):
        p = n - 1
        return (
            go(p, a, c, b) + [(a, b)] + go(p, c, b, a)
        ) if 0 < n else []
    return lambda a: lambda b: lambda c: go(n, a, b, c)


# TEST ----------------------------------------------------
if __name__ == '__main__':

    # fromTo :: (String, String) -> String
    def fromTo(xy):
        '''x -> y'''
        x, y = xy
        return x.rjust(5, ' ') + ' -> ' + y

    print(__doc__ + ':\n\n' + '\n'.join(
        map(fromTo, hanoi(4)('left')('right')('mid'))
    ))

```

### python_code_5.txt
```python
'''Towers of Hanoi'''

from itertools import accumulate, chain, repeat
from inspect import signature
import operator


# hanoi :: Int -> [(Int, Int)]
def hanoi(n):
    '''A list of index pairs, representing disk moves
       between indexed Hanoi positions.
    '''
    def go(n, a, b, c):
        p = n - 1
        return (
            go(p, a, c, b) + [(a, b)] + go(p, c, b, a)
        ) if 0 < n else []
    return go(n, 0, 2, 1)


# hanoiState :: ([Int],[Int],[Int], String) -> (Int, Int) ->
#               ([Int],[Int],[Int], String)
def hanoiState(tpl, ab):
    '''A new Hanoi tower state'''
    a, b = ab
    xs, ys = tpl[a], tpl[b]

    w = 3 * (2 + (2 * max(map(max, filter(len, tpl[:-1])))))

    def delta(i):
        return tpl[i] if i not in ab else xs[1:] if (
            i == a
        ) else [xs[0]] + ys

    tkns = moveName(('left', 'mid', 'right'))(ab)
    caption = ' '.join(tkns)
    return tuple(map(delta, [0, 1, 2])) + (
        (caption if tkns[0] != 'mid' else caption.rjust(w, ' ')),
    )


# showHanoi :: ([Int],[Int],[Int], String) -> String
def showHanoi(tpl):
    '''Captioned string representation of an updated Hanoi tower state.'''

    def fullHeight(n):
        return lambda xs: list(repeat('', n - len(xs))) + xs

    mul = curry(operator.mul)
    lt = curry(operator.lt)
    rods = fmap(fmap(mul('__')))(
        list(tpl[0:3])
    )
    h = max(map(len, rods))
    w = 2 + max(
        map(
            compose(max)(fmap(len)),
            filter(compose(lt(0))(len), rods)
        )
    )
    xs = fmap(concat)(
        transpose(fmap(
            compose(fmap(center(w)(' ')))(
                fullHeight(h)
            )
        )(rods))
    )
    return tpl[3] + '\n\n' + unlines(xs) + '\n' + ('___' * w)


# moveName :: (String, String, String) -> (Int, Int) -> [String]
def moveName(labels):
    '''(from, to) index pair represented as an a -> b string.'''
    def go(ab):
        a, b = ab
        return [labels[a], ' to ', labels[b]] if a < b else [
            labels[b], ' from ', labels[a]
        ]
    return lambda ab: go(ab)


# TEST ----------------------------------------------------
def main():
    '''Visualisation of a Hanoi tower sequence for N discs.
    '''
    n = 3
    print('Hanoi sequence for ' + str(n) + ' disks:\n')
    print(unlines(
        fmap(showHanoi)(
            scanl(hanoiState)(
                (enumFromTo(1)(n), [], [], '')
            )(hanoi(n))
        )
    ))


# GENERIC -------------------------------------------------

# center :: Int -> Char -> String -> String
def center(n):
    '''String s padded with c to approximate centre,
       fitting in but not truncated to width n.'''
    return lambda c: lambda s: s.center(n, c)


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [[a]] -> [a]
# concat :: [String] -> String
def concat(xs):
    '''The concatenation of all the elements
       in a list or iterable.'''

    def f(ys):
        zs = list(chain(*ys))
        return ''.join(zs) if isinstance(ys[0], str) else zs

    return (
        f(xs) if isinstance(xs, list) else (
            chain.from_iterable(xs)
        )
    ) if xs else []


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    if 1 < len(signature(f).parameters):
        return lambda x: lambda y: f(x, y)
    else:
        return f


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))


# fmap :: (a -> b) -> [a] -> [b]
def fmap(f):
    '''fmap over a list.
       f lifted to a function over a list.
    '''
    return lambda xs: list(map(f, xs))


# scanl :: (b -> a -> b) -> b -> [a] -> [b]
def scanl(f):
    '''scanl is like reduce, but returns a succession of
       intermediate values, building from the left.
    '''
    return lambda a: lambda xs: (
        accumulate(chain([a], xs), f)
    )


# showLog :: a -> IO String
def showLog(*s):
    '''Arguments printed with
       intercalated arrows.'''
    print(
        ' -> '.join(map(str, s))
    )


# transpose :: Matrix a -> Matrix a
def transpose(m):
    '''The rows and columns of the argument transposed.
       (The matrix containers and rows can be lists or tuples).
    '''
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            map(inner, z) if tuple != inner else z
        )
    else:
        return m


# unlines :: [String] -> String
def unlines(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)


# TEST ----------------------------------------------------
if __name__ == '__main__':
    main()

```

