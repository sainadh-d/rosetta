# Reverse a string

## Task Link
[Rosetta Code - Reverse a string](https://rosettacode.org/wiki/Reverse_a_string)

## Java Code
### java_code_1.txt
```java
String str = 'Hello World!';
str = str.reverse();
system.debug(str);

```

### java_code_2.txt
```java
String reversed = new StringBuilder("as⃝df̅").reverse().toString(); // fd⃝sa
String reversed = new StringBuffer("as⃝df̅").reverse().toString(); // fd⃝sa

```

### java_code_3.txt
```java
String string = "as⃝df̅";
StringBuilder reversed = new StringBuilder();
for (int index = string.length() - 1; index >= 0; index--)
    reversed.append(string.charAt(index));
reversed; // fd⃝sa

```

### java_code_4.txt
```java
import java.text.BreakIterator;

public class Reverse {
  /* works with Java 20+ only
   * cf. https://bugs.openjdk.org/browse/JDK-8291660
   */
  public static StringBuilder graphemeReverse(String text) {
    BreakIterator boundary = BreakIterator.getCharacterInstance();
    boundary.setText(text);
    StringBuilder reversed = new StringBuilder();
    int end = boundary.last();
    int start = boundary.previous();
    while (start != BreakIterator.DONE) {
      reversed.append(text.substring(start, end));
      end = start;
      start = boundary.previous();
    }
    return reversed;
  }
  public static void main(String[] args) throws Exception {
    String a = "as⃝df̅";
    System.out.println(graphemeReverse(a)); // f̅ds⃝a
  }
}

```

## Python Code
### python_code_1.txt
```python
input()[::-1]

```

### python_code_2.txt
```python
string[::-1]

```

### python_code_3.txt
```python
''.join(reversed(string))

```

### python_code_4.txt
```python
import unicodedata

def ureverse(ustring):
    'Reverse a string including unicode combining characters'
    groupedchars = []
    uchar = list(ustring)
    while uchar:
        if unicodedata.combining(uchar[0]) != 0:
            groupedchars[-1] += uchar.pop(0)
        else:
            groupedchars.append(uchar.pop(0))
    # Grouped reversal
    groupedchars = groupedchars[::-1]
 
    return ''.join(groupedchars)

def say_string(s):
    return ' '.join([s, '=', ' | '.join(unicodedata.name(ch, '') for ch in s)])

def say_rev(s):
    print(f"Input:              {say_string(s)}")
    print(f"Character reversed: {say_string(s[::-1])}")
    print(f"Unicode reversed:   {say_string(ureverse(s))}")
    print(f"Unicode reverse²:   {say_string(ureverse(ureverse(s)))}")
        
if __name__ == '__main__':
    ucode = ''.join(chr(int(n[2:], 16)) for n in 
                     'U+0041 U+030A U+0073 U+0074 U+0072 U+006F U+0308 U+006D'.split())
    say_rev(ucode)

```

### python_code_5.txt
```python
ucode = ''.join(chr(int(n[2:], 16)) for n in 
                 'U+006B U+0301 U+0075 U+032D U+006F U+0304 U+0301 U+006E'.split())
say_rev(ucode)

```

### python_code_6.txt
```python
ucode = ''.join(chr(int(n, 16))
                 for n in ['61', '73', '20dd', '64', '66', '305'])
say_rev(ucode)

```

