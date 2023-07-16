# War card game

## Task Link
[Rosetta Code - War card game](https://rosettacode.org/wiki/War_card_game)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public final class WarCardGame {

	public static void main(String[] args) {
		WarGame warGame = new WarGame();
		
		while ( ! warGame.gameOver() ) {
			warGame.nextTurn();
		}
		
		warGame.declareWinner();
	}	
	
}

final class WarGame {
	
	public WarGame() {
		deck = new ArrayList<Card>(52);	    
        for ( Character suit : SUITS ) {
            for ( Character pip : PIPS ) {
                deck.add( new Card(suit, pip) );
            }
        }
        Collections.shuffle(deck);
        
        handA = new ArrayList<Card>(deck.subList(0, 26));
        handB = new ArrayList<Card>(deck.subList(26, 52));
        tabledCards = new ArrayList<Card>();        
	}
	
	public void nextTurn() {
		Card cardA = handA.remove(0);
		Card cardB = handB.remove(0);
		tabledCards.add(cardA);
		tabledCards.add(cardB);
		int rankA = PIPS.indexOf(cardA.pip);
		int rankB = PIPS.indexOf(cardB.pip);
		
		System.out.print(cardA + "  " + cardB);
		if ( rankA > rankB ) {
            System.out.println("  Player A takes the cards");
            Collections.shuffle(tabledCards);
            handA.addAll(tabledCards);
            tabledCards.clear();
		} else if ( rankA < rankB ) {
            System.out.println("  Player B takes the cards");
            Collections.shuffle(tabledCards);
            handB.addAll(tabledCards);
            tabledCards.clear();
		} else {
	        System.out.println("      War!");
            if ( gameOver() ) {
                return;
            }
            
            Card cardAA = handA.remove(0);
            Card cardBB = handB.remove(0);
            tabledCards.add(cardAA);
    		tabledCards.add(cardBB);
    		System.out.println("?   ?   Cards are face down");    		
    		if ( gameOver() ) {
                return;
            }
    		
            nextTurn();
		}
	}
	
	public boolean gameOver() {
		return handA.size() == 0 || handB.size() == 0;
	}
    
    public void declareWinner() {    	
        if ( handA.size() == 0 && handB.size() == 0 ) {
        	System.out.println("The game ended in a tie");
        } else if ( handA.size() == 0 ) {
        	System.out.println("Player B has won the game");
        } else {
            System.out.println("Player A has won the game");
        }
    }
    
    private record Card(Character suit, Character pip) {
    	
    	@Override
    	public String toString() {
    		return "" + pip + suit;
    	}
    	
    }
	
	private List<Card> deck, handA, handB, tabledCards;
	
	private static final List<Character> PIPS = 
		Arrays.asList( '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' );
	private static final List<Character> SUITS = List.of( 'C', 'D', 'H', 'S' );
	
}

```

## Python Code
### python_code_1.txt
```python
""" https://bicyclecards.com/how-to-play/war/ """

from numpy.random import shuffle

SUITS = ['♣', '♦', '♥', '♠']
FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f + s for f in FACES for s in SUITS]
CARD_TO_RANK = dict((DECK[i], (i + 3) // 4) for i in range(len(DECK)))


class WarCardGame:
    """ card game War """
    def __init__(self):
        deck = DECK.copy()
        shuffle(deck)
        self.deck1, self.deck2 = deck[:26], deck[26:]
        self.pending = []

    def turn(self):
        """ one turn, may recurse on tie """
        if len(self.deck1) == 0 or len(self.deck2) == 0:
            return self.gameover()

        card1, card2 = self.deck1.pop(0), self.deck2.pop(0)
        rank1, rank2 = CARD_TO_RANK[card1], CARD_TO_RANK[card2]
        print("{:10}{:10}".format(card1, card2), end='')
        if rank1 > rank2:
            print('Player 1 takes the cards.')
            self.deck1.extend([card1, card2])
            self.deck1.extend(self.pending)
            self.pending = []
        elif rank1 < rank2:
            print('Player 2 takes the cards.')
            self.deck2.extend([card2, card1])
            self.deck2.extend(self.pending)
            self.pending = []
        else:  #  rank1 == rank2
            print('Tie!')
            if len(self.deck1) == 0 or len(self.deck2) == 0:
                return self.gameover()

            card3, card4 = self.deck1.pop(0), self.deck2.pop(0)
            self.pending.extend([card1, card2, card3, card4])
            print("{:10}{:10}".format("?", "?"), 'Cards are face down.', sep='')
            return self.turn()

        return True

    def gameover(self):
        """ game over who won message """
        if len(self.deck2) == 0:
            if len(self.deck1) == 0:
                print('\nGame ends as a tie.')
            else:
                print('\nPlayer 1 wins the game.')
        else:
            print('\nPlayer 2 wins the game.')

        return False


if __name__ == '__main__':
    WG = WarCardGame()
    while WG.turn():
        continue

```

