# Generator/Exponential

## Task Link
[Rosetta Code - Generator/Exponential](https://rosettacode.org/wiki/Generator/Exponential)

## Java Code
### java_code_1.txt
```java
import java.util.function.LongSupplier;
import static java.util.stream.LongStream.generate;

public class GeneratorExponential implements LongSupplier {
    private LongSupplier source, filter;
    private long s, f;

    public GeneratorExponential(LongSupplier source, LongSupplier filter) {
        this.source = source;
        this.filter = filter;
        f = filter.getAsLong();
    }

    @Override
    public long getAsLong() {
        s = source.getAsLong();

        while (s == f) {
            s = source.getAsLong();
            f = filter.getAsLong();
        }

        while (s > f) {
            f = filter.getAsLong();
        }

        return s;
    }

    public static void main(String[] args) {
        generate(new GeneratorExponential(new SquaresGen(), new CubesGen()))
                .skip(20).limit(10)
                .forEach(n -> System.out.printf("%d ", n));
    }
}

class SquaresGen implements LongSupplier {
    private long n;

    @Override
    public long getAsLong() {
        return n * n++;
    }
}

class CubesGen implements LongSupplier {
    private long n;

    @Override
    public long getAsLong() {
        return n * n * n++;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import islice, count

def powers(m):
    for n in count():
        yield n ** m
    
def filtered(s1, s2):
    v, f = next(s1), next(s2)
    while True:
        if v > f:
            f = next(s2)
            continue
        elif v < f:
            yield v
        v = next(s1)

squares, cubes = powers(2), powers(3)
f = filtered(squares, cubes)
print(list(islice(f, 20, 30)))

```

### python_code_2.txt
```python
'''Exponentials as generators'''

from itertools import count, islice


# powers :: Gen [Int]
def powers(n):
    '''A non-finite succession of integers,
       starting at zero,
       raised to the nth power.'''

    def f(x):
        return pow(x, n)

    return map(f, count(0))


# main :: IO ()
def main():
    '''Taking the difference between two derived generators.'''
    print(
        take(10)(
            drop(20)(
                differenceGen(powers(2))(
                    powers(3)
                )
            )
        )
    )


# GENERIC -------------------------------------------------


# differenceGen :: Gen [a] -> Gen [a] -> Gen [a]
def differenceGen(ga):
    '''All values of ga except any
       already seen in gb.'''
    def go(a, b):
        stream = zip(a, b)
        bs = set([])
        while True:
            xy = next(stream, None)
            if None is not xy:
                x, y = xy
                bs.add(y)
                if x not in bs:
                    yield x
            else:
                return
    return lambda gb: go(ga, gb)


# drop :: Int -> [a] -> [a]
# drop :: Int -> String -> String
def drop(n):
    '''The sublist of xs beginning at
       (zero-based) index n.'''
    def go(xs):
        if isinstance(xs, list):
            return xs[n:]
        else:
            take(n)(xs)
            return xs
    return lambda xs: go(xs)


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.'''
    return lambda xs: (
        xs[0:n]
        if isinstance(xs, list)
        else list(islice(xs, n))
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

