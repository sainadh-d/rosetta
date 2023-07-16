# String comparison

## Task Link
[Rosetta Code - String comparison](https://rosettacode.org/wiki/String_comparison)

## Java Code
### java_code_1.txt
```java
public class Compare
{
	/**
	 * Test in the developer console:
	 * Compare.compare('Hello', 'Hello');
	 * Compare.compare('5', '5.0');
	 * Compare.compare('java', 'Java');
	 * Compare.compare('ĴÃVÁ', 'ĴÃVÁ');
	*/
    
    public static void compare (String A, String B)
    {
        if (A.equals(B))
            System.debug(A + ' and  ' + B + ' are lexically equal.');
        else
            System.debug(A + ' and  ' + B + ' are not lexically equal.');

        if (A.equalsIgnoreCase(B))
            System.debug(A + ' and  ' + B + ' are case-insensitive lexically equal.');
        else
            System.debug(A + ' and  ' + B + ' are not case-insensitive lexically equal.');
 
        if (A.compareTo(B) < 0)
            System.debug(A + ' is lexically before ' + B);
        else if (A.compareTo(B) > 0)
            System.debug(A + ' is lexically after ' + B);
 
        if (A.compareTo(B) >= 0)
            System.debug(A + ' is not lexically before ' + B);
        if (A.compareTo(B) <= 0)
            System.debug(A + ' is not lexically after ' + B);
 
        System.debug('The lexical relationship is: ' + A.compareTo(B));
    }
}

```

### java_code_2.txt
```java
public class Compare
{
    public static void main (String[] args)
    {
        compare("Hello", "Hello");
        compare("5", "5.0");
        compare("java", "Java");
        compare("ĴÃVÁ", "ĴÃVÁ");
        compare("ĴÃVÁ", "ĵãvá");
    }
    public static void compare (String A, String B)
    {
        if (A.equals(B))
            System.out.printf("'%s' and '%s' are lexically equal.", A, B);
        else
            System.out.printf("'%s' and '%s' are not lexically equal.", A, B);
        System.out.println();

        if (A.equalsIgnoreCase(B))
            System.out.printf("'%s' and '%s' are case-insensitive lexically equal.", A, B);
        else
            System.out.printf("'%s' and '%s' are not case-insensitive lexically equal.", A, B);
        System.out.println();
    
        if (A.compareTo(B) < 0)
            System.out.printf("'%s' is lexically before '%s'.\n", A, B);
        else if (A.compareTo(B) > 0)
            System.out.printf("'%s' is lexically after '%s'.\n", A, B);

        if (A.compareTo(B) >= 0)
            System.out.printf("'%s' is not lexically before '%s'.\n", A, B);
        if (A.compareTo(B) <= 0)
            System.out.printf("'%s' is not lexically after '%s'.\n", A, B);

        System.out.printf("The lexical relationship is: %d\n", A.compareTo(B));
        System.out.printf("The case-insensitive lexical relationship is: %d\n\n", A.compareToIgnoreCase(B));
    }
}

```

## Python Code
### python_code_2.txt
```python
def compare(a, b):
    print("\n%r is of type %r and %r is of type %r"
          % (a, type(a), b, type(b)))
    if a <  b:      print('%r is strictly less than  %r' % (a, b))
    if a <= b:      print('%r is less than or equal to %r' % (a, b))
    if a >  b:      print('%r is strictly greater than  %r' % (a, b))
    if a >= b:      print('%r is greater than or equal to %r' % (a, b))
    if a == b:      print('%r is equal to %r' % (a, b))
    if a != b:      print('%r is not equal to %r' % (a, b))
    if a is b:      print('%r has object identity with %r' % (a, b))
    if a is not b:  print('%r has negated object identity with %r' % (a, b))

compare('YUP', 'YUP')
compare('BALL', 'BELL')
compare('24', '123')
compare(24, 123)
compare(5.0, 5)

```

