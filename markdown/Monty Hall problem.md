# Monty Hall problem

## Task Link
[Rosetta Code - Monty Hall problem](https://rosettacode.org/wiki/Monty_Hall_problem)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
public class Monty{
	public static void main(String[] args){
		int switchWins = 0;
		int stayWins = 0;
		Random gen = new Random();
		for(int plays = 0;plays < 32768;plays++ ){
			int[] doors = {0,0,0};//0 is a goat, 1 is a car
			doors[gen.nextInt(3)] = 1;//put a winner in a random door
			int choice = gen.nextInt(3); //pick a door, any door
			int shown; //the shown door
			do{
				shown = gen.nextInt(3);
			//don't show the winner or the choice
			}while(doors[shown] == 1 || shown == choice);
			
			stayWins += doors[choice];//if you won by staying, count it
			
			//the switched (last remaining) door is (3 - choice - shown), because 0+1+2=3
			switchWins += doors[3 - choice - shown];
		}
		System.out.println("Switching wins " + switchWins + " times.");
		System.out.println("Staying wins " + stayWins + " times.");
	}
}

```

## Python Code
### python_code_1.txt
```python
'''
I could understand the explanation of the Monty Hall problem
but needed some more evidence

References:
  http://www.bbc.co.uk/dna/h2g2/A1054306
  http://en.wikipedia.org/wiki/Monty_Hall_problem especially:
  http://en.wikipedia.org/wiki/Monty_Hall_problem#Increasing_the_number_of_doors
'''
from random import randrange

doors, iterations = 3,100000  # could try 100,1000

def monty_hall(choice, switch=False, doorCount=doors):
  # Set up doors
  door = [False]*doorCount
  # One door with prize
  door[randrange(doorCount)] = True

  chosen = door[choice]

  unpicked = door
  del unpicked[choice]

  # Out of those unpicked, the alternative is either:
  #   the prize door, or
  #   an empty door if the initial choice is actually the prize.
  alternative = True in unpicked

  if switch:
    return alternative
  else:
    return chosen

print "\nMonty Hall problem simulation:"
print doors, "doors,", iterations, "iterations.\n"

print "Not switching allows you to win",
print sum(monty_hall(randrange(3), switch=False)
          for x in range(iterations)),
print "out of", iterations, "times."
print "Switching allows you to win",
print sum(monty_hall(randrange(3), switch=True)
          for x in range(iterations)),
print "out of", iterations, "times.\n"

```

### python_code_2.txt
```python
import random
 #1 represents a car
 #0 represent a goat

stay = 0  #amount won if stay in the same position
switch = 0 # amount won if you switch 

for i in range(1000):
    lst = [1,0,0]           # one car and two goats
    random.shuffle(lst)     # shuffles the list randomly
    
    ran = random.randrange(3) # gets a random number for the random guess

    user = lst[ran] #storing the random guess 

    del(lst[ran]) # deleting the random guess

    huh = 0
    for i in lst: # getting a value 0 and deleting it
        if i ==0:
            del(lst[huh]) # deletes a goat when it finds it
            break
        huh+=1
        
    if user ==1: # if the original choice is 1 then stay adds 1
        stay+=1
        
    if lst[0] == 1: # if the switched value is 1 then switch adds 1
        switch+=1

print("Stay =",stay)
print("Switch = ",switch)
#Done by Sam Witton 09/04/2014

```

