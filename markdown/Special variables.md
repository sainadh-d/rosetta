# Special variables

## Task Link
[Rosetta Code - Special variables](https://rosettacode.org/wiki/Special_variables)

## Java Code
### java_code_1.txt
```java
Object object = null

```

### java_code_2.txt
```java
boolean value = true

```

### java_code_3.txt
```java
this.object

```

### java_code_4.txt
```java
super(value)

```

### java_code_5.txt
```java
import static java.lang.Math.*;

```

### java_code_6.txt
```java
double area = PI * (2 * 2);

```

### java_code_7.txt
```java
public static void main(String[] args)

```

### java_code_8.txt
```java
import java.util.Arrays;

public class SpecialVariables {

    public static void main(String[] args) {

        //String-Array args contains the command line parameters passed to the program
        //Note that the "Arrays.toString()"-call is just used for pretty-printing
        System.out.println(Arrays.toString(args));

        //<Classname>.class might qualify as a special variable, since it always contains a Class<T>-object that
        //is used in Reflection
        System.out.println(SpecialVariables.class);


        //The following are not really "variables", since they are properly encapsulated:

        //System.getenv() returns a String-String-Map of environment-variables
        System.out.println(System.getenv());

        //System.getProperties() returns a Map of "things somebody might want to know", including OS and architecture
        // the Java VM runs on, various paths like home direcoty of the user that runs the program, class (library) paths,
        System.out.println(System.getProperties());

        //Runtime.getRuntime() returns a Runtime-Object that contains "changing" data about the running Java VM's 
        // environment, like available processor cores or available RAM 
        System.out.println(Runtime.getRuntime().availableProcessors());

    }
}

```

## Python Code
### python_code_1.txt
```python
names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print( '\n'.join(' '.join(names[i:i+8]) for i in range(0, len(names), 8)) )

```

