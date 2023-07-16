# Morse code

## Task Link
[Rosetta Code - Morse code](https://rosettacode.org/wiki/Morse_code)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class MorseCode {

    final static String[][] code = {
        {"A", ".-     "}, {"B", "-...   "}, {"C", "-.-.   "}, {"D", "-..    "},
        {"E", ".      "}, {"F", "..-.   "}, {"G", "--.    "}, {"H", "....   "},
        {"I", "..     "}, {"J", ".---   "}, {"K", "-.-    "}, {"L", ".-..   "},
        {"M", "--     "}, {"N", "-.     "}, {"O", "---    "}, {"P", ".--.   "},
        {"Q", "--.-   "}, {"R", ".-.    "}, {"S", "...    "}, {"T", "-      "},
        {"U", "..-    "}, {"V", "...-   "}, {"W", ".-   - "}, {"X", "-..-   "},
        {"Y", "-.--   "}, {"Z", "--..   "}, {"0", "-----  "}, {"1", ".----  "},
        {"2", "..---  "}, {"3", "...--  "}, {"4", "....-  "}, {"5", ".....  "},
        {"6", "-....  "}, {"7", "--...  "}, {"8", "---..  "}, {"9", "----.  "},
        {"'", ".----. "}, {":", "---... "}, {",", "--..-- "}, {"-", "-....- "},
        {"(", "-.--.- "}, {".", ".-.-.- "}, {"?", "..--.. "}, {";", "-.-.-. "},
        {"/", "-..-.  "}, {"-", "..--.- "}, {")", "---..  "}, {"=", "-...-  "},
        {"@", ".--.-. "}, {"\"", ".-..-."}, {"+", ".-.-.  "}, {" ", "/"}}; // cheat a little

    final static Map<Character, String> map = new HashMap<>();

    static {
        for (String[] pair : code)
            map.put(pair[0].charAt(0), pair[1].trim());
    }

    public static void main(String[] args) {
        printMorse("sos");
        printMorse("   Hello     World!");
        printMorse("Rosetta Code");
    }

    static void printMorse(String input) {
        System.out.printf("%s %n", input);

        input = input.trim().replaceAll("[ ]+", " ").toUpperCase();
        for (char c : input.toCharArray()) {
            String s = map.get(c);
            if (s != null)
                System.out.printf("%s ", s);
        }
        System.out.println("\n");
    }
}

```

## Python Code
### python_code_1.txt
```python
import time, winsound #, sys

char2morse = {          
          "!": "---.",      "\"": ".-..-.",     "$": "...-..-",    "'": ".----.",  
          "(": "-.--.",      ")": "-.--.-",     "+": ".-.-.",      ",": "--..--", 
          "-": "-....-",     ".": ".-.-.-",     "/": "-..-.", 
          "0": "-----",      "1": ".----",      "2": "..---",      "3": "...--", 
          "4": "....-",      "5": ".....",      "6": "-....",      "7": "--...", 
          "8": "---..",      "9": "----.", 
          ":": "---...",     ";": "-.-.-.",     "=": "-...-",      "?": "..--..", 
          "@": ".--.-.", 
          "A": ".-",         "B": "-...",       "C": "-.-.",       "D": "-..", 
          "E": ".",          "F": "..-.",       "G": "--.",        "H": "....", 
          "I": "..",         "J": ".---",       "K": "-.-",        "L": ".-..", 
          "M": "--",         "N": "-.",         "O": "---",        "P": ".--.", 
          "Q": "--.-",       "R": ".-.",        "S": "...",        "T": "-", 
          "U": "..-",        "V": "...-",       "W": ".--",        "X": "-..-", 
          "Y": "-.--",       "Z": "--..", 
          "[": "-.--.",      "]": "-.--.-",     "_": "..--.-",
 }

e = 50      # Element time in ms. one dit is on for e then off for e
f = 1280    # Tone freq. in hertz
chargap = 1 # Time between characters of a word, in units of e
wordgap = 7 # Time between words, in units of e

def gap(n=1):
    time.sleep(n * e / 1000)
off = gap

def on(n=1):
    winsound.Beep(f, n * e)

def dit():
    on(); off()

def dah():
    on(3); off()

def bloop(n=3):
    winsound.Beep(f//2, n * e)

def windowsmorse(text):
    for word in text.strip().upper().split():
        for char in word:
            for element in char2morse.get(char, '?'):
                if element == '-':
                    dah()
                elif element == '.':
                    dit()
                else:
                    bloop()
            gap(chargap)
        gap(wordgap)

# Outputs its own source file as Morse. An audible quine!
#with open(sys.argv[0], 'r') as thisfile:
#    windowsmorse(thisfile.read())
    
while True:
    windowsmorse(input('A string to change into morse: '))

```

