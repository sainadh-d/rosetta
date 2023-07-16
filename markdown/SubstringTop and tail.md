# Substring/Top and tail

## Task Link
[Rosetta Code - Substring/Top and tail](https://rosettacode.org/wiki/Substring/Top_and_tail)

## Java Code
### java_code_1.txt
```java
String strOrig = 'brooms';
String str1 = strOrig.substring(1, strOrig.length());
system.debug(str1);
String str2 = strOrig.substring(0, strOrig.length()-1);
system.debug(str2);
String str3 = strOrig.substring(1, strOrig.length()-1);
system.debug(str3);

// Regular Expressions approach
String strOrig = 'brooms';
String str1 = strOrig.replaceAll( '^.', '' );
system.debug(str1);
String str2 = strOrig.replaceAll( '.$', '' ) ;
system.debug(str2);
String str3 = strOrig.replaceAll( '^.|.$', '' );
system.debug(str3);

```

### java_code_2.txt
```java
public class RM_chars {
  public static void main( String[] args ){
    System.out.println( "knight".substring( 1 ) );
    System.out.println( "socks".substring( 0, 4 ) );
    System.out.println( "brooms".substring( 1, 5 ) );
      // first, do this by selecting a specific substring
      // to exclude the first and last characters
    
    System.out.println( "knight".replaceAll( "^.", "" ) );
    System.out.println( "socks".replaceAll( ".$", "" ) );
    System.out.println( "brooms".replaceAll( "^.|.$", "" ) );
      // then do this using a regular expressions
  }
}

```

## Python Code
### python_code_1.txt
```python
print "knight"[1:]     # strip first character
print "socks"[:-1]     # strip last character
print "brooms"[1:-1]   # strip both first and last characters

```

### python_code_2.txt
```python
from functools import (reduce)


def main():
    for xs in transpose(
        (chunksOf(3)(
            ap([tail, init, compose(init)(tail)])(
                ['knights', 'socks', 'brooms']
            )
        ))
    ):
        print(xs)


# GENERIC -------------------------------------------------

# tail :: [a] -> [a]
def tail(xs):
    return xs[1:]


# init::[a] - > [a]
def init(xs):
    return xs[:-1]


# ap (<*>) :: [(a -> b)] -> [a] -> [b]
def ap(fs):
    return lambda xs: reduce(
        lambda a, f: a + reduce(
            lambda a, x: a + [f(x)], xs, []
        ), fs, []
    )


# chunksOf :: Int -> [a] -> [[a]]
def chunksOf(n):
    return lambda xs: reduce(
        lambda a, i: a + [xs[i:n + i]],
        range(0, len(xs), n), []
    ) if 0 < n else []


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    return lambda f: lambda x: g(f(x))


# transpose :: [[a]] -> [[a]]
def transpose(xs):
    return list(map(list, zip(*xs)))


if __name__ == '__main__':
    main()

```

