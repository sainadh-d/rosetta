# Strip comments from a string

## Task Link
[Rosetta Code - Strip comments from a string](https://rosettacode.org/wiki/Strip_comments_from_a_string)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class StripLineComments{
    public static void main( String[] args ){
	if( args.length < 1 ){
	    System.out.println("Usage: java StripLineComments StringToProcess");
	}
	else{
	    String inputFile = args[0];
	    String input = "";
	    try{
		BufferedReader reader = new BufferedReader( new FileReader( inputFile ) );
		String line = "";
		while((line = reader.readLine()) != null){
		    System.out.println( line.split("[#;]")[0] );
		}
	    }
	    catch( Exception e ){
		e.printStackTrace();
	    }
	}
    }
}

```

## Python Code
### python_code_1.txt
```python
def remove_comments(line, sep):
    for s in sep:
        i = line.find(s)
        if i >= 0:
            line = line[:i]
    return line.strip()

# test
print remove_comments('apples ; pears # and bananas', ';#')
print remove_comments('apples ; pears # and bananas', '!')

```

### python_code_2.txt
```python
import re

m = re.match(r'^([^#]*)#(.*)$', line)
if m:  # The line contains a hash / comment
    line = m.group(1)

```

### python_code_3.txt
```python
'''Comments stripped with itertools.takewhile'''

from itertools import takewhile


# stripComments :: [Char] -> String -> String
def stripComments(cs):
    '''The lines of the input text, with any
       comments (defined as starting with one
       of the characters in cs) stripped out.
    '''
    def go(cs):
        return lambda s: ''.join(
            takewhile(lambda c: c not in cs, s)
        ).strip()
    return lambda txt: '\n'.join(map(
        go(cs),
        txt.splitlines()
    ))


if __name__ == '__main__':
    print(
        stripComments(';#')(
            '''apples, pears # and bananas
               apples, pears ; and bananas
            '''
        )
    )

```

