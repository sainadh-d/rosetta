# SEDOLs

## Task Link
[Rosetta Code - SEDOLs](https://rosettacode.org/wiki/SEDOLs)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class SEDOL{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			String sedol = sc.next();
			System.out.println(sedol + getSedolCheckDigit(sedol));
		}
	}
	
	private static final int[] mult = {1, 3, 1, 7, 3, 9};
	
	public static int getSedolCheckDigit(String str){
	    if(!validateSedol(str)){
	    	System.err.println("SEDOL strings must contain six characters with no vowels.");
	    	return -1;
	    }
	    str = str.toUpperCase();
	    int total = 0;
	    for(int i = 0;i < 6; i++){
	        char s = str.charAt(i);
	        total += Character.digit(s, 36) * mult[i];
	    }
	    return (10 - (total % 10)) % 10;
	}

	public static boolean validateSedol(String str){
		return (str.length() == 6) && !str.toUpperCase().matches(".*?[AEIOU].*?");
	}
}

```

## Python Code
### python_code_1.txt
```python
def char2value(c):
  assert c not in 'AEIOU', "No vowels"
  return int(c, 36)

sedolweight = [1,3,1,7,3,9]

def checksum(sedol):
    tmp = sum(map(lambda ch, weight: char2value(ch) * weight,
                  sedol, sedolweight)
               )
    return str((10 - (tmp % 10)) % 10)

for sedol in '''
    710889
    B0YBKJ
    406566
    B0YBLH
    228276
    B0YBKL
    557910
    B0YBKR
    585284
    B0YBKT
    '''.split():
    print sedol + checksum(sedol)

```

### python_code_2.txt
```python
'''SEDOL checksum digits'''

from functools import reduce


# sedolCheckSumDigitLR :: String -> Either String Char
def sedolCheckSumDigitLR(s):
    '''Either an explanatory message, or a
       checksum digit character to append
       to a given six-character SEDOL string.
    '''
    def goLR(lr, cn):
        c, n = cn
        return bindLR(lr)(
            lambda a: bindLR(sedolValLR(c))(
                lambda x: Right(a + x * n)
            )
        )
    return bindLR(
        reduce(
            goLR,
            zip(s, [1, 3, 1, 7, 3, 9]),
            Right(0)
        )
    )(lambda d: Right(str((10 - (d % 10)) % 10)))


# sedolValLR :: Char -> Either String Char
def sedolValLR(c):
    '''Either an explanatory message, or the
       SEDOL value of a given character.
    '''
    return Right(int(c, 36)) if (
        c not in 'AEIOU'
    ) else Left('Unexpected vowel in SEDOL string: ' + c)


# TEST -------------------------------------------------
def main():
    '''Append checksums where valid.'''

    print(
        fTable(__doc__ + ':\n')(str)(
            either(str)(str)
        )(sedolCheckSumDigitLR)(
            '''710889
               B0YBKJ
               406566
               B0YBLH
               228276
               B0YBKL
               BOYBKL
               557910
               B0YBKR
               585284
               B0YBKT
               B00030
            '''.split()
        )
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


# bindLR (>>=) :: Either a -> (a -> Either b) -> Either b
def bindLR(m):
    '''Either monad injection operator.
       Two computations sequentially composed,
       with any value produced by the first
       passed as an argument to the second.'''
    return lambda mf: (
        mf(m.get('Right')) if None is m.get('Left') else m
    )


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# either :: (a -> c) -> (b -> c) -> Either a b -> c
def either(fl):
    '''The application of fl to e if e is a Left value,
       or the application of fr to e if e is a Right value.'''
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


# fTable :: String -> (a -> String) ->
#                     (b -> String) ->
#        (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```
