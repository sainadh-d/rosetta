# Split a character string based on change of character

## Task Link
[Rosetta Code - Split a character string based on change of character](https://rosettacode.org/wiki/Split_a_character_string_based_on_change_of_character)

## Java Code
### java_code_1.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

```

### java_code_2.txt
```java
String split(String string) {
    Pattern pattern = Pattern.compile("(.)\\1*");
    Matcher matcher = pattern.matcher(string);
    StringBuilder strings = new StringBuilder();
    int index = 0;
    while (matcher.find()) {
        if (index++ != 0)
            strings.append(", ");
        strings.append(matcher.group());
    }
    return strings.toString();
}

```

### java_code_3.txt
```java
package org.rosettacode;

import java.util.ArrayList;
import java.util.List;


/**
 * This class provides a main method that will, for each arg provided,
 * transform a String into a list of sub-strings, where each contiguous
 * series of characters is made into a String, then the next, and so on,
 * and then it will output them all separated by a comma and a space.
 */
public class SplitStringByCharacterChange {
    
    public static void main(String... args){
        for (String string : args){
            
            List<String> resultStrings = splitStringByCharacter(string);
            String output = formatList(resultStrings);
            System.out.println(output);
        }
    }
    
    /**
     * @param string String - String to split
     * @return List<\String> - substrings of contiguous characters
     */
    public static List<String> splitStringByCharacter(String string){
        
        List<String> resultStrings = new ArrayList<>();
        StringBuilder currentString = new StringBuilder();
        
        for (int pointer = 0; pointer < string.length(); pointer++){
            
            currentString.append(string.charAt(pointer));
            
            if (pointer == string.length() - 1 
                    || currentString.charAt(0) != string.charAt(pointer + 1)) {
                resultStrings.add(currentString.toString());
                currentString = new StringBuilder();
            }
        }
        
        return resultStrings;
    }
    
    /**
     * @param list List<\String> - list of strings to format as a comma+space-delimited string
     * @return String
     */
    public static String formatList(List<String> list){
        
        StringBuilder output = new StringBuilder();
        
        for (int pointer = 0; pointer < list.size(); pointer++){
            output.append(list.get(pointer));
            
            if (pointer != list.size() - 1){
                output.append(", ");
            }
        }
        
        return output.toString();
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import groupby

def splitter(text):
    return ', '.join(''.join(group) for key, group in groupby(text))

if __name__ == '__main__':
    txt = 'gHHH5YY++///\\'      # Note backslash is the Python escape char.
    print(f'Input: {txt}\nSplit: {splitter(txt)}')

```

### python_code_2.txt
```python
def splitterz(text):
    return (''.join(x + ('' if x == nxt else ', ') 
            for x, nxt in zip(txt, txt[1:] + txt[-1])))

if __name__ == '__main__':
    txt = 'gHHH5YY++///\\'
    print(splitterz(txt))

```

### python_code_3.txt
```python
import itertools

try: input = raw_input
except: pass

s = input()
groups = []
for _, g in itertools.groupby(s):
    groups.append(''.join(g))
print('      input string:  %s' % s)
print('     output string:  %s' % ', '.join(groups))

```

