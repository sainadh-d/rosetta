# 24 game

## Task Link
[Rosetta Code - 24 game](https://rosettacode.org/wiki/24_game)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class Game24 {
    static Random r = new Random();

    public static void main(String[] args) {

        int[] digits = randomDigits();
        Scanner in = new Scanner(System.in);

        System.out.print("Make 24 using these digits: ");
        System.out.println(Arrays.toString(digits));
        System.out.print("> ");

        Stack<Float> s = new Stack<>();
        long total = 0;
        for (char c : in.nextLine().toCharArray()) {
            if ('0' <= c && c <= '9') {
                int d = c - '0';
                total += (1 << (d * 5));
                s.push((float) d);
            } else if ("+/-*".indexOf(c) != -1) {
                s.push(applyOperator(s.pop(), s.pop(), c));
            }
        }
        if (tallyDigits(digits) != total)
            System.out.print("Not the same digits. ");
        else if (Math.abs(24 - s.peek()) < 0.001F)
            System.out.println("Correct!");
        else
            System.out.print("Not correct.");
    }

    static float applyOperator(float a, float b, char c) {
        switch (c) {
            case '+':
                return a + b;
            case '-':
                return b - a;
            case '*':
                return a * b;
            case '/':
                return b / a;
            default:
                return Float.NaN;
        }
    }

    static long tallyDigits(int[] a) {
        long total = 0;
        for (int i = 0; i < 4; i++)
            total += (1 << (a[i] * 5));
        return total;
    }

    static int[] randomDigits() {        
        int[] result = new int[4];
        for (int i = 0; i < 4; i++)
            result[i] = r.nextInt(9) + 1;
        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
'''
 The 24 Game

 Given any four digits in the range 1 to 9, which may have repetitions,
 Using just the +, -, *, and / operators; and the possible use of
 brackets, (), show how to make an answer of 24.

 An answer of "q" will quit the game.
 An answer of "!" will generate a new set of four digits.
 Otherwise you are repeatedly asked for an expression until it evaluates to 24

 Note: you cannot form multiple digit numbers from the supplied digits,
 so an answer of 12+12 when given 1, 2, 2, and 1 would not be allowed.

'''

from __future__ import division, print_function
import random, ast, re
import sys

if sys.version_info[0] < 3: input = raw_input

def choose4():
    'four random digits >0 as characters'
    return [str(random.randint(1,9)) for i in range(4)]

def welcome(digits):
    print (__doc__)
    print ("Your four digits: " + ' '.join(digits))

def check(answer, digits):
    allowed = set('() +-*/\t'+''.join(digits))
    ok = all(ch in allowed for ch in answer) and \
         all(digits.count(dig) == answer.count(dig) for dig in set(digits)) \
         and not re.search('\d\d', answer)
    if ok:
        try:
            ast.parse(answer)
        except:
            ok = False
    return ok

def main():    
    digits = choose4()
    welcome(digits)
    trial = 0
    answer = ''
    chk = ans = False
    while not (chk and ans == 24):
        trial +=1
        answer = input("Expression %i: " % trial)
        chk = check(answer, digits)
        if answer.lower() == 'q':
            break
        if answer == '!':
            digits = choose4()
            print ("New digits:", ' '.join(digits))
            continue
        if not chk:
            print ("The input '%s' was wonky!" % answer)
        else:
            ans = eval(answer)
            print (" = ", ans)
            if ans == 24:
                print ("Thats right!")
    print ("Thank you and goodbye")   

if __name__ == '__main__': main()

```

### python_code_2.txt
```python
import random, re
chars = ["(",")","/","+","-","*"]  
while True:
    charsandints, ints = [], []
    for x in range(4):
        ints.append(str(random.randrange(1,10)))
    charsandints = chars + ints
    print "Numbers are:", ints
    guess = raw_input("Enter your guess:")
    if guess.lower() == "q":
        break
    elif guess.lower() == "|":
        pass
    else:
        flag = True
        for a in guess:
            if a not in charsandints or guess.count(a) > charsandints.count(a):
                flag = False
        if re.search("\d\d", guess):
            print "You cannot combine digits."
            break
        if flag:
            print "Your result is: ", eval(guess)
            if eval(guess) == 24:
                print "You won"
                break
            else:
                print "You lost"
                break
        else:
            print "You cannot use anthing other than", charsandints
            break
print "Thanks for playing"

```

