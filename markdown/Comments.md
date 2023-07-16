# Comments

## Task Link
[Rosetta Code - Comments](https://rosettacode.org/wiki/Comments)

## Java Code
### java_code_1.txt
```java
/*
 * This is a multi-line comment.
 */
Int i = 0;     // This is an end-of-line comment

```

### java_code_2.txt
```java
/* This is a comment */

```

### java_code_3.txt
```java
/*
 * This is
 * a multiple
 * line comment.
 */

```

### java_code_4.txt
```java
// This is a comment

```

### java_code_5.txt
```java
/** This is a Javadoc comment */

```

### java_code_6.txt
```java
/**
 * This is
 * a multiple
 * line Javadoc comment
 */

```

### java_code_7.txt
```java
public class JustComments {
    /*
    \u002A\u002F\u0070\u0075\u0062\u006C\u0069\u0063\u0020\u0073\u0074\u0061\u0074\u0069\u0063
    \u0020\u0076\u006F\u0069\u0064\u0020\u006D\u0061\u0069\u006E\u0028
    \u0053\u0074\u0072\u0069\u006E\u0067\u005B\u005D\u0061\u0072\u0067\u0073\u0029
    \u007B\u0053\u0079\u0073\u0074\u0065\u006D\u002E\u006F\u0075\u0074\u002E
    \u0070\u0072\u0069\u006E\u0074\u006C\u006E\u0028\u0022\u0048\u0065\u006C\u006C\u006F\u0022
    \u002B\u0022\u0020\u0057\u006F\u0072\u006C\u0064\u0021\u0022\u0029\u003B\u007D\u002F\u002A
    */
}

```

### java_code_8.txt
```java
// a single-line comment

/* a multi-line
   comment
*/

/*
 * a multi-line comment
 * with some decorative stars
 */

// comment out a code line
// println("foo");
 
// comment at the end of a line
println("foo bar"); // "baz"

```

## Python Code
### python_code_1.txt
```python
# Nim supports single-line comments

var x = 0 ## Documentation comments start with double hash characters.

var y = 0 ## Documentation comments are a proper part of the syntax (they're not discarded by parser, and a real part of AST).

#[
There are also multi-line comments
Everything inside of #[]# is commented.
]#

# You can also discard multiline statements:

discard """This can be considered as a "comment" too
This is multi-line"""

```

### python_code_2.txt
```python
# a single-line comment
 
"""
Not strictly a comment, bare multi-line strings are used
in Python as multi-line comments. They are also used as
documentation strings or 'docstrings' when placed as the
first element inside function or class definitions.
"""
 
# comment out a code line
# println("foo")

# comment at the end of a line
println("foo bar") # "baz"

# there is no way to make an inline comment

```

### python_code_3.txt
```python
# This is a comment
foo = 5 # You can also append comments to statements

```

### python_code_4.txt
```python
"""Un-assigned strings in triple-quotes might be used 
   as multi-line comments
"""

'''
   "triple quoted strings" can be delimited by either 'single' or "double" quote marks; and they can contain mixtures
   of other quote marks without any need to \escape\ them using any special characters.  They also may span multiple
   lines without special escape characters.
'''

```

### python_code_5.txt
```python
#!/usr/bin/env python
# Example of using doc strings
"""My Doc-string example"""
 
class Foo:
     '''Some documentation for the Foo class'''
     def __init__(self):
        "Foo's initialization method's documentation"
 
def bar():
    """documentation for the bar function"""
 
if __name__ == "__main__":
    print (__doc__)
    print (Foo.__doc__)
    print (Foo.__init__.__doc__)
    print (bar.__doc__)

```

