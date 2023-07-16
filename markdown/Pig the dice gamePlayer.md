# Pig the dice game/Player

## Task Link
[Rosetta Code - Pig the dice game/Player](https://rosettacode.org/wiki/Pig_the_dice_game/Player)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class Pigdice {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int players = 0;
		
		//Validate the input
		while(true) {
			//Get the number of players
			System.out.println("Hello, welcome to Pig Dice the game! How many players? ");
			if(scan.hasNextInt()) {
				
				//Gotta be more than 0
				int nextInt = scan.nextInt();
				if(nextInt > 0) {
					players = nextInt;
					break;
				}
			}
			else {
				System.out.println("That wasn't an integer. Try again. \n");
				scan.next();
			}
		}
		System.out.println("Alright, starting with " + players + " players. \n");
		
		//Start the game
		play(players, scan);
		
		scan.close();
	}
	
	public static void play(int group, Scanner scan) {
		//Set the number of strategies available.
		final int STRATEGIES = 5;
		
		//Construct the dice- accepts an int as an arg for number of sides, but defaults to 6.
		Dice dice = new Dice();
		
		//Create an array of players and initialize them to defaults.
		Player[] players = new Player[group];
		for(int count = 0; count < group; count++) {
			players[count] = new Player(count);
			System.out.println("Player " + players[count].getNumber() + "  is alive! ");
		}
		
		/*****Print strategy options here. Modify Player.java to add strategies. *****/
		System.out.println("Each strategy is numbered 0 - " + (STRATEGIES - 1) + ". They are as follows: ");
		System.out.println(">> Enter '0' for a human player. ");
		System.out.println(">> Strategy 1 is a basic strategy where the AI rolls until 20+ points and holds unless the current max is 75+.");
		System.out.println(">> Strategy 2 is a basic strategy where the AI, after 3 successful rolls, will randomly decide to roll or hold. ");
		System.out.println(">> Strategy 3 is similar to strategy 2, except it's a little gutsier and will attempt 5 successful rolls. ");
		System.out.println(">> Strategy 4 is like a mix between strategies 1 and 3. After turn points are >= 20 and while max points are still less than 75, it will randomly hold or roll. ");
		
		//Get the strategy for each player
		for(Player player : players) {
			System.out.println("\nWhat strategy would you like player " + player.getNumber() + " to use? ");

			//Validate the strategy is a real strategy.
			while(true) {
				if(scan.hasNextInt()) {
					int nextInt = scan.nextInt();
					if (nextInt < Strategy.STRATEGIES.length) {
						player.setStrategy(Strategy.STRATEGIES[nextInt]);
						break;
					}
				}
				else {
					System.out.println("That wasn't an option. Try again. ");
					scan.next();
				}
			}
		}
		
		//Here is where the rules for the game are programmatically defined.
		int max = 0;
		while(max < 100) {
			
			//Begin the round
			for(Player player : players) {
				System.out.println(">> Beginning Player " + player.getNumber() + "'s turn. ");
				
				//Set the points for the turn to 0
				player.setTurnPoints(0);
				
				//Determine whether the player chooses to roll or hold.
				player.setMax(max);
				while(true) {
					Move choice = player.choose();
					if(choice == Move.ROLL) {
						int roll = dice.roll();
						System.out.println("   A " + roll + " was rolled. ");
						player.setTurnPoints(player.getTurnPoints() + roll);
						
						//Increment the player's built in iterator.
						player.incIter();
						
						//If the player rolls a 1, their turn is over and they gain 0 points this round.
						if(roll == 1) {
							player.setTurnPoints(0);
							break;
						}
					}
					//Check if the player held or not.
					else {
						System.out.println("   The player has held. ");
						break;
					}
				}
				
				//End the turn and add any accumulated points to the player's pool.
				player.addPoints(player.getTurnPoints());
				System.out.println("   Player " + player.getNumber() + "'s turn is now over. Their total is " + player.getPoints() + ". \n");
				
				//Reset the player's built in iterator.
				player.resetIter();
				
				//Update the max score if necessary.
				if(max < player.getPoints()) {
					max = player.getPoints();
				}
				
				//If someone won, stop the game and announce the winner.
				if(max >= 100) {
					System.out.println("Player " + player.getNumber() + " wins with " + max + " points! End scores: ");
					
					//Announce the final scores.
					for(Player p : players) {
						System.out.println("Player " + p.getNumber() + " had " + p.getPoints() + " points. ");
					}
					break;
				}
			}
		}
		
	}
	
}

```

### java_code_2.txt
```java
public class Player {

