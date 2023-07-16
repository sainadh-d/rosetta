# Egyptian division

## Task Link
[Rosetta Code - Egyptian division](https://rosettacode.org/wiki/Egyptian_division)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class EgyptianDivision {

    /**
     * Runs the method and divides 580 by 34
     *
     * @param args not used
     */
    public static void main(String[] args) {

        divide(580, 34);

    }

    /**
     * Divides <code>dividend</code> by <code>divisor</code> using the Egyptian Division-Algorithm and prints the
     * result to the console
     *
     * @param dividend
     * @param divisor
     */
    public static void divide(int dividend, int divisor) {

        List<Integer> powersOf2 = new ArrayList<>();
        List<Integer> doublings = new ArrayList<>();

        //populate the powersof2- and doublings-columns
        int line = 0;
        while ((Math.pow(2, line) * divisor) <= dividend) { //<- could also be done with a for-loop
            int powerOf2 = (int) Math.pow(2, line);
            powersOf2.add(powerOf2);
            doublings.add(powerOf2 * divisor);
            line++;
        }

        int answer = 0;
        int accumulator = 0;

        //Consider the rows in reverse order of their construction (from back to front of the List<>s)
        for (int i = powersOf2.size() - 1; i >= 0; i--) {
            if (accumulator + doublings.get(i) <= dividend) {
                accumulator += doublings.get(i);
                answer += powersOf2.get(i);
            }
        }

        System.out.println(String.format("%d, remainder %d", answer, dividend - accumulator));
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product

def egyptian_divmod(dividend, divisor):
    assert divisor != 0
    pwrs, dbls = [1], [divisor]
    while dbls[-1] <= dividend:
        pwrs.append(pwrs[-1] * 2)
        dbls.append(pwrs[-1] * divisor)
    ans, accum = 0, 0
    for pwr, dbl in zip(pwrs[-2::-1], dbls[-2::-1]):
        if accum + dbl <= dividend:
            accum += dbl
            ans += pwr
    return ans, abs(accum - dividend)

if __name__ == "__main__":
    # Test it gives the same results as the divmod built-in
    for i, j in product(range(13), range(1, 13)):
            assert egyptian_divmod(i, j) == divmod(i, j)
    # Mandated result
    i, j = 580, 34
    print(f'{i} divided by {j} using the Egyption method is %i remainder %i'
          % egyptian_divmod(i, j))

```

### python_code_2.txt
```python
'''Quotient and remainder of division by the Rhind papyrus method.'''

from functools import reduce


# eqyptianQuotRem :: Int -> Int -> (Int, Int)
def eqyptianQuotRem(m):
    '''Quotient and remainder derived by the Eqyptian method.'''

    def expansion(xi):
        '''Doubled value, and next power of two - both by self addition.'''
        x, i = xi
        return Nothing() if x > m else Just(
            ((x + x, i + i), xi)
        )

    def collapse(qr, ix):
        '''Addition of a power of two to the quotient,
           and subtraction of a paired value from the remainder.'''
        i, x = ix
        q, r = qr
        return (q + i, r - x) if x < r else qr

    return lambda n: reduce(
        collapse,
        unfoldl(expansion)(
            (1, n)
        ),
        (0, m)
    )


# ------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Test'''
    print(
        eqyptianQuotRem(580)(34)
    )


# ------------------- GENERIC FUNCTIONS -------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.'''
    return {'type': 'Maybe', 'Nothing': True}


# unfoldl(lambda x: Just(((x - 1), x)) if 0 != x else Nothing())(10)
# -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''Dual to reduce or foldl.
       Where these reduce a list to a summary value, unfoldl
       builds a list from a seed value.
       Where f returns Just(a, b), a is appended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        x, r = v, v
        xs = []
        while True:
            mb = f(x)
            if mb.get('Nothing'):
                return xs
            else:
                x, r = mb.get('Just')
                xs.insert(0, r)
        return xs
    return go


# MAIN ----------------------------------------------------
if __name__ == '__main__':
    main()

```

