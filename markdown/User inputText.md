# User input/Text

## Task Link
[Rosetta Code - User input/Text](https://rosettacode.org/wiki/User_input/Text)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;

public class GetInput {
    public static void main(String[] args) throws Exception {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = s.nextLine();
        System.out.print("Enter an integer: ");
        int i = Integer.parseInt(s.next());
    }
}

```

### java_code_2.txt
```java
import java.util.Scanner;

public class GetInput {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String string = stdin.nextLine();
        int number = stdin.nextInt();
    }
}

```

## Python Code
### python_code_1.txt
```python
   string = raw_input("Input a string: ")

```

### python_code_2.txt
```python
   string = input("Input a string: ")

```

### python_code_3.txt
```python
   number = input("Input a number: ")  # Deprecated, please don't use.

```

### python_code_4.txt
```python
   number = eval(input("Input a number: ")) # Evil, please don't use.

```

### python_code_5.txt
```python
   number = float(raw_input("Input a number: "))

```

### python_code_6.txt
```python
   number = float(input("Input a number: "))

```