	private int points = 0;
	private int turnPoints = 0;
	private Strategy strategy = null;
	private int max = 0;
	private int number;
	private int iter = 0;
	
	public Player(int val) {
		number = val;
	}
	
	public int getPoints() {
		return points;
	}
	public int getTurnPoints() {
		return turnPoints;
	}
	public int getMax() {
		return max;
	}
	public int getNumber() {
		return number;
	}
	public int getIter() {
		return iter;
	}
	public void addPoints(int val) {
		points += val;
	}
	public void setTurnPoints(int val) {
		turnPoints = val;
	}
	public void setStrategy(Strategy strat) {
		strategy = strat;
	}
	public void setMax(int val) {
		max = val;
	}
	public void setNumber(int val) {
		number = val;
	}
	public void resetIter() {
		iter = 0;
	}
	public void incIter() {
		iter++;
	}
	public void aiIntro() {
		System.out.println("   Player " + getNumber() + "'s turn points are " + getTurnPoints() + ". Their total is " + getPoints() + ". ");
		System.out.println("   The max points any player currently has is " + getMax() + ". ");
	}
	public Move choose() {
		return strategy.choose(this);
	}

}

```

### java_code_3.txt
```java
public enum Move { ROLL, HOLD }

```

### java_code_4.txt
```java
import java.util.Scanner;

public interface Strategy {

	Move choose(Player player);
	
	static final Scanner str = new Scanner(System.in);
	static final Dice die = new Dice(2);
	static final int ROOF = 75;
	static final int FLOOR = 20;
	static final int BASEMENT = 10;
	
	/*****MODIFY THIS AREA TO MODIFY THE STRATEGIES*****/
	//Determine whether to roll or hold based on the strategy for this player.
	public static final Strategy[] STRATEGIES = {
		
		//Strategy 0 is a user-defined strategy
		player -> {
			System.out.println("   Your turn points are " + player.getTurnPoints() + ". Your total is " + player.getPoints() + ". ");
			System.out.println("   The max points any player currently has is " + player.getMax() + ". (H)old or (R)oll?");
			System.out.println("   Enter 'h' to hold and 'r' to roll. ");
			while(true) {
				String input = null;
				if(str.hasNextLine()) {
					input = str.nextLine();
				}
				if(input.contains("r")) {
					return Move.ROLL;
				}
				else if(input.contains("h")) {
					return Move.HOLD;
				}
				else {
					System.out.println("  Enter an h or an r. \n");
					System.out.println(input);
				}
			}
		},
		
		//Strategy 1 is a basic strategy where the AI rolls until 20+ points and holds unless the current max is 75+.
		player -> {
			player.aiIntro();
			if(player.getTurnPoints() < FLOOR || player.getMax() >= ROOF) {
				if(player.getTurnPoints() >= (100 - player.getPoints())) {
					return Move.HOLD;					
				}
				else {
					return Move.ROLL;
				}
			}
			else {
				return Move.HOLD;
			}
		},
		
		//Strategy 2 is a basic strategy where the AI, after 3 successful rolls, will randomly decide to roll or hold.
		player -> {
			player.aiIntro();
			if(player.getPoints() == 0 && player.getTurnPoints() >= (BASEMENT / 2)) {
				return Move.HOLD;
			}
			if(player.getIter() > 3) {
				int roll = die.roll();
				
				if(roll == 1) {
					return Move.HOLD;
				}
				else {
					return Move.ROLL;
				}
			}
			else {
				return Move.ROLL;
			}
		},
		
		//Strategy 3 is similar to strategy 2, except it's a little gutsier and will attempt 5 successful rolls.
		player -> {
			player.aiIntro();
			if(player.getIter() > 5) {
				int roll = die.roll();
				
				if(roll == 1) {
					return Move.HOLD;
				}
				else {
					return Move.ROLL;
				}
			}
			else if(player.getPoints() < BASEMENT && player.getTurnPoints() > BASEMENT) {
				return Move.HOLD;
			}
			else {
				return Move.ROLL;
			}
		},
		
		/*Strategy 4 is like a mix between strategies 1 and 3. After turn points are >= 20 and while max points are still less than 75, it will randomly hold or roll.
		Unless their total is zero, in which case they'll hold at 10 points. */
		player -> {
			player.aiIntro();
			if(player.getPoints() == 0 && player.getTurnPoints() >= (BASEMENT / 2)) {
				return Move.HOLD;
			}
			else if(player.getTurnPoints() < FLOOR || player.getMax() >= ROOF) {
				if(player.getTurnPoints() >= (100 - player.getPoints())) {
					return Move.HOLD;					
				}
				else {
					return Move.ROLL;
				}
			}
			else if(player.getTurnPoints() > FLOOR && player.getMax() <= ROOF) {
				int roll = die.roll();
				
				if(roll == 1) {
					return Move.HOLD;
				}
				else {
					return Move.ROLL;
				}
			}
			else {
				return Move.HOLD;
			}
		}
	};

}

