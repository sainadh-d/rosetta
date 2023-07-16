# Bulls and cows/Player

## Task Link
[Rosetta Code - Bulls and cows/Player](https://rosettacode.org/wiki/Bulls_and_cows/Player)

## Java Code
### java_code_1.txt
```java
public class BullsAndCowsPlayerGame {

    private static int count;
    private static Console io = System.console();

    private final GameNumber secret;
    private List<AutoGuessNumber> pool = new ArrayList<>();

    public BullsAndCowsPlayerGame(GameNumber secret) {
        this.secret = secret;
        fillPool();
    }

    private void fillPool() {
        for (int i = 123; i < 9877; i++) {
            int[] arr = AutoGuessNumber.parseDigits(i, 4);

            if (GameNumber.isGuess(arr)) {
                pool.add(new AutoGuessNumber(i, 4));
            }
        }
    }

    public void play() {
        io.printf("Bulls and Cows%n");
        io.printf("==============%n");
        io.printf("Secret number is %s%n", secret);

        do {
            AutoGuessNumber guess = guessNumber();
            io.printf("Guess #%d is %s from %d%n", count, guess, pool.size());

            GuessResult result = secret.match(guess);
            if (result != null) {
                printScore(io, result);

                if (result.isWin()) {
                    io.printf("The answer is %s%n", guess);
                    break;
                }

                clearPool(guess, result);
            } else {
                io.printf("No more variants%n");
                System.exit(0);
            }
        } while (true);
    }

    private AutoGuessNumber guessNumber() {
        Random random = new Random();
        if (pool.size() > 0) {
            int number = random.nextInt(pool.size());
            count++;
            return pool.get(number);
        }
        return null;
    }

    private static void printScore(Console io, GuessResult result) {
        io.printf("%1$d  %2$d%n", result.getBulls(), result.getCows());
    }

    private void clearPool(AutoGuessNumber guess, GuessResult guessResult) {
        pool.remove(guess);

        for (int i = 0; i < pool.size(); i++) {
            AutoGuessNumber g = pool.get(i);
            GuessResult gr = guess.match(g);

            if (!guessResult.equals(gr)) {
                pool.remove(g);
            }
        }
    }

    public static void main(String[] args) {
        new BullsAndCowsPlayerGame(new GameNumber()).play();
    }
}

```

### java_code_2.txt
```java
public abstract class AbstractGuessNumber {

    protected int[] digits;
    private int length;

    public AbstractGuessNumber(int length) {
        this.length = length;
        this.digits = new int[this.length];
    }

    public int[] getDigits() {
        return digits;
    }

    public int getLength() {
        return length;
    }

    public GuessResult match(AbstractGuessNumber guessable) {
        int bulls = 0;
        int cows = 0;

        if (guessable != null) {
            for (int i = 0; i < this.getLength(); i++) {
                for (int j = 0; j < guessable.getLength(); j++) {

                    if (digits[i] == guessable.getDigits()[j]) {
                        if (i == j) {
                            bulls++;
                        } else {
                            cows++;
                        }
                    }
                }
            }
        }
        return new GuessResult(getLength(), bulls, cows);
    }
}

```

### java_code_3.txt
```java
public class GameNumber extends AbstractGuessNumber {

    public GameNumber() {
        super(4);
        defineNumber();
    }

    public static boolean isGuess(int[] digits) {
        return (digits != null && isUnique(digits) && isAllDigits(digits));
    }

    protected static boolean isAllDigits(int[] array) {
        for (int i = 0; i < array.length; i++) {
            char digit = (char) (array[i] + '0');

            if (!Character.isDigit(digit)) {
                return false;
            }
        }
        return true;
    }

    protected static boolean isUnique(int[] array) {
        for (int j = 0; j < array.length; j++) {
            int a = array[j];

            for (int i = 0; i < j; i++) {
                if (a == array[i]) {
                    // seen this int before
                    return false;
                }
            }
        }
        return true;
    }

    public static int[] parseDigits(int number, int length) {
        int[] arr = new int[length];
        int temp = number;
        for (int i = length - 1; i >= 0; i--) {
            arr[i] = temp % 10;
            temp /= 10;
        }
        return arr;
    }

    protected void defineNumber() {
        int[] arr = generateRandom();

        for (int i = 0; i < getLength(); i++) {
            digits[i] = arr[i];
        }
    }

    private int[] generateRandom() {
        int[] arr;
        do {
            Random random = new Random();
            int number = random.nextInt(9877) + 123;
            arr = parseDigits(number, getLength());
        } while (!isGuess(arr));
        return arr;
    }

    @Override
    public String toString() {
        return Arrays.toString(digits);
    }
}

```

### java_code_4.txt
```java
public class AutoGuessNumber extends AbstractGuessNumber {

    public AutoGuessNumber(int number, int lenght) {
        super(lenght);
        defineNumber(number);
    }

    public static int[] parseDigits(int number, int length) {
        int[] arr = new int[length];
        int temp = number;
        for (int i = length - 1; i >= 0; i--) {
            arr[i] = temp % 10;
            temp /= 10;
        }
        return arr;
    }

    protected void defineNumber(int number) {
        int[] arr = parseDigits(number, getLength());

        for (int i = 0; i < getLength(); i++) {
            digits[i] = arr[i];
        }
    }

    @Override
    public String toString() {
        return Arrays.toString(digits);
    }
}

```

### java_code_5.txt
```java
public class GuessResult {

    private static int guessNum = 0;
    private int bulls;
    private int cows;
    private int length;

    public GuessResult(int length, int bulls, int cows) {
        this.length = length;
        this.bulls = bulls;
        this.cows = cows;
        guessNum++;
    }

    public int getBulls() {
        return bulls;
    }

    public int getCows() {
        return cows;
    }

    public boolean isWin() {
        return (bulls == length);
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("GuessResult {");
        sb.append("bulls=").append(bulls);
        sb.append(", cows=").append(cows);
        sb.append('}');
        return sb.toString();
    }

    public int getId() {
        return guessNum;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GuessResult that = (GuessResult) o;
        return bulls == that.bulls &&
                cows == that.cows &&
                length == that.length;
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations
from random import shuffle

try:
    raw_input
except:
    raw_input = input
try:
    from itertools import izip
except:
    izip = zip
    
digits = '123456789'
size = 4

def parse_score(score):
    score = score.strip().split(',')
    return tuple(int(s.strip()) for s in score)

def scorecalc(guess, chosen):
    bulls = cows = 0
    for g,c in izip(guess, chosen):
        if g == c:
            bulls += 1
        elif g in chosen:
            cows += 1
    return bulls, cows

choices = list(permutations(digits, size))
shuffle(choices)
answers = []
scores  = []

print ("Playing Bulls & Cows with %i unique digits\n" % size)
       
while True:
    ans = choices[0]
    answers.append(ans)
    #print ("(Narrowed to %i possibilities)" % len(choices))
    score = raw_input("Guess %2i is %*s. Answer (Bulls, cows)? "
                      % (len(answers), size, ''.join(ans)))
    score = parse_score(score)
    scores.append(score)
    #print("Bulls: %i, Cows: %i" % score)
    found =  score == (size, 0)
    if found:
        print ("Ye-haw!")
        break
    choices = [c for c in choices if scorecalc(c, ans) == score]
    if not choices:
        print ("Bad scoring? nothing fits those scores you gave:")
        print ('  ' +
               '\n  '.join("%s -> %s" % (''.join(an),sc)
                           for an,sc in izip(answers, scores)))
        break

```

