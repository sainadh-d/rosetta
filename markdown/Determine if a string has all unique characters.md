# Determine if a string has all unique characters

## Task Link
[Rosetta Code - Determine if a string has all unique characters](https://rosettacode.org/wiki/Determine_if_a_string_has_all_unique_characters)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.Map;

//  Title:  Determine if a string has all unique characters

public class StringUniqueCharacters {

    public static void main(String[] args) {
        System.out.printf("%-40s  %2s  %10s  %8s  %s  %s%n", "String", "Length", "All Unique", "1st Diff", "Hex", "Positions");
        System.out.printf("%-40s  %2s  %10s  %8s  %s  %s%n", "------------------------", "------", "----------", "--------", "---", "---------");
        for ( String s : new String[] {"", ".", "abcABC", "XYZ ZYX", "1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ"} ) {
            processString(s);
        }
    }
    
    
    
    private static void processString(String input) {
        Map<Character,Integer> charMap = new HashMap<>(); 
        char dup = 0;
        int index = 0;
        int pos1 = -1;
        int pos2 = -1;
        for ( char key : input.toCharArray() ) {
            index++;
            if ( charMap.containsKey(key) ) {
                dup = key;
                pos1 = charMap.get(key);
                pos2 = index;
                break;
            }
            charMap.put(key, index);
        }
        String unique = dup == 0 ? "yes" : "no";
        String diff = dup == 0 ? "" : "'" + dup + "'";
        String hex = dup == 0 ? "" : Integer.toHexString(dup).toUpperCase();
        String position = dup == 0 ? "" : pos1 + " " + pos2;
        System.out.printf("%-40s  %-6d  %-10s  %-8s  %-3s  %-5s%n", input, input.length(), unique, diff, hex, position);
    }

}

```

### java_code_2.txt
```java
import java.util.HashSet;
import java.util.List;
import java.util.OptionalInt;
import java.util.Set;

public final class DetermineUniqueCharacters {

	public static void main(String[] aArgs) {
		List<String> words = List.of( "", ".", "abcABC", "XYZ ZYX", "1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ" );
		
		for ( String word : words ) {		
			Set<Integer> seen = new HashSet<Integer>();
	        OptionalInt first = word.chars().filter( ch -> ! seen.add(ch) ).findFirst();
	        if ( first.isPresent() ) {	            
	            final char ch = (char) first.getAsInt();
	            final String hex = Integer.toHexString(ch).toUpperCase();
	            System.out.println("Word: \"" + word + "\" contains a repeated character.");
	            System.out.println("Character '" + ch + "' (hex " + hex + ") occurs at positions "
	            	+ word.indexOf(ch) + " and " + word.indexOf(ch, word.indexOf(ch) + 1));
	        } else {
	        	System.out.println("Word: \"" + word + "\" has all unique characters.");
	        }
	        System.out.println();			
		}
	}

}

```

## Python Code
### python_code_1.txt
```python
'''Determine if a string has all unique characters'''

from itertools import groupby


# duplicatedCharIndices :: String -> Maybe (Char, [Int])
def duplicatedCharIndices(s):
    '''Just the first duplicated character, and
       the indices of its occurrence, or
       Nothing if there are no duplications.
    '''
    def go(xs):
        if 1 < len(xs):
            duplicates = list(filter(lambda kv: 1 < len(kv[1]), [
                (k, list(v)) for k, v in groupby(
                    sorted(xs, key=swap),
                    key=snd
                )
            ]))
            return Just(second(fmap(fst))(
                sorted(
                    duplicates,
                    key=lambda kv: kv[1][0]
                )[0]
            )) if duplicates else Nothing()
        else:
            return Nothing()
    return go(list(enumerate(s)))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test over various strings.'''

    def showSample(s):
        return repr(s) + ' (' + str(len(s)) + ')'

    def showDuplicate(cix):
        c, ix = cix
        return repr(c) + (
            ' (' + hex(ord(c)) + ') at ' + repr(ix)
        )

    print(
        fTable('First duplicated character, if any:')(
            showSample
        )(maybe('None')(showDuplicate))(duplicatedCharIndices)([
            '', '.', 'abcABC', 'XYZ ZYX',
            '1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ'
        ])
    )


# FORMATTING ----------------------------------------------

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


# GENERIC -------------------------------------------------

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


# fmap :: (a -> b) -> [a] -> [b]
def fmap(f):
    '''fmap over a list.
       f lifted to a function over a list.
    '''
    return lambda xs: [f(x) for x in xs]


# fst :: (a, b) -> a
def fst(tpl):
    '''First member of a pair.'''
    return tpl[0]


# head :: [a] -> a
def head(xs):
    '''The first element of a non-empty list.'''
    return xs[0] if isinstance(xs, list) else next(xs)


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if (
        None is m or m.get('Nothing')
    ) else f(m.get('Just'))


# second :: (a -> b) -> ((c, a) -> (c, b))
def second(f):
    '''A simple function lifted to a function over a tuple,
       with f applied only to the second of two values.
    '''
    return lambda xy: (xy[0], f(xy[1]))


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# swap :: (a, b) -> (b, a)
def swap(tpl):
    '''The swapped components of a pair.'''
    return (tpl[1], tpl[0])


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
'''Determine if a string has all unique characters'''

from functools import reduce


# duplicatedCharIndices :: String -> Maybe (Char, [Int])
def duplicatedCharIndices(s):
    '''Just the first duplicated character, and
       the indices of its occurrence, or
       Nothing if there are no duplications.
    '''
    def go(dct, ic):
        i, c = ic
        return dict(
            dct,
            **{c: dct[c] + [i] if c in dct else [i]}
        )
    duplicates = [
        (k, v) for (k, v)
        in reduce(go, enumerate(s), {}).items()
        if 1 < len(v)
    ]
    return Just(
        min(duplicates, key=compose(head, snd))
    ) if duplicates else Nothing()


# And another alternative here would be to fuse the 1 < len(v)
# filtering, and the min() search for the earliest duplicate,
# down to a single `earliestDuplication` fold:

# duplicatedCharIndices_ :: String -> Maybe (Char, [Int])
def duplicatedCharIndices_(s):
    '''Just the first duplicated character, and
       the indices of its occurrence, or
       Nothing if there are no duplications.
    '''
    def positionRecord(dct, ic):
        i, c = ic
        return dict(
            dct,
            **{c: dct[c] + [i] if c in dct else [i]}
        )

    def earliestDuplication(sofar, charPosns):
        c, indices = charPosns
        return (
            maybe(Just((c, indices)))(
                lambda kxs: Just((c, indices)) if (
                    # Earlier duplication ?
                    indices[0] < kxs[1][0]
                ) else sofar
            )(sofar)
        ) if 1 < len(indices) else sofar

    return reduce(
        earliestDuplication,
        reduce(
            positionRecord,
            enumerate(s),
            {}
        ).items(),
        Nothing()
    )


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Test over various strings.'''

    def showSample(s):
        return repr(s) + ' (' + str(len(s)) + ')'

    def showDuplicate(cix):
        c, ix = cix
        return repr(c) + (
            ' (' + hex(ord(c)) + ') at ' + repr(ix)
        )

    print(
        fTable('First duplicated character, if any:')(
            showSample
        )(maybe('None')(showDuplicate))(duplicatedCharIndices_)([
            '', '.', 'abcABC', 'XYZ ZYX',
            '1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ'
        ])
    )


# FORMATTING ----------------------------------------------

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


# GENERIC -------------------------------------------------

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


# compose :: ((a -> a), ...) -> (a -> a)
def compose(*fs):
    '''Composition, from right to left,
       of a series of functions.
    '''
    return lambda x: reduce(
        lambda a, f: f(a),
        fs[::-1], x
    )


# head :: [a] -> a
def head(xs):
    '''The first element of a non-empty list.'''
    return xs[0] if isinstance(xs, list) else next(xs)


# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(v):
    '''Either the default value v, if m is Nothing,
       or the application of f to x,
       where m is Just(x).
    '''
    return lambda f: lambda m: v if (
        None is m or m.get('Nothing')
    ) else f(m.get('Just'))


# snd :: (a, b) -> b
def snd(tpl):
    '''Second member of a pair.'''
    return tpl[1]


# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
import re

pattern = '(.)' + '.*?' + r'\1'

def find_dup_char(subject):
    match = re.search(pattern, subject)
    if match:
        return match.groups(0)[0], match.start(0), match.end(0)

def report_dup_char(subject):
    dup = find_dup_char(subject)
    prefix = f'"{subject}" ({len(subject)})'
    if dup:
        ch, pos1, pos2 = dup
        print(f"{prefix}: '{ch}' (0x{ord(ch):02x}) duplicates at {pos1}, {pos2-1}")
    else:
        print(f"{prefix}: no duplicate characters")

show = report_dup_char
show('coccyx')
show('')
show('.')
show('abcABC')
show('XYZ ZYX')
show('1234567890ABCDEFGHIJKLMN0PQRSTUVWXYZ')

```

