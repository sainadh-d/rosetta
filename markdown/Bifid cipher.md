# Bifid cipher

## Task Link
[Rosetta Code - Bifid cipher](https://rosettacode.org/wiki/Bifid_cipher)

## Java Code
### java_code_1.txt
```java
import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public final class BifidCipher {

	public static void main(String[] aArgs) {
		final String message1 = "ATTACKATDAWN";
		final String message2 = "FLEEATONCE";
		final String message3 = "The invasion will start on the first of January".toUpperCase().replace(" ", "");
		
		Bifid bifid1 = new Bifid(5, "ABCDEFGHIKLMNOPQRSTUVWXYZ");
		Bifid bifid2 = new Bifid(5, "BGWKZQPNDSIOAXEFCLUMTHYVR");
		
		runTest(bifid1, message1);
		runTest(bifid2, message2);
		runTest(bifid2, message1);
		runTest(bifid1, message2);
		
		Bifid bifid3 = new Bifid(6, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
		runTest(bifid3, message3);
	}	
	
	private static void runTest(Bifid aBifid, String aMessage) {
		System.out.println("Using Polybius square:");
		aBifid.display();
		System.out.println("Message:   " + aMessage);
		String encrypted = aBifid.encrypt(aMessage);
		System.out.println("Encrypted: " + encrypted);
		String decrypted = aBifid.decrypt(encrypted);
		System.out.println("Decrypted: " + decrypted);
		System.out.println();
	}	
	
}
	
final class Bifid {
	
	public Bifid(int aN, String aText) {
		if ( aText.length() != aN * aN ) {
			throw new IllegalArgumentException("Incorrect length of text");
		}
		
		grid = new char[aN][aN];			
		int row = 0;
		int col = 0;		 
		for ( char ch : aText.toCharArray() ) {
		    grid[row][col] = ch;
		    coordinates.put(ch, new Point(row, col) );
		    col += 1;
		    if ( col == aN ) {
		    	col = 0;
		    	row += 1;
		     }
		 }
		
		 if ( aN == 5 ) {
		     coordinates.put('J', coordinates.get('I'));
		 }
	}	
	
	public String encrypt(String aText) {		 
		List<Integer> rowOne = new ArrayList<Integer>();
		List<Integer> rowTwo = new ArrayList<Integer>();
		for ( char ch : aText.toCharArray() ) {
			Point coordinate = coordinates.get(ch);
			rowOne.add(coordinate.x);
			rowTwo.add(coordinate.y);
		 }
		  
		 rowOne.addAll(rowTwo);
		 StringBuilder result = new StringBuilder();
		 for ( int i = 0; i < rowOne.size() - 1; i += 2 ) {
			 result.append(grid[rowOne.get(i)][rowOne.get(i + 1)]);
		 }
		 return result.toString();
	}
	
	public String decrypt(String aText) {
		List<Integer> row = new ArrayList<Integer>();
		for ( char ch : aText.toCharArray() ) {
			Point coordinate = coordinates.get(ch);
		    row.add(coordinate.x);
		    row.add(coordinate.y);
		}
		
		final int middle = row.size() / 2;
		List<Integer> rowOne = row.subList(0, middle);
		List<Integer> rowTwo = row.subList(middle, row.size());
		StringBuilder result = new StringBuilder();
		for ( int i = 0; i < middle; i++ ) {
			result.append(grid[rowOne.get(i)][rowTwo.get(i)]);
		}
		return result.toString();
	}

    public void display() {
		Arrays.stream(grid).forEach( row -> System.out.println(Arrays.toString(row)) );
	}
	
	private char[][] grid;
	private Map<Character, Point> coordinates = new HashMap<Character, Point>();
	
}

```

## Python Code
### python_code_1.txt
```python
"""Bifid cipher. Requires Python >=3.7."""
import math
import pprint
import string

from itertools import chain
from itertools import zip_longest

from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import Tuple
from typing import TypeVar


T = TypeVar("T")


def group(it: Iterable[T], n: int) -> Iterator[Tuple[T, ...]]:
    """Return the input iterable split in to `n` equal chunks, padded with `None`."""
    return zip_longest(*[iter(it)] * n)


Square = Tuple[Tuple[str, ...], ...]


def polybius_square(alphabet: str) -> Square:
    """Return the given alphabet as a tuple of tuples, representing a Polybius square."""
    return tuple(group(alphabet, math.ceil(math.sqrt(len(alphabet)))))


def polybius_map(square: Square) -> Dict[str, Tuple[int, int]]:
    """Return a reverse lookup for the given Polybius square."""
    return {
        square[i][j]: (i + 1, j + 1)
        for i in range(len(square))
        for j in range(len(square))
    }


def encrypt(message: str, square: Square) -> str:
    """Encrypt a plaintext message using a bifid cipher with the given Polybius square."""
    _map = polybius_map(square)
    return "".join(
        square[x - 1][y - 1]
        for x, y in group(
            chain.from_iterable(zip(*(_map[c] for c in message if c in _map))),
            2,
        )
    )


def decrypt(message: str, square: Square) -> str:
    """Decrypt a ciphertext message using a bifid cipher with the given Polybius square."""
    _map = polybius_map(square)
    return "".join(
        square[x - 1][y - 1]
        for x, y in zip(
            *group(
                chain.from_iterable((_map[c] for c in message if c in _map)),
                len(message),
            )
        )
    )


def normalize(message: str) -> str:
    """Normalize a message for the typical Polybius square."""
    return message.upper().replace("J", "I")


TYPICAL_POLYBIUS_SQUARE = polybius_square(
    alphabet="".join(c for c in string.ascii_uppercase if c != "J")
)


EXAMPLE_POLYBIUS_SQUARE = polybius_square(
    alphabet="BGWKZQPNDSIOAXEFCLUMTHYVR",
)


def main() -> None:
    test_cases = [
        ("ATTACKATDAWN", TYPICAL_POLYBIUS_SQUARE),  # 1
        ("FLEEATONCE", EXAMPLE_POLYBIUS_SQUARE),  # 2
        ("FLEEATONCE", TYPICAL_POLYBIUS_SQUARE),  # 3
        (
            normalize("The invasion will start on the first of January"),
            polybius_square(alphabet="PLAYFIREXMBCDGHKNOQSTUVWZ"),
        ),
        (
            "The invasion will start on the first of January".upper(),
            polybius_square(alphabet=string.ascii_uppercase + string.digits),
        ),
    ]

    for message, square in test_cases:
        pprint.pprint(square)
        print("Message  :", message)
        print("Encrypted:", encrypt(message, square))
        print("Decrypted:", decrypt(encrypt(message, square), square))
        print("")


if __name__ == "__main__":
    main()

```

