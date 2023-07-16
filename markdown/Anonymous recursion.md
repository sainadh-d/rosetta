# Anonymous recursion

## Task Link
[Rosetta Code - Anonymous recursion](https://rosettacode.org/wiki/Anonymous_recursion)

## Java Code
### java_code_1.txt
```java
public static long fib(int n) {
    if (n < 0)
        throw new IllegalArgumentException("n can not be a negative number");

    return new Object() {
        private long fibInner(int n) {
            return (n < 2) ? n : (fibInner(n - 1) + fibInner(n - 2));
        }
    }.fibInner(n);
}

```

### java_code_2.txt
```java
import java.util.function.Function;

@FunctionalInterface
interface SelfApplicable<OUTPUT> {
    OUTPUT apply(SelfApplicable<OUTPUT> input);
}

class Utils {
    public static <INPUT, OUTPUT> SelfApplicable<Function<Function<Function<INPUT, OUTPUT>, Function<INPUT, OUTPUT>>, Function<INPUT, OUTPUT>>> y() {
        return y -> f -> x -> f.apply(y.apply(y).apply(f)).apply(x);
    }

    public static <INPUT, OUTPUT> Function<Function<Function<INPUT, OUTPUT>, Function<INPUT, OUTPUT>>, Function<INPUT, OUTPUT>> fix() {
        return Utils.<INPUT, OUTPUT>y().apply(Utils.<INPUT, OUTPUT>y());
    }

    public static long fib(int m) {
        if (m < 0)
            throw new IllegalArgumentException("n can not be a negative number");

        return Utils.<Integer, Long>fix().apply(
                f -> n -> (n < 2) ? n : (f.apply(n - 1) + f.apply(n - 2))
        ).apply(m);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
>>> fib = lambda f: lambda n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2)))
>>> [ Y(fib)(i) for i in range(-2, 10) ]
[None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### python_code_2.txt
```python
>>>from functools import partial
>>> Y = lambda f: (lambda x: x(x))(lambda y: partial(f, lambda *args: y(y)(*args)))
>>> fib = lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2)))
>>> [ Y(fib)(i) for i in range(-2, 10) ]
[None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### python_code_3.txt
```python
>>> from functools import partial
>>> Y = lambda f: partial(f, f)
>>> fib = lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f, n-1) + f(f, n-2)))
>>> [ Y(fib)(i) for i in range(-2, 10) ]
[None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### python_code_4.txt
```python
>>> from inspect import currentframe
>>> from types import FunctionType
>>> def myself (*args, **kw):
...    caller_frame = currentframe(1)
...    code = caller_frame.f_code
...    return FunctionType(code, caller_frame.f_globals)(*args, **kw)
...
>>> print "factorial(5) =",
>>> print (lambda n:1 if n<=1 else n*myself(n-1)) ( 5 )

```

### python_code_5.txt
```python
>>> Y = lambda f: lambda n: f(f,n)
>>> fib = lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f,n-1) + f(f,n-2))) #same as the first three implementations
>>> [ Y(fib)(i) for i in range(-2, 10) ]
[None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### python_code_6.txt
```python
>>> fib_func = (lambda f: lambda n: f(f,n))(lambda f, n: None if n < 0 else (0 if n == 0 else (1 if n == 1 else f(f,n-1) + f(f,n-2))))
>>> [ fib_func(i) for i in range(-2, 10) ]
[None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

