# Function composition

## Task Link
[Rosetta Code - Function composition](https://rosettacode.org/wiki/Function_composition)

## Java Code
### java_code_1.txt
```java
public class Compose {

    // Java doesn't have function type so we define an interface
    // of function objects instead
    public interface Fun<A,B> {
        B call(A x);
    }

    public static <A,B,C> Fun<A,C> compose(final Fun<B,C> f, final Fun<A,B> g) {
        return new Fun<A,C>() {
            public C call(A x) {
                return f.call(g.call(x));
            }
        };
    }

    public static void main(String[] args) {
        Fun<Double,Double> sin = new Fun<Double,Double>() {
            public Double call(Double x) {
                return Math.sin(x);
            }
        };
        Fun<Double,Double> asin = new Fun<Double,Double>() {
            public Double call(Double x) {
                return Math.asin(x);
            }
        };

        Fun<Double,Double> sin_asin = compose(sin, asin);

        System.out.println(sin_asin.call(0.5)); // prints "0.5"
    }
}

```

### java_code_2.txt
```java
import java.util.function.Function;

public class Compose {
    public static void main(String[] args) {
        Function<Double,Double> sin_asin = ((Function<Double,Double>)Math::sin).compose(Math::asin);

        System.out.println(sin_asin.apply(0.5)); // prints "0.5"
    }
}

```

### java_code_3.txt
```java
import java.util.function.Function;

public class Compose {
    public static <A,B,C> Function<A,C> compose(Function<B,C> f, Function<A,B> g) {
        return x -> f.apply(g.apply(x));
    }

    public static void main(String[] args) {
        Function<Double,Double> sin_asin = compose(Math::sin, Math::asin);

        System.out.println(sin_asin.apply(0.5)); // prints "0.5"
    }
}

```

## Python Code
### python_code_1.txt
```python
compose = lambda f, g: lambda x: f( g(x) )

```

### python_code_2.txt
```python
>>> compose = lambda f, g: lambda x: f( g(x) )
>>> from math import sin, asin
>>> sin_asin = compose(sin, asin)
>>> sin_asin(0.5)
0.5
>>>

```

### python_code_3.txt
```python
from math import (acos, cos, asin, sin)


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g, f):
    '''Right to left function composition.'''
    return lambda x: g(f(x))


# main :: IO ()
def main():
    '''Test'''

    print(list(map(
        lambda f: f(0.5),
        zipWith(compose)(
            [sin, cos, lambda x: x ** 3.0]
        )([asin, acos, lambda x: x ** (1 / 3.0)])
    )))


# GENERIC FUNCTIONS ---------------------------------------


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    '''A list constructed by zipping with a
       custom function, rather than with the
       default tuple constructor.'''
    return lambda xs: lambda ys: (
        map(f, xs, ys)
    )


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
from functools import reduce
from math import sqrt


def compose(*fs):
    '''Composition, from right to left,
       of an arbitrary number of functions.
    '''
    def go(f, g):
        return lambda x: f(g(x))

    return reduce(go, fs, lambda x: x)


# ------------------------- TEST -------------------------
def main():
    '''Composition of three functions.'''

    f = compose(
        half,
        succ,
        sqrt
    )

    print(
        f(5)
    )


# ----------------------- GENERAL ------------------------
def half(n):
    return n / 2


def succ(n):
    return 1 + n


if __name__ == '__main__':
    main()

```

### python_code_5.txt
```python
# Contents of `pip install compositions'

class Compose(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        return self.func(x)

    def __mul__(self, neighbour):
        return Compose(lambda x: self.func(neighbour.func(x)))

# from composition.composition import Compose
if __name__ == "__main__":
    # Syntax 1
    @Compose
    def f(x):
        return x

    # Syntax 2
    g = Compose(lambda x: x)

    print((f * g)(2))

```

