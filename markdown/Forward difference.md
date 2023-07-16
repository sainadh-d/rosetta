# Forward difference

## Task Link
[Rosetta Code - Forward difference](https://rosettacode.org/wiki/Forward_difference)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
public class FD {
    public static void main(String args[]) {
        double[] a = {90, 47, 58, 29, 22, 32, 55, 5, 55, 73};
        System.out.println(Arrays.toString(dif(a, 1)));
        System.out.println(Arrays.toString(dif(a, 2)));
        System.out.println(Arrays.toString(dif(a, 9)));
        System.out.println(Arrays.toString(dif(a, 10)));      //let's test
        System.out.println(Arrays.toString(dif(a, 11)));
        System.out.println(Arrays.toString(dif(a, -1)));
        System.out.println(Arrays.toString(dif(a, 0)));
    }

    public static double[] dif(double[] a, int n) {
        if (n < 0)
            return null; // if the programmer was dumb

        for (int i = 0; i < n && a.length > 0; i++) {
            double[] b = new double[a.length - 1];
            for (int j = 0; j < b.length; j++){
                b[j] = a[j+1] - a[j];
            }
            a = b; //"recurse"
        }
        return a;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> dif = lambda s: [x-s[i] for i,x in enumerate(s[1:])]
>>> # or, dif = lambda s: [x-y for x,y in zip(s[1:],s)]
>>> difn = lambda s, n: difn(dif(s), n-1) if n else s

>>> s = [90, 47, 58, 29, 22, 32, 55, 5, 55, 73]
>>> difn(s, 0)
[90, 47, 58, 29, 22, 32, 55, 5, 55, 73]
>>> difn(s, 1)
[-43, 11, -29, -7, 10, 23, -50, 50, 18]
>>> difn(s, 2)
[54, -40, 22, 17, 13, -73, 100, -32]

>>> from pprint import pprint
>>> pprint( [difn(s, i) for i in xrange(10)] )
[[90, 47, 58, 29, 22, 32, 55, 5, 55, 73],
 [-43, 11, -29, -7, 10, 23, -50, 50, 18],
 [54, -40, 22, 17, 13, -73, 100, -32],
 [-94, 62, -5, -4, -86, 173, -132],
 [156, -67, 1, -82, 259, -305],
 [-223, 68, -83, 341, -564],
 [291, -151, 424, -905],
 [-442, 575, -1329],
 [1017, -1904],
 [-2921]]

```

### python_code_2.txt
```python
'''Forward difference'''


from itertools import islice
from operator import sub


# forwardDifference :: Num a => [a] -> [a]
def forwardDifference(xs):
    '''1st order forward difference of xs.
    '''
    return [sub(*x) for x in zip(xs[1:], xs)]


# nthForwardDifference :: Num a => [a] -> Int -> [a]
def nthForwardDifference(xs):
    '''Nth order forward difference of xs.
    '''
    return index(iterate(forwardDifference)(xs))


# ------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Nth order forward difference.'''

    xs = [90, 47, 58, 29, 22, 32, 55, 5, 55, 73]

    print('9th order forward difference of:')
    print(xs)
    print('')
    print(
        ' -> ' + repr(nthForwardDifference(xs)(9))
    )

    print('\nSuccessive orders of forward difference:')
    print(unlines([
        str(i) + ' -> ' + repr(x) for i, x in
        enumerate(take(10)(
            iterate(forwardDifference)(xs)
        ))
    ]))


# ------------------- GENERIC FUNCTIONS -------------------

# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        xs[n] if (
            hasattr(xs, "__getitem__")
        ) else next(islice(xs, n, None))
    )


# iterate :: (a -> a) -> a -> Gen [a]
def iterate(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return go


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


# MAIN ---
if __name__ == '__main__':
    main()

```

