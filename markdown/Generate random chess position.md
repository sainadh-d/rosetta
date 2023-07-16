# Generate random chess position

## Task Link
[Rosetta Code - Generate random chess position](https://rosettacode.org/wiki/Generate_random_chess_position)

## Java Code
### java_code_1.txt
```java
import static java.lang.Math.abs;
import java.util.Random;

public class Fen {
    static Random rand = new Random();

    public static void main(String[] args) {
        System.out.println(createFen());
    }

    static String createFen() {
        char[][] grid = new char[8][8];

        placeKings(grid);
        placePieces(grid, "PPPPPPPP", true);
        placePieces(grid, "pppppppp", true);
        placePieces(grid, "RNBQBNR", false);
        placePieces(grid, "rnbqbnr", false);

        return toFen(grid);
    }

    static void placeKings(char[][] grid) {
        int r1, c1, r2, c2;
        while (true) {
            r1 = rand.nextInt(8);
            c1 = rand.nextInt(8);
            r2 = rand.nextInt(8);
            c2 = rand.nextInt(8);
            if (r1 != r2 && abs(r1 - r2) > 1 && abs(c1 - c2) > 1)
                break;
        }
        grid[r1][c1] = 'K';
        grid[r2][c2] = 'k';
    }

    static void placePieces(char[][] grid, String pieces, boolean isPawn) {
        int numToPlace = rand.nextInt(pieces.length());
        for (int n = 0; n < numToPlace; n++) {
            int r, c;
            do {
                r = rand.nextInt(8);
                c = rand.nextInt(8);

            } while (grid[r][c] != 0 || (isPawn && (r == 7 || r == 0)));

            grid[r][c] = pieces.charAt(n);
        }
    }

    static String toFen(char[][] grid) {
        StringBuilder fen = new StringBuilder();
        int countEmpty = 0;
        for (int r = 0; r < 8; r++) {
            for (int c = 0; c < 8; c++) {
                char ch = grid[r][c];
                System.out.printf("%2c ", ch == 0 ? '.' : ch);
                if (ch == 0) {
                    countEmpty++;
                } else {
                    if (countEmpty > 0) {
                        fen.append(countEmpty);
                        countEmpty = 0;
                    }
                    fen.append(ch);
                }
            }
            if (countEmpty > 0) {
                fen.append(countEmpty);
                countEmpty = 0;
            }
            fen.append("/");
            System.out.println();
        }
        return fen.append(" w - - 0 1").toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

board = [[" " for x in range(8)] for y in range(8)]
piece_list = ["R", "N", "B", "Q", "P"]


def place_kings(brd):
	while True:
		rank_white, file_white, rank_black, file_black = random.randint(0,7), random.randint(0,7), random.randint(0,7), random.randint(0,7)
		diff_list = [abs(rank_white - rank_black),  abs(file_white - file_black)]
		if sum(diff_list) > 2 or set(diff_list) == set([0, 2]):
			brd[rank_white][file_white], brd[rank_black][file_black] = "K", "k"
			break

def populate_board(brd, wp, bp):
	for x in range(2):
		if x == 0:
			piece_amount = wp
			pieces = piece_list
		else:
			piece_amount = bp
			pieces = [s.lower() for s in piece_list]
		while piece_amount != 0:
			piece_rank, piece_file = random.randint(0, 7), random.randint(0, 7)
			piece = random.choice(pieces)
			if brd[piece_rank][piece_file] == " " and pawn_on_promotion_square(piece, piece_rank) == False:
				brd[piece_rank][piece_file] = piece
				piece_amount -= 1

def fen_from_board(brd):
	fen = ""
	for x in brd:
		n = 0
		for y in x:
			if y == " ":
				n += 1
			else:
				if n != 0:
					fen += str(n)
				fen += y
				n = 0
		if n != 0:
			fen += str(n)
		fen += "/" if fen.count("/") < 7 else ""
	fen += " w - - 0 1\n"
	return fen

def pawn_on_promotion_square(pc, pr):
	if pc == "P" and pr == 0:
		return True
	elif pc == "p" and pr == 7:
		return True
	return False


def start():
	piece_amount_white, piece_amount_black = random.randint(0, 15), random.randint(0, 15)
	place_kings(board)
	populate_board(board, piece_amount_white, piece_amount_black)
	print(fen_from_board(board))
	for x in board:
		print(x)

#entry point
start()

```

