# Find Chess960 starting position identifier

## Task Link
[Rosetta Code - Find Chess960 starting position identifier](https://rosettacode.org/wiki/Find_Chess960_starting_position_identifier)

## Java Code
### java_code_1.txt
```java
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.Predicate;

public final class Chess960SPID {

	public static void main(String[] aArgs) {
		String[] positions = { "QNRBBNKR", "RNBQKBNR", "RQNBBKRN", "RNQBBKRN" };
		
		createKnightsTable();
		
		for ( String position : positions ) {		
			validate("RQNBBKRN");
			System.out.println("Position " + position + " has Chess960 SP-ID = " + calculateSPID(position));
		}
	}
	
	private static void validate(String aPosition) {
		if ( aPosition.length() != 8 ) {
			throw new AssertionError("Chess position has invalid length: " + aPosition.length() + ".");
		}
		
		Map<Character, Integer> pieces = new HashMap<Character, Integer>();
		for ( char ch : aPosition.toCharArray() ) {
			pieces.merge(ch, 1, (oldV, newV) -> oldV + 1);
		}
		Set<Map.Entry<Character, Integer>> correctPieces =
			Set.of(Map.entry('R', 2), Map.entry('N', 2), Map.entry('B', 2), Map.entry('Q', 1), Map.entry('K', 1));
		if ( ! pieces.entrySet().equals(correctPieces) ) {
			throw new AssertionError("Chess position contains incorrect pieces.");
		}
		
		List<Integer> bishops = List.of(aPosition.indexOf('B'), aPosition.lastIndexOf('B'));
		if ( ( bishops.get(1) - bishops.get(0) ) % 2 == 0 ) {
			throw new AssertionError("Bishops must be on different coloured squares.");
		}
		
		List<Integer> rookKing = List.of(aPosition.indexOf('R'), aPosition.indexOf('K'), aPosition.lastIndexOf('R'));
		if ( ! ( rookKing.get(0) < rookKing.get(1) && rookKing.get(1) < rookKing.get(2) ) ) {
			throw new AssertionError("The king must be between the two rooks.");
		}
	}
	
	private static int calculateSPID(String aPosition) {
		String noBishopsOrQueen = retainIf(aPosition, s -> s != 'B' && s != 'Q');
		final int N = knightsTable.get(List.of(noBishopsOrQueen.indexOf('N'), noBishopsOrQueen.lastIndexOf('N')));
		
		String noBishops = retainIf(aPosition, s -> s != 'B');
		final int Q = noBishops.indexOf('Q');

		final int indexOne = aPosition.indexOf('B');
		final int indexTwo = aPosition.lastIndexOf('B');
		final int D = ( indexOne % 2 == 0 ) ? indexOne / 2 : indexTwo / 2;  
		final int L = ( indexOne % 2 == 0 ) ? indexTwo / 2 : indexOne / 2;  
		
		return 96 * N + 16 * Q + 4 * D + L;
	}
	
	private static String retainIf(String aText, Predicate<Character> aPredicate) {
		return aText.chars()
				    .mapToObj( i -> (char) i )
				    .filter(aPredicate)
				    .map(String::valueOf)
				    .reduce("", String::concat);
	}
	
	private static void createKnightsTable() {
		knightsTable = new HashMap<List<Integer>, Integer>();
		knightsTable.put(List.of(0, 1), 0);
		knightsTable.put(List.of(0, 2), 1);
		knightsTable.put(List.of(0, 3), 2);
		knightsTable.put(List.of(0, 4), 3);
		knightsTable.put(List.of(1, 2), 4);
		knightsTable.put(List.of(1, 3), 5);
		knightsTable.put(List.of(1, 4), 6);
		knightsTable.put(List.of(2, 3), 7);
		knightsTable.put(List.of(2, 4), 8);
		knightsTable.put(List.of(3, 4), 9);
	}	
	
	private static Map<List<Integer>, Integer> knightsTable;

}

```

## Python Code
### python_code_1.txt
```python
# optional, but task function depends on it as written
def validate_position(candidate: str):
    assert (
        len(candidate) == 8
    ), f"candidate position has invalide len = {len(candidate)}"

    valid_pieces = {"R": 2, "N": 2, "B": 2, "Q": 1, "K": 1}
    assert {
        piece for piece in candidate
    } == valid_pieces.keys(), f"candidate position contains invalid pieces"
    for piece_type in valid_pieces.keys():
        assert (
            candidate.count(piece_type) == valid_pieces[piece_type]
        ), f"piece type '{piece_type}' has invalid count"

    bishops_pos = [index for index, 
                   value in enumerate(candidate) if value == "B"]
    assert (
        bishops_pos[0] % 2 != bishops_pos[1] % 2
    ), f"candidate position has both bishops in the same color"

    assert [piece for piece in candidate if piece in "RK"] == [
        "R",
        "K",
        "R",
    ], "candidate position has K outside of RR"


def calc_position(start_pos: str):
    try:
        validate_position(start_pos)
    except AssertionError:
        raise AssertionError
    # step 1
    subset_step1 = [piece for piece in start_pos if piece not in "QB"]
    nights_positions = [
        index for index, value in enumerate(subset_step1) if value == "N"
    ]
    nights_table = {
        (0, 1): 0,
        (0, 2): 1,
        (0, 3): 2,
        (0, 4): 3,
        (1, 2): 4,
        (1, 3): 5,
        (1, 4): 6,
        (2, 3): 7,
        (2, 4): 8,
        (3, 4): 9,
    }
    N = nights_table.get(tuple(nights_positions))

    # step 2
    subset_step2 = [piece for piece in start_pos if piece != "B"]
    Q = subset_step2.index("Q")

    # step 3
    dark_squares = [
        piece for index, piece in enumerate(start_pos) if index in range(0, 9, 2)
    ]
    light_squares = [
        piece for index, piece in enumerate(start_pos) if index in range(1, 9, 2)
    ]
    D = dark_squares.index("B")
    L = light_squares.index("B")

    return 4 * (4 * (6*N + Q) + D) + L

if __name__ == '__main__':
    for example in ["QNRBBNKR", "RNBQKBNR", "RQNBBKRN", "RNQBBKRN"]:
        print(f'Position: {example}; Chess960 PID= {calc_position(example)}')

```

