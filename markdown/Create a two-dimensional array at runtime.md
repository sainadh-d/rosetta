# Create a two-dimensional array at runtime

## Task Link
[Rosetta Code - Create a two-dimensional array at runtime](https://rosettacode.org/wiki/Create_a_two-dimensional_array_at_runtime)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class twoDimArray {
  public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int nbr1 = in.nextInt();
        int nbr2 = in.nextInt();
        
        double[][] array = new double[nbr1][nbr2];
        array[0][0] = 42.0;
        System.out.println("The number at place [0 0] is " + array[0][0]);
  }
}

```

## Python Code
### python_code_1.txt
```python
width = int(raw_input("Width of myarray: "))
height = int(raw_input("Height of Array: "))
myarray = [[0] * width for i in range(height)]
myarray[0][0] = 3.5
print (myarray[0][0])

```

### python_code_2.txt
```python
myarray = {(w,h): 0 for w in range(width) for h in range(height)}
# or, in pre 2.7 versions of Python: myarray = dict(((w,h), 0) for w in range(width) for h in range(height))
myarray[(0,0)] = 3.5
print (myarray[(0,0)])

```

