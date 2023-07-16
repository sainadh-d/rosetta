# Van Eck sequence

## Task Link
[Rosetta Code - Van Eck sequence](https://rosettacode.org/wiki/Van_Eck_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;

public class VanEckSequence {

    public static void main(String[] args) {
        System.out.println("First 10 terms of Van Eck's sequence:");
        vanEck(1, 10);
        System.out.println("");
        System.out.println("Terms 991 to 1000 of Van Eck's sequence:");
        vanEck(991, 1000);
    }
    
    private static void vanEck(int firstIndex, int lastIndex) {
        Map<Integer,Integer> vanEckMap = new HashMap<>();        
        int last = 0;
        if ( firstIndex == 1 ) {
            System.out.printf("VanEck[%d] = %d%n", 1, 0);
        }
        for ( int n = 2 ; n <= lastIndex ; n++ ) {
            int vanEck = vanEckMap.containsKey(last) ? n - vanEckMap.get(last) : 0;
            vanEckMap.put(last, n);
            last = vanEck;
            if ( n >= firstIndex ) {
                System.out.printf("VanEck[%d] = %d%n", n, vanEck);
            }
        }
        
    }

}

```

## Python Code
### python_code_1.txt
```python
def van_eck():
    n, seen, val = 0, {}, 0
    while True:
        yield val
        last = {val: n}
        val = n - seen.get(val, n)
        seen.update(last)
        n += 1
#%%
if __name__ == '__main__':
    print("Van Eck: first 10 terms:  ", list(islice(van_eck(), 10)))
    print("Van Eck: terms 991 - 1000:", list(islice(van_eck(), 1000))[-10:])

```

### python_code_2.txt
```python
def van_eck():
    n = 0
    seen = [0]
    val = 0
    while True:
        yield val
        if val in seen[1:]:
            val = seen.index(val, 1)
        else:
            val = 0
        seen.insert(0, val)
        n += 1

```

### python_code_3.txt
```python
'''Van Eck sequence'''

from functools import reduce
from itertools import repeat


# vanEck :: Int -> [Int]
def vanEck(n):
    '''First n terms of the van Eck sequence.'''

    return churchNumeral(n)(
        lambda xs: cons(
            maybe(0)(succ)(
                elemIndex(xs[0])(xs[1:])
            )
        )(xs) if xs else [0]
    )([])[::-1]


# TEST ----------------------------------------------------
def main():
    '''Terms of the Van Eck sequence'''
    print(
        main.__doc__ + ':\n\n' +
        'First 10: '.rjust(18, ' ') + repr(vanEck(10)) + '\n' +
        '991 - 1000: '.rjust(18, ' ') + repr(vanEck(1000)[990:])
    )


# GENERIC -------------------------------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# churchNumeral :: Int -> (a -> a) -> a -> a
def churchNumeral(n):
    '''n applications of a function
    '''
    return lambda f: lambda x: reduce(
        lambda a, g: g(a), repeat(f, n), x
    )


# cons :: a -> [a] -> [a]
def cons(x):
    '''Construction of a list from a head and a tail.
    '''
    return lambda xs: [x] + xs


# elemIndex :: Eq a => a -> [a] -> Maybe Int
def elemIndex(x):
    '''Just the index of the first element in xs
       which is equal to x,
       or Nothing if there is no such element.
    '''
    def go(xs):
        try:
            return Just(xs.index(x))
        except ValueError:
            return Nothing()
    return go


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if None is m or m.get('Nothing') else (
        f(m.get('Just'))
    )


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
'''Van Eck series by map-accumulation'''

from functools import reduce
from itertools import repeat


# vanEck :: Int -> [Int]
def vanEck(n):
    '''First n terms of the vanEck sequence.'''
    def go(xns, i):
        x, ns = xns

        prev = ns[x]
        v = i - prev if 0 is not prev else 0
        return (
            (v, insert(ns, x, i)),
            v
        )

    return [0] + mapAccumL(go)((0, list(repeat(0, n))))(
        range(1, n)
    )[1]


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''The last 10 of the first N vanEck terms'''
    print(
        fTable(main.__doc__ + ':\n')(
            lambda m: 'N=' + str(m), repr,
            lambda n: vanEck(n)[-10:], [10, 1000, 10000]
        )
    )


# ----------------------- FORMATTING -----------------------
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
    return go


# ------------------------ GENERIC -------------------------

# insert :: Array Int -> Int -> Int -> Array Int
def insert(xs, i, v):
    '''An array updated at position i with value v.'''
    xs[i] = v
    return xs


# mapAccumL :: (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
def mapAccumL(f):
    '''A tuple of an accumulation and a list derived by a
       combined map and fold,
       with accumulation from left to right.
    '''
    def go(a, x):
        tpl = f(a[0], x)
        return (tpl[0], a[1] + [tpl[1]])
    return lambda acc: lambda xs: (
        reduce(go, xs, (acc, []))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

