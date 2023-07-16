# Determine if a string is squeezable

## Task Link
[Rosetta Code - Determine if a string is squeezable](https://rosettacode.org/wiki/Determine_if_a_string_is_squeezable)

## Java Code
### java_code_1.txt
```java
//  Title:  Determine if a string is squeezable

public class StringSqueezable {

    public static void main(String[] args) {
        String[] testStrings = new String[] {
                "", 
                "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ", 
                "..1111111111111111111111111111111111111111111111111111111111111117777888", 
                "I never give 'em hell, I just tell the truth, and they think it's hell. ", 
                "                                                    --- Harry S Truman  ",
                "122333444455555666666777777788888888999999999",
                "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
                "headmistressship"};

        String[] testChar = new String[] {
                " ", 
                "-", 
                "7", 
                ".", 
                " -r",
                "5",
                "e",
                "s"};
        for ( int testNum = 0 ; testNum < testStrings.length ; testNum++ ) {
            String s = testStrings[testNum];
            for ( char c : testChar[testNum].toCharArray() ) {
                String result = squeeze(s, c);
                System.out.printf("use: '%c'%nold:  %2d <<<%s>>>%nnew:  %2d <<<%s>>>%n%n", c, s.length(), s, result.length(), result);
            }
        }
    }
    
    private static String squeeze(String in, char include) {
        StringBuilder sb = new StringBuilder();
        for ( int i = 0 ; i < in.length() ; i++ ) {
            if ( i == 0 || in.charAt(i-1) != in.charAt(i) || (in.charAt(i-1) == in.charAt(i) && in.charAt(i) != include)) {
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

def squeezer(s, txt):
    return ''.join(item if item == s else ''.join(grp)
                   for item, grp in groupby(txt))

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
    squeezers = ' ,-,7,., -r,e,s,a,😍'.split(',')
    for txt, chars in zip(strings, squeezers):
        this = "Original"
        print(f"\n{this:14} Size: {len(txt)} «««{txt}»»»" )
        for ch in chars:
            this = f"Squeezer '{ch}'"
            sqz = squeezer(ch, txt)
            print(f"{this:>14} Size: {len(sqz)} «««{sqz}»»»" )

```

