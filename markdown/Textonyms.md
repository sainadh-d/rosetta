# Textonyms

## Task Link
[Rosetta Code - Textonyms](https://rosettacode.org/wiki/Textonyms)

## Java Code
### java_code_1.txt
```java
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Vector;

public class RTextonyms {

  private static final Map<Character, Character> mapping;
  private int total, elements, textonyms, max_found;
  private String filename, mappingResult;
  private Vector<String> max_strings;
  private Map<String, Vector<String>> values;

  static {
    mapping = new HashMap<Character, Character>();
    mapping.put('A', '2'); mapping.put('B', '2'); mapping.put('C', '2');
    mapping.put('D', '3'); mapping.put('E', '3'); mapping.put('F', '3');
    mapping.put('G', '4'); mapping.put('H', '4'); mapping.put('I', '4');
    mapping.put('J', '5'); mapping.put('K', '5'); mapping.put('L', '5');
    mapping.put('M', '6'); mapping.put('N', '6'); mapping.put('O', '6');
    mapping.put('P', '7'); mapping.put('Q', '7'); mapping.put('R', '7'); mapping.put('S', '7');
    mapping.put('T', '8'); mapping.put('U', '8'); mapping.put('V', '8');
    mapping.put('W', '9'); mapping.put('X', '9'); mapping.put('Y', '9'); mapping.put('Z', '9');
  }

  public RTextonyms(String filename) {

    this.filename = filename;
    this.total = this.elements = this.textonyms = this.max_found = 0;
    this.values = new HashMap<String, Vector<String>>();
    this.max_strings = new Vector<String>();

    return;
  }

  public void add(String line) {

    String mapping = "";
    total++;
    if (!get_mapping(line)) {
      return;
    }
    mapping = mappingResult;

    if (values.get(mapping) == null) {
      values.put(mapping, new Vector<String>());
    }

    int num_strings;
    num_strings = values.get(mapping).size();
    textonyms += num_strings == 1 ? 1 : 0;
    elements++;

    if (num_strings > max_found) {
      max_strings.clear();
      max_strings.add(mapping);
      max_found = num_strings;
    }
    else if (num_strings == max_found) {
      max_strings.add(mapping);
    }

    values.get(mapping).add(line);

    return;
  }

  public void results() {

    System.out.printf("Read %,d words from %s%n%n", total, filename);
    System.out.printf("There are %,d words in %s which can be represented by the digit key mapping.%n", elements,
        filename);
    System.out.printf("They require %,d digit combinations to represent them.%n", values.size());
    System.out.printf("%,d digit combinations represent Textonyms.%n", textonyms);
    System.out.printf("The numbers mapping to the most words map to %,d words each:%n", max_found + 1);
    for (String key : max_strings) {
      System.out.printf("%16s maps to: %s%n", key, values.get(key).toString());
    }
    System.out.println();

    return;
  }

  public void match(String key) {

    Vector<String> match;
    match = values.get(key);
    if (match == null) {
      System.out.printf("Key %s not found%n", key);
    }
    else {
      System.out.printf("Key %s matches: %s%n", key, match.toString());
    }

    return;
  }

  private boolean get_mapping(String line) {

    mappingResult = line;
    StringBuilder mappingBuilder = new StringBuilder();
    for (char cc : line.toCharArray()) {
      if (Character.isAlphabetic(cc)) {
        mappingBuilder.append(mapping.get(Character.toUpperCase(cc)));
      }
      else if (Character.isDigit(cc)) {
        mappingBuilder.append(cc);
      }
      else {
        return false;
      }
    }
    mappingResult = mappingBuilder.toString();

    return true;
  }

  public static void main(String[] args) {

    String filename;
    if (args.length > 0) {
      filename = args[0];
    }
    else {
      filename = "./unixdict.txt";
    }
    RTextonyms tc;
    tc = new RTextonyms(filename);
    Path fp = Paths.get(filename);
    try (Scanner fs = new Scanner(fp, StandardCharsets.UTF_8.name())) {
      while (fs.hasNextLine()) {
        tc.add(fs.nextLine());
      }
    }
    catch (IOException ex) {
      ex.printStackTrace();
    }

    List<String> numbers = Arrays.asList(
        "001", "228", "27484247", "7244967473642",
        "."
        );

    tc.results();
    for (String number : numbers) {
      if (number.equals(".")) {
        System.out.println();
      }
      else {
        tc.match(number);
      }
    }

    return;
  }
}

```

## Python Code
### python_code_1.txt
```python
from collections import defaultdict
import urllib.request

CH2NUM = {ch: str(num) for num, chars in enumerate('abc def ghi jkl mno pqrs tuv wxyz'.split(), 2) for ch in chars}
URL = 'http://www.puzzlers.org/pub/wordlists/unixdict.txt'


def getwords(url):
 return urllib.request.urlopen(url).read().decode("utf-8").lower().split()

def mapnum2words(words):
    number2words = defaultdict(list)
    reject = 0
    for word in words:
        try:
            number2words[''.join(CH2NUM[ch] for ch in word)].append(word)
        except KeyError:
            # Reject words with non a-z e.g. '10th'
            reject += 1
    return dict(number2words), reject

def interactiveconversions():
    global inp, ch, num
    while True:
        inp = input("\nType a number or a word to get the translation and textonyms: ").strip().lower()
        if inp:
            if all(ch in '23456789' for ch in inp):
                if inp in num2words:
                    print("  Number {0} has the following textonyms in the dictionary: {1}".format(inp, ', '.join(
                        num2words[inp])))
                else:
                    print("  Number {0} has no textonyms in the dictionary.".format(inp))
            elif all(ch in CH2NUM for ch in inp):
                num = ''.join(CH2NUM[ch] for ch in inp)
                print("  Word {0} is{1} in the dictionary and is number {2} with textonyms: {3}".format(
                    inp, ('' if inp in wordset else "n't"), num, ', '.join(num2words[num])))
            else:
                print("  I don't understand %r" % inp)
        else:
            print("Thank you")
            break


if __name__ == '__main__':
    words = getwords(URL)
    print("Read %i words from %r" % (len(words), URL))
    wordset = set(words)
    num2words, reject = mapnum2words(words)
    morethan1word = sum(1 for w in num2words if len(num2words[w]) > 1)
    maxwordpernum = max(len(values) for values in num2words.values())
    print("""
There are {0} words in {1} which can be represented by the Textonyms mapping.
They require {2} digit combinations to represent them.
{3} digit combinations represent Textonyms.\
""".format(len(words) - reject, URL, len(num2words), morethan1word))

    print("\nThe numbers mapping to the most words map to %i words each:" % maxwordpernum)
    maxwpn = sorted((key, val) for key, val in num2words.items() if len(val) == maxwordpernum)
    for num, wrds in maxwpn:
        print("  %s maps to: %s" % (num, ', '.join(wrds)))

    interactiveconversions()

```

