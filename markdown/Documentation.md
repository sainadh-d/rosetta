# Documentation

## Task Link
[Rosetta Code - Documentation](https://rosettacode.org/wiki/Documentation)

## Java Code
### java_code_1.txt
```java
/**
 * This is a class documentation comment. This text shows at the top of the page for this class
 * @author Joe Schmoe
 */
public class Doc{
   /**
    * This is a field comment for a variable
    */
   private String field;

   /**
    * This is a method comment. It has parameter tags (param), an exception tag (throws),
    * and a return value tag (return).
    *
    * @param num a number with the variable name "num"
    * @throws BadException when something bad happens
    * @return another number
    */
   public int method(long num) throws BadException{
      //...code here
   }
}

```

## Python Code
### python_code_1.txt
```python
class Doc(object):
   """
   This is a class docstring. Traditionally triple-quoted strings are used because
   they can span multiple lines and you can include quotation marks without escaping.
   """
   def method(self, num):
      """This is a method docstring."""
      pass

```

### python_code_2.txt
```python
>>> def somefunction():
	"takes no args and returns None after doing not a lot"

	
>>> help(somefunction)
Help on function somefunction in module __main__:

somefunction()
    takes no args and returns None after doing not a lot

>>>

```

