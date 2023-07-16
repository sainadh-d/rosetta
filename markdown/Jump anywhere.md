# Jump anywhere

## Task Link
[Rosetta Code - Jump anywhere](https://rosettacode.org/wiki/Jump_anywhere)

## Java Code
### java_code_1.txt
```java
loop1: while (x != 0) {
    loop2: for (int i = 0; i < 10; i++) {
        loop3: do {
            //some calculations...
            if (/*some condition*/) {
                //this continue will skip the rest of the while loop code and start it over at the next iteration
                continue loop1;
            }
            //more calculations skipped by the continue if it is executed
            if (/*another condition*/) {
                //this break will end the for loop and jump to its closing brace
                break loop2;
            }
        } while (y < 10);
        //loop2 calculations skipped if the break is executed
    }
    //loop1 calculations executed after loop2 is done or if the break is executed, skipped if the continue is executed
}

```

### java_code_2.txt
```java
public class FizzBuzzThrower {
    public static void main( String [] args ) {
        for ( int i = 1; i <= 30; i++ ) {
            try {
                String message = "";
                if ( i % 3 == 0 ) message = "Fizz";
                if ( i % 5 == 0 ) message += "Buzz";
                if ( ! "".equals( message ) ) throw new RuntimeException( message );
                System.out.print( i );
            } catch ( final RuntimeException x ) {
                System.out.print( x.getMessage() );
            } finally {
                System.out.println();
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# Example 2: Restarting a loop:
from goto import goto, label
label .start
for i in range(1, 4):
    print i
    if i == 2:
        try:
            output = message
        except NameError:
            print "Oops - forgot to define 'message'!  Start again."
            message = "Hello world"
            goto .start
print output, "\n"

```

