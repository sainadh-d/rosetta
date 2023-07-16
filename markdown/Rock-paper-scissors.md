# Rock-paper-scissors

## Task Link
[Rosetta Code - Rock-paper-scissors](https://rosettacode.org/wiki/Rock-paper-scissors)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Random;

public class RPS {
	public enum Item{
		ROCK, PAPER, SCISSORS, /*LIZARD, SPOCK*/;
		public List<Item> losesToList;
		public boolean losesTo(Item other) {
			return losesToList.contains(other);
		}
		static {
			SCISSORS.losesToList = Arrays.asList(ROCK/*, SPOCK*/);
			ROCK.losesToList = Arrays.asList(PAPER/*, SPOCK*/);
			PAPER.losesToList = Arrays.asList(SCISSORS/*, LIZARD*/);
			/*
			SPOCK.losesToList = Arrays.asList(PAPER, LIZARD);
			LIZARD.losesToList = Arrays.asList(SCISSORS, ROCK);
			*/
                }
	}
	//EnumMap uses a simple array under the hood
	public final Map<Item, Integer> counts = new EnumMap<Item, Integer>(Item.class){{
		for(Item item:Item.values())
			put(item, 1);
	}};

	private int totalThrows = Item.values().length;

	public static void main(String[] args){
		RPS rps = new RPS();
		rps.run();
	}

	public void run() {
		Scanner in = new Scanner(System.in);
		System.out.print("Make your choice: ");
		while(in.hasNextLine()){
			Item aiChoice = getAIChoice();
			String input = in.nextLine();
			Item choice;
			try{
				choice = Item.valueOf(input.toUpperCase());
			}catch (IllegalArgumentException ex){
				System.out.println("Invalid choice");
				continue;
			}
			counts.put(choice, counts.get(choice) + 1);
			totalThrows++;
			System.out.println("Computer chose: " + aiChoice);
			if(aiChoice == choice){
				System.out.println("Tie!");
			}else if(aiChoice.losesTo(choice)){
				System.out.println("You chose...wisely. You win!");
			}else{
				System.out.println("You chose...poorly. You lose!");
			}
			System.out.print("Make your choice: ");
		}
	}

	private static final Random rng = new Random();
	private Item getAIChoice() {
		int rand = rng.nextInt(totalThrows);
		for(Map.Entry<Item, Integer> entry:counts.entrySet()){
			Item item = entry.getKey();
			int count = entry.getValue();
			if(rand < count){
				List<Item> losesTo = item.losesToList;
				return losesTo.get(rng.nextInt(losesTo.size()));
			}
			rand -= count;
		}
		return null;
	}
}

```

## Python Code
### python_code_1.txt
```python
from random import choice

rules = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
previous = ['rock', 'paper', 'scissors']

while True:
    human = input('\nchoose your weapon: ')
    computer = rules[choice(previous)]  # choose the weapon which beats a randomly chosen weapon from "previous"

    if human in ('quit', 'exit'): break

    elif human in rules:
        previous.append(human)
        print('the computer played', computer, end='; ')

        if rules[computer] == human:  # if what beats the computer's choice is the human's choice...
            print('yay you win!')
        elif rules[human] == computer:  # if what beats the human's choice is the computer's choice...
            print('the computer beat you... :(')
        else: print("it's a tie!")

    else: print("that's not a valid choice")

```

### python_code_2.txt
```python
from random import randint

hands = ['rock', 'scissors', 'paper']; judge = ['its a tie!', 'the computer beat you... :(', 'yay you win!']
while True:
    try:
        YOU = hands.index(input('Choose your weapon: ')) # YOU = hands.index(raw_input('Choose your weapon: '))   If you use Python2.7
    except ValueError:
        break
    NPC = randint(0, 2)
    print('The computer played ' + hands[NPC] + '; ' + judge[YOU-NPC])

```

