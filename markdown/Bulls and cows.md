# Bulls and cows

## Task Link
[Rosetta Code - Bulls and cows](https://rosettacode.org/wiki/Bulls_and_cows)

## Java Code
### java_code_1.txt
```java
import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class BullsAndCows{
	public static void main(String[] args){
		Random gen= new Random();
		int target;
		while(hasDupes(target= (gen.nextInt(9000) + 1000)));
		String targetStr = target +"";
		boolean guessed = false;
		Scanner input = new Scanner(System.in);
		int guesses = 0;
		do{
			int bulls = 0;
			int cows = 0;
			System.out.print("Guess a 4-digit number with no duplicate digits: ");
			int guess;
			try{
				guess = input.nextInt();
				if(hasDupes(guess) || guess < 1000) continue;
			}catch(InputMismatchException e){
				continue;
			}
			guesses++;
			String guessStr = guess + "";
			for(int i= 0;i < 4;i++){
				if(guessStr.charAt(i) == targetStr.charAt(i)){
					bulls++;
				}else if(targetStr.contains(guessStr.charAt(i)+"")){
					cows++;
				}
			}
			if(bulls == 4){
				guessed = true;
			}else{
				System.out.println(cows+" Cows and "+bulls+" Bulls.");
			}
		}while(!guessed);
		System.out.println("You won after "+guesses+" guesses!");
	}

	public static boolean hasDupes(int num){
		boolean[] digs = new boolean[10];
		while(num > 0){
			if(digs[num%10]) return true;
			digs[num%10] = true;
			num/= 10;
		}
		return false;
	}
}

```

## Python Code
### python_code_1.txt
```python
'''
 Bulls and cows. A game pre-dating, and similar to, Mastermind.
'''

import random

digits = '123456789'
size = 4
chosen = ''.join(random.sample(digits,size))
#print chosen # Debug
print '''I have chosen a number from %s unique digits from 1 to 9 arranged in a random order.
You need to input a %i digit, unique digit number as a guess at what I have chosen''' % (size, size)
guesses = 0
while True:
    guesses += 1
    while True:
        # get a good guess
        guess = raw_input('\nNext guess [%i]: ' % guesses).strip()
        if len(guess) == size and \
           all(char in digits for char in guess) \
           and len(set(guess)) == size:
            break
        print "Problem, try again. You need to enter %i unique digits from 1 to 9" % size
    if guess == chosen:
        print '\nCongratulations you guessed correctly in',guesses,'attempts'
        break
    bulls = cows = 0
    for i in range(size):
        if guess[i] == chosen[i]:
            bulls += 1
        elif guess[i] in chosen:
            cows += 1
    print '  %i Bulls\n  %i Cows' % (bulls, cows)

```

