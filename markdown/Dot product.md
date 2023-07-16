# Dot product

## Task Link
[Rosetta Code - Dot product](https://rosettacode.org/wiki/Dot_product)

## Java Code
### java_code_1.txt
```java
public class DotProduct {
	
	public static void main(String[] args) {
		double[] a = {1, 3, -5};
		double[] b = {4, -2, -1};
		
		System.out.println(dotProd(a,b));
	}
	
	public static double dotProd(double[] a, double[] b){
		if(a.length != b.length){
			throw new IllegalArgumentException("The dimensions have to be equal!");
		}
		double sum = 0;
		for(int i = 0; i < a.length; i++){
			sum += a[i] * b[i];
		}
		return sum;
	}
}

```

## Python Code
### python_code_1.txt
```python
def dotp(a,b):
    assert len(a) == len(b), 'Vector sizes must match'
    return sum(aterm * bterm for aterm,bterm in zip(a, b))

if __name__ == '__main__':
    a, b = [1, 3, -5], [4, -2, -1]
    assert dotp(a,b) == 3

```

### python_code_2.txt
```python
'''Dot product'''

from operator import (mul)


# dotProduct :: Num a => [a] -> [a] -> Either String a
def dotProduct(xs):
    '''Either the dot product of xs and ys,
       or a string reporting unmatched vector sizes.
    '''
    return lambda ys: Left('vector sizes differ') if (
        len(xs) != len(ys)
    ) else Right(sum(map(mul, xs, ys)))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Dot product of other vectors with [1, 3, -5]'''

    print(
        fTable(main.__doc__ + ':\n')(str)(str)(
            compose(
                either(append('Undefined :: '))(str)
            )(dotProduct([1, 3, -5]))
        )([[4, -2, -1, 8], [4, -2], [4, 2, -1], [4, -2, -1]])
    )


# GENERIC -------------------------------------------------

# Left :: a -> Either a b
def Left(x):
    '''Constructor for an empty Either (option type) value
       with an associated string.
    '''
    return {'type': 'Either', 'Right': None, 'Left': x}


# Right :: b -> Either a b
def Right(x):
    '''Constructor for a populated Either (option type) value'''
    return {'type': 'Either', 'Left': None, 'Right': x}


# append (++) :: [a] -> [a] -> [a]
# append (++) :: String -> String -> String
def append(xs):
    '''Two lists or strings combined into one.'''
    return lambda ys: xs + ys


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# either :: (a -> c) -> (b -> c) -> Either a b -> c
def either(fl):
    '''The application of fl to e if e is a Left value,
       or the application of fr to e if e is a Right value.
    '''
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


# FORMATTING ----------------------------------------------

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
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
def (dot_product x y)
  (sum+map (*) x y)

```

