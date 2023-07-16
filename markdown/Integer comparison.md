# Integer comparison

## Task Link
[Rosetta Code - Integer comparison](https://rosettacode.org/wiki/Integer_comparison)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class compInt {
   public static void main(String[] args) {
       try {
           BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

           int nbr1 = Integer.parseInt(in.readLine());
           int nbr2 = Integer.parseInt(in.readLine());

           if(nbr1<nbr2)
               System.out.println(nbr1 + " is less than " + nbr2);

           if(nbr1>nbr2)
                System.out.println(nbr1 + " is greater than " + nbr2);

           if(nbr1==nbr2)
                System.out.println(nbr1 + " is equal to " + nbr2);
       } catch(IOException e) { }
   }
}

```

## Python Code
### python_code_1.txt
```python
let a = input('Enter value of a: ')
let b = input('Enter value of b: ')

if a < b:
    print 'a is less than b'
elif a > b:
    print 'a is greater than b'
elif a == b:
    print 'a is equal to b'

```

### python_code_2.txt
```python
#!/usr/bin/env python
a = input('Enter value of a: ')
b = input('Enter value of b: ')

if a < b:
    print 'a is less than b'
elif a > b:
    print 'a is greater than b'
elif a == b:
    print 'a is equal to b'

```

### python_code_3.txt
```python
#!/usr/bin/env python
import sys
try:
   a = input('Enter value of a: ')
   b = input('Enter value of b: ')
except (ValueError, EnvironmentError), err:
   print sys.stderr, "Erroneous input:", err
   sys.exit(1)

dispatch = {
    -1: 'is less than',
     0: 'is equal to',
     1: 'is greater than'
     }
 print a, dispatch[cmp(a,b)], b

```