```

### java_code_5.txt
```java
import java.util.Random;

public class Dice {
	Random rand = new Random();
	int sides;
	Dice(int numSides) {
		sides = numSides;
	}
	Dice() {
		sides = 6;
	}
	int roll() {
		return rand.nextInt(sides) + 1;
	}
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python3

'''
See: http://en.wikipedia.org/wiki/Pig_(dice)

This program scores, throws the dice, and plays for an N player game of Pig.

'''

from random import randint
from collections import namedtuple
import random
from pprint import pprint as pp
from collections import Counter


playercount = 2
maxscore = 100
maxgames = 100000


Game = namedtuple('Game', 'players, maxscore, rounds')
Round = namedtuple('Round', 'who, start, scores, safe')


class Player():
    def __init__(self, player_index):
        self.player_index = player_index

    def __repr__(self):
        return '%s(%i)' % (self.__class__.__name__, self.player_index)

    def __call__(self, safescore, scores, game):
        'Returns boolean True to roll again'
        pass

class RandPlay(Player):
    def __call__(self, safe, scores, game):
        'Returns random boolean choice of whether to roll again'
        return bool(random.randint(0, 1))

class RollTo20(Player):
    def __call__(self, safe, scores, game):
        'Roll again if this rounds score < 20'
        return (((sum(scores) + safe[self.player_index]) < maxscore)    # Haven't won yet
                and(sum(scores) < 20))                                  # Not at 20 this round

class Desparat(Player):
    def __call__(self, safe, scores, game):
        'Roll again if this rounds score < 20 or someone is within 20 of winning'
        return (((sum(scores) + safe[self.player_index]) < maxscore)    # Haven't won yet
                and( (sum(scores) < 20)                                 # Not at 20 this round
                     or max(safe) >= (maxscore - 20)))                  # Someone's close


def game__str__(self):
    'Pretty printer for Game class'
    return ("Game(players=%r, maxscore=%i,\n  rounds=[\n    %s\n  ])"
            % (self.players, self.maxscore,
               ',\n    '.join(repr(round) for round in self.rounds)))
Game.__str__ = game__str__


def winningorder(players, safescores):
    'Return (players in winning order, their scores)'
    return tuple(zip(*sorted(zip(players, safescores),
                            key=lambda x: x[1], reverse=True)))

def playpig(game):
    '''
    Plays the game of pig returning the players in winning order
    and their scores whilst updating argument game with the details of play.
    '''
    players, maxscore, rounds = game
    playercount = len(players)
    safescore = [0] * playercount   # Safe scores for each player
    player = 0                      # Who plays this round
    scores=[]                       # Individual scores this round

    while max(safescore) < maxscore:
        startscore = safescore[player]
        rolling = players[player](safescore, scores, game)
        if rolling:
            rolled = randint(1, 6)
            scores.append(rolled)
            if rolled == 1:
                # Bust! 
                round = Round(who=players[player],
                              start=startscore,
                              scores=scores,
                              safe=safescore[player])
                rounds.append(round)
                scores, player = [], (player + 1) % playercount
        else:
            # Stick
            safescore[player] += sum(scores)
            round = Round(who=players[player],
                          start=startscore,
                          scores=scores,
                          safe=safescore[player])
            rounds.append(round)
            if safescore[player] >= maxscore:
                break
            scores, player = [], (player + 1) % playercount

    # return players in winning order and all scores
    return winningorder(players, safescore)

if __name__ == '__main__':
    game = Game(players=tuple(RandPlay(i) for i in range(playercount)),
                maxscore=20,
                rounds=[])
    print('ONE GAME')
    print('Winning order: %r; Respective scores: %r\n' % playpig(game))
    print(game)
    game = Game(players=tuple(RandPlay(i) for i in range(playercount)),
                maxscore=maxscore,
                rounds=[])
    algos = (RollTo20, RandPlay, Desparat)
    print('\n\nMULTIPLE STATISTICS using %r\n  for %i GAMES'
          % (', '.join(p.__name__ for p in algos), maxgames,))
    winners = Counter(repr(playpig(game._replace(players=tuple(random.choice(algos)(i)
                                                               for i in range(playercount)),
                                                 rounds=[]))[0])
                      for i in range(maxgames))
    print('  Players(position) winning on left; occurrences on right:\n    %s'
          % ',\n    '.join(str(w) for w in winners.most_common()))

```

