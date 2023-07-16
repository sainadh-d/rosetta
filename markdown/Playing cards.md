# Playing cards

## Task Link
[Rosetta Code - Playing cards](https://rosettacode.org/wiki/Playing_cards)

## Java Code
### java_code_1.txt
```java
public enum Pip { Two, Three, Four, Five, Six, Seven, 
    Eight, Nine, Ten, Jack, Queen, King, Ace }

```

### java_code_2.txt
```java
public enum Suit { Diamonds, Spades, Hearts, Clubs }

```

### java_code_3.txt
```java
public class Card {
    private final Suit suit;
    private final Pip value;

    public Card(Suit s, Pip v) {
        suit = s;
        value = v;
    }

    public String toString() {
        return value + " of " + suit;
    }
}

```

### java_code_4.txt
```java
import java.util.Collections;
import java.util.LinkedList;

public class Deck {
    private final LinkedList<Card> deck= new LinkedList<Card>();

    public Deck() {
        for (Suit s : Suit.values())
            for (Pip v : Pip.values())
                deck.add(new Card(s, v));
    }

    public Card deal() {
        return deck.poll();
    }

    public void shuffle() {
        Collections.shuffle(deck); // I'm such a cheater
    }

    public String toString(){
        return deck.toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

class Card(object):
    suits = ("Clubs","Hearts","Spades","Diamonds")
    pips = ("2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace")

    def __init__(self, pip,suit):
        self.pip=pip
        self.suit=suit

    def __str__(self):
        return "%s %s"%(self.pip,self.suit)

class Deck(object):
    def __init__(self):
        self.deck = [Card(pip,suit) for suit in Card.suits for pip in Card.pips]

    def __str__(self):
        return "[%s]"%", ".join( (str(card) for card in self.deck))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.shuffle()  # Can't tell what is next from self.deck
        return self.deck.pop(0)

```

### python_code_2.txt
```python
from pokerhand import Card, suit, face
from itertools import product
from random import randrange

class Deck():
    def __init__(self):
        self.__deck = [Card(f, s) for f,s in product(face, suit)]
    
    def __repr__(self):
        return 'Deck of ' + ' '.join(repr(card) for card in self.__deck)
    
    def shuffle(self):
        pass
    
    def deal(self):
        return self.__deck.pop(randrange(len(self.__deck)))

if __name__ == '__main__':
    deck = Deck()
    print('40 cards from a deck:\n')
    for i in range(5):
        for j in range(8):
            print(deck.deal(), end=' ')
        print()
    print('\nThe remaining cards are a', deck)

```

