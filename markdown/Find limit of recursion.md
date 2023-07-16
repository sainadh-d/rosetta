# Find limit of recursion

## Task Link
[Rosetta Code - Find limit of recursion](https://rosettacode.org/wiki/Find_limit_of_recursion)

## Java Code
### java_code_1.txt
```java
public class RecursionTest {
	
    private static void recurse(int i) {
        try {
	    recurse(i+1);
	} catch (StackOverflowError e) {
	    System.out.print("Recursion depth on this system is " + i + ".");
	}
    }
	
    public static void main(String[] args) {
        recurse(0);
    }
}

```

## Python Code
### python_code_1.txt
```python
import sys
print(sys.getrecursionlimit())

```

### python_code_2.txt
```python
import sys
sys.setrecursionlimit(12345)

```

### python_code_3.txt
```python
def recurse(counter):
  print(counter)
  counter += 1
  recurse(counter)

```

### python_code_4.txt
```python
File "<stdin>", line 2, in recurse
RecursionError: maximum recursion depth exceeded while calling a Python object
996

```

### python_code_5.txt
```python
def recurseDeeper(counter):
    try:
        print(counter)
        recurseDeeper(counter + 1)
    except RecursionError:
        print("RecursionError at depth", counter)
        recurseDeeper(counter + 1)

```

### python_code_6.txt
```python
1045
Fatal Python error: Cannot recover from stack overflow.

```

