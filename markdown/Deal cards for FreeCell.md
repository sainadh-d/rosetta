# Deal cards for FreeCell

## Task Link
[Rosetta Code - Deal cards for FreeCell](https://rosettacode.org/wiki/Deal_cards_for_FreeCell)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Shuffler {
	
	private int seed;
	
	private String[] deck = {
			"AC", "AD", "AH", "AS",
			"2C", "2D", "2H", "2S",
			"3C", "3D", "3H", "3S",
			"4C", "4D", "4H", "4S",
			"5C", "5D", "5H", "5S",
			"6C", "6D", "6H", "6S",
			"7C", "7D", "7H", "7S",
			"8C", "8D", "8H", "8S",
			"9C", "9D", "9H", "9S",
			"TC", "TD", "TH", "TS",
			"JC", "JD", "JH", "JS",
			"QC", "QD", "QH", "QS",
			"KC", "KD", "KH", "KS",
	};
	
	private int random() {
		seed = (214013 * seed + 2531011) & Integer.MAX_VALUE;
		return seed >> 16;
	}
	
	//shuffled cards go to the end
	private String[] getShuffledDeck() {
		String[] deck = Arrays.copyOf(this.deck, this.deck.length);
		for(int i = deck.length - 1; i > 0; i--) {
			int r = random() % (i + 1);
			String card = deck[r];
			deck[r] = deck[i];
			deck[i] = card;
		}
		return deck;
	}
	
	//deal from end first
	public void dealGame(int seed) {
		this.seed = seed;
		String[] shuffledDeck = getShuffledDeck();
		for(int count = 1, i = shuffledDeck.length - 1; i >= 0; count++, i--) {
			System.out.print(shuffledDeck[i]);
			if(count % 8 == 0) {
				System.out.println();
			} else {
				System.out.print(" ");
			}
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		Shuffler s = new Shuffler();
		s.dealGame(1);
		System.out.println();
		s.dealGame(617);
	}
	
}

```

## Python Code
### python_code_1.txt
```python
def randomGenerator(seed=1):
    max_int32 = (1 << 31) - 1
    seed = seed & max_int32

    while True:
        seed = (seed * 214013 + 2531011) & max_int32
        yield seed >> 16

def deal(seed):
    nc = 52
    cards = list(range(nc - 1, -1, -1))
    rnd = randomGenerator(seed)
    for i, r in zip(range(nc), rnd):
        j = (nc - 1) - r % (nc - i)
        cards[i], cards[j] = cards[j], cards[i]
    return cards

def show(cards):
    l = ["A23456789TJQK"[int(c/4)] + "CDHS"[c%4] for c in cards]
    for i in range(0, len(cards), 8):
        print(" ".join(l[i : i+8]))

if __name__ == '__main__':
    from sys import argv
    seed = int(argv[1]) if len(argv) == 2 else 11982
    print("Hand {}".format(seed))
    deck = deal(seed)
    show(deck)

```

