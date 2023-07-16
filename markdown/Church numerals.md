# Church numerals

## Task Link
[Rosetta Code - Church numerals](https://rosettacode.org/wiki/Church_numerals)

## Java Code
### java_code_1.txt
```java
package lvijay;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;

public class Church {
    public static interface ChurchNum extends Function<ChurchNum, ChurchNum> {
    }

    public static ChurchNum zero() {
        return f -> x -> x;
    }

    public static ChurchNum next(ChurchNum n) {
        return f -> x -> f.apply(n.apply(f).apply(x));
    }

    public static ChurchNum plus(ChurchNum a) {
        return b -> f -> x -> b.apply(f).apply(a.apply(f).apply(x));
    }

    public static ChurchNum pow(ChurchNum m) {
        return n -> m.apply(n);
    }

    public static ChurchNum mult(ChurchNum a) {
        return b -> f -> x -> b.apply(a.apply(f)).apply(x);
    }

    public static ChurchNum toChurchNum(int n) {
        if (n <= 0) {
            return zero();
        }
        return next(toChurchNum(n - 1));
    }

    public static int toInt(ChurchNum c) {
        AtomicInteger counter = new AtomicInteger(0);
        ChurchNum funCounter = f -> {
            counter.incrementAndGet();
            return f;
        };

        plus(zero()).apply(c).apply(funCounter).apply(x -> x);

        return counter.get();
    }

    public static void main(String[] args) {
        ChurchNum zero  = zero();
        ChurchNum three = next(next(next(zero)));
        ChurchNum four  = next(next(next(next(zero))));

        System.out.println("3+4=" + toInt(plus(three).apply(four))); // prints 7
        System.out.println("4+3=" + toInt(plus(four).apply(three))); // prints 7

        System.out.println("3*4=" + toInt(mult(three).apply(four))); // prints 12
        System.out.println("4*3=" + toInt(mult(four).apply(three))); // prints 12

        // exponentiation.  note the reversed order!
        System.out.println("3^4=" + toInt(pow(four).apply(three))); // prints 81
        System.out.println("4^3=" + toInt(pow(three).apply(four))); // prints 64

        System.out.println("  8=" + toInt(toChurchNum(8))); // prints 8
    }
}

```

## Python Code
### python_code_1.txt
```python
'''Church numerals'''

from itertools import repeat
from functools import reduce


# ----- CHURCH ENCODINGS OF NUMERALS AND OPERATIONS ------

def churchZero():
    '''The identity function.
       No applications of any supplied f
       to its argument.
    '''
    return lambda f: identity


def churchSucc(cn):
    '''The successor of a given
       Church numeral. One additional
       application of f. Equivalent to
       the arithmetic addition of one.
    '''
    return lambda f: compose(f)(cn(f))


def churchAdd(m):
    '''The arithmetic sum of two Church numerals.'''
    return lambda n: lambda f: compose(m(f))(n(f))


def churchMult(m):
    '''The arithmetic product of two Church numerals.'''
    return lambda n: compose(m)(n)


def churchExp(m):
    '''Exponentiation of Church numerals. m^n'''
    return lambda n: n(m)


def churchFromInt(n):
    '''The Church numeral equivalent of
       a given integer.
    '''
    return lambda f: (
        foldl
        (compose)
        (identity)
        (replicate(n)(f))
    )


# OR, alternatively:
def churchFromInt_(n):
    '''The Church numeral equivalent of a given
       integer, by explicit recursion.
    '''
    if 0 == n:
        return churchZero()
    else:
        return churchSucc(churchFromInt(n - 1))


def intFromChurch(cn):
    '''The integer equivalent of a
       given Church numeral.
    '''
    return cn(succ)(0)


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    'Tests'

    cThree = churchFromInt(3)
    cFour = churchFromInt(4)

    print(list(map(intFromChurch, [
        churchAdd(cThree)(cFour),
        churchMult(cThree)(cFour),
        churchExp(cFour)(cThree),
        churchExp(cThree)(cFour),
    ])))


# ------------------ GENERIC FUNCTIONS -------------------

# compose (flip (.)) :: (a -> b) -> (b -> c) -> a -> c
def compose(f):
    '''A left to right composition of two
       functions f and g'''
    return lambda g: lambda x: g(f(x))


# foldl :: (a -> b -> a) -> a -> [b] -> a
def foldl(f):
    '''Left to right reduction of a list,
       using the binary operator f, and
       starting with an initial value a.
    '''
    def go(acc, xs):
        return reduce(lambda a, x: f(a)(x), xs, acc)
    return lambda acc: lambda xs: go(acc, xs)


# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# replicate :: Int -> a -> [a]
def replicate(n):
    '''A list of length n in which every
       element has the value x.
    '''
    return lambda x: repeat(x, n)


# succ :: Enum a => a -> a
def succ(x):
    '''The successor of a value.
       For numeric types, (1 +).
    '''
    return 1 + x if isinstance(x, int) else (
        chr(1 + ord(x))
    )


if __name__ == '__main__':
    main()

```

