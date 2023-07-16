# Mad Libs

## Task Link
[Rosetta Code - Mad Libs](https://rosettacode.org/wiki/Mad_Libs)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class MadLibs {
    
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
        String name, gender, noun;
        
        System.out.print("Enter a name: ");
        name = input.next();
        
        System.out.print("He or she: ");
        gender = input.next();
        
        System.out.print("Enter a noun: ");
        noun = input.next();
        
        System.out.println("\f" + name + " went for a walk in the park. " + gender + "\nfound a " + noun + ". " + name + " decided to take it home.");
        
    
    }
}

```

## Python Code
### python_code_1.txt
```python
import re

# Optional Python 2.x compatibility
#try: input = raw_input
#except: pass

template = '''<name> went for a walk in the park. <he or she>
found a <noun>. <name> decided to take it home.'''

def madlibs(template):
    print('The story template is:\n' + template)
    fields = sorted(set( re.findall('<[^>]+>', template) ))
    values = input('\nInput a comma-separated list of words to replace the following items'
                   '\n  %s: ' % ','.join(fields)).split(',')
    story = template
    for f,v in zip(fields, values):
        story = story.replace(f, v)
    print('\nThe story becomes:\n\n' + story)

madlibs(template)

```

