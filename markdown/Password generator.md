# Password generator

## Task Link
[Rosetta Code - Password generator](https://rosettacode.org/wiki/Password_generator)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class PasswordGenerator {
    final static Random rand = new Random();

    public static void main(String[] args) {
        int num, len;

        try {
            if (args.length != 2)
                throw new IllegalArgumentException();

            len = Integer.parseInt(args[0]);
            if (len < 4 || len > 16)
                throw new IllegalArgumentException();

            num = Integer.parseInt(args[1]);
            if (num < 1 || num > 10)
                throw new IllegalArgumentException();

            for (String pw : generatePasswords(num, len))
                System.out.println(pw);

        } catch (IllegalArgumentException e) {
            String s = "Provide the length of the passwords (min 4, max 16) you "
                    + "want to generate,\nand how many (min 1, max 10)";
            System.out.println(s);
        }
    }

    private static List<String> generatePasswords(int num, int len) {
        final String s = "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~";

        List<String> result = new ArrayList<>();

        for (int i = 0; i < num; i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(s.charAt(rand.nextInt(s.length())));
            sb.append((char) (rand.nextInt(10) + '0'));
            sb.append((char) (rand.nextInt(26) + 'a'));
            sb.append((char) (rand.nextInt(26) + 'A'));

            for (int j = 4; j < len; j++) {
                int r = rand.nextInt(93) + '!';
                if (r == 92 || r == 96) {
                    j--;
                } else {
                    sb.append((char) r);
                }
            }
            result.add(shuffle(sb));
        }
        return result;
    }

    public static String shuffle(StringBuilder sb) {
        int len = sb.length();
        for (int i = len - 1; i > 0; i--) {
            int r = rand.nextInt(i);
            char tmp = sb.charAt(i);
            sb.setCharAt(i, sb.charAt(r));
            sb.setCharAt(r, tmp);
        }
        return sb.toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

lowercase = 'abcdefghijklmnopqrstuvwxyz' # same as string.ascii_lowercase
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # same as string.ascii_uppercase
digits = '0123456789'                    # same as string.digits
punctuation = '!"#$%&\'()*+,-./:;<=>?@[]^_{|}~' # like string.punctuation but without backslash \ nor grave `

allowed = lowercase + uppercase + digits + punctuation

visually_similar = 'Il1O05S2Z'


def new_password(length:int, readable=True) -> str:
    if length < 4:
        print("password length={} is too short,".format(length),
            "minimum length=4")
        return ''
    choice = random.SystemRandom().choice
    while True:
        password_chars = [
            choice(lowercase),
            choice(uppercase),
            choice(digits),
            choice(punctuation)
            ] + random.sample(allowed, length-4)
        if (not readable or 
                all(c not in visually_similar for c in password_chars)):
            random.SystemRandom().shuffle(password_chars)
            return ''.join(password_chars)


def password_generator(length, qty=1, readable=True):
    for i in range(qty):
        print(new_password(length, readable))

```

### python_code_2.txt
```python
import "random" for Random
import "/ioutil" for FileUtil, File, Input
import "/fmt" for Fmt
import "os" for Process

var r  = Random.new()
var rr = Random.new() // use a separate generator for shuffles
var lb = FileUtil.lineBreak

var lower = "abcdefghijklmnopqrstuvwxyz"
var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
var digit = "0123456789"
var other = """!"#$%&'()*+,-./:;<=>?@[]^_{|}~"""

var exclChars = [
    "'I', 'l' and '1'",
    "'O' and '0'     ",
    "'5' and 'S'     ",
    "'2' and 'Z'     "
]

var shuffle = Fn.new { |s|
    var sl = s.toList
    rr.shuffle(sl)
    return sl.join()
}

var generatePasswords = Fn.new { |pwdLen, pwdNum, toConsole, toFile|
    var ll = lower.count
    var ul = upper.count
    var dl = digit.count
    var ol = other.count
    var tl = ll + ul + dl + ol
    var fw = toFile ? File.create("pwds.txt") : null
 
    if (toConsole) System.print("\nThe generated passwords are:")
    for (i in 0...pwdNum) {
        var pwd = lower[r.int(ll)] + upper[r.int(ul)] + digit[r.int(dl)] + other[r.int(ol)]
        for (j in 0...pwdLen - 4) {
            var k = r.int(tl)
            pwd = pwd + ((k < ll)      ? lower[k] :
                         (k < ll + ul) ? upper[k - ll] :
                         (k < tl - ol) ? digit[k - ll - ul] : other[tl - 1 - k])
        }
        for (i in 1..5) pwd = shuffle.call(pwd) // shuffle 5 times say
        if (toConsole) Fmt.print("  $2d: $s", i + 1, pwd)
        if (toFile) {
            fw.writeBytes(pwd)
            if (i < pwdNum - 1) fw.writeBytes(lb)
        }
    }
    if (toFile) {
       System.print("\nThe generated passwords have been written to the file pwds.txt")
       fw.close()
    }
}

var printHelp = Fn.new {
    System.print("""
This program generates up to 99 passwords of between 5 and 20 characters in
length.

You will be prompted for the values of all parameters when the program is run
- there are no command line options to memorize.

The passwords can either be written to the console or to a file (pwds.txt),
or both.

The passwords must contain at least one each of the following character types:
   lower-case letters :  a -> z
   upper-case letters :  A -> Z
   digits             :  0 -> 9
   other characters   :  !"#$%&'()*+,-./:;<=>?@[]^_{|}~

Optionally, a seed can be set for the random generator
(any non-zero number) otherwise the default seed will be used.
Even if the same seed is set, the passwords won't necessarily be exactly
the same on each run as additional random shuffles are always performed.

You can also specify that various sets of visually similar characters
will be excluded (or not) from the passwords, namely: Il1  O0  5S  2Z

Finally, the only command line options permitted are -h and -help which
will display this page and then exit.

Any other command line parameters will simply be ignored and the program
will be run normally.

""")
}

var args = Process.arguments
if (args.count == 1 && (args[0] == "-h" || args[0] == "-help")) {
   printHelp.call()
   return
}

System.print("Please enter the following and press return after each one")

var pwdLen = Input.integer("  Password length (5 to 20)     : ", 5, 20)
var pwdNum = Input.integer("  Number to generate (1 to 99)  : ", 1, 99)

var seed   = Input.number ("  Seed value (0 to use default) : ")
if (seed != 0) r = Random.new(seed)

System.print("  Exclude the following visually similar characters")
for (i in 0..3) {
    var yn = Input.option("    %(exclChars[i]) y/n : ", "ynYN")
    if (yn == "y" || yn == "Y") {
        if (i == 0) {
            upper = upper.replace("I", "")
            lower = lower.replace("l", "")
            digit = digit.replace("1", "")
        } else if (i == 1) {
            upper = upper.replace("O", "")
            digit = digit.replace("0", "")
        } else if (i == 2) {
            upper = upper.replace("S", "")
            digit = digit.replace("5", "")
        } else if (i == 3) {
            upper = upper.replace("Z", "")
            digit = digit.replace("2", "")
        }
    }
}

var toConsole = Input.option("  Write to console   y/n : ", "ynYN")
toConsole = toConsole == "y" || toConsole == "Y"
var toFile = true
if (toConsole) {
    toFile = Input.option("  Write to file      y/n : ", "ynYN")
    toFile = toFile == "y" || toFile == "Y"
}

generatePasswords.call(pwdLen, pwdNum, toConsole, toFile)

```

