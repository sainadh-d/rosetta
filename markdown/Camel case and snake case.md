# Camel case and snake case

## Task Link
[Rosetta Code - Camel case and snake case](https://rosettacode.org/wiki/Camel_case_and_snake_case)

## Java Code
### java_code_1.txt
```java
"snakeCase", "snake_case", "variable_10_case", "variable10Case", "ɛrgo rE tHis",
"hurry-up-joe!", "c://my-docs/happy_Flag-Day/12.doc", "  spaces  "

```

### java_code_2.txt
```java
import java.util.List;

public final class CamelCaseAndSnakeCase {

	public static void main(String[] aArgs) {
		List<String> variableNames = List.of( "snakeCase", "snake_case", "variable_10_case", "variable10Case",
			"ergo rE tHis", "hurry-up-joe!", "c://my-docs/happy_Flag-Day/12.doc", "  spaces  ");
		
		System.out.println(String.format("%48s", "=== To snake_case ==="));
		for ( String text : variableNames ) {
			System.out.println(String.format("%34s%s%s", text, " --> ", toSnakeCase(text)));
		}

		System.out.println();
		System.out.println(String.format("%48s", "=== To camelCase ==="));
		for ( String text : variableNames ) {
			System.out.println(String.format("%34s%s%s", text, " --> ", toCamelCase(text)));
		}
	}	
	
	private static String toSnakeCase(String aCamel) {
		aCamel = aCamel.trim().replace(SPACE, UNDERSCORE).replace(HYPHEN, UNDERSCORE);
	    StringBuilder snake = new StringBuilder();
	    boolean first = true;
	    for ( char ch : aCamel.toCharArray() ) {
	        if ( first ) {
	            snake.append(ch);
	            first = false;
	        } else if ( ! first && Character.isUpperCase(ch) ) {
	            if ( snake.toString().endsWith(UNDERSCORE) ) {
	                snake.append(Character.toLowerCase(ch));
	            } else {
	                snake.append(UNDERSCORE + Character.toLowerCase(ch));
	            }
	        } else {
	            snake.append(ch);
	        }
	    }
	    return snake.toString();
		
	}
	
	private static String toCamelCase(String aSnake) {
		aSnake = aSnake.trim().replace(SPACE, UNDERSCORE).replace(HYPHEN, UNDERSCORE);
	    StringBuilder camel = new StringBuilder();
	    boolean underscore = false;
	    for ( char ch : aSnake.toCharArray() ) {
	        if ( Character.toString(ch).equals(UNDERSCORE) ) {
	            underscore = true;
	        } else if ( underscore ) {
	            camel.append(Character.toUpperCase(ch));
	            underscore = false;
	        } else {
	            camel.append(ch);
	        }
	    }
	    return camel.toString();		
	}
	
	private static final String SPACE = " ";
	private static final String UNDERSCORE = "_";
	private static final String HYPHEN = "-";
	
}

```

## Python Code
### python_code_1.txt
```python
""" https://rosettacode.org/wiki/Camel_case_and_snake_case """

import re

def snakeToCamelCase(nam, sep='[_]+', lcmiddle=False):
    """ convert snake '_' separator case to camel case """
    if nam == '':
        return nam
    words = re.split(sep, nam.strip())
    if lcmiddle:
        words = [w.lower() for w in words]
    words[1:] = [w[0].upper() + w[1:] for w in words[1:] if len(w) > 0]
    return ''.join(words)


def spaceToCamelCase(nam):
    """ convert space case to camel case """
    return snakeToCamelCase(nam, sep='\s+')

def kebabToCamelCase(nam):
    """ convert kebab '-' case to camel case """
    return snakeToCamelCase(nam, sep='[\-]+')

def periodToCamelCase(nam):
    """ convert period '.' case to camel case """
    return snakeToCamelCase(nam, sep='[\.]+')

def allsepToCamelCase(nam):
    """ convert all separators in allsep to camel case """
    return snakeToCamelCase(nam, sep='[ \-_\.]+')

def lowermiddle_allsepToCamelCase(nam):
    """ convert all separators to camel case, and all but word starts to lowercase """
    return snakeToCamelCase(nam, sep='[ \-_\.]+', lcmiddle=True)

def camel_to_snake_case(nam, sep='_', allsep='[_]+', lcmiddle=True):
    """ convert camel case to snake case (separate with '_') """
    nam = re.sub('([A-Z]+)', sep + r"\1", nam.strip())
    sep1 = '\\' + sep if sep == '.' else sep
    if lcmiddle:
        nam = sep.join([w.lower() for w in nam.split(sep1) if len(w) > 0])
    else:
        nam = sep.join([w[0].lower() + w[1:] for w in nam.split(sep1) if len(w) > 0])
    return re.sub(allsep, sep, nam)

def preserve_midcaps_camel_to_snake_case(nam):
    return camel_to_snake_case(nam, lcmiddle=False)

def allsep_to_snake_case(nam):
    return camel_to_snake_case(nam, allsep='[ \-\._]+')

def allsep_to_kebab_case(nam):
    return camel_to_snake_case(nam, allsep='[ \-\._]+', sep='-')

def allsep_to_space_case(nam):
    return camel_to_snake_case(nam, allsep='[ \-\._]+', sep=' ')

def allsep_to_period_case(nam):
    return camel_to_snake_case(nam, allsep='[ \-\._]+', sep='.')

def allsep_to_slash_case(nam):
    return camel_to_snake_case(nam, allsep='[ \-\._]+', sep='/')

for f in [
    snakeToCamelCase,
    spaceToCamelCase,
    kebabToCamelCase,
    periodToCamelCase,
    allsepToCamelCase,
    lowermiddle_allsepToCamelCase,
    camel_to_snake_case,
    preserve_midcaps_camel_to_snake_case,
    allsep_to_snake_case,
    allsep_to_kebab_case,
    allsep_to_space_case,
    allsep_to_period_case,
    allsep_to_slash_case]:
    print(f"Testing function {f}:")
    for teststring in [
        "snakeCase",
        "snake_case",
        "snake-case",
        "snake case",
        "snake CASE",
        "snake.case",
        "variable_10_case",
        "variable10Case",
        "ɛrgo rE tHis",
        "hurry-up-joe!",
        "c://my-docs/happy_Flag-Day/12.doc",
        " spaces "]:
        print(teststring.rjust(36), " => ", f(teststring))
    print()

```

