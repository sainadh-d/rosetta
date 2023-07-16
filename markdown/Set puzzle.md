# Set puzzle

## Task Link
[Rosetta Code - Set puzzle](https://rosettacode.org/wiki/Set_puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class SetPuzzle {

    enum Color {

        GREEN(0), PURPLE(1), RED(2);

        private Color(int v) {
            val = v;
        }
        public final int val;
    }

    enum Number {

        ONE(0), TWO(1), THREE(2);

        private Number(int v) {
            val = v;
        }
        public final int val;
    }

    enum Symbol {

        OVAL(0), DIAMOND(1), SQUIGGLE(2);

        private Symbol(int v) {
            val = v;
        }
        public final int val;
    }

    enum Fill {

        OPEN(0), STRIPED(1), SOLID(2);

        private Fill(int v) {
            val = v;
        }
        public final int val;
    }

    private static class Card implements Comparable<Card> {

        Color c;
        Number n;
        Symbol s;
        Fill f;

        @Override
        public String toString() {
            return String.format("[Card: %s, %s, %s, %s]", c, n, s, f);
        }

        @Override
        public int compareTo(Card o) {
            return (c.val - o.c.val) * 10 + (n.val - o.n.val);
        }
    }
    private static Card[] deck;

    public static void main(String[] args) {
        deck = new Card[81];
        Color[] colors = Color.values();
        Number[] numbers = Number.values();
        Symbol[] symbols = Symbol.values();
        Fill[] fillmodes = Fill.values();
        for (int i = 0; i < deck.length; i++) {
            deck[i] = new Card();
            deck[i].c = colors[i / 27];
            deck[i].n = numbers[(i / 9) % 3];
            deck[i].s = symbols[(i / 3) % 3];
            deck[i].f = fillmodes[i % 3];
        }
        findSets(12);
    }

    private static void findSets(int numCards) {
        int target = numCards / 2;
        Card[] cards;
        Card[][] sets = new Card[target][3];
        int cnt;
        do {
            Collections.shuffle(Arrays.asList(deck));
            cards = Arrays.copyOfRange(deck, 0, numCards);
            cnt = 0;

            outer:
            for (int i = 0; i < cards.length - 2; i++) {
                for (int j = i + 1; j < cards.length - 1; j++) {
                    for (int k = j + 1; k < cards.length; k++) {
                        if (validSet(cards[i], cards[j], cards[k])) {
                            if (cnt < target)
                                sets[cnt] = new Card[]{cards[i], cards[j], cards[k]};
                            if (++cnt > target) {
                                break outer;
                            }
                        }
                    }
                }
            }
        } while (cnt != target);

        Arrays.sort(cards);

        System.out.printf("GIVEN %d CARDS:\n\n", numCards);
        for (Card c : cards) {
            System.out.println(c);
        }
        System.out.println();

        System.out.println("FOUND " + target + " SETS:\n");
        for (Card[] set : sets) {
            for (Card c : set) {
                System.out.println(c);
            }
            System.out.println();
        }
    }

    private static boolean validSet(Card c1, Card c2, Card c3) {
        int tot = 0;
        tot += (c1.c.val + c2.c.val + c3.c.val) % 3;
        tot += (c1.n.val + c2.n.val + c3.n.val) % 3;
        tot += (c1.s.val + c2.s.val + c3.s.val) % 3;
        tot += (c1.f.val + c2.f.val + c3.f.val) % 3;
        return tot == 0;
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python
    
from itertools import product, combinations
from random import sample
 
## Major constants
features = [ 'green purple red'.split(),
             'one two three'.split(),
             'oval diamond squiggle'.split(),
             'open striped solid'.split() ]
             
deck = list(product(list(range(3)), repeat=4))

dealt = 9
 
## Functions
def printcard(card):
    print(' '.join('%8s' % f[i] for f,i in zip(features, card)))
 
def getdeal(dealt=dealt):
    deal = sample(deck, dealt)
    return deal
 
def getsets(deal):
    good_feature_count = set([1, 3])
    sets = [ comb for comb in combinations(deal, 3)
             if all( [(len(set(feature)) in good_feature_count)
                     for feature in zip(*comb)]
                   ) ]
    return sets
 
def printit(deal, sets):
    print('Dealt %i cards:' % len(deal))
    for card in deal: printcard(card)
    print('\nFound %i sets:' % len(sets))
    for s in sets:
        for card in s: printcard(card)
        print('')
 
if __name__ == '__main__':
    while True:
        deal = getdeal()
        sets = getsets(deal)
        if len(sets) == dealt / 2:
           break
    printit(deal, sets)

```

### python_code_2.txt
```python
import random, pprint
from itertools import product, combinations

N_DRAW = 9
N_GOAL = N_DRAW // 2

deck = list(product("red green purple".split(),
                    "one two three".split(),
                    "oval squiggle diamond".split(),
                    "solid open striped".split()))

sets = []
while len(sets) != N_GOAL:
    draw = random.sample(deck, N_DRAW)
    sets = [cs for cs in combinations(draw, 3)
            if all(len(set(t)) in [1, 3] for t in zip(*cs))]

print "Dealt %d cards:" % len(draw)
pprint.pprint(draw)
print "\nContaining %d sets:" % len(sets)
pprint.pprint(sets)

```

