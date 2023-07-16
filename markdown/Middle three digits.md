# Middle three digits

## Task Link
[Rosetta Code - Middle three digits](https://rosettacode.org/wiki/Middle_three_digits)

## Java Code
### java_code_1.txt
```java
public class MiddleThreeDigits {

    public static void main(String[] args) {
        final long[] passing = {123, 12345, 1234567, 987654321, 10001, -10001,
            -123, -100, 100, -12345, Long.MIN_VALUE, Long.MAX_VALUE};

        final int[] failing = {1, 2, -1, -10, 2002, -2002, 0, Integer.MIN_VALUE,
            Integer.MAX_VALUE};

        for (long n : passing)
            System.out.printf("middleThreeDigits(%s): %s\n", n, middleThreeDigits(n));

        for (int n : failing)
            System.out.printf("middleThreeDigits(%s): %s\n", n, middleThreeDigits(n));
    }

    public static <T> String middleThreeDigits(T n) {
        String s = String.valueOf(n);
        if (s.charAt(0) == '-')
            s = s.substring(1);
        int len = s.length();
        if (len < 3 || len % 2 == 0)
            return "Need odd and >= 3 digits";
        int mid = len / 2;
        return s.substring(mid - 1, mid + 2);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def middle_three_digits(i):
	s = str(abs(i))
	length = len(s)
	assert length >= 3 and length % 2 == 1, "Need odd and >= 3 digits"
	mid = length // 2
	return s[mid-1:mid+2]

>>> passing = [123, 12345, 1234567, 987654321, 10001, -10001, -123, -100, 100, -12345]
>>> failing = [1, 2, -1, -10, 2002, -2002, 0]
>>> for x in passing + failing:
	try:
		answer = middle_three_digits(x)
	except AssertionError as error:
		answer = error
	print("middle_three_digits(%s) returned: %r" % (x, answer))

	
middle_three_digits(123) returned: '123'
middle_three_digits(12345) returned: '234'
middle_three_digits(1234567) returned: '345'
middle_three_digits(987654321) returned: '654'
middle_three_digits(10001) returned: '000'
middle_three_digits(-10001) returned: '000'
middle_three_digits(-123) returned: '123'
middle_three_digits(-100) returned: '100'
middle_three_digits(100) returned: '100'
middle_three_digits(-12345) returned: '234'
middle_three_digits(1) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(2) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(-1) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(-10) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(2002) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(-2002) returned: AssertionError('Need odd and >= 3 digits',)
middle_three_digits(0) returned: AssertionError('Need odd and >= 3 digits',)
>>>

```

### python_code_2.txt
```python
'''Middle 3 digits'''


# mid3digits :: Int -> Either String String
def mid3digits(n):
    '''Either the middle three digits,
       or an explanatory string.'''
    m = abs(n)
    s = str(m)
    return Left('Less than 3 digits') if (100 > m) else (
        Left('Even digit count') if even(len(s)) else Right(
            s[(len(s) - 3) // 2:][0:3]
        )
    )


# TEST ----------------------------------------------------
def main():
    '''Test'''

    def bracketed(x):
        return '(' + str(x) + ')'

    print(
        tabulated('Middle three digits, where defined:\n')(str)(
            either(bracketed)(str)
        )(mid3digits)([
            123, 12345, 1234567, 987654321, 10001, -10001, -123,
            -100, 100, -12345, 1, 2, -1, -10, 2002, -2002, 0
        ])
    )


# GENERIC -------------------------------------------------

# Left :: a -> Either a b
def Left(x):
    '''Constructor for an empty Either (option type) value
       with an associated string.'''
    return {'type': 'Either', 'Right': None, 'Left': x}


# Right :: b -> Either a b
def Right(x):
    '''Constructor for a populated Either (option type) value'''
    return {'type': 'Either', 'Left': None, 'Right': x}


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


# either :: (a -> c) -> (b -> c) -> Either a b -> c
def either(fl):
    '''The application of fl to e if e is a Left value,
       or the application of fr to e if e is a Right value.'''
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


# even :: Int -> Bool
def even(x):
    '''Is x even ?'''
    return 0 == x % 2


# tabulated :: String -> (b -> String) -> (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
                f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(str), xs))
        return s + '\n' + '\n'.join(
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


if __name__ == '__main__':
    main()

```

