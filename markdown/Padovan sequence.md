# Padovan sequence

## Task Link
[Rosetta Code - Padovan sequence](https://rosettacode.org/wiki/Padovan_sequence)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public final class Padovan {

	public static void main(String[] aArgs) {
		for ( int i = 0; i < 64; i++ ) {
			recurrences.add(padovanRecurrence(i));
			floors.add(padovanFloor(i));
		}		
		
		System.out.println("The first 20 terms of the Padovan sequence:");
		recurrences.subList(0, 20).forEach( term -> System.out.print(term + " ") );		
		System.out.println(System.lineSeparator());
		
		System.out.print("Recurrence and floor functions agree for first 64 terms? " + recurrences.equals(floors));
		System.out.println(System.lineSeparator());
		
		List<String> words = createLSystem();		
		
		System.out.println("The first 10 terms of the L-system:");
		words.subList(0, 10).forEach( term -> System.out.print(term + " ") );		
		System.out.println(System.lineSeparator());
		
		System.out.print("Length of first 32 terms produced from the L-system match Padovan sequence? ");		
		List<Integer> wordLengths = words.stream().map( s -> s.length() ).toList();
		System.out.println(wordLengths.equals(recurrences.subList(0, 32)));
	}
	
	private static int padovanRecurrence(int aN) {
		return ( aN <= 2 ) ? 1 : recurrences.get(aN - 2) + recurrences.get(aN - 3);		
	}
	
	private static int padovanFloor(int aN) {
		return (int) Math.floor(Math.pow(PP, aN - 1) / SS + 0.5);
	}
	
	private static List<String> createLSystem() {
		List<String> words = new ArrayList<String>();		
		StringBuilder stringBuilder = new StringBuilder();
		String text = "A";
		
		do {
			words.add(text);
			stringBuilder.setLength(0);
			for ( char ch : text.toCharArray() ) {
				String entry = switch ( ch ) {
					case 'A' -> "B";
					case 'B' -> "C";
					case 'C' -> "AB";
					default -> throw new AssertionError("Unexpected character found: " + ch);
				};
				
				stringBuilder.append(entry);
			}
			
			text = stringBuilder.toString();
		} while ( words.size() < 32 );
		
		return words;
	}
	
	private static List<Integer> recurrences = new ArrayList<Integer>();
	private static List<Integer> floors = new ArrayList<Integer>();
	
	private static final double PP = 1.324717957244746025960908854;
	private static final double SS = 1.0453567932525329623;

}

```

## Python Code
### python_code_1.txt
```python
from math import floor
from collections import deque
from typing import Dict, Generator


def padovan_r() -> Generator[int, None, None]:
    last = deque([1, 1, 1], 4)
    while True:
        last.append(last[-2] + last[-3])
        yield last.popleft()

_p, _s = 1.324717957244746025960908854, 1.0453567932525329623

def padovan_f(n: int) -> int:
    return floor(_p**(n-1) / _s + .5)

def padovan_l(start: str='A',
             rules: Dict[str, str]=dict(A='B', B='C', C='AB')
             ) -> Generator[str, None, None]:
    axiom = start
    while True:
        yield axiom
        axiom = ''.join(rules[ch] for ch in axiom)


if __name__ == "__main__":
    from itertools import islice

    print("The first twenty terms of the sequence.")
    print(str([padovan_f(n) for n in range(20)])[1:-1])

    r_generator = padovan_r()
    if all(next(r_generator) == padovan_f(n) for n in range(64)):
        print("\nThe recurrence and floor based algorithms match to n=63 .")
    else:
        print("\nThe recurrence and floor based algorithms DIFFER!")

    print("\nThe first 10 L-system string-lengths and strings")
    l_generator = padovan_l(start='A', rules=dict(A='B', B='C', C='AB'))
    print('\n'.join(f"  {len(string):3} {repr(string)}"
                    for string in islice(l_generator, 10)))

    r_generator = padovan_r()
    l_generator = padovan_l(start='A', rules=dict(A='B', B='C', C='AB'))
    if all(len(next(l_generator)) == padovan_f(n) == next(r_generator)
           for n in range(32)):
        print("\nThe L-system, recurrence and floor based algorithms match to n=31 .")
    else:
        print("\nThe L-system, recurrence and floor based algorithms DIFFER!")

```

### python_code_2.txt
```python
'''Padovan series'''

from itertools import chain, islice
from math import floor
from operator import eq


# padovans :: [Int]
def padovans():
    '''Non-finite series of Padovan numbers,
       defined in terms of recurrence relations.
    '''
    def recurrence(abc):
        a, b, c = abc
        return a, (b, c, a + b)

    return unfoldr(recurrence)(
        (1, 1, 1)
    )


# padovanFloor :: [Int]
def padovanFloor():
    '''The Padovan series, defined in terms
       of a floor function.
    '''
    p = 1.324717957244746025960908854
    s = 1.0453567932525329623

    def f(n):
        return floor(p ** (n - 1) / s + 0.5), 1 + n

    return unfoldr(f)(0)


# padovanLSystem : [Int]
def padovanLSystem():
    '''An L-system generating terms whose lengths
       are the values of the Padovan integer series.
    '''
    def rule(c):
        return 'B' if 'A' == c else (
            'C' if 'B' == c else 'AB'
        )

    def f(s):
        return s, ''.join(list(concatMap(rule)(s)))

    return unfoldr(f)('A')


# ------------------------- TEST -------------------------

# prefixesMatch :: [a] -> [a] -> Bool
def prefixesMatch(xs, ys, n):
    '''True if the first n items of each
       series are the same.
    '''
    return all(map(eq, take(n)(xs), ys))


# main :: IO ()
def main():
    '''Test three Padovan functions for
       equivalence and expected results.
    '''
    print('\n'.join([
        "First 20 padovans:\n",
        repr(take(20)(padovans())),

        "\nThe recurrence and floor-based functions" + (
            " match over 64 terms:\n"
        ),
        repr(prefixesMatch(
            padovans(),
            padovanFloor(),
            64
        )),

        "\nFirst 10 L-System strings:\n",
        repr(take(10)(padovanLSystem())),

        "\nThe lengths of the first 32 L-System strings",
        "match the Padovan sequence:\n",
        repr(prefixesMatch(
            padovans(),
            (len(x) for x in padovanLSystem()),
            32
        ))
    ]))


# ----------------------- GENERIC ------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated map'''
    def go(xs):
        return chain.from_iterable(map(f, xs))
    return go


# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''A lazy (generator) list unfolded from a seed value
       by repeated application of f until no residue remains.
       Dual to fold/reduce.
       f returns either None, or just (value, residue).
       For a strict output list, wrap the result with list()
    '''
    def go(x):
        valueResidue = f(x)
        while None is not valueResidue:
            yield valueResidue[0]
            valueResidue = f(valueResidue[1])
    return go


# take :: Int -> [a] -> [a]
# take :: Int -> String -> String
def take(n):
    '''The prefix of xs of length n,
       or xs itself if n > length xs.
    '''
    def go(xs):
        return (
            xs[0:n]
            if isinstance(xs, (list, tuple))
            else list(islice(xs, n))
        )
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

