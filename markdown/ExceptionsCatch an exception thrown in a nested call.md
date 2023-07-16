# Exceptions/Catch an exception thrown in a nested call

## Task Link
[Rosetta Code - Exceptions/Catch an exception thrown in a nested call](https://rosettacode.org/wiki/Exceptions/Catch_an_exception_thrown_in_a_nested_call)

## Java Code
### java_code_1.txt
```java
class U0 extends Exception { }
class U1 extends Exception { }

public class ExceptionsTest {
    public static void foo() throws U1 {
        for (int i = 0; i <= 1; i++) {
            try {
                bar(i);
            } catch (U0 e) {
                System.out.println("Function foo caught exception U0");
            }
        }
    }

    public static void bar(int i) throws U0, U1 {
        baz(i); // Nest those calls
    }

    public static void baz(int i) throws U0, U1 {
        if (i == 0)
            throw new U0();
        else
            throw new U1();
    }

    public static void main(String[] args) throws U1 {
        foo();
    }
}

```

## Python Code
### python_code_1.txt
```python
class U0(Exception): pass
class U1(Exception): pass

def foo():
    for i in range(2):
        try:
            bar(i)
        except U0:
            print("Function foo caught exception U0")

def bar(i):
    baz(i) # Nest those calls

def baz(i):
    raise U1 if i else U0

foo()

```

