# Input loop

## Task Link
[Rosetta Code - Input loop](https://rosettacode.org/wiki/Input_loop)

## Java Code
### java_code_1.txt
```java
import java.io.InputStream;
import java.util.Scanner;

public class InputLoop {
    public static void main(String args[]) {
        // To read from stdin:
        InputStream source = System.in;

        /*
        Or, to read from a file:
        InputStream source = new FileInputStream(filename);

        Or, to read from a network stream:
        InputStream source = socket.getInputStream();
        */

        Scanner in = new Scanner(source);
        while(in.hasNext()){
            String input = in.next(); // Use in.nextLine() for line-by-line reading

            // Process the input here. For example, you could print it out:
            System.out.println(input);
        }
    }
}

```

### java_code_2.txt
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

public class InputLoop {
    public static void main(String args[]) {
        // To read from stdin:
        Reader reader = new InputStreamReader(System.in);

        /*
        Or, to read from a file:
        Reader reader = new FileReader(filename);

        Or, to read from a network stream:
        Reader reader = new InputStreamReader(socket.getInputStream());
        */

        try {
            BufferedReader inp = new BufferedReader(reader);
            while(inp.ready()) {
                int input = inp.read(); // Use in.readLine() for line-by-line

                // Process the input here. For example, you can print it out.
                System.out.println(input);
            }
        }  catch (IOException e) {
            // There was an input error.
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
while(True):
      x = input("What is your age? ")
      print(x)

```

### python_code_2.txt
```python
my_file = open(filename, 'r')
try:
    for line in my_file:
        pass # process line, includes newline
finally:
    my_file.close()

```

### python_code_3.txt
```python
#from __future__ import with_statement  # is not needed in Python 3.6

with open(filename, 'r') as f:
    for line in f:
        pass # process line, includes newline

```

### python_code_4.txt
```python
line = my_file.readline() # returns a line from the file
lines = my_file.readlines() # returns a list of the rest of the lines from the file

```

### python_code_5.txt
```python
import fileinput
for line in fileinput.input():
    pass # process line, includes newline

```

