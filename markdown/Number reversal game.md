# Number reversal game

## Task Link
[Rosetta Code - Number reversal game](https://rosettacode.org/wiki/Number_reversal_game)

## Java Code
### java_code_1.txt
```java
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;


public class ReversalGame {
    private List<Integer> gameList;

    public ReversalGame() {
        initialize();
    }

    public void play() throws Exception {
        int i = 0;
        int moveCount = 0;
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(gameList);
            System.out.println("Please enter a index to reverse from 2 to 9. Enter 99 to quit");
            i = scanner.nextInt();
            if (i == 99) {
                break;
            }
            if (i < 2 || i > 9) {
                System.out.println("Invalid input");
            } else {
                moveCount++;
                reverse(i);
                if (isSorted()) {
                    System.out.println("Congratulations you solved this in " + moveCount + " moves!");
                    break;
                }
            }

        }
        scanner.close();
    }

    private void reverse(int position) {
        Collections.reverse(gameList.subList(0, position));
    }

    private boolean isSorted() {
        for (int i=0; i < gameList.size() - 1; ++i) {
            if (gameList.get(i).compareTo(gameList.get(i + 1)) > 0) {
                return false;
            }
        }
        return true;
    }

    private void initialize() {
        this.gameList = new ArrayList<Integer>(9);
        for (int i=1; i < 10; ++i) {
            gameList.add(i);
        }
        while (isSorted()) {
            Collections.shuffle(gameList);
        }
    }


    public static void main(String[] args) {
        try {
            ReversalGame game = new ReversalGame();
            game.play();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
print '# Number reversal game'

var data, trials = list(1..9), 0

while data == sort data:
    random.shuffle data

while data != sort data:
    trials += 1
    flip = int input '#${trials}: LIST: ${join data} Flip how many?: '
    data[:flip] = reverse data[:flip]

print '\nYou took ${trials} attempts to put digits in order!'

```

### python_code_2.txt
```python
'''
number reversal game
    Given a jumbled list of the numbers 1 to 9
    Show the list.
    Ask the player how many digits from the left to reverse.
    Reverse those digits then ask again.
    until all the digits end up in ascending order.

'''

import random

print(__doc__)
data, trials = list('123456789'), 0
while data == sorted(data):
    random.shuffle(data)
while data != sorted(data):
    trials += 1
    flip = int(input('#%2i: LIST: %r Flip how many?: ' % (trials, ' '.join(data))))
    data[:flip] = reversed(data[:flip])

print('\nYou took %2i attempts to put the digits in order!' % trials)

```

