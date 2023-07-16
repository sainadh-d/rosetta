# Test a function

## Task Link
[Rosetta Code - Test a function](https://rosettacode.org/wiki/Test_a_function)

## Java Code
### java_code_1.txt
```java
import static ExampleClass.pali; // or from wherever it is defined
import static ExampleClass.rPali; // or from wherever it is defined
import org.junit.*;
public class PalindromeTest extends junit.framework.TestCase {
    @Before
    public void setUp(){
        //runs before each test
        //set up instance variables, network connections, etc. needed for all tests
    }
    @After
    public void tearDown(){
        //runs after each test
        //clean up instance variables (close files, network connections, etc.).
    }

    /**
     * Test the pali(...) method.
     */
    @Test
    public void testNonrecursivePali() throws Exception {
        assertTrue(pali("abcba"));
        assertTrue(pali("aa"));
        assertTrue(pali("a"));
        assertTrue(pali(""));
        assertFalse(pali("ab"));
        assertFalse(pali("abcdba"));
    }
    /**
     * Test the rPali(...) method.
     */
    @Test
    public void testRecursivePali() throws Exception {
        assertTrue(rPali("abcba"));
        assertTrue(rPali("aa"));
        assertTrue(rPali("a"));
        assertTrue(rPali(""));
        assertFalse(rPali("ab"));
        assertFalse(rPali("abcdba"));
    }

    /**
     * Expect a WhateverExcpetion
     */
    @Test(expected=WhateverException.class)
    public void except(){
        //some code that should throw a WhateverException
    }
}

```

### java_code_2.txt
```java
public class RunTests{
  public static main(String[] args){
    org.junit.runner.JUnitCore.runClasses(PalindromeTest.class/*, other classes here if you have more*/);
  }
}

```

## Python Code
### python_code_1.txt
```python
def is_palindrome(s):
    '''
        >>> is_palindrome('')
        True
        >>> is_palindrome('a')
        True
        >>> is_palindrome('aa')
        True
        >>> is_palindrome('baa')
        False
        >>> is_palindrome('baab')
        True
        >>> is_palindrome('ba_ab')
        True
        >>> is_palindrome('ba_ ab')
        False
        >>> is_palindrome('ba _ ab')
        True
        >>> is_palindrome('ab'*2)
        False
        >>> x = 'ab' *2**15
        >>> len(x)
        65536
        >>> xreversed = x[::-1]
        >>> is_palindrome(x+xreversed)
        True
        >>> len(x+xreversed)
        131072
        >>> 
    '''
    return s == s[::-1]

def _test():
    import doctest
    doctest.testmod()
    #doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()

```

