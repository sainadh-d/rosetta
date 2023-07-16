# Harshad or Niven series

## Task Link
[Rosetta Code - Harshad or Niven series](https://rosettacode.org/wiki/Harshad_or_Niven_series)

## Java Code
### java_code_1.txt
```java
public class Harshad{
    private static long sumDigits(long n){
        long sum = 0;
        for(char digit:Long.toString(n).toCharArray()){
            sum += Character.digit(digit, 10);
        }
        return sum;
    }
    public static void main(String[] args){
        for(int count = 0, i = 1; count < 20;i++){
            if(i % sumDigits(i) == 0){
                System.out.println(i);
                count++;
            }
        }
        System.out.println();
        for(int i = 1001; ; i++){
            if(i % sumDigits(i) == 0){
                System.out.println(i);
                break;
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> import itertools
>>> def harshad():
	for n in itertools.count(1):
		if n % sum(int(ch) for ch in str(n)) == 0:
			yield n

		
>>> list(itertools.islice(harshad(), 0, 20))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42]
>>> for n in harshad():
	if n > 1000:
		print(n)
		break

	
1002
>>>

```

### python_code_2.txt
```python
>>> from itertools import count, islice
>>> harshad = (n for n in count(1) if n % sum(int(ch) for ch in str(n)) == 0)
>>> list(islice(harshad, 0, 20))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42]
>>> next(x for x in harshad if x > 1000)
1002
>>>

```

### python_code_3.txt
```python
'''Harshad or Niven series'''

from itertools import count, dropwhile, islice


# harshads :: () -> [Int]
def harshads():
    '''Harshad series'''
    return (
        x for x in count(1)
        if 0 == x % digitSum(x)
    )


# digitSum :: Int -> Int
def digitSum(n):
    '''Sum of the decimal digits of n.'''
    def go(x):
        return None if 0 == x else divmod(x, 10)
    return sum(unfoldl(go)(n))


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''First 20, and first above 1000.'''

    def firstTwenty(xs):
        return take(20)(xs)

    def firstAbove1000(xs):
        return take(1)(
            dropwhile(lambda x: 1000 >= x, xs)
        )

    print(
        fTable(__doc__ + ':\n')(
            lambda x: x.__name__
        )(showList)(lambda f: f(harshads()))([
            firstTwenty,
            firstAbove1000
        ])
    )


# ----------------------- GENERIC ------------------------

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


# unfoldl :: (b -> Maybe (b, a)) -> b -> [a]
def unfoldl(f):
    '''A lazy (generator) list unfolded from a seed value
       by repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None or just (residue, value).
       For a strict output list, wrap the result with list()
    '''
    def go(v):
        residueValue = f(v)
        while residueValue:
            yield residueValue[1]
            residueValue = f(residueValue[0])
    return go


# ----------------------- DISPLAY ------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function ->
       fx display function -> f -> xs -> tabular string.
    '''
    def gox(xShow):
        def gofx(fxShow):
            def gof(f):
                def goxs(xs):
                    ys = [xShow(x) for x in xs]
                    w = max(map(len, ys))

                    def arrowed(x, y):
                        return y.rjust(w, ' ') + ' -> ' + (
                            fxShow(f(x))
                        )
                    return s + '\n' + '\n'.join(
                        map(arrowed, xs, ys)
                    )
                return goxs
            return gof
        return gofx
    return gox


# showList :: [a] -> String
def showList(xs):
    '''Stringification of a list.'''
    return '[' + ','.join(repr(x) for x in xs) + ']'


# MAIN ---
if __name__ == '__main__':
    main()

```

