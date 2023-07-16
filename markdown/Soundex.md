# Soundex

## Task Link
[Rosetta Code - Soundex](https://rosettacode.org/wiki/Soundex)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args){
    System.out.println(soundex("Soundex"));
    System.out.println(soundex("Example"));
    System.out.println(soundex("Sownteks"));
    System.out.println(soundex("Ekzampul"));
  }

private static String getCode(char c){
  switch(c){
    case 'B': case 'F': case 'P': case 'V':
      return "1";
    case 'C': case 'G': case 'J': case 'K':
    case 'Q': case 'S': case 'X': case 'Z':
      return "2";
    case 'D': case 'T':
      return "3";
    case 'L':
      return "4";
    case 'M': case 'N':
      return "5";
    case 'R':
      return "6";
    default:
      return "";
  }
}

public static String soundex(String s){
  String code, previous, soundex;
  code = s.toUpperCase().charAt(0) + "";

  // EDITED : previous = "7";
  previous = getCode(s.toUpperCase().charAt(0));

  for(int i = 1;i < s.length();i++){
    String current = getCode(s.toUpperCase().charAt(i));
    if(current.length() > 0 && !current.equals(previous)){
      code = code + current;
    }
    previous = current;
  }
  soundex = (code + "0000").substring(0, 4);
  return soundex;
}

```

## Python Code
### python_code_1.txt
```python
from itertools import groupby

def soundex(word):
   codes = ("bfpv","cgjkqsxz", "dt", "l", "mn", "r")
   soundDict = dict((ch, str(ix+1)) for ix,cod in enumerate(codes) for ch in cod)
   cmap2 = lambda kar: soundDict.get(kar, '9')
   sdx =  ''.join(cmap2(kar) for kar in word.lower())
   sdx2 = word[0].upper() + ''.join(k for k,g in list(groupby(sdx))[1:] if k!='9')
   sdx3 = sdx2[0:4].ljust(4,'0')
   return sdx3

```

### python_code_2.txt
```python
>>>print soundex("soundex")
S532
>>>print soundex("example")
E251
>>>print soundex("ciondecks")
C532
>>>print soundex("ekzampul")
E251

```

