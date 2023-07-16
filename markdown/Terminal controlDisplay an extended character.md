# Terminal control/Display an extended character

## Task Link
[Rosetta Code - Terminal control/Display an extended character](https://rosettacode.org/wiki/Terminal_control/Display_an_extended_character)

## Java Code
### java_code_1.txt
```java
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

public class Main
{
    public static void main(String[] args) throws UnsupportedEncodingException
    {
        PrintStream writer = new PrintStream(System.out, true, "UTF-8");
        writer.println("£");
        writer.println("札幌");
    }
}

```

## Python Code
### python_code_1.txt
```python
print u'\u00a3'

```

### python_code_2.txt
```python
£ = '£'
print(£)

```

