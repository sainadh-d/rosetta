# Dice game probabilities

## Task Link
[Rosetta Code - Dice game probabilities](https://rosettacode.org/wiki/Dice_game_probabilities)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class Dice{
	private static int roll(int nDice, int nSides){
		int sum = 0;
		Random rand = new Random();
		for(int i = 0; i < nDice; i++){
			sum += rand.nextInt(nSides) + 1;
		}
		return sum;
	}
	
	private static int diceGame(int p1Dice, int p1Sides, int p2Dice, int p2Sides, int rolls){
		int p1Wins = 0;
		for(int i = 0; i < rolls; i++){
			int p1Roll = roll(p1Dice, p1Sides);
			int p2Roll = roll(p2Dice, p2Sides);
			if(p1Roll > p2Roll) p1Wins++;
		}
		return p1Wins;
	}
	
	public static void main(String[] args){
		int p1Dice = 9; int p1Sides = 4;
		int p2Dice = 6; int p2Sides = 6;
		int rolls = 10000;
		int p1Wins = diceGame(p1Dice, p1Sides, p2Dice, p2Sides, rolls);
		System.out.println(rolls + " rolls, p1 = " + p1Dice + "d" + p1Sides + ", p2 = " + p2Dice + "d" + p2Sides);
		System.out.println("p1 wins " + (100.0 * p1Wins / rolls) + "% of the time");
		
		System.out.println();
		
		p1Dice = 5; p1Sides = 10;
		p2Dice = 6; p2Sides = 7;
		rolls = 10000;
		p1Wins = diceGame(p1Dice, p1Sides, p2Dice, p2Sides, rolls);
		System.out.println(rolls + " rolls, p1 = " + p1Dice + "d" + p1Sides + ", p2 = " + p2Dice + "d" + p2Sides);
		System.out.println("p1 wins " + (100.0 * p1Wins / rolls) + "% of the time");
		
		System.out.println();
		
		p1Dice = 9; p1Sides = 4;
		p2Dice = 6; p2Sides = 6;
		rolls = 1000000;
		p1Wins = diceGame(p1Dice, p1Sides, p2Dice, p2Sides, rolls);
		System.out.println(rolls + " rolls, p1 = " + p1Dice + "d" + p1Sides + ", p2 = " + p2Dice + "d" + p2Sides);
		System.out.println("p1 wins " + (100.0 * p1Wins / rolls) + "% of the time");
		
		System.out.println();
		
		p1Dice = 5; p1Sides = 10;
		p2Dice = 6; p2Sides = 7;
		rolls = 1000000;
		p1Wins = diceGame(p1Dice, p1Sides, p2Dice, p2Sides, rolls);
		System.out.println(rolls + " rolls, p1 = " + p1Dice + "d" + p1Sides + ", p2 = " + p2Dice + "d" + p2Sides);
		System.out.println("p1 wins " + (100.0 * p1Wins / rolls) + "% of the time");
	}
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product

def gen_dict(n_faces, n_dice):
    counts = [0] * ((n_faces + 1) * n_dice)
    for t in product(range(1, n_faces + 1), repeat=n_dice):
        counts[sum(t)] += 1
    return counts, n_faces ** n_dice

def beating_probability(n_sides1, n_dice1, n_sides2, n_dice2):
    c1, p1 = gen_dict(n_sides1, n_dice1)
    c2, p2 = gen_dict(n_sides2, n_dice2)
    p12 = float(p1 * p2)

    return sum(p[1] * q[1] / p12
               for p, q in product(enumerate(c1), enumerate(c2))
               if p[0] > q[0])

print beating_probability(4, 9, 6, 6)
print beating_probability(10, 5, 7, 6)

```

### python_code_2.txt
```python
from __future__ import print_function, division

def combos(sides, n):
    if not n: return [1]
    ret = [0] * (max(sides)*n + 1)
    for i,v in enumerate(combos(sides, n - 1)):
        if not v: continue
        for s in sides: ret[i + s] += v
    return ret

def winning(sides1, n1, sides2, n2):
    p1, p2 = combos(sides1, n1), combos(sides2, n2)
    win,loss,tie = 0,0,0 # 'win' is 1 beating 2
    for i,x1 in enumerate(p1):
        # using accumulated sum on p2 could save some time
        win += x1*sum(p2[:i])
        tie += x1*sum(p2[i:i+1])
        loss+= x1*sum(p2[i+1:])
    s = sum(p1)*sum(p2)
    return win/s, tie/s, loss/s

print(winning(range(1,5), 9, range(1,7), 6))
print(winning(range(1,11), 5, range(1,8), 6)) # this seem hardly fair

# mountains of dice test case
# print(winning((1, 2, 3, 5, 9), 700, (1, 2, 3, 4, 5, 6), 800))

```

### python_code_3.txt
```python
from __future__ import division, print_function
from itertools import accumulate # Python3 only

def combos(sides, n):
    ret = [1] + [0]*(n + 1)*sides # extra length for negative indices
    for p in range(1, n + 1):
        rolling_sum = 0
        for i in range(p*sides, p - 1, -1):
            rolling_sum += ret[i - sides] - ret[i]
            ret[i] = rolling_sum
        ret[p - 1] = 0
    return ret

def winning(d1, n1, d2, n2):
    c1, c2 = combos(d1, n1), combos(d2, n2)
    ac = list(accumulate(c2 + [0]*(len(c1) - len(c2))))

    return sum(v*a for  v,a in zip(c1[1:], ac)) / (ac[-1]*sum(c1))


print(winning(4, 9, 6, 6))
print(winning(5, 10, 6, 7))

#print(winning(6, 700, 8, 540))

```

