# Guess the number/With feedback (player)

## Task Link
[Rosetta Code - Guess the number/With feedback (player)](https://rosettacode.org/wiki/Guess_the_number/With_feedback_(player))

## Java Code
### java_code_1.txt
```java
import java.util.AbstractList;
import java.util.Collections;
import java.util.Scanner;

public class GuessNumber {
    public static final int LOWER = 0, UPPER = 100;
    public static void main(String[] args) {
	System.out.printf("Instructions:\n" +
			  "Think of integer number from %d (inclusive) to %d (exclusive) and\n" +
			  "I will guess it. After each guess, you respond with L, H, or C depending\n" +
			  "on if my guess was too low, too high, or correct.\n",
			  LOWER, UPPER);
	int result = Collections.binarySearch(new AbstractList<Integer>() {
		private final Scanner in = new Scanner(System.in);
		public int size() { return UPPER - LOWER; }
		public Integer get(int i) {
		    System.out.printf("My guess is: %d. Is it too high, too low, or correct? (H/L/C) ", LOWER+i);
		    String s = in.nextLine();
		    assert s.length() > 0;
		    switch (Character.toLowerCase(s.charAt(0))) {
		    case 'l':
			return -1;
		    case 'h':
			return 1;
		    case 'c':
			return 0;
		    }
		    return -1;
		}
	    }, 0);
	if (result < 0)
	    System.out.println("That is impossible.");
	else
	    System.out.printf("Your number is %d.\n", result);
    }
}

```

## Python Code
### python_code_1.txt
```python
inclusive_range = mn, mx = (1, 10)

print('''\
Think of a number between %i and %i and wait for me to guess it.
On every guess of mine you should state whether the guess was
too high, too low, or equal to your number by typing h, l, or =
''' % inclusive_range)

i = 0
while True:
    i += 1
    guess = (mn+mx)//2
    txt = input("Guess %2i is: %2i. The score for which is (h,l,=): "
                % (i, guess)).strip().lower()[0]
    if txt not in 'hl=':
        print("  I don't understand your input of '%s' ?" % txt)
        continue
    if txt == 'h':
        mx = guess-1
    if txt == 'l':
        mn = guess+1
    if txt == '=':
        print("  Ye-Haw!!")
        break
    if (mn > mx) or (mn < inclusive_range[0]) or (mx > inclusive_range[1]):
        print("Please check your scoring as I cannot find the value")
        break
        
print("\nThanks for keeping score.")

```

### python_code_2.txt
```python
import bisect
try: input = raw_input
except: pass

class GuessNumberFakeList(object):
    def __getitem__(self, i):
        s = input("Is your number less than or equal to %d?" % i)
        return 0 if s.lower().startswith('y') else -1

LOWER, UPPER = 0, 100

if __name__ == "__main__":
    print("""Instructions:
Think of integer number from %d (inclusive) to %d (exclusive) and
I will guess it. After each guess, I will ask you if it is less than
or equal to some number, and you will respond with "yes" or "no".
""" % (LOWER, UPPER))
    result = bisect.bisect_left(GuessNumberFakeList(), 0, LOWER, UPPER)
    print("Your number is %d." % result)

```

