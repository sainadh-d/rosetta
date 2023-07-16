# Program name

## Task Link
[Rosetta Code - Program name](https://rosettacode.org/wiki/Program_name)

## Java Code
### java_code_1.txt
```java
public class ScriptName {
	public static void main(String[] args) {
		String program = System.getProperty("sun.java.command").split(" ")[0];
		System.out.println("Program: " + program);
	}
}

```

### java_code_2.txt
```java
public class ScriptName {
	public static void main(String[] args) {
		Class c = new Object(){}.getClass().getEnclosingClass();
		System.out.println("Program: " + c.getName());
	}
}

```

### java_code_3.txt
```java
public class ScriptName {
	public static void main(String[] args) {
		Class c = System.getSecurityManager().getClassContext()[0];
		System.out.println("Program: " + c.getName());
	}
}

```

### java_code_4.txt
```java
public class ScriptName {
	public static void main(String[] args) {
		String program = Thread.currentThread().getStackTrace()[1].getClassName();
		System.out.println("Program: " + program);
	}
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python

import sys

def main():
    program = sys.argv[0]
    print("Program: %s" % program)

if __name__ == "__main__":
    main()

```

### python_code_2.txt
```python
#!/usr/bin/env python

import inspect

def main():
    program = inspect.getfile(inspect.currentframe())
    print("Program: %s" % program)

if __name__ == "__main__":
    main()

```

