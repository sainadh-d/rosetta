# Determine if a string is collapsible

## Task Link
[Rosetta Code - Determine if a string is collapsible](https://rosettacode.org/wiki/Determine_if_a_string_is_collapsible)

## Java Code
### java_code_1.txt
```java
//  Title:  Determine if a string is collapsible

public class StringCollapsible {

    public static void main(String[] args) {
        for ( String s : new String[] {
              "", 
              "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ", 
              "..1111111111111111111111111111111111111111111111111111111111111117777888", 
              "I never give 'em hell, I just tell the truth, and they think it's hell. ", 
              "                                                    --- Harry S Truman  ",
              "122333444455555666666777777788888888999999999",
              "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
              "headmistressship"}) {
            String result = collapse(s);
            System.out.printf("old:  %2d <<<%s>>>%nnew:  %2d <<<%s>>>%n%n", s.length(), s, result.length(), result);
        }
    }
    
    private static String collapse(String in) {
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < in.length() ; i++ ) {
            if ( i == 0 || in.charAt(i-1) != in.charAt(i) ) {
                sb.append(in.charAt(i));
            }
        }
        return sb.toString();
    }

}

```

## Python Code
### python_code_1.txt
```python
from itertools import groupby

def collapser(txt):
    return ''.join(item for item, grp in groupby(txt))

if __name__ == '__main__':
    strings = [
            "",
            '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln ',
            "..1111111111111111111111111111111111111111111111111111111111111117777888",
            "I never give 'em hell, I just tell the truth, and they think it's hell. ",
            "                                                   ---  Harry S Truman  ",
            "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
            "headmistressship",
            "aardvark",
            "😍😀🙌💃😍😍😍🙌",
            ]
    for txt in strings:
        this = "Original"
        print(f"\n{this:14} Size: {len(txt)} «««{txt}»»»" )
        this = "Collapsed"
        sqz = collapser(txt)
        print(f"{this:>14} Size: {len(sqz)} «««{sqz}»»»" )

```

### python_code_2.txt
```python
'''Determining if a string is collapsible'''

from operator import eq


# isCollapsible :: String -> Bool
def isCollapsible(s):
    '''True if s contains any consecutively
       repeated characters.
    '''
    return False if 2 > len(s) else (
        any(map(eq, s, s[1:]))
    )


# ------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Determining whether each string is collapsible'''
    xs = [
        "",
        '"If I were two-faced, would I be wearing this one?" --- Abraham Lincoln ',
        "..1111111111111111111111111111111111111111111111111111111111111117777888",
        "I never give 'em hell, I just tell the truth, and they think it's hell. ",
        "                                                   ---  Harry S Truman  ",
        "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
        "headmistressship",
        "aardvark",
        "😍😀🙌💃😍😍😍🙌",
        "abcdefghijklmnopqrstuvwxyz"
    ]
    print([
        isCollapsible(x) for x in xs
    ])


# MAIN ---
if __name__ == '__main__':
    main()

```

