# Phrase reversals

## Task Link
[Rosetta Code - Phrase reversals](https://rosettacode.org/wiki/Phrase_reversals)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class PhraseRev{
	private static String reverse(String x){
		return new StringBuilder(x).reverse().toString();
	}
	
	private static <T> T[] reverse(T[] x){
		T[] rev = Arrays.copyOf(x, x.length);
		for(int i = x.length - 1; i >= 0; i--){
			rev[x.length - 1 - i] = x[i];
		}
		return rev;
	}
	
	private static String join(String[] arr, String joinStr){
		StringBuilder joined = new StringBuilder();
		for(int i = 0; i < arr.length; i++){
			joined.append(arr[i]);
			if(i < arr.length - 1) joined.append(joinStr);
		}
		return joined.toString();
	}
	
	public static void main(String[] args){
		String str = "rosetta code phrase reversal";
		
		System.out.println("Straight-up reversed: " + reverse(str));
		String[] words = str.split(" ");
		for(int i = 0; i < words.length; i++){
			words[i] = reverse(words[i]);
		}
		System.out.println("Reversed words: " + join(words, " "));
		System.out.println("Reversed word order: " + join(reverse(str.split(" ")), " "));
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> phrase = "rosetta code phrase reversal"
>>> phrase[::-1]					  # Reversed.
'lasrever esarhp edoc attesor'
>>> ' '.join(word[::-1] for word in phrase.split())	  # Words reversed.
'attesor edoc esarhp lasrever'
>>> ' '.join(phrase.split()[::-1])	                  # Word order reversed.
'reversal phrase code rosetta'
>>>

```

### python_code_2.txt
```python
'''String reversals at different levels.'''


# reversedCharacters :: String -> String
def reversedCharacters(s):
    '''All characters in reversed sequence.'''
    return reverse(s)


# wordsWithReversedCharacters :: String -> String
def wordsWithReversedCharacters(s):
    '''Characters within each word in reversed sequence.'''
    return unwords(map(reverse, words(s)))


# reversedWordOrder :: String -> String
def reversedWordOrder(s):
    '''Sequence of words reversed.'''
    return unwords(reverse(words(s)))


# TESTS -------------------------------------------------
# main :: IO()
def main():
    '''Tests'''

    s = 'rosetta code phrase reversal'
    print(
        tabulated(s + ':\n')(
            lambda f: f.__name__
        )(lambda s: "'" + s + "'")(
            lambda f: f(s)
        )([
            reversedCharacters,
            wordsWithReversedCharacters,
            reversedWordOrder
        ])
    )


# GENERIC -------------------------------------------------


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


# reverse :: [a] -> [a]
# reverse :: String -> String
def reverse(xs):
    '''The elements of xs in reverse order.'''
    return xs[::-1] if isinstance(xs, str) else (
        list(reversed(xs))
    )


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
                f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join(
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# unwords :: [String] -> String
def unwords(xs):
    '''A space-separated string derived from a list of words.'''
    return ' '.join(xs)


# words :: String -> [String]
def words(s):
    '''A list of words delimited by characters
       representing white space.'''
    return s.split()


if __name__ == '__main__':
    main()

```

