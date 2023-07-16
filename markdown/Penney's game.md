# Penney's game

## Task Link
[Rosetta Code - Penney's game](https://rosettacode.org/wiki/Penney%27s_game)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class PenneysGame {

    public static void main(String[] args) {
        Random rand = new Random();

        String compChoice = "", playerChoice;
        if (rand.nextBoolean()) {

            for (int i = 0; i < 3; i++)
                compChoice += "HT".charAt(rand.nextInt(2));
            System.out.printf("Computer chooses %s%n", compChoice);

            playerChoice = prompt(compChoice);

        } else {

            playerChoice = prompt(compChoice);

            compChoice = "T";
            if (playerChoice.charAt(1) == 'T')
                compChoice = "H";
            compChoice += playerChoice.substring(0, 2);
            System.out.printf("Computer chooses %s%n", compChoice);
        }

        String tossed = "";
        while (true) {
            tossed += "HT".charAt(rand.nextInt(2));
            System.out.printf("Tossed %s%n" , tossed);
            if (tossed.endsWith(playerChoice)) {
                System.out.println("You win!");
                break;
            }
            if (tossed.endsWith(compChoice)) {
                System.out.println("Computer wins!");
                break;
            }
        }
    }

    private static String prompt(String otherChoice) {
        Scanner sc = new Scanner(System.in);
        String s;
        do {
            System.out.print("Choose a sequence: ");
            s = sc.nextLine().trim().toUpperCase();
        } while (!s.matches("[HT]{3}") || s.equals(otherChoice));
        return s;
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function
import random
from time import sleep

first = random.choice([True, False])

you = ''
if first:
    me = ''.join(random.sample('HT'*3, 3))
    print('I choose first and will win on first seeing {} in the list of tosses'.format(me))
    while len(you) != 3 or any(ch not in 'HT' for ch in you) or you == me:
        you = input('What sequence of three Heads/Tails will you win with: ')
else:
    while len(you) != 3 or any(ch not in 'HT' for ch in you):
        you = input('After you: What sequence of three Heads/Tails will you win with: ')
    me = ('H' if you[1] == 'T' else 'T') + you[:2]
    print('I win on first seeing {} in the list of tosses'.format(me))
    
print('Rolling:\n  ', end='')
rolled = ''
while True:
    rolled += random.choice('HT')
    print(rolled[-1], end='')
    if rolled.endswith(you):
        print('\n  You win!')
        break
    if rolled.endswith(me):
        print('\n  I win!')
        break
    sleep(1)    # For dramatic effect

```

