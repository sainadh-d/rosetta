# Conditional structures

## Task Link
[Rosetta Code - Conditional structures](https://rosettacode.org/wiki/Conditional_structures)

## Java Code
### java_code_1.txt
```java
if (s == 'Hello World') {
    foo();
} else if (s == 'Bye World') {
    bar();
} else {
    deusEx();
}

```

### java_code_10.txt
```java
s.equals("Hello World") ? foo() : bar();

```

### java_code_11.txt
```java
Object newValue = s.equals("Hello World") ? a : b;

```

### java_code_12.txt
```java
switch (c) {
    case 'a':
        foo();
        break;
    case 'b':
        bar();
    default:
        foobar();
}

```

### java_code_13.txt
```java
if (c == 'a') {
   foo();
} else if (c == 'b') {
   bar();
   foobar();
} else {
   foobar();
}

```

### java_code_2.txt
```java
if(obj != null && obj.foo()){
   aMethod();
}

```

### java_code_3.txt
```java
if(obj != null & obj.foo()){
   aMethod();
}

```

### java_code_4.txt
```java
s == 'Hello World' ? foo() : bar();

```

### java_code_5.txt
```java
a = 3
if( a == 1 ){
    io.writeln( 'a == 1' )
}else if( a== 3 ){
    io.writeln( 'a == 3' )
}else{
    io.writeln( 'a is neither 1 nor 3' )
}

```

### java_code_6.txt
```java
a = 3
switch( a ){
case 0: io.writeln( 'case 0' )
case 1, 2: io.writeln( 'case 1,2' )
case 3, 4, 5: io.writeln( 'case 3,4,5' )
default: io.writeln( 'default' )
}

```

### java_code_7.txt
```java
if (s.equals("Hello World")) {
    foo();
} else if (s.equals("Bye World"))
    bar(); // braces optional for one-liners
else {
    deusEx();
}

```

### java_code_8.txt
```java
if (obj != null && obj.foo()) {
   aMethod();
}

```

### java_code_9.txt
```java
if (obj != null & obj.foo()) {
   aMethod();
}

```

## Python Code
### python_code_1.txt
```python
if x == 0:
    foo()
elif x == 1:
    bar()
elif x == 2:
    baz()
else:
    qux()

match x:
    0 => foo()
    1 => bar()
    2 => baz()
    _ => qux()

(a) ? b : c

```

### python_code_2.txt
```python
if x == 0:
    foo()
elif x == 1:
    bar()
elif x == 2:
    baz()
else:
    boz()

```

### python_code_3.txt
```python
true_value if condition else false_value

```

### python_code_4.txt
```python
>>> secret='foo'
>>> print 'got it' if secret=='foo' else 'try again'
'got it'

```

### python_code_5.txt
```python
>>> secret = 'foo'
>>> result = 'got it' if secret=='foo' else 'try again'
>>> print result
'got it'

```

### python_code_6.txt
```python
dispatcher = dict()
dispatcher[0]=foo  # Not foo(): we bind the dictionary entry to the function's object,
                   # NOT to the results returned by an invocation of the function
dispatcher[1]=bar
dispatcher[2]=baz  # foo,bar, baz, and boz are defined functions.

# Then later
results = dispatcher.get(x, boz)()  # binding results to a name is optional
# or with no "default" case:
if x in dispatcher:
    results=dispatcher[x]()

```

### python_code_7.txt
```python
# The above, but with a dict literal
dispatcher = {
    0: foo,
    1: bar,
    2: baz,
}
# ...
results = dispatcher.get(x, boz)()

```

### python_code_8.txt
```python
# Or without the temp variable
# (it's up to the reader to decide how "pythonic" this is or isn't)
results = {
    0: foo,
    1: bar,
    2: baz,
}.get(x, boz)()

```

