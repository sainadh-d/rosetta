# Mind boggling card trick

## Task Link
[Rosetta Code - Mind boggling card trick](https://rosettacode.org/wiki/Mind_boggling_card_trick)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public final class MindBogglingCardTrick {

	public static void main(String[] aArgs) {		
		List<Character> cards = new ArrayList<Character>(52);
		cards.addAll(Collections.nCopies(26, 'R'));
		cards.addAll(Collections.nCopies(26, 'B'));
		Collections.shuffle(cards);
		
		List<Character> redPile = new ArrayList<Character>();
		List<Character> blackPile = new ArrayList<Character>();
		List<Character> discardPile = new ArrayList<Character>();	
	
		for ( int i = 0; i < 52; i += 2 ) {
			if ( cards.get(i) == 'R' ) {
				redPile.add(cards.get(i + 1));
			} else {
				blackPile.add(cards.get(i + 1));
			}	        
	        discardPile.add(cards.get(i));
	    }
		
		System.out.println("A sample run." + System.lineSeparator());
		System.out.println("After dealing the cards the state of the piles is:");
		System.out.println(String.format("    Red    : %2d cards -> %s", redPile.size(), redPile));
		System.out.println(String.format("    Black  : %2d cards -> %s", blackPile.size(), blackPile));
		System.out.println(String.format("    Discard: %2d cards -> %s", discardPile.size(), discardPile));
		
		ThreadLocalRandom random = ThreadLocalRandom.current();
	    final int minimumSize = Math.min(redPile.size(), blackPile.size());
	    final int choice = random.nextInt(1, minimumSize + 1);
	    
	    List<Integer> redIndexes = IntStream.range(0, redPile.size()).boxed().collect(Collectors.toList()); 
	    List<Integer> blackIndexes = IntStream.range(0, blackPile.size()).boxed().collect(Collectors.toList());
	    Collections.shuffle(redIndexes);
	    Collections.shuffle(blackIndexes);
	    List<Integer> redChosenIndexes = redIndexes.subList(0, choice);
	    List<Integer> blackChosenIndexes = blackIndexes.subList(0, choice);

	    System.out.println(System.lineSeparator() + "Number of cards are to be swapped: " + choice);
	    System.out.println("The respective zero-based indices of the cards to be swapped are:");
	    System.out.println("    Red    : " + redChosenIndexes);
	    System.out.println("    Black  : " + blackChosenIndexes);
		
	    for ( int i = 0; i < choice; i++ ) {
	        final char temp = redPile.get(redChosenIndexes.get(i));
	        redPile.set(redChosenIndexes.get(i), blackPile.get(blackChosenIndexes.get(i)));
	        blackPile.set(blackChosenIndexes.get(i), temp);
	    }
	    
	    System.out.println(System.lineSeparator() + "After swapping cards the state of the red and black piless is:");
	    System.out.println("    Red    : " + redPile);
	    System.out.println("    Black  : " + blackPile);
	    
	    int redCount = 0;
	    for ( char ch : redPile ) {
	    	if ( ch == 'R' ) {
	    		redCount += 1;
	    	}
	    }
	    
	    int blackCount = 0;
	    for ( char ch : blackPile ) {
	    	if ( ch == 'B' ) {
	    		blackCount += 1;
	    	}
	    }
	    
	    System.out.println(System.lineSeparator() + "The number of red cards in the red pile: " + redCount);
	    System.out.println("The number of black cards in the black pile: " + blackCount);
	    if ( redCount == blackCount ) {
	    	System.out.println("So the asssertion is correct.");
	    } else {
	    	System.out.println("So the asssertion is incorrect.");
	    }		
	}

}

```

## Python Code
### python_code_1.txt
```python
import random

## 1. Cards
n = 52
Black, Red = 'Black', 'Red'
blacks = [Black] * (n // 2) 
reds = [Red] * (n // 2)
pack = blacks + reds
# Give the pack a good shuffle.
random.shuffle(pack)

## 2. Deal from the randomised pack into three stacks
black_stack, red_stack, discard = [], [], []
while pack:
    top = pack.pop()
    if top == Black:
        black_stack.append(pack.pop())
    else:
        red_stack.append(pack.pop())
    discard.append(top)
print('(Discards:', ' '.join(d[0] for d in discard), ')\n')

## 3. Swap the same, random, number of cards between the two stacks.
# We can't swap more than the number of cards in a stack.
max_swaps = min(len(black_stack), len(red_stack))
# Randomly choose the number of cards to swap.
swap_count = random.randint(0, max_swaps)
print('Swapping', swap_count)
# Randomly choose that number of cards out of each stack to swap.
def random_partition(stack, count):
    "Partition the stack into 'count' randomly selected members and the rest"
    sample = random.sample(stack, count)
    rest = stack[::]
    for card in sample:
        rest.remove(card)
    return rest, sample

black_stack, black_swap = random_partition(black_stack, swap_count)
red_stack, red_swap = random_partition(red_stack, swap_count)

# Perform the swap.
black_stack += red_swap
red_stack += black_swap

## 4. Order from randomness?
if black_stack.count(Black) == red_stack.count(Red):
    print('Yeha! The mathematicians assertion is correct.')
else:
    print('Whoops - The mathematicians (or my card manipulations) are flakey')

```

