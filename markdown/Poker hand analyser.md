# Poker hand analyser

## Task Link
[Rosetta Code - Poker hand analyser](https://rosettacode.org/wiki/Poker_hand_analyser)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;

public class PokerHandAnalyzer {

    final static String faces = "AKQJT98765432";
    final static String suits = "HDSC";
    final static String[] deck = buildDeck();

    public static void main(String[] args) {
        System.out.println("Regular hands:\n");
        for (String input : new String[]{"2H 2D 2S KS QD",
            "2H 5H 7D 8S 9D",
            "AH 2D 3S 4S 5S",
            "2H 3H 2D 3S 3D",
            "2H 7H 2D 3S 3D",
            "2H 7H 7D 7S 7C",
            "TH JH QH KH AH",
            "4H 4C KC 5D TC",
            "QC TC 7C 6C 4C",
            "QC TC 7C 7C TD"}) {
            System.out.println(analyzeHand(input.split(" ")));
        }

        System.out.println("\nHands with wildcards:\n");
        for (String input : new String[]{"2H 2D 2S KS WW",
            "2H 5H 7D 8S WW",
            "AH 2D 3S 4S WW",
            "2H 3H 2D 3S WW",
            "2H 7H 2D 3S WW",
            "2H 7H 7D WW WW",
            "TH JH QH WW WW",
            "4H 4C KC WW WW",
            "QC TC 7C WW WW",
            "QC TC 7H WW WW"}) {
            System.out.println(analyzeHandWithWildcards(input.split(" ")));
        }
    }

    private static Score analyzeHand(final String[] hand) {
        if (hand.length != 5)
            return new Score("invalid hand: wrong number of cards", -1, hand);

        if (new HashSet<>(Arrays.asList(hand)).size() != hand.length)
            return new Score("invalid hand: duplicates", -1, hand);

        int[] faceCount = new int[faces.length()];
        long straight = 0, flush = 0;
        for (String card : hand) {

            int face = faces.indexOf(card.charAt(0));
            if (face == -1)
                return new Score("invalid hand: non existing face", -1, hand);
            straight |= (1 << face);

            faceCount[face]++;

            if (suits.indexOf(card.charAt(1)) == -1)
                return new Score("invalid hand: non-existing suit", -1, hand);
            flush |= (1 << card.charAt(1));
        }

        // shift the bit pattern to the right as far as possible
        while (straight % 2 == 0)
            straight >>= 1;

        // straight is 00011111; A-2-3-4-5 is 1111000000001
        boolean hasStraight = straight == 0b11111 || straight == 0b1111000000001;

        // unsets right-most 1-bit, which may be the only one set
        boolean hasFlush = (flush & (flush - 1)) == 0;

        if (hasStraight && hasFlush)
            return new Score("straight-flush", 9, hand);

        int total = 0;
        for (int count : faceCount) {
            if (count == 4)
                return new Score("four-of-a-kind", 8, hand);
            if (count == 3)
                total += 3;
            else if (count == 2)
                total += 2;
        }

        if (total == 5)
            return new Score("full-house", 7, hand);

        if (hasFlush)
            return new Score("flush", 6, hand);

        if (hasStraight)
            return new Score("straight", 5, hand);

        if (total == 3)
            return new Score("three-of-a-kind", 4, hand);

        if (total == 4)
            return new Score("two-pair", 3, hand);

        if (total == 2)
            return new Score("one-pair", 2, hand);

        return new Score("high-card", 1, hand);
    }

    private static WildScore analyzeHandWithWildcards(String[] hand) {
        if (Collections.frequency(Arrays.asList(hand), "WW") > 2)
            throw new IllegalArgumentException("too many wildcards");

        return new WildScore(analyzeHandWithWildcardsR(hand, null), hand.clone());
    }

    private static Score analyzeHandWithWildcardsR(String[] hand,
            Score best) {

        for (int i = 0; i < hand.length; i++) {
            if (hand[i].equals("WW")) {
                for (String card : deck) {
                    if (!Arrays.asList(hand).contains(card)) {
                        hand[i] = card;
                        best = analyzeHandWithWildcardsR(hand, best);
                    }
                }
                hand[i] = "WW";
                break;
            }
        }
        Score result = analyzeHand(hand);
        if (best == null || result.weight > best.weight)
            best = result;
        return best;
    }

    private static String[] buildDeck() {
        String[] dck = new String[suits.length() * faces.length()];
        int i = 0;
        for (char s : suits.toCharArray()) {
            for (char f : faces.toCharArray()) {
                dck[i] = "" + f + s;
                i++;
            }
        }
        return dck;
    }

    private static class Score {
        final int weight;
        final String name;
        final String[] hand;

        Score(String n, int w, String[] h) {
            weight = w;
            name = n;
            hand = h != null ? h.clone() : h;
        }

        @Override
        public String toString() {
            return Arrays.toString(hand) + " " + name;
        }
    }

    private static class WildScore {
        final String[] wild;
        final Score score;

        WildScore(Score s, String[] w) {
            score = s;
            wild = w;
        }

        @Override
        public String toString() {
            return String.format("%s%n%s%n", Arrays.toString(wild),
                    score.toString());
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
:- initialization(main).


faces([a,k,q,j,10,9,8,7,6,5,4,3,2]).

face(F) :- faces(Fs), member(F,Fs).
suit(S) :- member(S, ['♥','♦','♣','♠']).


best_hand(Cards,H) :-
    straight_flush(Cards,C) -> H = straight-flush(C)
  ; many_kind(Cards,F,4)    -> H = four-of-a-kind(F)
  ; full_house(Cards,F1,F2) -> H = full-house(F1,F2)
  ; flush(Cards,S)          -> H = flush(S)
  ; straight(Cards,F)       -> H = straight(F)
  ; many_kind(Cards,F,3)    -> H = three-of-a-kind(F)
  ; two_pair(Cards,F1,F2)   -> H = two-pair(F1,F2)
  ; many_kind(Cards,F,2)    -> H = one-pair(F)
  ; many_kind(Cards,F,1)    -> H = high-card(F)
  ;                            H = invalid
  .

straight_flush(Cards, c(F,S)) :- straight(Cards,F), flush(Cards,S).

full_house(Cards,F1,F2) :-
    many_kind(Cards,F1,3), many_kind(Cards,F2,2), F1 \= F2.

flush(Cards,S) :- maplist(has_suit(S), Cards).
has_suit(S, c(_,S)).

straight(Cards,F) :-
    select(c(F,_), Cards, Cs), pred_face(F,F1), straight(Cs,F1).
straight([],_).
pred_face(F,F1) :- F = 2 -> F1 = a ; faces(Fs), append(_, [F,F1|_], Fs).

two_pair(Cards,F1,F2) :-
    many_kind(Cards,F1,2), many_kind(Cards,F2,2), F1 \= F2.

many_kind(Cards,F,N) :-
    face(F), findall(_, member(c(F,_), Cards), Xs), length(Xs,N).


% utils/parser
parse_line(Cards)  --> " ", parse_line(Cards).
parse_line([C|Cs]) --> parse_card(C), parse_line(Cs).
parse_line([])     --> [].

parse_card(c(F,S)) --> parse_face(F), parse_suit(S).

parse_suit(S,In,Out) :- suit(S), atom_codes(S,Xs), append(Xs,Out,In).
parse_face(F,In,Out) :- face(F), face_codes(F,Xs), append(Xs,Out,In).

face_codes(F,Xs) :- number(F) -> number_codes(F,Xs) ; atom_codes(F,Xs).


% tests
test(" 2♥  2♦ 2♣ k♣  q♦").
test(" 2♥  5♥ 7♦ 8♣  9♠").
test(" a♥  2♦ 3♣ 4♣  5♦").
test(" 2♥  3♥ 2♦ 3♣  3♦").
test(" 2♥  7♥ 2♦ 3♣  3♦").
test(" 2♥  7♥ 7♦ 7♣  7♠").
test("10♥  j♥ q♥ k♥  a♥").
test(" 4♥  4♠ k♠ 5♦ 10♠").
test(" q♣ 10♣ 7♣ 6♣  4♣").

run_tests :-
    test(Line), phrase(parse_line(Cards), Line), best_hand(Cards,H)
  , write(Cards), write('\t'), write(H), nl
  .
main :- findall(_, run_tests, _), halt.

```

### python_code_2.txt
```python
from collections import namedtuple

class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)


suit = '♥ ♦ ♣ ♠'.split()
# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 10 j q k a'
lowaces = 'a 2 3 4 5 6 7 8 9 10 j q k'
# faces as lists
face   = faces.split()
lowace = lowaces.split()


def straightflush(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'straight-flush', ordered[-1].face
    return False

def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return 'four-of-a-kind', [f, allftypes.pop()]
    else:
        return False

def fullhouse(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return 'full-house', [f, allftypes.pop()]
    else:
        return False

def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return 'flush', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)
    return False

def straight(hand):
    f,fs = ( (lowace, lowaces) if any(card.face == '2' for card in hand)
             else (face, faces) )
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return 'straight', ordered[-1].face
    return False

def threeofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) <= 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 3:
            allftypes.remove(f)
            return ('three-of-a-kind', [f] +
                     sorted(allftypes,
                            key=lambda f: face.index(f),
                            reverse=True))
    else:
        return False

def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return 'two-pair', pairs + other if face.index(p0) > face.index(p1) else pairs[::-1] + other

def onepair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return 'one-pair', pairs + sorted(allftypes,
                                      key=lambda f: face.index(f),
                                      reverse=True)

def highcard(hand):
    allfaces = [f for f,s in hand]
    return 'high-card', sorted(allfaces,
                               key=lambda f: face.index(f),
                               reverse=True)

handrankorder =  (straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)
              
def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        rank = ranker(hand)
        if rank:
            break
    assert rank, "Invalid: Failed to rank cards: %r" % cards
    return rank

def handy(cards='2♥ 2♦ 2♣ k♣ q♦'):
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        assert f in face, "Invalid: Don't understand card face %r" % f
        assert s in suit, "Invalid: Don't understand card suit %r" % s
        hand.append(Card(f, s))
    assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
    assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
    return hand


if __name__ == '__main__':
    hands = ["2♥ 2♦ 2♣ k♣ q♦",
     "2♥ 5♥ 7♦ 8♣ 9♠",
     "a♥ 2♦ 3♣ 4♣ 5♦",
     "2♥ 3♥ 2♦ 3♣ 3♦",
     "2♥ 7♥ 2♦ 3♣ 3♦",
     "2♥ 7♥ 7♦ 7♣ 7♠",
     "10♥ j♥ q♥ k♥ a♥"] + [
     "4♥ 4♠ k♠ 5♦ 10♠",
     "q♣ 10♣ 7♣ 6♣ 4♣",
     ]
    print("%-18s %-15s %s" % ("HAND", "CATEGORY", "TIE-BREAKER"))
    for cards in hands:
        r = rank(cards)
        print("%-18r %-15s %r" % (cards, r[0], r[1]))

```

