# Pig the dice game

## Task Link
[Rosetta Code - Pig the dice game](https://rosettacode.org/wiki/Pig_the_dice_game)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class PigDice {

    public static void main(String[] args) {
        final int maxScore = 100;
        final int playerCount = 2;
        final String[] yesses = {"y", "Y", ""};

        int[] safeScore = new int[2];
        int player = 0, score = 0;

        Scanner sc = new Scanner(System.in);
        Random rnd = new Random();

        while (true) {
            System.out.printf(" Player %d: (%d, %d) Rolling? (y/n) ", player,
                    safeScore[player], score);
            if (safeScore[player] + score < maxScore
                    && Arrays.asList(yesses).contains(sc.nextLine())) {
                final int rolled = rnd.nextInt(6) + 1;
                System.out.printf(" Rolled %d\n", rolled);
                if (rolled == 1) {
                    System.out.printf(" Bust! You lose %d but keep %d\n\n",
                            score, safeScore[player]);
                } else {
                    score += rolled;
                    continue;
                }
            } else {
                safeScore[player] += score;
                if (safeScore[player] >= maxScore)
                    break;
                System.out.printf(" Sticking with %d\n\n", safeScore[player]);
            }
            score = 0;
            player = (player + 1) % playerCount;
        }
        System.out.printf("\n\nPlayer %d wins with a score of %d",
                player, safeScore[player]);
    }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import java.util.stream.IntStream;

public interface PigDice {
  public static void main(String... arguments) {
    final int maxScore = 100;
    final int playerCount = 2;
    final String[] yesses = {"y", "Y", ""};

    final Scanner scanner = new Scanner(System.in);
    final Random random = new Random();

    final int[] safeScore = new int[2];
    final int[] score = new int[2];

    IntStream.iterate(0, player -> (player + 1) % playerCount)
      .map(player -> {
        boolean isRolling = true;
        while (isRolling) {
          System.out.printf(
            "Player %d: (%d, %d) Rolling? (y/n) ",
            player,
            safeScore[player],
            score[player]
          );
          isRolling =
            safeScore[player] + score[player] < maxScore
              && Arrays.asList(yesses).contains(scanner.nextLine())
          ;
          if (isRolling) {
            final int rolled = random.nextInt(6) + 1;
            System.out.printf("Rolled %d\n", rolled);
            if (rolled == 1) {
              System.out.printf(
                "Bust! You lose %d but keep %d\n\n",
                score[player],
                safeScore[player]
              );
              return -1;
            } else {
              score[player] += rolled;
            }
          } else {
            safeScore[player] += score[player];
            if (safeScore[player] >= maxScore) {
              return player;
            }
            System.out.printf("Sticking with %d\n\n", safeScore[player]);
          }
        }
        score[player] = 0;
        return -1;
      })
      .filter(player -> player > -1)
      .findFirst()
      .ifPresent(player ->
        System.out.printf(
          "\n\nPlayer %d wins with a score of %d",
          player,
          safeScore[player]
        )
      )
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python3

'''
See: http://en.wikipedia.org/wiki/Pig_(dice)

This program scores and throws the dice for a two player game of Pig

'''

from random import randint

playercount = 2
maxscore = 100
safescore = [0] * playercount
player = 0
score=0

while max(safescore) < maxscore:
    rolling = input("Player %i: (%i, %i) Rolling? (Y) "
                    % (player, safescore[player], score)).strip().lower() in {'yes', 'y', ''}
    if rolling:
        rolled = randint(1, 6)
        print('  Rolled %i' % rolled)
        if rolled == 1:
            print('  Bust! you lose %i but still keep your previous %i'
                  % (score, safescore[player]))
            score, player = 0, (player + 1) % playercount
        else:
            score += rolled
    else:
        safescore[player] += score
        if safescore[player] >= maxscore:
            break
        print('  Sticking with %i' % safescore[player])
        score, player = 0, (player + 1) % playercount
        
print('\nPlayer %i wins with a score of %i' %(player, safescore[player]))

```

