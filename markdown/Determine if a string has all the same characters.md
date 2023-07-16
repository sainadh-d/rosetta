# Determine if a string has all the same characters

## Task Link
[Rosetta Code - Determine if a string has all the same characters](https://rosettacode.org/wiki/Determine_if_a_string_has_all_the_same_characters)

## Java Code
### java_code_1.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

```

### java_code_2.txt
```java
public static void main(String[] args) {
    String[] strings = {
        "", "   ", "2", "333", ".55", "tttTTT", "5", "4444 444k"
    };
    for (String string : strings)
        System.out.println(printCompare(string));
}

static String printCompare(String string) {
    String stringA = "'%s' %d".formatted(string, string.length());
    Pattern pattern = Pattern.compile("(.)\\1*");
    Matcher matcher = pattern.matcher(string);
    StringBuilder stringB = new StringBuilder();
    /* 'Matcher' works dynamically, so we'll have to denote a change */
    boolean difference = false;
    char character;
    String newline = System.lineSeparator();
    while (matcher.find()) {
        if (matcher.start() != 0) {
            character = matcher.group(1).charAt(0);
            stringB.append(newline);
            stringB.append("  Char '%s' (0x%x)".formatted(character, (int) character));
            stringB.append(" @ index %d".formatted(matcher.start()));
            difference = true;
        }
    }
    if (!difference)
        stringB.append(newline).append("  All characters are the same");
    return stringA + stringB;
}

```

### java_code_3.txt
```java
public class Main{
	public static void main(String[] args){
		String[] tests = {"", "   ", "2", "333", ".55", "tttTTT", "4444 444k"};
		for(String s:tests)
			analyze(s);
	}

	public static void analyze(String s){
		System.out.printf("Examining [%s] which has a length of %d:\n", s, s.length());
		if(s.length() > 1){
			char firstChar = s.charAt(0);
			int lastIndex = s.lastIndexOf(firstChar);
			if(lastIndex != 0){
				System.out.println("\tNot all characters in the string are the same.");
				System.out.printf("\t'%c' (0x%x) is different at position %d\n", firstChar, (int) firstChar, lastIndex);
				return;
			}
		}
		System.out.println("\tAll characters in the string are the same.");
	}
}

```

### java_code_4.txt
```java
import java.util.OptionalInt;

public final class AllSameCharacters {

	public static void main(String[] aArgs) {
		String[] words = { "", "   ", "2", "333", ".55", "tttTTT", "4444 444k" };
		for ( String word : words ) {
			analyse(word);
		}		
	}
	
	private static void analyse(String aText) {
		System.out.println("Examining \"" + aText + "\", which has length " + aText.length() + ":");

		OptionalInt mismatch = aText.chars().filter( ch -> ch != aText.charAt(0) ).findFirst();		
		
		if ( mismatch.isPresent() ) {
			char fault = (char) mismatch.getAsInt();
			System.out.println("    Not all characters in the string are the same.");
			System.out.println("    Character \"" + fault + "\" (" + Integer.toHexString((char) fault)
			                        + ") is different at index " + aText.indexOf(fault));
		} else {
			System.out.println("    All characters in the string are the same.");			
		}		
	}

}

```

## Python Code
### python_code_1.txt
```python
'''Determine if a string has all the same characters'''

from itertools import groupby


# firstDifferingCharLR :: String -> Either String Dict
def firstDifferingCharLR(s):
    '''Either a message reporting that no character changes were
       seen, or a dictionary with details of the  first character
       (if any) that differs from that at the head of the string.
    '''
    def details(xs):
        c = xs[1][0]
        return {
            'char': repr(c),
            'hex': hex(ord(c)),
            'index': s.index(c),
            'total': len(s)
        }
    xs = list(groupby(s))
    return Right(details(xs)) if 1 < len(xs) else (
        Left('Total length ' + str(len(s)) + ' - No character changes.')
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test of 7 strings'''

    print(fTable('First, if any, points of difference:\n')(repr)(
        either(identity)(
            lambda dct: dct['char'] + ' (' + dct['hex'] +
            ') at character ' + str(1 + dct['index']) +
            ' of ' + str(dct['total']) + '.'
        )
    )(firstDifferingCharLR)([
        '',
        '   ',
        '2',
        '333',
        '.55',
        'tttTTT',
        '4444 444'
    ]))


# GENERIC -------------------------------------------------

# either :: (a -> c) -> (b -> c) -> Either a b -> c
def either(fl):
    '''The application of fl to e if e is a Left value,
       or the application of fr to e if e is a Right value.
    '''
    return lambda fr: lambda e: fl(e['Left']) if (
        None is e['Right']
    ) else fr(e['Right'])


# identity :: a -> a
def identity(x):
    '''The identity function.'''
    return x


# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
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


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
'''Determine if a string has all the same characters'''

from itertools import takewhile


# inconsistentChar :: String -> Maybe (Int, Char)
def inconsistentChar(s):
    '''Just the first inconsistent character and its position,
       or Nothing if all the characters of s are the same,
    '''
    if s:
        h = s[0]
        pre, post = span(lambda c: h == c)(s)
        return Just((len(pre), post[0])) if post else Nothing()
    else:
        return Nothing()


# --------------------------TEST---------------------------
# main :: IO ()
def main():
    '''Consistency tests of seven strings'''

    samples = ['', '   ', '2', '333', '.55', 'tttTTT', '4444 444']
    w = 1 + max(map(len, samples))

    def pfx(s):
        return ("'" + s).rjust(w) + "' -> "

    def charPosn(ic):
        i, c = ic
        return "inconsistent '" + c + "' (" + hex(ord(c)) + ")" + (
            " at char " + str(1 + i)
        )

    print(main.__doc__ + ':\n')
    print(
        '\n'.join([
            pfx(s) + maybe('consistent')(charPosn)(
                inconsistentChar(s)
            )
            for s in samples
        ])
    )


# -------------------------GENERIC-------------------------

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


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if None is m or m.get('Nothing') else (
        f(m.get('Just'))
    )


# span :: (a -> Bool) -> [a] -> ([a], [a])
def span(p):
    '''The longest (possibly empty) prefix of xs
       that contains only elements satisfying p,
       tupled with the remainder of xs.
       span p xs is equivalent to (takeWhile p xs, dropWhile p xs).
    '''
    def go(xs):
        prefix = list(takewhile(p, xs))
        return (prefix, xs[len(prefix):])
    return lambda xs: go(xs)


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
# inconsistentChar :: String -> Maybe (Int, Char)
def inconsistentChar(s):
    '''Just the first inconsistent character and its index,
       or Nothing if all the characters of s are the same.
    '''
    return next(
        (Just(ix) for ix in enumerate(s) if s[0] != ix[1]),
        Nothing()
    )

```

