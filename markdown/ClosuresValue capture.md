# Closures/Value capture

## Task Link
[Rosetta Code - Closures/Value capture](https://rosettacode.org/wiki/Closures/Value_capture)

## Java Code
### java_code_1.txt
```java
import java.util.function.Supplier;
import java.util.ArrayList;

public class ValueCapture {
    public static void main(String[] args) {
	ArrayList<Supplier<Integer>> funcs = new ArrayList<>();
	for (int i = 0; i < 10; i++) {
	    int j = i;
	    funcs.add(() -> j * j);
	}

	Supplier<Integer> foo = funcs.get(3);
	System.out.println(foo.get()); // prints "9"
    }
}

```

### java_code_2.txt
```java
import java.util.List;
import java.util.function.IntSupplier;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;

public interface ValueCapture {
  public static void main(String... arguments) {
    List<IntSupplier> closures = IntStream.rangeClosed(0, 10)
      .<IntSupplier>mapToObj(i -> () -> i * i)
      .collect(toList())
    ;

    IntSupplier closure = closures.get(3);
    System.out.println(closure.getAsInt()); // prints "9"
  }
}

```

## Python Code
### python_code_1.txt
```python
funcs = []
for i in range(10):
    funcs.append(lambda: i * i)
print funcs[3]() # prints 81

```

### python_code_2.txt
```python
funcs = []
for i in range(10):
    funcs.append(lambda i=i: i * i)
print funcs[3]() # prints 9

```

### python_code_3.txt
```python
funcs = [lambda i=i: i * i for i in range(10)]
print funcs[3]() # prints 9

```

### python_code_4.txt
```python
funcs = []
for i in range(10):
    funcs.append((lambda i: lambda: i * i)(i))
print funcs[3]() # prints 9

```

### python_code_5.txt
```python
funcs = [(lambda i: lambda: i)(i * i) for i in range(10)]
print funcs[3]() # prints 9

```

### python_code_6.txt
```python
funcs = map(lambda i: lambda: i * i, range(10))
print funcs[3]() # prints 9

```

### python_code_7.txt
```python
funcs=[eval("lambda:%s"%i**2)for i in range(10)]
print funcs[3]() # prints 9

```

