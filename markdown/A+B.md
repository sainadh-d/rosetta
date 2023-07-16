# A+B

## Task Link
[Rosetta Code - A+B](https://rosettacode.org/wiki/A%2BB)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args) {
    int A = Integer.parseInt(args[0]);
    int B = Integer.parseInt(args[1]);
    System.out.println(A + B);
}

```

### java_code_2.txt
```java
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int A = scanner.nextInt();
    int B = scanner.nextInt();
    System.out.println(A + B);
}

```

### java_code_3.txt
```java
import static java.nio.charset.StandardCharsets.UTF_8;
import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

```

### java_code_4.txt
```java
int sum(InputStream input) throws IOException {
    BufferedReader reader = new BufferedReader(new InputStreamReader(input));
    String line = reader.readLine();
    reader.close();
    /* split parameter here is a regex */
    String[] values = line.split(" +");
    int A = Integer.parseInt(values[0]);
    int B = Integer.parseInt(values[1]);
    return A + B;
}

```

### java_code_5.txt
```java
import java.util.Scanner;

public class Sum2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); // Standard input
        System.out.println(in.nextInt() + in.nextInt()); // Standard output
    }
}

```

### java_code_6.txt
```java
import java.io.*;
import java.util.*;

public class SumDif {
   StreamTokenizer in;
   PrintWriter out;

   public static void main(String[] args) throws IOException {
      new SumDif().run();
   }

   private int nextInt() throws IOException {
      in.nextToken();
      return (int)in.nval;
   }

   public void run() throws IOException {
      in = new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in))); // Standard input
      out = new PrintWriter(new OutputStreamWriter(System.out)); // Standard output
      solve();
      out.flush();
   }

   private void solve() throws IOException {
      out.println(nextInt() + nextInt());
   }
}

```

### java_code_7.txt
```java
import java.io.*;
import java.nio.charset.Charset;

public class AplusB {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(new InputStreamReader(System.in, Charset.defaultCharset()));
        in.nextToken();
        int a = (int) in.nval;
        in.nextToken();
        int b = (int) in.nval;

        try (Writer out = new OutputStreamWriter(System.out, Charset.defaultCharset())) {
            out.write(Integer.toString(a + b));
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
try: raw_input
except: raw_input = input

print(sum(map(int, raw_input().split())))

```

### python_code_2.txt
```python
import sys

for line in sys.stdin:
    print(sum(map(int, line.split())))

```

### python_code_3.txt
```python
a = int(input("First number: "))
b = int(input("Second number: "))
print("Result:", a+b)

```

