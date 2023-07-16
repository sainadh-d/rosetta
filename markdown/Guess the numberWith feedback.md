# Guess the number/With feedback

## Task Link
[Rosetta Code - Guess the number/With feedback](https://rosettacode.org/wiki/Guess_the_number/With_feedback)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
import java.util.Scanner;
public class Main
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        Random random = new Random();
        long from = 1;
        long to = 100;
        int randomNumber = random.nextInt(to - from + 1) + from;
        int guessedNumber = 0;

        System.out.printf("The number is between %d and %d.\n", from, to);

        do
        {
            System.out.print("Guess what the number is: ");
            guessedNumber = scan.nextInt();
            if (guessedNumber > randomNumber)
                System.out.println("Your guess is too high!");
            else if (guessedNumber < randomNumber)
                System.out.println("Your guess is too low!");
            else
                System.out.println("You got it!");
        } while (guessedNumber != randomNumber);
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

inclusive_range = (1, 100)

print("Guess my target number that is between %i and %i (inclusive).\n"
      % inclusive_range)
target = random.randint(*inclusive_range)
answer, i = None, 0
while answer != target:
    i += 1
    txt = input("Your guess(%i): " % i)
    try:
        answer = int(txt)
    except ValueError:
        print("  I don't understand your input of '%s' ?" % txt)
        continue
    if answer < inclusive_range[0] or answer > inclusive_range[1]:
        print("  Out of range!")
        continue
    if answer == target:
        print("  Ye-Haw!!")
        break
    if answer < target: print("  Too low.")
    if answer > target: print("  Too high.")

print("\nThanks for playing.")

```

