# Sierpinski triangle

## Task Link
[Rosetta Code - Sierpinski triangle](https://rosettacode.org/wiki/Sierpinski_triangle)

## Java Code
### java_code_1.txt
```java
public class SierpinskiTriangle {

    public static void main(String[] args) {
        System.out.println(getSierpinskiTriangle(4));
    }
    
    private static final String getSierpinskiTriangle(int n) {
        if ( n == 0 ) {
            return "*";
        }

        String s = getSierpinskiTriangle(n-1);
        String [] split = s.split("\n");
        int length = split.length;

        //  Top triangle
        StringBuilder sb = new StringBuilder();
        String top = buildSpace((int)Math.pow(2, n-1));
        for ( int i = 0 ; i < length ;i++ ) {
            sb.append(top);
            sb.append(split[i]);
            sb.append("\n");
        }
        
        //  Two triangles side by side
        for ( int i = 0 ; i < length ;i++ ) {
            sb.append(split[i]);
            sb.append(buildSpace(length-i));
            sb.append(split[i]);
            sb.append("\n");
        }
        return sb.toString();
    }
    
    private static String buildSpace(int n) {
        StringBuilder sb = new StringBuilder();
        while ( n > 0 ) {
            sb.append(" ");
            n--;
        }
        return sb.toString();
    }
    
}

```

### java_code_2.txt
```java
void setup() {
  size(410, 230);
  background(255);
  fill(0);
  sTriangle (10, 25, 100, 5);
}
 
void sTriangle(int x, int y, int l, int n) {
    if( n == 0) text("*", x, y);
    else {
        sTriangle(x, y+l, l/2, n-1);
        sTriangle(x+l, y, l/2, n-1);
        sTriangle(x+l*2, y+l, l/2, n-1);
    }
}

```

### java_code_3.txt
```java
void setup() {
  print(getSierpinskiTriangle(3));
}
String getSierpinskiTriangle(int n) {
  if ( n == 0 ) {
    return "*";
  }
  String s = getSierpinskiTriangle(n-1);
  String [] split = s.split("\n");
  int length = split.length;
  //  Top triangle
  String ns = "";
  String top = buildSpace((int)pow(2, n-1));
  for ( int i = 0; i < length; i++ ) {
    ns += top;
    ns += split[i];
    ns += "\n";
  }
  //  Two triangles side by side
  for ( int i = 0; i < length; i++ ) {
    ns += split[i];
    ns += buildSpace(length-i);
    ns += split[i];
    ns += "\n";
  }
  return ns.toString();
}

String buildSpace(int n) {
  String ns = "";
  while ( n > 0 ) {
    ns += " ";
    n--;
  }
  return ns;
}

```

## Python Code
### python_code_1.txt
```python
def sierpinski(n):
    d = ["*"]
    for i in xrange(n):
        sp = " " * (2 ** i)
        d = [sp+x+sp for x in d] + [x+" "+x for x in d]
    return d

print "\n".join(sierpinski(4))

```

### python_code_2.txt
```python
import functools

def sierpinski(n):

    def aggregate(TRIANGLE, I):
        SPACE = " " * (2 ** I)
        return [SPACE+X+SPACE for X in TRIANGLE] + [X+" "+X for X in TRIANGLE]

    return functools.reduce(aggregate, range(n), ["*"])

print("\n".join(sierpinski(4)))

```

### python_code_3.txt
```python
'''Sierpinski triangle'''

from functools import reduce
from operator import add


# sierpinski :: Int -> String
def sierpinski(n):
    '''Nth iteration of a Sierpinksi triangle.'''
    def go(xs, i):
        s = ' ' * (2 ** i)
        return concatMap(lambda x: [s + x + s])(xs) + (
            concatMap(lambda x: [x + ' ' + x])(xs)
        )
    return '\n'.join(reduce(go, range(n), '*'))


# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    '''A concatenated list or string over which a function f
       has been mapped.
       The list monad can be derived by using an (a -> [b])
       function which wraps its output in a list (using an
       empty list to represent computational failure).
    '''
    return lambda xs: (
        reduce(add, map(f, xs), [])
    )


print(sierpinski(4))

```

### python_code_4.txt
```python
x = 1
while True:
	print(bin(x)[2:].replace('0', ' '))
	x ^= x<<1

```

