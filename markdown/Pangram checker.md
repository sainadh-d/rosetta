# Pangram checker

## Task Link
[Rosetta Code - Pangram checker](https://rosettacode.org/wiki/Pangram_checker)

## Java Code
### java_code_1.txt
```java
public class Pangram {
    public static boolean isPangram(String test){
        for (char a = 'A'; a <= 'Z'; a++)
            if ((test.indexOf(a) < 0) && (test.indexOf((char)(a + 32)) < 0))
                return false;
        return true;
    }

    public static void main(String[] args){
        System.out.println(isPangram("the quick brown fox jumps over the lazy dog"));//true
        System.out.println(isPangram("the quick brown fox jumped over the lazy dog"));//false, no s
        System.out.println(isPangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"));//true
        System.out.println(isPangram("ABCDEFGHIJKLMNOPQSTUVWXYZ"));//false, no r
        System.out.println(isPangram("ABCDEFGHIJKL.NOPQRSTUVWXYZ"));//false, no m
        System.out.println(isPangram("ABC.D.E.FGHI*J/KL-M+NO*PQ R\nSTUVWXYZ"));//true
        System.out.println(isPangram(""));//false
    }
}

```

## Python Code
### python_code_1.txt
```python
import string, sys
if sys.version_info[0] < 3:
    input = raw_input

def ispangram(sentence, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(sentence.lower())

print ( ispangram(input('Sentence: ')) )

```

