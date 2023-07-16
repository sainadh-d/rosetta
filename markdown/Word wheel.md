# Word wheel

## Task Link
[Rosetta Code - Word wheel](https://rosettacode.org/wiki/Word_wheel)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.function.Predicate;

public final class WordWheel {

	public static void main(String[] args) throws IOException {
		String wordWheel = "N  D  E"
				         + "O  K  G"
				         + "E  L  W";		
		
		String allLetters = wordWheel.toLowerCase().replace(SPACE_CHARACTER, EMPTY_STRING);		
		String middleLetter = allLetters.substring(4, 5);
		
		Predicate<String> correctWords = word -> {
			if ( ! word.contains(middleLetter) || 3 > word.length() || word.length() > 9 ) {
				return false;
			}
						
			for ( String letter : allLetters.split(EMPTY_STRING) ) {
				word = word.replaceFirst(letter, EMPTY_STRING);
			}
			
			return word.isEmpty();
		};
		
		String url = "http://wiki.puzzlers.org/pub/wordlists/unixdict.txt";		
		InputStream stream = URI.create(url).toURL().openStream();
		BufferedReader reader = new BufferedReader( new InputStreamReader(stream) );
		reader.lines().filter(correctWords).forEach(System.out::println);
	}	
	
	private static final String EMPTY_STRING = "";
	private static final String SPACE_CHARACTER = " ";

}

```

## Python Code
### python_code_1.txt
```python
import urllib.request
from collections import Counter


GRID = """
N 	D 	E
O 	K 	G
E 	L 	W
"""


def getwords(url='http://wiki.puzzlers.org/pub/wordlists/unixdict.txt'):
    "Return lowercased words of 3 to 9 characters"
    words = urllib.request.urlopen(url).read().decode().strip().lower().split()
    return (w for w in words if 2 < len(w) < 10)

def solve(grid, dictionary):
    gridcount = Counter(grid)
    mid = grid[4]
    return [word for word in dictionary
            if mid in word and not (Counter(word) - gridcount)]


if __name__ == '__main__':
    chars = ''.join(GRID.strip().lower().split())
    found = solve(chars, dictionary=getwords())
    print('\n'.join(found))

```

### python_code_2.txt
```python
'''Word wheel'''

from os.path import expanduser


# gridWords :: [String] -> [String] -> [String]
def gridWords(grid):
    '''The subset of words in ws which contain the
       central letter of the grid, and can be completed
       by single uses of some or all of the remaining
       letters in the grid.
    '''
    def go(ws):
        cs = ''.join(grid).lower()
        wheel = sorted(cs)
        wset = set(wheel)
        mid = cs[4]
        return [
            w for w in ws
            if 2 < len(w) and (mid in w) and (
                all(c in wset for c in w)
            ) and wheelFit(wheel, w)
        ]
    return go


# wheelFit :: String -> String -> Bool
def wheelFit(wheel, word):
    '''True if a given word can be constructed
       from (single uses of) some subset of
       the letters in the wheel.
    '''
    def go(ws, cs):
        return True if not cs else (
            False if not ws else (
                go(ws[1:], cs[1:]) if ws[0] == cs[0] else (
                    go(ws[1:], cs)
                )
            )
        )
    return go(wheel, sorted(word))


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Word wheel matches for a given grid in a copy of
       http://wiki.puzzlers.org/pub/wordlists/unixdict.txt
    '''
    print('\n'.join(
        gridWords(['NDE', 'OKG', 'ELW'])(
            readFile('~/unixdict.txt').splitlines()
        )
    ))


# ------------------------ GENERIC -------------------------

# readFile :: FilePath -> IO String
def readFile(fp):
    '''The contents of any file at the path
       derived by expanding any ~ in fp.
    '''
    with open(expanduser(fp), 'r', encoding='utf-8') as f:
        return f.read()


# MAIN ---
if __name__ == '__main__':
    main()

```

