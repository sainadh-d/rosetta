# Nim game

## Task Link
[Rosetta Code - Nim game](https://rosettacode.org/wiki/Nim_game)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class NimGame {

    public static void main(String[] args) {
        runGame(12);
    }
    
    private static void runGame(int tokens) {
        System.out.printf("Nim game.%n%n");

        Scanner in = new Scanner(System.in);;
        
        do {            
            boolean humanInputOk = false;
            int humanTokens = 0;
            while ( ! humanInputOk ) {
                System.out.printf("Human takes how many tokens?  ");
                String input = in.next();
                try {
                    humanTokens = Integer.parseInt(input);
                    if ( humanTokens >= 1 && humanTokens <= 3 ) {
                        humanInputOk = true;
                    }
                    else {
                        System.out.printf("Try a number between 1 and 3.%n");
                    }
                }
                catch (NumberFormatException e) {
                    System.out.printf("Invalid input.  Try a number between 1 and 3.%n");
                }
            }
            
            tokens -= humanTokens;
            
            System.out.printf("You take %d token%s.%n%d token%s remaining.%n%n", humanTokens, humanTokens > 1 ? "s" : "", tokens, tokens != 1 ? "s" : "");
            if ( tokens == 0 ) {
                System.out.printf("You win!!.%n%n");
                break;
            }
            int computerTokens = 4 - humanTokens;
            tokens -= computerTokens;
            
            System.out.printf("Computer takes %d token%s.%n%d token%s remaining.%n%n", computerTokens, computerTokens != 1 ? "s" : "", tokens, tokens != 1 ? "s" : "");
            if ( tokens == 0 ) {
                System.out.printf("Computer wins!!.%n%n");
            }

        } while (tokens > 0);

        in.close();
    }

}

```

## Python Code
### python_code_1.txt
```python
print("Py Nim\n")

def getTokens(curTokens):
	global tokens
	
	print("How many tokens would you like to take? ", end='')
	take = int(input())
	
	if (take < 1 or take > 3):
		print("Number must be between 1 and 3.\n")
		getTokens(curTokens)
		return
	
	tokens = curTokens - take
	print(f'You take {take} tokens.')
	print(f'{tokens} tokens remaining.\n')

def compTurn(curTokens):
	global tokens
	
	take = curTokens % 4
	tokens = curTokens - take
	print (f'Computer takes {take} tokens.')
	print (f'{tokens} tokens remaining.\n')
	

tokens = 12
while (tokens > 0):
	getTokens(tokens)
	compTurn(tokens)

print("Computer wins!")

```

